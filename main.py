
from ui import MainWindow
import subprocess

# Install requirements.txt
try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
except:
    print('you may want to update the requirements.txt')







open_window = MainWindow()



open_window.mainloop()




