import os

# 讀檔並轉換
def convert(filename):
	chat = []
	name = None
	# 檔案存在
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			if 'Allen' in line or 'Tom' in line:
				name = line
			else:
				if name:
					chat.append(name + ':' + line)	
	return chat				

# 寫入檔案
def write_file(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')

# 主程式
def main():
	if os.path.isfile('input.txt'):
		chat = convert('input.txt')
		write_file('output.txt', chat)
	else:
		print('檔案不存在')	

#執行程式
main()