<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Connector for User Requests
</h1>
<h4 align="center">A Python backend that simplifies user access to OpenAI's powerful language models.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework: FastAPI" />
  <img src="https://img.shields.io/badge/Backend-Python-red" alt="Backend: Python" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database: PostgreSQL" />
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="LLMs: OpenAI" />
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/ai-connector-mvp?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/ai-connector-mvp?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/ai-connector-mvp?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository contains the backend for the AI Connector for User Requests MVP. It provides a simple and user-friendly interface for interacting with OpenAI's powerful language models, enabling users to leverage AI capabilities without needing technical expertise.

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architectural pattern with separate directories for different functionalities, ensuring easier maintenance and scalability.             |
| 📄 | **Documentation**  | The repository includes a README file that provides a detailed overview of the MVP, its dependencies, and usage instructions.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as FastAPI, Uvicorn, Pydantic, SQLAlchemy, psycopg2-binary, OpenAI, python-multipart, dotenv, pytest, pytest-cov, and flake8, which are essential for building and managing the backend, interacting with the database and the OpenAI API, and handling file uploads. |
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities such as the API, models, services, utils, and tests.|
| 🧪 | **Testing**        | Implement unit tests using frameworks like pytest to ensure the reliability and robustness of the codebase.       |
| ⚡️  | **Performance**    | The performance of the system can be optimized based on factors such as the database and hardware being used. Consider implementing caching strategies and asynchronous operations for better efficiency.|
| 🔐 | **Security**       | Enhance security by implementing measures such as input validation, API key management, data encryption, and secure communication protocols.|
| 🔀 | **Version Control**| Utilizes Git for version control with appropriate workflow files for automated build and release processes.|
| 🔌 | **Integrations**   | Interacts with external services through HTTP requests, including integrations with OpenAI's API.|
| 📶 | **Scalability**    | Design the system to handle increased user load and data volume, utilizing caching strategies and cloud-based solutions for better scalability.           |

## 📂 Structure

```text
ai-connector-mvp/
├── src/
│   ├── api/
│   │   └── main.py
│   ├── models/
│   │   └── models.py
│   ├── utils/
│   │   └── logger.py
│   ├── services/
│   │   └── openai_service.py
│   ├── tests/
│   │   ├── test_openai_service.py
│   │   └── test_api.py
│   └── config/
│       └── settings.py
├── .env
├── startup.sh
├── requirements.txt
├── .flake8
└── Dockerfile
```

## 💻 Installation

### 🔧 Prerequisites

- Python 3.9+
- pip
- PostgreSQL (optional)
- Docker (optional)

### 🚀 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/coslynx/ai-connector-mvp.git
   cd ai-connector-mvp
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   * Create a `.env` file in the root directory and populate it with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key
   ```

5. **(Optional) Set up PostgreSQL:**

   * Install PostgreSQL if you haven't already.
   * Create a database for the application.
   * Update the `DATABASE_URL` in your `.env` file with the correct connection string.

## 🏗️ Usage

### 🏃‍♂️ Running the MVP

1. **Start the application:**

   ```bash
   uvicorn src.api.main:app --reload
   ```

2. **Access the API:**

   - Open your browser to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the API documentation.

## 🌐 Hosting

### 🚀 Deployment Instructions

**Deploying to Heroku:**

1. Create a Heroku app.
2. Push your application code to Heroku using the Heroku CLI.
3. Configure environment variables on Heroku (OPENAI_API_KEY, DATABASE_URL, etc.).
4. Run migrations if you are using a database.

### 🔑 Environment Variables

- **`OPENAI_API_KEY`:** Your OpenAI API key.
- **`DATABASE_URL`:** The connection string for your PostgreSQL database (if using a database).
- **`LOG_LEVEL`:** The logging level for the application.

## 📜 API Documentation

### 🔍 Endpoints

- **POST `/api/v1/request`:**  
    - Description: Sends a user request to OpenAI's API.
    - Request Body:
        ```json
        {
          "text": "Summarize this text: ...", // User request
          "model": "text-davinci-003", // OpenAI model to use (optional, defaults to 'text-davinci-003')
          "max_tokens": 1024, // Maximum number of tokens in the response (optional)
          "temperature": 0.7 // Controls the creativity of the response (optional)
        }
        ```
    - Response Body:
        ```json
        {
          "message": "Success", // Success message
          "response": "...", // AI-generated response
          "error": null // Error message (if any)
        }
        ```

## 📜 License & Attribution

### 📄 License

This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP

This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: ai-connector-mvp

### 📞 Contact

For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="" />
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="" />
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="" />
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="" />
</div>