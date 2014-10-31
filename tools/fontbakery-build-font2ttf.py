#!/usr/bin/env python
# coding: utf-8
# Copyright 2013 The Font Bakery Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.
#
# Convert a source font into OpenType-TTF and optionally also OpenType-CFF
#
# $ fontbakery-build-font2ttf.py font.sfd font.ttf font.otf
# $ fontbakery-build-font2ttf.py font.sfdir font.ttf font.otf
# $ fontbakery-build-font2ttf.py font.ufo font.ttf font.otf
# $ fontbakery-build-font2ttf.py font.otf font.ttf
import argparse
import sys

from bakery_cli.scripts import font2ttf


parser = argparse.ArgumentParser()
parser.add_argument('--otf', type=str)
parser.add_argument('source', type=str)
parser.add_argument('ttf', type=str)


args = parser.parse_args()

font2ttf.convert(args.source, args.ttf, args.otf)
