# © 2017 Intel Corporation

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

project('mesa-demos', ['c', 'cpp'], license : 'MIT', version : '8.3.0')

host_system = host_machine.system()
cc = meson.get_compiler('c')
# Meson uses 'cpp' for C++, rather than using both cpp and cxx just stick with
# meson's naming scheme, even though many associate 'cpp' with 'C
# PreProcessor', not C++
cpp = meson.get_compiler('cpp')

require_native = (host_system != 'windows' and host_system != 'darwin')

dep_egl = []
dep_gl = []
dep_gles1 = []
dep_gles2 = []
dep_glu = []
dep_m = []
dep_osmesa = []
dep_thread = []
dep_wayland = []
dep_x11 = []
dep_xext = []
dep_glut = dependency('freeglut', required : false)
if dep_glut.found()
  add_project_arguments('-DHAVE_FREEGLUT', language : 'c')
  add_project_arguments('-DHAVE_FREEGLUT', language : 'cpp')
else
  dep_glut = cc.find_library('glut')
  if cc.has_function('glutInitContextProfile', args : ['GL/glut.h', 'GL/freeglut.h'])
    add_project_arguments('-DHAVE_FREEGLUT', language : 'c')
    add_project_arguments('-DHAVE_FREEGLUT', language : 'cpp')
  endif
endif

if host_system == 'windows'
  dep_gl = cc.find_library('opengl32')
  dep_glu = cc.find_library('glu32')
else
  dep_gl = dependency('gl')
  dep_glu = dependency('glu')
endif

if host_system.startswith('linux')
  add_project_arguments('-D_GNU_SOURCE', '-DPTHREADS', language : 'c')
  add_project_arguments('-D_GNU_SOURCE', '-DPTHREADS', language : 'cpp')
  dep_thread = dependency('threads')
  dep_m = cc.find_library('m')
  dep_xll = dependency('x11')
elif host_system.contains('gnu')
  add_project_arguments('-D_GNU_SOURCE', '-DPTHREADS', language : 'c')
  add_project_arguments('-D_GNU_SOURCE', '-DPTHREADS', language : 'cpp')
  dep_thread = dependency('threads')
  dep_xll = dependency('x11')
elif host_system.startswith('solaris')
  add_project_arguments('-DPTHREADS', '-DSVR4', language : 'c')
  add_project_arguments('-DPTHREADS', '-DSVR4', language : 'cpp')
  dep_thread = dependency('threads')
  dep_xll = dependency('x11')
  # TODO: some things are missing here
elif host_system.startswith('cygwin')
  add_project_arguments('-DPTHREADS', language : 'c')
  add_project_arguments('-DPTHREADS', language : 'cpp')
  dep_thread = dependency('threads')
  dep_xll = dependency('x11')
elif host_system == 'windows'
  # Nobody likes to include windows.h:
  # - Microsoft's GL/gl.h header depends on windows.h but doesn't include it;
  # - GLEW temporarily defines the necessary defines but undefines them later
  # - certain GLUT distributions don't include it;
  # - most of our programs are meant to be portable so don't include it.
  #
  # We could try to replicate the windows.h definitions required by GL/gl.h,
  # but the build time savings don't compensate the constant headaches that
  # brings, so instead we force windows.h to be included on every file.
  if cc.get_id() == 'msvc'
    # TODO
  else  # MinGw
    add_project_arguments('--include', 'windows.h', language : 'c')
    add_project_arguments('--include', 'windows.h', language : 'cpp')

    if cc.has_argument('-static-libgcc')
      add_project_link_arguments('-static-libgcc', language : 'c')
    endif
    if cc.has_argument('-static-libstdc++')
      add_project_link_arguments('-static-libstdc++', language : 'cpp')
    endif

    # XXX: this probably isn't right, but it gets things building
    add_project_arguments('-DGLUT_DISABLE_ATEXIT_HACK', language : 'c')
    add_project_arguments('-DGLUT_DISABLE_ATEXIT_HACK', language : 'cpp')
  endif
  
  # Don't define min/max macros
  add_project_arguments('-DNOMINMAX', language : 'c')
  add_project_arguments('-DNOMINMAX', language : 'cpp')

  # MSVC and MinGW only define and use APIENTRY
  add_project_arguments('-DGLAPIENTRY=__stdcall', language : 'c')
  add_project_arguments('-DGLAPIENTRY=__stdcall', language : 'cpp')
endif

with_egl = false
with_freetype2 = false
with_gbm = false
with_gles1 = false
with_gles2 = false
with_libdrm = false
with_mesa_source = get_option('mesa-sourcedir') != 'none'
with_osmesa = false
with_rbug = get_option('with-rbug')
with_vg = false
with_wayland = false
with_wgl = false
with_x11 = false
if with_rbug
  if not with_mesa_source
    error('rbug requires mesa source')
  endif
endif
if with_mesa_source
  prog_python = find_program('python2', 'python')
  mesa_source = get_option('mesa-sourcedir')
endif
if get_option('with-egl') != 'no'
  dep_egl = dependency('egl', required : get_option('with-egl') == 'yes')
  with_egl = dep_egl.found()
endif
if get_option('with-wgl') != 'no'
  with_wgl = (host_system == 'windows')
  if not with_wgl and get_option('with-wgl') == 'yes'
    error('WGL only support when targeting Windows')
  endif
endif
if get_option('with-gles1') != 'no'
  dep_gles1 = dependency('glesv1_cm', required : get_option('with-gles1') == 'yes')
  with_gles1 = dep_gles1.found()
endif
if get_option('with-gles2') != 'no'
  dep_gles2 = dependency('glesv2', required : get_option('with-gles2') == 'yes')
  with_gles2 = dep_gles2.found()
endif
# TODO: I'm not sure this is correct.
if get_option('with-vg') != 'no'
  dep_vg = dependency('vg', required : get_option('with-vg') == 'yes')
  with_vg = dep_vg.found()
endif
if get_option('with-osmesa') != 'no'
  dep_osmesa = dependency('osmesa', required : get_option('with-osmesa') == 'yes')
  with_osmesa = dep_osmesa.found()
endif
if get_option('with-libdrm') != 'no'
  dep_libdrm = dependency('libdrm', required : get_option('with-libdrm') == 'yes')
  with_libdrm = dep_libdrm.found()
endif
if get_option('with-x11') != 'no'
  dep_x11 = dependency('x11', required : get_option('with-x11') == 'yes')
  with_x11 = dep_x11.found()
  if dep_x11.found()
    dep_xext = dependency('xext')
  endif
endif
if get_option('with-wayland') != 'no'
  dep_wayland += dependency('wayland-client', required : get_option('with-wayland') == 'yes')
  dep_wayland += dependency('wayland-egl', required : get_option('with-wayland') == 'yes')
  with_wayland = dep_wayland.found()
endif
if get_option('with-gbm') != 'no'
  dep_gbm = dependency('gbm', required : get_option('with-gbm') == 'yes')
  with_gbm = dep_gbm.found()
endif
if get_option('with-freetype2') != 'no'
  dep_freetype2 = dependency('freetype2', required : get_option('with-freetype2') == 'yes')
  with_freetype2 = dep_freetype2.found()
endif

if cc.get_id() == 'msvc'
  # TODO:
else
  potential_c_flags = [
    '-Wall',
    '-Wpointer-arith',
    '-Wstrict-prototypes',
    '-Wmissing-prototypes',
    '-Wmissing-declarations',
    '-Wnested-externs',
    '-Wno-strict-aliasing',
    '-Wbad-function-cast',
    '-Wold-style-definition',
    '-Wdeclaration-after-statement',
  ]
endif

foreach f : potential_c_flags
  if cc.has_argument(f)
    add_project_arguments(f, language : 'c')
  endif
endforeach

# TODO: Make this configurable
add_project_arguments('-DDEMOS_DATA_DIR="../data/"', language: 'c')
add_project_arguments('-DDEMOS_DATA_DIR="../data/"', language: 'cpp')

# subprojects are targets, they must be set after project arguments
dep_epoxy = dependency('epoxy', required : require_native)
if not dep_epoxy.found()
  epoxy = subproject('epoxy')
  dep_epoxy = epoxy.get_variable('libepoxy_dep')
endif

subdir('src')
