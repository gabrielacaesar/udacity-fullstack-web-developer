import time
import webbrowser

starttime=time.time()
while True:
  webbrowser.open("https://www.youtube.com/watch?v=u_UC6kAyK4g")
  time.sleep(120.0 - ((time.time() - starttime) % 120.0))