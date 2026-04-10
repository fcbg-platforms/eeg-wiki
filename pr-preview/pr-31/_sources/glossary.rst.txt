.. include:: ./links.inc

Glossary
========

The Glossary provides short definitions of vocabulary specific to EEG and general
neuroimaging concepts. Many entries are taken from `MNE-Python <mne stable_>`_.

.. glossary::
    :sorted:

    anatomical landmark
    anatomical landmarks
    fiducial
    fiducial point
    fiducial points
        Fiducials are objects placed in the field of view of an imaging system to act as
        known spatial references that are easy to localize. In neuroimaging, fiducials
        are often placed on anatomical landmarks such as the `nasion (NAS) <Nasion_>`_
        or `left/right preauricular points (LPA and RPA) <LRPA_>`_.

        These known reference locations are used to define a coordinate system for
        localizing sensors (hence `NAS <Nasion_>`_, `LPA and RPA <LRPA_>`_ are often
        called "cardinal points" because they define the cardinal directions of the head
        coordinate system). The cardinal points are also useful when co-registering
        measurements in different coordinate systems.

        Due to the common neuroimaging practice of placing fiducial objects on
        anatomical landmarks, the terms "fiducial", "anatomical landmark", and "cardinal
        point" are often (erroneously) used interchangeably.

    BEM
    boundary element model
    boundary element method
        BEM is the acronym for boundary element method or boundary element model. Both
        are related to the definion of the conductor model in the forward model
        computation. The boundary element model consists of surfaces such as the inner
        skull, outer skull, and outer skin (scalp) that define compartments of tissues
        of the head.
