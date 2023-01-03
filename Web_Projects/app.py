from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('rectangle.html')

@app.route("/", methods=['POST','GET'])
def size():
    if request.method == "POST":
        user = request.form.getlist('corner[]')
        print(user)
        print(len(user))
        return redirect(url_for('main'))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')