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


def do_splits(directory_given):
    # 70, 15, 15 split
    allFileNames = os.listdir(images_path + directory_given)
    np.random.shuffle(allFileNames)
    train, test, validate = np.split(np.array(allFileNames),
                                     [int(len(allFileNames) * 0.7), int(len(allFileNames) * 0.85)])
    return [train, test, validate]


refresh_dir(images_path, "\Bunnies-Train")
refresh_dir(images_path, "\Bunnies-Validate")
refresh_dir(images_path, "\Bunnies-Test")
refresh_dir(images_path, "\Other-Train")
refresh_dir(images_path, "\Other-Validate")
refresh_dir(images_path, "\Other-Test")

# bunny, 611
# human, 100
# nature background, 100
# text, 75
# dogs, 50
# cats, 50
# hamsters, 50
# suggestively sexual, 50
# suggestively violent, 50
# abstract background, 50
# empty cages, 25
# bunny drawings 11
