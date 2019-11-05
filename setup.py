from setuptools import setup
from limiarizacao import __version__

setup(name='limiarizacao',
      version=__version__,
      description='Limiarização em binários',
      url='https://github.com/liragabriel/limiarizacao',
      author='Gabriel Lira',
      author_email='contact@liragabriel.com',
      license='MIT',
      packages=['limiarizacao'],
      install_requires=['flask', 'pandas', 'matplotlib', 'werkzeug', 'opencv-python'],
      zip_safe=False)
