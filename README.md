# **Linux Systemd Log Analyzer with FastAPI and Groq**

Bu proje, Linux sistem loglarını analiz eden bir FastAPI uygulamasıdır. Sistem logları Groq API kullanılarak analiz edilir ve sonuçlar temiz bir HTML formatında sunulur. 

## 🚀 **Özellikler**
- **Linux Sistem Log Analizi**: `dmesg` komutu kullanarak sistem loglarını çeker.
- **Groq API Desteği**: LangChain ile entegre bir Groq Chat modeli kullanarak logları analiz eder.
- **FastAPI Uygulaması**: Analiz sonuçlarını HTML formatında bir web arayüzünde gösterir.
- **Kolay Kurulum**: `.env` dosyası aracılığıyla Groq API anahtarı hızlı bir şekilde eklenir.

---

## 🛠️ **Gereksinimler**

Bu projeyi çalıştırmak için aşağıdaki yazılım ve araçlar gereklidir:

- **Python** (3.8 veya daha yeni sürüm)
- **Linux** (dmesg komutunun desteklendiği bir sistem)
- **pip** (Python bağımlılık yöneticisi)
- Bir **Groq API anahtarı** (https://console.groq.com adresinden alınabilir)

---

## 📦 **Kurulum**

1. **Depoyu klonlayın:**

```bash
git clone https://github.com/kullaniciadi/linux-log-analyzer.git
cd linux-log-analyzer
```

2. **Gereksinimleri yükleyin:**

```bash
pip install -r requirements.txt
```

3. **Çevresel değişkenleri ekleyin:**

Proje dizininde bir `.env` dosyası oluşturun ve Groq API anahtarınızı aşağıdaki şekilde ekleyin:

```env
GROQ_API_KEY=your_api_key_here
```

4. **Uygulamayı başlatın:**

```bash
uvicorn main:app --reload
```

5. **Uygulamayı tarayıcıda görüntüleyin:**

Tarayıcınızı açarak aşağıdaki adrese gidin:

```
http://127.0.0.1:8000
```

---

## 📝 **Kullanım**

1. **Sistem Logları**: Uygulama, `dmesg` komutu kullanarak Linux sistemindeki son 100 satırı otomatik olarak çeker.
2. **Analiz**: Groq Chat modeli ile loglar analiz edilerek temiz bir çıktı oluşturulur.
3. **Sonuç Gösterimi**: Analiz sonuçları bir HTML sayfasında kullanıcıya sunulur.

---

## 📂 **Proje Yapısı**

```
linux-log-analyzer/
│
├── main.py                 # FastAPI uygulaması
├── requirements.txt        # Gerekli bağımlılıkların listesi
├── .env                    # Çevresel değişkenler (API Anahtarı)
└── README.md               # Proje açıklaması
```

---

## 💻 **Örnek Kullanım**

1. Servisi başlattığınızda `http://127.0.0.1:8000` adresine gidin.  
2. HTML formatında analiz edilmiş sistem loglarını görebilirsiniz.

---

## 🔧 **Sık Karşılaşılan Hatalar**

1. **Groq API Anahtarı Hatası**:  
   - `.env` dosyasına doğru anahtarın eklenip eklenmediğini kontrol edin.
   - API anahtarının geçerli olduğundan emin olun.

2. **Bağımlılık Hataları**:  
   - `requirements.txt` dosyasındaki bağımlılıkları doğru bir Python ortamında yüklediğinizden emin olun.

---

## 🤝 **Katkıda Bulunma**

Katkılarınızı bekliyoruz! Projeye katkıda bulunmak için:

1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun: `git checkout -b feature-branch`.
3. Değişikliklerinizi yapın ve commit edin: `git commit -m 'Yeni özellik ekle'`.
4. Branch'i gönderin: `git push origin feature-branch`.
5. Bir pull request (PR) oluşturun.

---

## 📃 **Lisans**

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) kapsamında lisanslanmıştır.

---

## 💬 **İletişim**

Proje ile ilgili sorularınız veya geri bildirimleriniz için lütfen benimle iletişime geçin:

- **GitHub**: [kullaniciadi](https://github.com/kullaniciadi)
- **E-posta**: example@email.com

---

Bu README dosyasını projenizin dizinine ekleyerek, GitHub üzerinde paylaşabilirsiniz.
