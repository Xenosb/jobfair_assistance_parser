#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, re, csv

class CompanyData():
  def __init__(self):
    self.student = ''
    self.coffee = 0
    self.water = 0
    self.assistance = 0

def main(argv):
  arg_len = len(argv)
  if arg_len == 1:
    i = open(argv[0], 'r')
    o = sys.stdout
  elif arg_len == 2:
    i = open(argv[0], 'r')
    o = open(argv[1], 'wb')
  else:
    print('Run command as: praser <input.file> [<output.file>]')
    return 0;

  companies = parse_data(i)
  write(companies, o)

  i.close()
  o.close()

#@mpetrunic, Ericsson Nikola Tesla želi vodu na štandu B21!

def parse_data(in_file):
  lines = filter(None, (line.rstrip() for line in in_file))
  valid = filter(lambda line: line[0]=='@' and line[-1]=='!' and 'želi' in line, lines)
  companies = dict()

  for line in valid:
    parts = line.split(' želi ')
    words = (parts[0].split(' ')[0], parts[0].split(', ')[1], parts[1].split(' ')[0])
    (student, company_name, service) = words
    if company_name not in companies:
      companies[company_name] = CompanyData()
      companies[company_name].student = student
    if service == 'vodu':
      companies[company_name].water += 1
    elif service == 'kavu':
      companies[company_name].coffee += 1
    elif service == 'pomoć':
      companies[company_name].assistance += 1
  return companies
  
def write(companies, o):
  print(len(companies))
  wr = csv.writer(o, quoting=csv.QUOTE_ALL)
  for company in companies:
    wr.writerow([company, companies[company].student, companies[company].water, companies[company].coffee, companies[company].assistance])

if __name__ == "__main__":
  main(sys.argv[1:])