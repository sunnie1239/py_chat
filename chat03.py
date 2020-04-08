import os

# 讀取檔案--存入list--回傳list
def read_file(filename):
	line_list = []
	with open(filename, 'r', encoding='utf-8') as f: # 假設文字從txt檔抓出後，在cmd顯示上有亂碼，須改為此種編碼 encoding='utf-8-sig'
		for line in f:
			line_list.append(line.strip())
	return line_list
			
# 計算發話次數&字數
def convert(line_list):
	allen_spk  = 0 # Allen發話次數
	allen_word = 0 # Allen字數
	viki_spk   = 0 # Viki發話次數
	viki_word  = 0 # Viki字數

	for line in line_list:
		s = line.split(' ')
		if s[1] == 'Allen':
			allen_spk += 1
			for msg in s[2:]:
				allen_word += len(msg)
		elif s[1] == 'Viki':
			viki_spk += 1
			for msg in s[2:]:
				viki_word += len(msg)

	print('Allen發話次數: ', allen_spk, '總字數: ', allen_word)
	print('Viki發話次數: ', viki_spk, '總字數: ', viki_word)		

# 寫入檔案
def write_file(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')

# 主程式
def main():
	if os.path.isfile('[LINE]Viki.txt'):
		result = read_file('[LINE]Viki.txt')
		result = convert(result)
		# write_file('output.txt', result)
	else:
		print('檔案不存在')	

#執行程式
main()