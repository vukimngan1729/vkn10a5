"""
debai 
Viet python ham hi()
Nhap vao ten :name va trave cau chao 'Hi {name}!'

input 
name='some name'

output 
Hi some name!
"""

def hi(name):
  return f'Hi {name}!'

if __name__=='__main__':
  name = 'AI BTX'
  print(hi(name))
