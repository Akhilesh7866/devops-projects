# Flask Task Manager Web Application

## Project Description
This is a Task Manager web application built using Flask and MongoDB Atlas.
It allows users to add tasks using a web form and store them in a cloud database.
The application also provides REST API endpoints to retrieve task data.

## Features
- Add new tasks through a web form
- Store tasks in MongoDB Atlas
- View tasks in JSON format
- File-based API using tasks.json
- Error handling and validation
- Secure database connection using environment variables

## Technologies Used
- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- python-dotenv

## Project Structure

task_manager/
│
├── app.py
├── tasks.json
├── requirements.txt
├── .gitignore
└── templates/
    ├── index.html
    └── success.html


## Installation and Setup

1. Clone the repository

git clone https://github.com/your-username/flask-task-manager.git

2. Navigate to project folder

cd flask-task-manager

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file in the root folder and add your MongoDB connection string

MONGO_URL=your_mongodb_connection_string_here

5. Run the application

python app.py

6. Open in browser

http://127.0.0.1:5000


## API Endpoints

GET    /               → Home page and form  
GET    /api/tasks      → Get tasks from JSON file  
GET    /tasks          → Get tasks from MongoDB  
GET    /success        → Success page after submission  


## Output

- User can submit tasks
- Data is stored in MongoDB Atlas
- Success message is displayed after submission
- Tasks can be retrieved using REST APIs


## Learning Outcome

This project demonstrates:
- Flask web development
- REST API creation
- MongoDB cloud integration
- Environment variable usage
- Error handling and validation
- Backend project structure


## Author

Akhilesh Jaiswal
