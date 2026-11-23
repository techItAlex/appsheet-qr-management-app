# QR Asset Tag App (AppSheet)

Activity 5, Asset Tag. A mobile app built in Google AppSheet (free prototype plan). It scans an asset's QR code and shows the asset's **Picture, Owner, Item Name and Status**, and has a dashboard with charts of all assets.

## Try the app (for the instructor)

> **App link:** `PASTE YOUR APPSHEET APP LINK HERE`
> **Data source (Google Sheet):** `PASTE YOUR GOOGLE SHEET LINK HERE`

You need two things: the app and a QR code to scan.

1. **Open the app.**
   - **On a phone (best, camera scanning works):** install the free **AppSheet** app (Android / iOS), sign in with the Google account the app was shared with, and open **Asset Tag**. Or open the app link above in the phone's browser.
   - **On a computer:** open the app link in a browser. The scan icon needs a camera, so use a phone for scanning (see step 3 for a no-camera alternative).
2. **Get the QR codes.** Open [`QR_Sheet.png`](QR_Sheet.png) in this repo. It has all 15 codes, each labelled with its code and item name. Show it on a second screen or print it.
3. **Scan.** On the **Home** or **Assets** tab tap the **search** icon, then the **scan** icon in the search bar, and point the camera at a code.
   - *No camera?* Type the code (e.g. `AT-05`) into the search bar. It does the same filter.
4. **View the result.** The list narrows to the one matching asset. Tap it to see its details.
5. **Open the Dashboard tab** to see the charts.

### What you should see

| Action | Expected result |
| --- | --- |
| Scan `AT-05` | Chair 5, Jose, **BAD**, with its picture |
| Scan `AT-12` | Computer 2, Maria, **Good**, with its picture |
| Scan any of the 15 codes | Only the matching asset |
| Scan a QR code not from the sheet | No results; the app keeps working |
| Dashboard tab | Status: 12 Good / 3 BAD. Owner: Jose 11 / Maria 4. Category: Fix Asset 10 / Electronics 5 |

## What the app does

- **Scan:** reads a QR code with the phone camera and filters the Assets list to the matching asset.
- **Assets list:** all 15 assets with picture, item name, owner and status (Good or BAD).
- **Dashboard:** three pie charts of assets by Status, by Designated Owner and by Category.
- **Home:** the first screen, with the status chart and the asset list so scanning is available immediately.
- **Unknown QR code:** returns no results and the app keeps working.

## Data

Source: `Asset.xlsx` (provided sample), uploaded to Google Sheets and used as the AppSheet data source. `Assets.csv` in this repo is the same table, rebuilt from the sample file.

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

Totals: 15 assets; 12 Good and 3 BAD (Chair 5, Table 1, Computer 1); 10 Fix Asset and 5 Electronics; Jose 11 and Maria 4.

## How it works: QR codes

Each asset has one QR code that encodes its **Asset Code** (`AT-01` to `AT-15`), not the plain Asset Number. A plain number such as `5` also matches `15` and any text containing a 5, so a scan returned several assets. The zero-padded code matches exactly one.

| Asset | QR code contains |
| --- | --- |
| Chair 5 (asset 5) | `AT-05` |
| Computer 2 (asset 12) | `AT-12` |
| Computer 5 (asset 15) | `AT-15` |

## How it was built (AppSheet setup)

1. Import `Assets.csv` into Google Sheets, then create the app from that sheet (Create, App, Start with existing data).
2. Set the column types as in the table above. Asset Number is the key; Item Name is the label.
3. On Asset Code, tick **Searchable** and **Scannable** (this adds the scan icon to the search bar). Untick Searchable on all other columns so a scan matches only the Asset Code.
4. Create the Assets view (deck, sorted by Asset Number, no grouping), with Picture as the main image, Designated Owner as the secondary header and Status as the summary column.
5. Create three chart views (aggregate piechart, COUNT) with Chart columns set to Status, Designated Owner and Category. Combine them in a Dashboard view.
6. Set the chart colours so BAD and Good are easy to tell apart.

## Files

| File | Purpose |
| --- | --- |
| `Assets.csv` | The 15 asset records, with the Asset Code column |
| `QR_Sheet.png` | Printable sheet of the 15 QR codes |
| `make_assets.py` | Script that generates `Assets.csv` and `QR_Sheet.png` |
| `Documentation.docx` | Write-up of how the app was built and tested |
| `make_doc.py` | Script that generates `Documentation.docx` |

The `Picture` values in `Assets.csv` are placeholder paths. In the live Google Sheet they are Google Drive links to the photos.

## Regenerate the CSV and QR sheet

Requires Python 3 with the `qrcode` and `Pillow` packages.

```
pip install "qrcode[pil]"
python make_assets.py
```

## Notes

- Built on the AppSheet free prototype plan, with the built-in scanner only. No paid plan, add-on or API key is used.
- Scanning filters the list to the matching asset; the user taps the result to open the detail view.
- The app only displays the data; adding and editing assets was outside the task.
- Photos of BAD items (Chair 5, Table 1, Computer 1) are staged to match the Status in the data.
