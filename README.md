# Django Student-Teacher App
This Django app provides models for students and teachers, along with a relationship to courses offered. The app makes use of inheritance from a BaseModel, which includes basic information such as name, email, and creation/update dates.

## Requirements
* Python 3.x
* Django 3.x
* Django Rest Framework

## Installation
1. Clone the repository <br>
``` git clone https://github.com/UsmanRepos/django-rest-frame-work-school-app.git ``` <br><br>
2. Install the required packages <br>
``` pip install -r requirements.txt ``` <br><br>
3. Run migrations <br>
``` python manage.py migrate ``` <br><br>
4. Run the development server  
``` python manage.py runserver ``` <br><br>

## Models
* BaseModel: contains basic information fields including first name, last name, email, created at and updated at dates.
* Courses: contains fields for name and duration of a course.
* Student: extends the BaseModel and has a many-to-many relationship with Courses. Also contains fields for major and CGPA.
* Teacher: extends the BaseModel and has a many-to-many relationship with Courses. Also contains fields for experience and subject expertise.

## Field-level validators
The project includes field-level validators to ensure that the data entered is valid. These validators check special characters and the length of the fields to ensure that they do not exceed a specified length.

## Usage
The app can be used for tracking student and teacher information for educational purposes. The many-to-many relationship with Courses allows for students and teachers to be associated with multiple courses, and courses to have multiple students and teachers. 

## Contributing
Contributions are welcome! If you would like to contribute to this project, you can start by forking the repository



