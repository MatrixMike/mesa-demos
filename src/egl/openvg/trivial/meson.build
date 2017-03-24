# Copyright © 2017 Intel Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

common_deps = [dep_x11, dep_egl, dep_vg, dep_m]

executables = [
  'cap',
  'clear',
  'color_transform',
  'coord',
  'dash',
  'ellipse',
  'filter',
  'gradorigin',
  'image',
  'layer',
  'lineto',
  'lingrad',
  'lookup',
  'mask4',
  'mask',
  'mask_render',
  'paint',
  'path3',
  'radialgrad',
  'readpixels',
  'roundedrect',
  'star-nonzero',
  'star-oddeven',
  'stroke2',
  'stroke',
]
foreach e : executables
  executable(e, e + '.c', dependencies : common_deps)
endforeach

libvgcommon = static_library('vgcommon', ['eglcommon.c', 'eglcommon.h'])
executable('arc', 'arc.c', dependencies : common_deps, link_with : libvgcommon)
executable('blend', 'blend.c', dependencies : common_deps, link_with : libvgcommon)
