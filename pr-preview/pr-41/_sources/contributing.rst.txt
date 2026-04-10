.. include:: ./links.inc

Contributing Guide
==================

Tracker
-------

Contributions in all forms to this wiki are welcome. This wiki is hosted and build on
`GitHub <project github_>`_. The `issue tracker <project issue tracker_>`_ can be used
to propose changes, additions and report issues and solutions found when working with
EEG data from our site.

Pull Requests
-------------

If comfortable with git and collaborative development, pull request to the repository
are welcome. The wiki is organized as a python project with a sphinx documentation.
The documentation, used to generate the website HTML pages, is written in
`reStructuredText format <rst_>`_ in the `doc <project github doc_>`_ folder.

In a pull request, the automatic workflows will build the documentation and check for
conformity. Any warnings and errors during the build process must be resolved before
the pull request can be merged.

Building the documentation locally
----------------------------------

To confirm that the documentation build without warning, it is possible to build the
documentation locally. After cloning the repository, the project and its dependencies
can be installed in a python environment with:

.. code-block:: bash

    $ pip install -e path/to/eeg-wiki[all]

Additionally, `pre-commit`_ hooks are available to check for common errors before
committing changes.

.. code-block:: bash

   $ pip install pre-commit
   $ pre-commit install

The documentation can be build from the ``eeg-wiki/doc`` folder with ``make`` commands:

- ``make html`` to build the entire website.
- ``make html-noplot`` to build the website without running the tutorials.
- ``make clean`` to remove the generated and build files.
- ``make view`` to open the build website in the default browser.
- ``make linkcheck`` followed by ``make linkcheck-grep`` to test for broken URLs.

Tutorials
---------

Python-based tutorials and code snippet are executed using `sphinx-gallery`_. The
tutorials are written in a plain python ``.py`` file in the folder
``eeg-wiki/tutorials``. The file naming must follow the pattern ``dd_*.py`` with ``dd``
corresponding to 2 digits used to order the tutorials. The ``# %%`` jupyter syntax is
used to denote separate sections.
