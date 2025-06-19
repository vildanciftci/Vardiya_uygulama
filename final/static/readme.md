



````markdown
# 🎨 CSS Dosyaları Hakkında

Bu klasör, web uygulamasının görsel stilini oluşturan tüm CSS dosyalarını içerir.

---

## 📁 Dosyalar

### `style.css`
- **Açıklama:** Tüm sayfalarda ortak kullanılan temel stilleri barındırır.
- **Uygulama:** `base.html` dosyasına bağlıdır.
- **İçerik:**
  - Genel `body`, `header`, `nav`, `main` ve bağlantı (`<a>`) stilleri
  - Renk uyumu: lacivert (#003366) – beyaz kombinasyonu
  - Temiz ve sade bir görünüm için uygun

### `dashboard.css`
- **Açıklama:** Ana sayfa (dashboard) için özel stiller içerir.
- **Uygulama:** `dashboard.html` dosyasına `<link>` ile bağlanır.
- **İçerik:**
  - Karşılama mesajı, hakkında bölümü ve hızlı erişim menüsü
  - Yuvarlatılmış kutular, gölgeler ve responsive yapı
  - Renk uyumu: beyaz arka plan, koyu mavi başlıklar

---

## 🛠️ Özelleştirme

### Renk Paletini Değiştirmek
- `style.css` ve `dashboard.css` dosyalarında ana renk `#003366` (lacivert)
- Dilersen bunu başka bir marka rengiyle (örneğin `#0066cc` veya `#2c3e50`) değiştirebilirsin

### Font Değişikliği
- Varsayılan font: `Arial` ve benzer sans-serif font ailesi
- Farklı bir font kullanmak istersen, Google Fonts'tan import edebilirsin:
  ```css
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
````

---

## 💡 Notlar

* Tüm CSS dosyaları `static/` klasöründe yer almalıdır.
* Flask uygulamasında CSS'e erişim şu şekilde yapılır:

  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

---

## ✍️ Hazırlayan

**Çiftçi Yazılım - 2024**
Proje Sahibi: Vildan Çiftçi

````

---

### Alternatif: CSS dosyasının en üstüne yorum olarak ekleyebilirsin

Örneğin `style.css` dosyasının en başına şu şekilde:

```css
/* 
    style.css
    ----------------------------
    Genel stil dosyasıdır. Tüm HTML sayfalarında geçerlidir.
    - Header ve nav menü tasarımı
    - Renk uyumu: Lacivert (#003366), beyaz
    - Kullanıldığı yer: base.html
    Hazırlayan: Çiftçi Yazılım
*/
````

---


