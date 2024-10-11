from pathlib import Path
import sys

mypkg1_directory = Path(__file__).resolve().parent

# Step 2: Navigate up to the 'src' directory
src_root = mypkg1_directory.parent  # This goes up one level

# Step 3: Add the 'src' directory to the system path
sys.path.append(str(src_root))  

# Now import the functions you need
from mypkg2.mymodule2_1 import calculate_area_of_circle
from mypkg2.mymodule2_2 import fetch_user_data

mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}

if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file using pathlib.Path. Prove it exists.

    if __name__ == '__main__':
        # The functions are in the modules in mypkg2. You will need to import them.

       # Calculate the area of a circle with a radius of 10. Print the result.
       area = calculate_area_of_circle(10)
       print(f"The area is {area}.")

       # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
       print(fetch_user_data(42, mock_database))