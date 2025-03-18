import qrcode
from PIL import Image, ImageDraw, ImageOps
import os
from config import DATA, QR_CODE_FILE, LOGO_PATH

# Crea la cartella di output se non esiste
os.makedirs("output", exist_ok=True)

# Se esiste già un QR Code, lo rimuoviamo
if os.path.exists(QR_CODE_FILE):
    os.remove(QR_CODE_FILE)

# Creazione del QR Code
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(DATA)
qr.make(fit=True)

# Creazione immagine QR
qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

# Controlliamo se il logo esiste prima di aggiungerlo
if LOGO_PATH and os.path.exists(LOGO_PATH):
    print("[INFO] Logo trovato! Lo aggiungo al QR Code...")

    # Carica il logo originale con la massima qualità
    logo = Image.open(LOGO_PATH).convert("RGBA")

    # Impostiamo la dimensione del logo mantenendo le proporzioni
    max_logo_size = int(qr_img.size[0] * 0.3)  # 30% della larghezza del QR Code
    
    # Calcola le nuove dimensioni mantenendo l'aspect ratio
    logo_width, logo_height = logo.size
    ratio = min(max_logo_size / logo_width, max_logo_size / logo_height)
    new_width = int(logo_width * ratio)
    new_height = int(logo_height * ratio)
    
    # Ridimensiona il logo usando LANCZOS per la massima qualità
    logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Calcola lo spessore del bordo (3% della dimensione minima del logo, minimo 2 pixel)
    border_thickness = max(int(min(new_width, new_height) * 0.03), 2)
    
    # Calcola il raggio per gli angoli arrotondati
    border_radius = min(new_width, new_height) // 4
    
    # Crea una nuova immagine con bordo nero (dimensioni aumentate dello spessore del bordo)
    bordered_logo_width = new_width + (2 * border_thickness)
    bordered_logo_height = new_height + (2 * border_thickness)
    bordered_logo = Image.new("RGBA", (bordered_logo_width, bordered_logo_height), (0, 0, 0, 0))
    
    # Crea la maschera per il bordo esterno arrotondato
    outer_mask = Image.new("L", (bordered_logo_width, bordered_logo_height), 0)
    draw_outer = ImageDraw.Draw(outer_mask)
    draw_outer.rounded_rectangle((0, 0, bordered_logo_width-1, bordered_logo_height-1), 
                               radius=border_radius + border_thickness, fill=255)
    
    # Crea un'immagine temporanea per il bordo nero
    black_border = Image.new("RGBA", (bordered_logo_width, bordered_logo_height), (0, 0, 0, 255))
    
    # Applica la maschera esterna al bordo nero
    black_border_masked = Image.new("RGBA", (bordered_logo_width, bordered_logo_height), (0, 0, 0, 0))
    black_border_masked.paste(black_border, (0, 0), outer_mask)
    
    # Crea la maschera per l'area interna (più piccola)
    inner_mask = Image.new("L", (bordered_logo_width, bordered_logo_height), 0)
    draw_inner = ImageDraw.Draw(inner_mask)
    draw_inner.rounded_rectangle((border_thickness, border_thickness, 
                               bordered_logo_width - border_thickness - 1, 
                               bordered_logo_height - border_thickness - 1), 
                              radius=border_radius, fill=255)
    
    # Crea un'immagine bianca per "ritagliare" il bordo interno
    white_fill = Image.new("RGBA", (bordered_logo_width, bordered_logo_height), (255, 255, 255, 255))
    
    # Applica la maschera interna all'immagine bianca
    white_masked = Image.new("RGBA", (bordered_logo_width, bordered_logo_height), (0, 0, 0, 0))
    white_masked.paste(white_fill, (0, 0), inner_mask)
    
    # Combina il bordo nero con l'area bianca interna
    bordered_bg = Image.alpha_composite(black_border_masked, white_masked)
    
    # Ora inseriamo il logo nell'area bianca
    # Creiamo una maschera per il logo con gli stessi angoli arrotondati
    logo_mask = Image.new("L", logo.size, 0)
    draw_logo = ImageDraw.Draw(logo_mask)
    draw_logo.rounded_rectangle((0, 0, new_width-1, new_height-1), radius=border_radius, fill=255)
    
    # Posizione per centrare il logo all'interno del bordo
    logo_position = (border_thickness, border_thickness)
    
    # Applichiamo il logo con la sua maschera
    bordered_bg.paste(logo, logo_position, logo_mask)
    
    # Ottieni le dimensioni finali del logo con bordo
    final_logo = bordered_bg
    
    # Calcola la posizione centrale nel QR code
    qr_width, qr_height = qr_img.size
    position_x = (qr_width - bordered_logo_width) // 2
    position_y = (qr_height - bordered_logo_height) // 2
    
    # Inserisci il logo con bordo nel QR code
    qr_img.paste(final_logo, (position_x, position_y), final_logo)
    
    print("[OK] Logo con bordo nero e angoli arrotondati applicato in alta definizione!")
elif LOGO_PATH:
    print("[ERRORE] Logo specificato ma non trovato al percorso:", LOGO_PATH)
else:
    print("[INFO] Nessun logo specificato, il QR Code sarà senza logo.")

# --- AGGIUNGI BORDO ALL'INTERO QR CODE ---
# Configurazione del bordo del QR code
qr_border_width = 8  # Spessore del bordo in pixel
qr_border_color = (0, 0, 0)  # Colore del bordo (nero)
qr_border_radius = 30  # Raggio degli angoli arrotondati

# Ottieni le dimensioni del QR code
qr_width, qr_height = qr_img.size

# Crea una nuova immagine con le dimensioni aumentate per il bordo
final_width = qr_width + (2 * qr_border_width)
final_height = qr_height + (2 * qr_border_width)
final_img = Image.new("RGB", (final_width, final_height), qr_border_color)

# Per creare angoli arrotondati, usiamo una maschera
mask = Image.new("L", (final_width, final_height), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle((0, 0, final_width-1, final_height-1), 
                           radius=qr_border_radius, fill=255)

# Creiamo un'immagine temporanea per il contenuto interno (bianco)
temp_img = Image.new("RGB", (final_width, final_height), qr_border_color)

# Incolla il QR code al centro della nuova immagine
temp_img.paste(qr_img, (qr_border_width, qr_border_width))

# Applica la maschera con angoli arrotondati
final_img = temp_img
if qr_border_radius > 0:
    # Conserva solo l'area definita dalla maschera
    final_img.putalpha(mask)
    # Converti di nuovo a RGB (perdendo la trasparenza)
    final_img = final_img.convert("RGB")

# Salvataggio del QR Code con il nuovo nome
final_img.save(QR_CODE_FILE, quality=95)  # Aumentiamo la qualità del salvataggio JPEG
print(f"[COMPLETO] QR Code con bordo salvato correttamente in: {QR_CODE_FILE}")
print(f"[INFO] Il QR Code punta a: {DATA}")