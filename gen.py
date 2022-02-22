from PIL import Image
import itertools
import glob

#Trait Lists
bg_list = []
body_list = []
cig_list = []
chain_list = [0]
hat_list = [0]
smoke_list = []

#Load in trait images
for filename in glob.glob('images/bg/*.png'):
    im=Image.open(filename)
    bg_list.append(im)

for filename in glob.glob('images/body/*.png'):
    im=Image.open(filename)
    body_list.append(im)

for filename in glob.glob('images/chain/*.png'):
    im=Image.open(filename)
    chain_list.append(im)

for filename in glob.glob('images/cig/*.png'):
    im=Image.open(filename)
    cig_list.append(im)

for filename in glob.glob('images/hats/*.png'):
    im=Image.open(filename)
    hat_list.append(im)

for filename in glob.glob('images/smoke/*.png'):
    im=Image.open(filename)
    smoke_list.append(im)

#Create a master list and calculate every combination
main_list = [bg_list, body_list, cig_list, chain_list, hat_list, smoke_list]

main_list = itertools.product(*main_list)

output_list = []

output_counter = 0

#Generate images for every combination
for i in main_list:
    counter = 0
    prev_x = Image.new("RGBA", (1255, 1153))
    for x in i: 
        if x != 0:
            prev_x.paste(x, (0,0), mask = x)
        if counter == 5:
            prev_x.save("images/output/" + str(output_counter) +".png")
        counter += 1
    output_counter += 1
