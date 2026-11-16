# Consolidated Engineers, rebuild (navy and gold)

Regenerated 2026-11-16 from the approved concept image (`image_70d84c81.jpg`): navy and gold
identity, Fraunces + Inter typography, hero with functional product and services links.

Live preview: https://consolidated-engineers-rebuild.vercel.app/

## Core pages (this design)

```
index.html                 landing page (concept hero, product tiles, services, sectors, contact form)
about.html                 history, registrations, organisation
products.html              eight capability categories with anchored navigation
services.html              after-sales scope
sectors.html               civilian government, defence, private industry (+ agency / partners)
contact.html               enquiry form and office details
css/styles.css             design system (navy #0d1828 + gold #c9962e, 62.5% root)
js/main.js                 reveals, count-ups, scroll-spy, mobile menu, enquiry form handling
assets/images/             concept-hero.jpg (approved concept), stock-*.jpg (Pexels Free License),
                           craft/*.jpg (original navy/gold technical line art), logo.png
```

## Retained from the previous rebuild

`insights.html` + `insights/*.html` (five articles), `projects.html`, `privacy.html`,
`terms.html`, `cookies.html`, `404.html`, styled by `assets/css/site.css` (graphite/orange).
They are not linked from the new navigation; reachable by URL and sitemap.

## Notes

- All pages are `noindex` and `robots.txt` disallows crawlers until the client approves. Remove
  the robots meta and open robots.txt at go-live.
- The enquiry form posts to `enquiry.php` (Hostinger package in `deliverables/`). On this static
  preview it falls back to composing an email to `info@cedefense.com`.
- Image credits: `CREDITS.md` (Pexels Free License stock) and the firm's own product photography.
