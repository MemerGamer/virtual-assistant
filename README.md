# virtual-assistant

## Installation
`pip install -r requirements.txt` - Installs all the required packages
### Manual installation for windows users
### Dependecies you need

| Packages | Usage |
|---|---|
| `pip install speechRecognition`  | For the assistant to listen to our voice/speech |
| `pip install pyttsx3` |  For the assistant to speak, text to speech |
| `pip install pywhatkit` | For advance control on browser |
| `pip install wikipedia` | To get wikipedia data |
| `pip install pyjokes` | To get funny jokes |


### For GNU/Linux users
Make sure to use `pip3`, because in linux `pip` refers for `python2` and `pip3` refers to `python3`.

| Packages | Usage |
|---|---|
| `pip3 install pyAudio` | for python audio |
| `pip3 install portAudio` | for python audio |


## Usage
After installing the required packages you should start the `main.py` in your terminal (for example cmd, powershell or st, kitty, etc)

After starting the application, in your terminal should appear a `listening...` message.
When you see that message you could say the keyword `Alex` and after that a command.

### Currently available commands:
| Commands | What it does |
|---|---|
| `play` < title > | Alex plays < title > on YouTube |
| tell me the `time` | Alex tells you the current time |
| `who is` < name > | Alex tells you information about < name > |
| `what is` < name > | Alex tells you information about < name > |
| tell me a `joke` | Alex tells you a joke |
| `open` < name > | Alex opens < name > (Currently only youtube & google is available) |

NOTE: As long as you have the keywords: `play` , `time`, `who is`, `what is`, `joke` & `open` in your command Alex will run the corressponding functions.

#### Issues
If you encounter any problems feel free to open a new issue. Before that check other closed issues and check if your issue matches with any older issues.
