# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This is a simple number-guessing web game where the player tries to find a secret number within a difficulty-dependent range and a limited number of attempts. The UI shows remaining attempts, optionally gives high/low hints, and tracks score and guess history. The player continues guessing the secret number until they win by guessing the correct number or they lose by running out of guesses and can optionally start a new game. 

- [ ] Detail which bugs you found.
Restarting with the "New Game" button didn’t fully reset the session state because the status remained "won"/"lost" even after the button was pressed. So, the app hit the early-exit guard and st.stop() on rerun, making the "Submit guess" button appear non-responsive even after clicking the "New Game" button. Additionally, the box for entering a guess did not get cleared when the  "New Game" button was clicked, making it hard to understand if a new game had started. The guess-comparison logic mixed ints and strings producing wrong high/low hints (e.g., '9' > '10'), and the hint text that was output onto the UI was inverted.

- [ ] Explain what fixes you applied.
I refactored parse_guess and check_guess into logic_utils.py and fixed the hint messages so they match the numeric outcomes. I changed the "New Game" handler to reset attempts, status, score, history, and to assign a new secret using the current difficulty range so the early-exit guard no longer blocks the restarted game. Finally, I ran the test suite and verified the end-to-end behavior manually in the code transcript so the fixes are covered and reproducible.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The page loads when the game is run and the UI shows "Attempts left: 7" (because attempts starts at 1 and attempt_limit for Normal is 8). The current state is: score=0, status="playing", history=[].
   
2. Then, the player types in a guess, for example 40, in the box under the text "Enter your guess:" and clicks the "Submit Guess" button.
In the game, the attempts completed increments up one, parse_guess returns 40, and the check_guess function produces the outcome "Too Low" with the UI showing the message "📈 Go HIGHER!" if the "Show hint" button is clicked. Then, update_score subtracts 5 for a "Too Low" and the "Attempts left" counter goes down by one. 

3. Then the user might submit another guess, 70, by typing 70 into the input box and and clicking "Submit Guess".
In the game, the attempts completed increments up one, parse_guess returns 70, and the check_guess function produces the outcome "Too High" with the UI showing the message "📉 Go LOWER!" if the "Show hint" button is clicked. Then, update_score subtracts 5 for a "Too High" so the score is - 10 and the "Attempts left" counter goes down by one.

4. The player may guess the correct number (example: types 55 and clicks "Submit Guess"). The attempts increments up one, parse_guess returns 55, and the check_guess function produces the outcome "Win". The update_score awards win points and the score is updated accordingly (if previously -10, final score = 40). The status becomes "won" and the app displays balloons and success with the interface output "You won! The secret was 55. Final score: 40" for example. After this, further Submit clicks do nothing until a New Game resets the state.

5. Alternatively, the player runs out of chances because they keep submitting wrong guesses until attempts reach the limit.
After each wrong submission, the attempts counter increments and when attempts >= attempt_limit (≥ 8 for Normal) and the latest outcome is not "Win", the app sets the status to "lost".
The interface displays "Out of attempts! The secret was [secret]. Score: [score]". The history shows all attempted values and score reflects accumulated updates. After status is "lost", further Submit clicks are blocked by the app's early-exit guard until New Game resets state.

6. The player presses the "New Game" button. Internally, resets are performed and the secret becomes a new random number in the current difficulty range (low..high), the status changes to "playing", the score changes to 0, and the history becomes []. The app also clears the text-input "Enter your guess" box and calls st.rerun() so the UI refreshes.


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
