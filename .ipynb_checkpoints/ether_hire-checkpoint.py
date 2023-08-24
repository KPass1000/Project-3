## Cryptocurrency Project - Employee Search Using Blockchain!

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
import os

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################


print("Current Working Directory:", os.getcwd())

# Import the following functions from the `crypto_wallet.py` file:
import streamlit as st
from crypto_wallet import generate_account, get_balance, send_transaction
from web3 import Web3

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# (A single Ether is currently determined in the program as well.)
candidate_database = {
    "Henry": [
        "Henry",
        "0xc4F8e5023c772bc76bDfc22DEbAC4DC78041fE64",
        "4.3",
        0.20,
        "lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0x0fa99ABaD643e6c00AF22f658c05b5Fd632C1272",
        "5.0",
        0.33,
        "ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0xD22F65E6d92CE6CFA95912A3fe19C493DD5b5b5e",
        "4.7",
        0.19,
        "jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x74e8bD6D2BbA93Af291fbbDF38430e00944a7eF6",
        "4.1",
        0.16,
        "kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates first names
people = ["Henry", "Ash", "Jo", "Kendall"]


def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    for number in range(len(people)):
        # Construct the absolute path to the image file
        image_path = os.path.join(current_dir, db_list[number][4])

        # Display the image
        st.image(image_path, width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        
         # Display star rating using Streamlit's slider
        st.write("Rate this candidate:")
        stars = st.slider("", 0, 5, int(float(db_list[number][2])), key=f"{db_list[number][0]}_rating")
        st.write("Rating:", stars, "stars")
        
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Ether Hire")
st.markdown("## Fueling Your Fintech Team!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code

#Fetch Current Price of Etherium
import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["ethereum"]["usd"]

eth_price = get_eth_price()
st.sidebar.write(f"Ether Price (USD): ${eth_price}")

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account(w3)

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Write the returned ether balance to the sidebar
def display_balance():
    balance = get_balance(account.address)
    st.sidebar.write(f"Account Balance: {balance} ETH")

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people, key="person_selection1")

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours", key="hours_input1")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################

# Calculate the wage in ether based on the professional’s hourly rate and the number of hours worked
def calculate_wage(hourly_rate, hours):
    return hourly_rate * hours

# Write the code to allow a customer (you) to send an Ethereum blockchain transaction that pays the hired candidate
def pay_candidate(account, candidate_address, wage):
    try:
        # Send the transaction
        
        transaction_hash = send_transaction(w3, account, candidate_address, wage)

        # Display the transaction hash in the Streamlit web interface
        st.sidebar.write(f"Transaction Hash: {transaction_hash.hex()}")

        # Display success message
        st.sidebar.success("Payment Transaction Successful!")

    except Exception as e:
        # Display error message if the transaction fails
        st.sidebar.error(f"Transaction Failed: {str(e)}")
                  
# Write the `wage` calculation to the Streamlit sidebar
# Calculate and display the wage in ether in the Streamlit sidebar
person = st.sidebar.selectbox("Select a Person", people, key="person_selection2")
hours = st.sidebar.number_input("Number of Hours", key="hours_input2")
hourly_rate = candidate_database[person][3]
wage = calculate_wage(hourly_rate, hours)
st.sidebar.write(f"Candidate's Wage: {wage} ETH")

# Allow the customer (you) to send an Ethereum blockchain transaction that pays the hired candidate
if st.sidebar.button("Send Transaction", key="send_button1"):
    pay_candidate(account, candidate_database[person][1], w3.to_wei(wage, "ether"))

    # Celebrate your successful payment
    st.balloons()


# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

################################################################################

## All transaction are displayed in Ganache (provided in Github). Addresses for each client were copied from Ganache as well.