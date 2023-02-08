class Print:
    def __init__(self, tekst="Tekst Nije Unesen"): 
        self.tekst=tekst
        self.Print_Funkcija()
        
    def Print_Funkcija(self):
            print(self.tekst)


Print("Tekst")
