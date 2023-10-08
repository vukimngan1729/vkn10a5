def chambai(testcase, dapan_f, bailam_f):
  o_TESTCASE = testcase.get('output')

  if dapan_f:
    o_DAPAN = dapan_f(**testcase['input'])  # aka output_DAPAN
  else:
    o_DAPAN = None

  assert o_TESTCASE or o_DAPAN, 'MUST HAVE output fr either o_TESTCASE or o_DAPAN to score :bailam ^^'
  assert callable(bailam_f),    'MUST HAVE bailam_f() method to score :bailam ^^'
  
  try:
    o_BAILAM = bailam_f(**testcase['input'])  # aka input_DAPAN
  except:
    o_BAILAM = None

  '''NOTE
  we MUST HAVE o_BAILAM matched with either
  00 o_TESTCASE
  01 o_DAPAN = dapan_f() 
  '''
  is__bailam_eq_dapan = int(o_BAILAM == o_DAPAN)
  is__bailam_eq_tc    = int(o_BAILAM == o_TESTCASE)
  score01 = int(
       is__bailam_eq_dapan
    or is__bailam_eq_tc
  )
  return score01, o_DAPAN, o_BAILAM
