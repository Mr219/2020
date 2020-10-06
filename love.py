#!/usr/bin/python3
#coding=utf-8
from os import system, name
import os,sys,time

try:
	os.system('mpv ')
except:
	os.system("pip install mpv")
	# os.system("python3 "+ sys.argv[0] + "")
love="KHIN"

class co:
   P = '\033[1;35;48m'
   C = '\033[1;36;48m'
   BO = '\033[1;37;48m'
   BL = '\033[1;34;48m'
   G = '\033[1;32;48m'
   Y = '\033[1;33;48m'
   R = '\033[1;31;48m'
   B = '\033[1;30;48m'
   U = '\033[4;37;48m'
   E = '\033[1;37;0m'

def clear():
	if name == 'nt': 
		_ = system('cls')
	else:
		_ = system('clear')

def flu(st,a):
	if a == "l":
		st = len(st)
	for _ in range(st):
		time.sleep(0.05)
		sys.stdout.write('\033[D \033[D')
		sys.stdout.flush()

def psb(z):
	for e in z:
		print(e, end ='') 
		sys.stdout.flush()
		time.sleep(0.05)
def gom(z):
	print(co.G+"                                                   U |",end="")
	for x in range(3, 41):
		time.sleep(0.05)
		msg = "\r{}{}{}".format("| I"," " * x, "၊- "+z+" -"+">")
		print(msg,end="")
		sys.stdout.flush()
	# print("i love u")
def po(s):
	# print("|", s.center(50, ''),"|")
	print("|"+co.C,end="")
	psb(s.center(52," "))
	print(co.G+"|")
try:
	clear()
	print("\n\n")
	print(co.G+"", ('').center(52, '_'),"")
	print(co.G+"|", ('').center(50, ' '),"|")

	psb("| Enter Your Name : ")
	##############check crush...################
	crush = input("\t")

	if love not in crush.upper():
		print(co.G+"|", ('').center(50, '-'),"|")
		print(co.R+"|", (' Bye Bye,This is for my crush ').center(50, ' '),"|")
		print(co.G+"|", ('').center(50, '_'),"|")
		sys.exit()

	print(co.G+"|", ('').center(50, '-'),"|"+co.E)
	psb(co.G+"|"+("Dear My "+crush).center(52, ' ')+"|\n")
	gom("❤")

	print("\n|", ('').center(50, '_'),"|")
	po("")
	po("As long as the stars twinkle in the sky,")
	po("As long as angels are there up high, ")
	po("Till the ocean run dry and till the day I die.")
	po(" I will love U.")
	po("")
	print("|", ('').center(50, '_'),"|")
	po("")
	print("|\t",co.R,"  ,d88b.d88b,",co.G)
	print("|\t",co.R,"  88888888888",co.G)
	print("|\t",co.R,"  `Y8888888Y'",co.G)
	print("|\t",co.R,"    `Y888Y'    -Love You-",co.G)
	print("|\t",co.R,"      `Y'",co.G)
	print("|", ('').center(50, '_'),"|")
	os.system("mpv --fs http://www.zayycho.com/ktv/saisai.mp3")
	print("|", ('').center(50, '_'),"|")
	time.sleep(2000)
except KeyboardInterrupt:
    print(co.G+"", ('').center(52, '_'),"")
except:
	print('')
