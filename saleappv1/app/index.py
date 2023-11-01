from flask import render_template, request
import dao
from app import app


@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    products = dao.load_products(kw)

    return render_template('index.html', categories=cates, products=products)


if __name__ == '__main__':
    app.run(debug=True)
