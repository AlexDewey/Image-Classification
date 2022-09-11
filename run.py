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


def do_splits(src, directory_given):
    # 70, 15, 15 split
    allFileNames = os.listdir(images_path + directory_given)
    np.random.shuffle(allFileNames)
    train, test, validate = np.split(np.array(allFileNames),
                                     [int(len(allFileNames) * 0.7), int(len(allFileNames) * 0.85)])
    train_FileNames = [src + directory_given + "\\" + name for name in train.tolist()]
    val_FileNames = [src + directory_given + "\\" + name for name in validate.tolist()]
    test_FileNames = [src + directory_given + "\\" + name for name in test.tolist()]

    # Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, src + '/train//' + cls)

    for name in val_FileNames:
        shutil.copy(name, src + '/val//' + cls)

    for name in test_FileNames:
        shutil.copy(name, src + '/test//' + cls)
    return [train_FileNames, test_FileNames, val_FileNames]


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

for class_dir in classes:
    do_splits(images_path, class_dir)

print("test")