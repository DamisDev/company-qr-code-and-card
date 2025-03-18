# Digiservice QR Code e Cartellino Aziendale - Start Kit

Questo progetto genera un QR code personalizzato e crea un cartellino aziendale professionale pronto per la stampa e la plastificazione.

### `Per ogni modifica è consigliato usare il branch develop`

## Struttura del Progetto

```
project/
│
├── assets/
│   ├── css/
│   │   └── style.css         # Stili per il cartellino aziendale
│   │
│   └── images/
│       └── company-logo.jpg  # Logo aziendale Digiservice
│
├── output/
│   └── digiservice_qr_code.jpg  # QR code generato (creato automaticamente)
│
├── cartellino-qr.html        # Template HTML per il cartellino
├── config.py                 # File di configurazione
└── main.py                   # Script principale per generare il QR code
```

## Descrizione dei File

### `main.py`
Script Python principale che genera il QR code personalizzato. Funzionalità:
- Creazione di un QR code che punta all'URL specificato in `config.py`
- Aggiunta opzionale del logo aziendale con bordo nero e angoli arrotondati
- Ottimizzazione della qualità dell'immagine per una migliore scansione

### `config.py`
File di configurazione che contiene:
- `DATA`: L'URL di destinazione per il QR code (Linktree Digiservice)
- `QR_CODE_FILE`: Percorso dove salvare il QR code generato
- `LOGO_PATH`: Percorso del logo da sovrapporre al QR code (opzionale)

### `cartellino-qr.html`
Template HTML per creare un cartellino professionale che include:
- Logo dell'azienda nella parte superiore
- QR code con il link a Linktree sulla sinistra
- Spazio per nome e mansione dell'impiegato sulla destra
- Messaggio "Scan to connect with us" nella parte inferiore
- Segni di taglio per facilitare il ritaglio preciso

### `style.css`
File CSS che definisce lo stile del cartellino, inclusi:
- Dimensioni standard di un biglietto da visita (85mm x 55mm)
- Layout responsive con logo, QR code e informazioni dell'impiegato
- Effetti di sfumatura dal nero al rosso sui testi
- Segni di taglio e bordo per la stampa professionale

## Guida all'Uso

### Generazione del QR Code

1. Assicurati di avere Python 3.x installato con le dipendenze richieste:
   ```bash
   pip install qrcode pillow
   ```

2. Aggiorna i valori in `config.py` secondo le tue esigenze:
   ```python
   DATA = "https://linktr.ee/digiserviceSolutions"
   QR_CODE_FILE = "output/digiservice_qr_code.jpg"
   LOGO_PATH = "percorso/al/tuo/logo.jpg"  # Lascia vuoto se non desideri un logo
   ```

3. Esegui lo script principale:
   ```bash
   python main.py
   ```

4. Il QR code verrà generato e salvato nella cartella `output/`

### Creazione del Cartellino

1. Modifica il file `cartellino-qr.html` per personalizzare nome e mansione dell'impiegato:
   ```html
   <div class="employee-info-name">Giuseppe Damis</div>
   <div class="employee-info-job">Software Developer</div>
   ```

2. Apri il file HTML in un browser (Chrome o Firefox)

3. Stampa in PDF:
   - Premi CTRL+P (o CMD+P su Mac)
   - Seleziona "Salva come PDF"
   - Usa l'opzione "Dimensioni effettive"
   - Imposta i margini su "Nessuno"
   - Disabilita intestazioni e piè di pagina

### Consigli per la Stampa e Plastificazione

Per preparare un cartellino di qualità professionale da plastificare:

1. **Carta**: Usa una carta spessa di alta qualità (170-250 g/m²) per una migliore resistenza e aspetto professionale.

2. **Stampante**: Una stampante a colori laser offrirà la migliore qualità e resistenza per il QR code.

3. **Plastificazione**: 
   - Usa una plastificazione di qualità professionale con uno spessore di almeno 125 micron
   - Per una maggiore durabilità, considera una plastificazione opaca che riduce i riflessi e rende più facile la scansione
   - Lascia un bordo di plastificazione di 2-3mm attorno al cartellino per proteggere i bordi

Il QR code così preparato sarà facile da scansionare anche dopo la plastificazione, e il cartellino avrà un aspetto professionale che si adatta bene all'immagine aziendale di Digiservice Solutions.

## Personalizzazione

- **Colori**: Puoi modificare le sfumature nei testi cambiando i valori di colore nel file CSS
- **Logo**: Sostituisci il file `company-logo.jpg` con il logo aziendale
- **Layout**: Modifica il CSS per cambiare la disposizione degli elementi

## Note

Il QR code generato punta a un profilo Linktree che offre ai visitatori la possibilità di scegliere tra diverse destinazioni (sito web aziendale, profilo LinkedIn, ecc.). Questa soluzione permette di aggiornare le destinazioni senza dover rigenerare il QR code.
