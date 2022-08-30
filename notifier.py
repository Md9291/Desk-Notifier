'''
Desktop Notifier in Python
Author: MOHAMMAD YUNUS
'''

#import the necessary module!
from plyer import notification


#specify the parameters
title = 'Hello Guys '

message= 'How are you Today?, Take care!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)