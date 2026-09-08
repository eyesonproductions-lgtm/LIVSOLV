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
| cooking-during-power-outage.html | BioLite EcoZoom Dura | Manufacturer | Available at audit | EcoZoom Versa is a functional alternate where dual-fuel capability is useful |
| cooking-during-power-outage.html | BioLite EcoZoom Versa | Manufacturer | Available at audit | EcoZoom Dura is lower-cost alternate |
| cooking-during-power-outage.html | GoSun Sport | Do not recommend as primary | Sold out at audit | Recommend current Sport-E instead |
| cooking-during-power-outage.html | GoSun Sport-E | Manufacturer | Available at audit | Go for smaller use case; Fusion for family-size use case |
| cooking-during-power-outage.html | GoSun Go | Manufacturer | Available at audit | Sport-E for larger/hybrid use case |
| cooking-during-power-outage.html | GoSun Fusion | Manufacturer | Available at audit | Sport-E for smaller household use case |
| emergency-communications.html | Midland ER310 / ER310PRO family | Manufacturer/current lineup | Audited 2026-09-08 | Prefer current ER310PRO where available; ER310 remains fallback |
| emergency-communications.html | Midland FRS radios | Manufacturer/current lineup | Older exact SKU risk identified | Link to current lineup unless exact current model is verified |
| emergency-communications.html | ZOLEO Satellite Communicator | Manufacturer | Audited; volatile price removed from page | Manufacturer product page |
| emergency-communications.html | Garmin inReach Messenger Plus | Manufacturer | Audited; volatile price removed from page | Manufacturer product page |
| emergency-water-treatment.html | Sawyer Squeeze | Manufacturer | Available/current at audit | Keep manufacturer link until exact Amazon ASIN is verified |
| emergency-water-treatment.html | LifeStraw Peak Series Gravity Purifier | Manufacturer | Available/current at audit; current page shows Add to cart and virus-removal specification | If purifier is unavailable, do not silently substitute the similarly named 8L Gravity Filter because that filter does not provide the same virus-removal capability |
| emergency-water-treatment.html | GRAYL GeoPress 24 oz Purifier | Manufacturer | Current Nature and Covert purifier variants available at audit | Link to GeoPress collection/current variant if a color-specific page becomes unavailable |

## Important product distinctions discovered during audit

### LifeStraw Peak Series
The `Peak Series Gravity Purifier with virus removal` and `Peak Series Gravity Filter System - 8L` are not interchangeable recommendations. The purifier is specified for viruses, bacteria and parasites. The standard 8L gravity filter is specified for bacteria and parasites but not viruses. A sold-out purifier must therefore not be replaced with the standard filter while preserving a claim of virus protection.

### GRAYL GeoPress
Current GeoPress purifier bottles were available during the 2026-09-08 audit, while some replacement-cartridge variants/options showed sold-out states. Product availability and replacement-cartridge availability must be treated separately.

## Next audit queue

1. emergency-water-storage.html
2. car-emergency-kit.html
3. best-emergency-food-kits.html
4. best-home-first-aid-kits.html
5. generator-backup-power.html
6. small-backup-power.html
7. solar-power-bank-vs-folding-panel.html
8. solar-recharging-power-station.html
9. home-power-outage-essentials.html

## Future automation boundary

Safe automated checks may validate internal links and ordinary non-Amazon external URLs for HTTP failures. They must not be treated as proof of inventory, because sold-out pages commonly return HTTP 200. Amazon availability/price should not be scraped. Product availability requires a separate commerce audit using permitted public/manufacturer information or approved Amazon tooling when available.
