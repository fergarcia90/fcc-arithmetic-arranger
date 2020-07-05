import re

def arithmetic_arranger(problems, resolve=False):
  validation = validate(problems)
  if(not validation['result']):
    return validation['error']
  first_line = []
  second_line = []
  third_line = []
  results = []
  for prob in problems:
    prob_list = prob.split()
    largest_num = getLargestNumber(prob_list)
    if(prob_list[0] == largest_num):
      whitespace_number = ' '*(len(largest_num)-len(prob_list[2]))
      first_operand = '  '+prob_list[0]
      second_operand = whitespace_number+prob_list[2]
    else:
      whitespace_number = ' '*(len(largest_num)-len(prob_list[0])+2)
      first_operand = whitespace_number+prob_list[0]
      second_operand = prob_list[2]
    operator = prob_list[1]
    bottom_line = '-' * (len(largest_num)+2)
    first_line.append(first_operand)
    second_line.append(operator+' '+second_operand)
    third_line.append(bottom_line)
    if(resolve):  
      if(prob_list[1] == '+'):
        result = str(int(prob_list[0])+int(prob_list[2]))
      else:
        result = str(int(prob_list[0])-int(prob_list[2]))
      whitespace_number = ' '*(len(largest_num)-len(result)+2)
      results.append(whitespace_number+result)

  if(resolve):
    arranged_problems = '    '.join(first_line)+'\n'+'    '.join(second_line)+'\n'+'    '.join(third_line)+'\n'+'    '.join(results)
  else:
    arranged_problems = '    '.join(first_line)+'\n'+'    '.join(second_line)+'\n'+'    '.join(third_line)

  return arranged_problems

def getLargestNumber(prob):
  largest_num = ''
  for p in prob:
    if(len(p) > len(largest_num)):
      largest_num = p
      
  return largest_num

def validate(problems):
  validation = dict()
  if(len(problems) > 5):
    validation['result'] = False
    validation['error'] = "Error: Too many problems."
    return validation
  for prob in problems:
    prob_list = prob.split()
    if(prob_list[1] != '+' and prob_list[1] != '-'):
      validation['result'] = False
      validation['error'] = "Error: Operator must be '+' or '-'."
      return validation
    if(re.match(r'^\d+$',prob_list[0]) is None or re.match(r'^\d+$',prob_list[2]) is None):
      validation['result'] = False
      validation['error'] = "Error: Numbers must only contain digits."
      return validation
    if(len(prob_list[0]) > 4 or len(prob_list[2]) > 4):
      validation['result'] = False
      validation['error'] = "Error: Numbers cannot be more than four digits."
      return validation
  validation['result'] = True
  return validation
