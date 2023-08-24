# Cryptocurrency Wallet

################################################################################
# For this Challenge, you will assume the perspective of a KryptoJobs2Go
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a KryptoJobs2Go candidate for their work.

# * Digitally sign a transaction that pays a KryptoJobs2Go candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to the Transactions
# section of Ganache to review the blockchain transaction details. To confirm that
# you have successfully created the transaction, you will save screenshots to the
# README.md file of your GitHub repository for this Challenge assignment.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
import os

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the KryptoJobs2Go Application

# In this section, you'll import several functions from the `crypto_wallet.py`
# script into the file `krypto_jobs.py`, which contains code for Fintech
# Finder’s customer interface, in order to add wallet operations to the
# application. For this section, you will assume the perspective of a Fintech
# Finder customer (i.e., you’ll provide your Ethereum wallet and account
# information to the application).

# Complete the following steps:

# 1. Review the code contained in the `crypto_wallet.py` script file. Note that
# the Ethereum transaction functions that you have built throughout this
# module-including `wallet`, `wallet.derive_acount`, `get_balance`, `fromWei`,
# `estimateGas`, `sendRawTransaction`, and others&mdash;have now been
# incorporated into Python functions that allow you to automate the process of
# accessing them.

# 2. Add your mnemonic seed phrase (provided by Ganache) to the starter code’s `SAMPLE.env` file.
# When the information has been added, rename the file `.env`.

# 3. Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# 4. Within the Streamlit sidebar section of code, create a variable named
# `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the KryptoJobs2Go customer’s (in this
# case, your) HD wallet and Ethereum account.

# 5. Within this same section of the `krypto_jobs.py` file, define a
# new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function
# and pass it your Ethereum `account.address`.


################################################################################
print("Current Working Directory:", os.getcwd())
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
import streamlit as st
from crypto_wallet import generate_account, get_balance, send_transaction
from web3 import Web3

# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
# YOUR CODE HERE

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Henry": [
        "Henry",
        "0x8E1be5e08c8588294362E4b08F0Bd611970BBBf7",
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
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the KryptoJobs2Go
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account(w3)

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
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
# Step 2: Sign and Execute a Payment Transaction

# Complete the following steps:

# 1. KryptoJobs2Go customers will select a fintech professional from the
# application interface’s drop-down menu, and then input the amount of time for
# which they’ll hire the worker. Code the application so that once a customer
# completes these steps, the application will calculate the amount that the
# worker will be paid in ether. To do so, complete the following steps:

# * Write the equation that calculates the candidate’s wage. This equation
#  should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.

# * Write the `wage` variable to the Streamlit sidebar by
# using `st.sidebar.write`.

# 2. Now that the application can calculate a candidate’s wage, write the code
# that will allow a customer (you, in this case) to send an Ethereum blockchain
# transaction that pays the hired candidate. To accomplish this, locate the
# code that reads `if st.sidebar.button("Send Transaction")`. You’ll need to
# add logic to this `if` statement that sends the appropriate information to
# the `send_transaction` function (which you imported from the `crypto_wallet`
# script file). Inside the `if` statement, add the following functionality:

# * Call the `send_transaction()` function and pass it three parameters:
# - Your Ethereum `account` information. (Remember that this `account`
# instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the
#  `account.address` information that is needed to populate the `from` data
# attribute in the raw transaction.
# - The `candidate_address` (which will be created and identified in the
# sidebar when a customer selects a candidate). This will populate the `to`
# data attribute in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to
# determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns
# as a variable named `transaction_hash`, and have it display on the
# application’s web interface.

##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. This equation
# should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.
# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# @TODO
# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
# Calculate the wage in ether based on the professional’s hourly rate and the number of hours worked
def calculate_wage(hourly_rate, hours):
    return hourly_rate * hours

# Step 2 (Continued):
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
                  
# @TODO
# Write the `wage` calculation to the Streamlit sidebar
# Calculate and display the wage in ether in the Streamlit sidebar
person = st.sidebar.selectbox("Select a Person", people, key="person_selection2")
hours = st.sidebar.number_input("Number of Hours", key="hours_input2")
hourly_rate = candidate_database[person][3]
wage = calculate_wage(hourly_rate, hours)
st.sidebar.write(f"Candidate's Wage: {wage} ETH")

# Step 2 (Continued):
# Allow the customer (you) to send an Ethereum blockchain transaction that pays the hired candidate
if st.sidebar.button("Send Transaction", key="send_button1"):
    pay_candidate(account, candidate_database[person][1], w3.to_wei(wage, "ether"))


##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
# - Your Ethereum `account` information. (Remember that this `account`
# instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the
#  `account.address` information that is needed to populate the `from` data
# attribute in the raw transaction.
# - The `candidate_address` (which will be created and identified in the
# sidebar when a customer selects a candidate). This will populate the `to`
# data attribute in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to
# determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Send Transaction", key="send_button2"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    # YOUR CODE HERE

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

################################################################################
# Step 3: Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `krypto_jobs.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run krypto_jobs.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
# * Take a screenshot of the address, balance, and transaction (TX) count.
# Save this screenshot to the README.md file of your GitHub repository for
#  this Challenge assignment.

# 6. Navigate to the Ganache transactions tab and locate the transaction.
# * Click the transaction and take a screenshot of it.
# Save this screenshot to the README.md file of your GitHub repository for
#  this Challenge assignment.
