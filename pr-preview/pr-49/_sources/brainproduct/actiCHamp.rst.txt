.. include:: ../links.inc

actiCHamp
=========

A BrainProduct `actiCHamp`_ amplifier is available on the platform. This system is
provided with 4 32-channels modules and with 64 channel caps which uses 2/4 module
connectors available. With 64 channels, the `actiCHamp`_ system is capable of recording
EEG signals with a sampling rate up to 50 kHz.

Connectivity
------------

The setup is composed of the following components:

* Amplifier
* External battery
* USB cable to connect the recording PC
* Trigger cable

.. note::

    The battery is bulky and has the same form factor as the amplifier. It is common to
    place the amplifier on top of the battery. The amplifier starts as soon as the
    battery is connected. There is no ``ON/OFF`` button on the amplifier.

.. image:: ../_static/actiCHamp/actiCHamp-setup.jpg
    :align: center
    :class: img-with-border
    :width: 80%

On the front of the amplifier, 8 connectors are available for auxiliary channels.

.. image:: ../_static/actiCHamp/actiCHamp-aux.jpg
    :align: center
    :class: img-with-border
    :width: 50%

On the top of the amplifier, 4 32-channels modules are available to connect the caps.

.. note::

    Since we only provide 64 channels caps, only the 2 connectors on the front are used.

.. image:: ../_static/actiCHamp/actiCHamp-cap-connectors.jpg
    :align: center
    :class: img-with-border
    :width: 50%

Trigger IN
----------

The `actiCHamp`_ system provides a female DB-9 trigger input connector. A DB-9 to DB-25
cable is provided to connect the amplifier to standard
:ref:`parallel port <parallelport:Parallel Port Trigger>`.

.. image:: ../_static/actiCHamp/trigger-in-db9.png
    :align: center
    :class: img-with-border
    :width: 50%

Trigger OUT
-----------

The `actiCHamp`_ system also provides a trigger out port used to control external
equipment via TTL pulses.

.. image:: ../_static/actiCHamp/trigger-out-db9.png
    :align: center
    :class: img-with-border
    :width: 50%

Channel 1 - module 1
--------------------

The channel 1 in module 1 has 2 important functions:

* Impedance measurement
* Active shielding mode: the signal on channel 1 / module 1 is used as a signal source
  for determining the environmental noise. Therefore, this channel should be place in an
  area with low physiological activity to avoid EEG/EMG artifacts on all electrodes due
  to overcompensation.
