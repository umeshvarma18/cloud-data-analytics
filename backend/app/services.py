import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO


def get_dataframe_summary(df: pd.DataFrame):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary_statistics": df.describe(include="all").fillna("").to_dict()
    }


def generate_charts(df: pd.DataFrame):
    charts = {}

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:

        plt.figure(figsize=(6,4))
        sns.histplot(df[numeric_columns[0]], kde=True)

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        charts["histogram"] = base64.b64encode(buffer.getvalue()).decode()

        plt.close()

    if len(numeric_columns) > 1:

        plt.figure(figsize=(6,4))
        corr = df[numeric_columns].corr()

        sns.heatmap(corr, annot=True, cmap="coolwarm")

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        charts["correlation_heatmap"] = base64.b64encode(buffer.getvalue()).decode()

        plt.close()

    return charts