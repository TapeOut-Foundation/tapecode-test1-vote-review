// 在已登录 X 的浏览器页面里运行（只读）：滚动当前账号的主页或 /with_replies 页，
// 收集自发帖、回复对象、转帖，并标出含关键词的原创、回复核心账号、转帖了关键词/核心账号内容的条目。
// 用法：打开 https://x.com/<账号> 与 https://x.com/<账号>/with_replies，在控制台里执行
//   await scan('<账号>')
// 注意：转帖识别依赖 socialContext 含“转帖/repost”，本次核查中尚未用已知转帖案例校准。
async function scan(h){
  window.scrollTo(0,0);
  for(let k=0;k<10&&!document.querySelector('article[data-testid="tweet"]');k++)await new Promise(r=>setTimeout(r,700));
  const seen=new Map();const H=h.toLowerCase();
  for(let i=0;i<14;i++){
    let prev='';
    document.querySelectorAll('article[data-testid="tweet"]').forEach(a=>{
      const t=a.querySelector('time');const l=t&&t.closest('a');const u=l?l.getAttribute('href'):'';
      const un=((a.querySelector('[data-testid="User-Name"]')||{}).innerText||'');const m=un.match(/@\w+/);const who=m?m[0].toLowerCase():'';
      const txt=((a.querySelector('[data-testid="tweetText"]')||{}).innerText||'').replace(/\s+/g,' ');
      const ctx=((a.querySelector('[data-testid="socialContext"]')||{}).innerText||'');
      const rt=/转帖|repost/i.test(ctx);
      if(u&&!seen.has(u)){const own=who==='@'+H;if(own||rt)seen.set(u,{u:u.replace(/^\//,''),d:t.getAttribute('datetime').slice(5,10),au:who,own:own?1:0,rt:rt?1:0,re:(own&&!rt&&prev&&prev!==who)?prev:'',x:txt.slice(0,120)});}
      prev=who;
    });
    window.scrollBy(0,2000);await new Promise(r=>setTimeout(r,900));
  }
  const a=[...seen.values()];
  const kw=/tapeout|tapecode|test1|bem|nand|latch|矿机|礦機|流片|電路|电路|firsto|tapeup|晶体管|晶體管|tapekit|巨兽|behemoth/i;
  const core=/@(tapeoutworld|firstoai|blonskr|tapeoutcf|xing8047|0x_dadada|tapeuptony|bitcoin2themars|sciencedegens|glen_ignix|tapeupio|fabx_global|foundrytape|cryptoloser9|miloxx23|mostqin)/;
  const ownkw=a.filter(p=>p.own&&!p.rt&&kw.test(p.x));
  const ownre=a.filter(p=>p.own&&!p.rt&&core.test(p.re));
  const rts=a.filter(p=>p.rt);
  const rtk=rts.filter(p=>kw.test(p.x)||core.test(p.au));
  return {h,own:a.filter(p=>p.own&&!p.rt).length,rt:rts.length,ownKW:ownkw,replyToCore:ownre,rtKWorCore:rtk};
}
