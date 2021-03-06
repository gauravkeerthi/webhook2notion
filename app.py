
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, name, email):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = name
    row.email = email


@app.route('/create_member', methods=['GET'])
def create_todo():


    name = request.args.get('name')
    email = request.args.get('email')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, name,email)
    return f'added {name} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
