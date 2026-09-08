# LivSolv Commerce Link Health Registry

Last audit: 2026-09-08

## Rules
- Verify exact product and current manufacturer/retailer page before recommending it.
- Never invent an Amazon ASIN. Add a Special Link only after exact model/ASIN verification.
- Put a clear disclosure near Amazon recommendations and retain `/affiliate-disclosure.html`.
- Do not hard-code volatile Amazon prices or availability.
- Prefer current models with stable distribution and legitimate fallbacks.
- HTTP 200 does not prove inventory. Do not scrape Amazon stock or price.
- Firsthand labels require actual ownership/use. Discontinued owned products are examples, not current shopping recommendations.

## LivSolv evidence standard
Preparedness guidance must not be built from government checklists alone. Triangulate across the layers that apply:
1. Safety-critical authoritative guidance for hard boundaries such as carbon monoxide, food temperature, contaminated water, heat illness, fire and radio law.
2. Manufacturer documentation for specifications, compatibility and limitations.
3. Independent preparedness specialists and technically serious prepper resources.
4. Firsthand reports from people who lived through outages and disasters, including Reddit/preparedness communities.
5. LivSolv firsthand ownership/use and field experience where it genuinely exists.

Community anecdotes identify practical failure modes and overlooked needs. They do not automatically prove a practice safe. When community practice conflicts with a strong life-safety boundary, explain the conflict.

Recurring real-world themes: fuel becomes limiting; cell service can degrade; electric wells stop with power; refrigeration outranks convenience loads; ice and fuel may sell out; solar output is weather-dependent; grid-tied solar may not function during an outage without backup capability; small efficient comfort zones can beat whole-house loads; paper communication plans survive dead networks; layered systems outperform dependence on one generator, battery or charging method; drills reveal failures before emergencies.

## Audited recommendations
| Page | Product | Status | Action |
|---|---|---|---|
| fridge-freezer-backup-power.html | EcoFlow DELTA 3 Plus | Exact Amazon product verified + manufacturer fallback | Retain tagged Amazon link and fallback |
| fridge-freezer-backup-power.html | Jackery Explorer 2000 v2 | Exact Amazon product verified + manufacturer fallback | Retain tagged Amazon link and fallback |
| fridge-freezer-backup-power.html | BLUETTI AC200L | Manufacturer only | Do not add Amazon until exact ASIN verified |
| 72-hour-backup-power.html | Jackery Explorer 2000 v2 / EcoFlow DELTA 3 Plus | Exact Amazon products verified | Tagged links + manufacturer fallbacks |
| solar-recharging-power-station.html | EcoFlow DELTA 3 Plus | Exact Amazon ASIN B0DCC2BVFW verified | Tagged Amazon + manufacturer fallback added 2026-09-08 |
| solar-recharging-power-station.html | Jackery Explorer 2000 v2 | Exact Amazon ASIN B0DFG2WDQH verified | Tagged Amazon + manufacturer fallback added 2026-09-08 |
| solar-recharging-power-station.html | BLUETTI AC200L | Manufacturer only | Exact Amazon ASIN still withheld |
| cooking-during-power-outage.html | GoSun Sport | Sold out | Do not recommend as primary; use Sport-E |
| cooking-during-power-outage.html | GoSun Sport-E / Go / Fusion | Current manufacturer products at audit | Choose by size/capability |
| emergency-communications.html | Midland ER310 / ER310PRO family | Current lineup audited | Prefer current ER310PRO where available; ER310 fallback |
| emergency-water-treatment.html | Sawyer Squeeze | Current manufacturer product | Manufacturer link until exact Amazon ASIN verified |
| emergency-water-treatment.html | LifeStraw Peak Gravity Purifier | Current | Never confuse with non-virus-removing 8L Gravity Filter |
| emergency-water-treatment.html | GRAYL GeoPress 24 oz | Current collection | Collection link; cartridge inventory separate |
| emergency-water-storage.html | Reliance Aqua-Tainer 7 gal | Corrected prior size mismatch | Jumbo-Tainer 7 gal fallback |
| emergency-water-storage.html | WaterBrick 3.5 gal / waterBOB | Current at audit | Retain current shop/product paths |
| generator-backup-power.html | etrailer #333-0005 dual-fuel generator | LivSolv-owned + current exact retailer product | Keep non-inverter warning prominent |
| car-emergency-kit.html | NOCO GB40 / Slime #40088 / DEWALT DCC020IB | Current manufacturer products | Retain practical non-battery fallbacks where relevant |
| car-emergency-kit.html | Unbranded solar + USB flashlight | LivSolv-owned; manufacturer unknown | Recommend feature architecture only |
| small-backup-power.html | Goal Zero Yeti 150 | LivSolv-owned; discontinued | Example only |
| small-backup-power.html | Anker C300 / Jackery 300 Plus / EcoFlow RIVER 3 | Removed from current shortlist | Do not restore until clean availability audit |
| small-backup-power.html | Goal Zero Yeti 300 | Current manufacturer product at audit | Current replacement class for owned Yeti 150 |
| solar-power-bank-vs-folding-panel.html | Sherpa 100PD / Nomad 20 | Current at audit | Retain current Goal Zero path |

## Completed non-commerce research passes
- `storm-emergency-grocery-list.html`: broadened beyond storms; added outage-derived ice, fuel, well-water, thermometer and cold-storage lessons.
- `home-emergency-communication-plan.html`: added real-outage cell/network failure, paper plan, rendezvous, testing and layered communications.
- `home-first-aid-emergency-kit.html`: already incorporates prepper organization/training lessons while keeping medical authority boundaries.
- `fridge-freezer-backup-power.html`: added real-outage prioritization and system-testing lessons.
- `72-hour-backup-power.html`: added layered power and real-load testing lessons.
- `solar-recharging-power-station.html`: added real-outage solar limitations, grid-tied solar caveat, layered recharge architecture, drill recommendation and LivSolv Yeti 150 experience.

## Critical distinctions
- LifeStraw Peak Gravity Purifier and Peak Gravity Filter 8L are not interchangeable; virus-removal claims differ.
- Product heading and destination size/model must match exactly.
- LivSolv-owned etrailer #333-0005 is not an inverter generator; do not route sensitive electronics directly to it.
- LivSolv's unbranded solar flashlight supports only observed ownership/use claims, not guessed battery/lumen/IP specs.
- Goal Zero Yeti 150 is firsthand but discontinued.
- A technically good sold-out product is not a useful recommendation.

## Next audit queue
1. home-power-outage-essentials.html
2. extreme-heat-cold-power-outage.html product/supporting-equipment pass
3. remaining product-bearing pages not yet represented here

## Future automation boundary
Automated checks may validate internal and ordinary non-Amazon external URLs for HTTP failure, but not inventory. Amazon availability/price should not be scraped. Product availability needs a separate commerce audit using permitted public/manufacturer information or approved Amazon tooling.