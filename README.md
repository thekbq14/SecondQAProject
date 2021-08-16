# SecondQAProject - Travel App

**Introduction**

**Objective**
The objective of this project was to create an Application in Python with service-orientated architecture, using the Flask Micro-framework. Alongside, this other requirements are needed, such as a Tracking board, be that on either Trello or Jira, a relational database being produced. A risk assessment, automated tests done through Jenkins, version source control through GitHub, clear documentation and finally testing, this could be done by Unit testing through Pytest which requires coding the desired outcome of a function.

**Proposal**

Front-end - Service 1
	
Random location - Service 2
	
Random mode of transport - Service 3
	
Time taken to travel - Service 4

**Diagrams**

**Risk Assessment**

<img width="515" alt="Screenshot 2021-08-16 080853" src="https://user-images.githubusercontent.com/57040413/129524761-4d793b4a-a8cc-42cf-b0dc-8b1493518347.png">
<img width="517" alt="Screenshot 2021-08-16 080954" src="https://user-images.githubusercontent.com/57040413/129524862-213c5b9b-2dee-4864-b598-5870bd6d95a3.png">
<img width="528" alt="Screenshot 2021-08-16 081040" src="https://user-images.githubusercontent.com/57040413/129524925-af34e358-9f0f-4298-93ad-1260924fcc3b.png">


**Continous Integration**

Continous Integration is used in my project because it creates an integrated environment to development as everything is synced together. It also is rapid as well, because things such as files can be saved to VCS very quickly such as GitHub, at the same time this will allow automated testing in Jenkins. It is also used to deploy the app through Docker as these use containers instead of Virtual Machines, these tend to better because they are more lightweight and allow apps to get deployed faster. There are different parts of Docker, with Docker Compose being responsible for the building and pushing, whilst swarm is used for the app to be deployed. In between is Ansible which is a configuartion manager which configures how the the app would want to be run before it is deployed.

<img width="287" alt="Screenshot 2021-08-16 082042" src="https://user-images.githubusercontent.com/57040413/129526100-aba1c169-bbf5-422f-a778-6b6ce4353da9.png">


**ERD**

The project contains one database table so therefore and ERD of the table is needed to create a structure for it, before it used in the app properly.

<img width="128" alt="Screenshot 2021-08-16 082715" src="https://user-images.githubusercontent.com/57040413/129526762-1b56e0c3-f2d9-4993-9060-1bfe01c82e9f.png">


**Tracking Board**

Due to the complexity of the task a lot of the original ideas could not make it, as a result the application is a much more of a streamlined version then what it should be.

<img width="845" alt="Screenshot 2021-08-16 084135" src="https://user-images.githubusercontent.com/57040413/129528502-8f9b2109-4cbd-4598-8b6e-8594380e17ca.png">


**Interaction Diagram**

The app is meant to be produced that there is one main front end application which is Service 1, then everything either uses a GET or Post request to interact with it. Ideally, and in this case, Service 2 and 3 use GET requests to put there APIs through to the front end, as it is giving results to the database in order for the application to update, whilst Service 4, uses Post requests as it needs to be able to recieve information from the front end Service 1, but also give infomation to it as well. The frontend will also be connected to the database so it can show the results of it as well.

![image](https://user-images.githubusercontent.com/57040413/129527916-3e944e86-d8bc-4fba-a02a-56397fbe4291.png)


**Development**

**Application - Front End/API**

On the application, first page the user will see is the home page. This has been designed in the mind that the user's have already logged in and that this what they first see. What they will be able to see is a list off all the different a city, transport mode and journey time that will change when updated. This works by the different services and APIs interacting with one another. There is only one route that is in use as well, as a result from the looks of it the application seems pretty simple, however though the main aim of the task was to try and connect the different services using Docker and deploying them.

Below will be examples of me trying to run Docker Swarm on the machines, and the different versions of the application that have been attempted to be containerized.

<img width="680" alt="Screenshot 2021-08-16 085412" src="https://user-images.githubusercontent.com/57040413/129530820-e0cff458-07a2-4e7f-9fa6-ca1065fcff37.png">
<img width="728" alt="Screenshot 2021-08-16 085516" src="https://user-images.githubusercontent.com/57040413/129530845-00e8cfb5-8dc2-4a35-b51d-910f205e4639.png">
<img width="476" alt="Screenshot 2021-08-16 085620" src="https://user-images.githubusercontent.com/57040413/129530873-8b892625-f732-422c-87a5-4d74caf762a5.png">

I have also ran into issues with GCP that does not allow me to run my Jenkins VM as a result was not able to run Jenkins to automate the tests.

<img width="651" alt="Screenshot 2021-08-16 085330" src="https://user-images.githubusercontent.com/57040413/129530971-ad97b1e3-ce02-4ef8-99ef-6b3dd3380729.png">

**Testing**

From the testing results and also because of how the app is produced with no input are being produced which would mean that only unit testing would be needed not integration testing.

**Unit Testing**

Unit Testing was done so by testing each functions separately and seeing the results that was printed off and test to see if an exepected response to the assertion happens. These are run by the developer by using the "python3 -m pytest" command to test to see if the test will pass or not. Another similar command that can be used is "python3 -m pytest tests --cov=application --cov-report term-missing", this is done to test to see how much of the code are covered by the tests, this is sorted out by the higher the percentage the more code that are covered by the tests created. Another way that this can be done is through Jenkins which will run through a Git Webhook this will enable tests run automatically after every Git push.

**Conclusion/Future Improvements**

Overall, do feel like that the program could have been conducted in a much better way, as although every part of the specification was attempted at some point, not everything worked or was fully done to it's best. If done again a lot of changes could be done to it, such as doing Test Driven Development, this is because when programming the app one of the main issues, I had was with coding the unit tests, this could have been avoided by doing this first then building the app around it, however despite using it my experience is limited. Also, would have done a better attempt at Docker, although I did install it and use it for this task it could have been done much more bette and cohesive. I also felt like that I should have been more open and honest to my trainers by asking them for help when I needed it as well.



**Author**

Kwame Bamfo-Quaicoe

**Acknowledgements**

Oliver Nichols

Ryan Wright
