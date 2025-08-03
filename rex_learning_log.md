Learning lessons thus far:

- Accidently put files in ai_research_assistant/ai_research_assistant. Used mv * .* ../ 2>/dev/null
that moved all files up one directory
- untrack venv_ai_research_assistant Folder from Git, otherwise will load 882 files. Use command git rm -r --cached venv_ai_research_assistant
- always make the venv with a specific name, do not keep it simple like "venv"pip
- .env file holds the API key that is hidden adn private
- *.pdf in gitignore will ignore all files with ".pdf"