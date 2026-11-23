from docx import Document

d = Document()
d.add_heading("QR Asset Tag App: How I Built It", 0)

def h(t): d.add_heading(t, 1)
def p(t): d.add_paragraph(t)
def num(items):
    for i in items: d.add_paragraph(i, style="List Number")
def bul(items):
    for i in items: d.add_paragraph(i, style="List Bullet")
def table(rows):
    t = d.add_table(rows=len(rows), cols=len(rows[0])); t.style = "Light Grid Accent 1"
    for r, row in enumerate(rows):
        for c, v in enumerate(row): t.cell(r, c).text = v
    d.add_paragraph()

h("Overview")
p("I built a mobile app in AppSheet that scans an asset's QR code and shows its picture, owner, item name and status. It also has a dashboard with charts of all 15 assets. The data comes from the provided sample file, Asset.xlsx, and I used only AppSheet's free plan.")

h("The data")
p("I put the 15 assets from Asset.xlsx into a Google Sheet, which AppSheet reads as its database. The sheet has these columns:")
table([["Column", "What it holds"],
 ["Asset Number", "1 to 15, the unique ID of each asset"],
 ["Item Name", "Chair 1-5, Table 1-5, Computer 1-5"],
 ["Category", "Fix Asset or Electronics"],
 ["Status", "Good or BAD"],
 ["Designated Owner", "Jose or Maria"],
 ["Picture", "Link to the item's photo"],
 ["Asset Code", "The text each QR code contains, AT-01 to AT-15"]])
p("The totals are 12 Good and 3 BAD (Chair 5, Table 1 and Computer 1), 10 Fix Asset and 5 Electronics, and 11 assets for Jose and 4 for Maria.")

h("Pictures")
p("The Picture column in the original file did not work, so I added a photo for each of the 15 items. I uploaded the photos to a Google Drive folder, shared the folder so the app can read it, and used a short formula in the sheet to turn each photo's Drive link into a link AppSheet can display. The photos of the three BAD items (Chair 5, Table 1 and Computer 1) show items that look damaged, so the picture matches the status.")

h("QR codes")
p("Each asset has its own QR code. I made all 15 with a short Python script and put them on one printable page, each labelled with its code and item name (QR_Sheet.png).")
p("The codes contain AT-01 to AT-15 instead of the plain number 1 to 15. At first I used plain numbers, but scanning \"5\" matched every item with a 5 in it, such as 15 and Table 5, so several assets appeared. The zero-padded code, like AT-05, matches only one asset.")
table([["Asset", "QR code contains"],
 ["Chair 5 (asset 5)", "AT-05"],
 ["Computer 2 (asset 12)", "AT-12"],
 ["Computer 5 (asset 15)", "AT-15"]])
d.add_picture("QR_Sheet.png", width=d.sections[0].page_width * 0.6)

h("Building the app in AppSheet")
num(["Connect the data. I created the app from the Google Sheet (Create, App, Start with existing data).",
 "Set up the columns. Asset Number is the key, Item Name is the label, and Category, Status and Designated Owner are drop-down types. Picture is an image.",
 "Turn on scanning. On the Asset Code column I switched on Searchable and Scannable, which adds a scan icon to the search bar. I switched Searchable off on the other columns so a scan matches only the Asset Code.",
 "Assets tab. A list of all 15 assets with the photo, name, owner and status, sorted by Asset Number.",
 "Charts. Three pie charts count the assets by Status, by Designated Owner and by Category.",
 "Dashboard tab. The three charts shown together on one screen.",
 "Home tab. The first screen when the app opens: the status chart with the asset list below it, so the scan icon is available straight away.",
 "Colours. I set the chart colours so BAD and Good are easy to tell apart."])

h("How to use and test it")
num(["Install the AppSheet app on a phone and open Asset Tag.",
 "On the Home or Assets tab, tap the search icon, then the scan icon in the search bar.",
 "Point the camera at a QR code from the printed sheet.",
 "The list narrows to that asset. Tap it to open its details."])
table([["Scan", "Expected result"],
 ["AT-05", "Chair 5, Jose, BAD, with its picture"],
 ["AT-12", "Computer 2, Maria, Good, with its picture"],
 ["Any of the 15 codes", "The matching asset only"],
 ["A QR code not from this sheet", "No result, and the app keeps working"]])
p("The Dashboard tab should show 12 Good and 3 BAD, Jose 11 and Maria 4, and Fix Asset 10 and Electronics 5.")

h("Notes")
bul(["I used only AppSheet's free plan and its built-in scanner. No paid plan, add-on or API key was needed.",
 "Scanning filters the list to the matching asset, and you tap the result to open it, rather than opening the details straight away.",
 "The app only displays the data, since adding and editing assets was outside the task.",
 "The data source is the provided Asset.xlsx, and every record matches it."])

d.save("Documentation.docx")
