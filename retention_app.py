import streamlit as st
import matplotlib.pyplot as plt

# Title and Instructions
st.title("User retention over time")
st.write("This script simulates user retention over a year in a SaaS business by modeling monthly churn and acquisition rates, allowing you to see how the user base evolves over time. Starting with an initial user count, the script applies a rolling 30-day churn rate each month, compounding losses from the remaining user base. At the same time, it models monthly acquisition, which can be a fixed number of new users added each month or a percentage of the remaining user base. This approach reflects realistic user growth and retention dynamics, with the results displayed in a line chart that illustrates the overall trend in user count across 12 months.")
st.write("For any questions or inquiries, please contact me at tomas.hermansky@gmail.com.")
st.write("View the [source code on GitHub](https://github.com/pax-385/SAAS_retention).")

# Input Widgets
rolling_30_churn_rate = st.number_input("Rolling 30-day Churn Rate (%)", min_value=0.0, max_value=100.0, value=9.9) / 100
initial_user_count = st.number_input("Initial User Count", min_value=0, value=1000)

# Option to select acquisition type
acquisition_type = st.radio("Monthly Acquisition Type", ["Percentage of Current Users", "Absolute Number" ])

# Acquisition input based on the selected type
if acquisition_type == "Absolute Number":
    monthly_acquisition = st.number_input("Monthly Acquisition (new users per month)", min_value=0, value=100)
else:
    monthly_acquisition_percentage = st.number_input("Monthly Acquisition Rate (%)", min_value=0.0, max_value=100.0, value=5.0) / 100

# Lists to store monthly user counts and time points
user_counts = [initial_user_count]
months = list(range(1, 13))

# Calculate user retention for each month
for month in months:
    # Apply churn rate to current user count
    retained_users = user_counts[-1] * (1 - rolling_30_churn_rate)
    
    # Determine new acquisition based on the selected acquisition type
    if acquisition_type == "Absolute Number":
        new_total = retained_users + monthly_acquisition
    else:
        new_total = retained_users * (1 + monthly_acquisition_percentage)
    
    # Append new total user count to list
    user_counts.append(new_total)

# Plot the retention graph
fig, ax = plt.subplots()
ax.plot(range(13), user_counts, marker='o', linestyle='-', color='b')
ax.set_title('User Retention Over 12 Months')
ax.set_xlabel('Month')
ax.set_ylabel('Total Users')
ax.set_xticks(range(13))
ax.grid(True)

# Show the plot in Streamlit
st.pyplot(fig)
