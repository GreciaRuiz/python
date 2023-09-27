import os
import sys

so = os.name
plataforma = sys.platform;
if so == "nt":
    print("Tiene un SO Windows")
elif so == "posix" and plataforma == "darwin":    
    print("Tiene un SO Linux")
else:
    print("Tiene un SO MAC")


input()