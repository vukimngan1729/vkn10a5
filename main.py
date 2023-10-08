from s02_chambai import chambai

from s01_dapan  import hi as dapan_f
from s00_bailam import hi as bailam_f


testkey_list = [
    {'tc_name': 'tc0', 'input': {'name':'AI BTX'}, 'output':'Hi AI BTX'},  
    {'tc_name': 'tc1', 'input': {'name':None},     'output':'Hi'},    
    {'tc_name': 'tc2', 'input': {'name':''},       'output':'Hi'},
]

ketqua_list = []
for tc in testkey_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_DAPAN, o_BAILAM = \
    chambai(tc, dapan_f, bailam_f)
  
  ketqua_list.append({
    'tc_name'  : tc['tc_name'],
    'tc_score' : tc_score,  
    'o_DAPAN'  : o_DAPAN,    
    'o_BAILAM' : o_BAILAM,  
  })

print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_DAPAN  = {kq['o_DAPAN']}
o_BAILAM = {kq['o_DAPAN']}
  '''.strip()+'\n')

print('\n---ketqua')
for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
