from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import io
import json

import plotly.express as px


app = FastAPI()


# Allow React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "Cloud Data Analytics API Running"
    }



@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    contents = await file.read()


    df = pd.read_csv(
        io.BytesIO(contents)
    )


    charts = {}


    # Get numeric columns
    numeric_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()


    # Remove ID columns
    numeric_columns = [
        col for col in numeric_columns
        if "id" not in col.lower()
    ]



    # ==========================
    # Scatter Chart
    # ==========================

    if "Salary" in df.columns and "Experience" in df.columns:

        scatter = px.scatter(
            df,
            x="Experience",
            y="Salary",
            title="Salary vs Experience"
        )

        charts["scatter"] = json.loads(
            scatter.to_json()
        )


    elif len(numeric_columns) >= 2:

        scatter = px.scatter(
            df,
            x=numeric_columns[0],
            y=numeric_columns[1],
            title=f"{numeric_columns[0]} vs {numeric_columns[1]}"
        )

        charts["scatter"] = json.loads(
            scatter.to_json()
        )



    # ==========================
    # Histogram
    # ==========================

    histogram_column = None


    if "Salary" in df.columns:
        histogram_column = "Salary"

    elif len(numeric_columns) > 0:
        histogram_column = numeric_columns[0]


    if histogram_column:

        histogram = px.histogram(
            df,
            x=histogram_column,
            title=f"{histogram_column} Distribution"
        )

        charts["histogram"] = json.loads(
            histogram.to_json()
        )



    # ==========================
    # Bar Chart
    # ==========================

    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns.tolist()


    if (
        "Department" in df.columns
        and "Salary" in df.columns
    ):

        bar = px.bar(
            df,
            x="Department",
            y="Salary",
            title="Salary by Department"
        )

        charts["bar"] = json.loads(
            bar.to_json()
        )


    elif len(categorical_columns) > 0 and len(numeric_columns) > 0:

        bar = px.bar(
            df,
            x=categorical_columns[0],
            y=numeric_columns[0],
            title=f"{numeric_columns[0]} by {categorical_columns[0]}"
        )

        charts["bar"] = json.loads(
            bar.to_json()
        )



    result = {

        "filename": file.filename,

        "rows": len(df),

        "columns": len(df.columns),


        "column_names": df.columns.tolist(),


        "data_types": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        },


        "missing_values": df.isnull().sum().to_dict(),


        "summary_statistics":
            df.describe().fillna("").to_dict(),


        "charts": charts

    }


    return result