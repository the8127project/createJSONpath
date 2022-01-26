import json
from os import listdir
from os.path import isfile, join

def create_copy_command():
    path = '../LevelEditor/pngs/characters/good'
    onlydir = [f for f in sorted(listdir(path)) if not isfile(join(path, f))]
    for i in onlydir:

        path2 = join(path, i)
        onlyfiles = [f for f in sorted(listdir(path2)) if isfile(join(path2, f))]
        # print(onlyfiles)
        series999 = 0
        for x in onlyfiles:
            position = 'none'
            if (x.lower().find('attack') >= 0): position = 'attack'
            if (x.lower().find('stone') >= 0): position = 'stone'
            if (x.lower().find('anger') >= 0): position = 'anger'
            if (x.lower().find('flight') >= 0): position = 'flight'
            if (x.lower().find('jump') >= 0): position = 'jump'
            if (x.lower().find('high_jump') >= 0): position = 'high_jump'
            if (x.lower().find('run') >= 0): position = 'run'
            if (x.lower().find('run+attack') >= 0): position = 'run+attack'
            if (x.lower().find('walk+attack') >= 0): position = 'walk+attack'
            if (x.lower().find('blade') >= 0): position = 'blade'
            if (x.lower().find('fire') >= 0): position = 'fire'
            if (x.lower().find('lightning') >= 0): position = 'lightning'
            if (x.lower().find('run') >= 0): position = 'run'
            if (x.lower().find('walk') >= 0): position = 'walk'
            if (x.lower().find('death') >= 0): position = 'death'
            if (x.lower().find('hurt') >= 0): position = 'hurt'
            if (x.lower().find('idle') >= 0): position = 'xidle'
            if (x.lower().find('explosion') >= 0): position = 'explosion'
            if (x.lower().find('web') >= 0): position = 'web'
            #x = x.lower().replace('idle', 'xidle')

            if (position != 'none'):

                # print(position, x.lower(), x.lower().find('walk') )
                if (position == 'xidle' and x[-5:-4] == '1'):
                    print('cp ', join(path2, x), path + '/' + i.lower() + '_'+position + '_' + x.lower()[:-5] + '_series999' + '.png')
                    series999 = 1
                else:
                    print('cp ', join(path2, x), path + '/' + i.lower() + '_'+position + '_'  + x.lower()[:-5] + '_series00' + x[-5:-4] + '.png')
                    backup = 'cp ' +  join(path2, x) + ' ' + path + '/' + i.lower() + '_' +position + '_' + x.lower()[:-5] + '_series999' + '.png'
        if (series999 == 0):
                print(backup)

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
                position = 'none'
                if (x.lower().find('attack') >= 0): position = 'attack'
                if (x.lower().find('stone') >= 0): position = 'stone'
                if (x.lower().find('anger') >= 0): position = 'anger'
                if (x.lower().find('flight') >= 0): position = 'flight'
                if (x.lower().find('jump') >= 0): position = 'jump'
                if (x.lower().find('high_jump') >= 0): position = 'high_jump'
                if (x.lower().find('run') >= 0): position = 'run'
                if (x.lower().find('run+attack') >= 0): position = 'run+attack'
                if (x.lower().find('walk+attack') >= 0): position = 'walk+attack'
                if (x.lower().find('blade') >= 0): position = 'blade'
                if (x.lower().find('fire') >= 0): position = 'fire'
                if (x.lower().find('lightning') >= 0): position = 'lightning'
                if (x.lower().find('run') >= 0): position = 'run'
                if (x.lower().find('walk') >= 0): position = 'walk'
                if (x.lower().find('death') >= 0): position = 'death'
                if (x.lower().find('hurt') >= 0): position = 'hurt'
                if (x.lower().find('idle') >= 0): position = 'xidle'
                if (x.lower().find('explosion') >= 0): position = 'explosion'
                if (x.lower().find('web') >= 0): position = 'web'

                sublist.append({'position': position, 'path': join(path, x)})
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
path = '../LevelEditor/pngs/characters/evil/'
object = process_filelist(path, prefix = 'e', solid = 0, hurtlevel = 5, enemy=1, collect = 0, food = 0, heart= 0)
objectlist.append({"Level":"evil", "Content": object})

#good
path = '../LevelEditor/pngs/characters/good/'
object = process_filelist(path, prefix = 'e', solid = 0, hurtlevel = 5, enemy=0, collect = 0, food = 0, heart= 0)
objectlist.append({"Level":"good", "Content": object})

#path = '../LevelEditor/pngs/worlds/castle/enemies/'
#object = process_filelist(path)
#objectlist.append({"Level":"enemies", "Content": object})

#food
#create_copy_command()
#potion

with open('../LevelEditor/pngs/level1.json', 'w',  encoding='utf-8') as JSONfile:
    json.dump(objectlist, JSONfile, ensure_ascii=False, indent=4)