# REPORT.md -> report.html -> REPORT.pdf（用本机 Chrome 无头打印）
import markdown,subprocess,pathlib,sys
root=pathlib.Path(__file__).resolve().parent.parent
md=(root/'REPORT.md').read_text(encoding='utf-8')
body=markdown.markdown(md,extensions=['tables','fenced_code'])
css='''body{font-family:"PingFang SC","Helvetica Neue",sans-serif;max-width:900px;margin:32px auto;padding:0 24px;color:#1b2033;line-height:1.7;font-size:14px}
h1{font-size:26px;border-bottom:3px solid #4da3ff;padding-bottom:8px}h2{font-size:20px;margin-top:30px;border-left:5px solid #ff9a3d;padding-left:10px}h3{font-size:16px;margin-top:20px}
table{border-collapse:collapse;width:100%;margin:10px 0}th,td{border:1px solid #d5daea;padding:6px 10px;text-align:left}th{background:#eef2fb}
blockquote{background:#f4f7ff;border-left:4px solid #4da3ff;margin:12px 0;padding:6px 14px;color:#444}img{max-width:100%;border:1px solid #d5daea;border-radius:8px;margin:8px 0}
code{background:#eef2fb;padding:1px 5px;border-radius:4px;font-size:12.5px}a{color:#2a6fb0}tr,img{page-break-inside:avoid}'''
html=f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>Test1 NFT 设计大赛 · 投票复核报告</title><style>{css}</style></head><body>{body}</body></html>'
(root/'report.html').write_text(html,encoding='utf-8')
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
subprocess.run([chrome,'--headless=new','--disable-gpu','--no-pdf-header-footer','--allow-file-access-from-files',f'--print-to-pdf={root/"REPORT.pdf"}',f'file://{root/"report.html"}'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
(root/'report.html').unlink()
