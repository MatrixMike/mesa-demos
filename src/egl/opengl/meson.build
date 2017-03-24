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

executable('eglinfo', 'eglinfo.c', dependencies : dep_egl,
           include_directories : inc_util)
executable('peglgears', 'peglgears.c', dependencies : [dep_gl, dep_egl, dep_m],
           include_directories : inc_util)
if with_libdrm and with_gbm
  executable('eglkms', 'eglkms.c', dependencies : [dep_gl, dep_egl, dep_libdrm, dep_gbm],
             include_directories : inc_util)
endif
if with_x11
  executable('eglgears_x11', 'eglgears.c', dependencies : [dep_m, dep_gl, dep_eglut_x11],
             include_directories : inc_util)
  executable('egltri_x11', 'egltri.c', dependencies : [dep_gl, dep_eglut_x11],
             include_directories : inc_util)
  executable('xeglgears', 'xeglgears.c', dependencies : [dep_m, dep_gl, dep_eglut_x11],
             include_directories : inc_util)
  executable('xeglthreads', 'xeglthreads.c',
             dependencies : [dep_m, dep_gl, dep_eglut_x11, dep_thread],
             include_directories : inc_util)
endif
