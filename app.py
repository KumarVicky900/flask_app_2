from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def default():
    return "<h1>search /home to do blogging<h1>"


@app.route('/home', methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)