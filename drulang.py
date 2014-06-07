from flask import Flask,request,render_template,url_for

dlapp = Flask(__name__,static_folder="assets")

@dlapp.route("/")
def index():
    return render_template("index.html")

@dlapp.route("/freelance")
def freelance():
    return render_template("freelance.html")

@dlapp.route("/brew")
def brew():
    return render_template("brew.html")

@dlapp.route("/homelab")
def homelab():
    return render_template("homelab.html")

@dlapp.route("/lbt")
def lbt():
    return render_template("lbt.html")

if __name__ == "__main__":
    dlapp.run(host="0.0.0.0", port=5002)

