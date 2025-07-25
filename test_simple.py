"""Test semplice per verificare che Flask funzioni"""

try:
    # Test import della nostra app
    from app.main import app
    print("✅ App importata correttamente")

    # Test che l'app sia configurata
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("✅ App risponde correttamente")
        else:
            print("❌ App non risponde")
            exit(1)

    print("🎉 Tutti i test sono passati!")
    
except Exception as e:
    print(f"❌ Errore: {e}")
    exit(1)
