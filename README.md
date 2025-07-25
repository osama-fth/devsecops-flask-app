# DevSecOps Flask App

Una semplice applicazione Flask containerizzata con Docker e testata tramite GitHub Actions CI/CD.

## 🚀 Funzionalità
- 🐍 **Flask backend** - Applicazione web minimalista
- 🧪 **Test automatici** - Test semplici con Python
- ⚙️ **CI/CD Pipeline** - GitHub Actions per testing automatico
- 🐳 **Dockerizzata** - Container pronto per il deploy

## 🛠️ Esecuzione Locale

### Con Python
```bash
# Installa dipendenze
pip install -r requirements.txt

# Avvia l'applicazione
python app/main.py
```

### Con Docker
```bash
# Build del container
docker build -t flask-app .

# Esecuzione del container
docker run -p 8080:8080 flask-app
```

Vai su: **http://localhost:8080**

## 🧪 Testing

### Test locale
```bash
python test_simple.py
```

### CI/CD
La pipeline GitHub Actions si attiva automaticamente su:
- Push al branch `main`
- Pull request verso `main`

## 📁 Struttura Progetto
```
devsecops-flask-app/
├── app/
│   └── main.py          # Applicazione Flask
├── .github/workflows/
│   └── ci.yml          # Pipeline CI/CD
├── test_simple.py      # Test semplici
├── requirements.txt    # Dipendenze Python
├── dockerfile         # Configurazione Docker
└── README.md          # Documentazione
```

## 🎯 Primi Passi DevSecOps
Questo progetto dimostra i concetti base di DevSecOps:
- **Dev**: Sviluppo con Flask
- **Sec**: Best practices di sicurezza
- **Ops**: Automazione CI/CD e containerizzazione
