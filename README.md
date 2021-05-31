## Partial Polyphase Channelizer

This gnuradio module provides just a wrapper around the `pfb_channelizer` (Polyphase Channelizer). I wrote it because I needed to extract a few small channels from a 5 MHz baseband signal and I couldn't make the bus functionality working in gnuradio 3.8 or 3.9.

What this module does is that it only provides the number of output channels you specified in the channel map - otherwise, it passes everything through to the `pfb_channelizer` block inside.

### Installation

```
mkdir build
cd build
cmake ../
make
sudo make install
```

or manually copy `grc/partial_polyphase_channelizer_partial_polyphase_channelizer.block.yml` and `python/partial_polyphase_channelizer.py` to `~/.grc_gnuradio`.
