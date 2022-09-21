import os
import shutil

def DELETE_ALL():
    try:
        shutil.rmtree(f"{os.getenv('USERPROFILE')}\\Downloads\\UPDATED_IMAGES")
    except Exception as e:
        print(f"No directory called UPDATED_IMAGES ERROR:{e}")

    try:
        shutil.rmtree(f"{os.getenv('USERPROFILE')}\\Downloads\\word")
    except Exception as e:
        print(f"No directory called word: ERROR:{e}")
        
DELETE_ALL()




