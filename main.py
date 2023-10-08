from s02_chambai import chambai


from s01_dapan  import hi as dapan_f
from s00_bailam import hi as bailam_f

testkey_list = [
    {'tc_name': 'tc0', 'input': {'name':'AI BTX'}, 'output':'Hi AI BTX'},  
    {'tc_name': 'tc1', 'input': {'name':None},     'output':'Hi'},    
    {'tc_name': 'tc2', 'input': {'name':''},       'output':'Hi'},
]

for tc in testkey_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score = chambai(tc, dapan_f, bailam_f)
  print(f'''{tc['tc_name']} {tc_score}''')
