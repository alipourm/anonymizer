import os, sys





def anonymize_fname(fname):
    name_parts = fname.split('_')
    uhid = name_parts[1]
    anonymid = str(hash(uhid))
    return fname.replace(uhid, anonymid)




topdir = sys.argv[1]   
    
for root, dirs, files in os.walk(topdir, topdown=False):
    for fname in files:
        if fname.endswith('.py'):
        
            orig_filepath = os.path.join(root, fname)
            anon_filepath = os.path.join(root, anonymize_fname(fname)) + '.NEW'
            with open(orig_filepath, 'r') as f:
                with open(anon_filepath, 'w') as newf:
                    print 'processing {} ...'.format(orig_filepath), 
                    lines = f.readlines()
                    newlines = map(lambda x: '# {}'.format(hash(x)) if x.startswith('#') else x , lines)
                    newf.write('\n'.join(newlines))
                    newf.flush()
                    newf.close()
                    f.close()
                    print 'DONE'
   
