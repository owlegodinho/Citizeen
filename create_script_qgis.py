import os

def write_script():
    os.chdir(orig_dir)
    with open('python_qgis.py', 'w') as f:
    lines = f.read().splitlines()
    for line in lines:
        if line.startswith('layer_path'):
            f.write(line.replace('D:/test/f.xml', 'C:/try/X.xml'))
        else:
            f.write(line)

