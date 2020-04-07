import os

# 讀取檔案--存入list--回傳list
def read_file(filename):
	line_list = []
	with open(filename, 'r', encoding='utf-8') as f: # 假設文字從txt檔抓出後，在cmd顯示上有亂碼，須改為此種編碼 encoding='utf-8-sig'
		for line in f:
			line_list.append(line.strip())
	return line_list
			
# 轉換格式
def convert(line_list):
	chat = []
	name = None
	for line in line_list:
		if 'Allen' in line or 'Tom' in line:
			name = line
		elif name:
			chat.append(name + ': ' + line)
	return chat		

# 寫入檔案
def write_file(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')

# 主程式
def main():
	if os.path.isfile('input.txt'):
		result = read_file('input.txt')
		result = convert(result)
		write_file('output.txt', result)
	else:
		print('檔案不存在')	

#執行程式
main()