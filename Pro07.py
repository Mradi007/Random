import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from adi64 import main
    main()
elif bit == '32bit':
    from adi32 import main
    main()
