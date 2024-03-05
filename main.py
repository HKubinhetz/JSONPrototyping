# -------------------------------------------- Imports --------------------------------------------
import json
import time
import os.path


# -------------------------------------------- Functions --------------------------------------------
def save_cookies(path, cookies):
    with open(path + "/config/cookies.json", 'w') as file:
        json.dump(cookies, file)


def validate_cookies(path):
    # Defines if cookies are valid by checking if there was a recent execution.
    # The current time is recorded on a json file and used for this endeavor.
    # Returns <True> if cookies are still fresh (max 15 minutes old);
    # Returns <False> otherwise.

    filecheck = os.path.isfile(path + "/config/lastrun.json")
    timedelta = 0

    if filecheck:
        # If file exists, calculations are made and the new time is saved.
        with open(path + "/config/lastrun.json", 'r+') as jsonfile:

            # Part 1 - Read file and calculate time since last execution
            json_contents = jsonfile.read()
            json_data = json.loads(json_contents)
            lastrun = json_data['lastrun']
            timedelta = time.time() - lastrun

            # Part 2 - Clear file contents and record current time
            jsonfile.seek(0)
            jsonfile.truncate()
            data = {'lastrun': time.time()}
            json.dump(data, jsonfile)

            # Cookie is valid for 900 seconds, or 15 minutes.
            if timedelta < 900:
                return True
            else:
                return False

    if not filecheck:
        # If file doesn't exist, creates a new one.
        # Current time is recorded and function returns <False> to its caller.

        data = {'lastrun': time.time()}
        with open(path + "/config/lastrun.json", 'w') as jsonfile:
            json.dump(data, jsonfile)
        return False


