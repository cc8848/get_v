# coding:GBK
'''
Created on Jun 28, 2015

@author: �����
@mail: llych#126.com
'''

import sys
import getopt
import os
from get_v import main

def usage():
    print '''
    Usage:{0} --url=http://xxoo.xx  --dir=/data
    --url=��Ƶ��ַ
    --dir=������Ƶ��ŵ�·��
    
Ŀǰ֧��:'''.format(os.path.basename(sys.argv[0]))
    main.help()

if __name__ == '__main__':
    try:
        opts,args=getopt.getopt(sys.argv[1:],"h",["help","url=", "dir="])
        opts=dict(opts)
        if '-h' in opts.keys() or '--help' in opts.keys():
            usage()
            sys.exit(2)
        if len(opts)==0:
            usage()
            sys.exit(2)

        url=opts.get('--url',None)
        dir=opts.get('--dir',None)
        #print url,dir
        
    except Exception, e:
        usage()
        sys.exit(2)
    main.main(url,dir)