⚫ Online Voting System

✦ Introduction :-

▸ The Online Voting System is a secure, scalable web-based voting platform developed using Django. The system enables users to register, authenticate, and participate in elections by casting votes digitally, while administrators manage elections, candidates, and voting processes through an integrated admin dashboard.
▸ The project demonstrates secure authentication, structured backend design, and real-time vote tracking, serving as a proof-of-concept for modern digital election systems.
▸ Designed with usability, security, and scalability in mind, the platform provides a responsive user interface and ensures fair voting through controlled access and validation mechanisms.

✦ Why Online Voting?

▸ Traditional voting systems often involve manual processes, logistical challenges, and limited accessibility. Digital voting platforms aim to:
▸ Improve accessibility and convenience
▸ Reduce manual errors
▸ Provide real-time result tracking
▸ Enhance transparency and automation
▸ Demonstrate secure web application architecture
▸This project showcases how modern web technologies like Django can be used to build reliable voting solutions.

✦ System Overview

The application consists of two main components:

👤 User Panel

Users can:

▸ Register new accounts
▸Login securely
▸View available elections
▸Vote for candidates

View election results

👨‍💼 Admin Panel

Administrators can:

Create and manage elections

▸ Add or update candidates
▸ Upload candidate images
▸ Monitor voting activity

Manage users

✦ Key Features

✅ Secure User Authentication (Register / Login / Logout)
✅ One Vote Per User Enforcement
✅ Real-Time Vote Counting
✅ Django Admin Panel Integration
✅ Responsive Modern UI (Bootstrap)
✅ Candidate Image Upload Support
✅ Structured Project Architecture

✦ Technology Stack

▸ Python
▸ Django Framework
▸ SQLite Database
▸ Bootstrap (Frontend UI)
▸ HTML / CSS
▸ Django Templates

✦ Project Architecture

▸ The project follows Django’s modular app-based structure:

online_voting_system/
│
├── accounts/        # Authentication and user management
├── elections/       # Election and candidate models
├── voting/          # Voting logic and validation
├── config/          # Project configuration/settings
├── templates/       # HTML templates
├── static/          # CSS, JS, images
├── manage.py
└── requirements.txt

✦ System Workflow

1️⃣ User registers and logs into the platform.
2️⃣ Admin creates elections and adds candidates.
3️⃣ Users access available elections.
4️⃣ Voting system validates one vote per user.
5️⃣ Votes are counted and results displayed automatically.

✦ Installation & Setup

▸ Clone Repository
▸ git clone <your-repository-url>
▸ cd online_voting_system
▸ Create Virtual Environment
▸ python -m venv venv

✦ Activate environment:

▸ source venv/bin/activate        # Linux/Mac
▸ venv\Scripts\activate           # Windows
▸ Install Dependencies
▸ pip install -r requirements.txt
▸ Apply Database Migrations
▸ python manage.py migrate
▸ Create Admin User
▸ python manage.py createsuperuser
▸ Run Development Server
▸ python manage.py runserver

✦ Open browser:

http://127.0.0.1:8000/

✦ Security Rules

▸ Users must be authenticated to vote.
▸ Each user can vote only once per election.
▸ Voting actions are validated server-side.
▸ Admin privileges are restricted via Django admin roles.
▸ Candidate Image Handling
▸ Candidate image upload is optional.
▸ Default image will be used if no image is provided.
▸ Future Improvements
▸ Email verification for users
▸ Role-based access control
▸ Election scheduling and timers
▸ Blockchain-based vote verification (advanced concept)
▸ Deployment with Docker & Cloud hosting

✦ Developer

Subham Dey
dey.subham200414@gmail.com

