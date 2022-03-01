# %%
import joblib
from flask import request, render_template
from flask import Flask

# %%
app = Flask(__name__)  # run this code

# %%
# decorator, run this function first before running the subsequent function


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_REG")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI using Regression is : " + str(pred1)
        model2 = joblib.load("STI_REG")
        pred2 = model2.predict([[Nikkei]])
        str2 = "The prediction for STI using Regression is : " + str(pred2)
        model3 = joblib.load("STI_REG")
        pred3 = model3.predict([[Nikkei]])
        str3 = "The prediction for STI using Regression is : " + str(pred3)
        model4 = joblib.load("STI_REG")
        pred4 = model4.predict([[Nikkei]])
        str4 = "The prediction for STI using Regression is : " + str(pred4)
        model5 = joblib.load("STI_REG")
        pred5 = model5.predict([[Nikkei]])
        str5 = "The prediction for STI using Regression is : " + str(pred5)
        return(render_template("index.html", result1=str1, result2=str2, result3=str3, result4=str4, result5=str5))
    else:
        return(render_template("index.html", result1="2"))


# %%
if __name__ == "__main__":  # to ensure that it is this program running in the cloud
    app.run(host="127.0.0.1", port=int("80"))

# %%
