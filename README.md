
# README #

Python3 API with basic dependencies (Flask, Mongodb, PyMongo).

### How do I get set up? ###
* Install Git and Clone this repository (git clone <clone utl>)
* Install python dependencies (pip install -r requirements.txt)
* Run the API with (python index.py)
  
  
 ### To run apiServer in Docker

To Build the Docker image 

```bash
$ docker build -t apiserver:latest .
```

To Run the Docker container 

```bash
$ docker run -d -p 5555:5555 apiserver
```
The application will be accessible at http:127.0.0.1:5555
