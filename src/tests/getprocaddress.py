#!/usr/bin/env python


# Helper for the getprocaddress.c test.

import argparse
import sys,re, os


if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('mesa_path')
        parser.add_argument('c_file')
        parser.add_argument('-f', '--file_name')
        args = parser.parse_args()

        if not args.file_name:
            args.file_name = os.path.join(args.mesa_path, "gl_API.xml")

        sys.path.insert(0, args.mesa_path)
        import gl_XML
        import license



def FindTestFunctions(c_file):
	"""Scan getprocaddress.c for lines that start with "test_" to find
	extension function tests.  Return a list of names found."""
	functions = []
	f = open(c_file)
	if not f:
		return functions
	for line in f.readlines():
		v = re.search("^test_([a-zA-Z0-9]+)", line)
		if v:
			func = v.group(1)
			functions.append(func)
	f.close
	return functions


class PrintExports(gl_XML.gl_print_base):
	def __init__(self, c_file):
		gl_XML.gl_print_base.__init__(self)

		self.name = "getprocaddress.py (from Mesa)"
		self.license = license.bsd_license_template % ( \
"""Copyright (C) 1999-2001  Brian Paul   All Rights Reserved.
(C) Copyright IBM Corporation 2004""", "BRIAN PAUL, IBM")

		self.tests = FindTestFunctions(c_file)
		self.prevCategory = ""
		return


	def printRealHeader(self):
		print """
struct name_test_pair {
   const char *name;
   GLboolean (*test)(generic_func);
};

static struct name_test_pair functions[] = {"""

	def printBody(self, api):
		prev_category = None
		

		for f in api.functionIterateByCategory():
			[category, num] = api.get_category_for_name( f.name )
			if category != prev_category:
				print '   { "-%s", NULL},' % category
				prev_category = category
			
			test = "NULL"
			for name in f.entry_points:
				if name in self.tests:
					test = "test_%s" % name
					break

			print '   { "gl%s", %s },' % (f.name, test)

		print ''
		print '   { NULL, NULL }'
		print '};'
		print ''
		return


if __name__ == '__main__':
	printer = PrintExports(args.c_file)

	api = gl_XML.parse_GL_API( args.file_name, gl_XML.gl_item_factory() )

	printer.Print( api )
