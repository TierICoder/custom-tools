# custom-tools
Çeşitli amaçlar için yazılmış script ve benzeri içerikler 

### 📦 Gereksinimler
Bu script Python 3 ile yazılmıştır ve sadece `sqlite3` modülünü kullanır. Ekstra bir kütüphane gerektirmez.

### 🖥️ Nasıl Kullanılır?

1. Script’i çalıştırmadan önce Chrome’u kapatın.
2. `targeted_chrome_history_cleaner.py` dosyasını not defteri veya bir IDE ile açın.
3. Script içinde yer alan `keyword` değişkenini silmek istediğiniz kelimeye göre düzenleyin:

Örneğin:

keyword = "discord.com"  # Discord geçmişini silmek için

İhtiyacınıza göre farklı kelimelerle (örn. 'facebook.com', 'twitter.com') geçmişi temizleyebilirsiniz.

Scripti masaüstüne veya herhangi bir klasöre kopyalayın Sol Shit+ Mouse sağ tıkla PowerShell penceresini burada açına tıklayın

python targeted_chrome_history_cleaner.py yazarak scripti çalıştırın ve işte çalışıyor.

Bu script Veri analizi ve hedefli veri silme mantığını içeriyor.
sqlite3 kullanımı açısından gerçek bir “under the hood” örneği.

Tarayıcıdan silmekten daha güçlü çünkü:

→ Tarayıcı genelde “temizle” deyince sadece zaman damgası bazlı siliyor.
→ Ama bu script hedefli veriyi veritabanından çekip nokta atışı siliyor.

⚠️ Uyarı
Geçmişi silmeden önce, Chrome geçmişinizin bir yedeğini almayı unutmayın. Bu işlem geri alınamaz.
