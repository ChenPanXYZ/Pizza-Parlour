#!/bin/bash



rm data/Foodora.csv
rm data/Menu.json
rm data/Orders.json
rm data/Types.json
rm data/Uber.json

cp sample-data/Foodora.csv data
cp sample-data/Menu.json data
cp sample-data/Orders.json data
cp sample-data/Types.json data
cp sample-data/Uber.json data

python PizzaParlour.py

python -m pytest --cov-report term --cov=. tests/class_tests

python PizzaParlour.py
python -m pytest --cov-report term --cov=. tests/test_routes.py

rm data/Foodora.csv
rm data/Menu.json
rm data/Orders.json
rm data/Types.json
rm data/Uber.json

cp sample-data/Foodora.csv data
cp sample-data/Menu.json data
cp sample-data/Orders.json data
cp sample-data/Types.json data
cp sample-data/Uber.json data