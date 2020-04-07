import os

filename1 = 'input.txt'
filename2 = 'output.txt'

if os.path.isfile(filename1):
	chat = []
	# 檔案存在
	with open(filename1, 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			if 'Allen' in line or 'Tom' in line:
				name = line
				continue
			else:
				chat.append(name + ':' + line)	
	# print(chat)
	# 寫入檔案
	with open(filename2, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')
else:
	print('檔案不存在')	