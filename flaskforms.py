from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def show_index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # is_checked = False
        
        # if request.form.get("confirm"):
        #     is_checked = True
        
        # return str(is_checked)
        
        # Also written as:
        return str("confirm" in request.form)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)