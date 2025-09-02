from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

# Home / Portfolio Page
@app.route("/")
def home():
    if "user" in session:
        return render_template("portfolio.html", user=session["user"])
    return redirect(url_for("login"))

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Hardcoded credentials (can be replaced with database later)
        if username == "gursimar" and password == "1234":
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return "Invalid Credentials, Try Again!"

    return render_template("login.html")

# Logout Route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
