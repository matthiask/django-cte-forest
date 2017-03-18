# -*- coding: utf-8 -*-
#
# This document is free and open-source software, subject to the OSI-approved
# BSD license below.
#
# Copyright (c) 2011 - 2013 Alexis Petrounias <www.petrounias.org>,
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# * Neither the name of the author nor the names of its contributors may be used
# to endorse or promote products derived from this software without specific
# prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Sphinx configuration for Django CTE Forest.
"""

import os
import sys


# add package root as well as dummy Django application so models can be
# imported
sys.path.append(os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'cte_forest_test.settings'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Django CTE Forest'
copyright = u'2011 - 2013 Alexis Petrounias <www.petrounias.org>'

version = __import__('cte_forest').__version__
release = version

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'DjangoCTEForestdoc'

latex_documents = [(
    'index',
    'DjangoCTEForest.tex',
    u'Django CTE Forest Documentation',
    u'Alexis Petrounias \\textless{}www.petrounias.org\\textgreater{}',
    'manual',
)]

man_pages = [(
    'index',
    'djangocteforest',
    u'Django CTE Forest Documentation',
    [u'Alexis Petrounias <www.petrounias.org>'],
    1,
)]

texinfo_documents = [
  ('index', 'DjangoCTEForest', u'Django CTE Forest Documentation',
   u'Alexis Petrounias <www.petrounias.org>', 'DjangoCTEForest',
  'Experimental implementation of Adjacency-List trees for Django'
  ' using PostgreSQL Common Table Expressions (CTE).',
   'Miscellaneous'),
]
