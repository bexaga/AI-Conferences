import streamlit as st
import pandas as pd
import plotly.express as px

# Load the Excel file
def load_data(file_path):
    return pd.read_excel(file_path)

# Function to filter data
def filter_data(df, region, start_date, end_date):
    filtered_df = df[(df['Region'] == region) &
                     (df['Start Date'] >= start_date) &
                     (df['End Date'] <= end_date)]
    return filtered_df

# Function to create timeline
def create_timeline(df):
    fig = px.timeline(df, x_start="Start Date", x_end="End Date", y="Conference Name", color="Region", title="Conference Timeline")
    fig.update_yaxes(categoryorder="total ascending")
    return fig

# Streamlit app
def main():
    st.title("AI Conferences Timeline")

    # Load data
    file_path = "AI-Conferences.xls"  # Update with the correct path if needed
    data = load_data(file_path)

    # Sidebar for filters
    st.sidebar.header("Filter Options")
    regions = data['Region'].unique()
    selected_region = st.sidebar.selectbox("Select Region", regions)
    start_date = st.sidebar.date_input("Start Date", data['Start Date'].min())
    end_date = st.sidebar.date_input("End Date", data['End Date'].max())

    # Filter data based on user input
    filtered_data = filter_data(data, selected_region, start_date, end_date)

    # Display filtered data
    st.subheader("Filtered Conferences")
    st.dataframe(filtered_data)

    # Create and display timeline
    st.subheader("Conference Timeline")
    timeline_fig = create_timeline(filtered_data)
    st.plotly_chart(timeline_fig)

if __name__ == "__main__":
    main()

