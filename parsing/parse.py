import os
import numpy as np

listdir = os.listdir(".")

file_names=[]
for names in listdir:
	if names.endswith(".txt"):
		file_names.append(names)
nodes_list=[]

inp1=[]
inp_string=""
count=0
j=0
AM=[]
inp1.append("0");
for i in file_names:
	file = open(i,"r")
	for inp in file:
		print inp
		inp.strip()
		if j == 0:
			n=int(inp)
			AM = np.zeros(shape=(n,n),dtype=int)
			j += 1
		else:
			x,y=inp.split("\t")
			AM[int(x)][int(y)]=1
			inp_string="a"
			inp1.append(inp_string)
			inp_string="e "+str(x)+" "+str(y)
			inp1.append(inp_string)
			count+=1
			AM[int(y)][int(x)]=1
			inp_string="a"
			inp1.append(inp_string)
			inp_string="e "+str(y)+" "+str(x)
			inp1.append(inp_string)
			count+=1	
	file.close
np.savetxt("AM.txt",AM,fmt='%d')
inp1[0]=str(count)
np.savetxt("input_email.txt",np.array(inp1),fmt='%s')
