
# Çiftçi Yazılım - Personel Takip ve Vardiya Denetim Sistemi

Bu proje, **Çiftçi Yazılım** tarafından geliştirilen bir personel takip ve vardiya denetim sistemidir. Flask tabanlı bu web uygulaması sayesinde personel bilgileri kolayca yönetilebilir, vardiyalar planlanabilir ve giriş/çıkış kayıtları takip edilebilir.

---

## 🔧 Özellikler

- 👨‍💼 Personel ekleme, düzenleme, silme
- 📋 Giriş/çıkış kayıtlarını görüntüleme
- 📆 Vardiya yönetimi (08:00–16:00, 16:00–00:00, 00:00–08:00)
- 🔐 Kullanıcı kayıt ve giriş sistemi (Login/Register)
- 🖥️ Modern ve sade kullanıcı arayüzü (HTML + CSS)

---

## 🚀 Kurulum

Projenin yerel ortamda çalıştırılması için aşağıdaki adımları takip edebilirsiniz:

### 1. Depoyu klonlayın
```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi
````

### 2. Sanal ortam oluşturun

```bash
python -m venv venv
source venv/bin/activate      # (Linux/macOS)
venv\Scripts\activate         # (Windows)
```

### 3. Gereksinimleri yükleyin

```bash
pip install -r requirements.txt
```

### 4. Veritabanını başlatın

```bash
flask db init
flask db migrate -m "İlk veritabanı"
flask db upgrade
```

### 5. Uygulamayı çalıştırın

```bash
flask run
```

---

## 🗂️ Proje Yapısı

```
proje-adi/
├── app.py
├── static/
│   ├── style.css
│   └── dashboard.css
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── personel_listesi.html
│   ├── personel_ekle.html
│   └── giris_kayitlari.html
├── models.py
├── forms.py
├── requirements.txt
└── README.md
```

---

## 🧪 Kullanıcı Giriş Bilgisi (Varsayılan)

```txt
Kullanıcı Adı: admin@example.com
Şifre: 123456
```

> İlk kullanıcıyı kendiniz `register` sayfasından oluşturabilirsiniz.

---

## 📸 Ekran Görüntüleri

> (Buraya proje arayüzünden ekran görüntüleri ekleyebilirsiniz.)

---

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına göz atabilirsiniz.

---

## ✉️ İletişim

**Vildan Çiftçi**
📧 [vildan@example.com](mailto:vildan@example.com)
🌐 [GitHub Profilim](https://github.com/kullaniciadi)

---

> Bu sistem eğitim amaçlı geliştirilmiştir. Gerçek firmalarda kullanmadan önce güvenlik, performans ve erişim kontrolleri açısından detaylı test edilmesi önerilir.

```

---

İstersen bu dosyayı `.md` formatında kaydedip sana hazır şekilde sunabilirim. Projeyi GitHub’a yükledikten sonra ana dizine yerleştirmen yeterlidir.  
İsim, e-posta, GitHub adresi gibi alanları istersen özelleştiririm. Ekleyeyim mi?
```

