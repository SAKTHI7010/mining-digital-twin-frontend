import json

with open('assets/html/process_scene.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
with open('assets/js/process_scene.js', 'r', encoding='utf-8') as js_f:
    js_content = js_f.read()

data_str = json.dumps({})
html_content = html_content.replace('// INJECT_DATA_HERE', f'window.plantData = {data_str};')
html_content = html_content.replace('<script id="main-script"></script>', f'<script>\n{js_content}\n</script>')

with open('scratch/out.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
