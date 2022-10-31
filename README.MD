# Poor Man's Twitter with Django and Vue

## SetUp for the backend

#### Clone this repository
```
git clone https://github.com/PeluMike/Poor-Man-Twitter.git
```


#### Create the virtual environment
```
python -m venv venv
```


#### Activate the virtual environment

*Windows:*
```
venv\Scripts\activate
```

*POSIX(macOS/Linux):*
```
source venv\bin\activate
```


#### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```
pip install -r requirements.txt
```


#### Migrate the database
```
python manage.py makemigrations
python manage.py migrate
```

#### Create a superuser
```
python manage.py createsuperuser
```


The server will default on local environments to be running at [127.0.0.1:8000](127.0.0.1:8000)


## SetUp for the frontend

```
Open the index.html file in your browser or use the Vscode live server. 
```

