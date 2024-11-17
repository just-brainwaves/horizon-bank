import pickle
file_path = 'custdata.pkl'
with open(file_path, 'wb') as file:
    pickle.dump({}, file)
