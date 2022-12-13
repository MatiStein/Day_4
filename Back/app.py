from flask import (
    Flask,
    request,
    )
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy_imageattach.entity import Image, image_attachment


api = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Shop.sqlite3'
app.config['SECRET_KEY'] = "random string"
CORS(app)
db = SQLAlchemy(app)


class Shop(db.Model):
    Id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(400))
    price = db.Column(db.float(6))
    #img = db.image_attachment('prd_img')

    def __init__(self, name, description, price, img):
        self.name = name
        self.description = description
        self.price = price
        self.img = img


@app.route('/shop/', methods=["GET", 'POST', "DELETE", "PUT"])
def products():
    if request.method =="GET": 
        if id > -1: 
            products = Shop.query.get(id)    
            return({"name":Shop.name,"description":Shop.description,"price":Shop.price, "img": Shop.img})

        else:
            prd=[]
            for products in Shop.query.all():
                prd.append({"name":Shop.name,"description":Shop.description,"price":Shop.price, "id":Shop.id})
                return  (json.dumps(prd))
        
    
    if request.method =="POST": 
        request_data = request.get_json()
        name= request_data["name"]
        description = request_data['description']
        price= request_data["price"]
        img= request_data["img"]
    
        newPrd= Shop(name,description,price,img)
        db.session.add (newPrd)
        db.session.commit()
        return "a new record was create"

    if request.method =="DELETE":
        print(id)
        prd = Shop.query.get(id)
        if(prd):
            db.session.delete(prd)
            db.session.commit()
            return "delete"
        else:
            return "unknown id"

    if request.method =="PUT":
        prd = Shop.query.get(id)
        request_data = request.get_json()
        prd.name= request_data["name"]
        prd.description = request_data['description']
        prd.price= request_data["price"]
        prd.img= request_data["img"]
        db.session.commit()
        return "a row was update" 



if __name__ == '__main__':
    api.run(debug=True)
