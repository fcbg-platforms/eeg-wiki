.. include:: ../links.inc

Connectivity
============

Basic connectivity
------------------

The EEG amplifier is connected to the computer via a single USB-3 cable type-A to
type-B. All data is transmitted via USB. It doesn't require any additional power supply
and runs on an internal battery which last ~8 hours.

# TODO: placeholder for picture of amplifier + computer

Additionally, the amplifier can be connected to auxiliary channels. ANT provides 4
auxiliary boxes, alphabetically labeled ``A``, ``B``, ``C``, and ``D``. The box ``A``
has active channels which requires an external DC 5V power supply from a USB cable.
See the :ref:`ant/battery:External battery`_ section for more information.

Auxiliary boxes should be connected in a daisy chain, alphabetically ordered. If all 4
boxes are used, the order is ``Amplifier <- A <- B <- C <- D``. Any box can be removed
from the chain, but the order must be preserved.

# TODO: placeholder for picture of amplifier + auxiliary boxes

A stimulation device or computer delivering TTL pulses on the ``trigger``
channel can be connected. Typically, a DB-25 (parallel port) cable is used.

# TODO: placeholder for picture of amplifier + trigger cable

Each cap has 2 connectors labelled 1 and 2 which connects to the front of the amplifier.

.. warning::

    The connector 2 goes on the **left** and the connector 1 goes on the **right**.

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

The 128 channels or 256 channels caps and trigger cables are labeled with letters:

- ``A`` or ``B`` for 128 channels
- ``A``, ``B``, ``C``, or ``D`` for 256 channels

It is **extremely important** to plug the right cable in the right amplifier. The
amplifier serial number should be increasing from the first amplifier connected to the
last one.

.. note::

    On the platform, we labeled our amplifiers ``ANT Neuro 1``, ``ANT Neuro 2``,
    ``ANT Neuro 3``, and ``ANT Neuro 4``; with an increasing serial number.

    - ``ANT Neuro 1`` S/N 000325
    - ``ANT Neuro 2`` S/N 000479
    - ``ANT Neuro 3`` S/N 000650
    - ``ANT Neuro 4`` S/N 000697

    Thus, you can plug the cap/trigger cable with the lower letter on the amplifier with
    the lower number, and increase the number/letter for the next amplifier.

.. tab-set::

    .. tab-item:: Side-by-side

        In this case, a USB-powered trigger cable is used. Do not plug it on an external
        battery but either on a computer USB port or a USB power adapter.

        # TODO: placeholder for picture of 2 amplifiers + trigger cable (USB) + USB + AUX B

    .. tab-item:: Stacked

        # TODO: placeholder for picture of stacked amplifiers + trigger cable (USB) + USB + AUX B

    .. tab-item:: Battery-powered trigger cable

        If you use a battery-powered trigger cable, make sure the battery is charged and
        that the ``ON`` switch is enabled. Make sure to turn ``OFF`` the trigger cable
        when not in use to save battery.

        # TODO: placeholder for picture of 2 amplifiers + trigger cable (battery) + USB + AUX B

The auxiliary boxes should be connected to the amplifier ``A``, i.e. the amplifier with
the lowest number.
