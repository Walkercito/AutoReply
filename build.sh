python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
rm -f backend.zip
deactivate