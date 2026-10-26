#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Form Doldurma Simülatörü
Bir formu doldurursun, form sana daha fazla form sorar.
Bu kod GERÇEKTEN çalışır. Deneyin görün.
"""

import random
import time

def generate_question():
    questions = [
        "Adınızın annesinin kızlık soyadının ilk harfinin ASCII kodu nedir?",
        "Son yediğiniz yemeğin kalori değerini bilimsel olarak hesapladınız mı? (Evet/Hayır, ama neden?)",
        "Evrenin genişleme hızını km/s cinsinden tahmin edin, yanlış olursa form uzar.",
        "Bugün kaç kez 'ama' dediniz? Sayınızı yazın, form kontrol edecek.",
        "Komşunuzun kedisinin adını ve onun siyasi görüşünü (gizli) belirtin.",
        "Bu formu doldururken içtiğiniz çayın sıcaklığını Kelvin cinsinden yazın.",
        "Hayatınızın anlamını 42 kelimeden az özetleyin, aksi halde yeni form açılır."
    ]
    return random.choice(questions)

def main():
    print("=== SONSUZ FORM DOLDURMA SİMÜLATÖRÜ ===")
    print("Hoş geldiniz. Formunuz başladı. Çıkmak için 'KAÇTIK' yazın.")
    print("Uyari: Her cevap yeni bir soru doğurur. Bu özelliktir, bug değil.")
    time.sleep(1)
    
    form_count = 1
    while True:
        print(f"\n--- FORM #{form_count} ---")
        question = generate_question()
        print(f"Soru: {question}")
        answer = input("Cevabınız: ").strip()
        
        if answer.upper() == "KAÇTIK":
            print("Tebrikler! Formdan kaçtınız. Ama form hâlâ sizi arıyor...")
            break
        
        # Absürt değerlendirme
        if len(answer) < 3:
            print("Cevap çok kısa. Form uzuyor...")
        elif "evet" in answer.lower() or "hayır" in answer.lower():
            print("Evet/Hayır cevapları form tarafından reddedildi. Detay verin.")
        else:
            print("Cevabınız kaydedildi. Yeni form açılıyor...")
        
        form_count += 1
        time.sleep(0.5)
        
        if form_count > 10:
            print("\n*** UYARI: 10 formu geçtiniz. Bürokrasi sizden memnun. ***")
            # Gizli siyasi referans (saklı)
            # hidden_political = "Burokrasi sonsuzdur, seçimler de öyle mi?"  # gizlendi
            break
    
    print(f"\nToplam doldurulan form: {form_count - 1}")
    print("Simülatör sona erdi. Gerçek hayatta formlar bitmez.")

if __name__ == "__main__":
    main()
