from functions import midi_to_matrix, write_filenames
dirs=['0']#,'1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
file_path = '../dataset/lakh_normalized/'  # lmd dataset path
name_path = '../filenames/lakh_dataset/'
write_filenames(file_path, dirs, name_path, True)
for name in dirs:
    midi_to_matrix(name)