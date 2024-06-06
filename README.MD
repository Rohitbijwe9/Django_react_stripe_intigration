# Django and React Authentication with JWT and Stripe Payment

This project integrates Django (backend) and React (frontend) with JWT authentication and Stripe payment processing.

## Project Structure

- `client`: React application
- `server`: Django backend

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Node.js 14.15.0+
- npm 6.14.9+

## Installation

cd server

python -m venv env
source env/bin/activate  # On Windows use `.\env\Scripts\activate`
pip install -r requirements.txt
STRIPE_SECRET_KEY=your_stripe_secret_key
PRICE_ID=your_price_id
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

