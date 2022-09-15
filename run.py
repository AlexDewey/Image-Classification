import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

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
    allFileNames = os.listdir(images_path + directory_given)
    allFileNames = [src + directory_given + "\\" + name for name in allFileNames]
    directory = "\Other-Usable"

    idx = 0
    for name in allFileNames:
        failed_naming = True
        while failed_naming:
            try:
                shutil.copy(name, src + directory)
                os.rename(src + directory + "\\" + name.rsplit('||', 1)[-1],
                          src + directory + '\\' + str(class_idx) + "-" + str(idx) + name.rsplit('\\', 1)[-1])
                failed_naming = False
            except:
                idx += 1
            idx += 1

    # def do_splits(src, directory_given, class_idx):
    #     # 70, 15, 15 split
    #     allFileNames = os.listdir(images_path + directory_given)
    #     np.random.shuffle(allFileNames)
    #     train, test, validate = np.split(np.array(allFileNames),
    #                                      [int(len(allFileNames) * 0.7), int(len(allFileNames) * 0.85)])
    #     train_FileNames = [src + directory_given + "\\" + name for name in train.tolist()]
    #     val_FileNames = [src + directory_given + "\\" + name for name in validate.tolist()]
    #     test_FileNames = [src + directory_given + "\\" + name for name in test.tolist()]
    #
    #     splits = [train_FileNames, val_FileNames, test_FileNames]
    #
    #     if directory_given == "\Bunnies-Base":
    #         directories = ["\Bunnies-Train", "\Bunnies-Validate", "\Bunnies-Test"]
    #     else:
    #         directories = ["\Other-Train", "\Other-Validate", "\Other-Test"]
    #
    #     for split_index, directory in enumerate(directories):
    #         split = splits[split_index]
    #         idx = 0
    #         for name in split:
    #             failed_naming = True
    #             while failed_naming:
    #                 try:
    #                     shutil.copy(name, src + directory)
    #                     os.rename(src + directory + '\\' + name.rsplit('\\', 1)[-1],
    #                               src + directory + '\\' + str(class_idx) + "-" + str(idx) + name.rsplit('\\', 1)[-1])
    #                     failed_naming = False
    #                 except:
    #                     idx += 1
    #             idx += 1

# ===================================
# Refreshing directories
refresh_directories = ["\Other-Usable"]
for ref_dir in refresh_directories:
    refresh_dir(images_path, ref_dir)

# ===================================
# Balancing and ordering classes
classes = ["\Other-Base\\Human", "\Other-Base\\Nature-Background", "\Other-Base\\Text", "\Other-Base\\Dogs",
           "\Other-Base\\Cats", "\Other-Base\\Hamsters", "\Other-Base\\Suggestively-Sexual",
           "\Other-Base\\Suggestively-Violent", "\Other-Base\\Abstract-Background", "\Other-Base\\Empty-Cages",
           "\Other-Base\\Bunny-Drawings"]
class_idx = 0
for class_dir in classes:
    do_splits(images_path, class_dir, class_idx)
    class_idx += 1

# ===================================

batch_size = 32
img_height = 180
img_width = 180

print(images_path + "\Bunnies-Train")

bunny_train_dir = tf.keras.utils.image_dataset_from_directory(
    images_path + "\Bunnies-Train",
    image_size=(img_height, img_width),
    batch_size=batch_size
)

plt.figure(figsize=(10, 10))
for images, labels in bunny_train_dir.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title("bunnies :D")
        plt.axis("off")



print("done")
