import os
import cv2
import shutil
import zipfile

#---------------------------------
#           HOW TO USE:  ;D

#    press windows-key: type CMD and write:   pip install opencv-python
#    for mac idk download opencv however you do it on mac
#    
#    put the word file you want to edit the images of in your DOWNLOADS folder
#
#    enter the name of the word file (the one you put in downloads) OBS: REMEMBER (.docx) at the end
#    example : my file name is "nokling1.docx"

wordfilename = "nokling1.docx"

#    change IMG_SIZE (scale up/down) 100 = NO IMAGE CHANGE

IMG_SIZE_SCALING = 60

#    PRESS RUN! filene lagrer seg som UPDATED_IMAGES i downloads folderen din

#---------------------------------

def FindDownloadFolder():
    if os.name == "nt":
        DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"
    else:  # PORT: For linux/mac systems
        DOWNLOAD_FOLDER = f"{os.getenv('HOME')}/Downloads"
    return DOWNLOAD_FOLDER

def zipoutimages():

    PATHWORDFILE = f"{os.getenv('USERPROFILE')}\\Downloads\\{wordfilename}"

    archive = zipfile.ZipFile(PATHWORDFILE)
    for file in archive.filelist:
        if file.filename.startswith('word/media/') and file.file_size > 300000:
            archive.extract(file, path=FindDownloadFolder())

def make_new_img():

    try:
        shutil.rmtree(f"{os.getenv('USERPROFILE')}\\Downloads\\UPDATED_IMAGES")
    except Exception as e:
        print(f"No directory called UPDATED_IMAGES ERROR:{e}")

    PATHPHOTOS = f"{os.getenv('USERPROFILE')}\\Downloads\\word\\media"
    os.makedirs(f"{os.getenv('USERPROFILE')}\\Downloads\\UPDATED_IMAGES")
    newuploadfolder = (f"{os.getenv('USERPROFILE')}\\Downloads\\UPDATED_IMAGES")

    problemimages = []
    
    for counter,img in enumerate(os.listdir(PATHPHOTOS)):
        
        try:
            img_array = cv2.imread(os.path.join(PATHPHOTOS,img),cv2.IMREAD_UNCHANGED)

            width = int(img_array.shape[1] * IMG_SIZE_SCALING / 100)
            height = int(img_array.shape[0] * IMG_SIZE_SCALING / 100)
            dim = (width, height)

            new_img = cv2.resize(img_array, dim,interpolation = cv2.INTER_AREA)

            filename = f"{newuploadfolder}\{str(counter)}.jpg"
            cv2.imwrite(filename, new_img)

        except Exception as e:
            print(e)
            problemimages.append(os.path.join(PATHPHOTOS,img))
            pass

    print(f"number of images gone through = {counter} \n Images with problems")
    for problem in problemimages:
        print(f"problem image (check them out) {problem}")

    try:
        shutil.rmtree(f"{os.getenv('USERPROFILE')}\\Downloads\\word")
    except Exception as e:
        print(f"No directory called word: ERROR:{e}")

#files run here!

zipoutimages()

make_new_img()




