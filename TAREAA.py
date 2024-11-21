while True:
    print("Cálculo del puntaje")
    
    
    fichas_rojas = 3  
    fichas_amarillas = 4  
    fichas_azules = 6  
    
    # Cálculo del puntaje
    puntaje = (fichas_rojas ** 3) + (2 * fichas_azules) - (fichas_amarillas ** 2)
    print(f"Fichas rojas: {fichas_rojas}")
    print(f"Fichas azules: {fichas_azules}")
    print(f"Fichas amarillas: {fichas_amarillas}")
    print(f"Puntaje total: {puntaje}")
    
    # Preguntar si el usuario desea realizar otro cálculo
    repetir = input("\n¿Deseas calcular nuevamente el puntaje? (s/n): ").strip().lower()
    if repetir != 's':
        print("ADIOS")
        break
