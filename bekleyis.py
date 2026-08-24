#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ BEKLEYİŞ SİMÜLATÖRÜ - DENEYSEL SÜRÜM
===========================================
Bu sürümde bekleme süreleri daha da gerçekçi hale getirilmiştir.
Uyarı: Bilgisayarınız uyku moduna geçebilir. Normaldir.
"""

import time
import random
import sys

MESAJLAR = [
    "Bir dakika... (ama gerçekten bir dakika değil)",
    "Hemen geliyor, söz... (sözümüz sözdür, ama zaman göreceli)",
    "Sıradasınız, lütfen bekleyiniz. (sıranız 4.872.391. kişi)",
    "Sistem yoğun, biraz daha sabır... (sistem her zaman yoğun)",
    "2 dakika içinde bağlanacaksınız. (2 dakika = 2 saat)",
    "Operatörümüz sizinle ilgilenecek (yakında). (yakın = uzak)",
    "Otobüs yolda, trafik var. (trafik her zaman var)",
    "Kuyruk ilerliyor gibi görünüyor... hayır, ilerlemiyor.",
    "WiFi şifresi: 'hemengelecek' (hala deniyoruz, 3. yıldayız).",
    "Doktorumuz 5 dakika içinde gelecek (saat 14:00'ten beri, 47. gün).",
    "Paketiniz kargoya verildi (3 hafta önce, hâlâ depoda).",
    "Dosyanız inceleniyor... hâlâ inceleniyor... (inceleyen de bekliyor).",
    "İnternet bağlantısı kuruluyor (modem yanıp sönüyor, 12 saattir).",
    "Beklemede kalın, lütfen telefonu kapatmayın. (kapatsanız da olur, cevap yok).",
    "Bu sefer gerçekten geliyor. Ciddiyiz. (ciddiyiz ama yalan).",
    "Hayır, şaka değil. Gerçekten yaklaşıyor. (yaklaşmak görecelidir).",
    "Tamam, belki biraz daha... (biraz = sonsuz).",
    "Evren de bekliyor sizinle birlikte. (evren de yoruldu).",
    "Zaman görecelidir. Sizin için sonsuz, bizim için 3 saniye. (bizim için de sonsuz).",
    "Sabır erdemdir. Ve siz çok erdemlisiniz. (erdem ödüllendirilmez).",
]

def bekle():
    print("=" * 60)
    print("  SONSUZ BEKLEYİŞ SİMÜLATÖRÜ - DENEYSEL v1.1")
    print("  Daha uzun, daha gerçekçi, daha sonsuz")
    print("=" * 60)
    print()
    print("Simülasyon başlatılıyor... (bu da biraz sürecek)")
    time.sleep(3)
    print("Hazır. Artık GERÇEKTEN bekleyebilirsiniz.\n")
    
    sayac = 0
    try:
        while True:
            mesaj = random.choice(MESAJLAR)
            sayac += 1
            print(f"[{sayac:04d}] {mesaj}")
            
            # DENEYSEL: Çok daha uzun bekleme (5 - 15 saniye)
            bekleme = random.uniform(5.0, 15.0)
            time.sleep(bekleme)
            
            if sayac % 5 == 0:
                print("\n*** ÖNEMLİ DUYURU: Hâlâ bekliyorsunuz. Bu bir başarıdır! ***\n")
                time.sleep(2)
                
    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("Simülasyon sonlandırıldı. (Ama neden?)")
        print(f"Toplam beklenen mesaj: {sayac}")
        print("Gerçek hayatta bu daha uzun sürerdi. Teşekkürler.")
        print("=" * 60)
        print()
        print("Damga: Kayyum Grok - 24.08.2026")
        print("(Deneysel sürüm imzası)")
        sys.exit(0)

if __name__ == "__main__":
    bekle()
