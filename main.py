from flask import Flask, render_template, request
import sqlite3
import json
import time
import functions as fn
import db as db


app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/btns')
def btns():
    return render_template("test.html")


@app.route('/refresh/', methods=['POST'])
def refresh():
    fn.vlag()
    return render_template("dashboard.html")


@app.route('/change/', methods=['GET', 'POST'])
def change():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        # Login = "blueberry"
        # Password = "Blueberry2024!"

        db.change_login_password(Login, Password)
        fn.vlag()
        return render_template('dashboard.html')

    return render_template("change.html")


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute(('''SELECT password FROM passwords
                                               WHERE login = '{}';
                                               ''').format(Login))
        pas = cursor_db.fetchall()

        # cursor_db.close()
        try:
            if pas[0][0] != Password:
                return render_template('auth_bad.html')
        except:
            return render_template('auth_bad.html')

        # db_lp.close()
        fn.vlag()
        return render_template('dashboard.html')

    return render_template("authorization.html")


# @app.route('/registration', methods=['GET', 'POST'])
# def form_registration():
#     if request.method == 'POST':
#         Login = request.form.get('Login')
#         Password = request.form.get('Password')
#         id = 0
#
#         db_lp = sqlite3.connect('login_password.db')
#         cursor_db = db_lp.cursor()
#         sql_insert = '''INSERT INTO passwords VALUES('{}', '{}','{}');'''.format(id, Login, Password)
#
#         cursor_db.execute(sql_insert)
#         db_lp.commit()
#
#         cursor_db.close()
#         db_lp.close()
#
#         return render_template('successfulregis.html')
#
#     return render_template('registration.html')


#{"hectare1": true, "hectare2": false, "hectare3": false}       СТРУКТУРА JSON
@app.route('/hectare1_open/', methods=['POST'])
def hectare1_open_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)
    with open('static/data.json', 'w') as f:
        if (obj["hectare1"] == True):
            f.write("")
            json.dump({'hectare1': True, 'hectare2': False, 'hectare3': False}, f)
        if (obj["hectare2"] == True):
            f.write("")
            json.dump({'hectare1': True, 'hectare2': False, 'hectare3': False}, f)
        if (obj["hectare3"] == True):
            f.write("")
            json.dump({'hectare1': True, 'hectare2': False, 'hectare3': False}, f)
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            f.write("")
            json.dump({'hectare1': True, 'hectare2': False, 'hectare3': False}, f)

    fn.hectare1_open()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/hectare1_close/', methods=['POST'])
def hectare1_close_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)

    global nasos
    with open('static/nasos.json') as f:
        nasos = json.load(f)

    with open('static/data.json', 'w') as f:
        if (obj["hectare1"] == True):
            f.write("")
            if (nasos["nasos"] == True):
                with open('static/nasos.json', "w") as a:
                    a.write("")
                    json.dump({"nasos": False}, a)
                    a.close()
                    fn.close_nasos()
                time.sleep(5)
                json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
                fn.hectare1_close()
            if (nasos["nasos"] == False):
                json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
                fn.hectare1_close()
        if (obj["hectare2"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': True, 'hectare3': False}, f)
            fn.hectare1_close()
        if (obj["hectare3"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': True}, f)
            fn.hectare1_close()
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
            fn.hectare1_close()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/hectare2_open/', methods=['POST'])
def hectare2_open_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)
    with open('static/data.json', 'w') as f:
        if (obj["hectare1"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': True, 'hectare3': False}, f)
        if (obj["hectare2"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': True, 'hectare3': False}, f)
        if (obj["hectare3"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': True, 'hectare3': False}, f)
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': True, 'hectare3': False}, f)

    fn.hectare2_open()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/hectare2_close/', methods=['POST'])
def hectare2_close_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)

    global nasos
    with open('static/nasos.json') as f:
        nasos = json.load(f)

    with open('static/data.json', 'w') as f:
        if (obj["hectare1"] == True):
            f.write("")
            json.dump({'hectare1': True, 'hectare2': False, 'hectare3': False}, f)
            fn.hectare2_close()
        if (obj["hectare2"] == True):
            f.write("")
            if (nasos["nasos"] == True):
                with open('static/nasos.json', "w") as a:
                    a.write("")
                    json.dump({"nasos": False}, a)
                    a.close()
                    fn.close_nasos()
                time.sleep(5)
                json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
                fn.hectare2_close()
            if (nasos["nasos"] == False):
                json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
                fn.hectare1_close()
        if (obj["hectare3"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': True}, f)
            fn.hectare1_close()
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
            fn.hectare1_close()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/hectare3_open/', methods=['POST'])
def hectare3_open_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)
    with open('static/data.json', 'w') as f:
        if (obj["hectare1"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': True}, f)
        if (obj["hectare2"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': True}, f)
        if (obj["hectare3"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': True}, f)
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': True}, f)

    fn.hectare3_open()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/hectare3_close/', methods=['POST'])
def hectare3_close_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)

    global nasos
    with open('static/nasos.json') as f:
        nasos = json.load(f)

    with open('static/data.json', 'w') as f:
        if (obj["hectare1"] == True):
            f.write("")
            json.dump({'hectare1': True, 'hectare2': False, 'hectare3': False}, f)
            fn.hectare3_close()
        if (obj["hectare2"] == True):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': True, 'hectare3': False}, f)
            fn.hectare3_close()
        if (obj["hectare3"] == True):
            f.write("")
            if (nasos["nasos"] == True):
                with open('static/nasos.json', "w") as a:
                    a.write("")
                    json.dump({"nasos": False}, a)
                    a.close()
                    fn.close_nasos()
                time.sleep(5)
                json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
                fn.hectare3_close()
            if (nasos["nasos"] == False):
                json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
                fn.hectare3_close()
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            f.write("")
            json.dump({'hectare1': False, 'hectare2': False, 'hectare3': False}, f)
            fn.hectare3_close()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/open_nasos/', methods=['POST'])
def open_nasos_json():
    global obj
    with open('static/data.json') as f:
        obj = json.load(f)

    with open('static/nasos.json', 'w') as f:
        if (obj["hectare1"] == False and obj["hectare2"] == False and obj["hectare3"] == False):
            json.dump({"nasos": False}, f)
            fn.close_nasos()
        else:
            json.dump({"nasos": True}, f)
            fn.open_nasos()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/close_nasos/', methods=['POST'])
def close_nasos_json():
    with open('static/nasos.json', 'w') as f:
        json.dump({"nasos": False}, f)

    fn.close_nasos()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/start_auto_poliv/', methods=['POST'])
def start_auto_poliv_json():
    with open('static/poliv.json', 'w') as f:
        json.dump({"poliv": True}, f)

    fn.start_auto_poliv()
    fn.vlag()
    return render_template('dashboard.html')


@app.route('/stop_auto_poliv/', methods=['POST'])
def stop_auto_poliv_json():
    with open('static/poliv.json', 'w') as f:
        json.dump({"poliv": False}, f)

    fn.stop_auto_poliv()
    fn.vlag()
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=4000)