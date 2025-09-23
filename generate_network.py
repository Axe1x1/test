import csv
from collections import defaultdict
import math

# Input file
CSV_FILE = 'dialogue_records.csv'

# Output svg
SVG_FILE = 'relationship_graph.svg'

# Read data
speaker_counts = defaultdict(int)
edge_counts = defaultdict(int)

with open(CSV_FILE, encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row:
            continue
        speaker = row[0].lstrip('\ufeff').strip()
        target_field = row[2].strip()
        # Clean target names
        target_field = target_field.replace('？','').replace('?','')
        target_field = target_field.replace('「','').replace('」','')
        targets = [t.strip() for t in target_field.split('&') if t.strip()]
        if not targets:
            targets = ['Unknown']
        speaker_counts[speaker] += 1
        for tgt in targets:
            edge_counts[(speaker, tgt)] += 1

# Determine node ordering and sizes
nodes = list(speaker_counts.keys())
N = len(nodes)

max_lines = max(speaker_counts.values())
max_edge = max(edge_counts.values()) if edge_counts else 1

# Circular layout
R = 200
coords = {}
for i, node in enumerate(nodes):
    angle = 2*math.pi*i/N
    x = R*math.cos(angle)
    y = R*math.sin(angle)
    coords[node] = (x, y)

# Generate SVG
svg_elements = []
svg_elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{2*R+100}" height="{2*R+100}" viewBox="{-R-50} {-R-50} {2*R+100} {2*R+100}">')

# Draw edges
for (src, dst), w in edge_counts.items():
    x1, y1 = coords.get(src, (0,0))
    x2, y2 = coords.get(dst, (0,0))
    width = 1 + 4*w/max_edge
    svg_elements.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="gray" stroke-width="{width}" opacity="0.6"/>')

# Draw nodes
for node, count in speaker_counts.items():
    x, y = coords[node]
    radius = 5 + 20*count/max_lines
    svg_elements.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="skyblue" stroke="black"/>')
    svg_elements.append(f'<text x="{x}" y="{y}" text-anchor="middle" dy="4" font-size="12">{node}</text>')

svg_elements.append('</svg>')

with open(SVG_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_elements))

print('Generated', SVG_FILE)
