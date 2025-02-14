# Import library yang dibutuhkan
from flask import Flask, render_template, request
from model import predict_result, preprocess_img

# Mendeclare kamus
kamus = {0: "Sneakers", 1: "Flat Shoes", 2: "Slip On",
         3: "Running Shoes", 4: "Sepatu Sandal", 5: "Kitten Heels"}


# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])  # type: ignore
def predict_image_file():
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=[kamus[_] for _ in pred])
    except:
        error = "File tidak dapat diproses."
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
