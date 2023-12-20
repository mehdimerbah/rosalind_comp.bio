#!/usr/bin/env python3


import sys
from scipy.special import comb

try:
    input_file = open('mendel_input.txt', 'rt')
except:
    print('File not found!')
    sys.exit()


population= input_file.readline().strip('\n').split(' ')

## Read in all the population segments: Homozygous dominant, heterozygous, homozygous recessive
homoz_d = int(population[0])
heter = int(population[1])
homoz_r = int(population[2])

totalPop = homoz_d + homoz_r + heter

## We get the total number of combinations possible for the entire population set, these include both individuals with the dominant allele and those without
total_combos = comb(totalPop, 2)


## Now get the number of combinations that would get you a dominant allele

## The combination of all possible Homo_d individuals would give us an individual with dominant allele
homoz_d_cross = comb(homoz_d, 2)
## Crossing a Homoz_d and a Heter would also give us an offspring with a dominant allele
homoz_d_heter_cross = homoz_d*heter
## Crossing a Homoz_d and Homoz_r would also give us an offspring with a dominant allele
homoz_d_homoz_r_cross = homoz_d*homoz_r
## Crossing a Homoz_r and a Heter individual would give us half a population with a dominant allele (2/4) (So we multiply it by 1/2)
homoz_r_heter_cross = .5*homoz_r*heter
## Crossing two Heter individuals would give us a population with 75% having the dominant allele (3/4) (So we multiply it by 3/4)
heter_cross = .75*comb(heter, 2)
## We get the number of combos that give us offspring with a dominant allele
dominant_combos = homoz_d_cross + homoz_d_heter_cross + homoz_d_homoz_r_cross + homoz_r_heter_cross + heter_cross


## Now let's divide the number of combinations that would generate a dominant allele with the total number of possible combinations
probability = round(dominant_combos/total_combos, 5)

print(probability)

input_file.close()