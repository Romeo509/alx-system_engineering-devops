
<h1>Regular Expression Project - README</h2>
<h2>Overview</h2>
This project focuses on mastering regular expressions using the Oniguruma library in Ruby. The tasks involve creating Ruby scripts with specific regex patterns to fulfill various requirements. Below is a breakdown of the tasks and the rationale behind each solution.

<h2>Task 0: Simply Matching School</h2>
Description:
The goal here is to create a regex that matches the string "School." The provided Ruby script (0-simply_match_school.rb) takes an argument and applies the regex using the scan method.

Example:

./0-simply_match_school.rb School | cat -e outputs School$
<h2>Task 1-6: Repetition Tokens</h2>
Description:
These tasks require finding regex patterns that match specific cases. Each script (1-repetition_token_0.rb, 2-repetition_token_1.rb, etc.) accepts an argument and uses the scan method to apply the corresponding regex pattern.

<h2>Task 7: OMG WHY ARE YOU SHOUTING?</h2>
Description:
The objective is to create a regex that matches only capital letters. The script (7-OMG_WHY_ARE_YOU_SHOUTING.rb) takes an argument, applies the regex using scan, and outputs the matched uppercase letters.

Example:

./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e outputs ILOVESYSADMIN$
Task 8: Textme (Advanced)
Description:
This advanced task involves parsing log files to extract information about text messages. The script (100-textme.rb) outputs the sender, receiver, and flags for each text message transaction.

Example:

./100-textme.rb '... [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] ...' | cat -e outputs Google,+16474951758,-1:0:-1:0:-1$
Additional Notes
Scripts are organized and follow best practices for code readability.
Scripts are tested with various inputs to ensure robustness.
The README is regularly updated with any additional information or changes.
Acknowledgments
