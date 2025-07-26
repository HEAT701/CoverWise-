========================================================
             WARRANTY MANAGEMENT SYSTEM
========================================================

📌 PROJECT NAME: WarrantyVault
📌 VERSION: 1.0.0
📌 DEVELOPED BY: [CoverWise]
📌 TECHNOLOGY STACK: Django (Python), HTML, CSS, SQLite/PostgreSQL
📌 LAST UPDATED: [26 -07-2025]

--------------------------------------------------------
🔍 DESCRIPTION
--------------------------------------------------------

WarrantyVault is a web-based warranty management system that helps users:
- Register their purchased products
- Track warranty periods
- Receive alerts before expiry
- Store receipts, invoices, and serial numbers securely
- Get OTP or SMS/email notifications for warranty updates

Perfect for individuals and small businesses who need to manage warranty lifecycles effectively.

--------------------------------------------------------
🛠️ FEATURES
--------------------------------------------------------

✔️ User registration and login with OTP support  
✔️ Profile and product management  
✔️ Upload invoices/images for warranty proof  
✔️ Auto-expiry tracking and reminders (SMS/Email)  
✔️ Admin dashboard for analytics  
✔️ Mobile responsive frontend (HTML/CSS)  
✔️ Secure backend with Django  
✔️ JWT-based API authentication (for mobile or future integrations)

--------------------------------------------------------
🚀 INSTALLATION GUIDE
--------------------------------------------------------

1. 📦 Clone the Repository:
   > git clone https://github.com/yourusername/warrantyvault.git

2. 🐍 Create a virtual environment:
   > python -m venv env  
   > source env/bin/activate (Linux/Mac)  
   > env\Scripts\activate (Windows)

3. 🛠️ Install dependencies:
   > pip install -r requirements.txt

4. 🛠️ Run migrations:
   > python manage.py makemigrations  
   > python manage.py migrate

5. ⚙️ Start the development server:
   > python manage.py runserver

6. 🔑 Create superuser (for admin access):
   > python manage.py createsuperuser

7. 🌐 Open in browser:
   > http://127.0.0.1:8000

--------------------------------------------------------
📁 FOLDER STRUCTURE
--------------------------------------------------------

- /warrantyvault/         → Main Django project folder
- /templates/             → HTML templates (login, dashboard, etc.)
- /static/                → CSS, JS, images
- /accounts/              → User authentication and profile
- /products/              → Product and warranty logic
- /media/                 → Uploaded files (invoices, etc.)

--------------------------------------------------------
📨 SMS/OTP NOTIFICATION (Optional)
--------------------------------------------------------

- Integrated via Twilio or Fast2SMS
- Requires setup of `.env` or settings.py with API credentials
- Celery + Redis recommended for asynchronous scheduling

--------------------------------------------------------
🧪 TESTING
--------------------------------------------------------

> python manage.py test

You can add your own test cases inside `tests.py` for each app.

--------------------------------------------------------
📃 LICENSE
--------------------------------------------------------

This project is licensed under the MIT License.

--------------------------------------------------------
📞 SUPPORT
--------------------------------------------------------

For support or customization, contact:
📧 Email: yourname@example.com  
🌐 Website: www.yourwebsite.com  

--------------------------------------------------------
