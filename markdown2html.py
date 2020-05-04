#!/usr/bin/python3
"""convert markdown to html"""

if __name__ == '__main__':
    import sys
    import re

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1]) as f, open(sys.argv[2], 'w') as out:
            IN_LIST = False

            for line in f:
                if IN_LIST:
                    if line.startswith('- '):
                        out.write('<li>{}</li>'.format(line[:-1]))
                    else:
                        out.write('</ul>\n')
                        IN_LIST = False

                match = re.match('^#{1,6} ', line)
                if match:
                    level = len(match.group().strip())
                    out.write("<h{}>{}</h{}>\n".format(
                        level, line[level+1:-1], level))
                    continue

                if line.startswith('- '):
                    IN_LIST = True
                    out.write('<ul>\n<li>{}</li>\n'.format(line[:-1]))
                else:
                    out.write(line)
    except FileNotFoundError:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
