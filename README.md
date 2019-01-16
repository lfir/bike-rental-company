This repository contains modules with classes and tests for a program that can be used to register rentals, written in Python 3.

----
## Design


### Class diagram
![alt text](https://i.postimg.cc/mgVhwdcq/bike-rental-3.png)

### Guidelines
Class-based design with mainly composition and collaboration relations between objects. Also inheritance was used with strongly related classes.

Abstract base classes were used to declare and enforce the minimum required interface for the system and the separation of responsibilities.

----
## Development practices
* UML.
* TDD.
* SOLID principles.

----
## How to run the tests
1. Install pipenv and git. For instance on Fedora they can be installed running:

 sudo dnf install pipenv git

2. Clone this repository and cd to its dir.

 git clone https://github.com/Asta1986/bike-rental-company.git

 cd bike-rental-company

3. Create a virtual environment and install dependencies.

 pipenv install

4. Run tests with coverage report.

 PYTHONPATH=. pipenv run pytest --cov-report term-missing --cov=bike_rental/ tests/

Output should look like this:
![alt text](https://i.postimg.cc/0y5ybptC/Screenshot-at-2019-01-15-21-35-44.png)
