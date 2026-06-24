# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I first looked at the game, it originally seemed like a well-created game with clear instructions "Guess a number between 1 and 100. Attempts left: 7" and three buttons to carry out different functionalities: Submit Guess, New Game, and Show hint. I was able to enter a number as a guess and submit it, but that is when I realized that the hints it was giving me were incorrect and one of the buttons, "New Game", was not functional. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  One bug I noticed almost immediately was that the hints were the opposite of what the expected hint should have been. When I guessed a number higher than the correct guess, the game would prompt me to guess higher when it should have prompted me to guess lower. Additionally, when I guessed a number lower than the correct guess, the game would prompt me to guess lower when it should have prompted me to guess higher. Additionally, when I would try to start a new game using the "New Game" button, the game would not restart. The only thing that changed was the "Attempts left" counter but I was no longer able to submit new guesses. Pressing the "Submit Guess" button does not produce any new outputs. Lastly, when a new game starts and the  "Attempts left" counter refreshes, it does not go down when I click the "Submit Guess" button. With each guess the counter should decrease by one but it stays at the number that it start with.

  AI explanation of one of the bugs:

What happens:

Clicking New Game sets st.session_state.attempts = 0 and a new secret, then immediately calls st.rerun().
The code later checks if st.session_state.status != "playing": ... st.stop(). Because the New Game handler does NOT reset st.session_state.status, if the previous game had set status to "lost" or "won" that value persists.
On rerun the guard sees status != "playing", runs the "game over" / "you already won" branch and calls st.stop(). st.stop() halts further execution of the script for that run, so the submit button handler (the if submit: block) never runs — pressing Submit appears to do nothing.

Why the "Attempts left" counter changed but Submit didn't work:

You did set attempts to 0, and the page re-rendered, so the computed "Attempts left" (which is attempt_limit - st.session_state.attempts) updated accordingly.
But because status was still "lost"/"won", the script reached the early-exit guard and stopped before it evaluated the if submit: branch. So the UI shows the updated attempt count but the app is effectively in a stopped "game over" state and won't process guesses.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input          | Expected Behavior | Actual Behavior | Console Output / Error |
|-------         |-------------------|-----------------|------------------------|
guess of 2        "Go HIGHER!"        "Go LOWER!"        None
guess of 88       "Go LOWER!"         "Go HIGHER!"       None
"New Game" button pressed | Expected: previous guess disappears | Actual: previous guess still in text box | None  


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
  I used the AI coding assistant in VS code which uses GPT-5

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  When I told the AI that the "New Game" button did not successfully prompt a new game, it suggested that the reason was because the New Game handler did not reset the st.session_state.status. The suggestion was correct and the AI recommended to change the code by ensuring that the status is set back to "playing" instead of "win" or "lose" when the "New Game" button is clicked. I verified that this repair was correct by playing the game after the code changes were made and ensuring that pressing the "New Game" button would start a new game and allow me to submit new guesses.
  
  One misleading part of the AI's suggestion occurred when I reported that the "New Game" button was not successfully starting a new game. The AI suggested code changes to reset the game state when the button was pressed, and most of these changes were correct. However, the suggestion was somewhat misleading because it did not address clearing the text box where the player enters guesses. Even after the button was pressed, the previous guess remained in the text box, creating the impression that the game had not been reset properly and making it difficult to determine whether the "New Game" button was actually working as intended. After implementing the recommended changes, I verified the result by running and playing the game. While the game itself reset correctly, the previous guess remained visible in the input field after pressing the "New Game" button. This could make it appear as though a new game had not started, even though the game state had been reset. I then had to prompt the AI to recommend another change to the code in order to ensure that this issue was resolved. I then played the game again after the second round of recommendations were implemented and I verified that the game was operating correctly with the input text book clearing when the reset button was pressed. 


  
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I decided that a bug was fixed by manually testing the game after implementing the code changes. Rather than assuming the AI's recommendations were correct, I ran the application and interacted with the game to confirm that the behavior matched the intended functionality. If the issue no longer occurred and the game behaved as expected, I considered the bug resolved.
  
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One manual test I ran involved the "New Game" button. After implementing the AI's suggested changes, I played the game several times until it reached a win or lose state and then pressed the "New Game" button. This test showed that the game state was being reset correctly because I could submit new guesses again. However, it also revealed that the previous guess remained in the input text box, which made it appear as though the game had not fully reset. After implementing an additional fix, I repeated the test and confirmed that both the game state and the input field were properly reset when the button was pressed.


  
- Did AI help you design or understand any tests? How?

  Yes. The AI helped me identify what parts of the application should be tested after making code changes. For example, after suggesting changes to the "New Game" functionality, it led me to focus on testing whether the game state was reset correctly and whether the user could submit new guesses. Although I relied primarily on manual testing to verify the fixes, the AI helped me understand which behaviors were most important to check after modifying the code.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
