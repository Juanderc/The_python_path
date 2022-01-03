FROM python:3.10

#install the dependencies
RUN pip install -r requirements.txt

#set a directory for the app
WORKDIR /app

#copy all the files in the root path to the container
COPY . /app

#make a port to the container
EXPOSE 5000

#execute the program
CMD ["python", "app.py"]