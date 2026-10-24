from load import *
import collections,csv,json
R={n:detail(n+'投票明细') for n in ['56进3','3进2','2进1']}
r1=collections.defaultdict(list); r2=collections.defaultdict(list)
for r in R['56进3']: r1[r[2]].append(r[0])
for r in R['3进2']: r2[r[2]].append(r[0])
final=R['2进1']
out=[]
for r in final:
    if r[7]=='是' and r[8]!='是':
        a=r[2]; w=r[0]
        o1=r1.get(a,[]); o2=r2.get(a,[])
        if w=='056':
            if '033' in o1: g='A 033转投账号'
            elif not o1 and not o2: g='B R3首次出现'
            elif not o1: g='B R2首次出现'
            elif o1==['056']: g='C 自R1起一直投056'
            else: g='D 其他(R1投别的作品)'
        else:
            if o1==['003'] and o2==['003']: g='E 自R1起一直投003'
            elif not o1 and not o2: g='G R3首次出现'
            elif not o1: g='G R2首次出现'
            else: g='F 中途转投003'
        out.append((w,a,g,'/'.join(o1) or '-','/'.join(o2) or '-'))
json.dump(out,open('../data/conclusions/groups.json','w'),ensure_ascii=False)
print(collections.Counter((w,g) for w,a,g,_,_ in out))
