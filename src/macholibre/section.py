#!/usr/bin/python

'''
Copyright 2016 Aaron Stephens <aaron@icebrg.io>, ICEBRG

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


class Section(object):

    # Constructor
    def __init__(self, name=None, segname=None, addr=None, offset=None,
                 align=None, reloff=None, nreloc=None, size=None):
        # Fields
        self.name = name
        self.segname = segname
        self.addr = addr
        self.offset = offset
        self.align = align
        self.reloff = reloff
        self.nreloc = nreloc
        self.size = size
        self.type = None
        self.attrs = []

    # Generators
    def gen_attrs(self):
        for i in self.attrs:
            yield i

    # Functions
    def add_attr(self, attr): self.attrs.append(attr)
