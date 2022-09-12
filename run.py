import os
import shutil
import numpy as np

images_path = os.getcwd()
images_path = images_path + "\Images"


def refresh_dir(path, name):
    try:
        shutil.rmtree(path + name)
    except Exception as e:
        print("Couldn't remove " + str(path) + str(name))
    finally:
        os.mkdir(path + name)


def do_splits(src, directory_given, class_idx):
    # 70, 15, 15 split
    allFileNames = os.listdir(images_path + directory_given)
    np.random.shuffle(allFileNames)
    train, test, validate = np.split(np.array(allFileNames),
                                     [int(len(allFileNames) * 0.7), int(len(allFileNames) * 0.85)])
    train_FileNames = [src + directory_given + "\\" + name for name in train.tolist()]
    val_FileNames = [src + directory_given + "\\" + name for name in validate.tolist()]
    test_FileNames = [src + directory_given + "\\" + name for name in test.tolist()]

    if directory_given == "\Bunnies-Base":
        # Copy-pasting images
        idx = 0
        for name in train_FileNames:
            shutil.copy(name, src + '\Bunnies-Train')
            os.rename(src + '\Bunnies-Train', src + '\Bunnies-Train' + str(class_idx) + "-" + str(idx))
            idx += 1

        idx = 0
        for name in val_FileNames:
            shutil.copy(name, src + '\Bunnies-Validate')
            os.rename(src + '\Bunnies-Validate', src + '\Bunnies-Validate' + str(class_idx) + '-' + str(idx))
            idx += 1

        idx = 0
        for name in test_FileNames:
            shutil.copy(name, src + '\Bunnies-Test')
            os.rename(src + '\Bunnies-Test', src + '\Bunnies-Test' + str(class_idx) + '-' + str(idx))
            idx += 1
    else:
        # Copy-pasting images
        idx = 0
        for name in train_FileNames:
            shutil.copy(name, src + '\Other-Train')
            os.rename(src + '\Other-Train', src + '\Other-Train' + str(class_idx) + '-' + str(idx))
            idx += 1

        idx = 0
        for name in val_FileNames:
            shutil.copy(name, src + '\Other-Validate')
            os.rename(src + '\Other-Validate', src + '\Other-Validate' + str(class_idx) + '-' + str(idx))
            idx += 1

        idx = 0
        for name in test_FileNames:
            shutil.copy(name, src + '\Other-Test')
            os.rename(src + '\Other-Test', src + '\Other-Test' + str(class_idx) + '-' + str(idx))
            idx += 1


refresh_dir(images_path, "\Bunnies-Train")
refresh_dir(images_path, "\Bunnies-Validate")
refresh_dir(images_path, "\Bunnies-Test")
refresh_dir(images_path, "\Other-Train")
refresh_dir(images_path, "\Other-Validate")
refresh_dir(images_path, "\Other-Test")

classes = ["\Bunnies-Base", "\Other-Base\\Human", "\Other-Base\\Nature-Background", "\Other-Base\\Text",
           "\Other-Base\\Dogs", "\Other-Base\\Cats", "\Other-Base\\Hamsters", "\Other-Base\\Suggestively-Sexual",
           "\Other-Base\\Suggestively-Violent", "\Other-Base\\Abstract-Background", "\Other-Base\\Empty-Cages",
           "\Other-Base\\Bunny-Drawings"]

class_idx = 0
for class_dir in classes:
    do_splits(images_path, class_dir, class_idx)

print("test")
