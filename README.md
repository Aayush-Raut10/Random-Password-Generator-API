
# Random Password Generator API

A simple **FastAPI** project to generate random passwords and check their strength. Perfect for developers, testers, or anyone who needs secure passwords quickly.

---

## Features

* Generate random passwords with letters (uppercase, lowercase), digits, and special symbols.
* Validate password strength based on standard security rules:

  * Minimum 8 characters
  * Contains uppercase and lowercase letters
  * Contains digits
  * Contains special symbols (e.g., @#$)
* Customizable password length (up to 500 characters).

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Aayush-Raut10/Random-Password-Generator-API.git
cd Random-Password-Generator-API
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv

source venv/bin/activate # On macOS/Linux

venv\Scripts\activate # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

2. Open your browser and go to the interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. Generate Password

* **URL:** `/generate_password`

* **Method:** `GET`

* **Query Parameter:**

  * `length` (int, optional, default=8)
 

---

### 2. Check Password Strength

* **URL:** `/check_password`
* **Method:** `POST`
* **Body Example:**

```json
{
  "password": "Example@123"
}
```


## Output Screenshots

### Generate random password:
![API Output](<assets/screenshots/outputscreenshot1.png>)

### Check the password strength:
![API Output](<assets/screenshots/Screenshot 2026-03-23 223118.png>)

![API Output](<assets/screenshots/outputscreenshot3.png>)
## License

This project is licensed under the MIT License.
