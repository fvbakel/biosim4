#!/usr/bin/python3

import igraph
import os
from argparse import ArgumentParser

def make_graph(filename):
    basename = os.path.splitext(filename)[0]
    output_filename = basename + '.svg'
    # load data into a graph
    g = igraph.Graph.Read_Ncol(filename, names=True, weights=True)

    for v in g.vs:
        v['size'] = 35
        v['label'] = v['name']
        if v['name'] in ['Lx', 'Ly', 'EDx', 'EDy', 'ED', 'Bfd', 'Blr', 'Gen', 'LMx', 'LMy', 'LPf', 'LPb', 'Pop', 'Pfd', 'Plr', 'Osc', 'Age', 'Rnd', 'Sg', 'Sfd', 'Slr']:
            v['color'] = 'lightblue'
        elif v['name'] in ['MvX', 'MvY', 'MvE', 'MvW', 'MvN', 'MvS', 'Mfd', 'MvL', 'MvR', 'MRL', 'Mrv', 'Mrn', 'OSC', 'LPD', 'Res', 'SG', 'Klf' ]:
            v['color'] = 'lightpink'
        else:
            v['color'] = 'lightgrey'

    # convert edge weights to color and size
    for e in g.es:
        #print(e['weight'])
        if e['weight'] < 0:
            e['color'] = 'lightcoral'
        elif e['weight'] == 0:
            e['color'] = 'grey'
        else:
            e['color'] = 'green'

        width = abs(e['weight'])
        e['width'] = 1 + 1.25 * (width / 8192.0)


    # plot graph

    print(len(g.vs))

    if len(g.vs) < 6:
        bbox = (300,300)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 12:
        bbox = (400,400)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 18:
        bbox = (500,500)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 24:
        bbox = (520,520)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 26:
        bbox = (800,800)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 50:
        bbox = (1000,1000)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 130:
        bbox = (1200,1000)
        layout = 'fruchterman_reingold'
    elif len(g.vs) < 150:
        bbox = (4000,4000)
        layout = 'fruchterman_reingold'
        for v in g.vs:
            v['size'] = v['size'] * 1.5
    elif len(g.vs) < 200:
        bbox = (4000,4000)
        layout = 'kamada_kawai'
        for v in g.vs:
            v['size'] = v['size'] * 2
    else:
        bbox = (8000,8000)
        layout = 'fruchterman_reingold'

    igraph.plot(g, output_filename, edge_curved=True, bbox=bbox, margin=64, layout=layout)


def process_dir(input_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith("net.txt"):
            make_graph(os.path.join(input_dir, filename))

if __name__ == "__main__":
    parser = ArgumentParser(description="Convert a net txt file to a graph\n")
    #requiredNamed = parser.add_argument_group('required arguments')
    parser.add_argument("--file", "-f", help="Filename of the net txt file", type=str,default="net.txt")
    parser.add_argument("--dir", "-d", help="Directory with net txt files", type=str,default=None)

    args = parser.parse_args()
    filename =args.file
    dirname =args.dir

    if dirname is None:
        make_graph(filename)
    else:
        process_dir(dirname)


