# QR Asset Tag App (AppSheet)

Activity 5, Asset Tag. A mobile app built in Google AppSheet (free prototype plan) that scans an asset's QR code and shows its Picture, Owner, Item Name and Status, plus a dashboard of all assets.

## What the app does

- **Scan:** the scan icon in the search bar reads a QR code with the phone camera and filters the Assets list to the matching asset. Tap the asset to open its detail view.
- **Assets list:** all 15 assets with picture, item name, owner and status (Good or BAD).
- **Dashboard:** three pie charts showing assets by Status, by Designated Owner and by Category.
- **Unknown QR code:** returns no results and the app keeps working.

## Data

Source: `Asset.xlsx`, uploaded to Google Sheets and used as the AppSheet data source. `Assets.csv` in this repo is the same table, rebuilt from the sample file.

| Column | Type in AppSheet | Notes |
| --- | --- | --- |
| Asset Number | Number (key) | 1 to 15 |
| Item Name | Name (label) | Chair 1-5, Table 1-5, Computer 1-5 |
| Description | LongText | Empty in the sample data |
| Category | Enum | Fix Asset, Electronics |
| Status | Enum | Good, BAD |
| Designated Owner | Enum | Jose, Maria |
| Picture | Image | Photo of each item, hosted on Google Drive |
| Asset Code | Text | `AT-01` to `AT-15`; the only searchable and scannable column |

Expected totals: 15 assets; 12 Good and 3 BAD (Chair 5, Table 1, Computer 1); 10 Fix Asset and 5 Electronics; Jose 11 and Maria 4.

## QR codes

Each asset has one QR code that encodes its Asset Code (`AT-01` to `AT-15`), not the plain Asset Number. A plain number such as `5` also matches `15` and any text containing a 5, so a scan returned several assets. The zero-padded code matches exactly one.

`QR_Sheet.png` is a printable A4 sheet with all 15 codes, each labelled with its code and item name.

## Files

| File | Purpose |
| --- | --- |
| `Assets.csv` | The 15 asset records, with the Asset Code column |
| `QR_Sheet.png` | Printable sheet of the 15 QR codes |
| `make_assets.py` | Script that generates `Assets.csv` and `QR_Sheet.png` |

The `Picture` values in `Assets.csv` are placeholder paths. In the live Google Sheet they are Google Drive links to the photos.

## Regenerate the CSV and QR sheet

Requires Python 3 with the `qrcode` and `Pillow` packages.

```
pip install "qrcode[pil]"
python make_assets.py
```

## AppSheet setup summary

1. Import `Assets.csv` into Google Sheets, then create the app from that sheet (Create, App, Start with existing data).
2. Set the column types as in the table above. Asset Number is the key; Item Name is the label.
3. On Asset Code, tick Searchable and Scannable. Untick Searchable on all other columns.
4. Create the Assets view (deck, sorted by Asset Number, no grouping), with Picture as the main image, Designated Owner as the secondary header and Status as the summary column.
5. Create three chart views (aggregate piechart, COUNT) with Chart columns set to Status, Designated Owner and Category. Combine them in a Dashboard view.

## Notes

- Built on the AppSheet free prototype plan, with the built-in scanner only. No paid plan, add-on or API key is used.
- Scanning filters the list to the matching asset; the user taps the result to open the detail view.
- Photos of BAD items (Chair 5, Table 1, Computer 1) are staged to match the Status in the data.
