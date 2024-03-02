export FLASK_APP=src/seguid_calculator/app.py
export FLASK_ENV=development
micromamba run -n bjorn311 flask run --debug
echo "press any key to close"
read -n1 slask
