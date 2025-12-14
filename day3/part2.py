total = 0
false_numbers = 0

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            nb_max = []
            nb_i = []
            for i in range(12):
                str_test = l[nb_i[-1] + 1 if nb_i else 0:len(l)-12+i]
                #print("str_test: " + str(str_test))
                #print("nb_max: " + str(nb_max))
                #print("nb_i: " + str(nb_i))
                max_in_loop = 0
                idx_in_loop = 0
                for idx, x in enumerate(str_test):
                    c = int(x)
                    if c > max_in_loop and idx + (nb_i[-1]+1 if nb_i else 0) + 1 not in nb_i:
                        max_in_loop = c
                        idx_in_loop = idx + (nb_i[-1]+1 if nb_i else 0)
                    #print("index: " + str(idx + (nb_i[-1]+1 if nb_i else 0)) + " i: " + str(i) + " max_in_loop: " + str(max_in_loop))

                if max_in_loop == 0:
                    false_numbers += 1
                nb_max.append(max_in_loop)
                nb_i.append(idx_in_loop)
                #print("max_in_loop: " + str(max_in_loop) + " idx_in_loop: " + str(idx_in_loop) + " nb_max: " + str(nb_max))

            number = sum(n * (10 ** (11 - idx)) for idx, n in enumerate(nb_max))
            total += number
            print("Adding " + str(number) + " to total")

print("False numbers: " + str(false_numbers))
print(total)