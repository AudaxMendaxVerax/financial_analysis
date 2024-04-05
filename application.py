import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_path = 'all_clients_forecasts_2024_all.csv'
data = pd.read_csv(data_path)

# Streamlit UI
st.title('Client Forecast Report for 2024')

# Dropdown to select the client code
client_code = st.selectbox('Select Client Code', options=data['Client Code'].unique())

# Filter data for the selected client
client_data = data[data['Client Code'] == client_code]

# Display Client and Consultant Information
if not client_data.empty:
    client_info = client_data.iloc[0]  # Assuming all rows have the same client info
    st.subheader("Client Information")
    st.write(f"Name: {client_info['Name']} {client_info['Surname']}")
    st.write(f"Client ID: {client_info['Client Code']}")
    st.write(f"Consultant: {client_info['Consultant Name']}")
    st.write(f"Consultant ID: {client_info['Consultant Code']}")
    
    # Financial Overview Graphs
    st.subheader("Financial Overview")
    fig, ax = plt.subplots()
    ax.plot(client_data['Reference Month'], client_data['Total Liquidity'], label='Total Liquidity')
    ax.plot(client_data['Reference Month'], client_data['Total Loans/Engagements'], label='Total Loans/Engagements')
    ax.plot(client_data['Reference Month'], client_data['Total Investments'], label='Total Investments')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.legend()
    # Rotate x-axis labels
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    # Interest Margin Graph
    fig, ax = plt.subplots()
    ax.plot(client_data['Reference Month'], client_data['Interest Margin'], color='purple', label='Interest Margin')
    ax.set_xlabel('Month')
    ax.set_ylabel('Margin')
    ax.legend()
    # Rotate x-axis labels
    plt.xticks(rotation=90)
    st.pyplot(fig)

    # Expenses Analysis Graphs
    st.subheader("Expenses Analysis")
    expenses_columns = ['Food Expenses', 'Transport Expenses', 'Entertainment Expenses', 'Healthcare Expenses']
    fig, axs = plt.subplots(len(expenses_columns), 1, figsize=(5, 20))  # Adjusted figsize for better spacing
    for i, col in enumerate(expenses_columns):
        axs[i].plot(client_data['Reference Month'], client_data[col], label=col)
        axs[i].set_xlabel('Month')
        axs[i].set_ylabel('Amount')
        axs[i].legend()
        #Rotate x-axis labels
        axs[i].tick_params(axis='x', rotation=90)

    plt.tight_layout(pad=3.0)  # Adjust the padding between and around subplots.
    st.pyplot(fig)