from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://chinmayjavalagi:Chinnuser1234@cluster0.sltpagz.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
CORS(app)
db = mongo.db

@app.route("/", methods = ['GET', 'POST'])
def notes():
    if request.method == 'GET':
        notes_cursor = db.notes.find()
        notes = [{'title': note['title'], 'content': note['content'], '_id': str(note['_id'])} for note in notes_cursor]    
        return jsonify({'notes': notes})
    elif request.method == 'POST':
        new_note = request.json
        result = db.notes.insert_one(new_note)
        new_note['_id'] = str(result.inserted_id)
        return jsonify({'message': 'Note created successfully', 'note': new_note})

if __name__ == "__main__":
    app.run(debug=True)
