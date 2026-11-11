#!/usr/bin/env python3
"""Build the Consolidated Engineers rebuild."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://cedefense.com"
BRAND = "Consolidated Engineers"
PHONE = "+92 42 3576 4907-08"
PHONE_ALT = "+92 42 3576 1247"
EMAIL = "info@cedefense.com"
ADDRESS = "CE House, 108 E-1, Gulberg III, Lahore, Pakistan"

CAPABILITIES = [
    {
        "num": "01",
        "id": "ground-support",
        "title": "Ground support equipment",
        "summary": "Aircraft towing tractors, runway repair units and purpose-built airfield machines, specified around the aircraft and the apron.",
        "image": "tow-tractor.jpg",
        "label": "Ground support",
    },
    {
        "num": "02",
        "id": "cranes",
        "title": "Cranes and lifting",
        "summary": "Industrial, tower, truck-mounted and luffing cranes, sized against the load chart and the ground the machine will stand on.",
        "image": "crane-yellow.jpg",
        "label": "Cranes and lifting",
    },
    {
        "num": "03",
        "id": "access",
        "title": "Access platforms",
        "summary": "Vehicle-mounted elevating platforms for overhead maintenance, lighting, signage and infrastructure inspection.",
        "image": "aerial-lift.jpg",
        "label": "Access platforms",
    },
    {
        "num": "04",
        "id": "mining",
        "title": "Mining machinery",
        "summary": "Loaders, drilling units and support equipment for quarrying and mineral extraction, with a documented spares path.",
        "image": "mining-loader.jpg",
        "label": "Mining machinery",
    },
    {
        "num": "05",
        "id": "construction",
        "title": "Road and construction",
        "summary": "Earthmoving, compaction and site equipment for infrastructure programmes, supplied with commissioning and training.",
        "image": "crane-factory.jpg",
        "label": "Road and construction",
    },
    {
        "num": "06",
        "id": "lighting",
        "title": "Flood lighting",
        "summary": "Mobile and fixed lighting for airfields, yards, ports and remote works where the shift does not stop at dusk.",
        "image": "crane-dusk.jpg",
        "label": "Flood lighting",
    },
    {
        "num": "07",
        "id": "aviation-tyres",
        "title": "Aviation tyres",
        "summary": "Genuine Goodyear aircraft tyres and tubes, supplied to the correct part number with traceability documentation.",
        "image": "aviation-tyres.jpg",
        "label": "Aviation tyres",
    },
    {
        "num": "08",
        "id": "parts",
        "title": "Parts and spares",
        "summary": "OEM parts, electronic components and consumables for the equipment we supply, including discontinued models.",
        "image": "parts-electronics.jpg",
        "label": "Parts and spares",
    },
]

SECTORS = [
    {
        "num": "01",
        "title": "Civilian government",
        "summary": "Federal and provincial departments requiring indexed products, transparent documentation and delivery against a published procurement timetable.",
        "image": "crane-city.jpg",
        "points": ["Product indexing", "Tender response", "Delivery scheduling", "Commissioning"],
    },
    {
        "num": "02",
        "title": "Defence and military",
        "summary": "Registered supply under the Directorate General Defence Purchase since 1985, including demonstration, user acceptance and post-delivery support.",
        "image": "tow-tractor.jpg",
        "points": ["DGDP registration", "Demonstration", "Import compliance", "Technical support"],
    },
    {
        "num": "03",
        "title": "Private industry",
        "summary": "Commercial enterprises that need the same equipment, the same documentation and direct access to the manufacturer.",
        "image": "crane-pair.jpg",
        "points": ["Specification", "Delivery position", "Installation", "Spares and service"],
    },
]

PROJECTS = [
    {
        "title": "Tower crane package",
        "sector": "Cranes and lifting",
        "place": "Lahore",
        "image": "crane-tower.jpg",
        "summary": "Two hammer-head cranes specified against the load chart, the site radius and the erection sequence, with climbing and dismantling included in the scope.",
    },
    {
        "title": "Airfield ground support",
        "sector": "Ground support",
        "place": "Punjab",
        "image": "tow-tractor.jpg",
        "summary": "Tow tractors configured for narrow-body and wide-body clearances, delivered with operator training and a documented spares path.",
    },
    {
        "title": "Underground loader fleet",
        "sector": "Mining",
        "place": "Khyber Pakhtunkhwa",
        "image": "mining-loader.jpg",
        "summary": "Compact load and haul units for narrow headings, supplied with first-line maintenance training and a parts schedule.",
    },
    {
        "title": "Aviation tyre programme",
        "sector": "Aviation",
        "place": "National",
        "image": "aviation-tyres.jpg",
        "summary": "Aircraft tyres and tubes supplied by part number, with traceability documents and a storage and rotation routine for the operator.",
    },
    {
        "title": "Aerial lift fleet",
        "sector": "Access platforms",
        "place": "Sindh",
        "image": "aerial-fleet.jpg",
        "summary": "Vehicle-mounted platforms for municipal lighting and overhead maintenance, with commissioning and a training handover.",
    },
    {
        "title": "Factory lifting system",
        "sector": "Industrial",
        "place": "Punjab",
        "image": "crane-green.jpg",
        "summary": "An industrial crane package for a process plant, sized for continuous duty and integrated with the existing production layout.",
    },
]

ARTICLES = [
    {
        "slug": "crane-specification",
        "category": "Cranes and lifting",
        "title": "What a crane specification should actually say",
        "dek": "Load charts, radii and ground bearing are where most crane briefs fail. A practical guide to writing a specification that can be priced, erected and delivered.",
        "date": "10 November 2026",
        "read": "8 min read",
        "image": "crane-tower.jpg",
        "alt": "Tower cranes standing over a construction site",
        "body": """
<p>A crane enquiry that begins with a capacity in tonnes is not yet a specification. It is a wish. The capacity is the answer to a set of conditions that have to be written down first: what is being lifted, how far from the centre of the crane, how high, how often, and what the machine will stand on.</p>
<p>When those conditions are missing, every supplier prices a different crane. The quotations look comparable because they share a headline number. They are not comparable at all.</p>
<h2>Start with the lift, not the machine</h2>
<p>Write down the load, including the rigging, the spreader and anything that hangs from the hook. Then write the radius at which the load must be placed, not the radius at which the crane will sit. A load chart is a map of capacity against radius and height, and the useful figure is always the one at the working radius.</p>
<p>Do the same for the height. The hook height is not the same as the building height. Add the clearance above the load, the sling length and any obstruction between the hook and the landing point.</p>
<h2>The four numbers that decide the machine</h2>
<ul>
<li><strong>Load:</strong> the gross load at the hook, not the net weight on the drawing.</li>
<li><strong>Radius:</strong> the distance from the slewing centre to the load, at the worst position in the lift.</li>
<li><strong>Height:</strong> hook height plus clearance, under the boom or jib configuration you will actually use.</li>
<li><strong>Duty:</strong> how many lifts, how often, and whether the crane works continuously or intermittently.</li>
</ul>
<p>Those four numbers eliminate most of the catalogue. What remains is a short list of machines that can do the job, and a much more useful conversation about erection, foundations and site access.</p>
<blockquote>A crane quotation without a load chart is a price for a photograph, not for a machine on your site.</blockquote>
<h2>Ground bearing is part of the specification</h2>
<p>The crane does not stand on the drawing. It stands on a slab, a road, a pile mat or made ground. The outrigger or track pressure has to be checked against what is actually there, and the temporary works to spread that load have to be in somebody's scope.</p>
<p>This is the most common gap in a brief. The crane is specified, the foundation is assumed, and the first week on site is spent discovering that the ground will not take the pressure. Ask for the maximum outrigger load and the bearing pressure at the worst configuration, then confirm who is responsible for the mat or the slab.</p>
<h2>Erection, climbing and dismantling</h2>
<p>A tower crane is not delivered. It is erected, climbed and eventually dismantled, and each of those operations needs space, a mobile crane and a competent crew. On a dense urban site, the erection plan can decide the crane as much as the load chart does.</p>
<p>Put the sequence in the brief: the position of the crane, the mobile crane needed to erect it, the climbing stages, the tie-in levels and the dismantling route. If the site cannot support the sequence, the crane is wrong even if the chart says it is right.</p>
<h2>What to put in the brief</h2>
<ul>
<li>The lift plan, including the worst case rather than the typical case.</li>
<li>Load, radius and height at that worst case.</li>
<li>Ground conditions and the temporary works assumption.</li>
<li>Erection, climbing and dismantling constraints.</li>
<li>Site access, delivery route and lay-down space.</li>
<li>Operator training, commissioning and handover requirements.</li>
<li>The documentation you expect at the end: load charts, certificates, inspection records and the manual.</li>
</ul>
<p>A specification written this way is longer than a capacity figure, but it is the difference between a quotation you can compare and a delivery you can hold someone to.</p>
<h2>The test of a good specification</h2>
<p>Give the brief to two suppliers and ask each to return the load chart for the proposed configuration. If the charts show the same working radius, the same hook height and the same ground pressure, you are comparing like with like. If they do not, the conversation is not about price yet.</p>
<p>The equipment is the easy part. The conditions around it are the work.</p>
""",
    },
    {
        "slug": "commissioning",
        "category": "After-sales",
        "title": "The hidden cost of a late commissioning",
        "dek": "A machine that arrives without commissioning, training or a signed handover is not an asset yet. It is a claim waiting to happen.",
        "date": "5 November 2026",
        "read": "7 min read",
        "image": "tow-tractor.jpg",
        "alt": "Yellow airport tow tractor parked outside a building",
        "body": """
<p>Procurement teams measure the success of a capital purchase at the point of delivery. Operations teams measure it at the point the equipment starts earning. Between those two points sits commissioning, and it is where schedules quietly disappear.</p>
<p>A tow tractor that arrives on the apron is not in service. It needs a pre-delivery inspection, a commissioning run, operator familiarisation, a handover record and a spares path. Each of those is a small task. Together they decide whether the machine is available next month.</p>
<h2>Delivery is not handover</h2>
<p>The delivery note proves the crate arrived. The handover record proves the equipment works to specification, the operator has been trained and the site has accepted the unit. Those are different documents, and only the second one protects the buyer.</p>
<p>A useful handover record includes the serial number, the configuration, the commissioning results, the name of the person who accepted the unit and the date. It also includes the outstanding items, because there are always outstanding items.</p>
<blockquote>An unsigned handover is an open-ended warranty discussion.</blockquote>
<h2>The training gap</h2>
<p>Operator training is often treated as an optional extra. It is not. A machine used outside its rated capacity, or maintained without the correct procedure, will fail earlier and cost more. The training is part of the specification, not a favour after the invoice.</p>
<p>Ask for training on the actual unit, at the actual site, with the people who will run it. A generic session in a classroom is better than nothing, but it does not cover the apron layout, the blind spots or the local operating rules.</p>
<h2>Commissioning is a schedule item</h2>
<p>Commissioning needs time on the project programme, not a slot after the handover meeting. The site needs power, access and a competent person available. The manufacturer may need a specialist. The operator may need to be released from shift.</p>
<p>If those dependencies are not in the programme, commissioning slips. The equipment sits idle, the project claims delay, and the supplier and the buyer spend the next month exchanging letters about whose fault it is.</p>
<h2>The spares path</h2>
<p>Commissioning is also the moment to confirm the spares path. Which parts are consumables, which are critical, what is held locally and what has to be imported. A machine that stops for a filter is as unavailable as one that stops for a gearbox.</p>
<p>Ask for the recommended spares list at handover, not after the first failure. Ask how discontinued models are supported. Ask who owns the part number and how long the lead time is. These are simple questions with expensive answers when they are asked late.</p>
<h2>What good looks like</h2>
<ul>
<li>Commissioning is in the contract and the programme, with named responsibilities.</li>
<li>The handover record is signed by the person who will operate the equipment.</li>
<li>Training happens on the unit, on site, before acceptance.</li>
<li>The spares list and the first-line maintenance schedule are handed over with the manual.</li>
<li>The supplier remains the named contact for the life of the machine.</li>
</ul>
<p>The cheapest commissioning is the one that is planned. The most expensive is the one that is discovered.</p>
""",
    },
    {
        "slug": "aviation-tyres",
        "category": "Aviation",
        "title": "Buying aviation tyres without a part number",
        "dek": "A tyre is not a commodity. Part numbers, traceability and storage decide whether the right unit reaches the aircraft.",
        "date": "29 October 2026",
        "read": "6 min read",
        "image": "aviation-tyres.jpg",
        "alt": "Genuine Goodyear aircraft tyres stacked in a warehouse",
        "body": """
<p>An aircraft tyre looks simple from the outside. It is a highly controlled part, and the control starts with the part number. Buy the wrong number and the tyre may fit the wheel but not the approved configuration. Buy without traceability and the maintenance organisation cannot sign it into service.</p>
<h2>The part number is the specification</h2>
<p>Aircraft tyres are identified by manufacturer part number, size, load rating and speed rating. The aircraft maintenance manual will name the approved tyre and, often, the approved wheel assembly. The part number is the link between the two.</p>
<p>A generic size is not enough. Two tyres can share a nominal size and differ in load rating, tread or construction. The approved configuration is the one in the manual, not the one that looks closest on the shelf.</p>
<blockquote>The cheapest tyre is the one that is approved, traceable and in the right condition when the aircraft needs it.</blockquote>
<h2>Traceability from manufacture to fit</h2>
<p>Aviation tyres carry a serial number and a manufacturing date. The maintenance organisation needs the documentation that connects the tyre to the approved source, the storage history and the fitment record.</p>
<p>Ask for the certificate or release document with the delivery. Keep the storage record. A tyre that has been stored badly, exposed to heat or ozone, or mounted and removed incorrectly is not the same as one that has been kept properly, even if the serial number is the same.</p>
<h2>Storage is part of the purchase</h2>
<p>Tyres are not inert. They age. Heat, sunlight, ozone and certain solvents accelerate that ageing. A store that is convenient but hot is a false economy.</p>
<p>Keep tyres clean, dry, out of direct sunlight and away from electric motors and solvents. Rotate stock so the oldest approved tyre is used first. Record the date of receipt and the date of fitment. Those records are what an audit will ask for.</p>
<h2>Retread and repair</h2>
<p>Retreading and repair are controlled processes. Not every tyre is eligible, and not every damage is repairable. The approved manual and the manufacturer's instructions decide. A repair that is not approved is a risk the maintenance organisation carries.</p>
<p>Ask the supplier what the approved repair and retread route is for the tyre you are buying, and whether the documentation will support it. The answer should be specific, not a general assurance.</p>
<h2>A practical buying checklist</h2>
<ul>
<li>The approved part number, taken from the aircraft manual.</li>
<li>The manufacturer and the release document.</li>
<li>The serial number and manufacturing date.</li>
<li>The storage history and the condition on receipt.</li>
<li>The approved fitment and removal procedure.</li>
<li>The repair and retread route, in writing.</li>
<li>The lead time for a repeat order, and the local stock position.</li>
</ul>
<p>None of this is exotic. It is the normal discipline of a controlled part. The failure mode is treating a tyre like a consumable from a catalogue, and discovering the gap at the aircraft rather than at the desk.</p>
""",
    },
    {
        "slug": "public-procurement",
        "category": "Public procurement",
        "title": "Why public procurement fails before the tender",
        "dek": "Most public equipment contracts are won or lost in the indexing and specification stage, long before the tender is published.",
        "date": "22 October 2026",
        "read": "8 min read",
        "image": "crane-city.jpg",
        "alt": "Tower crane beside a glass office building",
        "body": """
<p>Public procurement is often described as a tender process. In practice, the decisive work happens earlier: the product has to be indexed, the specification has to be written in a way the market can answer, and the budget has to survive the timetable. A tender is the visible part of a longer chain.</p>
<h2>Indexing is not paperwork</h2>
<p>In Pakistan, a new product may need to be indexed with the civilian departments and the Ministry of Defence before it can be introduced to a user unit. That is not a formality at the end of the process. It is the gate that decides whether the product can be demonstrated, procured and accepted.</p>
<p>A supplier who treats indexing as an administrative step discovers the problem when the user unit is ready and the product is not. The programme slips, and the slippage is rarely attributed to the missing index.</p>
<blockquote>A tender is a deadline. Indexing is the work that makes the deadline possible.</blockquote>
<h2>Specification drift</h2>
<p>Public specifications are written to be neutral, but neutrality is difficult. A specification that is too broad attracts offers that cannot be compared. One that is too narrow excludes the competition and may be challenged.</p>
<p>The useful middle ground is a specification written around performance and interface, with the mandatory standards named. What must the equipment do, in what conditions, with what documentation, and what must it connect to? Those questions produce a tender that can be evaluated.</p>
<h2>The documentation burden</h2>
<p>A public contract asks for more than a price. It asks for the registration, the tax position, the technical literature, the compliance statements, the delivery schedule, the warranty and the after-sales commitment. Each document has a format and a deadline.</p>
<p>A supplier who starts assembling the pack after the tender is published is already late. The pack should be a standing asset: current, indexed and ready to be adapted to the particular notice.</p>
<h2>The timetable is part of the specification</h2>
<p>Delivery dates in public procurement are often fixed before the supplier is chosen. The equipment may have an import lead time, a commissioning period and a training requirement. If those are not reflected in the timetable, the contract starts with an impossible date.</p>
<p>Ask for the realistic delivery position at the quotation stage, in writing. A supplier who promises an impossible date to win the tender is transferring the risk to the project, not removing it.</p>
<h2>What a good bid team does</h2>
<ul>
<li>Maintains the registrations and the standard document pack in date.</li>
<li>Indexes new products before they are offered to a user unit.</li>
<li>Writes the specification around performance, standards and interfaces.</li>
<li>States the delivery position and the dependencies honestly.</li>
<li>Plans demonstration, commissioning and training as part of the contract.</li>
<li>Keeps the after-sales record, because the next tender will ask for it.</li>
</ul>
<p>The tender is a test of preparation. The preparation is the procurement.</p>
""",
    },
    {
        "slug": "discontinued-support",
        "category": "After-sales",
        "title": "Discontinued is not abandoned",
        "dek": "Equipment bought decades ago is still in service. A supplier who disappears when the model is superseded leaves the user with a machine nobody will support.",
        "date": "15 October 2026",
        "read": "6 min read",
        "image": "mining-loader.jpg",
        "alt": "Underground mining loader working in a tunnel",
        "body": """
<p>Capital equipment has a long life. A crane, a tow tractor or a loader bought in the 1990s can still be doing useful work today. The manufacturer may have moved on to a new model, but the machine in the yard has not read the brochure.</p>
<p>This is the quiet test of a supplier. Anyone can sell the current model. The question is who answers the phone when the model is discontinued and the part is no longer in the catalogue.</p>
<h2>The lifecycle is longer than the sales cycle</h2>
<p>Sales teams are measured on the current range. Operators are measured on availability. The two clocks run at different speeds. A supplier that only supports what it currently sells is a supplier for the sales cycle, not the lifecycle.</p>
<p>The good outcome is a documented spares path that survives the model change: the part numbers, the alternate sources, the repair route and the person who owns the query.</p>
<blockquote>The end of a model is not the end of the obligation.</blockquote>
<h2>What to ask before you buy</h2>
<ul>
<li>Which parts are specific to this model and which are shared with the current range?</li>
<li>What is the manufacturer's stated support period after the model is discontinued?</li>
<li>Which parts are held locally, and which are imported on demand?</li>
<li>What is the typical lead time for a critical part?</li>
<li>Who is the named contact for a spares query in year ten?</li>
</ul>
<p>These questions are easier to ask before the order than after the failure. A supplier who cannot answer them is telling you something useful.</p>
<h2>The repair route</h2>
<p>Some parts can be repaired to the manufacturer's standard. Some cannot. The difference matters, because an unofficial repair can introduce a failure that the maintenance record will not show.</p>
<p>Ask for the approved repair route and the documentation that comes with it. If a part is no longer available, ask whether an approved alternative exists and who signs it off. The answer should be in writing, with a part number and a traceability document.</p>
<h2>Planning for obsolescence</h2>
<p>Obsolescence is not a surprise. It is a schedule. A fleet manager can plan for it by recording the critical parts, the lead times and the age of each unit, and by reviewing the list before the next failure.</p>
<p>The review does not need to be complicated. A spreadsheet with the unit, the critical part, the current source and the lead time is enough to start. The point is to know where the risk sits before it becomes an outage.</p>
<h2>The supplier's side</h2>
<p>For the supplier, supporting discontinued equipment is a discipline. It means keeping the old part numbers, the drawings and the contacts, and being willing to spend time on a low-value order because the machine matters to the user.</p>
<p>That is the business we are in. The equipment is the beginning of the relationship, not the end of it.</p>
""",
    },
]

for index, article in enumerate(ARTICLES):
    article["index"] = index


def canonical(slug):
    return BASE + "/" + slug


def head(title, description, slug, prefix="", extra=""):
    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": BRAND,
        "url": BASE,
        "email": EMAIL,
        "telephone": PHONE_ALT,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "CE House, 108 E-1, Gulberg III",
            "addressLocality": "Lahore",
            "addressCountry": "PK",
        },
        "foundingDate": "1969",
    }
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical(slug)}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#111416">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{prefix}assets/css/site.css">
{extra}<script type="application/ld+json">{json.dumps(schema, separators=(",", ":"))}</script>
</head>
<body>'''


def header(prefix, active):
    def current(name):
        return ' aria-current="page"' if active == name else ""

    return f'''<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar">
  <div class="wrap topbar-inner">
    <div class="topbar-group">
      <span>CE House, Gulberg III, Lahore</span>
      <span>Est. 1969</span>
    </div>
    <div class="topbar-group">
      <a href="tel:+924235764907">+92 42 3576 4907-08</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <span class="status">DGDP registered</span>
    </div>
  </div>
</div>

<header class="site-header" data-header>
  <div class="wrap header-inner">
    <a class="brand" href="{prefix}index.html" aria-label="Consolidated Engineers home">
      <span class="brand-mark" aria-hidden="true">CE</span>
      <span class="brand-text">
        <span class="brand-name">Consolidated Engineers</span>
        <span class="brand-sub">Defence · Aviation · Industry</span>
      </span>
    </a>
    <nav class="nav" data-nav aria-label="Main">
      <a href="{prefix}about.html"{current("about")}>About</a>
      <a href="{prefix}products.html"{current("products")}>Products</a>
      <a href="{prefix}services.html"{current("services")}>Services</a>
      <a href="{prefix}sectors.html"{current("sectors")}>Sectors</a>
      <a href="{prefix}projects.html"{current("projects")}>Projects</a>
      <a href="{prefix}insights.html"{current("insights")}>Insights</a>
      <a href="{prefix}contact.html"{current("contact")}>Contact</a>
    </nav>
    <div class="header-actions">
      <a class="btn" href="{prefix}contact.html">Request a quotation</a>
      <button class="menu-toggle" type="button" data-menu-toggle aria-label="Menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>'''


def footer(prefix):
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="brand" href="{prefix}index.html" aria-label="Consolidated Engineers home">
          <span class="brand-mark" aria-hidden="true">CE</span>
          <span class="brand-text">
            <span class="brand-name">Consolidated Engineers</span>
            <span class="brand-sub">Defence · Aviation · Industry</span>
          </span>
        </a>
        <p>Equipment supply, installation and after-sales support for defence, aviation, government and industry in Pakistan since 1969.</p>
      </div>
      <div class="footer-col">
        <h2>Capabilities</h2>
        <ul>
          <li><a href="{prefix}products.html#ground-support">Ground support</a></li>
          <li><a href="{prefix}products.html#cranes">Cranes and lifting</a></li>
          <li><a href="{prefix}products.html#access">Access platforms</a></li>
          <li><a href="{prefix}products.html#mining">Mining machinery</a></li>
          <li><a href="{prefix}products.html#aviation-tyres">Aviation tyres</a></li>
          <li><a href="{prefix}products.html#parts">Parts and spares</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>Company</h2>
        <ul>
          <li><a href="{prefix}about.html">About the firm</a></li>
          <li><a href="{prefix}services.html">After-sales services</a></li>
          <li><a href="{prefix}sectors.html">Sectors</a></li>
          <li><a href="{prefix}projects.html">Representative scopes</a></li>
          <li><a href="{prefix}insights.html">Insights</a></li>
          <li><a href="{prefix}contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h2>Office</h2>
        <ul>
          <li>CE House, 108 E-1<br>Gulberg III, Lahore, Pakistan</li>
          <li><a href="tel:+924235761247">+92 42 3576 1247</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Monday to Saturday<br>09:00 to 18:00 PKT</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Consolidated Engineers. All rights reserved.</span>
      <span>DGDP registered · LCCI 2806-A · Financial Category A</span>
      <span>Demonstration rebuild</span>
    </div>
  </div>
</footer>
<script src="{prefix}assets/js/site.js"></script>
</body>
</html>'''


def page(title, description, slug, active, body, prefix="", extra=""):
    return head(title, description, slug, prefix, extra) + header(prefix, active) + body + footer(prefix)


def page_hero(eyebrow, title, lead, crumb="", prefix=""):
    crumb_html = ""
    if crumb:
        crumb_html = f'<div class="crumb"><a href="{prefix}index.html">Home</a><span>/</span><span>{crumb}</span></div>'
    return f'''<section class="page-hero">
  <div class="wrap">
    {crumb_html}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>'''


def ticker():
    items = [
        "Ground support",
        "Cranes and lifting",
        "Access platforms",
        "Mining machinery",
        "Aviation tyres",
        "Parts and spares",
        "DGDP registered since 1985",
        "Financial Category A",
    ]
    row = "".join(f"<span>{item}</span>" for item in items)
    return f'''<div class="ticker" aria-hidden="true">
  <div class="ticker-track">{row}{row}</div>
</div>'''


def capability_index():
    items = "\n".join(
        f'''<a class="cap-item{' is-active' if i == 0 else ''}" href="products.html#{cap["id"]}" data-cap data-img="assets/img/{cap["image"]}" data-label="{cap["label"]}" data-index="{cap["num"]}">
  <span class="cap-num">{cap["num"]}</span>
  <div>
    <h3>{cap["title"]}</h3>
    <p>{cap["summary"]}</p>
  </div>
  <span class="cap-arrow" aria-hidden="true">&#8594;</span>
</a>'''
        for i, cap in enumerate(CAPABILITIES)
    )
    first = CAPABILITIES[0]
    return f'''<div class="cap-grid">
  <div class="cap-list">
    {items}
  </div>
  <div class="cap-media">
    <img data-cap-image src="assets/img/{first["image"]}" alt="{first["label"]}" width="700" height="875">
    <div class="cap-media-caption"><span data-cap-label>{first["label"]}</span><span data-cap-index>{first["num"]}</span></div>
  </div>
</div>'''


def sector_cards():
    return "\n".join(
        f'''<article class="sector-card" data-reveal>
  <img src="assets/img/{sector["image"]}" alt="{sector["title"]}" width="700" height="875" loading="lazy">
  <span class="sector-num">Sector {sector["num"]}</span>
  <h3>{sector["title"]}</h3>
  <p>{sector["summary"]}</p>
  <ul>{''.join(f"<li>{point}</li>" for point in sector["points"])}</ul>
</article>'''
        for sector in SECTORS
    )


def project_cards(items=None, prefix="", link=True):
    items = items or PROJECTS
    open_tag = (
        f'<a class="project-card" href="{prefix}projects.html" data-reveal>'
        if link
        else '<article class="project-card" data-reveal>'
    )
    close_tag = "</a>" if link else "</article>"
    return "\n".join(
        f'''{open_tag}
  <div class="project-media"><img src="{prefix}assets/img/{project["image"]}" alt="{project["title"]}" width="800" height="500" loading="lazy"></div>
  <div class="project-body">
    <div class="project-meta"><span>{project["sector"]}</span><span>{project["place"]}</span></div>
    <h3>{project["title"]}</h3>
    <p>{project["summary"]}</p>
  </div>
{close_tag}'''
        for project in items
    )


def insight_card(article, prefix=""):
    return f'''<a class="insight-card" href="{prefix}insights/{article["slug"]}.html" data-reveal>
  <div class="insight-media"><img src="{prefix}assets/img/{article["image"]}" alt="{article["alt"]}" width="800" height="500" loading="lazy"></div>
  <span class="insight-tag">{article["category"]}</span>
  <h3>{article["title"]}</h3>
  <p>{article["dek"]}</p>
  <div class="insight-meta">{article["date"]} · {article["read"]}</div>
</a>'''


def insight_grid(prefix=""):
    return "\n".join(insight_card(article, prefix) for article in ARTICLES[:4])


def build_home():
    body = f'''<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div data-reveal>
        <span class="eyebrow">Established 1969 · Lahore, Pakistan</span>
        <h1>The equipment is the <em>easy part.</em></h1>
        <p class="lead">Consolidated Engineers has supplied, installed and supported defence, aviation and government programmes for more than five decades. We carry the import, the documentation and the after-sales obligation, so the end user deals with a firm in Lahore rather than a supplier in another time zone.</p>
        <div class="hero-actions">
          <a class="btn btn-signal" href="products.html">Explore the range</a>
          <a class="btn btn-outline" href="contact.html">Send a requirement</a>
        </div>
        <div class="hero-meta">
          <div><strong>1969</strong><span>Established</span></div>
          <div><strong>1985</strong><span>DGDP registered</span></div>
          <div><strong>Cat A</strong><span>No contract limit</span></div>
          <div><strong>2806-A</strong><span>LCCI member</span></div>
        </div>
      </div>
      <figure class="hero-figure" data-reveal>
        <div class="hero-image">
          <img src="assets/img/hero-crane.jpg" alt="Tower crane against a clear sky on a construction site" width="700" height="430">
          <span class="corner tl"></span><span class="corner tr"></span><span class="corner bl"></span><span class="corner br"></span>
          <div class="hero-caption"><span>Fig. 01 / Tower crane</span><span>Lahore, PK</span></div>
        </div>
        <span class="vertical-note">Supplied · Installed · Supported</span>
      </figure>
    </div>
  </section>

  {ticker()}

  <section class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <span class="section-index">01 / Capabilities</span>
          <h2>Equipment selected for duty, not for a catalogue.</h2>
        </div>
        <p class="aside">Eight categories, each sourced from a manufacturer we represent directly. Where a model has been discontinued, we continue to support the units already in service.</p>
      </div>
      {capability_index()}
    </div>
  </section>

  <section class="section section-dark">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <span class="section-index">02 / Credentials</span>
          <h2>Registered, listed, accountable.</h2>
        </div>
        <p class="aside">The registrations are not decoration. They are the structure that lets a public buyer place a contract and a manufacturer appoint a local principal.</p>
      </div>
      <div class="cred-band">
        <div class="cred"><strong>1969</strong><span>Established in Lahore</span></div>
        <div class="cred"><strong>1972</strong><span>LCCI member 2806-A</span></div>
        <div class="cred"><strong>1985</strong><span>DGDP contractor</span></div>
        <div class="cred"><strong>A</strong><span>Financial Category, no limit</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <span class="section-index">03 / Sectors</span>
          <h2>Three sectors, one standard of delivery.</h2>
        </div>
        <p class="aside">Public procurement and private procurement fail for different reasons. We structure the response to the sector and keep the same accountability in both.</p>
      </div>
      <div class="sector-grid">
        {sector_cards()}
      </div>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <span class="section-index">04 / Representative scopes</span>
          <h2>The work behind a supply contract.</h2>
        </div>
        <p class="aside">Specification, import, indexing, demonstration, commissioning and training. These are representative scopes, not a logo wall.</p>
      </div>
      <div class="project-grid">
        {project_cards(PROJECTS[:4])}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <span class="section-index">05 / Insights</span>
          <h2>Notes from the procurement floor.</h2>
        </div>
        <p class="aside">Practical writing on specification, commissioning, spares and public procurement. Written for the people who have to make the equipment work.</p>
      </div>
      <div class="insight-grid">
        {insight_grid()}
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div>
        <h2>Tell us what the equipment has to do.</h2>
        <p>Send the application, the site conditions and any specification you already hold. We will respond with a sourced option, a delivery position and the support scope in writing.</p>
      </div>
      <a class="btn" href="contact.html">Start an enquiry</a>
    </div>
  </section>
</main>'''
    return page(
        "Consolidated Engineers | Defence, aviation and government equipment supply",
        "Consolidated Engineers has supplied, installed and supported defence, aviation and government programmes since 1969. DGDP registered, Financial Category A, Lahore.",
        "",
        "home",
        body,
    )


def build_about():
    body = f'''<main id="main">
  {page_hero(
      "The firm",
      "Fifty-five years of standing behind the delivery.",
      "Consolidated Engineers was established in 1969 and has done business with federal and provincial government departments ever since. The business model has changed over that time. The habit of accountability has not.",
      "About",
  )}

  <section class="section">
    <div class="wrap split">
      <div class="split-media" data-reveal>
        <img src="assets/img/crane-site.jpg" alt="Cranes and construction equipment on a large site" width="700" height="875" loading="lazy">
      </div>
      <div data-reveal>
        <span class="eyebrow">Introduction</span>
        <h2 style="font-size:clamp(2rem,4vw,3.4rem);margin:14px 0 22px">A local agent with the manufacturer still on the line.</h2>
        <p class="lead">Our role is to be the reliable local principal for international manufacturers in Pakistan: the entity that carries the import, the documentation, the demonstration and the after-sales obligation.</p>
        <p style="margin-top:18px;color:var(--steel)">Engagement with the defence department in 1985 established a position in the market that has held for four decades. Over the same period the business expanded into the civil departments of Pakistan, and was organised on modern business lines to become a supplier with the standing to take on contracts of any value.</p>
        <p style="margin-top:14px;color:var(--steel)">Every new product is additionally indexed with the civilian departments and the Ministry of Defence before it is introduced to a user unit for demonstration and procurement. That is the work behind a supply contract, and we do it as a matter of course.</p>
        <div class="timeline" style="margin-top:36px">
          <div class="timeline-row"><div class="timeline-year">1969</div><div><h3>Established</h3><p>The firm begins trading, and begins supplying federal and provincial departments.</p></div></div>
          <div class="timeline-row"><div class="timeline-year">1972</div><div><h3>Chamber membership</h3><p>Registered with the Lahore Chamber of Commerce and Industries as member 2806-A.</p></div></div>
          <div class="timeline-row"><div class="timeline-year">1985</div><div><h3>Defence registration</h3><p>Registered as a contractor with the Directorate General Defence Purchase, Ministry of Defence Production.</p></div></div>
          <div class="timeline-row"><div class="timeline-year">Today</div><div><h3>Category A</h3><p>Listed by the defence department in Financial Category A, with no limit of contract value.</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-dark">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <span class="section-index">Organisation</span>
          <h2>Four functions, one contract.</h2>
        </div>
        <p class="aside">A supply contract passes through four parts of the firm. The same person stays accountable across all four.</p>
      </div>
      <div class="service-grid" style="background:var(--line-dark);border-color:var(--line-dark)">
        <div class="service-card" style="background:var(--ink-2);color:var(--white)"><span class="num">01</span><h3>Principal relationships</h3><p style="color:rgba(251,248,242,.62)">Maintaining accredited agency agreements with foreign manufacturers, and the technical correspondence that goes with them.</p></div>
        <div class="service-card" style="background:var(--ink-2);color:var(--white)"><span class="num">02</span><h3>Procurement and compliance</h3><p style="color:rgba(251,248,242,.62)">Indexing with the civilian departments and the Ministry of Defence, tender response, and the documentation a public contract requires.</p></div>
        <div class="service-card" style="background:var(--ink-2);color:var(--white)"><span class="num">03</span><h3>Engineering and delivery</h3><p style="color:rgba(251,248,242,.62)">Specification against the site, import, installation, commissioning and calibration.</p></div>
        <div class="service-card" style="background:var(--ink-2);color:var(--white)"><span class="num">04</span><h3>After-sales</h3><p style="color:rgba(251,248,242,.62)">Training, maintenance, repair and the continuing spares path for equipment already in service.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div data-reveal>
        <span class="eyebrow">Vision</span>
        <h2 style="font-size:clamp(2rem,4vw,3.2rem);margin:14px 0 22px">To excel in supporting the end user.</h2>
        <p class="lead">Our vision is to excel in supporting our end users and customers, with the support of the principals and manufacturers we represent.</p>
        <p style="margin-top:18px;color:var(--steel)">That sentence is deliberately about the end user, not about us. The manufacturer supplies the equipment. We are accountable for the outcome.</p>
        <a class="link-arrow" href="services.html" style="margin-top:26px">See the after-sales scope</a>
      </div>
      <div class="timeline" data-reveal>
        <div class="timeline-row"><div class="timeline-year">01</div><div><h3>Registered office</h3><p>CE House, 108 E-1, Gulberg III, Lahore, Pakistan.</p></div></div>
        <div class="timeline-row"><div class="timeline-year">02</div><div><h3>DGDP contractor</h3><p>Directorate General Defence Purchase, Ministry of Defence Production, since 1985.</p></div></div>
        <div class="timeline-row"><div class="timeline-year">03</div><div><h3>Financial Category A</h3><p>Listed by the defence department in Financial Category A, with no limit of contract value.</p></div></div>
        <div class="timeline-row"><div class="timeline-year">04</div><div><h3>Accredited agent</h3><p>Acting in Pakistan on behalf of foreign principals and manufacturers.</p></div></div>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div><h2>Talk to us about a requirement.</h2><p>Sourcing and supplying global equipment as a reliable local agent to government, defence and private industry in Pakistan.</p></div>
      <a class="btn" href="contact.html">Contact the firm</a>
    </div>
  </section>
</main>'''
    return page(
        "About the firm | Consolidated Engineers",
        "Consolidated Engineers has supplied equipment to Pakistan's government and defence departments since 1969. DGDP registered since 1985, Financial Category A.",
        "about.html",
        "about",
        body,
    )


def build_services():
    services = [
        ("01", "Installation, commissioning and calibration", "Site installation, commissioning to the manufacturer's specification and instrument calibration, with a signed handover record. Where the site requires civil or electrical preparation, that scope is identified before delivery rather than discovered during it."),
        ("02", "Maintenance and operational training", "Operator and maintenance training delivered on your site, on your equipment. The objective is a team that can run the unit safely and carry out first-line maintenance without waiting for a service visit."),
        ("03", "Repair and maintenance", "Fault diagnosis, repair and scheduled maintenance. We source parts through the same principal relationships the equipment came from, so a repair does not depend on an unofficial substitute."),
        ("04", "Indexing, demonstration and procurement support", "A new product must be indexed with the civilian departments and the Ministry of Defence before it can be introduced to a user unit. We handle indexing, arrange the demonstration and support the procurement process through to contract."),
        ("05", "Parts and long-term support", "A continuing spares path for the equipment we supply, including discontinued models that remain in service. Send the part number, or a photograph of the failed item, and we will identify the source."),
    ]
    cards = "\n".join(
        f'''<article class="service-card" data-reveal>
  <span class="num">{num}</span>
  <h3>{title}</h3>
  <p>{copy}</p>
  <a class="link-arrow" href="contact.html">Discuss this scope</a>
</article>'''
        for num, title, copy in services
    )
    body = f'''<main id="main">
  {page_hero(
      "After-sales",
      "The after-sales scope is part of the supply.",
      "A crane that arrives without commissioning, or a tow tractor without operator training, is an unfinished delivery. These services exist so the equipment is actually in service when we close the file.",
      "Services",
  )}

  <section class="section">
    <div class="wrap">
      <div class="service-grid">
        {cards}
      </div>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap split">
      <div data-reveal>
        <span class="eyebrow">Response</span>
        <h2 style="font-size:clamp(2rem,4vw,3.2rem);margin:14px 0 22px">One named contact per requirement.</h2>
        <p class="lead">Tell us the unit, the serial number if you have it, the site and the fault. We will confirm the next step and the person who owns it.</p>
        <div class="timeline" style="margin-top:30px">
          <div class="timeline-row"><div class="timeline-year">01</div><div><h3>Enquiry</h3><p>Unit, site and fault, with photographs or a part number where possible.</p></div></div>
          <div class="timeline-row"><div class="timeline-year">02</div><div><h3>Assessment</h3><p>We confirm the technical position with the principal and reply in writing.</p></div></div>
          <div class="timeline-row"><div class="timeline-year">03</div><div><h3>Scope and date</h3><p>A named person owns the visit, the parts and the date.</p></div></div>
        </div>
      </div>
      <div class="split-media" data-reveal>
        <img src="assets/img/tow-tractor-2.jpg" alt="Airport tow tractor in a service yard" width="700" height="875" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div data-reveal>
        <span class="eyebrow">Why it matters</span>
        <h2 style="font-size:clamp(2rem,4vw,3.2rem);margin:14px 0 22px">Discontinued does not mean abandoned.</h2>
        <p class="lead">Equipment bought in 1995 is often still in service. A supplier who disappears when the model is superseded leaves the user with a machine nobody will support.</p>
        <p style="margin-top:18px;color:var(--steel)">We continue to support discontinued models for parts and service, because that is what the equipment in the field requires.</p>
      </div>
      <div class="timeline" data-reveal>
        <div class="timeline-row"><div class="timeline-year">01</div><div><h3>Commissioning records signed at handover.</h3><p>The record names the configuration and the person who accepted it.</p></div></div>
        <div class="timeline-row"><div class="timeline-year">02</div><div><h3>Training on site, on your equipment.</h3><p>Operators and maintainers learn the unit they will actually run.</p></div></div>
        <div class="timeline-row"><div class="timeline-year">03</div><div><h3>Parts through the original principal.</h3><p>The part number and the traceability document come from the manufacturer, not a substitute.</p></div></div>
        <div class="timeline-row"><div class="timeline-year">04</div><div><h3>Discontinued models supported.</h3><p>Old units remain in the spares path for as long as they are in service.</p></div></div>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div><h2>Send a service request.</h2><p>Include the unit, the serial number and the site. We will confirm the next step and the person who owns it.</p></div>
      <a class="btn" href="contact.html">Start a request</a>
    </div>
  </section>
</main>'''
    return page(
        "After-sales services | Consolidated Engineers",
        "Installation, commissioning and calibration, maintenance and operational training, repair and long-term spares support for equipment supplied by Consolidated Engineers.",
        "services.html",
        "services",
        body,
    )


def build_products():
    catalogue = "\n".join(
        f'''<article class="catalogue-item" id="{cap["id"]}">
  <div class="catalogue-media" data-reveal>
    <img src="assets/img/{cap["image"]}" alt="{cap["title"]}" width="700" height="525" loading="lazy">
  </div>
  <div class="catalogue-copy" data-reveal>
    <span class="num">{cap["num"]} / {cap["label"]}</span>
    <h2>{cap["title"]}</h2>
    <p>{cap["summary"]}</p>
    <ul class="catalogue-list">
      <li><span>Source</span><span>Direct from principal</span></li>
      <li><span>Scope</span><span>Supply, import, commissioning</span></li>
      <li><span>Support</span><span>Parts and service</span></li>
      <li><span>Documentation</span><span>Traceable</span></li>
    </ul>
    <a class="link-arrow" href="contact.html" style="margin-top:22px">Enquire about this range</a>
  </div>
</article>'''
        for cap in CAPABILITIES
    )
    nav = "\n".join(
        f'<a href="#{cap["id"]}">{cap["label"]}</a>' for cap in CAPABILITIES
    )
    body = f'''<main id="main">
  {page_hero(
      "Products",
      "Eight categories. One accountable supplier.",
      "Each line is sourced from a manufacturer we represent directly. Where a model has been discontinued, we continue to support the units already in service.",
      "Products",
  )}

  <section class="section-tight">
    <div class="wrap">
      <div class="cat-nav">{nav}</div>
      {catalogue}
      <div style="border-top:1px solid var(--line);padding-top:26px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:18px;align-items:center">
        <p style="max-width:52ch;color:var(--steel);font-size:.92rem">A part number or a photograph of the failed item is enough to start a spares enquiry. We will identify the source and the lead time.</p>
        <a class="btn btn-outline" href="contact.html">Send a parts enquiry</a>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div><h2>Need a specification checked?</h2><p>Send the application and the site conditions. We will confirm the configuration, the delivery position and the support scope.</p></div>
      <a class="btn" href="contact.html">Request a quotation</a>
    </div>
  </section>
</main>'''
    return page(
        "Products | Consolidated Engineers",
        "Ground support equipment, cranes and lifting systems, aerial lift trucks, mining machinery, flood lighting, Goodyear aviation tyres, parts and spares.",
        "products.html",
        "products",
        body,
    )


def build_sectors():
    blocks = "\n".join(
        f'''<article class="catalogue-item" id="sector-{sector["num"]}">
  <div class="catalogue-media" data-reveal>
    <img src="assets/img/{sector["image"]}" alt="{sector["title"]}" width="700" height="525" loading="lazy">
  </div>
  <div class="catalogue-copy" data-reveal>
    <span class="num">Sector {sector["num"]}</span>
    <h2>{sector["title"]}</h2>
    <p>{sector["summary"]}</p>
    <ul class="catalogue-list">
      {''.join(f"<li><span>{point}</span><span></span></li>" for point in sector["points"])}
    </ul>
  </div>
</article>'''
        for sector in SECTORS
    )
    body = f'''<main id="main">
  {page_hero(
      "Sectors",
      "Three sectors. One standard of delivery.",
      "Public procurement and private procurement fail for different reasons. We structure the response to the sector, and keep the same accountability in both.",
      "Sectors",
  )}

  <section class="section">
    <div class="wrap">
      {blocks}
    </div>
  </section>

  <section class="section section-dark">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div><span class="section-index">Accredited agency</span><h2>We act for the manufacturer, in Pakistan.</h2></div>
        <p class="aside">Consolidated Engineers works as the accredited agent in Pakistan on behalf of foreign principals and manufacturers. The manufacturer's technical position reaches you through a local entity that carries the contract.</p>
      </div>
      <div class="cred-band">
        <div class="cred"><strong>01</strong><span>DGDP contractor since 1985</span></div>
        <div class="cred"><strong>02</strong><span>Financial Category A</span></div>
        <div class="cred"><strong>03</strong><span>LCCI 2806-A since 1972</span></div>
        <div class="cred"><strong>04</strong><span>Accredited agent</span></div>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div><h2>Discuss an agency or supply requirement.</h2><p>Whether you are a department, a contractor or a manufacturer looking for a local principal, start with a conversation.</p></div>
      <a class="btn" href="contact.html">Contact the firm</a>
    </div>
  </section>
</main>'''
    return page(
        "Sectors we serve | Consolidated Engineers",
        "Consolidated Engineers supplies civilian government departments, military departments and private companies in Pakistan with imported equipment and after-sales support.",
        "sectors.html",
        "sectors",
        body,
    )


def build_projects():
    body = f'''<main id="main">
  {page_hero(
      "Representative scopes",
      "Representative scopes, not a logo wall.",
      "The useful question is not how many logos a supplier has collected. It is whether the specification, the delivery and the support can be described clearly.",
      "Projects",
  )}

  <section class="section">
    <div class="wrap">
      <div style="border:1px solid var(--line);background:var(--paper-2);padding:18px 22px;margin-bottom:34px;font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--steel)">
        Scopes shown are representative of the equipment and support the firm supplies. Client names and contract values are withheld.
      </div>
      <div class="project-grid">
        {project_cards(link=False)}
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div><h2>Have a similar scope?</h2><p>Send the application, the site and the constraint. We will tell you what the equipment has to do and what the support looks like.</p></div>
      <a class="btn" href="contact.html">Send a requirement</a>
    </div>
  </section>
</main>'''
    return page(
        "Representative scopes | Consolidated Engineers",
        "Representative equipment and support scopes across cranes, airfield ground support, mining, aviation tyres and access platforms in Pakistan.",
        "projects.html",
        "projects",
        body,
    )


def build_insights():
    body = f'''<main id="main">
  {page_hero(
      "Insights",
      "Notes from the procurement floor.",
      "Practical writing on specification, commissioning, spares and public procurement. Written for the people who have to make the equipment work.",
      "Insights",
  )}

  <section class="section">
    <div class="wrap">
      <div class="insight-grid">
        {insight_grid()}
        {insight_card(ARTICLES[4])}
      </div>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap split">
      <div data-reveal>
        <span class="eyebrow">Field notes</span>
        <h2 style="font-size:clamp(2rem,4vw,3.2rem);margin:14px 0 22px">A short note, a few times a year.</h2>
        <p class="lead">New articles on specification, after-sales and procurement. No newsletter theatre, and no daily mail.</p>
      </div>
      <div data-reveal>
        <form class="form" data-enquiry-form>
          <div class="field">
            <label for="note-email">Email address</label>
            <input id="note-email" name="email" type="email" required>
          </div>
          <button class="btn btn-signal" type="submit">Request field notes</button>
          <p class="form-note">This demonstration does not store addresses. Use the contact form for a real enquiry.</p>
          <p class="form-status" data-form-status></p>
          <p style="margin-top:8px;font-size:.78rem"><a data-form-mail href="mailto:{EMAIL}">Open an email draft</a></p>
        </form>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <div><h2>Have a technical question?</h2><p>Send the application and the constraint. We will reply with a sourced position, not a brochure.</p></div>
      <a class="btn" href="contact.html">Ask the firm</a>
    </div>
  </section>
</main>'''
    return page(
        "Insights | Consolidated Engineers",
        "Practical articles on crane specification, commissioning, aviation tyres, public procurement and long-term equipment support.",
        "insights.html",
        "insights",
        body,
    )


def build_article(article):
    related = [a for a in ARTICLES if a["slug"] != article["slug"]][:3]
    related_cards = "\n".join(
        f'''<a class="insight-card" href="{a["slug"]}.html">
  <div class="insight-media"><img src="../assets/img/{a["image"]}" alt="{a["alt"]}" width="800" height="500" loading="lazy"></div>
  <span class="insight-tag">{a["category"]}</span>
  <h3>{a["title"]}</h3>
  <div class="insight-meta">{a["date"]} · {a["read"]}</div>
</a>'''
        for a in related
    )
    body = f'''<div class="article-progress" data-progress></div>
<main id="main">
  <article data-article>
    <header class="article-head">
      <div class="wrap">
        <div class="crumb"><a href="../index.html">Home</a><span>/</span><a href="../insights.html">Insights</a><span>/</span><span>{article["category"]}</span></div>
        <span class="eyebrow">{article["category"]}</span>
        <h1>{article["title"]}</h1>
        <p class="lead">{article["dek"]}</p>
        <div class="article-meta"><span>{article["date"]}</span><span>{article["read"]}</span><span>Consolidated Engineers</span></div>
      </div>
      <div class="wrap">
        <div class="article-hero"><img src="../assets/img/{article["image"]}" alt="{article["alt"]}" width="1200" height="600"></div>
      </div>
    </header>

    <div class="wrap">
      <div class="article-body">
        {article["body"]}
        <div class="article-cta">
          <div>
            <span class="mono" style="color:var(--steel)">Next step</span>
            <p style="margin-top:6px;font-size:1.05rem;color:var(--ink)">Have a live requirement or a specification to check?</p>
          </div>
          <a class="btn btn-signal" href="../contact.html">Send it to the firm</a>
        </div>
      </div>
    </div>

    <section class="related">
      <div class="wrap">
        <span class="eyebrow">Related reading</span>
        <div class="related-grid">
          {related_cards}
        </div>
      </div>
    </section>
  </article>
</main>'''
    return page(
        article["title"] + " | Consolidated Engineers",
        article["dek"],
        "insights/" + article["slug"] + ".html",
        "insights",
        body,
        prefix="../",
    )


def build_contact():
    body = f'''<main id="main">
  {page_hero(
      "Contact",
      "Tell us what the equipment has to do.",
      "Send the application, the site conditions and any specification you already hold. We will respond with a sourced option, a delivery position and the support scope in writing.",
      "Contact",
  )}

  <section class="section">
    <div class="wrap contact-grid">
      <form class="form" data-enquiry-form>
        <div class="form-row">
          <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" required></div>
          <div class="field"><label for="org">Organisation</label><input id="org" name="organisation" type="text"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
          <div class="field"><label for="phone">Telephone</label><input id="phone" name="telephone" type="tel"></div>
        </div>
        <div class="field">
          <label for="category">What is the enquiry about</label>
          <select id="category" name="category">
            <option>Aircraft towing tractor</option>
            <option>Runway repair machine</option>
            <option>Industrial crane</option>
            <option>Tower crane</option>
            <option>Truck mounted crane</option>
            <option>Aerial lift truck</option>
            <option>Mining machinery</option>
            <option>Road and construction machinery</option>
            <option>Flood lighting</option>
            <option>Aviation tyres</option>
            <option>Parts and spares</option>
            <option>Installation and commissioning</option>
            <option>Maintenance and training</option>
            <option>Repair and maintenance</option>
            <option>Indexing and demonstration</option>
            <option>General enquiry</option>
          </select>
        </div>
        <div class="field"><label for="requirement">Requirement</label><textarea id="requirement" name="requirement" required placeholder="Application, site conditions, capacity, delivery position, or the part number you need."></textarea></div>
        <button class="btn btn-signal btn-block" type="submit">Send enquiry</button>
        <p class="form-note">We use your details only to answer this enquiry. No mailing list, no third parties.</p>
        <p class="form-status" data-form-status></p>
        <p style="margin-top:8px;font-size:.78rem"><a data-form-mail href="mailto:{EMAIL}">Open an email draft</a></p>
      </form>

      <aside>
        <div class="contact-block" style="margin-top:0;border-top:0;padding-top:0">
          <span class="eyebrow">Direct</span>
          <h2 style="margin-top:12px">Or reach the office directly.</h2>
          <p style="margin-top:12px"><strong>Registered office</strong><br>CE House, 108 E-1,<br>Gulberg III, Lahore, Pakistan</p>
          <p style="margin-top:12px"><a href="tel:+924235761247">{PHONE_ALT}</a><br><a href="tel:+924235764907">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p style="margin-top:12px"><strong>Office hours</strong><br>Monday to Saturday, 09:00 to 18:00 PKT.</p>
        </div>
        <div class="contact-block">
          <h2>What happens after you send it</h2>
          <p>Your enquiry is read by the person who will handle it. If it needs a manufacturer's technical position, we go to the principal and come back with a written answer rather than an estimate.</p>
        </div>
        <div class="contact-block">
          <h2>Finding the office</h2>
          <p>CE House is on E-1 in Gulberg III. If you are visiting about a tender or a demonstration, call ahead so the right person is on site.</p>
          <p style="margin-top:12px"><a href="https://maps.google.com/?q=CE+House+108+E-1+Gulberg+III+Lahore" target="_blank" rel="noopener">Open in Maps</a></p>
        </div>
      </aside>
    </div>
  </section>
</main>'''
    return page(
        "Contact and enquiries | Consolidated Engineers",
        "Contact Consolidated Engineers, CE House, 108 E-1, Gulberg III, Lahore. Telephone +92 42 3576 4907-08. Enquiries about equipment, spares and after-sales support.",
        "contact.html",
        "contact",
        body,
    )


def build_policy(slug, title, lead, sections):
    body = f'''<main id="main">
  <div class="wrap">
    <div class="policy">
      <div class="crumb"><a href="index.html">Home</a><span>/</span><span>{title}</span></div>
      <h1>{title}</h1>
      <p class="lead">{lead}</p>
      <p class="policy-note">Template. Review before publication.</p>
      {sections}
    </div>
  </div>
</main>'''
    return page(
        title + " | Consolidated Engineers",
        lead,
        slug + ".html",
        "",
        body,
    )


def build_404():
    body = '''<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <div class="crumb"><a href="index.html">Home</a><span>/</span><span>404</span></div>
      <span class="eyebrow">404</span>
      <h1>This page has moved on.</h1>
      <p class="lead">The link may be old, or the page may have been retired. The capabilities and the enquiry form are one click away.</p>
      <div class="hero-actions"><a class="btn btn-signal" href="products.html">Explore the range</a><a class="btn btn-outline" href="contact.html">Contact the firm</a></div>
    </div>
  </section>
</main>'''
    return page(
        "Page not found | Consolidated Engineers",
        "The page you asked for is not here. Return to the Consolidated Engineers capabilities or contact the firm.",
        "404.html",
        "",
        body,
    )


def main():
    outputs = {
        "index.html": build_home(),
        "about.html": build_about(),
        "services.html": build_services(),
        "products.html": build_products(),
        "sectors.html": build_sectors(),
        "projects.html": build_projects(),
        "insights.html": build_insights(),
        "contact.html": build_contact(),
        "404.html": build_404(),
    }
    for article in ARTICLES:
        outputs["insights/" + article["slug"] + ".html"] = build_article(article)

    privacy = build_policy(
        "privacy",
        "Privacy policy",
        "How this site handles personal information.",
        """
<h2>What we collect</h2>
<p>When you use the enquiry form, the site asks for your name, organisation, email address, telephone number, the category of enquiry and your requirement.</p>
<h2>Why we need it</h2>
<p>Only to answer the enquiry. We do not sell personal information and we do not add enquirers to a mailing list.</p>
<h2>Who sees it</h2>
<p>The people who need to answer the enquiry. A manufacturer may receive the technical details necessary to respond, but only where the enquiry requires it.</p>
<h2>How long we keep it</h2>
<p>Enquiries are kept for as long as needed to answer them and to keep a record of the commercial relationship, then removed when no longer useful.</p>
<h2>Your choices</h2>
<p>You can ask to see, correct or delete the information held about you. Write to info@cedefense.com.</p>
<h2>Cookies</h2>
<p>This demonstration does not set advertising cookies or tracking profiles. See the cookies page.</p>
""",
    )
    terms = build_policy(
        "terms",
        "Terms of use",
        "The terms that apply to this website.",
        """
<h2>Information on this site</h2>
<p>The content is provided for general information about the firm and its capabilities. It is not a quotation, a technical specification or an offer capable of acceptance.</p>
<h2>Enquiries</h2>
<p>An enquiry through this site is an invitation to discuss a requirement. A supply contract exists only when a written quotation is accepted or a purchase order is accepted in writing.</p>
<h2>Product descriptions</h2>
<p>Equipment descriptions are indicative. The configuration, capacity and documentation for a particular requirement are confirmed in the quotation and the manufacturer's datasheet.</p>
<h2>Intellectual property</h2>
<p>The Consolidated Engineers name, this site and its text and layout belong to the firm. Manufacturer names and marks belong to their respective owners.</p>
<h2>Liability</h2>
<p>Nothing in these terms removes rights you have under the law that applies to you. Beyond that, the firm is not liable for indirect loss arising from reliance on general information on this site.</p>
<h2>Contact</h2>
<p>Questions about these terms: info@cedefense.com.</p>
""",
    )
    cookies = build_policy(
        "cookies",
        "Cookies",
        "What this demonstration site stores in your browser.",
        """
<h2>What is stored</h2>
<p>This demonstration does not set advertising cookies and does not create tracking profiles. It does not store an enquiry draft in your browser.</p>
<h2>Third-party requests</h2>
<p>The site loads fonts from Google Fonts. Those requests are made to Google's servers and are subject to Google's own privacy terms. No analytics script is installed.</p>
<h2>If analytics is added</h2>
<p>Before publication, this page will list the service, the cookies it sets, their purpose and their lifetime, and a consent choice will be offered where the law requires one.</p>
<h2>How to clear cookies</h2>
<p>Use your browser settings, usually under privacy or site data. Clearing cookies does not affect your ability to read the site.</p>
<h2>Contact</h2>
<p>Questions about cookies: info@cedefense.com.</p>
""",
    )
    outputs["privacy.html"] = privacy
    outputs["terms.html"] = terms
    outputs["cookies.html"] = cookies

    for relative, content in outputs.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print("wrote", relative)


if __name__ == "__main__":
    main()
