# oe_project_2

**Running instruction**

Clone git repository.
  ```sh
    git clone https://github.com/kcbojanowski/oe_project_2.git
  ```

Change the current working directory.
  ```sh
    cd oe_project_2
  ```
Migrate django app
  ```sh
    python manage.py migrate
  ```

Create superuser for using /admin site
  ```sh
    python manage.py createsuperuser
  ```

Run Django application
  ```sh
    python manage.py runserver
  ```
