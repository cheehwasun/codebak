import os
import subprocess

srcdir=r'c:\2\tmp'
dstdir=r'c:\3'
dirs=os.listdir(srcdir)
for file in dirs:
	print(file)

	srcfile=file

	dstfile=os.path.splitext(srcfile)
	if dstfile[1]=='.py':
		print(dstfile[1])
	else:

		begin_time=0
		duration_time=238

		cmd1="ffmpeg -i "+os.path.join(srcdir,srcfile)+" 2>aa.txt"
		b=subprocess.run(cmd1,shell=True)

		total_time=0

##		with open ('aa.txt') as f:
##			lines=f.readlines()
##			total_time=56

		t1=31
		for i in range(t1):
			# outfile=os.path.join(dstdir,dstfile[0]+"_"+"{:0>2}".format(i+1)+dstfile[1])
			# cmd2="ffmpeg -ss "+str(begin_time+duration_time*i)+" -i "+srcfile+" -c copy -t 230 "+outfile
			cmd2="ffmpeg -ss "+str(begin_time+duration_time*i)+" -i "+srcfile+" -c copy -t 280 "+dstfile[0]+"_"+"{:0>2}".format(i+1)+dstfile[1]
			b=subprocess.run(cmd2,shell=True)
			print(cmd2)

		# outfile=os.path.join(dstdir,dstfile[0]+"_"+"{:0>2}".format(t1)+dstfile[1])
		# cmd3="ffmpeg -ss "+str(begin_time+duration_time*t1)+" -i "+srcfile+" -c copy "+outfile
		cmd3="ffmpeg -ss "+str(begin_time+duration_time*t1)+" -i "+srcfile+" -c copy "+dstfile[0]+"_"+"{:0>2}".format(1+t1)+dstfile[1]

		b=subprocess.run(cmd3,shell=True)
		print(cmd3)
