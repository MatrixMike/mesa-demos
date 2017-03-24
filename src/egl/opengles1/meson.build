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

common_deps = [dep_gles1, dep_egl, dep_x11, dep_m]

executables = [
  'bindtex.c',
  'es1_info.c',
  'msaa.c',
  'pbuffer.c',
  'render_tex.c',
  'texture_from_pixmap.c',
  'two_win.c',
]
foreach e : executables
  executable(e, e, dependencies : common_deps)
endforeach

executables = [
  ['clear', 'clear.c'],
  ['drawtex_x11', 'drawtex.c'],
  ['gears_x11', 'gears.c'],
  ['torus_x11', 'torus.c'],
  ['tri_x11', 'tri.c'],
]
foreach e : executables
  executable(e[0], e[1], dependencies : [common_deps, dep_eglut_x11])
endforeach
