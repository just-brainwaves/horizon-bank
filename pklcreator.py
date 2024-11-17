import pickle

# Path to the pickle file
file_path = 'custdata.pkl'

# write mode with 'wb' (write binary)
with open(file_path, 'wb') as file:
    # empty object ({})
    pickle.dump({}, file)