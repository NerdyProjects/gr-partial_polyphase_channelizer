# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Partial polyphase channelizer
# GNU Radio version: 3.8.2.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from gnuradio.filter import pfb





class partial_polyphase_channelizer(gr.hier_block2):
    def __init__(self, channel_map=[], channels=4, oversampling=1, taps=0):
        gr.hier_block2.__init__(
            self, "Not titled yet",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(len(channel_map), len(channel_map), gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.channel_map = channel_map
        self.channels = channels
        self.oversampling = oversampling
        self.taps = taps

        ##################################################
        # Variables
        ##################################################

        ##################################################
        # Blocks
        ##################################################
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
            channels,
            taps,
            oversampling,
            100)
        self.pfb_channelizer_ccf_0.set_channel_map(channel_map)
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self, 0), (self.pfb_channelizer_ccf_0, 0))
        count = len(channel_map)
        for i in range(count):
            self.connect((self.pfb_channelizer_ccf_0, i), (self, i))
        for i in range(len(channel_map), channels):
            self.connect((self.pfb_channelizer_ccf_0, i), (self.blocks_null_sink_0, i - count))


    def get_channel_map(self):
        return self.channel_map

    def set_channel_map(self, channel_map):
        self.channel_map = channel_map
        self.pfb_channelizer_ccf_0.set_channel_map(self.channel_map)

    def get_channels(self):
        return self.channels

    def get_oversampling(self):
        return self.oversampling

    def set_oversampling(self, oversampling):
        self.oversampling = oversampling

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.pfb_channelizer_ccf_0.set_taps([self.taps])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


