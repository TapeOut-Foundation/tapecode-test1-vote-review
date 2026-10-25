import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
plt.rcParams['font.sans-serif']=['PingFang SC','Arial Unicode MS','Heiti SC']; plt.rcParams['axes.unicode_minus']=False
C3,C56='#2a6fb0','#d9822b'; INK='#222'
O='../'
# chart 1: 所有口径
sc=[('A 官方严格票\n(首轮冻结名单)',56,45),('B 严格+复核\n快照账号',71,78),('C B+边缘2个\n(simplede22等)',77,78),('D 最终口径\n+1票地址',78,84),('E 全部快照\n不审核',95,165),('F 快照−033\n转投账号19人',95,108)]
fig,ax=plt.subplots(figsize=(12,5.4),dpi=150); x=np.arange(len(sc)); w=.36
b1=ax.bar(x-w/2,[s[1] for s in sc],w-.04,color=C3,label='003 @MostQin'); b2=ax.bar(x+w/2,[s[2] for s in sc],w-.04,color=C56,label='056 @Miloxx23')
for b in list(b1)+list(b2): ax.text(b.get_x()+b.get_width()/2,b.get_height()+2,int(b.get_height()),ha='center',color=INK,fontsize=11)
ax.set_xticks(x); ax.set_xticklabels([s[0] for s in sc],fontsize=9.5,color=INK)
ax.set_title('所有口径下的结果（除官方首轮冻结名单外，056 均领先）',fontsize=14,color=INK,loc='left')
ax.legend(frameon=False,loc='upper left'); [ax.spines[k].set_visible(False) for k in ('top','right')]
ax.yaxis.grid(True,color='#e5e5e5'); ax.set_axisbelow(True); ax.set_ylim(0,185)
fig.tight_layout(); fig.savefig(O+'chart1_scenarios.png')
# chart 2: 边缘账号组合
fig,ax=plt.subplots(figsize=(9,4.6),dpi=150)
M=np.zeros((4,5))
for a in range(4):
    for b in range(5):
        M[a,b]=1 if 84-3*a>78-3*b else (0.5 if 84-3*a==78-3*b else 0)
ax.imshow(M,origin='lower',cmap=ListedColormap([C3,'#b7b7b7',C56]),vmin=0,vmax=1,aspect='auto',alpha=.9,extent=(-.5,4.5,-.5,3.5))
for a in range(4):
    for b in range(5):
        y,x=84-3*a,78-3*b
        ax.text(b,a,f'{x}:{y}',ha='center',va='center',color='white',fontsize=11,fontweight='bold')
ax.set_xlabel('003 方剔除的边缘快照账号数（共 4 个：每个 3 票）',color=INK); ax.set_ylabel('056 方剔除的边缘快照账号数（共 3 个）',color=INK)
ax.set_title('边缘账号逐个拿掉后的结果（格内为 003:056；橙=056 胜，蓝=003 胜，灰=平）',fontsize=11.5,color=INK,loc='left')
ax.set_xticks(range(5)); ax.set_yticks(range(4))
fig.tight_layout(); fig.savefig(O+'chart2_pivot_grid.png')
