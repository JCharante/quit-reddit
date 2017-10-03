# quit-reddit
Overwrite your comment history with a random line from Tiel la Mondo Iras

# Setup

## Create Reddit Script Credentials

Go [here](https://www.reddit.com/prefs/apps) and create a script app.
The redirect URI and about can be anything.


## Environmental Variables

```bash
$ export client_id=REDDIT_SCRIPT_CLIENT_ID
$ export client_sercet=REDDIT_SCRIPT_CLIENT_SECRET
$ export password=YOUR_REDDIT_PASSWORD
$ export user_agent="User Agent"
$ export username=YOUR_REDDIT_USERNAME
```

# Running

```bash
$ python3.6 run.py
```
