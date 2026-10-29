import csv, qrcode
from PIL import Image, ImageDraw, ImageFont

rows = []
for n in range(1, 16):
    if n <= 5: name, cat = f"Chair {n}", "Fix Asset"
    elif n <= 10: name, cat = f"Table {n-5}", "Fix Asset"
    else: name, cat = f"Computer {n-10}", "Electronics"
    status = "BAD" if n in (5, 6, 11) else "Good"
    owner = "Jose" if n <= 11 else "Maria"  # from PDF row order; confirm in Asset.xlsx
    rows.append([n, name, "", cat, status, owner, f"pictures/{name.split()[0].lower()}.png", f"AT-{n:02d}"])

with open("Assets.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Asset Number", "Item Name", "Description", "Category", "Status", "Designated Owner", "Picture", "Asset Code"])
    w.writerows(rows)

try: font = ImageFont.truetype("arial.ttf", 28); small = ImageFont.truetype("arial.ttf", 22)
except OSError: font = small = ImageFont.load_default()

# A4 at 150 dpi, 3 columns x 5 rows
W, H = 1240, 1754
sheet = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(sheet)
cw, ch = W // 3, H // 5
for i, r in enumerate(rows):
    qr = qrcode.QRCode(box_size=8, border=2); qr.add_data(r[7]); qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB").resize((300, 300))
    x, y = (i % 3) * cw, (i // 3) * ch
    sheet.paste(img, (x + (cw - 300) // 2, y + 20))
    d.text((x + cw // 2, y + 335), f"{r[7]}  {r[1]}", fill="black", font=font, anchor="mm")
    d.rectangle([x + 10, y + 10, x + cw - 10, y + ch - 10], outline="#bbbbbb")
sheet.save("QR_Sheet.png")
