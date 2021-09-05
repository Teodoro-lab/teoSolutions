import os

def remove_empty_dirs(path,*ignore):
	directories_files_in_path = os.listdir(path)

	if len(directories_files_in_path) == 0:
		os.rmdir(path)
		return

	for directory_file in directories_files_in_path:
		file = path + f'/{directory_file}'
		if os.path.isdir(file):
			remove_empty_dirs(file)

string = os.getcwd()
remove_empty_dirs(
	#dir to analyze
	"C:\\Users\\Teo\\Desktop\\docs_m&f\\Media\\WhatsApp Voice Notes"
)

