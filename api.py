from flask import Flask, request, jsonify
from RecognitionLib import *
app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def add_message():
    content = request.json
    path = (content['path'])
    clf = loadModel("trainedModel.sav")
    #print(predict(clf, path))
    #return jsonify({"parkison":predict(clf, path)})
    return predict(clf, path)

if __name__ == '__main__':
    app.run(host= '127.0.0.1',debug=True)