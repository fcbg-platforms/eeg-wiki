.. include:: ./links.inc

LSL Real-time acquisition
=========================

Many amplifier manufacturers have adopted the Lab Streaming Layer protocol to offer a
real-time access to the data stream. Real-time access enables closed-loop experiments
where the data is processed and analyzed in real-time to provide feedback to the
subject.

Lab Streaming Layer
-------------------

`Lab Streaming Layer`_ (LSL) is an open-source networked middleware ecosystem to stream,
receive, synchronize, and record neural, physiological, and behavioral data streams
acquired from diverse sensor hardware.

This protocol is based on a C++ library, `liblsl <liblsl repo_>`_, which is available
for all major platforms (Windows, macOS, Linux) and architectures (x86, x64, ARM). Once
available on a system, the library can be used from many programming languages including
Python, C#, MATLAB, .. see this meta-package `labstreaminglayer <lsl meta repo_>`_ for
more information.

Many devices are compatible through native or third-party applications with LSL. See
this non-exhaustive list of the `LSL-compatible devices <lsl neta repo apps_>`_.

Python interface
----------------

`Lab Streaming Layer`_ has 2 interfaces in python:

- `pylsl`_: the legacy interface which offers the basic LSL objects and functions.
- `mne-lsl`_: the MNE-Python interface which offers both an efficient re-implementation
  of the low-level LSL API available in `pylsl`_  (:class:`mne_lsl.lsl.StreamInfo`,
  :class:`mne_lsl.lsl.StreamOutlet`, :class:`mne_lsl.lsl.StreamInlet`, ...) and a
  high-level API to easily connect to LSL streams handles them like MNE-Python objects
  (:class:`mne_lsl.stream.StreamLSL`, :class:`mne_lsl.stream.EpochsStream`, ...).

`mne-lsl`_ also bundles the `liblsl`_ C++ library inside its wheels, thus you don't need
to manually install or compile the library.

.. tab-set::

    .. tab-item:: PyPI

        .. code-block:: bash

            $ pip install mne-lsl

    .. tab-item:: Conda

        .. code-block:: bash

            $ conda install -c conda-forge mne-lsl

    .. tab-item:: MNE installers

        As of MNE-Python 1.6, `mne-lsl`_ is distributed in the
        `MNE standalone installers`_.

        The installers create a conda environment with the entire MNE-ecosystem setup,
        and more! This installation method is recommended for beginners.

    .. tab-item:: Source

        If you have the required compilers and libraries available, you can install
        from source to build `liblsl`_ for your platform with:

        .. code-block:: bash

            $ pip install mne-lsl --no-binary mne-lsl

        Or you can set the environment variable ``MNE_LSL_SKIP_LIBLSL_BUILD=1`` to skip
        the building phase of `liblsl`_ and provide your own compiled version in the
        environment variable ``MNE_LSL_LIB`` or ``PYLSL_LIB``.

MATLAB interface
----------------

A MATLAB interface is available `here <matlab lsl_>`_.
