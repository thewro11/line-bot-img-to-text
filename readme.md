# Line Bot with Image to Text Recognition and Detection with OpenCV and Tesseract

## Set Up
1. Before installing Python Modules, it is recommended to create and use virtual environments for this project, by using the following command:
```ps
# Windows
py -3 -m venv .venv
.venv\Scripts\activate
```

```bash
# MacOS
python3 -m venv .venv
. .venv/bin/activate
```

2. Run the following command to install necessary Python Modules
```bash
pip install -r requirements.txt
```

3. Follow the guide and install [tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html/).

4. Duplicate the `config.py.example` and rename it to `config.py`.
```ps
# Windows
copy config.py.example config.py
```

```bash
# MacOS
cp config.py.example config.py
```

5. Put your Line Bot's `CHANNEL_ACCESS_TOKEN` and `CHANNEL_SECRET`, and `PATH_TO_TESSERACT` command (e.g. `/opt/homebrew/Cellar/tesseract/5.3.3/bin/tesseract`) in the config file.

6. Run the following command to start the application
```bash
flask run --debug --host 0.0.0.0 --port 5001
```

### Run NGROK
To connect this Web API to Line Bot, you need to hook this Web API to Line's Webhook. To tunnel your local address to public address, you need to install [ngrok](https://ngrok.com/) and run the following command to expose this application's port to public.
```bash
ngrok http 5001
```

### Hook this Web API application to Line's Webhook
Navigate to [Line Developer Console Website](https://developers.line.biz/console) and follow their instructions to build Line Bot Official and connect the webhook. 
