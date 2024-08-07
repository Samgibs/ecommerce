Welcome to the E-commerce Platform repository. This project is a full-featured e-commerce application built with Django on the backend and React on the frontend. It includes functionalities for user authentication, product management, cart operations, and order processing.

Features User authentication (register, login, logout) Profile management Product listing and detail views Shopping cart management Order creation and history tracking Admin functionalities for managing products and orders Tech Stack Frontend:

React Redux Axios React Router JWT Decode Tailwind CSS dotenv Backend:

Django Django REST Framework MySQL Django REST Framework JWT Django CORS Headers Gunicorn Whitenoise

Setup Backend (Django)

Clone the repository: git clone https://github.com/your-username/ecommerce.git

cd ecommerce Create a virtual environment and activate it:

python3 -m venv env source env/bin/activate

Install dependencies: pip install -r requirements.txt

Set up environment variables: Create a .env file in the ecommerce/ directory and add your environment variables.

Run migrations: python manage.py migrate

Start the development server: python manage.py runserver

Frontend (React) Navigate to the frontend directory:

cd ecommerce-frontend Install dependencies:

Set up environment variables: Create a .env file in the ecommerce-frontend/ directory and add your environment variables.

Start the development server: npm start
