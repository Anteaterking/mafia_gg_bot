######## USER PREFERENCES ######
### Path to chromedriver

PATH = r'../chromedriver.exe'
URL = r'https://mafia.gg/login'

### Path to txt file with setups. These should be in form <setup code>:<description> on each line.
### Turn blank if you aren't using !possibilities

SETUP_PATH = r'../setups.txt'

### mafia.gg username/password for the bot

USERNAME = 'YOUR BOT USERNAME HERE'
PASSWORD = 'YOUR BOT PASSWORD HERE'

### What you want the lobby name to be

GAME_NAME = 'Semi-Closed Bot! by ' + USERNAME

### Set privileged users who can send the payload commands (changing setups,e.g.)
### Or set privilege_required to 0. I would make sure the bot is privileged probably.

PRIVILEGED_USERS = {"Anteaterking","CLWNDRGN"}
PRIVILEGE_REQUIRED = 1

### If you want the game listed or not, by default it is unlisted.

LISTED = 0

### If you want the bot to abandon a game after game start and start a new room, change this to 1. If you
### use abandon mode, you should make a setups.txt file even if you want the only option to be the same
### setup so that people at least get the helpful bot abandon start text.

ABANDON = 0
