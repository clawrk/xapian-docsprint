# -*- coding: utf-8 -*-
#
# Getting Started with Xapian documentation build configuration file, created by
# sphinx-quickstart on Sun Oct 30 10:34:37 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import re
import atexit
from docutils import nodes, utils
from docutils.parsers.rst import roles
from docutils.parsers.rst.roles import set_classes
from sphinx.directives.code import CodeBlock, LiteralInclude, directives
from sphinx.directives.other import Include

languages = [
        'c++',
        'csharp',
        'java',
        'lua',
        'perl',
        'php',
        'python',
        'python3',
        'ruby',
        'tcl'
        ]

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '--list-languages':
        print(str.join(' ', languages))
        sys.exit(0)
    sys.exit(1)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.2'
# The full version, including alpha/beta/rc tags.
release = '1.2.19'

# General information about the project.
_project = u'Getting Started with Xapian'
_authors = u'Xapian Documentation Team & Contributors'
project = u'%s %s' % ( _project, version)
copyright = u'2003-2016 ' + _authors

github_project_url = 'https://github.com/xapian/xapian-docsprint/blob/master'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build', 'attic', 'language_specific']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%s v%s" % (_project, release)

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "%s v%s" % (_project, version)

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'GettingStartedwithXapiandoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'GettingStartedwithXapian.tex', project,
   _authors, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# Cause todos to be displayed.
todo_include_todos = True

# We want to check for errors at the end of each .rst file - the simplest way
# to achieve this seems to be to add an epilog which calls a custom hook
# macro.
rst_epilog = """
.. xapianendoffile:: dummy
"""

# Default to setting 'python' tag if none are set, and set highlight language
# appropriately.

current_source = None
last_example = None
examples = set()
examples_used = {}
examples_missing = []
total_errors = 0
errors = 0

highlight_language = None
for t in languages:
    if tags.has(t):
        if highlight_language is not None:
            print "Multiple language tags set (at least %s and %s)" % (highlight_language, t)
            sys.exit(1)
        highlight_language = t

if highlight_language is None:
    tags.add('python')
    highlight_language = 'python'

if highlight_language.startswith('python'):
    ext = '.py'
elif highlight_language == 'c++':
    ext = '.cc'
elif highlight_language == 'csharp':
    ext = '.cs'
elif highlight_language == 'perl':
    ext = '.pl'
elif highlight_language == 'ruby':
    ext = '.rb'
else:
    # java lua php tcl:
    ext = '.' + highlight_language

if highlight_language == 'php':
    # By default, pygments expects '<?php' and '?>' around PHP code, so we
    # need to set the 'startinline' option.
    from sphinx.highlighting import lexers
    from pygments.lexers.web import PhpLexer
    lexers['php'] = PhpLexer(startinline=True)

def github_link_node(name, rawtext, options=()):
    try:
        base = github_project_url
        if not base:
            raise AttributeError
    except AttributeError, err:
        raise ValueError(
            'github_project_url configuration value is not set (%s)' % str(err))
    slash = '/' if base[-1] != '/' else ''
    ref = base + slash + rawtext
    if not options:
        options = {}
    set_classes(options)
    node = nodes.reference(name, utils.unescape(name), refuri=ref,
                           **options)
    return node


# Return filename for example ex in the current language.
def xapian_code_example_filename(ex):
    return "code/%s/%s%s" % (highlight_language, ex, ext)

# Return the command to show in the generated docs.
def xapian_code_example_command(ex):
    if highlight_language == 'lua':
        return "lua %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'perl':
        return "perl %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'php':
        return "php %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'python':
        return "python2 %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'python3':
        return "python3 %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'ruby':
        return "ruby %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'tcl':
        return "tclsh %s" % xapian_code_example_filename(ex)
    elif highlight_language == 'c++':
        return "g++ `xapian-config --cxxflags` %s support.cc -o %s `xapian-config --libs`\n./%s" \
            % (xapian_code_example_filename(ex), ex, ex)
    elif highlight_language == 'csharp':
        return "cli-csc -unsafe -target:exe -out:%s.exe %s -r:XapianSharp.dll\n./%s.exe" \
            % (ex, xapian_code_example_filename(ex), ex)
    elif highlight_language == 'java':
        return "javac %s\njava %s" \
            % (xapian_code_example_filename(ex), ex)
    else:
        print "Unhandled highlight_language '%s'" % highlight_language
        sys.exit(1)

# Lookup tool name in the environment with default.
def get_tool_name(envvar, default):
    tool = os.environ.get(envvar, default)
    if re.search(r'[^-/_+.A-Za-z0-9]', tool):
        # Or we could actually escape it...
        print("Bad characters in $%s" % envvar)
        sys.exit(1)
    return tool

# Return the command to actually test run examples using.
def xapian_run_example_command(ex):
    if highlight_language == 'lua':
        lua = get_tool_name('LUA', 'lua')
        return "%s %s" % (lua, xapian_code_example_filename(ex))
    elif highlight_language == 'perl':
        perl = get_tool_name('PERL', 'perl')
        return "%s %s" % (perl, xapian_code_example_filename(ex))
    elif highlight_language == 'php':
        php = get_tool_name('PHP', 'php')
        return "%s %s" % (php, xapian_code_example_filename(ex))
    elif highlight_language == 'python':
        python = get_tool_name('PYTHON', 'python2')
        return "%s %s" % (python, xapian_code_example_filename(ex))
    elif highlight_language == 'python3':
        python3 = get_tool_name('PYTHON3', 'python3')
        return "%s %s" % (python3, xapian_code_example_filename(ex))
    elif highlight_language == 'ruby':
        ruby = get_tool_name('RUBY', 'ruby')
        return "%s %s" % (ruby, xapian_code_example_filename(ex))
    elif highlight_language == 'tcl':
        tclsh = get_tool_name('TCLSH', 'tclsh')
        return "%s %s" % (tclsh, xapian_code_example_filename(ex))
    elif highlight_language == 'c++':
        cxx = get_tool_name('CXX', 'g++')
        xapian_config = get_tool_name('XAPIAN_CONFIG', 'xapian-config')
        pfx = ''
        xcopt = '--libs'
        if xapian_config != 'xapian-config' and not xapian_config.startswith('/usr/'):
            if os.system('%s --ltlibs > /dev/null 2>&1' % xapian_config) != 0:
                print "'%s --ltlibs' doesn't work" % xapian_config
                sys.exit(1)
            if os.system('%s --libs > /dev/null 2>&1' % xapian_config) != 0:
                pfx = 'libtool --quiet --mode=link '
                xcopt = '--ltlibs'
        return "%s%s `%s --cxxflags` %s code/c++/support.cc -o code/c++/%s `%s %s`\ncode/c++/%s" \
            % (pfx, cxx, xapian_config, xapian_code_example_filename(ex), ex, xapian_config, xcopt, ex)
    elif highlight_language == 'csharp':
        csc = get_tool_name('CSC', 'cli-csc')
        return "%s -unsafe -target:exe -out:%s.exe %s -r:XapianSharp.dll\n./%s.exe" \
            % (csc, ex, xapian_code_example_filename(ex), ex)
    elif highlight_language == 'java':
        javac = get_tool_name('JAVAC', 'javac')
        java = get_tool_name('JAVA', 'java')
        return "%s %s\n%s %s" \
            % (javac, xapian_code_example_filename(ex), java, ex)
    else:
        print "Unhandled highlight_language '%s'" % highlight_language
        sys.exit(1)

class XapianCodeExample(LiteralInclude):
    option_spec = {
        'linenos': directives.flag,
        'tab-width': int,
        'language': directives.unchanged_required,
        'encoding': directives.encoding,
        'pyobject': directives.unchanged_required,
        'lines': directives.unchanged_required,
        'start-after': directives.unchanged_required,
        'end-before': directives.unchanged_required,
        'prepend': directives.unchanged_required,
        'append': directives.unchanged_required,
        'emphasize-lines': directives.unchanged_required,
        'marker': directives.unchanged_required,
    }

    def run(self):
        global last_example, examples
        last_example = self.arguments[0]
        examples.add(last_example)
        filename = xapian_code_example_filename(last_example)
        if not os.path.exists(filename):
            global examples_missing
            examples_missing.append(last_example)
            return [nodes.literal(text = 'No version of example %s in language %s - patches welcome!'
                % (last_example, highlight_language))]
        self.arguments[0] = "/" + filename
        if 'start-after' not in self.options and 'end-before' not in self.options:
            if 'marker' in self.options:
                marker = self.options['marker']
                del self.options['marker']
            else:
                marker = 'example code'
            self.options['start-after'] = 'Start of ' + marker
            self.options['end-before'] = 'End of ' + marker
        return super(XapianCodeExample, self).run()

# Usage:
# .. xapianexample:: search_filters2
directives.register_directive('xapianexample', XapianCodeExample)

def xapian_escape_args(args):
    def esc_char(match):
        return "=%02x" % ord(match.group(0))
    return re.sub(r' ', r'_', re.sub(r'[^-A-Za-z0-9 .]', esc_char, args))

class XapianRunExample(LiteralInclude):
    option_spec = {
        'args': directives.unchanged_required,
        'cleanfirst': directives.unchanged,
        'shouldfail': directives.unchanged,
        'silent': directives.flag,
    }

    def run(self):
        global current_source, errors
        source = self.state_machine.get_source_and_line()[0]
        if current_source != source:
            # New file, so clean up databases.
            os.system("rm -rf db filtersdb statesdb")
            current_source = source

        ex = self.arguments[0]

        filename = xapian_code_example_filename(ex)
        if not os.path.exists(filename):
            global examples_missing
            examples_missing.append(last_example)
            return [nodes.literal(text = 'No version of example %s in language %s - patches welcome!'
                % (last_example, highlight_language))]
        command = xapian_code_example_command(ex)

        cleanfirst = ''
        if 'cleanfirst' in self.options:
            cleanfirst = self.options['cleanfirst']
        shouldfail = 0
        if 'shouldfail' in self.options:
            shouldfail = self.options['shouldfail']
        if 'args' in self.options:
            args = self.options['args']
            command = "%s %s" % (command, args)
            esc_args = xapian_escape_args(args)
            fullout = "%s.%s.out" % (filename, esc_args)
            if os.path.exists(fullout):
                filename = fullout
            else:
                filename = filename + ".out"
        else:
            args = ''
            filename = filename + ".out"
        if not os.path.exists(filename):
            print '*** No output file %s in language %s - patches welcome!' \
                % (filename, highlight_language)

        global examples_used
        if ex in examples_used:
            examples_used[ex].append(args)
        else:
            examples_used[ex] = [args]

        command = xapian_code_example_command(ex)
        filename = xapian_code_example_filename(ex)
        if len(cleanfirst):
            if re.search(r'[^-A-Za-z0-9_ ]', cleanfirst):
                # Or we could actually escape it...
                print("Bad characters in cleanfirst: ''" % cleanfirst)
                sys.exit(1)
            os.system("rm -rf %s" % cleanfirst)
        run_command = xapian_run_example_command(ex)
        status = os.system("%s %s > tmp.out 2> tmp2.out" % (run_command, args))
        os.system("cat tmp2.out >> tmp.out")
        if shouldfail:
            if status == 0:
                print '%s: (%s): Exit status 0, expected failure' % (filename, source)
                errors += 1
        else:
            if status != 0:
                print '%s: (%s): Exit status %d, expected 0' % (filename, source, status)
                errors += 1
        esc_args = xapian_escape_args(args)
        fullout = "%s.%s.out" % (filename, esc_args)
        tmp_out = "%s.%s.tmp" % (filename, esc_args)
        os.rename("tmp.out", tmp_out)
        if os.path.exists(fullout):
            filename = fullout
        else:
            filename = filename + ".out"
        if not os.path.exists(filename):
            print '*** No output file %s in language %s - patches welcome!' \
                % (filename, highlight_language)
            os.unlink("tmp2.out")
        else:
            sys.stdout.flush()
            if os.system("diff -u %s %s 2>&1" % (tmp_out, filename)):
                print "$ %s %s" % (command, args)
                print "vimdiff %s %s" % (tmp_out, filename)
                errors += 1
            else:
                os.unlink(tmp_out)
                os.unlink("tmp2.out")

        if 'silent' in self.options:
            return []

        self.options['prepend'] = re.sub(r'(?m)^', r'$ ', command)
        # FIXME: Only want this syntax highlighting for lines starting '$'.
        # self.options['language'] = 'sh'
        self.options['language'] = 'none'
        self.arguments[0] = "/" + filename
        return super(XapianRunExample, self).run()

# Usage:
# .. xapianrunexample:: search_filters2
directives.register_directive('xapianrunexample', XapianRunExample)


class XapianCodeSnippet(CodeBlock):
    option_spec = { }

    def run(self):
        if highlight_language != self.arguments[0]:
            return []
        return super(XapianCodeSnippet, self).run()

# Usage:
# .. xapiancodesnippet:: python
#
#     def foo():
#          return 42
directives.register_directive('xapiancodesnippet', XapianCodeSnippet)

class XapianInclude(Include):
    def run(self):
        self.arguments[0] = re.sub(r'\bLANGUAGE\b', highlight_language, self.arguments[0])
        return super(XapianInclude, self).run()

# Usage:
# .. xapianinclude:: LANGUAGE/index
directives.register_directive('xapianinclude', XapianInclude)

def xapian_code_example_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    if ex == '^' and last_example:
        ex = last_example
    code_path = xapian_code_example_filename(ex)
    return [github_link_node(code_path, code_path, options)], []


def xapian_code_example_short_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    if ex == '^' and last_example:
        ex = last_example
    return [
        github_link_node(
            os.path.basename(ex) + ext,
            xapian_code_example_filename(ex), options)
        ], []


def xapian_example_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    return [github_link_node(ex, ex, options)], []


def xapian_example_short_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    ex = utils.unescape(etext)
    return [github_link_node(os.path.basename(ex), ex, options)], []

def xapian_class_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    c = utils.unescape(etext)
    if highlight_language == 'c++':
        return [nodes.literal(text = 'Xapian::' + c)], []
    elif highlight_language == 'csharp':
        return [nodes.literal(text = 'Xapian.' + c)], []
    elif highlight_language == 'java':
        return [nodes.literal(text = 'org.xapian.' + c)], []
    elif highlight_language == 'lua':
        return [nodes.literal(text = 'xapian.' + c)], []
    elif highlight_language == 'perl':
        return [nodes.literal(text = 'Search::Xapian::' + c)], []
    elif highlight_language == 'php':
        return [nodes.literal(text = 'Xapian' + c)], []
    elif highlight_language == 'python':
        return [nodes.literal(text = 'xapian.' + c)], []
    elif highlight_language == 'python3':
        return [nodes.literal(text = 'xapian.' + c)], []
    elif highlight_language == 'ruby':
        return [nodes.literal(text = 'Xapian::' + c)], []
    elif highlight_language == 'tcl':
        return [nodes.literal(text = 'xapian::' + c)], []
    else:
        print "Unhandled highlight_language '%s'" % highlight_language
        sys.exit(1)

def decorate_param(m):
    # Avoid decorating literals or constants.
    # FIXME: Doesn't really handle expressions.
    if not re.match(r'^[a-z][a-z0-9_]+$', m.group(2)):
        return m.group(0)
    return m.group(1) + '$' + m.group(2)

def decorate_variables(t):
    if highlight_language in ('perl', 'php', 'ruby'):
        # Add a $ in front of each parameter which is a variable
        return re.sub(r'([(,]\s*)([^),]+)', decorate_param, t)
    # Correct for: c++ csharp java lua python python3
    # FIXME: I think tcl is going to need cleverer handling
    return t

def xapian_just_method_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    # FIXME: Need to adjust method names for csharp, java and ruby
    m = decorate_variables(utils.unescape(etext))
    return [nodes.literal(text = m)], []

def xapian_method_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    cm = utils.unescape(etext)
    if highlight_language == 'c++':
        return [nodes.literal(text = 'Xapian::' + cm)], []
    elif highlight_language == 'csharp':
        # FIXME: Need to adjust method names for csharp
        cm = re.sub(r'::', r'.', cm)
        return [nodes.literal(text = 'Xapian.' + cm)], []
    elif highlight_language == 'java':
        # FIXME: Need to adjust method names for java
        cm = re.sub(r'::', r'.', cm)
        return [nodes.literal(text = 'org.xapian.' + cm)], []
    elif highlight_language == 'lua':
        return [nodes.literal(text = 'xapian.' + cm)], []
    elif highlight_language == 'perl':
        # Add a $ in front of each parameter.
        cm = decorate_variables(cm)
        return [nodes.literal(text = 'Search::Xapian::' + cm)], []
    elif highlight_language == 'php':
        # Add a $ in front of each parameter.
        cm = decorate_variables(cm)
        return [nodes.literal(text = 'Xapian' + cm)], []
    elif highlight_language.startswith('python'):
        cm = re.sub(r'::', r'.', cm)
        return [nodes.literal(text = 'xapian.' + cm)], []
    elif highlight_language == 'ruby':
        # FIXME: Need to adjust method names for ruby
        return [nodes.literal(text = 'Xapian::' + cm)], []
    elif highlight_language == 'tcl':
        return [nodes.literal(text = 'xapian::' + cm)], []
    else:
        print "Unhandled highlight_language '%s'" % highlight_language
        sys.exit(1)

def xapian_variable_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    m = utils.unescape(etext)
    if highlight_language in ('perl', 'php', 'ruby'):
        return [nodes.literal(text = '$' + m)], []
    # Correct for: c++ csharp java lua python python3
    # FIXME: I think tcl is going to need cleverer handling
    return [nodes.literal(text = m)], []

def xapian_literal_role(typ, rawtext, etext, lineno, inliner,
                                 options=(), content=[]):
    t = utils.unescape(etext)
    if highlight_language == 'c++':
        return [nodes.literal(text = t)], []
    elif highlight_language == 'csharp':
        if t == 'DBL_MAX':
            t = 'double.MaxValue'
        elif t == 'false':
            t = 'false'
        elif t == 'true':
            t = 'true'
        elif t == 'NULL':
            t = 'null'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language == 'java':
        if t == 'DBL_MAX':
            t = 'java.lang.Double.MAX_VALUE'
        elif t == 'false':
            t = 'false'
        elif t == 'true':
            t = 'true'
        elif t == 'NULL':
            t = 'null'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language == 'lua':
        if t == 'DBL_MAX':
            # FIXME: is this available in lua?
            t = 'DBL_MAX'
        elif t == 'false':
            t = 'false'
        elif t == 'true':
            t = 'true'
        elif t == 'NULL':
            t = 'nil'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language == 'perl':
        if t == 'DBL_MAX':
            t = 'POSIX::DBL_MAX'
        elif t == 'false':
            t = '0'
        elif t == 'true':
            t = '1'
        elif t == 'NULL':
            t = 'undef'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language == 'php':
        if t == 'DBL_MAX':
            # Doesn't seem to a simple way to get this in PHP.
            # INF is infinity though.  FIXME: check this works.
            t = 'INF'
        elif t == 'false':
            t = 'FALSE'
        elif t == 'true':
            t = 'TRUE'
        elif t == 'NULL':
            t = 'NULL'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language.startswith('python'):
        if t == 'DBL_MAX':
            t = 'sys.float_info.max'
        elif t == 'false':
            t = 'False'
        elif t == 'true':
            t = 'True'
        elif t == 'NULL':
            t = 'None'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language == 'ruby':
        if t == 'DBL_MAX':
            t = 'Float::MAX'
        elif t == 'false':
            t = 'false'
        elif t == 'true':
            t = 'true'
        elif t == 'NULL':
            t = 'nil'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []
    elif highlight_language == 'tcl':
        if t == 'DBL_MAX':
            # FIXME: is this available in tcl?
            t = 'DBL_MAX'
        elif t == 'false':
            t = 'false'
        elif t == 'true':
            t = 'true'
        elif t == 'NULL':
            # FIXME: Tcl doesn't have natively have a 'null'
            # https://wiki.tcl.tk/17441 but SWIG-generated wrappers use the
            # string NULL to represent a NULL pointer:
            # http://www.swig.org/Doc3.0/Tcl.html#Tcl_nn19
            t = 'NULL'
        else:
            print "Unhandled literal '%s' for %s" % (t, highlight_language)
            sys.exit(1)
        return [nodes.literal(text = t)], []

    else:
        print "Unhandled highlight_language '%s'" % highlight_language
        sys.exit(1)

# Usage:
#
# The previous example was :xapian-code-example:`^`.
#
# The foo example is in :xapian-code-example:`foo`.
roles.register_local_role('xapian-code-example', xapian_code_example_role)
roles.register_local_role('xapian-basename-code-example', xapian_code_example_short_role)
roles.register_local_role('xapian-basename-example', xapian_example_short_role)
roles.register_local_role('xapian-example', xapian_example_role)
# e.g. :xapian-class:`Database`
roles.register_local_role('xapian-class', xapian_class_role)
# e.g. :xapian-just-method:`add_matchspy(spy)`
roles.register_local_role('xapian-just-method', xapian_just_method_role)
# e.g. :xapian-method:`Database::reopen()`
roles.register_local_role('xapian-method', xapian_method_role)
# e.g. :xapian-variable:`spy`
roles.register_local_role('xapian-variable', xapian_variable_role)
# e.g. :xapian-just-constant:`OP_OR`
# (Currently this just does the same as the method version, but when more
# languages are added this may change).
roles.register_local_role('xapian-just-constant', xapian_just_method_role)
# e.g. :xapian-constant:`Query::OP_OR`
# (Currently this just does the same as the method version, but when more
# languages are added this may change).
roles.register_local_role('xapian-constant', xapian_method_role)
# e.g. :xapian-literal:`DBL_MAX`
# Currently handles true, false, NULL, DBL_MAX.
roles.register_local_role('xapian-literal', xapian_literal_role)

class XapianEndOfFile(LiteralInclude):
    option_spec = { }

    def run(self):
        global errors, total_errors
        if errors > 0:
            total_errors += errors
            errors = 0
            raise self.error("%d error(s) with example code" % errors)
        return []

# "..xapianendoffile:" is used from the rst_epilog - it's not for manual use.
directives.register_directive('xapianendoffile', XapianEndOfFile)

def xapian_check_examples():
    global examples, examples_used, examples_missing, total_errors
    for ex in examples:
        if ex in examples_used:
            del examples_used[ex]
            continue
        if ex in examples_missing:
            continue
        print "Example %s isn't shown to be run anywhere" % ex
        total_errors += 1

    for ex in examples_used:
        print "Example %s is used but never shown anywhere" % ex
        total_errors += 1

    m_done = set()
    for ex in examples_missing:
        # Remove duplicate entries
        if ex in m_done:
            continue
        m_done.add(ex)
        print '*** No version of example %s in language %s - patches welcome!' \
            % (ex, highlight_language)

    if total_errors > 0:
        print "*** %d total error(s) with example code" % total_errors
        raise SystemExit()

atexit.register(xapian_check_examples)
