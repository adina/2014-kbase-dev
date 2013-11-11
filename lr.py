import sys
from scipy import stats

#To run, python lr.py ph abundance.txt mgm*
meta = sys.argv[3:]
abundance = sys.argv[2]
key_phrase = str(sys.argv[1])

#Gets the dictionary of the metadata abundance values for each sample
d_meta = {}
for f in meta:
    file = open(f, 'r')
    d_meta[f] = {}
    for line in file:
        dat = line.rstrip().split('\t')
        if key_phrase in dat[1].split(' '):
            d_meta[f] = dat[2]


#Gets the dictionary of the abundances of each function for each sample
d_func = {}

for n, line in enumerate(open(abundance, 'r')):
    if n == 0:
        dat = line.rstrip().split('\t')
        mgm_ids = dat[1:]
        d_mgm_map = {}
        for n2, x in enumerate(mgm_ids):
            d_mgm_map[n2] = x
    else:
        dat = line.rstrip().split('\t')
        function = dat[0]
        for n3, x in enumerate(dat[1:]):
            mg_id_map = d_mgm_map[n3]
            if d_func.has_key(mg_id_map):
                d_func[mg_id_map][function] = x
            else:
                d_func[mg_id_map] = {}
                d_func[mg_id_map][function] = x

#Checks correlation
sorted_func = sorted(d_func[d_mgm_map[0]].keys())

for each_func in sorted_func:
    l_meta = []
    l_function = []
    for mgm in d_func.keys():
        l_meta.append(float(d_meta[mgm]))
        l_function.append(float(d_func[mgm][each_func]))
    gradient, intercept, r_value, p_value, std_err = stats.linregress(l_meta, l_function)
    if p_value < 0.05:
        print key_phrase, each_func, p_value, '*'
    #else:
    #    print key_phrase, each_func, p_value

    
