from flask import Flask, render_template
from io import BytesIO
from temperature_CO2_plotter import plot_temperature, plot_CO2
import base64


app = Flask(__name__)

@app.route('/')
def root():
	temp_file = BytesIO()
	co2_file = BytesIO()
	plot_temperature(fig_file=temp_file)
	plot_CO2(fig_file=co2_file)
	temp_file.seek(0)
	co2_file.seek(0)
	temp_figdata_png = base64.b64encode(temp_file.getvalue()).decode()
	co2_figdata_png = base64.b64encode(co2_file.getvalue()).decode()
	return render_template('plots.html', co2_plot=co2_figdata_png, temp_plot=temp_figdata_png)


if __name__ == "__main__":
	app.run()