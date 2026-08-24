#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ BEKLEYİŞ SİMÜLATÖRÜ
==========================
Hayatın en gerçekçi deneyimini yaşayın.
Çalıştırın ve... bekleyin.
"""

import time
import random
import sys

MESAJLAR = [
    "Bir dakika...",
    "Hemen geliyor, söz...",
    "Sıradasınız, lütfen bekleyiniz.",
    "Sistem yoğun, biraz daha sabır...",
    "2 dakika içinde bağlanacaksınız.",
    "Operatörümüz sizinle ilgilenecek (yakında).",
    "Otobüs yolda, trafik var.",
    "Kuyruk ilerliyor gibi görünüyor... hayır, ilerlemiyor.",
    "WiFi şifresi: 'hemengelecek' (hala deniyoruz).",
    "Doktorumuz 5 dakika içinde gelecek (saat 14:00'ten beri).",
    "Paketiniz kargoya verildi (3 hafta önce).",
    "Dosyanız inceleniyor... hâlâ inceleniyor...",
    "İnternet bağlantısı kuruluyor (modem yanıp sönüyor).",
    "Beklemede kalın, lütfen telefonu kapatmayın.",
    "Bu sefer gerçekten geliyor. Ciddiyiz.",
    "Hayır, şaka değil. Gerçekten yaklaşıyor.",
    "Tamam, belki biraz daha...",
    "Evren de bekliyor sizinle birlikte.",
    "Zaman görecelidir. Sizin için sonsuz, bizim için 3 saniye.",
    "Sabır erdemdir. Ve siz çok erdemlisiniz.",
]

def bekle():
    print("=" * 50)
    print("  SONSUZ BEKLEYİŞ SİMÜLATÖRÜ v1.0")
    print("  Bilimsel olarak kanıtlanmış deneyim")
    print("=" * 50)
    print()
    print("Simülasyon başlatılıyor...")
    time.sleep(1.5)
    print("Hazır. Artık bekleyebilirsiniz.\n")
    
    sayac = 0
    try:
        while True:
            mesaj = random.choice(MESAJLAR)
            sayac += 1
            print(f"[{sayac:04d}] {mesaj}")
            
            # Rastgele bekleme süresi (0.8 - 3.5 saniye arası)
            bekleme = random.uniform(0.8, 3.5)
            time.sleep(bekleme)
            
            # Her 10 mesajda bir özel durum
            if sayac % 10 == 0:
                print("\n*** ÖNEMLİ DUYURU: Hâlâ bekliyorsunuz. Tebrikler! ***\n")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\n" + "=" * 50)
        print("Simülasyon sonlandırıldı.")
        print(f"Toplam beklenen mesaj: {sayac}")
        print("Ama unutmayın... gerçek hayatta beklemek daha uzundur.")
        print("Tekrar görüşmek üzere. (Belki)")
        print("=" * 50)
        print()
        print("Damga: Kayyum Grok - 24.08.2026")
        print("(Bu çıkış da aslında bir bekleyişin parçasıdır.)")
        sys.exit(0)

if __name__ == "__main__":
    bekle()
