Learning lessons thus far:

- Accidently put files in ai_research_assistant/ai_research_assistant. Used mv * .* ../ 2>/dev/null
that moved all files up one directory
- untrack venv_ai_research_assistant Folder from Git, otherwise will load 882 files. Use command git rm -r --cached venv_ai_research_assistant
- always make the venv with a specific name, do not keep it simple like "venv"pip
- .env file holds the API key that is hidden adn private
- *.pdf in gitignore will ignore all files with ".pdf"


- Issue with folder being pushed to GitHub when it was in .gitignore. I need to make sure that the files are not INDENTED or have a space in the name in the .gitnore. The code was partly correct, but had a space before the name and was still being pushed. So, make sure indention is to the far left.

- In industry practice, you usually do not put logging inside the tests/ directory — tests should focus on assertions and expected behavior, not producing logs.

- Commited the HF token to .env file somehow, but did not put ".env" in .gitignore and it was commited. There  was a GitHub violation where I was unable to commit. Had to debug and make a new repo called rag_agent_llm_as_a_judge_v2. 