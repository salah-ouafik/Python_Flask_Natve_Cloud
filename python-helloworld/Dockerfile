#Version of current python cmd
#a python application : a python base image is used
From python:3.9
#we label the docker image, we use the maintainer tag
Label maintainer="OUAFIK Salaheddine"
#Copy files from the host to the container filesystem
#all the files from the current dir to the '/app' directory in the container 
Copy . /app
#defines the working directory within the container
Workdir /app
#Run command within the container
#install all the dependencies defined in the new_requirement file
#new_requirement file was filled thanks to the output of the flask --version command
Run pip install -r new_requirements.txt
#provide a command to run on container start
#start the app.py application
CMD [ "python", "app.py" ]
