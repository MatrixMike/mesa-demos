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

libpbutil = static_library('pbutil', ['pbutil.c', 'pbutil.h'])

# FIXME: xdemo requires xmesa.h

executables = [
  'glsync',
  'glxdemo',
  'glxgears',
  'glxgears_pixmap',
  'glxcontexts',
  'glxheads',
  'glxpixmap',
  'glxpbdemo',
  'glxsnoop',
  'glxswapcontrol',
  'manywin',
  'multictx',
  'offset',
  'overlay',
  'shape',
  'sharedtex',
  'texture_from_pixmap',
  'wincopy',
  'xfont',
  'yuvrect_client',
]
foreach e : executables
  executable(
    e,
    e + '.c',
    dependencies : [dep_gl, dep_glu, dep_x11, dep_xext, dep_m],
    include_directories : inc_util,
    install : true,
  )
endforeach

executables = [
  'glthreads',
  'sharedtex_mt',
]
foreach e : executables
  executable(
    e,
    e + '.c',
    dependencies : [dep_gl, dep_x11, dep_thread, dep_m],
    include_directories : inc_util,
    install : true,
  )
endforeach

executables = [
  'glxgears_fbconfig',
  'pbinfo',
  'pbdemo',
]
foreach e : executables
  executable(
    e,
    e + '.c',
    dependencies : [dep_gl, dep_x11, dep_m],
    link_with : libpbutil,
    include_directories : inc_util,
    install : true,
  )
endforeach

executable(
  'glxinfo',
  ['glxinfo.c', 'glinfo_common.c', 'glinfo_common.h'],
  dependencies : [dep_x11, dep_gl],
  include_directories : inc_util,
  install : true,
)

executable(
  'xrotfontdemo',
  ['xrotfontdemo.c', 'xuserotfont.c', 'xuserotfont.h'],
  dependencies : [dep_x11, dep_gl],
  include_directories : inc_util,
  install : true,
)
