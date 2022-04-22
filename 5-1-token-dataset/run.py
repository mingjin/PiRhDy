from functions import get_token_dataset, write_filenames

dirs = ['0']  # ,'1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

file_path = '../dataset/sequence/'
name_path = '../filenames/sequence/'
write_filenames(file_path, dirs, name_path, True)

for name in dirs:
    get_token_dataset(name)
