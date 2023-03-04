from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():

    user ={'username':'Miguel'}
    posts= [
    
        {
            'author':{'username':'john'},
            'body':'beautiful day in Mexico'
        },
        {
            'author':{'username':'susan'},
            'body':'pinochio movie was great'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)