#!/usr/bin/python
import argparse
import re
import sys, os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), 
            default=sys.stdout)
    parser.add_argument('--template', '-t', default=None)
    parser.add_argument('--reps', '-r', nargs='*')
    params = parser.parse_args()
    return params

def reps_dict(extras):
    out = {}
    
    # Skip the loop if there's nothing to parse
    if not extras: return out

    for item in extras:
        parts = item.split('=', 2)
        if len(parts) == 2:
            out[parts[0]] = parts[1]
    return out

def get_template_path(params):
    TPL_PATH = os.getenv('HOME') + '/.touchas/'
    out = None
    if params.template == None:
        out_path = params.outfile.name
        ext = re.search(r'\.(.*?)$',  out_path)
        if ext != None:
            out = TPL_PATH + ext.group(1) + '.tpl'
    else:
        out = TPL_PATH + params.template + '.tpl'
    return out

def run_template(path, reps):
    def handle(m):
        print m.group(1), '---', m.group(2)
        if reps.has_key(m.group(1)):
            return reps[m.group(1)]
        else:
            return m.group(2)
    with open(path) as f: text = f.read()
    needle = r'\(%\s*(.*?)\|(.*?)\s*%\)'
    return re.sub(needle, handle, text, flags=re.DOTALL)
        
if __name__ == '__main__':
    params = parse_args()
    reps = reps_dict(params.reps)
    templ_path = get_template_path(params)
    if templ_path == None:
        print "Invalid path"
        sys.exit(1)
    data = run_template(templ_path, reps)
    params.outfile.write(data)
    params.outfile.close()

