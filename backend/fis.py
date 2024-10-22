import numpy as np
import skfuzzy as fuzz

# Generate universe variables
x_kualitas_makanan = np.arange(0, 11, 1) # buruk, sedang, bagus
x_kecepatan_layanan = np.arange(0, 31, 1) # cepat, lambat
x_kepuasan = np.arange(0, 11, 1) # kurang_puas, puas

# Generate fuzzy membership functions
kualitas_makanan_buruk = fuzz.trapmf(x_kualitas_makanan, [0, 0, 2, 4])
kualitas_makanan_sedang = fuzz.trapmf(x_kualitas_makanan, [2, 4, 5, 7])
kualitas_makanan_bagus = fuzz.trapmf(x_kualitas_makanan, [5, 7, 10, 10])
kecepatan_layanan_cepat = fuzz.trapmf(x_kecepatan_layanan, [0, 0, 5, 20])
kecepatan_layanan_lambat = fuzz.trapmf(x_kecepatan_layanan, [5, 20, 30, 30])

def fuzzification(input_val):
    fuzz_kualitas_makanan_result = [
        fuzz.interp_membership(x_kualitas_makanan, kualitas_makanan_buruk, input_val["kualitas_makanan"]),
        fuzz.interp_membership(x_kualitas_makanan, kualitas_makanan_sedang , input_val["kualitas_makanan"]),
        fuzz.interp_membership(x_kualitas_makanan, kualitas_makanan_bagus, input_val["kualitas_makanan"]),
    ]
    fuzz_kecepatan_layanan_result = [
        fuzz.interp_membership(x_kecepatan_layanan, kecepatan_layanan_cepat, input_val["kecepatan_layanan"]),
        fuzz.interp_membership(x_kecepatan_layanan, kecepatan_layanan_lambat, input_val["kecepatan_layanan"]),
    ]
    return fuzz_kualitas_makanan_result, fuzz_kecepatan_layanan_result
def inference(kualitas_makanan, kecepatan_layanan):
    rule_tidak_puas = max(
        min(kualitas_makanan[0], kecepatan_layanan[0]),
        min(kualitas_makanan[0], kecepatan_layanan[1]),
        min(kualitas_makanan[1], kecepatan_layanan[1])
    )
    rule_puas = max(
        min(kualitas_makanan[1], kecepatan_layanan[0]),
        min(kualitas_makanan[2], kecepatan_layanan[1]),
        min(kualitas_makanan[2], kecepatan_layanan[0]),
    )
    return rule_tidak_puas, rule_puas
def defuzzification(tidak_puas, puas):
    r_tidak_puas =  3
    r_puas = 8

    # Weighted average (Sugeno)
    numerator = tidak_puas * r_tidak_puas + puas * r_puas
    denominator = tidak_puas + puas

    if denominator == 0:
        return 0
    else:
        return numerator / denominator
def show_membership_degree():
    kualitas_makanan_ling = ["buruk", "sedang", "bagus"]
    kecepatan_layanan_ling = ["cepat", "lambat"]
    print(f'Input:\nKualitas Makanan: {in_kualitas_makanan}, Kecepatan layanan: {in_kecepatan_pelayanan}\n')
    print("Derajat keanggotaan Kualitas Makanan:")
    for i, item in enumerate(fuzz_kualitas_makanan):
        if item != 0:
            print(f'{kualitas_makanan_ling[i]}: {fuzz_kualitas_makanan[i]:.2f}')

    print("\nDerajat keanggotaan Kecepatan Layanan:")
    for i, item in enumerate(fuzz_kecepatan_layanan):
        if item != 0:
            print(f'{kecepatan_layanan_ling[i]}: {fuzz_kecepatan_layanan[i]:.2f}')
def show_result(result_val):
    print(f'Kepuasan Pelanggan: {result_val:.2f}')

# input crips
in_kualitas_makanan = float(input("Kualitas Makanan (1-10)\t: "))
in_kecepatan_pelayanan = float(input("Kecepatan Pelayanan (menit)\t: "))

# fuzzification
fuzz_kualitas_makanan, fuzz_kecepatan_layanan = fuzzification(input_val={
    "kualitas_makanan": in_kualitas_makanan,
    "kecepatan_layanan": in_kecepatan_pelayanan
})
show_membership_degree()

# inference
infer_tidak_puas, infer_puas = inference(fuzz_kualitas_makanan, fuzz_kecepatan_layanan)

# defuzzification and result
result = defuzzification(infer_tidak_puas, infer_puas)
show_result(result)
