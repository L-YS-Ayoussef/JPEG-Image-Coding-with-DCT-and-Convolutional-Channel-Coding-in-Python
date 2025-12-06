from .conv.encoder import channel_encoder
from .BPSK.bpsk_transmitter import bpsk_transmitter
from .channel_demod_channel_decode import channel_demod_channel_decode


def communication_link(s, generator_polynomials, K, fc, Ab, Tb, n, snr_start, snr_end, snr_step, block_size):
    """
    Communication Link (Source Encoding -> Channel Encoding -> Modulation -> AWGN Channel -> Demodulation -> Channel Decoding)
    :param s: original bit sequence
    :param generator_polynomials: generator polynomials
    :param K: constraint length
    :param fc: carrier frequency
    :param Ab: amplitude of carrier
    :param Tb: bit duration
    :param n: number of samples in one bit duration
    :param snr_start: start point of SNR
    :param snr_end: end point of SNR
    :param snr_step: step of SNR
    :return: restored bit sequence channel encoded signal
    """
    channel_encoded_sequence = channel_encoder(s, generator_polynomials, K, block_size)
    modulated_signal = bpsk_transmitter(channel_encoded_sequence, fc, Ab, Tb, n)
    modulated_signal_without_conv = bpsk_transmitter(s, fc, Ab, Tb, n)
    
    channel_decoded_signal_high_snr, channel_decoded_signal_medium_snr, channel_decoded_signal_low_snr, \
    restored_src_encoded_bit_seq_high_snr, restored_src_encoded_bit_seq_medium_snr, restored_src_encoded_bit_seq_low_snr \
    = channel_demod_channel_decode(s, modulated_signal_without_conv, modulated_signal,
                                                  generator_polynomials, K, snr_start, snr_end, snr_step, fc, Tb, n,
                                                  block_size)

    return channel_decoded_signal_high_snr, channel_decoded_signal_medium_snr, channel_decoded_signal_low_snr, \
        restored_src_encoded_bit_seq_high_snr, restored_src_encoded_bit_seq_medium_snr, restored_src_encoded_bit_seq_low_snr
