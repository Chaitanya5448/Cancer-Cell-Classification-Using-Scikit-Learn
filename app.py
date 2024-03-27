from flask import Flask, render_template, request, redirect, flash
import Cancer_Cell_Classi  # Import your classification code

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

@app.route('/', methods=['GET', 'POST'])
def classify():
    data_file = None
    classification_result = None
    if request.method == 'POST':
        data_file = request.files['data_file']  # Access uploaded file
        if data_file:
            try:
                classification_result = Cancer_Cell_Classi.classify(data_file.read())
            except Exception as e:
                flash(f"Classification failed: {str(e)}", 'error')
    return render_template('index.html', data_file=data_file, classification_result=classification_result)

if __name__ == '__main__':
    app.run(debug=True)
    