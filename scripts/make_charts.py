import json,csv,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['PingFang SC','Arial Unicode MS','Heiti SC']; plt.rcParams['axes.unicode_minus']=False
C3,C56='#2a6fb0','#d9822b'; INK='#222'; MUT='#666'
O='../'
# chart 1: scenarios
sc=[('A 官方历史严格票\n(现行公示)',56,45),('B 严格 + 全部快照持有人\n(无任何审核)',95,165),('C 快照持有人 − 33转投账号19人\n(其余全部计入)',95,108),('D 复核后\n(本报告)',71,78)]
fig,ax=plt.subplots(figsize=(10,5.2),dpi=150); x=np.arange(4); w=.36
b1=ax.bar(x-w/2,[s[1] for s in sc],w-.04,color=C3,label='003 @MostQin'); b2=ax.bar(x+w/2,[s[2] for s in sc],w-.04,color=C56,label='056 @Miloxx23')
for b in list(b1)+list(b2): ax.text(b.get_x()+b.get_width()/2,b.get_height()+2,int(b.get_height()),ha='center',color=INK,fontsize=12)
ax.set_xticks(x); ax.set_xticklabels([s[0] for s in sc],fontsize=10,color=INK)
ax.set_title('2进1 三种计票口径下的结果（同一份公示数据）',fontsize=14,color=INK,loc='left')
ax.legend(frameon=False,loc='upper left'); [ax.spines[k].set_visible(False) for k in ('top','right')]
ax.yaxis.grid(True,color='#e5e5e5'); ax.set_axisbelow(True); ax.set_ylim(0,185)
fig.tight_layout(); fig.savefig(O+'chart1_scenarios.png')
# chart 2: 复核后翻盘边界  056 方被剔除 k 个合格账号 (0..11)，003 方多被认可 m 个 (0..8)
fig,ax=plt.subplots(figsize=(9,5.6),dpi=150)
M=np.zeros((9,12))
for m in range(9):
    for k in range(12):
        M[m,k]=1 if 78-3*k>71+3*m else 0
from matplotlib.colors import ListedColormap
ax.imshow(M,origin='lower',cmap=ListedColormap([C3,C56]),aspect='auto',alpha=.85,extent=(-.5,11.5,-.5,8.5))
ax.set_xlabel('056 方被剔除的合格账号数（共 11 个，每个 3 票）',color=INK); ax.set_ylabel('003 方多被认可的账号数（另有 8 个未计入 / 存疑）',color=INK)
ax.set_title('复核后：要剔除或补计多少个账号才会翻盘？',fontsize=13,color=INK,loc='left')
ax.text(5.2,6,'003 胜',color='white',fontsize=16); ax.text(0.7,5,'056 胜区域在左下角',color='white',fontsize=11)
ax.scatter([0],[0],c='white',s=60,zorder=3); ax.annotate('现状：003 71 : 056 78',(0,0),(3.5,0.6),color='white',arrowprops=dict(arrowstyle='-',color='white'))
ax.set_xticks(range(0,12)); ax.set_yticks(range(0,9))
fig.tight_layout(); fig.savefig(O+'chart2_pivot_grid.png')
