#author heyaoyu
#:
#main sample

def main():
  print 'local change'
  print 'main'
  print 'another change will conflict, both added'
  print 'local change will conflict, both added'

if __name__=='__main__':
  main()