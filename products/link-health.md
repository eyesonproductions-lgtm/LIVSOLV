# LivSolv Commerce Link Health Registry

Last audit: 2026-09-08

## Rules

- Verify the exact product and current manufacturer page before adding a recommendation.
- Never invent an Amazon ASIN. Add an Amazon Special Link only after the exact model/ASIN is verified.
- Every Amazon affiliate recommendation must have a clear nearby disclosure. Site-wide disclosure remains at `/affiliate-disclosure.html`.
- Do not hard-code volatile Amazon prices or availability.
- Prefer current models with stable distribution. When a product is stock-sensitive, provide a legitimate substitute or manufacturer/category fallback.
- A page returning HTTP 200 does not prove that a product is in stock. Availability must be checked separately.
- Do not automatically scrape Amazon product pages for stock or price monitoring.
- Re-audit commercial recommendations when a reader reports an unavailable product, when a manufacturer replaces a model, and during scheduled commerce maintenance.
- Firsthand labels require actual ownership/use. If the exact model cannot be identified, describe the verified firsthand experience without inventing specifications or a brand.

## Audited recommendations

| Page | Product | Destination status | Availability/status checked | Fallback / action |
|---|---|---|---|---|
| fridge-freezer-backup-power.html | EcoFlow DELTA 3 Plus | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| fridge-freezer-backup-power.html | Jackery Explorer 2000 v2 | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| fridge-freezer-backup-power.html | BLUETTI AC200L | Manufacturer only | Amazon ASIN not verified with sufficient confidence | Do not add Amazon link until exact ASIN is verified |
| 72-hour-backup-power.html | Jackery Explorer 2000 v2 | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| 72-hour-backup-power.html | EcoFlow DELTA 3 Plus | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| 72-hour-backup-power.html | BLUETTI AC200L | Manufacturer only | Amazon ASIN not verified with sufficient confidence | Do not add Amazon link until exact ASIN is verified |
| cooking-during-power-outage.html | Coleman Cascade Classic | Manufacturer/current lineup | Audited 2026-09-08 | Use current Coleman stove lineup if exact model becomes unavailable |
| cooking-during-power-outage.html | BioLite EcoZoom Dura / Versa | Manufacturer | Available at audit | Each is a functional alternate depending use case |
| cooking-during-power-outage.html | GoSun Sport | Do not recommend as primary | Sold out at audit | Recommend current Sport-E instead |
| cooking-during-power-outage.html | GoSun Sport-E / Go / Fusion | Manufacturer | Available at audit | Choose size/capability appropriate to household |
| emergency-communications.html | Midland ER310 / ER310PRO family | Manufacturer/current lineup | Audited 2026-09-08 | Prefer current ER310PRO where available; ER310 remains fallback |
| emergency-communications.html | Midland FRS radios | Manufacturer/current lineup | Older exact SKU risk identified | Link to current lineup unless exact current model is verified |
| emergency-communications.html | ZOLEO Satellite Communicator | Manufacturer | Audited; volatile price removed | Manufacturer product page |
| emergency-communications.html | Garmin inReach Messenger Plus | Manufacturer | Audited; volatile price removed | Manufacturer product page |
| emergency-water-treatment.html | Sawyer Squeeze | Manufacturer | Available/current at audit | Keep manufacturer link until exact Amazon ASIN is verified |
| emergency-water-treatment.html | LifeStraw Peak Series Gravity Purifier | Manufacturer | Available/current at audit | Never substitute standard 8L Gravity Filter while preserving virus-removal claim |
| emergency-water-treatment.html | GRAYL GeoPress 24 oz Purifier | Manufacturer collection | Nature and Covert variants available 2026-09-08 | Collection link now used so color-specific slug changes do not break recommendation; cartridge inventory tracked separately |
| car-emergency-kit.html | NOCO Boost GB40 | Manufacturer | Current recommendation retained | Jumper cables provide battery-free fallback architecture |
| car-emergency-kit.html | Slime 12V Digital Tire Inflator #40088 | Manufacturer | Current product page and specs verified 2026-09-08 | 12V vehicle power avoids separate inflator battery maintenance |
| car-emergency-kit.html | DEWALT DCC020IB | Manufacturer | Current product page verified 2026-09-08 | Upgrade for households already using DEWALT 20V ecosystem; 12V DC is alternate input |
| car-emergency-kit.html | Unbranded solar + USB flashlight | Firsthand LivSolv use; no commerce link | Owned and used; exact manufacturer/model unknown | Recommend feature architecture only. Do not invent brand, capacity, charge time or ASIN |

## Important product distinctions discovered during audit

### LifeStraw Peak Series
The `Peak Series Gravity Purifier with virus removal` and `Peak Series Gravity Filter System - 8L` are not interchangeable recommendations. The purifier is specified for viruses, bacteria and parasites. The standard 8L gravity filter is specified for bacteria and parasites but not viruses.

### GRAYL GeoPress
Current GeoPress purifier bottles were available during the 2026-09-08 audit, while replacement-cartridge inventory can differ. Product availability and replacement-cartridge availability must be treated separately.

### LivSolv-owned solar flashlight
LivSolv owns and uses an unbranded flashlight with integrated solar panel, USB input, USB output, main beam and COB side light. It is kept in a sunny window and has remained ready in household use. Because there is no identifiable brand/model, the site may describe this firsthand experience but must not attach unsupported battery capacity, recharge-time or manufacturer claims.

## Next audit queue

1. emergency-water-storage.html
2. best-emergency-food-kits.html
3. best-home-first-aid-kits.html
4. generator-backup-power.html
5. small-backup-power.html
6. solar-power-bank-vs-folding-panel.html
7. solar-recharging-power-station.html
8. home-power-outage-essentials.html

## Future automation boundary

Safe automated checks may validate internal links and ordinary non-Amazon external URLs for HTTP failures. They must not be treated as proof of inventory, because sold-out pages commonly return HTTP 200. Amazon availability/price should not be scraped. Product availability requires a separate commerce audit using permitted public/manufacturer information or approved Amazon tooling when available.
