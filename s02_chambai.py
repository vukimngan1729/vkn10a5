def chambai(testcase, dapan_f, bailam_f):
  o_DAPAN = dapan_f(**testcase['input'])  # aka output_DAPAN

  try:
    o_BAILAM = bailam_f(**testcase['input'])  # aka input_DAPAN
  except:
    o_BAILAM = None

  score01 = int(o_BAILAM == o_DAPAN)
  return score01, o_DAPAN, o_BAILAM
