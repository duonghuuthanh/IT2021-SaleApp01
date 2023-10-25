def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "iPhone 13",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 2,
        "name": "Galaxy S23",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "iPhone 13",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "iPhone 13",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }, {
        "id": 1,
        "name": "iPhone 13",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
