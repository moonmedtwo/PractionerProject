import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER = os.path.dirname(THIS_FOLDER)
SAVED_WEIGHT = os.path.join(PARENT_FOLDER, 'SavedWeights')
print(THIS_FOLDER)
print(PARENT_FOLDER)
print(SAVED_WEIGHT)
print(os.path.isdir(SAVED_WEIGHT))

filename = 'test.csv'
file = open(os.path.join(SAVED_WEIGHT,filename),'w')
file.write('Sno,Weight\n')
file.close()
print(filename + " written!")
