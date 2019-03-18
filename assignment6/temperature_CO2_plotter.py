import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn



def plot_temperature(start_month=1, end_month=12, start_year=1818, end_year=2012, min_temp=None, max_temp=None, fig_file=None):
	"""
	Plot temperature of selected months across selected years.

    :param start_month: optional number of month to start plotting from
    :param end_month: optional number of month to end plotting to
    :param start_year: optional year to start plotting from
    :param end_year: optional year to stop plotting at
    :param min_temp: optional minimum temperature value
    :param max_temp: optional maximum temperature value
    """
	data = pd.read_csv('temperature.csv').set_index('Year')
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
	month_range = months[start_month-1:end_month]
	ax = data.loc[start_year:end_year][month_range].plot()
	ax.set_ylim([min_temp, max_temp])
	
	if fig_file:
		plt.savefig(fig_file, format='png')
	else:
		plt.show()



def plot_CO2(start_year=1818, end_year=2012, min_co2=None, max_co2=None, fig_file=None):
	"""
	Plot million metric tons carbon carbon dioxide emissions of selected years.

    :param start_year: optional year to start plotting from
    :param end_year: optional year to stop plotting at
    :param min_co2: optional minimum co2 value
    :param max_co2: optional maximum co2 value
    """
	data = pd.read_csv('co2.csv').set_index('Year')
	ax = data.loc[start_year:end_year].plot()
	ax.set_ylim([min_co2, max_co2])

	if fig_file:
		plt.savefig(fig_file, format='png')
	else:
		plt.show()


if __name__ == "__main__":
	plot_temperature(1,3,1818,1890)
	plot_CO2(1751,1780)

