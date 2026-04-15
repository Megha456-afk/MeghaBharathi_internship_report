from flask import Flask, render_template, request, redirect, session
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret123"   # required for login session

FILE = "output/ML_PREDICTIONS.xlsx"

# -------------------------
# LOGIN PAGE
# -------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # simple login check
        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Login ❌"

    return render_template("login.html")


# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():

    # protect route
    if "user" not in session:
        return redirect("/")

    pred = pd.read_excel(FILE, sheet_name="Referral_Predictions")
    seg  = pd.read_excel(FILE, sheet_name="Doctor_Segments")
    anom = pd.read_excel(FILE, sheet_name="Anomaly_Flags")

    return render_template("dashboard.html",
                           pred=pred.to_dict(orient="records"),
                           seg=seg.to_dict(orient="records"),
                           anom=anom.to_dict(orient="records"))


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)