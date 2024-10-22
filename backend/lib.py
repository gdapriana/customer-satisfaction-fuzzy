import matplotlib.pyplot as plt

def visualize(kualitas_makanan, kecepatan_layanan, km1, km2, km3, kl1, kl2):
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 10))
    ax0.plot(kualitas_makanan, km1, 'b', linewidth=1.5, label='buruk')
    ax0.plot(kualitas_makanan, km2, 'g', linewidth=1.5, label='Sedang')
    ax0.plot(kualitas_makanan, km3, 'r', linewidth=1.5, label='Baik')
    ax0.set_title('Kualitas Makanan')
    ax0.legend()

    ax1.plot(kecepatan_layanan, kl1, 'b', linewidth=1.5, label='Cepat')
    ax1.plot(kecepatan_layanan, kl2, 'r', linewidth=1.5, label='Lambat')
    ax1.set_title('Kecepatan Layanan')
    ax1.legend()

    # Turn off top/right axes
    for ax in (ax0, ax1):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()
    plt.show()
