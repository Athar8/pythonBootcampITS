# from datetime import datetime

# # Function to calculate the number of days old
# def calculate_days_old(birthdate_str):
#     # Convert birthdate string to datetime object
#     birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    
#     # Get the current date
#     today = datetime.now()
    
#     # Calculate the difference in days
#     age_in_days = (today - birthdate).days
    
#     return age_in_days

# # Input birthdate in YYYY-MM-DD format
# birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# # Calculate and display the number of days old
# days_old = calculate_days_old(birthdate_str)
# print(f"You are {days_old} days old.")



# 2. excel fil
 # 11.make a excel file
# import pandas as pd

# # Step 1: Create the Excel file

# # Sample data to be written to the Excel file
# data = {
#     "Name": ["Alice Johnson", "Bob Smith", "Charlie Brown"],
#     "College": ["Harvard University", "Stanford University", "MIT"],
#     "Email": ["alice.johnson@example.com", "bob.smith@example.com", "charlie.brown@example.com"]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Define the Excel file path
# file_path = 'student_info.xlsx'

# # Write the DataFrame to an Excel file
# df.to_excel(file_path, index=False)

# print(f"Excel file '{file_path}' has been created successfully.")

# # Step 2: Read the Excel file

# # Read the Excel file into a DataFrame
# df_read = pd.read_excel(file_path)

# # Display the DataFrame
# print("Content of the Excel file:")
# print(df_read)