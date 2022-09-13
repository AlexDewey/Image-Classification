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


# ===================================
# Refreshing directories
refresh_directories = ["\Bunnies-Train", "\Bunnies-Validate", "\Bunnies-Test", "\Other-Train", "\Other-Validate",
                       "\Other-Test"]
for ref_dir in refresh_directories:
    refresh_dir(images_path, ref_dir)

# ===================================
# Balancing and ordering classes
classes = ["\Bunnies-Base", "\Other-Base\\Human", "\Other-Base\\Nature-Background", "\Other-Base\\Text",
           "\Other-Base\\Dogs", "\Other-Base\\Cats", "\Other-Base\\Hamsters", "\Other-Base\\Suggestively-Sexual",
           "\Other-Base\\Suggestively-Violent", "\Other-Base\\Abstract-Background", "\Other-Base\\Empty-Cages",
           "\Other-Base\\Bunny-Drawings"]
class_idx = 0
for class_dir in classes:
    do_splits(images_path, class_dir, class_idx)
    class_idx += 1

bunny_test_len = len(os.listdir(images_path + "\Bunnies-Test"))
other_test_len = len(os.listdir(images_path + "\Other-Test"))
while bunny_test_len != other_test_len:
    if bunny_test_len > other_test_len:
        # put a test into bunny_train
        shutil.move(images_path + "\Bunnies-Test\\" + os.listdir(images_path + "\Bunnies-Test")[0], images_path + "\Bunnies-Train\\" + os.listdir(images_path + "\Bunnies-Test")[0])
    elif bunny_test_len < other_test_len:
        # put a other into other_train
        shutil.move(os.listdir(images_path + "\Other-Test\\" + images_path + "\Other-Test")[0], images_path + "\Other-Train\\")
    bunny_test_len = len(os.listdir(images_path + "\Bunnies-Test"))
    other_test_len = len(os.listdir(images_path + "\Other-Test"))

bunny_train_len = len(os.listdir(images_path + "\Bunnies-Train"))
other_train_len = len(os.listdir(images_path + "\Other-Train"))
while bunny_train_len != other_train_len:
    if bunny_train_len > other_train_len:
        # put a train into bunny_validate
        shutil.move(os.listdir(images_path + "\Bunnies-Train\\" + images_path + "\Bunnies-Train")[0], images_path + "\Bunnies-Validate\\")
    elif bunny_train_len < other_train_len:
        # put a other into other_validate
        shutil.move(os.listdir(images_path + "\Other-Train\\" + images_path + "\Other-Train")[0], images_path + "\Other-Validate\\")
    bunny_train_len = len(os.listdir(images_path + "\Bunnies-Train"))
    other_train_len = len(os.listdir(images_path + "\Other-Train"))

print("done")
