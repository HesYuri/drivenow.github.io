from flask import Flask, render_template

app = Flask(__name__)

WIKI = "https://commons.wikimedia.org/wiki/Special:FilePath/"

CARS = [
    {
        "name": "Toyota Camry",
        "class": "Бизнес",
        "price": 4500,
        "seats": 5,
        "gearbox": "Автомат",
        "image": WIKI + "2018_Toyota_Camry_(ASV70R)_Ascent_sedan_(2018-08-27)_01.jpg",
    },
    {
        "name": "Kia Rio",
        "class": "Эконом",
        "price": 2200,
        "seats": 5,
        "gearbox": "Автомат",
        "image": WIKI + "Berline_Kia_Rio_2018_au_SIAM_2018.jpg",
    },
    {
        "name": "Hyundai Solaris",
        "class": "Эконом",
        "price": 2000,
        "seats": 5,
        "gearbox": "Механика",
        "image": WIKI + "Hyundai_Solaris_(HC).jpg",
    },
    {
        "name": "BMW 5 Series",
        "class": "Премиум",
        "price": 8900,
        "seats": 5,
        "gearbox": "Автомат",
        "image": WIKI + "2017_BMW_520d_M_Sport_Automatic_2.0.jpg",
    },
    {
        "name": "Volkswagen Tiguan",
        "class": "Кроссовер",
        "price": 5200,
        "seats": 5,
        "gearbox": "Автомат",
        "image": WIKI + "Volkswagen_Tiguan_III_eHybrid_Auto_Zuerich_2023_1X7A1109.jpg",
    },
    {
        "name": "Mercedes-Benz V-Class",
        "class": "Минивэн",
        "price": 9500,
        "seats": 8,
        "gearbox": "Автомат",
        "image": WIKI + "Mercedes_Benz_V-Klasse_(13666332274).jpg",
    },
]

REVIEWS = [
    {"author": "Анна К.", "rating": 5, "date": "12.09.2026",
     "text": "Брала Kia Rio на выходные. Машина чистая, бак полный, оформление заняло 10 минут. Обязательно обращусь снова!"},
    {"author": "Дмитрий С.", "rating": 5, "date": "28.08.2026",
     "text": "Арендовал BMW 5 на свадьбу друга. Автомобиль в идеальном состоянии, менеджер подогнал его прямо к дому. Сервис на высоте."},
    {"author": "Елена и Игорь", "rating": 5, "date": "15.08.2026",
     "text": "Ездили всей семьёй на Mercedes V-Class в Карелию. Просторно, удобно, детские кресла дали бесплатно. Спасибо!"},
    {"author": "Максим Р.", "rating": 5, "date": "03.07.2026",
     "text": "Цены честные, никаких скрытых платежей. Залог вернули сразу после сдачи машины. Рекомендую."},
    {"author": "Ольга В.", "rating": 5, "date": "21.06.2026",
     "text": "Первый раз брала авто в аренду, очень переживала. Сотрудники всё подробно объяснили и были на связи 24/7. Всё прошло отлично!"},
]


@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.route("/fleet")
def fleet():
    return render_template("fleet.html", cars=CARS, active="fleet")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html", reviews=REVIEWS, active="reviews")


@app.route("/rules")
def rules():
    return render_template("rules.html", active="rules")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", active="contacts")

if __name__ == "__main__":
    app.run(debug=True)