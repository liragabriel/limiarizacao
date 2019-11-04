import os
from cv2 import cv2
from matplotlib import pyplot as plt
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route('/')
@app.route('/inicio')
def inicio():

    for item in os.listdir('static'):
        os.remove(f'static/'+item)

    return render_template('inicio.html')


@app.route('/resposta', methods=['POST'])
def resposta():

    limite = request.form['limite']
    imagem = request.files['imagem']
    filename = secure_filename(imagem.filename)
    imagem.save(os.path.join("static/"+filename))

    plt.figure(1)
    img = cv2.imread("static/"+imagem.filename)
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayscaled, int(limite), 255, cv2.THRESH_BINARY)
    cv2.imwrite('static/threshold.jpeg', threshold)

    return render_template('imagem.html')


if __name__ == '__main__':
    app.run(debug=True)
