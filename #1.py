from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def name():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link href="style.css">
</head>
<body>

<h1>Миссия Колонизация Марса</h1>

</body>
</html>"""


@app.route('/index/')
def dawiz():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link href="style.css">
</head>
<body>

<h1>И на Марсе будут яблони цвести!</h1>

</body>
</html>"""


@app.route('/image_mars/')
def mars():
    return render_template('index.html', filename=url_for('static', filename='img/1.jpeg'))


@app.route('/promotion_image/')
def recl_2():
    print(url_for('static', filename='css/style.css'))
    return render_template('2.html', filename=url_for('static', filename='img/1.jpeg'),
                           style=url_for('static', filename='css/style.css'))


@app.route('/promotion/')
def recl():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link href="style.css">
</head>
<body>

<h1>Человечество вырастает из детства.</h1>
<h2>Человечеству мала одна планета.</h2>
<h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
<h4>И начнем с Марса!</h4>
<h5>Присоединяйся!</h5>

</body>
</html>"""


@app.route('/astronaut_selection/')
def ancete():
    return render_template('anceta.html', style=url_for('static', filename='css/style.css'))


@app.route('/choice/<planet_name>/')
def choise(**kwargs):
    return render_template('choise.html', style=url_for('static', filename='css/style.css'),
                           planet=kwargs['planet_name'])


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(**kwargs):
    return render_template('result.html', style=url_for('static', filename='css/style.css'), **kwargs)


@app.route('/load_photo/', methods=['POST', 'GET'])
def image():
    if request.method == 'GET':
        return render_template('image.html', filename=url_for('static', filename='img/2.png'),
                               style=url_for('static', filename='css/style.css'))
    elif request.method == 'POST':
        f = request.files['file']
        with open(url_for('static', filename='img/2.png')[1:], 'wb') as fr:
            fr.write(f.read())
        return render_template('image.html', filename=url_for('static', filename='img/2.png'),
                               style=url_for('static', filename='css/style.css'))


@app.route('/images/')
def images():
    return render_template('images.html', filename1=url_for('static', filename='img/1.jpg'), filename2=url_for('static', filename='img/2.jpg'), filename3=url_for('static', filename='img/3.jpg'))


if __name__ == '__main__':
    print('http://127.0.0.1:8085/images/')
    app.run(port=8085, host='127.0.0.1')
