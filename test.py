import os
from threading import Thread

def lavalink():
  os.system("cd Lava && java -jar Lavalink.jar")
Thread(target=lavalink).start()
print("Hunter 87")
