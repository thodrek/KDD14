import sys
import math


f = open(sys.argv[1],'r')

bsrSTATdiff = {}
bsrSTATdiff['prec'] = []
bsrSTATdiff['rec'] = []
bsrSTATdiff['f1'] = []

SLSTATdiff = {}
SLSTATdiff['prec'] = []
SLSTATdiff['rec'] = []
SLSTATdiff['f1'] = []

N = 0.0

for l in f:
    l = l.rstrip('\n')
    l = l.split('\t')
    precBSR = float(l[0])
    recBSR = float(l[1])
    f1BSR = float(l[2])
    precLSTAT = float(l[3])
    recLSTAT = float(l[4])
    f1LSTAT = float(l[5])
    precSSTAT = float(l[6])
    recSSTAT = float(l[7])
    f1SSTAT = float(l[8])

    bsrSTATdiff['prec'].append(precSSTAT - precBSR)
    bsrSTATdiff['rec'].append(recSSTAT - recBSR)
    bsrSTATdiff['f1'].append(f1SSTAT - f1BSR)
    SLSTATdiff['prec'].append(precSSTAT - precLSTAT)
    SLSTATdiff['rec'].append(recSSTAT - recLSTAT)
    SLSTATdiff['f1'].append(f1SSTAT - f1LSTAT)

    N += 1.0


# sort differences
rankBSRSTATdiffPrec = sorted(range(len(bsrSTATdiff['prec'])), key=lambda k: abs(bsrSTATdiff['prec'][k]))
rankBSRSTATdiffRec = sorted(range(len(bsrSTATdiff['rec'])), key=lambda k: abs(bsrSTATdiff['rec'][k]))
rankBSRSTATdiffF1 = sorted(range(len(bsrSTATdiff['f1'])), key=lambda k: abs(bsrSTATdiff['f1'][k]))

rankSLSTATdiffPrec = sorted(range(len(SLSTATdiff['prec'])), key=lambda k: abs(SLSTATdiff['prec'][k]))
rankSLSTATdiffRec = sorted(range(len(SLSTATdiff['rec'])), key=lambda k: abs(SLSTATdiff['rec'][k]))
rankSLSTATdiffF1 = sorted(range(len(SLSTATdiff['f1'])), key=lambda k: abs(SLSTATdiff['f1'][k]))


# z  for prec SSTAT-BSR
rplus = 0.0
rminus = 0.0
for i in range(len(bsrSTATdiff['prec'])):
    d = bsrSTATdiff['prec'][i]
    if d > 0.0:
        rplus += float(rankBSRSTATdiffPrec[i])
    elif d < 0.0:
        rminus += float(rankBSRSTATdiffPrec[i])
    else:
        rplus += float(rankBSRSTATdiffPrec[i])/2.0
        rminus += float(rankBSRSTATdiffPrec[i])/2.0

T = min(rplus,rminus)
print "Z for prec SSTAT-BSR:",T
                          
# z  for rec SSTAT-BSR
rplus = 0.0
rminus = 0.0
for i in range(len(bsrSTATdiff['rec'])):
    d = bsrSTATdiff['rec'][i]
    if d > 0.0:
        rplus += float(rankBSRSTATdiffRec[i])
    elif d < 0.0:
        rminus += float(rankBSRSTATdiffRec[i])
    else:
        rplus += float(rankBSRSTATdiffRec[i])/2.0
        rminus += float(rankBSRSTATdiffRec[i])/2.0

T = min(rplus,rminus)
print "Z for rec SSTAT-BSR:",T


# z  for prec SSTAT-BSR
rplus = 0.0
rminus = 0.0
for i in range(len(bsrSTATdiff['f1'])):
    d = bsrSTATdiff['f1'][i]
    if d > 0.0:
        rplus += float(rankBSRSTATdiffF1[i])
    elif d < 0.0:
        rminus += float(rankBSRSTATdiffF1[i])
    else:
        rplus += float(rankBSRSTATdiffF1[i])/2.0
        rminus += float(rankBSRSTATdiffF1[i])/2.0

T = min(rplus,rminus)
print "Z for F1 SSTAT-BSR:",T
                          
                          
                          
# z  for prec SSTAT-LSTAT
rplus = 0.0
rminus = 0.0
for i in range(len(SLSTATdiff['prec'])):
    d = SLSTATdiff['prec'][i]
    if d > 0.0:
        rplus += float(rankSLSTATdiffPrec[i])
    elif d < 0.0:
        rminus += float(rankSLSTATdiffPrec[i])
    else:
        rplus += float(rankSLSTATdiffPrec[i])/2.0
        rminus += float(rankSLSTATdiffPrec[i])/2.0

T = min(rplus,rminus)
print "Z for prec SSTAT-LSTAT:",T

# z  for rec SSTAT-BSR
rplus = 0.0
rminus = 0.0
for i in range(len(SLSTATdiff['rec'])):
    d = SLSTATdiff['rec'][i]
    if d > 0.0:
        rplus += float(rankSLSTATdiffRec[i])
    elif d < 0.0:
        rminus += rankSLSTATdiffRec[i]
    else:
        rplus += float(rankSLSTATdiffRec[i])/2.0
        rminus += float(rankSLSTATdiffRec[i])/2.0

T = min(rplus,rminus)
print "Z for rec SSTAT-LSTAT:",T


# z  for prec SSTAT-BSR
rplus = 0.0
rminus = 0.0
for i in range(len(SLSTATdiff['f1'])):
    d = SLSTATdiff['f1'][i]
    if d > 0.0:
        rplus += float(rankSLSTATdiffF1[i])
    elif d < 0.0:
        rminus += rankSLSTATdiffF1[i]
    else:
        rplus += float(rankSLSTATdiffF1[i])/2.0
        rminus += float(rankSLSTATdiffF1[i])/2.0

T = min(rplus,rminus)
print "Z for F1 SSTAT-LSTAT:",T


