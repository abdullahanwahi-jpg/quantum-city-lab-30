# Publish Quantum City Lab as a separate website

1. Visit https://github.com/new and sign in. Create a new repository named `quantum-city-lab-30` (private is acceptable).
2. On the new repository page select **Add file > Upload files**. Extract this ZIP first and upload the files **inside** the folder (including `app.py`, `models.py`, `book_alignment.py`, and `requirements.txt`) to the repository root. Do not upload a ZIP as the application. Commit changes.
3. Visit https://share.streamlit.io/, sign in with GitHub, select **Create app**, choose your repository, branch `main`, and main file path `app.py`.
4. Pick an available subdomain, then deploy. Copy the resulting URL. This process needs your account authorization; no live URL exists yet.
5. Check program IDs 01, 15, 20, 25, 30, download a sample CSV, and inspect the book alignment section.

**Security:** This is a research prototype with illustrative models and no new IBM hardware job submission. Never commit `.env`, API keys, IBM CRN, private evidence, or personal data. A private GitHub repository does NOT make a Streamlit Community Cloud app private. For restricted access use an authenticated hosting solution.
