import yaml
from datetime import date
import os
import requests
from typing import Tuple


def load_env_variable():
    """
    Load env variables for local testing
    """
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass


def load_data() -> dict:
    """
    Reads yaml file with brithday and anniversary info and return the file in dict format

    Returns:
        _type_: _description_
    """
    try:
        file_name = os.getenv("YAML_FILE_NAME")
        with open(file_name, "r") as y:
            file_content = yaml.full_load(y)
    except FileNotFoundError:
        print(f"File with name {file_name} not found")
        os._exit(1)
    return file_content


def get_today_list(file_content: dict) -> Tuple[list, str]:
    """Reads the dict and return birthday and anniversary matching in list along with the date

    Returns:
        list: Matching entries for current date
        str: the Month and year e.g. January 14
    """
    today_month, today_date = date.today().strftime("%B-%-d").split("-")
    try:
        collected_details = file_content.get(today_month).get(int(today_date))
        return collected_details, f"{today_month}-{today_date}"
    except AttributeError:
        print(f'No entry found in yaml reference file for {today_month}-{today_date}\nExiting program."')
        os._exit(0)


def notify_discord(today_date: str, message_list: list):
    """Webhook call for Discord server

    Args:
        today_date (str): Today date to be sent in Discord message
        message_list (list): List of entries matching
    """
    discord_web_hook_url = os.getenv("DISCORD_WEBHOOK")
    message_str = "\n".join(message_list)
    headers = {"Content-Type": "application/json"}
    payload = {"content": f"Birthday & Anniversary reminder for {today_date} is {message_str}"}
    try:
        requests.post(discord_web_hook_url, headers=headers, json=payload)
        print("Message posted to discord successfully")
    except requests.exceptions.RequestException as err:
        print(f"Exception {err} receoved")


def main():
    """
    main program which is called on each run
    """
    if os.getenv("MODE") == None or os.getenv("MODE") != "pipeline":
        load_env_variable()
    file_content = load_data()
    collected_list, today_date = get_today_list(file_content)
    if collected_list:
        notify_discord(today_date, collected_list)
    else:
        print("No birthday or reminder found for today")


if __name__ == "__main__":
    main()
