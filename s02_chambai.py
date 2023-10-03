def chambai():
  INP_name = 'AI BTX'
  
  from s01_dapan import hi
  EXPECTED_result = hi(INP_name)

  try:
    from s00_bailam import hi
    ACTUAL_result = hi(INP_name)
  except:
    ACTUAL_result = None

  chambai_r = 1 if ACTUAL_result == EXPECTED_result else 0
  return chambai_r
