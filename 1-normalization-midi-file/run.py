from functions import normalization_midi_file, write_filenames
dirs=['0']#,'1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
file_path = '../dataset/lakh_dataset/'
name_path = '../filenames/lakh_dataset/'
write_filenames(file_path, dirs, name_path, True)
normalization_midi_file(dirs)