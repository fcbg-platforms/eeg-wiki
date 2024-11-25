.. include:: ../links.inc

Connectivity
============

.. image:: ../_static/ant-neuro/XT-20000QC3.png
    :align: right
    :width: 200

The EEG amplifier is connected to the computer via a single USB-3 cable type-A to
type-B. All data is transmitted via USB. It doesn't require any additional power supply
and should run on battery. However, if the battery is low, it can be connected to an
external DC power supply supplying 12V and 4 A. Typically, an `XT-20000QC3`_ external
power bank is used.

.. warning::

    Before connecting the power bank to the amplifier, make sure it is set to 12V or it
    will damage the amplifier.

Additionally, the amplifier can be connected to auxiliary channels. ANT provides 4
auxiliary boxes, alphabetically labeled ``A``, ``B``, ``C``, and ``D``. The box ``A``
has active channels which requires an external DC 5V power supply. Typically, a USB can
be used, e.g. an USB from the `XT-20000QC3`_ power bank. The other boxes have passive
bipolar channels.

Auxiliary boxes should be connected in a daisy chain, alphabetically ordered. If all 4
boxes are used, the order is ``Amplifier <- A <- B <- C <- D``. Any box can be removed
from the chain, but the order must be preserved.

Finally, a stimulation device or computer delivering TTL pulses on the ``trigger``
channel can be connected. Typically, a DB-25 (parallel port) cable is used.

.. note::

    If you are using 2 amplifiers together for 128 channels, or 4 amplifiers together,
    the appropriate trigger cable must be used to link and synchronize the amplifiers
    together. In this case, the trigger cable includes an external power source (either
    battery or USB) which constantly delivers triggers on the data pin 8 of the DB-25
    port. In this case, do not use any trigger value that would use the data pin 8, i.e.
    do not use values above 127.

    .. warning::

        If you use a trigger cable on battery, desynchronization errors/disconnection
        errors might be due to a dead battery. Try to replace it.

    .. warning::

        If you use a trigger cable with a USB connector, do not plug it on an external
        battery or on the `XT-20000QC3`_ power bank. The trigger cable won't pull enough
        power from the USB port which will result in the battery/power bank shutting
        down and to the amplifier desynchronization/disconnection.

        Instead, plug the USB connector on either:

        - A computer USB port
        - A USB power adapter (e.g. a phone charger)

Complete setup example
----------------------

Below is an example of a complete setup with an ANT amplifier powered by its internal
battery and by an external `XT-20000QC3`_ power bank with:

- 3 auxiliary boxes connected ``A``, ``B``, and ``C``. The auxiliary box A is powered
  by the `XT-20000QC3`_ power bank.
- A trigger to parallel port cable to deliber TTL pulses from a stimulation PC/device.
- A USB-3 cable to connect the recording PC.

.. image:: ../_static/ant-neuro/full-setup.jpg
    :align: center
    :class: img-with-border
    :width: 80%

Minimal setup example
---------------------

Below is a more minimalistic setup with an ANT amplifier powered by its internal battery
with only a USB-3 cable to connect a recording PC, a trigger to parallel port cable to
connect to a stimulation PC/device, and a single auxiliary box connected.

.. image:: ../_static/ant-neuro/partial-setup.jpg
    :align: center
    :class: img-with-border
    :width: 80%
