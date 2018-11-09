#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib as mpl


def format_label(value):
    return '{:0.0f}%'.format(value)


mpl.rcParams['font.size'] = 17.0

fig, ax = plt.subplots()
ax.axis('equal')

values = [26, 74]
text_labels = ['reproducible', 'irreproducible']
colors = ['#6D9CCE', '#F13F52']

text_labels = [
    '{value}% {text}'.format(text=text, value=value)
    for text, value in zip(text_labels, values)
    ]

radius = 1.36
width = 0.5
label_position = 0.8
start_angle = 10

circle, _, _ = ax.pie(
    values, colors=colors,
    radius=radius, startangle=start_angle,
    autopct=format_label, pctdistance=label_position
    )

plt.setp(circle, width=width, edgecolor='white')

ax.legend(circle, text_labels, frameon=False, loc='center')

plt.tight_layout()

plt.savefig('img/reproducibility_ratio_from_stodden.png')
