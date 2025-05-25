from flask import Flask, render_template, redirect, url_for, request, flash, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import locale
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gelistirme_anahtari'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Türkçe tarih ayarı
try:
    locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')
except locale.Error:
    pass  # Sistem desteklemiyorsa geç

# MODELLER
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Personel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_soyad = db.Column(db.String(200), nullable=False)
    departman = db.Column(db.String(100), nullable=False)

class GirisKaydi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarih_saat = db.Column(db.DateTime, nullable=False)  # Giriş saati
    cikis_saat = db.Column(db.DateTime, nullable=True)   # Yeni: Çıkış saati
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('giris_kayitlari', lazy=True))
# LOGIN
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def before_request():
    g.user = current_user

# ROUTE'LER

@app.route('/')
def base():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(name=name).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            giris_kaydi = GirisKaydi(tarih_saat=datetime.now(), user_id=user.id)
            db.session.add(giris_kaydi)
            db.session.commit()
            flash('Giriş başarılı!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Giriş başarısız. Lütfen kullanıcı adı ve şifreyi kontrol edin.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('username')

        if User.query.filter_by(email=email).first():
            flash('Bu e-posta zaten kayıtlı!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    # En son giriş yapan kaydı bul ve çıkış saatini güncelle
    son_kayit = GirisKaydi.query.filter_by(user_id=current_user.id).order_by(GirisKaydi.tarih_saat.desc()).first()
    if son_kayit and not son_kayit.cikis_saat:
        son_kayit.cikis_saat = datetime.now()
        db.session.commit()

    logout_user()
    return redirect(url_for('base'))

@app.route('/personel/listesi')
@login_required
def personel_listesi():
    personeller = Personel.query.all()
    return render_template('personel_listesi.html', personeller=personeller)

@app.route('/personel/ekle', methods=['GET', 'POST'])
@login_required
def personel_ekle():
    if request.method == 'POST':
        ad_soyad = request.form.get('ad_soyad')
        departman = request.form.get('departman')
        yeni_personel = Personel(ad_soyad=ad_soyad, departman=departman)
        db.session.add(yeni_personel)
        db.session.commit()
        flash('Personel başarıyla eklendi!', 'success')
        return redirect(url_for('personel_listesi'))
    return render_template('personel_ekle.html')

@app.route('/personel/duzenle/<int:id>', methods=['GET', 'POST'])
@login_required
def personel_duzenle(id):
    personel = Personel.query.get_or_404(id)
    if request.method == 'POST':
        personel.ad_soyad = request.form.get('ad_soyad')
        personel.departman = request.form.get('departman')
        db.session.commit()
        flash('Personel başarıyla güncellendi!', 'success')
        return redirect(url_for('personel_listesi'))
    return render_template('personel_duzenle.html', personel=personel)

@app.route('/giris/kayitlari')
@login_required
def giris_kayitlari():
    kayitlar = GirisKaydi.query.order_by(GirisKaydi.tarih_saat.desc()).all()
    giris_kayitlari = []

    for kayit in kayitlar:
        giris_kayitlari.append({
            'ad_soyad': kayit.user.name,
            'tarih': kayit.tarih_saat.strftime('%d %B %Y'),
            'giris_saati': kayit.tarih_saat.strftime('%H:%M:%S'),
            'cikis_saati': kayit.cikis_saat.strftime('%H:%M:%S') if kayit.cikis_saat else '---'
        })

    return render_template('giris_kayitlari.html', giris_kayitlari=giris_kayitlari)

# UYGULAMA BAŞLATMA
import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
