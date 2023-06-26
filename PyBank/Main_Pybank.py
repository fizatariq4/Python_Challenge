import csv

# Set the path to the CSV file
file_path = "resources_pybank/budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_path, "r") as file:
    csvreader = csv.reader(file, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop the rows in the CSV file
    for row in csvreader:
        # Count the total number of months
        total_months += 1
        
        # Calculate the net total amount
        net_total += int(row[1])
        
        # Calculate the change in profit/loss from the previous month
        current_profit_loss = int(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            total_change += change
            
            # Check for the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            
            # Check for the greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        
        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)

# Print the analysis results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
