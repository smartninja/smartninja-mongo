# Steps for deployment to PYPI.ORG

1. Create a Python 3 virtual environment.
2. Change the SmartNinja SQL version number.
3. Install setuptools and wheel: `pip install --upgrade setuptools wheel twine`
4. Run setup.py: `python setup.py sdist`
5. Upload via Twine: `twine upload dist/*`
