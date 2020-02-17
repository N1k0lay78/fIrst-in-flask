from flask import Flask

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


app.add_url_rule('/', name)
app.add_url_rule('/index/', dawiz)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')