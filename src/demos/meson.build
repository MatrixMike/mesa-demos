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
  'arbfplight.c',
  'arbfslight.c',
  'arbocclude.c',
  'arbocclude2.c',
  'bounce.c',
  'clearspd.c',
  'dinoshade.c',
  'fbotexture.c',
  'fogcoord.c',
  'fplight.c',
  'fslight.c',
  'gamma.c',
  'gearbox.c',
  'gears.c',
  'geartrain.c',
  'glinfo.c',
  'morph3d.c',
  'paltex.c',
  'pixeltest.c',
  'pointblast.c',
  'ray.c',
  'renormal.c',
  'shadowtex.c',
  'singlebuffer.c',
  'spectex.c',
  'spriteblast.c',
  'stex3d.c',
  'terrain.c',
  'tessdemo.c',
  'texenv.c',
  'trispd.c',
  'vao_demo.c',
  'copypix.c',
  'cubemap.c',
  'cuberender.c',
  'dissolve.c',
  'drawpix.c',
  'engine.c',
  'fbo_firecube.c',
  'fire.c',
  'gloss.c',
  'gltestperf.c',
  'ipers.c',
  'isosurf.c',
  'lodbias.c',
  'multiarb.c',
  'projtex.c',
  'readpix.c',
  'reflect.c',
  'teapot.c',
  'texcyl.c',
  'textures.c',
  'tunnel2.c',
  'winpos.c',
]

foreach e : executables
  executable(e, e, dependencies : [dep_gl, dep_epoxy, dep_util, dep_m], install : true)
endforeach
executable('tunnel', ['tunnel.c', 'tunneldat.h'], dependencies : dep_util, install : true)
executable('rain', ['rain.cxx', 'particles.cxx'], dependencies : dep_util, install : true)
