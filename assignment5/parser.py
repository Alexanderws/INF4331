#parser.py

import re

def parse_nwodkram(text):
	"""
	Convert text written in Nwodkram to corresponding HTML text.

	Example usage:
		>>> text = 	'This is %bold%.'
		>>> print(parse_nwodkram(text))
		This is <b>bold</b>.
		>>> text = 	'And this is *italic*.'
		>>> print(parse_nwodkram(text))
		And this is <i>italic</i>.
		>>> text = 	'While [this is a url](www.google.com).'
		>>> print(parse_nwodkram(text))
		While <a href="http://www.google.com">this is a url</a>.
	"""

	reg_bold = r"\%(\w+)\%"
	reg_bold_sub = r"<b>\1</b>"
	reg_italic = r"\*(\w+)\*"
	reg_italic_sub = r"<i>\1</i>"
	reg_url = r"\[([^\]]+)\]\((?:http://|https://)?([^)]+)\)"
	reg_img = r"<([^>]+)>\(w=(\d+),[ ]?h=(\d+)\)"
	reg_img_sub = r'<img src="\1" style="width:\2px;height:\3px;">'
	reg_quote = r'>>(.*)'
	reg_quote_sub = r"<blockquote>\1</blockquote>"
	reg_wiki = r"\[wp:\s?(.*)\]"
	reg_wiki_sub = r'<a href="https://en.wikipedia.org/w/index.php?title=Special:Search&search=\1">Search Wikipedia for \1</a>'
	converted_text = re.sub(reg_bold, reg_bold_sub, text)
	converted_text = re.sub(reg_italic, reg_italic_sub, converted_text)
	converted_text = re.sub(reg_img, reg_img_sub, converted_text)
	converted_text = re.sub(reg_quote, reg_quote_sub, converted_text)
	converted_text = re.sub(reg_wiki, reg_wiki_sub, converted_text)
	converted_text = re.sub("\\\\", "", converted_text);


	#fixed url handling https
	p = re.compile("(?<![\\\\])[\[](.*)(?<![\\\\])[\]](?<![\\\\])[\(](.*)(?<![\\\\])[\)]");
	links = p.findall(converted_text);
	for link in links:
		cur_link = link[1];
		cur_link_name = link[0];
		if cur_link.find("http") == -1:
			new_link = "http://" + cur_link;
		else:
			new_link = cur_link;
			cur_link = re.escape(cur_link);
			converted_text = re.sub("\["+cur_link_name+"\]\("+cur_link+"\)", "<a href=\'"+new_link+"\'>"+cur_link_name+"</a>", converted_text);

	return converted_text


if __name__ == "__main__":
	import doctest
	doctest.testmod()
