# TO-DO App
This application developed using FastAPI, SQLAlchemy, and JWT for user authentication and CRUD operations for managing TO-DO tasks.

1.Install the required depentences using "pip install dependence_name" command or use pip install -r requirements.txt after cloning the repo git clone https://github.com/baravind031/To-Do-Application-

2.In this Application API Endpoints are used  for User Registration , User Login , User Profile and CRUD Operations for TO-DO Tasks
  # User Registration Endpoint with
  A POST endpoint /register/ is defined for user registration
  # User Login Endpoint
  A POST endpoint /login/ is defined for user login
  # User Profile Endpoint
  A GET endpoint /profile/{id} is defined for retrieving user profile
  ## CRUD Operations for TO-DO Tasks
  Endpoints for CRUD operations on TO-DO tasks are defined similar to user endpoints
  Create a TO-DO task (/todos/ - POST)
  Read a TO-DO task (/todos/{todo_id} - GET)
  Update a TO-DO task (/todos/{todo_id} - PUT)
  Delete a TO-DO task (/todos/{todo_id} - DELETE)

3 . Defines two database models using SQLAlchemy ORM:
    i. Todo: Represents a TO-DO task with fields id, task, and content.
    ii. User_DB: Represents a user with fields id, username, email, and hashed_password.
4. Authentication Setup
  i. An OAuth2 password bearer authentication scheme oauth2_scheme is created with the token URL /login.
  ii. A password hashing context pwd_context is initialized with the bcrypt hashing scheme for hashing passwords securely.

5. The database session is managed using the SessionLocal object created by sessionmaker and Sessions are created and closed for each request using the get_db() dependency function 
6. The application is run using uvicorn.run() method
7. To run the TO-DO App use this command "uvicorn main:app --reload"

   
8. Can generate a new secret key and replace the existing one




