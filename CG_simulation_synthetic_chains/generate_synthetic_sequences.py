"""
Generate synthetic sequences with different positive, negative, and neutral fractions

"""
import numpy as np
import pandas as pd
from more_itertools import random_permutation


protein_length = 100
n_bins = 20 #divided the range of [0,1] by n_bins
fp = np.arange(0, 1.01, 1/n_bins)
fn = np.arange(0, 1.01, 1/n_bins)


aa_neutral = ['V', 'I', 'L', 'Q', 'N', 'H', 'W',
              'F', 'Y', 'S', 'T', 'M', 'A', 'G', 'P', 'C']
aa_positive = ['R', 'K']
aa_negative = ['D', 'E']

def gen_possitive(np):
    """
    generate np charged residues.
    composition of each residue in set of positive residues:
    e.g: Table 1 from DisProt:
    K=7.85%, R=4.82%
    %R = R/(R+K)=0.38
    
    """
    
    nR = round(np*0.38)
    nK = np-nR
    seq = nR*'R'+nK*'K'
    return seq

def gen_negative(nn):
    nD = round(nn*0.37)
    nE = nn-nD
    seq = nD*'D'+nE*'E'
    return seq


def gen_neutral(n0):
    nP  = round(n0*0.11)
    nQ  = round(n0*0.07)
    nA  = round(n0*0.11)
    nG  = round(n0*0.10)
    nT  = round(n0*0.08)
    nM  = round(n0*0.03)
    nN  = round(n0*0.05)
    nV  = round(n0*0.08)
    nH  = round(n0*0.03)
    nL  = round(n0*0.09)
    nF  = round(n0*0.03)
    nY  = round(n0*0.03)
    nI  = round(n0*0.05)
    nW  = round(n0*0.01)
    nC  = round(n0*0.01)
    nS = n0- (nP+nQ+nA+nG+nT+nM+nN+nV+nH+nL+nF+nY+nI+nW+nC)
    
    seq = nP*'P'+nS*'S'+nQ*'Q'+nA*'A'+nG*'G'+nT*'T'+nM*'M'+nN*'N'+nV*'V'+nH*'H'+nL*'L'+nF*'F'+nY*'Y'+nI*'I'+nW*'W'+nC*'C'
    return seq

def generate_completed_sequence(fraction_positve, fraction_negative, seq_length):
    # for production, this function should be run only once since the random_permutation is not fixed random_seed
    fraction_neutral = 1 - (fraction_positve+fraction_negative)
    number_positive_residues = int(fraction_positve*seq_length)
    number_negative_residues = int(fraction_negative*seq_length)
    number_neutral_residues = seq_length - (number_positive_residues+number_negative_residues)
    
    fasta_seq = gen_possitive(number_positive_residues) + gen_negative(number_negative_residues) + gen_neutral(number_neutral_residues)
    
    return ''.join(random_permutation(fasta_seq))


k = 1
print('idx, fp, fn, f0, seq')
data=pd.DataFrame(columns=['idx', 'f_positive','f_negative', 'sequence'])
for i in fp:
    for j in fn:
        if (i+j) <= 1:
            seq = generate_completed_sequence(i,j, protein_length)
            data = data.append({'idx':k, 'f_positive':i, 'f_negative':j, 'sequence':seq}, ignore_index=True)
            k+=1


data.to_pickle('sequence_100residues.pkl')
