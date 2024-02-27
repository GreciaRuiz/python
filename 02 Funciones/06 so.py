import os
import sys

so = os.name
plataforma = sys.platform;
if so == "nt":
    print("Tiene un SO Windows")
elif so == "posix" and plataforma == "linux":    
    print("Tiene un SO Linux")
else:
    print(plataforma)


input()