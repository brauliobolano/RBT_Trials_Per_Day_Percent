# RBT_Trials_Per_Day_Percent

---

# Calculate Actions for Days

## Overview

This Python script, `calculate_actions_for_days.py`, calculates the percentage representation of actions over a specified number of days. It is designed to help you determine the percentage of actions completed for a given total over a specific time frame.

## How It Works

The script takes three parameters:

- `total`: The total number of actions.
- `days`: The number of days you want to distribute the actions over.
- `trials_per_day`: The number of trials per day.

Using these parameters, it calculates the percentage representation of actions distributed over the specified duration.

## Example Usage

Here's how you can use the script to calculate and print the percentage representation of actions from 1 to 40 for a specific set of days and trials per day:

```python
# Calculate and print the values for action from 1 to 40 for x days
for total in range(1, 41):
    actions = calculate_actions_for_days(total, days=6, trials_per_day=6)
    print(f"{total}. {actions:.2f}")
```

## Output Style

The script produces output in the following style:

```
1. 2.78
2. 5.56
3. 8.33
4. 11.11
...
40. 166.67
```

## License

This script is provided under the [MIT License](LICENSE).

## Author

- [Braulio Bolano Trujillo] - [Your GitHub Profile](https://github.com/brauliobolano)

## Acknowledgments

- This script was created as a simple tool for calculating percentage representations of actions over time. Used for my work as Registerd Behavior Technician. 
