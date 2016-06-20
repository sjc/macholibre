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


class SymbolTable(object):

    # Constructor
    def __init__(self, offset=None, nsyms=None):
        # Fields
        self.offset = offset
        self.nsyms = nsyms
        self.il = None
        self.nl = None
        self.ie = None
        self.ne = None
        self.iu = None
        self.nu = None
        self.syms = []

    # Generators
    def gen_syms(self):
        for i in self.syms:
            yield i

    # Functions
    def add_sym(self, sym): self.syms.append(sym)
