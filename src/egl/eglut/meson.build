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

if with_egl and with_x11
  libeglut_x11 = static_library(
    'eglut_x11',
    ['eglut.c', 'eglut.h', 'eglutint.h', 'eglut_x11.c'],
    dependencies : [dep_x11, dep_egl],
  )

  dep_eglut_x11 = declare_dependency(
    link_with : libeglut_x11,
    include_directories : include_directories('.'),
  )
else
  dep_eglut_x11 = []
endif

if with_wayland
  libeglut_wl = static_library(
    'eglut_wl',
    ['eglut.c', 'eglut.h', 'eglutint.h', 'eglut_wayland.c'],
    dependencies : [dep_wayland, dep_egl],
  )

  dep_eglut_wl = declare_dependency(
    link_with : libeglut_wl,
    include_directories : include_directories('.'),
  )
else
  dep_eglut_wl = []
endif
