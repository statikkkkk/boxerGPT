# boxerGPT Dataset 

## Introduction
This dataset is collected manually from various websites. Overall, the dataset will look like this:

```
1, 2, 3
1, 1, 2
```

Following the boxer combo convention, the numbering of the combos will be as follows:

```
1 - Jab
2 - Cross
3 - Left Hook
4 - Right Hook
5 - Left Uppercut
6 - Right Uppercut
*: To the body
```

To add varity of the combos, the dataset will be augmented with slips, blocks, drops, and other defensive moves. The dataset will be augmented with the following:

```
7 - Left Slip
8 - Right Slip
9 - Drop
10 - Left Block
11 - Right Block
12 - Left Roll
13 - Right Roll
```

## Augmentation
Since the basic combo is quite small, the dataset is augmented with the following strategies:
1. Add body shots to the basic combos
2. Add defensive moves to the basic combos (slips, blocks, rolls, etc.) with a percentage chance of occuring

Just like GPT-2 and GPT-3, each sample will have `<CLS> and <SEP>` tokens at the beginning and end of the sample respectively.
```
14 - <CLS>
15 - <SEP>
```

## Sources for the basic combos used
The basic combos used are from the following websites, and is saved as a txt file in the data folder named `basic_drills.txt`:
- https://boxingholic.com/boxing-combos/basic-combos/
- https://evolve-mma.com/blog/15-basic-boxing-combinations-you-should-master-first/
