Here’s a detailed report for the number-guessing game project:

---

## **Project Report: Number Guessing Game**

### **Introduction**
The Number Guessing Game is a simple yet engaging CLI-based application designed to challenge users to guess a randomly selected number within a limited number of attempts. This project demonstrates core programming concepts, including loops, conditionals, user input handling, and random number generation. It is suitable for beginners and provides an opportunity to enhance problem-solving skills.

---

### **Objectives**
1. Create an interactive CLI-based number guessing game.
2. Allow users to select a difficulty level, which determines the number of attempts.
3. Provide feedback for each guess to guide the user toward the correct answer.
4. Track the number of attempts and provide a summary at the end of the game.
5. Offer additional features like replaying the game, tracking high scores, and timing the user’s performance.

---

### **Features**
1. **Welcome Screen**: Displays game instructions and rules.
2. **Random Number Generation**: The computer randomly selects a number between 1 and 100.
3. **Difficulty Levels**:
   - Easy: 10 chances.
   - Medium: 5 chances.
   - Hard: 3 chances.
4. **Feedback System**:
   - If the guess is too high, inform the user.
   - If the guess is too low, inform the user.
5. **Win/Loss Conditions**:
   - Display a congratulatory message if the user guesses the number correctly.
   - Notify the user when they run out of attempts.
6. **Replay Option**: Allows users to play multiple rounds.
7. **High Score Tracker**: Tracks the fewest attempts taken to guess correctly for each difficulty.
8. **Timer**: Measures the time taken to guess the correct number.

---

### **Implementation**
The game is implemented using **Python**, leveraging its simplicity and rich standard library. Key modules include:
- **`random`**: For generating random numbers.
- **`time`**: For tracking the elapsed time during gameplay.

#### **Code Structure**
1. **Game Initialization**:
   - Display welcome message and instructions.
   - Allow the user to select a difficulty level.
2. **Gameplay Loop**:
   - Generate a random number.
   - Prompt the user for guesses within the allowed attempts.
   - Provide feedback after each guess.
3. **End of Game**:
   - Display results (win/lose, attempts taken).
   - Option to replay or exit the game.
4. **Additional Features**:
   - Track high scores using an in-memory variable.
   - Measure time from the start to the correct guess.

---

### **Sample Output**
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 30
Congratulations! You guessed the correct number in 3 attempts!
Time taken: 1 minute and 15 seconds.
High Score: 3 attempts (Medium difficulty).

Would you like to play again? (yes/no): no
Thank you for playing!
```

---

### **Future Enhancements**
1. **Hint System**: Provide additional clues, such as divisibility or proximity ranges.
2. **Multiplayer Mode**: Allow multiple users to compete by taking turns.
3. **Leaderboard**: Save high scores persistently across sessions.
4. **Graphical Interface**: Enhance the game with a GUI for better user engagement.
5. **Expanded Difficulty Levels**: Add customizable ranges and attempts.
