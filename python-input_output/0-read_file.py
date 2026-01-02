  1 #!/usr/bin/python3
  2 """PART:I/O"""
  3 
  4 
  5 def read_file(filename=''):
  6     """funct"""
  7     with open(filename, 'r') as file:
  8         return file.read()
