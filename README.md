# EC2 Deployment:

## Install Dependencies:

sudo apt update && sudo apt upgrade -y

sudo apt install python3-pip python3-venv -y

## Setup python venv (optional) (need to look into requirement)
cd ~/chatbot

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

### Step 1 : Make sure the knowledge base Excel is up to date
### Step 2 : Run ingest script to create FAISS Vector mapping using excel 
python app/ingest.py
### Step 3 : Run FastAPI Server 
uvicorn app.main:app --host 0.0.0.0 --port 8000
### Step 4 : TMUX to keep server running
sudo apt install tmux -y

tmux

uvicorn app.main:app --host 0.0.0.0 --port 8000
#### Press Ctrl + B, then D to detach

### Step 5 : nginx for prod (optional) (needs discussion)
Install: sudo apt install nginx certbot python3-certbot-nginx

Configure /etc/nginx/sites-available/yourdomain.com

Point domain to EC2 IP via A record

Use: sudo certbot --nginx -d yourdomain.com

