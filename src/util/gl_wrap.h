#ifndef GL_WRAP_H
#define GL_WRAP_H

#include <epoxy/gl.h>
#ifdef __APPLE__
#  include <OpenGL/glu.h>
#else
#  include <GL/glu.h>
#endif

#ifndef GLAPIENTRY
#define GLAPIENTRY
#endif

#endif /* ! GL_WRAP_H */
