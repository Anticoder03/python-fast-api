
# FastAPI User CRUD API (In-Memory)

A simple FastAPI project demonstrating basic **CRUD operations** (Create, Read, Update, Delete) using an in-memory list as storage.  
This project is intended for **learning and practice purposes only**.

---

## 🚀 Features

- FastAPI framework
- In-memory data storage (Python list)
- Basic CRUD operations
- Auto-generated API documentation (Swagger & ReDoc)
- Beginner-friendly and easy to extend

---

## 📂 Project Structure

```

fastapi_project/
│
│── main.py
│
├── requirements.txt
└── README.md

````

---

## 🛠 Requirements

- Python 3.9+
- FastAPI
- Uvicorn

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Anticoder03/python-fast-api.git
cd python-fast-api
````

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📑 API Documentation

FastAPI provides built-in interactive documentation:

* **Swagger UI:**
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **ReDoc:**
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔗 API Endpoints

### 🔹 Get All Users

**GET** `/`

**Response**

```json
{
  "message": "Server is running",
  "status": "success",
  "users": []
}
```

---

### 🔹 Create User

**POST** `/create`

**Request Body**

```json
{
  "name": "Ashish",
  "age": 20,
  "city": "Vapi"
}
```

---

### 🔹 Update User

**PUT** `/update/{name}`

**Example**

```
/update/Ashish
```

**Request Body**

```json
{
  "age": 23,
  "city": "Ahmedabad"
}
```

---

### 🔹 Delete User

**DELETE** `/del/{name}`

**Example**

```
/del/Ashish
```

---

## ⚠️ Important Notes

* Data is stored **in memory**, so it resets when the server restarts.
* No database is used.
* No validation or authentication is implemented.
* This project is **not production-ready** and is meant for learning only.

---

## 🔮 Future Improvements

* Add Pydantic models for validation
* Use unique user IDs instead of names
* Connect PostgreSQL or MySQL
* Add proper HTTP status codes
* Dockerize the application
* Add authentication & authorization

---

## 👨‍💻 Author

**Ashish Prajapati**
GitHub: [https://github.com/Anticoder03](https://github.com/Anticoder03)

---

## 📄 License

This project is licensed under the MIT License.


