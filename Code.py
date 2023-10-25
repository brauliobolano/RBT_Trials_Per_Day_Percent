def calculate_actions_for_days(total, days, trials_per_day):
    # Calculate the percentage representation
    percentage = (total * 100)/(days*trials_per_day) 
    return percentage

# Calculate and print the values for action from 1 to 40 for x days
for total in range(1, 41):
    actions = calculate_actions_for_days(total,days = 6, trials_per_day = 6)
    print(f"{total}. {actions:.2f}")
  
# Output Style
# 1. 2.78
# 2. 5.56
# 3. 8.33
# 4. 11.11
# ... 
# 40. 166.67
