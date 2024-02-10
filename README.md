# Doctors Office Management System
<p align="justify">
Advancements in technology and communication have led to a wide range of tasks and activities being conducted in the Internet environment. One of the most important aspects of our daily lives is the availability of healthcare facilities. Due to the fast-growing population in cities, we have designed a system to facilitate making doctor appointments across the country. As a large-scale project, we have decided to implement a microservice architecture. To implement this project, there are three different services, including authentication, a user panel, and a doctor panel. This project consists of three phases.
  
  - **First phase:** implementing services.
  - **Second phase:** utilizing the *Docker Engine* to create a Docker Image for those services implemented in the previous phase.
  - **Third phase:** Utilizing *Docker-Compose* and *Docker-Swarm* to run the system in two different machines.
</p>

## First phase
In this phase, we have implemented services (patient and authentication) by using REST APIs, and Django frameworks. In the following, we delve into more details.

## Authentication Service
This service requires defining users and managing their access to different parts. This service is responsible for registration, authentication, and controlling user access. Users in this system can have three different roles as *doctor*, *regular user*, and *guest user*. To register as a doctor, either a medical license number or a phone number could be used. The code below shows the POST API for registering users.
<div align="center">

![Screenshot from 2024-02-09 20-45-24](https://github.com/SaraBolouriB/doctors_office_management_system/assets/45979215/3646638e-7862-4623-bc92-d95d97b35992)
</div>

## Patient Service
<p align="justify">
This service is designed as a panel for regular users. With this service, regular users can view a list of doctors in a specific city, filter the list by city, specialization, and education degree, schedule appointments for specific times (subject to the doctor's availability), and search for a doctor by name or medical license number.
As mentioned before, there are three different roles as *doctor*, *regular user*, and *guest user*, and each of them has their own accessibility. In the following, we delve into more details:
</p>

- ### Guest user
A user who has not registered or logged in is considered a guest user. This type of user can register and choose to be identified as either a doctor or a regular user. They should choose their role during registration. Their accessibilities are listed below:
1. Register and log in to the system
2. Search for a doctor by name, city, specialization, and education degree.
3. View the list of doctors and filter them by name, city, specialization, and education degree.

- ### Doctor
After registering as doctors and logging in, users have the following accessibilities:
1. View the list of patients who have requested an appointment.
2. Modify their personal information and access it.
3. Adjust their working days and hours.
4. View comments related to them.

- ### Regular user
After registering as regular users and logging in, users have the following accessibilities:
1. Request an appointment.
2. Add doctors to their favorite list.
3. Comment on each doctor.
4. Set and modify their personal information.

## Doctor Service
This system is designed for doctors to schedule appointments and adjust their attendance schedules. 
<hr />

## Second phase
<p align="justify">
We use the Docker Engine to create a Docker image for the patient service and execute it within a container. Images for other services are developed by different groups and shared with us.  To create the docker image, a DockerFile is generated, as illustrated in the image below.
</p>
<div align="center">
  
![image](https://github.com/SaraBolouriB/doctors_office_management_system/assets/45979215/869728db-f93b-4743-8272-2adbf71de80f)
</div>
<hr />

## Third phase
In this phase, all services are executed simultaneously through two different machines. To capsulate all services into one system, the docker-compose.yml file is generated and put all the images into a service section, as shown in the picture.

<div align="center">
  
![image](https://github.com/SaraBolouriB/doctors_office_management_system/assets/45979215/ad1bad18-fba0-4d35-8a81-605b41acbd79)
</div>
To facilitate the system's operation on two machines, we initially create virtual machines (e.g., using VirtualBox). Subsequently, with Docker Swarm, we establish a leader node and two worker nodes, and then set up a bridge network to enable communication between the machines. Ultimately, leveraging these nodes, our system is successfully operational.
