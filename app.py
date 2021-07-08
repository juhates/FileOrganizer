from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

# run pip install watchdog
username = "juhat"
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(track_folder):
            if filename == "desktop.ini":
                return
                
            print(filename)
            src = track_folder + "/" + filename
            new_destination = destination_folder + "/" + filename
            # move file
            print("Moving file: " + filename + " to " + new_destination)
            os.rename(src, new_destination)

track_folder = "C:/Users/" + username + "/Desktop/"
destination_folder = "C:/Users/" + username + "/Downloads/"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, track_folder, recursive=True)
observer.start()
 
try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop
observer.join()
