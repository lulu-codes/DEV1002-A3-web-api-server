# DEV1002: Assessment 3 - Web Server API

---

## Project Overview



### Comics Log API

This API is designed for tracking joke materials (bits), plan and build ordered set lists and log performance feedback.

### Entities

- Users
- Materials
- Set List Items (Junction Table between Materials and Performances)
- Performances
- Venues

---

## Getting Started

### System Requirements and Prerequisites

- Python Version 3.10+
- PostgreSQL
- Windows, Linux, WSL or MacOS
- PIP (Python package installer)
- Internet Connection - To download & install dependencies and clone repo
- Disk space -

## Installation Guide

**1. Verify Python Version:**

  - For Linux/WSL/MacOS users:
    ```bash
    python3 --version  # Should display Python 3.10 or higher
    ```

  - For Windows users:
    ```bash
    python3 --version  # Should display Python 3.10 or higher
    ```
**2. Clone Repository**
```bash
git clone https://github.com/lulu-codes/DEV1002-A3-web-api-server.git
cd DEV1002-A3-web-api-server
```

**3. Create and Activate Virtual Environment:**

  - For Linux/WSL/MacOS users:
    ```bash
    python3 -m venv .venv       # Creates virtual environment
    source .venv/bin/activate   # Activates virtual environment
    ```
  - For Windows users:
    ```bash
    python -m venv .venv            # Creates virtual environment
    .\.venv\Scripts\Activate.ps1    # Activates virtual environment
    ```

**4. Install Dependencies:**
```bash
pip install -r requirements.txt    # Depending on pip version, pip3 may be required instead
```

**5. Set Up Environment Files:**
  - Create a `.env` file.
  - Then copy the variables examples included in `.env.example` file into `.env` file.
    *Example:*
    ```
    DATABASE_URI=postgresql+psycopg2://<user>:<password>@localhost:5432/comicslog
    JWT_SECRET_KEY=<paste-your-secret-key-here>
    ```
    - **DATABASE_URI:** Replace 'user' and 'password' with your local Postgres user and password.
    - **JWT_SECRET_KEY:** Replace placeholder 'your_secret_key' with a secret long random string.
      - To generate a SECRET_KEY, you can use below method or alternative method of your choice. Copy the output and replace the placeholder secret key.
        ```bash
        python -c 'import os; print(os.urandom(16))'
        # Example of output: b'&\xdc\xb8\x93\x96G\xc5K?f@\xbdw\xd7\xc5K'
        ```
        > ⚠️ **IMPORTANT!**
        > **DO NOT reveal the secret key when posting questions or committing code.**
        > Please refer to Flask-JWT-Extended documentation if needing to invalidate issued tokens:
        https://flask-jwt-extended.readthedocs.io/en/stable/options.html#jwt-secret-key

  - Create a `.flaskenv` file and copy the `.flaskenv.example` into `.flaskenv`
    ```
    FLASK_APP=main:create_app
    FLASK_ENV=development
    FLASK_DEBUG=True
    ```

**6. Create a Local Database (using PostgreSQL):**
Create a PostgreSQL Database and Role (Ensure you adjust your user/password to match your `.env` file)

```bash
psql -U postgres -c "CREATE ROLE comicslog_user WITH LOGIN PASSWORD 'mypassword';"
psql -U postgres -c "CREATE DATABASE comicslog OWNER comicslog_user;"
```

**7. Initialise Database (CLI):**

```bash
flask db create
flask db seed
```

**8. Run API**
```bash
flask run
```

**9. To Deactivate Virtual Environment when Finished**

```bash
deactivate
```


## Tech Stack Used

- **Language:** Python Version 3.16.3
- **Framework:** Flask
- **Database:** PostgreSQL
- **Development Tools:** Visual Studio Code, Insomnia


## API Endpoints




### Entity Relationship Diagram (ERD)

![ERD for Comics Log](/docs/erd.png)

## Dependencies
