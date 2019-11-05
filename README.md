# Limiarização em binários

[![Author](https://img.shields.io/badge/author-Gabriel-blue)](http://www.liragabriel.com)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/liragabriel/limiarizacao/blob/master/LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-yellow)](https://github.com/liragabriel/limiarizacao/releases)


Limiarização é o processo de simplificar a imagem a níveis de preto e branco, para isso é necessário 
definir um limite para a limiarização, para cada posição da imagem, caso o valor seja maior que o
limite, ele será igual a 1, caso o contrário ele valerá 0, desta forma a imagem passa a ser composta
por valores binários.


Execute o arquivo `binarizacao.py` no console para ver o processo de limiarização.

Para executar com o Flask e fazer o processo com uma imagem real, segue abaixo os passos para a instalação no terminal linux:

    git clone https://github.com/liragabriel/limiarizacao.git
    cd limiarizacao
    pip install .

Após a instalação:

    Execute o arquivo com `python app.py` no terminal
    Acesse com `http://localhost:5000/` no navegador
