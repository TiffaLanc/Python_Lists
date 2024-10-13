# Task 1 Given the two lists, find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? 
# And how can you check to see if Alice is in both submitted and attended in one if statement?

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and attended:
    print("Alice attended class and submitted her assignment.")
else: 
    print("Oh no!")