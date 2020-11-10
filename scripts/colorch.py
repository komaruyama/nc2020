import pathlib
import re
import cairosvg

def text(path):
    with open(path, encoding='utf-8_sig', errors='ignore') as f:
        return f.read()

def out(path, text):
    with open(path, mode='w', encoding='utf-8_sig', errors='ignore') as f:
        return f.write(text)

def single_ch(text, tag, pre_rep_tps):
    t_tag = r'<\s*' + tag + r'(.|\s)+?' + r'/>'
    r_tag = re.compile(t_tag)
    ret = ''
    se = r_tag.search(text)
    pos = 0
    while se is not None:
        ret += text[pos:pos+se.start()]
        gre = se.group()
        for pre, rep in pre_rep_tps:
            if pre in gre:
                gre = gre.replace(pre, rep)
                break
        ret += gre
        pos = pos + se.end()
        se = r_tag.search(text[pos:])
    return ret + text[pos:]

def apply(args):
    pydir = pathlib.Path(__file__).resolve().parent
    outdir = pydir / 'out'
    outdir.mkdir(exist_ok=True)

    for file in pydir.glob('*.svg'):
        print(file)
        with open(file, encoding='utf-8_sig', errors='ignore') as fr:
            text = fr.read()

        for tag, pre_rep_tps in args:
            text = single_ch(text, tag, pre_rep_tps)

        with open(outdir / file.name, mode='w', encoding='utf-8_sig', errors='ignore') as fw:
            fw.write(text)
        outf = str(outdir / file.name)
        pdff = outf.replace('.svg', '.pdf')
        cairosvg.svg2pdf(url=(outdir / file.name), write_to=pdff)

def main1():
    args = []

    t_line = 'line'
    p_line = []
    p_line.append( ('stroke:#b8ed8e;stroke-width:5', 'stroke:#4fc94f;stroke-width:7') )
    p_line.append( ('stroke:#ed8e9c;stroke-width:5', 'stroke:#d43346;stroke-width:7') )
    p_line.append( ('stroke:#4fd0ff;stroke-width:5', 'stroke:#287d9c;stroke-width:7') )
    p_line.append( ('stroke:#ffc14f;stroke-width:5', 'stroke:#ffb226;stroke-width:7') )
    p_line.append( ('stroke:#90d1c2;stroke-width:1.5', 'stroke:#90d1c2;stroke-width:1.5;stroke-dasharray: 1 1') )
    # '#ed8e9c' '#d43346'
    # '#4fd0ff' '#287d9c'
    # '#ffc14f' '#ffb226'
    args.append( (t_line, p_line) )

    t_circle = 'circle'
    p_circle = []
    p_circle.append( ('stroke:#b8ed8e;stroke-width:2', 'stroke:#4fc94f;stroke-width:3') )
    p_circle.append( ('stroke:#ed8e9c;stroke-width:2', 'stroke:#d43346;stroke-width:3') )
    p_circle.append( ('stroke:#4fd0ff;stroke-width:2', 'stroke:#287d9c;stroke-width:3') )
    p_circle.append( ('stroke:#ffc14f;stroke-width:2', 'stroke:#ffb226;stroke-width:3') )

    p_circle.append( ('stroke:#c31f37;stroke-width:4', 'stroke:#7a0018;stroke-width:4.5') )
    p_circle.append( ('stroke:#00749f;stroke-width:4', 'stroke:#33c8ff;stroke-width:4.5') )
    p_circle.append( ('stroke:#4d9217;stroke-width:4', 'stroke:#1f540d;stroke-width:4.5') )
    args.append( (t_circle, p_circle) )

    apply(args)

if __name__ == '__main__':
    main1()
    # text ='''
    #   <line
    #      x1="-1380"
    #      x2="-1410"
    #      y1="123.89545"
    #      y2="123.89545"
    #      id="line64"
    #      style="fill:none;stroke:#b8ed8e;stroke-width:5" />'''
    # print(text)
    # t_tag = r'<\s*?' + 'line' + r'(.|\s)+?' + '/>'
    # r_tag = re.compile(t_tag)
    # rtt = r_tag.search(text)
    # st = rtt.start()
    # en = rtt.end()
    # print(text[st:en])
