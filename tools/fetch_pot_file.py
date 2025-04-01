"""Helper script for copying tlviewer translation file to the language pack directory.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/tlviewer_xx
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copyfile
from settings import *

ROOT_DIR = '../..'
APP = ''

os.chdir(ROOT_DIR)
potFile = 'timeline-view-tk/i18n/messages.pot'
if os.path.isfile(potFile):
    targetPath = f'tlviewer_{languageCode}/i18n'
    os.makedirs(targetPath, exist_ok=True)
    copyfile(potFile, f'{targetPath}/messages.pot')
print('Done.')
