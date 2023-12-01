# problem_foodtruck
Solution for Food Truck problem

Food Truck Finder is a Django project designed to help users discover nearby food trucks in San Francisco. This project includes functionalities to find food trucks based on geographic coordinates.

## Features

- Retrieve nearby food trucks based on latitude and longitude coordinates.
- API endpoints for accessing food truck data.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- MySQL

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Vishwassolanki/problem_foodtruck.git
   cd problem_food_truck
2. Ensure MySQL is installed and running.
3. Configure Django to use MySQL:
    Update the DATABASES setting in settings.py to use MySQL as the database backend.
4. Migrate the database.
5. Populate the MySQL database with food truck data:
    Use the provided sql file (data_foodtruck.sql) to import data into the MySQL database.
6. Run the development server:

### Usage
- Access the API endpoints:
  - Nearby Food Trucks: http://127.0.0.1:8000/data/food-trucks-near-me/?latitude={latitude}&longitude={longitude}

 ### If I had more time 
 1. Integration of a Display Template:

    - Objective: Enhance user experience by visually displaying food truck locations on a map using geographic coordinates.
    - Details:
      - Utilize a frontend framework (e.g., React, Vue.js) to create an interactive map display.
      - Implement functionality to plot food truck locations on the map based on their coordinates.
      - Allow users to interact with the map, providing a more visual representation of food truck locations.
     
 2. Additional Filtering Options:

    - Objective: Provide users with more refined filtering capabilities to view specific food trucks.
    - Details:
      - Implement filters to display only approved food trucks or those with specific items or cuisines.
      - Allow users to select various filters such as approved status, cuisine types, etc., for a tailored food truck display.
     
 3. Improved User Input for Coordinates:

    - Objective: Enhance user input for coordinates to improve ease of use and accessibility.
    - Details:
      - Add input boxes or interactive elements on the frontend to allow users to enter geographic coordinates easily.
      - Implement a user-friendly interface to collect coordinates without requiring direct URL input.
