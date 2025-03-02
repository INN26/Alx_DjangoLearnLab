# Django Role-Based Access Control (RBAC) Setup

## **Custom Permissions**
- `can_view`: View books
- `can_create`: Add new books
- `can_edit`: Edit existing books
- `can_delete`: Delete books

## **Groups and Their Permissions**
Group     Permissions                
Viewers   can_view                    
Editors   can_view, can_create, can_edit 
Admins    can_view, can_create, can_edit, can_delete 

## **Admin Setup**
To create a superuser:
```bash
python3 manage.py createsuperuser