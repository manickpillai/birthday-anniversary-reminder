### Birthday and Anniversary Reminder

A python program which pulls yaml file from a private repo and sends notification to a personal discord server for birthday or anniversary on current day.



#### Technology demostrated
- Python code to read yaml file for current day and construct the json payload for Discord notification
- Pulling file from a private repo using PAT (personal access tokens)
- Webhook by calling a discord server
- Public Docker image hosted
- Github actions workflow to run at midnight everyday

#### To run locally
- Clone the repo
- Create a yaml file of the below format and pass the file name to env variable to `YAML_FILE_NAME`
```yaml
January:
  1:
    - Ironman bday
  5:
    - John snow bday
    - Neo and Trinity Anniversary
```
- Create a discord webhook and update env variable `DISCORD_WEBHOOK`
- Required python dependencies are `requests` and `pyyaml` these are not included as public [docker image](https://hub.docker.com/repository/docker/manickpillai/manick-python/general) is used 