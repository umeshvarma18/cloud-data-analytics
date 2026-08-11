git status
# ☁️ Cloud Data Analytics

A full-stack cloud-based data analytics platform that allows users to upload CSV and Excel datasets, perform data analysis, identify missing values, view summary statistics, and generate interactive visualizations.

## 🚀 Features

* 📁 Upload CSV and Excel datasets
* 📊 Analyze datasets using Pandas
* 🔢 Perform numerical processing using NumPy
* 🔍 Detect missing values
* 📈 Generate summary statistics
* 📉 Create interactive Plotly visualizations
* ⚡ FastAPI REST API backend
* ⚛️ React-based frontend
* 🗄️ PostgreSQL database integration
* ☁️ AWS cloud integration
* 🐳 Docker support
* 🔄 REST API communication between frontend and backend

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │   Data Upload & UI   │
                    └──────────┬──────────┘
                               │
                               │ REST API
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐     ┌──────────┐    ┌─────────────┐
        │  Pandas  │     │  NumPy   │    │   Plotly    │
        │  Analysis│     │Processing│    │Visualization│
        └──────────┘     └──────────┘    └─────────────┘
              │
              ▼
       ┌───────────────┐
       │  PostgreSQL   │
       │   Database    │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │   AWS Cloud   │
       │ S3 / EC2 / RDS│
       └───────────────┘
```

## 🛠️ Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| React.js     | Frontend development           |
| Python       | Backend development            |
| FastAPI      | REST API framework             |
| Pandas       | Data analysis and processing   |
| NumPy        | Numerical computations         |
| Plotly       | Interactive data visualization |
| PostgreSQL   | Database                       |
| AWS          | Cloud infrastructure           |
| Docker       | Containerization               |
| Git & GitHub | Version control                |

## 📊 Data Analysis

The platform provides useful information about uploaded datasets, including:

* Total number of rows
* Total number of columns
* Column names
* Data types
* Missing values
* Summary statistics
* Interactive visualizations

## 📈 Visualization

The application automatically generates interactive Plotly charts when suitable numerical columns are available.

Users can explore the data visually instead of relying only on raw tables and statistics.

## 📸 Screenshots

### Dashboard

Add your dashboard screenshot here:

```text
screenshots/dashboard.png
```

```markdown
![Dashboard](screenshots/dashboard.png)
```

### Data Analysis

Add your analysis screenshot here:

```text
screenshots/analysis.png
```

```markdown
![Data Analysis](screenshots/analysis.png)
```

### Interactive Visualization

Add your chart screenshot here:

```text
screenshots/charts.png
```

```markdown
![Interactive Charts](screenshots/charts.png)
```

## 📁 Project Structure

```text
cloud-data-analytics/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── database.py
│   │
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── screenshots/
│
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/umeshvarma18/cloud-data-analytics.git
```

```bash
cd cloud-data-analytics
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

### 3. Frontend Setup

Open another terminal and navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## 🔌 API Endpoints

### Health Check

```http
GET /
```

Returns:

```json
{
  "message": "Cloud Data Analytics API Running"
}
```

### Analyze Dataset

```http
POST /analyze
```

Accepts an uploaded CSV or Excel dataset and returns analytical information such as:

* Rows
* Columns
* Column names
* Data types
* Missing values
* Summary statistics
* Chart data

## ☁️ Cloud Deployment

The project is designed with cloud deployment in mind.

Planned/implemented cloud components include:

* **AWS S3** — dataset storage
* **AWS RDS PostgreSQL** — database
* **AWS EC2** — application deployment
* **Docker** — application containerization

## 🎯 Project Objective

The objective of this project is to create an easy-to-use data analytics platform that combines modern web technologies, data analysis tools, and cloud infrastructure.

The platform simplifies the process of uploading datasets, analyzing data, identifying data quality issues, and generating visual insights.

## 🔮 Future Enhancements

* 🔐 User authentication and authorization
* ☁️ Complete AWS S3 integration
* 🗄️ Complete AWS RDS deployment
* 🚀 AWS EC2 deployment
* 📊 More advanced visualization options
* 🤖 Automated machine learning insights
* 📑 Export analysis reports
* 🐳 Complete Docker-based deployment
* 📱 Responsive UI improvements

## 👨‍💻 Author

**Payili Umesh**

GitHub: [umeshvarma18](https://github.com/umeshvarma18)

## ⭐ Project

If you find this project useful, consider giving it a ⭐ on GitHub.
