# Flask App File Downloader Deployed to Render

Visit my hosted site at: https://flask-authentication-app-pfg7.onrender.com/

OR

Deploy your own!

## Deploying to Render

1. Fork this repo  
2. Go to [Render.com](https://render.com) and create a new Web Service  
3. Connect your GitHub repo  
4. Add these environment variables:  
   - `FLASK_KEY`: your secret key  
   - `DB_URI`: your PostgreSQL URI from Render's database service  

5. Set the start command to:

   ```bash
   gunicorn main:app
Include .env.example with required variables
On Render:
My Workspace > Manage > Environment > Environment Variables

### Required Environment Variables

In your Render dashboard under **Environment → Environment Variables**, add the following:

- `FLASK_KEY` = your-secret-key  
- `DB_URI` = postgresql://user:password@host:5432/dbname  
  _(Make sure it begins with `postgresql://`)_
- `PYTHON_VERSION` = 3.12  
  _(Use a version below Python 3.13 or Render will fail during deployment)_

Deploy!
