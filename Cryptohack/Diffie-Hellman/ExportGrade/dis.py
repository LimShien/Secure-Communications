#!/usr/bin/python
from array import array
from cons import rads, lrads, linvs, lcms, rngs, mxms, logss
from operator import mod, sub
import sys

def eea(a,b):
	v1 = [a,1,0]
	v2 = [b,0,1]
	while v2[0]<>0:
	   p = v1[0]//v2[0]
	   v2, v1 = map(sub,v1,[p*vi for vi in v2]), v2
	return v1

def minv(m,k):
	v = eea(m,k)
	if v[1]>=0:
		return v[1]
	else:
		return k+v[1]
		
def mdiv(dor, dend, rad):
    inv=minv(dend, rad)
    return mod(inv*dor, rad)

def dusqrs():
	tot=2
	lst=[]
	bits=len(bin(xmxm))-1
	for ind in range(1, bits):
		lst.append(tot)
		tot=(tot**2)%xmxm
	return lst
	
def dexp(lind):
	str=bin(lind)[2:]
	dat=str[::-1]
	lim=len(dat)
	tot=1
	for ind in range( lim):
		if(dat[ind]=='1'):
			tot=(tot*sqrs[ind])%xmxm
	return tot

def lres2dec(ires):
	lim=len(ires)
	tot=ires[0]
	ind=1
	while ind<lim:
		lrad=lrads[ind]
		cry=mod(tot, lrad)
		dig=mod((ires[ind]-cry)*linvs[ind], lrad)
		tot+=dig*lcms[ind]
		ind+=1
	return tot
	
def durut(res):
	rut=[]
	for ind in range(len(res)):
		lrad=lrads[ind]
		logs=logss[ind]
		rut.append(logs[res[ind]]%lrad)
	return rut
	
def dec2res(numd):
	ar=[]
	for rad in rads:
		ar.append(numd%rad)
	return ar

def euc(ar0, ar1):
    while ar0>0:
        rx=ar1%ar0
        ar1=ar0
        ar0=rx
    return ar1

def ilgr(pres):
	rut=durut(pres)
	return lres2dec(rut)
	
def ilg(val):
	pres=dec2res(val)
	return ilgr(pres)
	
def dudif(trg):
	trgr=dec2res(trg)
	lim=len(trgr)
	clog=ilg(trg)%xlcm
	trg1=trg<<1
	if trg1>xmxm:
		trg1-xmxm
	clog1=ilg(trg1)%xlcm
	dif=(clog1-clog)%xlcm
	return (clog, dif)
	
def fnd(trg, stp):
	gcd=euc(stp, rng)
	if gcd>1:
		stp/=gcd
		trg/=gcd
	inv=minv(stp, rng)
	return (((inv*trg)%rng))
	
def duof(strt, nu):
	return mdiv(strt, (dexp(nu)), xmxm)

def clog(strt):
	loc=dudif(strt)
	locx=fnd(loc[0], loc[1])
	xp=duof(strt, locx)
	chk=((dexp(locx)%xmxm)*xp)%xmxm
	if chk!=strt:
		print 'err', xp, locx
		exit(1)
	return (xp, loc[0])

def man():
	if trg>xmxm:
		print 'target too large, increase radix count?'
		return
	loc=clog(trg)
	print 'trg', trg
	print 'rut', loc[0]
	print 'exp', loc[1]
	print 'mod', xmxm

if len(sys.argv)<3:
	print 'Usage clog <radix count> <target>'
	exit()
radcnt=int(sys.argv[1])
lim=len(rads)-1
if radcnt>len:
	print 'radix count limited to %d'%len
	radcnt=len
trg=int(sys.argv[2])
if trg<0:
	print 'target must be a positive integer'
	exit()
rads=rads[:radcnt]
lrads=lrads[:radcnt]
xmxm=mxms[radcnt]
rng=rngs[radcnt-1]
xlcm=lcms[radcnt]
sqrs=dusqrs()
man();
