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

executables = [
  'antialias',
  'arbfpspec',
  'arbfptest1',
  'arbfptexture',
  'arbfptrig',
  'arbgpuprog',
  'arbnpot',
  'arbnpot-mipmap',
  'arbvparray',
  'arbvptest1',
  'arbvptest3',
  'arbvptorus',
  'arbvpwarpmesh',
  'backspecular',
  'blendxor',
  'blitfb',
  'bufferobj',
  'bug_3050',
  'bug_3101',
  'bug_texstore_i8',
  'calibrate_rast',
  'clip',
  'condrender',
  'copypixrate',
  'cva',
  'cva_huge',
  'cylwrap',
  'drawbuffers',
  'drawbuffers2',
  'drawstencil',
  'exactrast',
  'ext422square',
  'fbotest1',
  'fbotest2',
  'fbotest3',
  'fogcoord',
  'fptest1',
  'fptexture',
  'front-back-modes',
  'getteximage',
  'glutfx',
  'interleave',
  'lineclip',
  'line-sample',
  'manytex',
  'mapbufrange',
  'minmag',
  'mipgen',
  'mipmap_comp',
  'mipmap_comp_tests',
  'mipmap_tunnel',
  'multipal',
  'multitexarray',
  'multiwindow',
  'no_s3tc',
  'packedpixels',
  'pbo',
  'persp_hint',
  'prim',
  'prog_parameter',
  'quads',
  'random',
  'readrate',
  'rubberband',
  'scissor',
  'scissor-viewport',
  'seccolor',
  'shader_api',
  'shadow-sample',
  'stencilreaddraw',
  'stencilwrap',
  'step',
  'streaming_rect',
  'subtex',
  'subtexrate',
  'tex1d',
  'texcmp',
  'texcompress2',
  'texcompsub',
  'texdown',
  'texfilt',
  'texgenmix',
  'texleak',
  'texline',
  'texobj',
  'unfilledclip',
  'viewmemory',
  'vparray',
  'vpeval',
  'vptest1',
  'vptest2',
  'vptest3',
  'vptorus',
  'vpwarpmesh',
  'yuvrect',
  'yuvsquare',
  'zbitmap',
  'zcomp',
  'zdrawpix',
  'zreaddraw',
]
foreach e : executables
  executable(
    'test_' + e, e + '.c',
    dependencies : [dep_glut, dep_glu, dep_epoxy, dep_m],
    include_directories : inc_util
  )
endforeach

executables = [
  'afsmultiarb',
  'arraytexture',
  'bug_3195',
  'bumpmap',
  'floattex',
  'fillrate',
  'invert',
  'linehacks',
  'mipmap_limits',
  'mipmap_view',
  'shader-interp',
  'texrect',
]
foreach e : executables
  executable('test_' + e, e + '.c', dependencies : [dep_util, dep_m])
endforeach

executables = [
  'auxbuffer',
  'jkrahntest',
  'sharedtex',
  'texobjshare',
]
foreach e : executables
  executable(
    'test_' + e, e + '.c',
    dependencies : [dep_glut, dep_epoxy, dep_glu, dep_x11, dep_m],
    include_directories : inc_util,
  )
endforeach

if with_mesa_source
  getproclist_h = custom_target(
    'getproclist_h',
    input : ['getprocaddress.py', join_paths(mesa_source, 'src/mapi/glapi/gen'),
             'getprocaddress.c'],
    output : ['getproclist.h'],
    command : [prog_python, '@INPUT0@', '@INPUT1@', '@INPUT2@'],
    capture : true,
    depend_files : join_paths(mesa_source, 'src/mapi/glapi/gen/gl_API.xml')
  )

  executable(
    'getproclist',
    ['getprocaddress.c', getproclist_h],
    dependencies : [dep_glut, dep_epoxy, dep_glu, dep_x11, dep_m],
    include_directories : inc_util,
  )
endif
