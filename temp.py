from ruamel.yaml import YAML
import os, sys
from glob import glob

# def convert_pelican_to_hugo(lines):
#     info = {}
# 
#     for l in lines:
#         contents = l.strip().split(':')
#         if len(contents) < 2:
#             continue
# 
#         tag, attribute = contents[0], ':'.join(contents[1:])
#         tag = tag.strip()
#         attribute = attribute.strip()
# 
#         if tag == 'Title':
#             info['title'] = attribute
#         elif tag == 'Date':
#             info['publishDate'] = attribute.replace(' ', 'T') + ':00'
#         elif tag == 'Category':
#             info['categories'] = attribute
#         elif tag == 'Tags':
#             info['tags'] = [a.strip() for a in attribute.split(',')]
#         elif tag == 'Slug':
#             info['slug'] = attribute
#         elif tag == 'Summary':
#             info['summary'] = attribute
#         else:
#             # print(f"Skipping file with title {info['title']}, got tag {tag}")
#             return None
# 
#     return info

tgts = [y for x in os.walk(sys.argv[1]) for y in glob(os.path.join(x[0], '*.md'))]

# yaml = YAML(typ='rt')

for file in tgts:
    file_parts = file.split('/')
    file_prefix = '/'.join(file_parts[1:3])
    file_lines = open(file, 'r').readlines()
    with open(file, 'w') as outfile:
        for l in file_lines:
            t = l.replace('(res', f'(/{file_prefix}/res')
            outfile.write(t)

    # header_line_idx = file_lines.index('\n')
    # header_lines = open(file, 'r').readlines()[:header_line_idx]
    # header_data = convert_pelican_to_hugo(header_lines)
    # if not header_data:
    #     print(f'Could not parse file {file}')
    # else:
        # with open(file, 'w') as outfile:
        #     outfile.write('---\n')
        #     yaml.dump(header_data, outfile)
        #     outfile.write('---\n')
        #     for l in file_lines[header_line_idx:]:
        #         outfile.write(l)
