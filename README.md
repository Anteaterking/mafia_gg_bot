# mafia_gg_bot
Bot for Mafia.gg to facilitate semi-closed setups, etc. Written with Selenium for Python

#### Initial Setup

1. Install `conda`: https://docs.anaconda.com/anaconda/install/
2. (Optional) Install `PyCharm` IDE: https://www.jetbrains.com/help/pycharm/installation-guide.html
3. Install `pre-commit`: https://pre-commit.com/#install
4. In IDE, set `src` as the `Sources Root` of your project.


#### Pre-Commit
This repo is configured to use pre-commit to manage code hygiene.  Please configure pre-commit before pushing code to
origin.

Instructions: (https://pre-commit.com/)
1. Install: `brew install pre-commit` or `conda install -c conda-forge pre-commit` or `pip install pre-commit`
2. (Optional) Setup automatic commit hook: `pre-commit install`
3. Manual lint: `pre-commit run --all-files` (multiple times until all steps pass)

#### Build
Run `./scripts/build.sh` to build the prod environment.
Run `./scripts/build-dev.sh` to build the dev/test environment.

Some code for Mafia_Semi_Bot v0.5 by Anteaterking

Requirements: Have Python3 on your computer, the selenium python package, and "chromedriver" (https://sites.google.com/a/chromium.org/chromedriver/downloads)

BEFORE RUNNING:

Open the parameter file and fill in the parameters I left blank (username/password for your bot's mafia.gg account) and consider changing some of the parameters (unless you want me to be the only privileged user of *your* bot).

Make sure this parameter file, chromedriver, and the mafia_bot.py file are all in the same folder or put an explicit path to chromedriver in the parameters.

TO USE:

Just run "python mafia_bot.py" in a terminal from the folder it's contained in!

This will open up a chromedriver browser, attempt to login to mafia.gg, and automatically open a room. From this point anyone can interact with the bot through a limited number of commands (with some commands such as !setup and !semi being restricted to just privileged users). Look through the options in parameters for what mode you want to run it in: unlisted/listed, privileged, abandon or stay in same room, etc. For example, if you just want the bot to make janitorial setups all day long, set listed to 1 and abandon to 1 with a setup text file with just Janitorial in it. That seems like a waste though.

Currently, games will inherit the last properties in terms of decks, timers, whether roles are hidden, whether setup is hidden, etc. so you'll want to set those to the right things before letting it lose.


TO DO

1. Commands for changing those properties
2. Add other useful commands that people might want
3. More bug testing
4. Right now everything is very dependent on the UI staying very similar for things like button placement, etc. But I just learned selenium today so...to be improved.
5. Xinde requested being able to read in a pastebin of setups.
6. 10% of the time my trick for getting login correct doesn't work because of inconsistent ids. This ### can be fixed by just rerunning but would be nice to fix.
7. Setup conda env -Xinde
8. Add typehints -Xinde
9. Setup pytest framework -Xinde

If you have comments, bugs, or suggestions, let me know!


VERSION NOTES:

v0.5 : 12/6/2020 Initial commit.
