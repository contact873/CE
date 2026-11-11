# Consolidated Engineers, rebuild

A complete redesign of the Consolidated Engineers website. New layout, new typography, new written content and five original articles. The firm's verified facts, credentials, contact details and photographs are retained.

The rebuild is a demonstration: all pages are `noindex`, `robots.txt` disallows crawlers, and the enquiry form produces an email draft rather than sending to a server.

Live preview: https://consolidated-engineers-rebuild.vercel.app/

Vercel project: `consolidated-engineers-rebuild`. The live `cedefense.com` site has not been touched; this is a separate preview deployment.

## What changed

- **Design.** Industrial editorial layout with a paper, graphite and safety-orange palette. Large Archivo headlines, Inter Tight body text and IBM Plex Mono labels.
- **Structure.** Home, about, products, services, sectors, projects, insights, five article pages, contact, privacy, terms, cookies and a 404 page.
- **Content.** All page copy rewritten. Five long-form articles on crane specification, commissioning, aviation tyres, public procurement and long-term equipment support.
- **Images.** The firm's own photographs, copied from the existing site and optimised. No stock photography.
- **Form.** A front-end demonstration that composes an email draft to `info@cedefense.com` and explains that the demo does not send.

## Pages

```
index.html                 home
about.html                 history, timeline, organisation
products.html              eight capability categories
services.html              after-sales scope
sectors.html               civilian government, defence, private industry
projects.html              representative scopes
insights.html              article index
insights/crane-specification.html
insights/commissioning.html
insights/aviation-tyres.html
insights/public-procurement.html
insights/discontinued-support.html
contact.html               enquiry form and office details
privacy.html
terms.html
cookies.html
404.html
```

## Preview

```bash
cd ~/Documents/consolidated-site
python3 -m http.server 8084
```

Then open http://localhost:8084/

## Deploy

Static site, no build step. On Vercel, import the folder, set the framework preset to **Other**, leave the build command empty and the output directory empty or `.`.

The site currently expects to sit at the domain root because links are relative. It works from a subfolder, except the `.htaccess` 404 path, which assumes the domain root.

## Rebuilding pages

All pages are generated from `tools/build_site.py`:

```bash
python3 tools/build_site.py
```

Edit the page functions or the `ARTICLES` list there. The stylesheet is `assets/css/site.css`; the behaviour is `assets/js/site.js`.

## Before publication

1. Confirm the founder, board and CEO message if they are to be included. They were not reconstructed.
2. Confirm the product models, capacities and current manufacturer datasheets. The rebuild describes categories, not model numbers or prices.
3. Confirm office hours and the enquiry recipient.
4. Review the policy pages with the firm.
5. Connect the form to a server-side handler or a form service. The current form only opens an email draft.
6. Remove `noindex, nofollow` from every page and the disallow rule in `robots.txt`.
7. Confirm the partner and manufacturer logos before adding them. None were added, because the source images could not all be matched to named companies with confidence.

## Notes

- Fonts are Archivo, Inter Tight and IBM Plex Mono from Google Fonts.
- The images are local, in `assets/img`, and are optimised JPEGs.
- The site uses no third-party JavaScript and no analytics.
- The map link opens Google Maps in a new tab; there is no embedded map.

## File tree

```
consolidated-site/
  index.html
  about.html
  products.html
  services.html
  sectors.html
  projects.html
  insights.html
  contact.html
  privacy.html
  terms.html
  cookies.html
  404.html
  insights/
    (five article pages)
  assets/
    css/site.css
    js/site.js
    img/ (23 photographs)
  tools/
    build_site.py
  .htaccess
  robots.txt
  sitemap.xml
  vercel.json
  site.config.json
```
