from PIL import Image
import glob

i1 = Image.open("datasets/101_2_1.jpg")

path = "datasets/*"
# dir_list = os.listdir(path)
list_1=[]
# for x in os.listdir(path):
for x in glob.iglob(path):
    i2 = Image.open(x)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = i1.size[0] * i1.size[1] * 3
    diff =(dif / 255.0 * 100) / ncomponents
    g = 100 - diff
    # print ("Difference :", diff)
    ans = float("{:.2f}".format(g))
    print ("Matches: ", ans,"%")