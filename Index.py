from flask import Flask, render_template
import os

app= Flask(__name__)

port = int(os.environ.get('PORT', 33507))  # add these lines in code

@app.route('/')

def home():
    return render_template('Home.html')

@app.route('/NeoCab')

def NeoCab():
    return render_template('Neo Cab.html')

if __name__=='__main__':
    app.run(host=args.host, port=port, debug=True)
    
    else
        app.run(host=args.host, port=port, debug=True)
