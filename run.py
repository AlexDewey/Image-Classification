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

    splits = [train_FileNames, val_FileNames, test_FileNames]

    if directory_given == "\Bunnies-Base":
        directories = ["\Bunnies-Train", "\Bunnies-Validate", "\Bunnies-Test"]
    else:
        directories = ["\Other-Train", "\Other-Validate", "\Other-Test"]

    for split_index, directory in enumerate(directories):
        split = splits[split_index]
        idx = 0
        for name in split:
            failed_naming = True
            while failed_naming:
                try:
                    shutil.copy(name, src + directory)
                    os.rename(src + directory + '\\' + name.rsplit('\\', 1)[-1],
                              src + directory + '\\' + str(class_idx) + "-" + str(idx) + name.rsplit('\\', 1)[-1])
                    failed_naming = False
                except:
                    idx += 1
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

print("done")










# Code for renaming values in case there's another blunder handling data

# values = ["Hamsters", "Human", "Nature-Background", "Suggestively-Sexual", "Suggestively-Violent", "Text"]
#
# for value in values:
#     allFileNames = os.listdir(images_path + "\Other-Base\\" + value + "\\")
#     for file_name in allFileNames:
#         old_name = file_name
#         for letter in range(len(file_name) - 1, 0, -1):
#             print(file_name[letter])
#             if file_name[letter] != 'g':
#                 file_name = file_name[:-1]
#                 print("popped")
#             else:
#                 print("found end!")
#                 os.rename(images_path + "\Other-Base\\" + value + "\\" + old_name,
#                           images_path + "\Other-Base\\" + value + "\\" + file_name)
#                 break


