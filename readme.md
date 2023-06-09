This script is useful when you need to provide large amounts of code as input to OpenAI's language model via the web UI, e.g., for providing an entire git repository as context for responses.

1️⃣ Run the script using the command python git-dump.py <directory>, where <directory> is the path to the directory you want to copy text from.

2️⃣ The script will read the contents of all Python and C++ files in the specified directory and its subdirectories and split the output into chunks of 300 lines each.

3️⃣ After each chunk is generated, it will be copied to your clipboard, and you will be prompted to press Enter to continue.

4️⃣ Open the OpenAI GPT web UI in your web browser and start a new prompt.

5️⃣ Paste the copied chunk into the prompt and wait for the model to generate a response (it should reply "OK").

6️⃣ Return to your terminal and press Enter to generate the next chunk, which will be copied automatically to your clipboard.

7️⃣ Repeat the previous two steps until you've finished pasting all the chunks.

