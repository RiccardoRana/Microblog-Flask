import os
from flask import Flask,render_template,request
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
 app = Flask(__name__)
 client=MongoClient(os.getenv("MONGODB_URI"))
 app.db=client.MicroblogFlask
 # mongodb+srv://RickyFrog:Xxpxxp249werty@microblogflask.rsfuzwh.mongodb.net/
 entries = []

 @app.route("/", methods=["GET","POST"])
 def blog_page():
    print([e for e in app.db.entries.find({})])
    if request.method == "POST":
        entry_content = request.form.get("content") #The name of the textarea!
        formatted_date = datetime.today().strftime("%Y-%m-%d") #String-Format-Time!
        print(entry_content,formatted_date)
        entries.append((entry_content,formatted_date))
        app.db.entries.insert_one({"content": entry_content, "date":formatted_date})
    
    entries_with_date = [ 
        (
        entry["content"],
        entry["date"], 
        datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")) 
        for entry in app.db.entries.find({})
        ]

    return render_template("blog.html", entries=entries_with_date)

 return app
 
#  class GalileanMoons():
#       def __init__(self,one,two,three,four):
#           self.one=one
#           self.two=two
#           self.three=three
#           self.four=four

#  @app.route("/home/")
#  def home_page():
#     return render_template('home.html')

#  @app.route("/about/")
#  def who_am_i():
#     return render_template('about.html')

#  @app.route("/market/")
#  def market_page():
#     items = [
#         {
#             "id":1, "name": "Iphone14", "price":450
#         },
#         {
#             "id":2, "name": "Iphone13", "price":300
#         },
#         {
#             "id":3, "name": "Iphone12", "price":250
#         }
#     ]

#     color = "BLue"
#     animal = "Dog"
#     animal_name = "Jhonny"
#     kwargs = {
#         "color" : color,
#         "animal": animal,
#         "animal_name" : animal_name,
#         "to_show": True
#     }
#     moon_groups = GalileanMoons("Io", "Europa", "Gamede", "Callisto")
#     return render_template('market.html', items=items, **kwargs, moons_groups = moon_groups)

#  @app.route("/", methods=["GET","POST"])
#  def blog_page():
#     print([e for e in app.db.entries.find({})])
#     if request.method == "POST":
#         entry_content = request.form.get("content") #The name of the textarea!
#         formatted_date = datetime.today().strftime("%Y-%m-%d") #String-Format-Time!
#         print(entry_content,formatted_date)
#         entries.append((entry_content,formatted_date))
#         app.db.entries.insert_one({"content": entry_content, "date":formatted_date})
    
#     entries_with_date = [ 
#         (
#         entry["content"],
#         entry["date"], 
#         datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")) 
#         for entry in app.db.entries.find({})
#         ]

#     return render_template("blog.html", entries=entries_with_date)

#  return app
 


















































