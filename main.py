from s00_bailam import solution as bailam_f


#region chambai
from s02_chambai import chambai

#region testkey_list
testcase_list = [
  {'tc_name': 'tc0', 'input': {'i1':1,    'i2':22},   'output':23},
  {'tc_name': 'tc1', 'input': {'i1':1,    'i2':None}, 'output':None},
  {'tc_name': 'tc0', 'input': {'i1':None, 'i2':22},   'output':None},
  {'tc_name': 'tc0', 'input': {'i1':None, 'i2':None}, 'output':None},
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
