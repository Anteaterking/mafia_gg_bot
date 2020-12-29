import random
import time

from selenium import webdriver

from config import parameter_file as pf

###############################
### Global Variables
current_afk_requests = 0

payload_command_list = {"!setup", "!semi"}
naked_command_list = {"!spam", "!start", "!semihelp", "!possibilities", "!afk"}

###############################


def chat(driver, message):
    chat_bar = driver.find_element_by_xpath("""//input[@placeholder="Chat with the group…"]""")
    chat_bar.send_keys(message + "\n")


def change_setup_code(driver, code):
    setup_options = driver.find_elements_by_class_name("button")[2]
    setup_options.click()
    try:
        setup_code = driver.find_element_by_xpath("""//input[@placeholder="Paste setup code…"]""")
        setup_code.clear()
        setup_code.send_keys(code + "\n")
    except:
        chat(driver, "Invalid setup code!")
    return ()


def start_up(path, url):
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(5)
    driver.get(url)
    return driver


def log_in(driver, username, password):
    account_box = driver.find_element_by_class_name("account-box")
    user_entry = account_box.find_elements_by_class_name("account-input")[0]
    outerHTML = user_entry.get_attribute("outerHTML")
    id = outerHTML[outerHTML.index("label for=") + 11 :][:18]
    login = driver.find_element_by_id(id)
    login.send_keys(username)
    time.sleep(0.5)
    login = driver.find_element_by_id(id[:-1] + "2")
    login.send_keys(password)
    login.send_keys("\n")
    return ()


def start_room(driver, game_name="", listed=0):
    if listed == 0:
        unlisted = driver.find_element_by_class_name("checkbox")
        unlisted.click()
    time.sleep(0.5)
    room_name_box = driver.find_elements_by_xpath("""//input[@type="text"]""")[1]
    if game_name != "":
        room_name_box.clear()
        room_name_box.send_keys(game_name)
    time.sleep(0.5)
    submit = driver.find_element_by_xpath("""//button[@type="submit"]""")
    submit.click()
    time.sleep(0.5)
    chat(driver, "Bot is ready!")
    driver.find_elements_by_class_name("button")[0].click()
    if pf.ABANDON == 1 and pf.PRIVILEGE_REQUIRED == 1:
        chat(
            driver,
            "I've gone rogue and am hosting games and abandoning them! Type !possiblities to see the different setups that I am choosing between (and hiding the results). Type !start once there are enough players and I'll start. Three !afk will initiate an afk check. Welcome to semi-closed fun! (Please report players who should be blacklisted to whomever is running this bot)",
        )
        codes, descriptions = unpack_setups()
        run_command(driver, "!semi", " ".join(codes))
    return ()


def run_command(driver, command, payload=""):
    if command == "!setup":
        change_setup_code(driver, payload)
    if command == "!spam":
        chat(driver, """>=( I'm the parity cop""")
    if command == "!start":
        start_game = driver.find_elements_by_class_name("button")[3]
        if start_game.is_enabled():
            chat(driver, "Game starting, good luck!")
            time.sleep(0.5)
            start_game.click()
            if pf.ABANDON == 0:
                wait_until_next_game(driver)
            else:
                driver.get(r"https://mafia.gg")
                start_room(driver, listed=1)  # You can't have unlisted abandoned games.
        else:
            chat(driver, "Not enough players!")
    if command == "!semihelp":
        chat(driver, """type '!semi = setup1 setup2 setup3' etc.""")
    if command == "!semi":
        setup_choices = payload.split(" ")
        choice = random.randint(0, len(setup_choices) - 1)
        change_setup_code(driver, setup_choices[choice])
    if command == "!possibilities":
        if pf.SETUP_PATH == "":
            chat(driver, "This isn't a possibilities configuration, partner!")
            return ()
        codes, descriptions = unpack_setups()
        for i in descriptions:
            time.sleep(1.1)
            chat(driver, i)
    if command == "!afk":
        global current_afk_requests
        current_afk_requests += 1
        if current_afk_requests >= 3:
            current_afk_requests = 0
            driver.find_elements_by_class_name("button")[1].click()
        else:
            chat(driver, "Need " + str((3 - current_afk_requests)) + " more !afk commands!")
    return ()


def wait_until_next_game(driver):
    while True:
        if len(driver.find_elements_by_class_name("game-chronicle-sys-message-text")) >= 3:
            data_messages = [i.get_attribute("data-text") for i in driver.find_elements_by_class_name("game-chronicle-sys-message-text")]
            if "The game has ended." in data_messages:
                chat(driver, "The game is over!")
                chat(driver, "Congrats to " + [j for j in data_messages if "Winning teams: " in j][0].split(":")[1] + " team(s) for the win!")
                time.sleep(1)
                chat(driver, "Starting new lobby in 10 seconds")
                time.sleep(10)
                driver.find_elements_by_class_name("button")[1].click()
                driver.find_elements_by_class_name("button")[-1].click()
                time.sleep(3)
                chat(driver, "Bot is ready!")
                return ()


def unpack_setups():
    with open(pf.SETUP_PATH, "r") as f:
        setup_blob = f.read()
    setups = setup_blob.split("\n")
    codes = []
    descriptions = []
    for i in setups:
        if ":" in i:
            codes.append(i.split(":")[0])
            descriptions.append(i.split(":")[1])
    return (codes, descriptions)


###################


# actual start

driver = start_up(pf.PATH, pf.URL)
try:
    log_in(driver, pf.USERNAME, pf.PASSWORD)
except:
    driver.refresh()
    log_in(driver, pf.USERNAME, pf.PASSWORD)
time.sleep(0.5)
start_room(driver, pf.GAME_NAME, pf.LISTED)


while True:
    current_text = "test"
    current_user = "user"
    while current_text[0] != "!":
        current_text = driver.find_elements_by_class_name("game-chronicle-chat-text")[-1].text
        current_user = driver.find_elements_by_class_name("game-chronicle-name")[-1].text
    trim = current_text[: (current_text + " ").index(" ")]
    chat(driver, "Executing command " + trim)
    time.sleep(0.5)
    if trim in naked_command_list:
        run_command(driver, current_text[: (current_text + " ").index(" ")], "")
    elif trim in payload_command_list and " = " in current_text:
        if current_user in pf.PRIVILEGED_USERS or pf.PRIVILEGE_REQUIRED != 1:
            command = current_text.split(" = ")[0]
            payload = current_text.split(" = ")[1]
            run_command(driver, command, payload)
        else:
            chat(driver, "You aren't cool enough to use that command")
    else:
        chat(driver, "Check syntax!")
