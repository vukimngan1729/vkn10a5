from s00_bailam import hi as bailam_f


#region chambai
from s02_chambai import chambai

testkey_list = [
    {'tc_name': 'tc0', 'input': {'name':'AI BTX'}, 'output':'Hi AI BTX'},  
    {'tc_name': 'tc1', 'input': {'name':'HSU'},    'output':'Hi'},    
    {'tc_name': 'tc2', 'input': {'name':None},     'output':'Hi'},
    {'tc_name': 'tc3', 'input': {'name':''},       'output':'Hi AI BTX'},  
]

ketqua_list = []
for tc in testkey_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)
  
  ketqua_list.append({
    'tc_name'    : tc['tc_name'],
    'tc_score'   : tc_score,  
    'o_TESTCASE' : tc['output'],    
    'o_BAILAM'   : o_BAILAM,  
  })
#endregion chambai

#region in ketquqa
print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_TESTCASE = {kq['o_TESTCASE']}
o_BAILAM   = {kq['o_BAILAM']}
  '''.strip()+'\n')

print('\n---ketqua')
for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
#endregion in ketquqa
