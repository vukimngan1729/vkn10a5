def chambai(testcase, dapan_f, bailam_f):
  r_DAPAN = dapan_f(**testcase['input'])

  try:
    r_THISINH = bailam_f(**testcase['input'])
  except:
    r_THISINH = None

  score01 = int(r_THISINH == r_DAPAN)
  return score01
