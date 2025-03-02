
import java.util.Scanner;
def calculate_average():
    print("Enter integers to calculate their average. Type 'done' to finish.")

    total = 0  
    count = 0  

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        
        if user_input.lower() == 'done':  
            break
        
        try:
            number = int(user_input)  
            total += number  
            count += 1  
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")

    if count == 0:
        print("No numbers were entered.")
    else:
        average = total / count
        print(f"The average of the entered numbers is: {average:.2f}")

calculate_average() 
