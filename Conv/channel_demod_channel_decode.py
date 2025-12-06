import numpy as np
import matplotlib.pyplot as plt
from Conv.BPSK.bpsk_receiver import bpsk_receiver
from Conv.util.util import awgn, calculate_ber,hamming_distance
from Conv.conv.decoder import channel_decoder


def channel_demod_channel_decode(bit_seq,bpsk_modulated_sequence_without_conv,modulated_signal,generator_polynomials,K,snr_start, snr_end, snr_step, fc, Tb, n,block_size):
    """
    Communication Link (AWGN Channel -> Demodulation -> Channel Decoding) and plot BER vs. SNR
    :param bpsk_modulated_sequence_without_conv:
    :param channel_encoded_sequence:
    :param modulated_signal:
    :param bit_seq: original bit sequence
    :param src_encoded_mod_sig: source encoded modulated signal
    :param channel_encoded_mod_sig: channel encoded modulated signal
    :param snr_start: start point of SNR
    :param snr_end: end point of SNR
    :param snr_step: step of SNR
    :return: restored bit sequence channel encoded signal
    """
    SNR_dB = np.arange(snr_start, snr_end + snr_step, snr_step)
    src_encoded_ber = np.zeros(len(SNR_dB))
    channel_decoded_ber = np.zeros(len(SNR_dB))
    for i in range(len(SNR_dB)):
        # AWGN Channel
        noisy_channel_encoded_sig = awgn(modulated_signal, SNR_dB[i])
        noisy_src_encoded_sig = awgn(bpsk_modulated_sequence_without_conv, SNR_dB[i])

        # Demodulation
        restored_channel_encoded_bit_seq = bpsk_receiver(noisy_channel_encoded_sig, fc, Tb, n)
        restored_src_encoded_bit_seq = bpsk_receiver(noisy_src_encoded_sig, fc, Tb, n)

        # BER
        src_encoded_ber[i] = calculate_ber(bit_seq, restored_src_encoded_bit_seq)
        channel_decoded_signal = channel_decoder(restored_channel_encoded_bit_seq,generator_polynomials,K,block_size)

        channel_decoded_ber[i] = hamming_distance(bit_seq, channel_decoded_signal)

        #if i == 0:      # at low SNR
        if SNR_dB[i] == -30:
            channel_decoded_signal_low_snr = channel_decoded_signal
            restored_src_encoded_bit_seq_low_snr = restored_src_encoded_bit_seq
        #elif i == len(SNR_dB) // 2:     # at medium SNR
        elif SNR_dB[i] == -20:
            channel_decoded_signal_medium_snr = channel_decoded_signal
            restored_src_encoded_bit_seq_medium_snr = restored_src_encoded_bit_seq

    # at high SNR
    channel_decoded_signal_high_snr = channel_decoded_signal
    restored_src_encoded_bit_seq_high_snr = restored_src_encoded_bit_seq

    plt.plot(SNR_dB, channel_decoded_ber, label='Channel Encoded')
    plt.plot(SNR_dB, src_encoded_ber, label='Source Encoded')
    plt.yscale('log')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.legend()
    plt.grid()
    plt.show()

    return channel_decoded_signal_high_snr, channel_decoded_signal_medium_snr, channel_decoded_signal_low_snr, \
        restored_src_encoded_bit_seq_high_snr, restored_src_encoded_bit_seq_medium_snr, restored_src_encoded_bit_seq_low_snr