cp sample-data/Menu.json sample-data/Orders.json sample-data/Types.json sample-data/Uber.json sample-data/Foodora.csv data
python3 -m pytest --cov-config=.coverageforclasstest --cov-report term --cov=. tests/class_tests
cp sample-data/Menu.json sample-data/Orders.json sample-data/Types.json sample-data/Uber.json sample-data/Foodora.csv data
python3 PizzaParlour.py