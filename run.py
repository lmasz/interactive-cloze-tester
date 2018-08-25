"""
Updated 7/22/18
@author: lisa m

This program runs the interactive-cloze-tester without the mongoDB backend. Mostly for testing, can be used if you have your own front/backend.

Input: N/A
Output: A json including: -the locations for blanks, the choices for the blanks, the answers.

"""

import preprocess_data as ppd
import os

cwd = os.getcwd()
docsPath = os.path.join(cwd, 'documents', 'security')

for item in os.listdir(docsPath):
    filename = os.path.join(docsPath, item)
    print ('processing: ', item)
    with open(filename, "r") as fid:
        text = fid.read()
        cal = ppd.process_document(text)
        print (cal)
    