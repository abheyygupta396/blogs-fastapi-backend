# FastAPI React Blog

This project is a simple blog application built with FastAPI (Python) for the backend and ReactJS for the frontend. The application allows users to perform CRUD (Create, Read, Update, Delete) operations on blog posts.

# Whole Source Code on branch:

master

## Installation

### Python (Backend)

1. Install Python (if not already installed): [Download Python](https://www.python.org/downloads/)

2. Create a virtual environment:

   ```bash
   python -m venv venv

   ```

3. Activate the virtual environment:
   MacOS / Linux: `source venv/bin/activate`

4. Install dependencies
   pip install -r requirements.txt

### Database Setup (PostgreSQL)

Install PostgreSQL

Create a new PostgreSQL database for the blog application.

Update the .env file in the backend with your database URL:

### Start command:

uvicorn main:app --reload

### Webservice Deployment Setup on Render.com

Step 1: Create a Render Account
If you don't have an account, sign up for Render at Render's official website.

Step 2: Add a New Web Service
Log in to Render.
Click on the "+New" button to create a new web service.
Connect your GitHub repository.
Configure the build command (e.g., yarn install && yarn run build for a React app).
Set the start command (e.g., yarn start for a React app).
Choose a service region.
Deploy your web service.

Step 3: Configure Environment Variables
In Render, go to your web service's settings, and under the "Environment" section, add the necessary environment variables (e.g., DATABASE_URL).

Step 4: Access Your Deployed Application
After deployment, Render will provide you with a unique URL to access your deployed FastAPI and ReactJS application.

To deploy a PostgreSQL database on Render, you can use managed database services. Render offers a fully managed PostgreSQL service called Render Databases. Below are the steps to deploy a PostgreSQL database on Render:

### Deploying PostgreSQL Database on Render

#### Step 1: Create a New Database on Render

1. Log in to your Render account.

2. In the Render dashboard, click on the "Add" button.

3. Select "Database" from the list of services.

4. Choose "PostgreSQL" as the database type.

5. Configure the database settings, including:

   - **Database Name:** Choose a name for your database.
   - **User:** Create a new user for the database.
   - **Password:** Set a strong password for the user.
   - **Version:** Choose the PostgreSQL version.

6. Click on the "Create Database" button.

#### Step 2: Configure Connection URL

1. Once the database is created, go to the database details page.

2. Under the "Settings" tab, find the "Connection Details" section.

3. Copy the "Connection URL" provided. This URL will be used in your FastAPI application to connect to the PostgreSQL database.

#### Step 3: Update FastAPI Application

In your FastAPI application (`main.py`), update the `DATABASE_URL` in your `.env` file or environment variables with the connection URL obtained from Render:

```env
DATABASE_URL=your_render_postgres_connection_url_here
```

#### Step 4: Deploy FastAPI Application

Follow the steps mentioned earlier to deploy your FastAPI application on Render. Ensure that you have updated the `DATABASE_URL` with the correct connection URL.

#### Step 5: Test the Deployed Application

After deploying both the PostgreSQL database and the FastAPI application on Render, test your application by accessing the provided URL. Verify that the application can connect to the Render-managed PostgreSQL database.

By following these steps, you can deploy both your FastAPI application and the PostgreSQL database on Render. Make sure to customize the configurations based on your project's requirements.

# Frontend Deployed Url:

[Deployed Blog Application](https://react-blogs-app.onrender.com/)

# Frontend Repository Url:

[Repository Url](https://github.com/abheyygupta396/blogs-react-frontend.git)
