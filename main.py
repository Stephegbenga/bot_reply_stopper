from flask import Flask, request
from models import Users
app = Flask(__name__)


@app.get("/")
def home():
    return {"status":"success", "message":"online"}


@app.get("/user/<id>")
def get_user(id):
    user = Users.find_one({"id": id})
    if user:
        return {"status":"paused"}
    return {"status":"not_paused"}



@app.post("/webhook")
def webhook():
    try:
        req = request.json
        sender = req['from']['sender']
        if sender == "admin":
            contact_id = req['contact_id']
            Users.update_one({"id": contact_id}, {"$set": {"status": True}}, upsert=True)

    except Exception as e:
        pass
    return {"status":"success", "message":"a new message came in"}


if __name__ == '__main__':
    app.run()
