#!/usr/bin/env python3
import os
import argparse
import multiprocessing as mp

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #
parser.add_argument('-p','-P','--process', type = int, default= 4)     #

#
args = parser.parse_args()
INPUT = args.input
Process = args.process

F = open(INPUT,'r').read().split("\n")

def run(i):
  os.system(i)

def multicore(Pool=Process):
  pool = mp.Pool(processes=Pool)
  for i in F:
    # Working function "echo" and the arg 'i'
    multi_res = [pool.apply_async(run,(i,))]
  pool.close()
  pool.join()

if __name__ == '__main__':
  multicore()
