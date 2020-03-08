from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lmaoabcdefg'

from app import routes