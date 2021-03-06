# -*- coding: utf-8 -*-
"""
Created on Fri Nov 2016
"""
__author__ = "yuhao"

import os
import json

PARAMS = {
    'datafl': 'testData/test.gslib',
    'icolx': 0,
    'icoly': 1,
    'icolvr': 3,
    'tmin': -1.0e21,
    'tmax': 1.0e21,
    'idbg': 3,
    'dbgfl': 'kb2d.dbg',
    'outfl': 'out.dat',
    'nx': 98,
    'xmn': 100,
    'xsiz': 200,
    'ny': 79,
    'ymn': 200,
    'ysiz': 1.0,
    'nxdis': 1,
    'nydis': 1,
    'ndmin': 3,
    'ndmax': 10,
    'radius': 12000,
    'isk': 0,
    'skmean': 14.69588,
    'nst': 1,
    'c0': 0.05,
    'it': [0],
    'cc': [0.65],
    'azm': [90],
    'a_max':[3715.9],
    'a_min': [3715.9]
}

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
PARAM_DIR = os.path.join(PARENT_DIR, 'testData')

with open(os.path.join(PARAM_DIR, 'test_krige2d.par'), 'w') as fout:
    fout.write(json.dumps(PARAMS, sort_keys=True, indent=4))
