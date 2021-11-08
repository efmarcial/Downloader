import pathlib
import os

dir_path = pathlib.Path(__file__).parent.resolve()
print(dir_path)

print('\n')

new_path = str(dir_path) + '/media/'

print(new_path)