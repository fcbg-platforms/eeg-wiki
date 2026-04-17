"""
.. _tut-precise-audio:

Precise audio presentation
==========================

.. include:: ../../links.inc

When delivering a sound through the soundcard of a computer and a trigger through the
parallel port, it's important to ensure that the sound and the trigger are synchronized.

Python sleep precision
----------------------

The :func:`time.sleep` function from the `time` module is not precise enough to halt the
program execution for a precise amount of time. The variability depends on the operating
system and python version and should be measured before using it in an experiment.
"""

# sphinx_gallery_thumbnail_path = '_static/tutorials/trigger-sound-delay-hist.png'

import time
import timeit

import numpy as np

times = timeit.repeat("time.sleep(0.005)", repeat=3, number=100, globals=globals())
times = np.array(times) / 100
print(f"Mean: {np.mean(times):.8f} seconds")
print(f"Standard Deviation: {np.std(times):.8f} seconds")

# %%
# Locally, I measured 5.06822 ms ± 61.4 μs per loop (mean ± std. dev. of 3 runs, 100
# loop each).
#
# If greater sleeping precision is needed, the sleeping period can be cut into segments
# waited with :func:`time.sleep` and a last segment where a :func:`time.perf_counter` is
# used to wait for the remaining time.
#
# .. note::
#
#     Note that using :func:`time.sleep` is important as it gives back the control to
#     the operating system, allowing other processes to run.


def high_precision_sleep(duration: float) -> None:
    """High precision sleep function."""
    start_time = time.perf_counter()
    assert 0 < duration, "The duration must be strictly positive."
    while True:
        elapsed_time = time.perf_counter() - start_time
        remaining_time = duration - elapsed_time
        if remaining_time <= 0:
            break
        if remaining_time >= 0.0002:
            time.sleep(remaining_time / 2)


times = timeit.repeat(
    "high_precision_sleep(0.005)", repeat=3, number=100, globals=globals()
)
times = np.array(times) / 100
print(f"Mean: {np.mean(times):.8f} seconds")
print(f"Standard Deviation: {np.std(times):.8f} seconds")

# %%
# Locally, I measured 5.00070 ms ± 0.08 μs per loop (mean ± std. dev. of 3 runs, 100
# loop each).
#
# Psychopy and Psychtoolbox
# -------------------------
#
# `Psychtoolbox`_ is a compiled toolbox for MATLAB that allows to present stimuli with
# precision. Despite a lack of funding and resources to support it, it's still one of
# the most used stimuli presentation toolboxes. Some of its functionalities are
# available in Python, especially through the `Psychopy`_ library.

# In this example, we will use the python interface of `Psychtoolbox`_ combined with
# triggers from :class:`byte_triggers.ParallelPortTrigger` to deliver synchronize audio
# stimuli and triggers.

import psychtoolbox as ptb
from byte_triggers import ParallelPortTrigger
from psychopy.sound.backend_ptb import SoundPTB

# create the sound and trigger object
sound = SoundPTB(value=440.0, secs=0.2, blockSize=16)
trigger = ParallelPortTrigger(0x2FB8)  # or "/dev/parport0" on linux

# loop 10 times and deliver 10 sounds
for k in range(10):
    now = ptb.GetSecs()
    sound.play(when=now + 0.2)  # schedule the sound in 200 ms
    high_precision_sleep(0.2)  # wait for 200 ms
    trigger.signal(1)  # send the trigger
    print(f"Sound {k + 1} delivered.")
    high_precision_sleep(0.5)  # wait between sounds

# %%
# The key elements are to schedule the sound with the ``when`` argument of the
# `Psychtoolbox`_ backend, wait for the scheduling duration, and deliver the trigger.
# With this method, the trigger to sound delay should be less than 1 ms.
#
# .. figure:: ../../_static/tutorials/trigger-sound-delay-epochs.png
#     :align: center
#     :alt: Epochs showing the trigger to sound delay
#
# The measure above was done with a 1024 Hz sampling rate on an ANT Neuro EEG system.
# Measuring algorithmically the delay between the trigger and the sound is possible
# through a threshold on the absolute value of the hilbert transformed signal, yielding:
#
# .. figure:: ../../_static/tutorials/trigger-sound-delay-hist.png
#     :align: center
#     :alt: Epochs showing the trigger to sound delay
#
# .. note::
#
#     Note that the measure through the absolute value of the hilbert transformed signal
#     is a good automatic sound onset detection method, but it's not perfect and the
#     thresholding inherently adds jitter to the measure.
