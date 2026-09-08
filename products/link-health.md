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
| fridge-freezer-backup-power.html | EcoFlow DELTA 3 Plus | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| fridge-freezer-backup-power.html | Jackery Explorer 2000 v2 | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| fridge-freezer-backup-power.html | BLUETTI AC200L | Manufacturer only | Amazon ASIN not verified with sufficient confidence | Do not add Amazon link until exact ASIN is verified |
| 72-hour-backup-power.html | Jackery Explorer 2000 v2 | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| 72-hour-backup-power.html | EcoFlow DELTA 3 Plus | Amazon affiliate + manufacturer fallback | Verified exact Amazon product before affiliate conversion | Manufacturer fallback retained |
| cooking-during-power-outage.html | GoSun Sport | Do not recommend as primary | Sold out at audit | Recommend current Sport-E instead |
| cooking-during-power-outage.html | GoSun Sport-E / Go / Fusion | Manufacturer | Available at audit | Choose size/capability appropriate to household |
| emergency-communications.html | Midland ER310 / ER310PRO family | Manufacturer/current lineup | Audited 2026-09-08 | Prefer current ER310PRO where available; ER310 remains fallback |
| emergency-water-treatment.html | Sawyer Squeeze | Manufacturer | Available/current at audit | Keep manufacturer link until exact Amazon ASIN is verified |
| emergency-water-treatment.html | LifeStraw Peak Series Gravity Purifier | Manufacturer | Available/current at audit | Never substitute standard 8L Gravity Filter while preserving virus-removal claim |
| emergency-water-treatment.html | GRAYL GeoPress 24 oz Purifier | Manufacturer collection | Nature and Covert variants available 2026-09-08 | Collection link used; cartridge inventory tracked separately |
| emergency-water-storage.html | Reliance Aqua-Tainer 7 gallon | Current retailer distribution | Audited 2026-09-08; prior LivSolv URL incorrectly pointed to 4-gallon model | Corrected to exact 7-gallon retail listing; Reliance Jumbo-Tainer 7 gallon added as same-capacity fallback |
| emergency-water-storage.html | Reliance Jumbo-Tainer 7 gallon | Current retailer product | Available at audit | Fallback if Aqua-Tainer 7 gallon unavailable |
| emergency-water-storage.html | WaterBrick 3.5 gallon | Manufacturer live shop | Current packs available at audit | Live WaterBrick shop used because colors/pack sizes change |
| emergency-water-storage.html | waterBOB | Manufacturer exact product | In stock at audit | Exact current product retained; one-time-use limitation stated |
| car-emergency-kit.html | NOCO Boost GB40 | Manufacturer | Current recommendation retained | Jumper cables provide battery-free fallback architecture |
| car-emergency-kit.html | Slime 12V Digital Tire Inflator #40088 | Manufacturer | Current product page/specs audited | 12V vehicle power avoids separate inflator battery maintenance |
| car-emergency-kit.html | DEWALT DCC020IB | Manufacturer | Current official product page verified | 12V DC input provides alternate path even without a charged DEWALT battery |
| car-emergency-kit.html | Unbranded solar + USB flashlight | Firsthand LivSolv use; no commerce link | Owned and used; exact manufacturer/model unknown | Recommend feature architecture only; never invent specs |
| small-backup-power.html | Goal Zero Yeti 150 | Firsthand LivSolv use; archived/discontinued | Goal Zero archive verified 2026-09-08 | Firsthand example only, never current purchase recommendation |
| solar-power-bank-vs-folding-panel.html | Goal Zero Yeti 150 | Firsthand LivSolv use; archived/discontinued | Goal Zero archive confirms 168Wh AGM and solar compatibility | Route shoppers to current equipment rather than old stock |
| solar-power-bank-vs-folding-panel.html | Goal Zero Sherpa 100PD | Current manufacturer product | Current page verified 2026-09-08 | Use current Goal Zero lineup if model changes |
| solar-power-bank-vs-folding-panel.html | Goal Zero Nomad 20 | Current manufacturer product | Current page verified 2026-09-08 | Pair only with compatible current battery/input architecture |

## Important product distinctions discovered during audit

### LifeStraw Peak Series
The `Peak Series Gravity Purifier with virus removal` and `Peak Series Gravity Filter System - 8L` are not interchangeable recommendations. The purifier is specified for viruses, bacteria and parasites. The standard 8L gravity filter is specified for bacteria and parasites but not viruses.

### Water storage size integrity
Do not let a product heading and destination disagree. The September 2026 audit found the `Reliance Aqua-Tainer 7 gallon` recommendation pointing to a 4-gallon manufacturer URL. The bad link was removed. The exact 7-gallon Aqua-Tainer remains in current retail distribution, while the Reliance Jumbo-Tainer provides a current same-capacity fallback.

### LivSolv-owned solar flashlight
LivSolv owns and uses an unbranded flashlight with integrated solar panel, USB input, USB output, main beam and COB side light. It is kept in a sunny window and has remained ready in household use. Because there is no identifiable brand/model, never attach unsupported battery capacity, recharge-time or manufacturer claims.

### LivSolv-owned Goal Zero Yeti 150
LivSolv owns and has used a Goal Zero Yeti 150 as a small solar-rechargeable power station. Goal Zero now lists the model as no longer available. Use it as firsthand evidence for battery-plus-separate-solar architecture, not as a shopping recommendation.

## Next audit queue

1. generator-backup-power.html
2. small-backup-power.html
3. solar-recharging-power-station.html
4. home-power-outage-essentials.html
5. remaining product-bearing pages not yet represented in this registry

## Future automation boundary

Safe automated checks may validate internal links and ordinary non-Amazon external URLs for HTTP failures. They must not be treated as proof of inventory, because sold-out pages commonly return HTTP 200. Amazon availability/price should not be scraped. Product availability requires a separate commerce audit using permitted public/manufacturer information or approved Amazon tooling when available.
