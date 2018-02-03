#!/usr/bin/python
#
# https://wikidocs.net/73

def prg2com(inlist, coms):
    outlist = []
    outsum = []
    for x in range(coms):
        outlist.append([])
        outsum.append(0)
    
    inlist.sort(reverse=True)

    for bread in inlist:
        lowbasket = outsum.index(min(outsum))
        outlist[lowbasket].append(bread)
        outsum[lowbasket] += bread
    return outlist

def main():
    print prg2com([3,15,6,22,13,2], 3)

if __name__ == "__main__":
    main()
