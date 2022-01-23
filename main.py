import json
from os import listdir
from os.path import isfile, join

def process_filelist(pathtofiles, prefix = 't', solid = 10, hurtlevel = 0, enemy=0, collect = 0, food = 0, heart= 0):
    id = 0
    object = []
    sublist = []
    onlyfiles = [f for f in sorted(listdir(path)) if isfile(join(path, f))]
    last_prefix = onlyfiles[0][0]
    for x in onlyfiles:
        if (x[0] ==last_prefix):
            id += 1
        else:
            last_prefix = x[0]
            id = 0
        if(x.find('series')>0):
            if (x.find('series999')>0):
                object.append({"id": prefix + x[0] + str(id), "path": join(path, x), "solid": solid, \
                               "hurtlevel": hurtlevel, "enemy": enemy, "collect": collect, "food": food, \
                               "heart": heart, "series": True, "next": sublist})
                sublist = []
            else:
                sublist.append(join(path, x))
        else:
            object.append({"id": prefix + x[0] + str(id), "path": join(path, x),  "solid": solid, \
                               "hurtlevel": hurtlevel, "enemy": enemy, "collect": collect, "food": food, \
                                "heart": heart, "series": False, "next":"" })
    return(object)

objectlist = []
background_object = []
#generate background
background_object.append({"id":"level0", "path": "../LevelEditor/pngs/worlds/castle/background/Bright/Background.png"})
background_object.append({"id":"level1", "path": "../LevelEditor/pngs/worlds/castle/background/Bright/sky.png"})
background_object.append({"id":"level2", "path": "../LevelEditor/pngs/worlds/castle/background/Bright/trees.png"})
background_object.append({"id":"level3", "path": "../LevelEditor/pngs/worlds/castle/background/Bright/down.png"})
objectlist.append({"Level":"background", "Content": background_object})

#liquids
path = '../LevelEditor/pngs/worlds/castle/liquids/'
object = process_filelist(path, prefix = 'l', solid = 5, hurtlevel = 0, enemy=0, collect = 0, food = 0, heart= 0)
objectlist.append({"Level":"liquids", "Content": object})

#tiles
path = '../LevelEditor/pngs/worlds/castle/tiles/'
object = process_filelist(path, prefix = 't', solid = 10, hurtlevel = 0, enemy=0, collect = 0, food = 0, heart= 0)
objectlist.append({"Level":"tiles", "Content": object})


#objects
path = '../LevelEditor/pngs/worlds/castle/objects/'
object = process_filelist(path, prefix = 'o', solid = 0, hurtlevel = 0, enemy=0, collect = 0, food = 0, heart= 0)
objectlist.append({"Level":"objects", "Content": object})

#enemies
#path = '../LevelEditor/pngs/worlds/castle/enemies/'
#object = process_filelist(path)
#objectlist.append({"Level":"enemies", "Content": object})

#food

#potion

with open('../LevelEditor/pngs/level1.json', 'w',  encoding='utf-8') as JSONfile:
    json.dump(objectlist, JSONfile, ensure_ascii=False, indent=4)