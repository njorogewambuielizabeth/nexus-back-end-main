This repository houses the backend code for our IoT device that provides real-time power usage monitoring and introduces the concept of power sharing among neighbors. This README will guide you through the setup and usage of the backend system.

## Project Overview
The Nexus Interface Unit is an IoT device designed to revolutionize the way users monitor and manage their power consumption.<br/>
 Here are some key features of our device:<br/>
 
- Real-time Power Usage Monitoring: The device offers real-time monitoring of power consumption, allowing users to track their electricity usage efficiently.<br/>
- Power Capacity Insights: Users can gain valuable insights into the available power capacity, enabling them to make informed decisions about their energy consumption. <br/>
- Power Sharing: In situations where electricity resources are limited, our device introduces an innovative feature that enables power sharing among neighbors. This promotes energy efficiency and collaboration within communities.

## Backend Features
The backend of the Nexus Interface Unit Backend is responsible for handling and serving data to the frontend dashboard. Here are the core features of our backend system:
- Dashboard Data: The backend provides data for the dashboard, including power consumption statistics, customer information, and meter status (active or inactive).
- API Endpoints: We have defined API endpoints that allow communication between the frontend and backend systems. These endpoints enable data retrieval and manipulation for the dashboard.
-  Processing: Our backend system processes and aggregates data from the IoT devices, ensuring that accurate and up-to-date information is available on the dashboard.

## Getting Started
To set up and run the Nexus Interface Unit Backend on your local development environment, 
follow these steps:
1. `Clone the Repository`:
   Begin by cloning this repository to your local machine using the git clone command.
```git clone https://github.com/yourusername/nexus-backend.git```
2. `Install Dependencies`:
   Navigate to the project directory and install the required dependencies. We recommend using a virtual environment for this step.
   `python3 -m venv venv`
3. Activate the virtual environment with
    `source venv/bin/activate`
4. cd nexus-backend
5. ``pip install -r requirements.txt``
6.  `Run the Backend`: Start the backend server using your preferred web framework (Django).
7.  Access the Dashboard`: Open a web browser and navigate to the backend server's URL to access the dashboard.
