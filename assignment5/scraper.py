#scraper.py

import re
import requests

def find_emails(text):
	"""
	Return all e-mails found in the HTML text.

	Example usage:
		>>> text = '''<div class="name center">
		... <p style="margin-bottom: 0">CPO &amp; VP Finance</p>
		... <h3 style="margin: 0">Stig Zerener Haugnæss</h3>
		... <p>stig@lucidtech.ai</p>
		... </div>'''
		>>> print(find_emails(text))
		['stig@lucidtech.ai']
	"""

	#Changed method so it dosnt accept numbers in start and end of domian.
	any_pattern = "[\.\#\$\%\&\~\’\*\+\-\/\=\?\_\‘\|\{\}a-zA-Z0-9]*";
	domain = "[a-zA-Z][a-zA-Z.]*[a-zA-Z]";
	email_pattern = re.compile(any_pattern+"\@"+any_pattern+"\.+"+domain);
	emails = email_pattern.findall(text)
	return emails



def find_hyperlinks(text):
	"""
	Return all urls found in the HTML text.

	Example usage:
		>>> text = 	'''<div>
		... <a href="https://demo.lucidtech.ai/" class="btn hidden-xs"><span>Request Demo</span></a>
		... <div id="menu-icon"><span></span></div>'''
		>>> print(find_urls(text))
		['https://demo.lucidtech.ai/']
	"""

	#fixed missmatch between " and ' around the link
	url_pattern = r"<a href=([\'\"])((?:http://|https://)?[\w_\-\.~/]+)([\'\"])"
	urls = re.findall(url_pattern, text, flags=re.MULTILINE)

	url_res = [];
	for match in urls:
		if match[0] == match[2]:
			url_res.append(match[1]);
	return url_res


def all_the_emails(url, depth):
	"""
	Return all emails found in the url and subdirectories specified by depth parameter.
	"""
	try:
		resp = requests.get(url)
	except:
		print("Failed at "+url)
		return []

	html = resp.text
	emails = find_emails(html)
	urls = find_urls(html)

	if depth>0:
		for u in urls:
			if re.match(r"^(:?https://|http://)", u):
				emails += all_the_emails(u, depth-1)
			else:
				if re.match(r".*\/$", url):
					new_url = url + u
					emails += all_the_emails(new_url, depth-1)
				else:
					new_url = url + "/" + u
					emails += all_the_emails(new_url, depth-1)
	return emails


if __name__ == "__main__":
	import doctest
	doctest.testmod()

	[print(email) for email in set(all_the_emails("https://lucidtech.io/",2))]

