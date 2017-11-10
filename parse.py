import os
import numpy as np

listdir = os.listdir(".")

file_names=[]
for names in listdir:
	if names.endswith(".edges"):
		file_names.append(names)
nodes_list=[]

AM=np.zeros(shape=(4039,4039),dtype=np.int)
inp1=[]
inp_string=""
count=0;
inp1.append("0");
for i in file_names:
	file = open(i,"r")
	q=i
	q.split(".")
	main_node=int(q[0])
	# inp_string="a"
	# inp1.append(inp_string)
	# inp_string="n "+str(main_node)
	# inp1.append(inp_string)
	# count+=1;
	for inp in file:
		inp.strip()
		nodes_list.append([int(e) for e in inp.split(" ")])
	for k in nodes_list:
		x,y=k
		# inp_string="a"
		# inp1.append(inp_string)
		# inp_string="n "+str(x)
		# inp1.append(inp_string)
		# count+=1
		# inp_string="a"
		# inp1.append(inp_string)
		# inp_string="n "+str(y)
		# inp1.append(inp_string)
		# count+=1
		AM[x][y]=1
		inp_string="a"
		inp1.append(inp_string)
		inp_string="e "+str(x)+" "+str(y)
		inp1.append(inp_string)
		count+=1
		AM[y][x]=1
		inp_string="a"
		inp1.append(inp_string)
		inp_string="e "+str(y)+" "+str(x)
		inp1.append(inp_string)
		count+=1
		AM[main_node][x]=1
		inp_string="a"
		inp1.append(inp_string)
		inp_string="e "+str(main_node)+" "+str(x)
		inp1.append(inp_string)
		count+=1
		AM[main_node][y]=1
		inp_string="a"
		inp1.append(inp_string)
		inp_string="e "+str(main_node)+" "+str(y)
		inp1.append(inp_string)
		count+=1
		AM[x][main_node]=1
		inp_string="a"
		inp1.append(inp_string)
		inp_string="e "+str(x)+" "+str(main_node)
		inp1.append(inp_string)
		count+=1
		AM[y][main_node]=1
		inp_string="a"
		inp1.append(inp_string)
		inp_string="e "+str(y)+" "+str(main_node)
		inp1.append(inp_string)
		count+=1
	file.close
# print inp1
np.savetxt("AM.txt",AM,fmt='%d')
inp1[0]=str(count)
np.savetxt("input.txt",np.array(inp1),fmt='%s')
