def provjera_palindroma(text):
    return  text==text[::-1]

tekst= input("Unesi Rijec :").lower()
print({True: tekst + " je polindrom", False: tekst + " nije polindrom"} [provjera_palindroma(tekst)]) 
