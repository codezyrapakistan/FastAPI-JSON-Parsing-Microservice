# 🧾 FastAPI SBOM Checker

A lightweight and efficient **FastAPI** application for analyzing and cleaning **Software Bill of Materials (SBOM)** files provided in JSON format.  
It exposes a simple REST API that validates, parses, and extracts key component details such as **name**, **version**, **license**, and **vulnerability count** — all without requiring a database.

---

## 🚀 Features

- 🔹 **Single POST Endpoint** — `/api/analyze` accepts SBOM JSON input.
- 🔹 **Validation with Pydantic** — Ensures clean and structured data.
- 🔹 **In-memory Processing** — No database layer; lightweight and fast.
- 🔹 **Cleaned Response** — Returns only the key fields.
- 🔹 **Graceful Error Handling** — Handles malformed or oversized files (up to ~5 MB).
- 🔹 **Clear Setup Instructions** — Easy to install and run.

---

## ⚙️ Tech Stack

- **Python 3.x**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

---

## 🧰 Project Structure
```bash
fastapi-sbom-checker/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes_sbom.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── sbom_models.py
│   ├── services/
│   │   └── osv_service.py
│   └── utils/
│       └── parser.py
│
├── tests/
│   └── test_sbom_api.py
│
├── requirements.txt
├── README.md
└── .gitignore


## 🧩 Installation & Run Instructions

Follow these simple steps to set up and run the FastAPI SBOM Checker on your system.

---

### 🪜 Step 1️ Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-sbom-checker.git

### 🪜 Step 2 Navigate into the project directory

```bash
cd fastapi-sbom-checker


