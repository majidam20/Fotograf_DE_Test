# Case study of running python files in docker images:


I did the task by following steps:

Firstly, creating images by command docker in the command prompt window and running python file (example.py) by docker. The required steps are as follows:

1- RUN `docker build example-python` <br />
2- RUN `docker run example-python`

<br />

## To debug the created image, you can do the following instructions: <br />

1- RUN  `docker images` <br />
2- Take the IMAGEID and Run `docker run SelectedImageId` <br />
3- RUN  `docker ps -a` <br />
4- RUN  `docker commit ContainerId` <br />
5- RUN  `docker run -it NewGeneratedId bash` <br />
6- RUN  `python example.py` <br />

<br />
Secondly, creating images by command docker-compose in the command prompt window and running the python file (example.py) by docker-compose. The required steps are as follows:
 
1- RUN `docker-compose build example-python` <br />
2- RUN `docker-compose up database` <br />
3- RUN `docker-compose run example-python` <br />
<br />

**Again to debug the created image, you can do the above debug instructions.**

<br />

Note1: The schema of the people and places CSVs was located in the corresponding SQL file name.

Note2: Environment values of MySQL in docker-compose.yml should be modified by your database configuration.
