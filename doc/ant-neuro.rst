ANT Neuro
=========

4 ANT Neuro mylab amplifiers are available on the platform. Each amplifier supports 64
EEG channels and 24 auxiliary channels. The amplifiers can be cascaded together to
support 128 channels (2 amplifiers) or 256 channels (4 amplifiers).

Connectivity
------------

.. image:: ./_static/ant-neuro/XT-20000QC3.png
    :align: right
    :width: 200

The EEG amplifier is connected to the computer via a single USB-3 cable type-A to
type-B. All data is transmitted via USB. It doesn't require any additional power supply
and should run on battery. However, if the battery is low, it can be connected to an
external DC power supply supplying 12V and 4 A. Typically, an XT-20000QC3 external power
bank is used.

.. warning::

    Before connecting the power bank to the amplifier, make sure it is set to 12V.

Additionally, the amplifier can be connected to auxiliary channels. ANT provides 4
auxiliary boxes, alphabetically labeled ``A``, ``B``, ``C``, and ``D``. The box ``A``
has active channels which records an external DC 5V power supply. Typically, a USB can
be used, e.g. an USB from the XT-20000QC3 power bank. The other boxes have passive
bipolar channels.

Auxiliary boxes should be connected in a daisy chain, alphabetically ordered. If all 4
boxes are used, the order is ``Amplifier <- A <- B <- C <- D``. Any box can be removed
from the chain, but the order must be preserved.

Finally, a stimulation device or computer delivering TTL pulses on the 'trigger'
channel can be connected. Typically, a DB-25 (parallel port) cable is used.

.. note::

    If you are using 2 amplifiers together for 128 channels, or 4 amplifiers together,
    the appropriate trigger cable must be used to link and synchronize the amplifiers
    together. In this case, the trigger cable included an external power source (either
    battery or USB) which constantly delivers triggers on the data pin 8 of the DB-25
    port. In this case, do not use any trigger value that would use the data pin 8, i.e.
    do not use values above 127.

Acquisition software
--------------------

The acquisition software is called ``eego``.

Selecting the number of amplifiers
----------------------------------

When connecting the amplifiers to the recording computer, the ``eego`` software might
already be set with the correct number of amplifiers or not. If not, you have to
change the number of amplifiers before starting an acquisition workflow or you won't be
able to select the desired amplifier settings and montage for your cap.
