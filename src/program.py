# Line 1
# Line 2
# Line 3
# Line 4

import os
print("Hello", os.environ.get('JOB_NAME'))

# print('::warning ::Warning no file')
# print('::error ::Error no file')

# print('::warning file={}::Warning File'.format(__file__))
# print('::error file={}::Error File'.format(__file__))

# print('::warning file={},line=1::Warning Line 1'.format(__file__))
# print('::error file={},line=2::Error Line 2'.format(__file__))

# print('::warning file={},line=3,col=2::Warning Line 3'.format(__file__))
# print('::error file={},line=4,col=4::Error Line 4'.format(__file__))

# print('::warning file={},line=5::Warning Multiline Line%0ALine2%0ALine3'.format(__file__))
# print('::error file={},line=6::Error Multiline Line%0ALine2%0ALine3%0ALine4'.format(__file__))
