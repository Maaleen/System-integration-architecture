import streamlit as st
import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title("Open Data API Demo")

# Define API endpoint and headers
url = "http://opendata.1212.mn/api/Data/DataList"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

# Define API payload
data = """
{
    "tbl_id": "DT_NSO_3900_004V6",
    "Period": "2015"
}
"""

# Make API request
response = requests.post(url, headers=headers, data=data)

# Check if the API request was successful
if response.status_code == 200:
    # Extract the data from the API response
    api_data = response.json()

    # Check if the API response contains data
    if "DataList" in api_data:
        # Get the data list from the API response
        data_list = api_data["DataList"]
        
       
        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data_list)
        
        # Remove the unwanted columns
        df = df.drop(columns=df.loc[:, "SCR_ENG":"SCR_ENG2"].columns.difference(["SCR_MN1"]))
        df = df.drop(columns=["TBL_ID"])
        
        df = df[df['SCR_MN'] != 'Бүгд']
        # Extract the table name (tbl_nm) if available; otherwise, set a default value
        table_name = api_data.get("tbl_nm", "ДОТООДЫН НИЙТ БҮТЭЭГДЭХҮҮНИЙ САЛБАРЫН БҮТЭЦ, салбараар хувиар")
        df = df.rename(columns={"Period": "Он"})
        df = df.rename(columns={"DTVAL_CO": "Тоо хэмжээ(₮)"})
        df = df.rename(columns={"CODE": "Дугаар"})
        df = df.rename(columns={"SCR_MN": "Бүс нутаг"})
        df = df.rename(columns={"SCR_MN1": "Нэгж"})
        # Extract the table ID (tbl_id)
        table_id = api_data.get("tbl_id", "DT_NSO_3900_004V6")

        # Set Streamlit app title with table name and ID
        st.title(f"{table_name} \n Хүснэгтийн дугаар : {table_id}")

        # Display the data in a table
        st.table(df)

        # Perform further visualization or analysis
        # For example, let's create a bar plot of a numeric column

        # Select a numeric column for visualization
        numeric_column = st.selectbox("Select a numeric column for visualization:", df.columns)

        # Create a bar plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(x=df[numeric_column], y=df.index)
        plt.xlabel(numeric_column)
        plt.ylabel("Index")
        plt.title(f"Bar Plot of {numeric_column}")
        st.pyplot(plt)

    else:
        st.error("No data available for the given parameters.")
else:
    st.error("Failed to retrieve data from the API.")



