from Languages import GetLanguages
import time
import os as some_lib
from __future__ import division

path = input()  # enter path of project
stats = GetLanguages.get_languages(path)
print(stats)
