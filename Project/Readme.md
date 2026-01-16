# Portfolio Projects

This portfolio contains two Python programs that solve real-world problems.

---

## Task 1: Beckett Pizza Plaza 4-for-3 Offer Calculator

### What it does
This program calculates the discount you get when ordering 4 pizzas and getting the cheapest one free.

### How it works
1. The program asks you to enter the prices of 4 pizzas
2. It automatically finds the cheapest pizza
3. It calculates how much you save by deducting the cheapest price from the total
4. It shows you the final cost and the percentage discount you received

### Example
- Pizza 1: £12.00
- Pizza 2: £15.00
- Pizza 3: £10.00
- Pizza 4: £13.00

The program finds that Pizza 3 is the cheapest (£10.00), so you get it free. Your final cost is £40.00 instead of £50.00 - that's a 20% discount!

### Features
- Input validation: Only accepts positive numbers
- Displays results with proper formatting and currency symbol (£)

---

## Task 2: Password Security Checker

### What it does
This program tests if you remember your password correctly by asking you to guess random letters from it.

### How it works
1. You enter your password
2. The program checks if it's long enough (at least 9 characters)
3. It randomly picks 3 letters from your password and asks you to guess them
4. If you guess all 3 letters correctly, the security check passes
5. If you guess any letter incorrectly, the check fails and stops

### Example
- You enter password: "MyPassword123"
- The program might ask: "Enter letter at position 5" (which is 's')
- If you answer correctly all 3 times, you pass the security check

### Features
- Validates that passwords are at least 9 characters long
- Uses random positions to make it harder to guess
- Stops immediately if you fail any check
- Clear feedback on whether you passed or failed

---

## Running the Programs

To run either program, use:
```
python Task1.py
```
or
```
python Task2.py
```

Then follow the prompts to enter your data.
