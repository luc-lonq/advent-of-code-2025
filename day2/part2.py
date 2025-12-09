invalid_ids = []
txt = ""

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            txt += l

ranges = txt.split(",")
for r in ranges:
    n1, n2 = r.split("-")
    n1 = int(n1)
    n2 = int(n2)
    
    for i in range(n1, n2 + 1):
        i_str = str(i)
        #print("=====")
        #print("i: " + i_str)
        
        for j in range(len(i_str)//2):
            if len(i_str) % (j+1) == 0:
                is_invalid = True
                test_str = i_str[j+1:]
                #print("test_str: " + test_str)
                patern = i_str[:j+1]
                #print("patern: " + patern)
                
                while test_str != "":
                    if test_str[:j+1] != patern:
                        is_invalid = False
                        break
                    else:
                        test_str = test_str[j+1:]
                
                if is_invalid:
                    #print("found invalid id: " + i_str)
                    invalid_ids.append(i)
                    break

total = 0
for invalid_id in invalid_ids:
    total += invalid_id
print(total)
