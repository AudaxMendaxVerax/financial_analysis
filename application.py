import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_path = 'all_clients_forecasts_2024_all.csv'
data = pd.read_csv(data_path)

# Streamlit UI setup
st.title('Client Forecast Report for 2024')

# Step 1: Consultant Selection and Display Consultant Information
consultant_id = st.selectbox('Select Consultant ID', options=[''] + list(data['Consultant Code'].unique()))

if consultant_id:
    consultant_info = data[data['Consultant Code'] == consultant_id].iloc[0]
    st.write(f"Consultant ID: {consultant_info['Consultant Code']}")
    st.write(f"Consultant Name: {consultant_info['Consultant Name']}")
    
    # Filter data for the selected consultant
    consultant_clients_data = data[data['Consultant Code'] == consultant_id]
    
    # Step 2: Client Code Selection (only after consultant is selected)
    client_code = st.selectbox('Select Client Code', options=[''] + list(consultant_clients_data['Client Code'].unique()))
    
    if client_code:
        # Further filter data for the selected client
        client_data = consultant_clients_data[consultant_clients_data['Client Code'] == client_code]
        
        # Display Client Information
        client_info = client_data.iloc[0]
        st.subheader("Client Information")
        st.write(f"Name: {client_info['Name']} {client_info['Surname']}")
        st.write(f"Client ID: {client_info['Client Code']}")
        
        # Plotting graphs after client selection...
        # Display Client and Consultant Information
        if not client_data.empty:
            client_info = client_data.iloc[0]
            
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
else:
    st.write("Please select a consultant to begin.")
    # Display empty graph or placeholder if no consultant is selected yet
    st.write("Graphs will appear here once a consultant and client have been selected.")

# The rest of the plotting logic remains the same, wrapped in the condition that checks if a client_code is selected
# This ensures that graphs are only attempted after a client selection is made


