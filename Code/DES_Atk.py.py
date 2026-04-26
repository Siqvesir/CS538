import random

class SboxPermDES: #class to hold all 8 used sboxes for the 6 rounds
    def __init__(user):
        user.sBoxes = [   
            # Sbox 1
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
            4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
            # Sbox 2
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
            0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
            # Sbox 3
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
            13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
            # Sbox 4
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
            10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
            # Sbox 5
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
             4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
            # Sbox 6
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
            9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
            # Sbox 7
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
            1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
            # Sbox 8
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
            7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,  2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]

        #inital permutation table 
        user.IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 
            30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 
            43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

        #expansion table 
        user.ExpTab = [  32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 
            16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
        
        #permutation p-box
        user.PBox = [ 16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
        
        #inverse of the p-box (needed for atk)
        user.IPBox = [ 9, 17, 23, 31, 13, 28,  2, 18, 24, 16, 30,  6, 26, 20, 10,  1,
            8, 14, 25,  3,  4, 29, 11, 19, 32, 12, 22,  7,  5, 27, 15, 21]
        
        #final perm table aka inverse IP
        user.FP = [ 40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 
            54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 
            3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
        
        #permuted choice 1
        user.PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 
            43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 
            54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

        #permuted choice 2
        user.PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 
            52, 31, 37, 47, 55, 30, 40,51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        
        #shuift schedule slightly altered to work w/ the 6-rounds
        user.SS = [1, 1, 2, 2, 2, 2, 2]
    
def permutation(block, t, inLen): #global variabl permutation to easily call on
    result = 0
    for i in t:
        shiftBy = inLen - i #input length minus cur position in tableto get first bit
        shiftBlock = block >> shiftBy #shift the block to index 0
        targBit = shiftBlock & 1 #only get bit at index 0
        result = result << 1 #shift result over 1 so new bit can be added
        result |= targBit #or result w/ target bit to add it to result
    return result


class sixRouDES: #first DES step: 6 rounds of encryption stuff
    def __init__(user, hxKey):
        user.tables = SboxPermDES() #get the sboxes for feistel stuff
        user.subK = user.genSK(int(hxKey, 16)) #get 6 subkeys in bits from main hex key

    def genSK(user, K): #handle PC1 and PC2 to get the needed subkeys
        subkeys = [] #set up subkey liust
        keyPC1 = permutation(K, user.tables.PC1, 64) #get 56b key from tossing key into PC1

        #split keys into 28b halves
        R = keyPC1 & 0xFFFFFFF #28b right half
        L = (keyPC1 >> 28) & 0xFFFFFFF #28b left half

        for i in range(6):
            cirShft = user.tables.SS[i] #set up shift values based on shift scheduler
            #implement circ shift left for 28b for both L and R w/ mask to ensure remains 28b
            R = ((R << cirShft) | (R >> (28 - cirShft))) & 0xFFFFFFF 
            L = ((L << cirShft) | (L >> (28 - cirShft))) & 0xFFFFFFF

            #combine R and L back together
            combine = (L << 28) | R
            #throw the R-L key combo into PC 2 to go from 56b to 48b
            subK = permutation(combine, user.tables.PC2, 56)
            subkeys.append(subK)
        return subkeys
    
    def feistel(user, R, sk): #does actual encryptiom mixing occurs
        #32b R xor w/ 32b of subkey
        exp = permutation(R, user.tables.ExpTab, 32) #expand R from 32b to 48b
        xorESK = exp ^ sk #mix the expansion w/ subkey using xor
        out = 0

        for i in range(8): #for-loop through 8sbox put the 6bit in take the 4 bit out and sbox them all abt I need sleep
            sboxStart = 6 * (7-i) #get start pos of the cur sbox
            sixBinp = (xorESK >> sboxStart) & 0x3F # shift xorESK right to get furthest left bits, mask to ensure only 6 taken 
            row = ((sixBinp & 0x20) >> 4) | (sixBinp & 0x01) #row - 1st bit and 6thbit of the input
            col = (sixBinp & 0x1E) >> 1 #col is middle 4 bits of 6bit inpup
            sbxRes = user.tables.sBoxes[i % len(user.tables.sBoxes)][(row*16)+col]
            out = (out << 4) | sbxRes #shifts result left 4 and add newest 4 to end. 8 loops give full 32b
        return permutation(out, user.tables.PBox, 32) #throw it all in permutation table to mix
    
    def encrypt(user, p):
        block = permutation(p, user.tables.IP, 64) #blocks from initial perm using plaintext
        L = (block >> 32) & 0xFFFFFFFF #shift block right 32 and mask to ensure only 32b to get Left
        R = block & 0xFFFFFFFF #get right half of block b masking 32b to ensure only 32b

        for i in range(6): #6 rounds of the DES feistel enc
            prvR = R #hold onto R bc it will be used for next L
            curRoundK = user.subK[i] #get cur subkey
            feistRes = user.feistel(R, curRoundK)

            #get new R and L values
            R = L ^ feistRes # new R is L xor fesitel result
            L = prvR

        #recombine R and L
        combine = (R << 32) | L #combine back into a 62b total where R6 on L and L6 on R bc put into inverse IP next
        #throw into the final perm table
        c = permutation(combine, user.tables.FP, 64)
        return c

class Analyze:#Adjusted analyze class to hold a map of the sboxes and act as a helper for the atk class instead
    def sBoxMap(user, sbox, num):
        #helper func to handle the mapping of sboxes for row and col
        #gets first bit while 0-ing everything else, shifts in right 4 theng rabs the 6th bit and combines w/ or to get row
        row = ((num & 0x20) >> 4) | (num & 0x01)
        #keeps middle 4 bits and then or's w/ 011110 (0x1E) to ensure shift doesn't end up w/ a 1 at pos 5. Shifts right 1 to 
        col = (num & 0x1E) >> 1
        #throw the row and col into one index w/ 16 rows and the col aka row 1 skips the 16 num of row 0 and etc.
        return sbox[(row * 16) + col]

class Atk:
    def __init__(user, encr, analyzer):
        #construct var for the enc to atk and to analyze stuff
        user.enc = encr
        user.analyze = analyzer
    
    def desAtk(user, difP,numTestIterations = 400000): #simulat the DES atk
        SboxGuess = []
        for i in range(8):
            guessLst = [0] * 64 #64 pos 6bit sk guesses
    
            #for-loop to get pairs of plaintext
            for j in range(numTestIterations):
                pTxt1 = random.getrandbits(64) #to crack use random 64b plaintext here
                pTxt2 = pTxt1 ^ difP #get pTxt2 by xoring w/ difference in chosen p-txt difference

                #Enc process
                cTxt1 = user.enc.encrypt(pTxt1)
                cTxt2 = user.enc.encrypt(pTxt2)
                
                #start dec process w/ FP
                decC1 = permutation(cTxt1, user.enc.tables.IP, 64)
                decC2 = permutation(cTxt2, user.enc.tables.IP, 64)

                #get R from decrypotion of C1 and C2
                R1 = decC1 & 0xFFFFFFFF #mask 32b to only take 32b of decC1
                R2 = decC2 & 0xFFFFFFFF #mask 32b to only take 32b of decC2
                #get L from dec of C1 and C2
                L1 = (decC1 >> 32) & 0xFFFFFFFF #shift L1 over so only 32 leftmost b used and mask w/ 32b so only 32b taen
                L2 = (decC2 >> 32) & 0xFFFFFFFF #shift L2 over so only 32 leftmost b used and mask w/ 32b so only 32b taken
                
                #get the xor dif that came after sboxes from L
                L = L1 ^ L2
                

                #get diff in sbox output by undoing permutation
                sbOutDif = permutation(L, user.enc.tables.IPBox, 32)
                sbDif = (sbOutDif >> (28 - (4*i))) &0x0F #ensure only 4b got from cur sbox bc sbox only ouput 4b

                if sbDif == 0: #if it's 0 skip it to avoid false positives for what the sk is (had issues w/o this here)
                    continue

                expR1 = permutation(R1, user.enc.tables.ExpTab, 32) #sb1 takes 6b from expaning R
                expR2 = permutation(R2, user.enc.tables.ExpTab, 32)

                #for-loop to guess keys
                for k in range(64):
                    sbStart = 6 * (7 - i) #start of the bits for current sbox
                    g1 = (expR1 >> sbStart) & 0x3F ^ k #guesses 6b using expR1 shifted by start of sbox workin w/ and masked to ensure only 6n
                    g2 = (expR2 >> sbStart) & 0x3F ^ k #same as g1 but w/ expR2

                    #check if guess gets right output
                    tmp1 = user.analyze.sBoxMap(user.enc.tables.sBoxes[i], g1)
                    tmp2 = user.analyze.sBoxMap(user.enc.tables.sBoxes[i], g2)
                    if ((tmp1 ^ tmp2) == sbDif):
                        guessLst[k] += 1
            
            #In case actual key doesn't show up as number one guess
            potentialKeys = [] #list of gussed hex pairs
            g = 0 #keep track of index in loop
            for numGuessed in guessLst:
                potentialKeys.append((g, numGuessed)) #add num guessed what spot it is in the guess rankings
                g += 1 #iterate by 1

            
            def getNumGuess(pair):
                return pair[1]

            potentialKeys.sort(key=getNumGuess, reverse=True) #sort in reverse by num times pair was guessed

            print(f"S-box {i+1} Top Potential Keys: ")
            for i in range(3):
                Key, numGuess = potentialKeys[i]
                print(f" Probability {i}: {hex(Key)} num Guessed = {numGuess}")
            
            topGuess = potentialKeys[0][0] #add top three to one array
            SboxGuess.append(topGuess) #throw the top three of the SBox into the returned guesses

        return SboxGuess
    
    def dec(user, c, subkeys):
        block = permutation(c, user.enc.tables.IP, 64) #64b block get
        #get L and R like with enc
        L = (block >> 32) & 0xFFFFFFFF
        R = block & 0xFFFFFFFF

        #loop w/ reveresd subkeys
        for i in range(6, 0, -1): #starts at six, stops at 0, and incrments down 1
            prvR = R #hold onto R bc it will be used for next L
            curRoundK = subkeys[i-1] #get cur subkey i-1 bc starting at 6 which is sk 5
            feistRes = user.enc.feistel(R, curRoundK)

            #get new R and L values
            R = L ^ feistRes # new R is L xor fesitel result
            L = prvR

        #recombine R and L
        combine = (R << 32) | L #combine back into a 64b total

        #throw into the final perm table
        cTxt = permutation(combine, user.enc.tables.FP, 64)
        return cTxt
    
    def checkAtkSucc(user, ogP): #check to ensure basic DES set up properly
        c = user.enc.encrypt(ogP) #encrypt p using des to get c
        decK = user.enc.subK #sub keys found during decryption
        decP = user.dec(c, decK)

        print(f"Original P: {hex(ogP)}\n")
        print(f"Decrypted P: {hex(decP)}\n")

        if decP == ogP:
            print("Success\n")
        else:
            print("Decryption Failed\n")        

class DES_ATK: #name class after file to execute here when run
    
    print("Key needed for both options to check output is right at the end\n\n")

    def __init__(user): #if named differently, doesn't interface so switched from main to __init__ even tho not a constructor
        user.analyze = Analyze()
    
        print("CS538 DES Attack Implementation\n")
        print("1) Check DES works\n")
        print("2) Just Attack \n") #chosen plaintext atk
        uInp = input("Choose 1 or 2: ")

        if uInp == '1':
            K = input("Enter Key: ")
            Phex = input("Enter Plaintext as Hex (64 bits only!): ")

            P = int(Phex, 16) #convert hex to int for plaintext bit math
            user.enc = (sixRouDES(K)) #sub key data generated and stored and go through the boxes
            user.DESatk = Atk(user.enc, user.analyze) #attack and analyze the key data with math guesses

            user.DESatk.checkAtkSucc(P) #check to make sure found P and OG P are the same

        elif uInp == '2': #

            K = input("Key Used: ")

            user.enc = sixRouDES(K)
            user.DESatk = Atk(user.enc, user.analyze)
            
            #get random plaintext pair w/ fixed difference
            diffP = 0x0000000000000010 #dif randomly decided by changing just 1 bit
            p1 = random.getrandbits(64)
            p2 = p1 ^ diffP

            c1 = user.enc.encrypt(p1)
            c2 = user.enc.encrypt(p2)

            #Values working with mostly for debugging if need be
            print(f"P1: {hex(p1)}")
            print(f"P2: {hex(p2)}")
            print(f"C1: {hex(c1)}")
            print(f"C2: {hex(c2)}")


            #set up comparison
            actSK = user.enc.subK[5] #48b subkey gotten from key
            
            #then split key into sbox blocks to compare w/ sbox subkey outputs
            sbActSK = []
            for i in range(8): #for the 8 subkeys
                tmp = (actSK >> (6 * (7-i))) & 0x3F #shifts actSK right to position cur sbox takes up and masks to ensure 6b 
                sbActSK.append(hex(tmp))
            print(f"Actual subkey in sbox blocks: {sbActSK}") # to compare w/ guess results

            #initiate attack to guess the subkeys
            guessedSK = user.DESatk.desAtk(diffP) #get most likely subkey

            #get the subkey as the typical 48b subkey
            testFullSK = 0
            j = 0
            for cur in guessedSK:
                testFullSK |= (cur << (6 * (7-j))) #reverse of getting chunks
                j += 1

            #print results:
            print(f"Top subkey guess in 48b: {hex(testFullSK)}")
            print(f"Actual subkey:  {hex(actSK)}")                                             

# won't run right if this isn't added
if __name__ == "__main__":
    DES_ATK()
 



