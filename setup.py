from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = str()
with open('README.md') as f:
    readme = f.read()

setup(name='pyFlask',
      version='1.0',
      description='OpenShift App',
      author='KasparEdor',
      author_email='---',
      url='---',
      install_requires=['Flask>=0.7.2', 'MarkupSafe'],
      )
