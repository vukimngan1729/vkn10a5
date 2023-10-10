#region import bailam_f
from s00_bailam import hi as bailam_f
#endregion import bailam_f

#region chambai
from s02_chambai import chambai

#region testkey_list
testcase_list = [
  {'tc_name': 'tc0', 'input': {'name':'Mom',    'gener':'f'},   'output':'Hi Ms Mom!'},
  {'tc_name': 'tc1', 'input': {'name':'Dad',    'gener':'m'},   'output':'Hi Mr Dad!'},
  {'tc_name': 'tc2', 'input': {'name':'AI-BTX', 'gener':None},  'output':'Hi AI-BTX!'},
  {'tc_name': 'tc3', 'input': {'name':None,     'gener':None},  'output':'Hi!'},
]
#endregion testkey_list

ketqua_list = []
for tc in testcase_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)
  
  ketqua_list.append({
    'tc_name'    : tc['tc_name'],
    'tc_score'   : tc_score,  
    'o_TESTCASE' : tc['output'],    
    'o_BAILAM'   : o_BAILAM,  
  })
#endregion chambai

#region in ketqua
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
#endregion in ketqua
