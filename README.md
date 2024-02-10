# Doctors Office Management System
<p align="justify">
Advancements in technology and communication have led to a wide range of tasks and activities being conducted in the Internet environment. One of the most important aspects of our daily lives is the availability of healthcare facilities. Due to the fast-growing population in cities, we have designed a system to facilitate making doctor appointments across the country. As a large-scale project, we have decided to implement a microservice architecture. To implement this project, there are three different services, including authentication, a patient, and a doctor. In the following, we delve into more details.
</p>

## Authentication Service
This service requires defining users and managing their access to different parts. This service is responsible for registration, authentication, and controlling user access. Users in this system can have three different roles as *doctor*, *regular user*, and *guest user*. To register as a doctor, either a medical license number or a phone number could be used. The code below is shown the POST API for registering users.
<div align="center">

![Screenshot from 2024-02-09 20-45-24](https://github.com/SaraBolouriB/doctors_office_management_system/assets/45979215/3646638e-7862-4623-bc92-d95d97b35992)
</div>

## Patient Service
<p align="justify">
This service is designed as a panel for regular users. With this service, regular users can view a list of doctors in a specific city, filter the list by city, specialization, and education degree, schedule appointments for specific times (subject to the doctor's availability), and search for a doctor by name or medical license number.
</p>
