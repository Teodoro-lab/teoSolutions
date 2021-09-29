import os
errorFiles = []
def find_files(path, destination_path,*ignore):
	global errorFiles
	for directory_file in os.listdir(path):
		file = path + f'/{directory_file}'
		if os.path.isdir(file):
			find_files(file, destination_path)
		else:
			try:
				os.rename(file, destination_path + f'{directory_file}')
			except:
				errorFiles.append((file, destination_path + f'{directory_file}'))

string = os.getcwd()
find_files(
	#dir to analyze
	"C:\\Users\\Teo\\Desktop\\docs_m&f\\Media\\WhatsApp Voice Notes",
	#path where the files are goin to be moved
    "C:\\Users\\Teo\\Desktop\\docs_m&f\\Media\\WhatsApp Voice Notes\\audios\\"
)