from flask import render_template, request
from unit_converter import app
from unit_converter.length import convert_length
from unit_converter.mass import convert_mass
from unit_converter.pressure import convert_pressure
from unit_converter.area import convert_area
from unit_converter.data_storage import convert_data_storage
from unit_converter.energy import Convert_energy
from unit_converter.speed import Convert_speed
from unit_converter.temperature import Convert_temperature
from unit_converter.timec import Convert_time
from unit_converter.volume import Convert_volume

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
@app.route("/Home")
def Home_page():
    return render_template('index.html')

@app.route("/About-page")
def About_page():
    return render_template('about.html')

@app.route("/Area-page", methods=['GET', 'POST'])
def Area_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = convert_area(int(from_unit), int(to_unit), from_value)
        return render_template('area.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('area.html')

@app.route("/Data-Storage-page", methods=['GET', 'POST'])
def Data_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = convert_data_storage(int(from_unit), int(to_unit), from_value)
        return render_template('data_storage.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('data_storage.html')

@app.route("/Energy-page", methods=['GET', 'POST'])
def Energy_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = Convert_energy(int(from_unit), int(to_unit), from_value)
        return render_template('energy.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('energy.html')

@app.route("/Length-page", methods=['GET', 'POST'])
def Length_page():
    if request.method == "POST":
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        from_value = float(request.form["from_value"])
        desc_result, short_result = convert_length(from_unit, to_unit, from_value)
        return render_template('length.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('length.html')

@app.route("/Mass-page", methods=['GET', 'POST'])
def Mass_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = convert_mass(int(from_unit), int(to_unit), from_value)
        return render_template('mass.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('mass.html')

@app.route("/Pressure-page", methods=['GET', 'POST'])
def Pressure_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = convert_pressure(int(from_unit), int(to_unit), from_value)
        return render_template('pressure.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('pressure.html')

@app.route("/Speed-page", methods=['GET', 'POST'])
def Speed_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = Convert_speed(int(from_unit), int(to_unit), from_value)
        return render_template('speed.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('speed.html')

@app.route("/Temperature-page", methods=['GET', 'POST'])
def Temperature_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = Convert_temperature(int(from_unit), int(to_unit), from_value)
        return render_template('temperature.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('temperature.html')

@app.route("/Time-page", methods=['GET', 'POST'])
def Time_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = Convert_time(int(from_unit), int(to_unit), from_value)
        return render_template('time.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('time.html')

@app.route("/Volume-page", methods=['GET', 'POST'])
def Volume_page():
    if request.method == "POST":
        from_unit = (request.form["from_unit"])
        to_unit = (request.form["to_unit"])
        from_value = float(request.form["from_value"])
        desc_result, short_result = Convert_volume(int(from_unit), int(to_unit), from_value)
        return render_template('volume.html', desc_result=desc_result, short_result=short_result, from_unit=from_unit, to_unit=to_unit)
    return render_template('volume.html')
