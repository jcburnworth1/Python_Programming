from setuptools import setup

setup(name='my_package',
      version='0.0.1',
      description='Some description',
      author='J.C. Burnworth',
      author_email='jcburnworth1@gmail.com',
      packages=['my_package'],
      install_requires=['matplotlib',
                        'numpy==1.22.0',
                        'pycodestyle>=2.4.0'])