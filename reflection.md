# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").


- I noticed the game kept telling me to guess higher when the correct guess was actually lower, and vice-versa
- I also noticed the range of numbers to guess from were not correctly assigned to the difficulty ranges (eg. 1-100 for Normal but 1-50 for Hard).
- I also noticed the numbers of attempts were not correctly assigned to the difficulty ranges (eg. 5 attempts for easy but 7 attempts for Normal).
- I also noticed I couldn't restart the game after I had clicked on the new game button twice

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used Claude Code in the VS Code IDE.


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  For the error where changing the difficulty levels didn't reflect on the games numnber ranges, Claude Code correctly identified that one of the errors was that the info message hardcodes "1 and 100" instead of using the dynamic low and high variables.

  I verified the result by crosschecking the tagged error code, then tracking back to where the low and high variables where declared, which correctly reflected what the AI identified.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  For the error where the hint always said "go higher" no matter what, my AI originally suggested that I just remove the alternating string conversion so the secrete variable is always passed as an integer.
  
  However, when I checked the function in lines 157-160 in app.py, there were other errors like the even-numbered atempts converting secret to a string, breaking numeric comparison.



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  
  I ran pytest cases for the specific logic I was fixing.

- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.
  I ran a numeric vs lexicographic test, making sure that integers were compared, not strings. It showed that the secret variable was being cast as a string instead of a numeric value.

- Did AI help you design or understand any tests? How?

  Yes, it did. It explained the aim of the tests, and showed me how to design new ones and run them on my terminal.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  I was because the random function to generate the secret was being re-run evry time the app reloaded. It should've been stored in a state.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Basically, Streamlit reloads the entire app every time a user interacts with the webpage(eg. clicking a button, writing in a text box, etc).
  
  Session states are used to store things you don't want to change even if the app reloads. It's like the way constant variables do not change no matter wwhat happens to the code.

- What change did you make that finally gave the game a stable secret number?

  I stored the secret in a session state and made sure there was no secret stored before generating a new one.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  One strategy I would keep implementing is understanding the code for myself before debugging with AI.

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?

  Next time, I would tell it to explain any suprising changes it's about to make before agreeing to change it.


- In one or two sentences, describe how this project changed the way you think about AI generated code.

  I no longer see it as cheating or a lazy route, but as a more efficient way to achieving my goals in a much shorter time. I just need to make sure to actually understand what I'm building to avoid running into quicksand code.
