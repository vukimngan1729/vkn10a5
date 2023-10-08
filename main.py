from s02_chambai import chambai


testkey_list = [
    {'tc_name': 'tc0', 'input': 'AI BTX', 'output':'Hi AI BTX'},  
    {'tc_name': 'tc1', 'input': None,     'output':'Hi'},    
    {'tc_name': 'tc2', 'input': '',       'output':'Hi'},
]

for tc in testkey_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score = chambai(INP_name)
  print(f'''{tc['tc_name']} {tc_score}''')
