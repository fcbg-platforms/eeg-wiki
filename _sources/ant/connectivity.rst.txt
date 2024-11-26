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

Minimal setup example
---------------------

Below is a minimalistic setup with an ANT amplifier powered by its internal battery
with only a USB-3 cable to connect a recording PC, a trigger to parallel port cable to
connect to a stimulation PC/device, and a single auxiliary box connected with bipolars
connectors.

.. image:: ../_static/ant-neuro/partial-setup.jpg
    :align: center
    :class: img-with-border
    :width: 80%

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

128 channels or 256 channels
----------------------------

The ANT amplifier(s) can be cascaded to increase the number of channels. With 2
amplifiers, 128 channels can be recorded. With 4 amplifiers, 256 channels can be
recorded. To synchronize the amplifiers, a common trigger cable including an external
power source is used. This cable disconnects the DB-25 ``D7`` last pin and use it
internally to deliver synchronization pulses to all amplifiers.

.. note::

    Since the last pin of the parallel port is disconnected, do not use trigger values
    above 127.

.. warning::

    If you use a trigger cable on battery, desynchronization errors/disconnection
    errors might be due to a dead battery. Try to replace it.

.. warning::

    If you use a trigger cable with a USB connector, do not plug it on an external
    battery or on the `XT-20000QC3`_ power bank. The trigger cable won't pull enough
    power from the USB port which will result in the battery/power bank shutting
    down and in the amplifier desynchronization/disconnection.

    Instead, plug the USB connector on either:

    - A computer USB port
    - A USB power adapter (e.g. a phone charger)

The 128 channels or 256 channels caps and trigger cables are labeled with either:

- a number ``1`` or ``2`` for 128 channels or ``1``, ``2``, ``3``, or ``4`` for 256
  channels
- a letter ``A`` or ``B`` for 128 channels or ``A``, ``B``, ``C``, or ``D`` for 256
  channels

It is **extremely important** to plug the right cable in the right amplifier. The
amplifier serial number should be increasing from the first amplifier connected to the
last one.

.. note::

    On the platform, with labeled our amplifiers ``ANT Neuro 1``, ``ANT Neuro 2``,
    ``ANT Neuro 3``, and ``ANT Neuro 4``; with an increasing serial number.

    - ``ANT Neuro 1`` S/N 000325
    - ``ANT Neuro 2`` S/N 000479
    - ``ANT Neuro 3`` S/N 000650
    - ``ANT Neuro 4`` S/N 000697

    Thus, you can plug the cap/trigger cable with the lower number/letter on the
    amplifier with the lower number, and increase the number/letter for the next
    amplifier.

Below is an example of a 128 channels setup with 2 ANT amplifiers powered by their
internal batteries with a single auxilibary box connected with bipolars connectors.

.. tab-set::

    .. tab-item:: Side-by-side

        In this case, a USB-powered trigger cable is used. Do not plug it on an external
        battery but either on a computer USB port or a USB power adapter.

        .. image:: ../_static/ant-neuro/128ch-unstack.jpg
            :align: center
            :class: img-with-border
            :width: 80%

    .. tab-item:: Stacked

        It is common to stack the 2 of 4 amplifiers on top of each other.

        .. image:: ../_static/ant-neuro/128ch-stack.jpg
            :align: center
            :class: img-with-border
            :width: 80%

    .. tab-item:: Battery-powered trigger cable

        If you use a battery-powered trigger cable, make sure the battery is charged and
        that the ``ON`` switch is enabled. Make sure to turn ``OFF`` the trigger cable
        when not in use to save battery.

        .. image:: ../_static/ant-neuro/128ch-stack-battery.jpg
            :align: center
            :class: img-with-border
            :width: 80%
