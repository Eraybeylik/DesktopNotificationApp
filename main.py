from plyer import notification

import time


while(True):
    notification.notify(
        title = "Reminder to take a brake",
        message = '''Drink water, take a walk''',
        timeout = 60
    )

    time.sleep(60*60)