==========
Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

- Added Django@master to the build matrix and fixed current problems
  with Django 2.0.
- Fixed all flake8_ warnings that are not explicitly ignored.
- Added our own documentation_ build on readthedocs.
- Removed documentation and tests from PyPI builds.


`0.2`_ (2016-11-12)
~~~~~~~~~~~~~~~~~~~

- Fixed a few deprecation warnings and raised the minimum Django version
  to 1.10, thanks ``base_manager_name``.


`0.1`_ (2016-09-03)
~~~~~~~~~~~~~~~~~~~

- Initial public release under the new name ``django-cte-forest``.
- Added support for Django 1.8 and Python 3.
- Fixed a few minor bugs related to hardcoded names for the virtual
  fields added by the CTE.
- Added continuous integration on Travis CI.


.. _0.1: https://github.com/matthiask/django-cte-forest/commit/6d89293b
.. _0.2: https://github.com/matthiask/django-cte-forest/compare/0.1...0.2
.. _Next version: https://github.com/matthiask/django-cte-forest/compare/0.2...master

.. _flake8: https://flake8.readthedocs.io/
.. _documentation: https://django-cte-forest.readthedocs.io/
