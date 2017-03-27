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

common_deps = [dep_epoxy, dep_glut, dep_glu]

sotest = executable(
  'sotest',
  ['sotest.c', 'framework.c', 'framework.h'],
  dependencies : common_deps,
  include_directories : inc_util,
)
cltest = executable(
  'cltest',
  ['cltest.c', 'framework.c', 'framework.h'],
  dependencies : common_deps,
  include_directories : inc_util,
)
vstest = executable(
  'vstest',
  ['vstest.c', 'framework.c', 'framework.h'],
  dependencies : common_deps,
  include_directories : inc_util,
)

# FIXME: piping to grep isn't portable
# Instead these should just return 1 if there is a failure
test('sotest', sotest)
test('cltest', cltest)
test('vstest', vstest)
