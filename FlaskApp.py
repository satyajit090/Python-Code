# from flask import Flask, render_template,request
# app = Flask(__name__)

# @app.route('/loggg', methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['name']
#         return f"Hello , {name}!"
#     return render_template('form.html')

# if __name__=='__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form' , methods=['GET' , 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)