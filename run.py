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
bunny_train, bunny_test, bunny_validate = do_splits("\Bunnies-Base")
# human, 100
human_train, human_test, human_validate = do_splits("\Other-Base\\Human")
# nature background, 100
nature_train, nature_test, nature_validate = do_splits("\Other-Base\\Nature-Background")
# text, 75
text_train, text_test, text_validate = do_splits("\Other-Base\\Text")
# dogs, 50
dogs_train, dogs_text, dogs_validate = do_splits("\Other-Base\\Dogs")
# cats, 50
cats_train, cats_text, cats_validate = do_splits("\Other-Base\\Cats")
# hamsters, 50
hamsters_train, hamsters_text, hamsters_validate = do_splits("\Other-Base\\Hamsters")
# suggestively sexual, 50
ss_train, ss_text, ss_validate = do_splits("\Other-Base\\Suggestively-Sexual")
# suggestively violent, 50
sv_train, sv_text, sv_validate = do_splits("\Other-Base\\Suggestively-Violent")
# abstract background, 50
ab_train, ab_text, ab_validate = do_splits("\Other-Base\\Abstract-Background")
# empty cages, 25
ec_train, ec_text, ec_validate = do_splits("\Other-Base\\Empty-Cages")
# bunny drawings 11
bd_train, bd_text, bd_validate = do_splits("\Other-Base\\Bunny-Drawings")

print("test")