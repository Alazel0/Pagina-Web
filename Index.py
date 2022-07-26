from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')

def home():
    return render_template('Home.html')

@app.route('/NeoCab')

def NeoCab():
    return render_template('Neo Cab.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))
