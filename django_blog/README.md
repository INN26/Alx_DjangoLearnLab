# Django Authentication System

## Installation
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Authentication Features
- User registration
- User login/logout
- Profile editing (coming soon)

## Security Measures
- CSRF protection enabled
- Secure password storage using Django’s built-in hashing

1️⃣ Blog Post CRUD Operations
ListView → Displays all blog posts.
DetailView → Shows the full content of a single blog post.
CreateView → Allows authenticated users to create a new post.
UpdateView → Enables the post author to edit their post.
DeleteView → Permits the post author to delete their post.
2️⃣ Permissions & Access Control
Only authenticated users can create posts.
Only the author of a post can edit or delete it.
All users (authenticated or not) can view posts.
3️⃣ URL Configuration
Feature	URL	Access
List all posts	/posts/	Public
View a post	/posts/<int:pk>/	Public
Create a post	/posts/new/	Authenticated users only
Edit a post	/posts/<int:pk>/edit/	Only the post author
Delete a post	/posts/<int:pk>/delete/	Only the post author
🛠 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd django_blog
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate
4️⃣ Create a Superuser (Optional)
bash
Copy
Edit
python manage.py createsuperuser
5️⃣ Run the Development Server
bash
Copy
Edit
python manage.py runserver
Then open http://127.0.0.1:8000/posts/ in your browser.

📝 Usage Guide
📌 Creating a Blog Post
Log in or register.
Click "New Post".
Fill in the title and content.
Click "Save".
📌 Editing a Blog Post
Navigate to your post.
Click "Edit" (only visible if you are the author).
Update the content and save.
📌 Deleting a Blog Post
Navigate to your post.
Click "Delete" (only visible if you are the author).
Confirm deletion.
🔐 Permissions & Data Handling
User Authentication: Uses Django’s built-in authentication system.
Security:
Uses LoginRequiredMixin for protecting create/edit/delete views.
Uses UserPassesTestMixin to ensure only authors can modify their posts.
Data Validation: Form fields are validated using Django’s ModelForm.
Database: SQLite by default (changeable in settings.py).