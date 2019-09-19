# API
The API for the Dekker Build Week project

## Installation

To install this applications dependencies on Mac with brew, first install and links its dependencies with
```
brew install openssl
brew install postgresql
export LDFLAGS="-L/usr/local/opt/openssl/lib"
pip3 install -r requirments.txt              # You should probs do this step in a virtual enviroment, but w/e
./release.sh
```
Then run the application by navigating to the  `andch_back` directory and run `python manage.py runserver`
