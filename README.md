# Flask App File Downloader Deployed to Render

Visit my hosted site at: https://flask-authentication-app-pfg7.onrender.com/

OR

Deploy your own!

## 🚀 Deploying to Render

1. Fork this repo  
2. Go to [Render.com](https://render.com) and create a new Web Service  
3. Connect your GitHub repo  
4. Add these environment variables:  
   - `FLASK_KEY`: your secret key  
   - `DB_URI`: your PostgreSQL URI from Render's database service  

5. Set the start command to:

   ```bash
   gunicorn main:app
✅ Include .env.example with required variables
On Render:
My Workspace > Manage > Environment > Environment Variables

Make sure you add:

env
Copy
Edit
FLASK_KEY=your-secret-key
DB_URI=postgresql://user:password@host:5432/dbname
PYTHON_VERSION=3.12
⚠️ Be sure the DB_URI starts with postgresql://, and the PYTHON_VERSION is below 3.13

Deploy!
