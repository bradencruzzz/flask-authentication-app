Flask App File Downloader Deployed to Render

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


### 2. ✅ Include `.env.example` with required variables

On Render:
My Workspace>Manage>Environment>Environment Variables

**Make sure you add a PYTHON_VERSION** in Environment Variables and set it to a
version less than Python 13.3, I used Python 3.12

Also include you:
FLASK_KEY=your-secret-key
DB_URI=postgresql://user:password@host:5432/dbname
(Make sure it's postgresql)

Deploy!
