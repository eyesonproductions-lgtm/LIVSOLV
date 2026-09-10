# LivSolv Commerce Link Health Registry

Last audit: 2026-09-10

## Rules
- Verify exact product and current manufacturer/retailer page before recommending it.
- Never invent an Amazon ASIN. Add a Special Link only after exact model/ASIN verification.
- Put a clear disclosure near Amazon recommendations and retain `/affiliate-disclosure.html`.
- Do not hard-code volatile Amazon prices or availability.
- Prefer current models with stable distribution and legitimate fallbacks.
- HTTP 200 does not prove inventory. Do not scrape Amazon stock or price.
- Firsthand labels require actual ownership/use. Discontinued owned products are examples, not current shopping recommendations.
- Never send LivSolv readers to Home Depot.

## LivSolv evidence standard
Preparedness guidance must not be built from government checklists alone. Triangulate across the layers that apply:
1. Safety-critical authoritative guidance for hard boundaries such as carbon monoxide, food temperature, contaminated water, heat illness, fire and radio law.
2. Manufacturer documentation for specifications, compatibility and limitations.
3. Independent preparedness specialists and technically serious preparedness resources.
4. Firsthand reports from people who lived through outages and disasters, including Reddit/preparedness communities.
5. LivSolv firsthand ownership/use and field experience where it genuinely exists.

Community anecdotes identify practical failure modes and overlooked needs. They do not automatically prove a practice safe. When community practice conflicts with a strong life-safety boundary, explain the conflict.

## Current audited recommendations
| Page | Product | Status / action |
|---|---|---|
| fridge-freezer-backup-power.html | EcoFlow DELTA 3 Plus | Exact product verified; retain tagged Amazon link and manufacturer fallback |
| fridge-freezer-backup-power.html | Jackery Explorer 2000 v2 | Exact product verified; retain tagged Amazon link and manufacturer fallback |
| fridge-freezer-backup-power.html | BLUETTI AC200L | Manufacturer link; verify exact Amazon ASIN before adding |
| solar-recharging-power-station.html | EcoFlow DELTA 3 Plus | Exact ASIN B0DCC2BVFW previously verified; tagged Amazon + manufacturer fallback |
| solar-recharging-power-station.html | Jackery Explorer 2000 v2 | Exact ASIN B0DFG2WDQH previously verified; tagged Amazon + manufacturer fallback |
| solar-recharging-power-station.html | BLUETTI AC200L | Manufacturer link; exact Amazon ASIN still withheld |
| cooking-during-power-outage.html | GoSun Sport-E / Go / Fusion | Manufacturer products; choose by size/capability |
| emergency-communications.html | Midland ER310 / ER310PRO family | Current lineup audited; prefer ER310PRO where available |
| emergency-water-treatment.html | Sawyer Squeeze | Current product; exact Amazon link requires verification |
| emergency-water-treatment.html | LifeStraw Peak Gravity Purifier | Do not confuse with non-virus-removing Peak Gravity Filter |
| emergency-water-treatment.html | GRAYL GeoPress 24 oz | Current product family; cartridge inventory separate |
| emergency-water-storage.html | Reliance Aqua-Tainer 7 gal | Current storage recommendation |
| emergency-water-storage.html | WaterBrick 3.5 gal / waterBOB | Current storage recommendations |
| generator-backup-power.html | etrailer #333-0005 dual-fuel generator | LivSolv-owned + exact retailer product; keep non-inverter warning prominent |
| car-emergency-kit.html | NOCO GB40 | Current established pick; add a lower-cost secondary after current availability research |
| car-emergency-kit.html | Fanttik X8 APEX | Current separate tire-inflator recommendation |
| small-backup-power.html | Goal Zero Yeti 150 | LivSolv-owned but discontinued; example only |
| solar-power-bank-vs-folding-panel.html | Portable USB-C battery + folding solar panel | Exact product/link pass still needed |

## Critical distinctions
- LifeStraw Peak Gravity Purifier and Peak Gravity Filter 8L are not interchangeable; virus-removal claims differ.
- Product heading and destination size/model must match exactly.
- LivSolv-owned etrailer #333-0005 is not an inverter generator; do not route sensitive electronics directly to it.
- LivSolv's unbranded solar flashlight supports only observed ownership/use claims, not guessed battery/lumen/IP specs.
- Goal Zero Yeti 150 is firsthand but discontinued.
- A technically good sold-out or nearly unavailable product is not a useful primary recommendation.

## Site housekeeping completed 2026-09-10
- Deleted `72-hour-backup-power.html` is no longer part of the current architecture and must not be restored or linked.
- Sitemap refreshed to remove the deleted page and include current public guides.
- `cool-emergency-gadgets.html` is canonical; obsolete `coolest-emergency-gadgets.html` redirects to it.
- Dakota fire-hole and primitive rocket-stove guides are live supporting pages for blackout cooking.

## Next commerce audit queue
1. car-emergency-kit.html: secondary lower-cost jump starter with healthy availability
2. exact Amazon/affiliate-link verification across product-bearing pages
3. product availability and manufacturer fallback review
4. site-wide affiliate disclosure consistency

## Future automation boundary
Automated checks may validate internal and ordinary non-Amazon external URLs for HTTP failure, but not inventory. Amazon availability/price should not be scraped. Product availability needs a separate commerce audit using permitted public/manufacturer information or approved Amazon tooling.