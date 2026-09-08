# LivSolv Commerce Link Health Registry

Last audit: 2026-09-08

## Rules
- Verify the exact product and current manufacturer or retailer page before adding a recommendation.
- Never invent an Amazon ASIN. Add an Amazon Special Link only after the exact model/ASIN is verified.
- Every Amazon affiliate recommendation must have a clear nearby disclosure. Site-wide disclosure remains at `/affiliate-disclosure.html`.
- Do not hard-code volatile Amazon prices or availability.
- Prefer current models with stable distribution. When a product is stock-sensitive, provide a legitimate substitute or manufacturer/category fallback.
- A page returning HTTP 200 does not prove that a product is in stock. Availability must be checked separately.
- Do not automatically scrape Amazon product pages for stock or price monitoring.
- Re-audit commercial recommendations when a reader reports an unavailable product, when a manufacturer replaces a model, and during scheduled commerce maintenance.
- Firsthand labels require actual ownership/use. Discontinued owned products may be used as firsthand examples, but must not be presented as current shopping recommendations.

## Audited recommendations
| Page | Product | Destination status | Availability/status checked | Fallback / action |
|---|---|---|---|---|
| fridge-freezer-backup-power.html | EcoFlow DELTA 3 Plus | Amazon affiliate + manufacturer fallback | Exact Amazon product verified | Manufacturer fallback retained |
| fridge-freezer-backup-power.html | Jackery Explorer 2000 v2 | Amazon affiliate + manufacturer fallback | Exact Amazon product verified | Manufacturer fallback retained |
| fridge-freezer-backup-power.html | BLUETTI AC200L | Manufacturer only | Amazon ASIN not verified sufficiently | Do not add Amazon link until exact ASIN verified |
| 72-hour-backup-power.html | Jackery Explorer 2000 v2 | Amazon affiliate + manufacturer fallback | Exact Amazon product verified | Manufacturer fallback retained |
| 72-hour-backup-power.html | EcoFlow DELTA 3 Plus | Amazon affiliate + manufacturer fallback | Exact Amazon product verified | Manufacturer fallback retained |
| cooking-during-power-outage.html | GoSun Sport | Do not recommend as primary | Sold out at audit | Recommend current Sport-E instead |
| cooking-during-power-outage.html | GoSun Sport-E / Go / Fusion | Manufacturer | Available at audit | Choose appropriate size/capability |
| emergency-communications.html | Midland ER310 / ER310PRO family | Manufacturer/current lineup | Audited 2026-09-08 | Prefer current ER310PRO where available; ER310 fallback |
| emergency-water-treatment.html | Sawyer Squeeze | Manufacturer | Available/current | Keep manufacturer link until exact Amazon ASIN verified |
| emergency-water-treatment.html | LifeStraw Peak Series Gravity Purifier | Manufacturer | Available/current | Never substitute standard 8L Gravity Filter while preserving virus-removal claim |
| emergency-water-treatment.html | GRAYL GeoPress 24 oz Purifier | Manufacturer collection | Nature and Covert variants available | Collection link used; cartridge inventory separate |
| emergency-water-storage.html | Reliance Aqua-Tainer 7 gallon | Current retailer distribution | Prior LivSolv URL incorrectly pointed to 4-gallon model | Corrected exact 7-gallon listing; Jumbo-Tainer fallback |
| emergency-water-storage.html | Reliance Jumbo-Tainer 7 gallon | Current retailer product | Available at audit | Same-capacity fallback |
| emergency-water-storage.html | WaterBrick 3.5 gallon | Manufacturer live shop | Current packs available | Shop used because colors/pack sizes change |
| emergency-water-storage.html | waterBOB | Manufacturer exact product | In stock at audit | Exact product retained; one-time-use limitation stated |
| generator-backup-power.html | etrailer 4,500-Watt Dual-Fuel Portable RV Generator #333-0005 | Firsthand LivSolv-owned + exact retailer product | Rechecked 2026-09-08 and listed in stock | Keep non-inverter/sensitive-electronics warning prominent |
| car-emergency-kit.html | NOCO Boost GB40 | Manufacturer | Current recommendation retained | Jumper cables provide battery-free fallback |
| car-emergency-kit.html | Slime 12V Digital Tire Inflator #40088 | Manufacturer | Current official product | 12V vehicle power avoids separate battery maintenance |
| car-emergency-kit.html | DEWALT DCC020IB | Manufacturer | Current official product | 12V DC alternate power path |
| car-emergency-kit.html | Unbranded solar + USB flashlight | Firsthand; no commerce link | Owned and used; manufacturer unknown | Recommend feature architecture only |
| small-backup-power.html | Goal Zero Yeti 150 | Firsthand; archived/discontinued | Goal Zero archive verified | Example only, never current purchase recommendation |
| small-backup-power.html | Anker SOLIX C300 | Current manufacturer product | Buy-now/current product verified 2026-09-08; 288Wh, 300W AC, 140W USB-C, 100W solar | Jackery 300 Plus is same-class fallback |
| small-backup-power.html | Jackery Explorer 300 Plus | Current manufacturer product | Current selectable product and fresh support specs verified 2026-09-08; 288Wh, 300W, 100W USB-C/solar | Anker C300 is same-class fallback |
| small-backup-power.html | EcoFlow RIVER 3 | Removed from primary buy list | EcoFlow US pages showed standalone model sold out/preorder during 2026-09-08 audit | Do not route shoppers to it while unavailable; Anker/Jackery current alternatives used |
| solar-power-bank-vs-folding-panel.html | Goal Zero Yeti 150 | Firsthand; archived/discontinued | Archive confirms 168Wh AGM and solar compatibility | Route shoppers to current equipment |
| solar-power-bank-vs-folding-panel.html | Goal Zero Sherpa 100PD | Current manufacturer product | Verified 2026-09-08 | Use current Goal Zero lineup if model changes |
| solar-power-bank-vs-folding-panel.html | Goal Zero Nomad 20 | Current manufacturer product | Verified 2026-09-08 | Pair only with compatible input architecture |

## Important product distinctions discovered during audit
### LifeStraw Peak Series
The `Peak Series Gravity Purifier with virus removal` and `Peak Series Gravity Filter System - 8L` are not interchangeable. The purifier is specified for viruses, bacteria and parasites. The standard 8L gravity filter is specified for bacteria and parasites but not viruses.

### Water storage size integrity
Do not let a product heading and destination disagree. The September 2026 audit found the `Reliance Aqua-Tainer 7 gallon` recommendation pointing to a 4-gallon URL. The bad link was removed and a same-capacity fallback added.

### LivSolv-owned etrailer generator
LivSolv owns etrailer generator #333-0005. Published output is 4,500W starting / 3,600W running on gasoline and 4,050W starting / 3,250W running on propane. It is not an inverter generator. etrailer warns against plugging sensitive electronics such as computers or televisions directly into it. Keep that distinction prominent.

### LivSolv-owned solar flashlight
LivSolv owns and uses an unbranded flashlight with integrated solar panel, USB input/output, main beam and COB side light. It is kept in a sunny window and has remained ready in household use. Never attach unsupported battery/recharge/manufacturer specs.

### LivSolv-owned Goal Zero Yeti 150
LivSolv owns and has used a Goal Zero Yeti 150. It is discontinued. Use it as firsthand evidence for battery-plus-separate-solar architecture, not as a shopping recommendation.

### Sold-out products are not recommendations
A technically good product is not a useful commerce recommendation if the reader cannot buy it. EcoFlow RIVER 3 was removed from the primary compact-power shortlist on 2026-09-08 after current EcoFlow US pages showed the standalone unit sold out/preorder. Reconsider it only after a later availability audit.

## Next audit queue
1. solar-recharging-power-station.html
2. home-power-outage-essentials.html
3. remaining product-bearing pages not yet represented in this registry

## Future automation boundary
Safe automated checks may validate internal links and ordinary non-Amazon external URLs for HTTP failures. They must not be treated as proof of inventory, because sold-out pages commonly return HTTP 200. Amazon availability/price should not be scraped. Product availability requires a separate commerce audit using permitted public/manufacturer information or approved Amazon tooling when available.
