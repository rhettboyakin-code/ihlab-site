# IHLab v4 restructure (preview)

Built from the "Investable Humanity Website" copy/UX doc. Static multi-page site in `/v4/`
(index, lab/, give/, about/). Live GitHub Pages output on `main` is untouched.

- Edit copy: `v4-src/build.py`, then `python3 v4-src/build.py`
- Styles: `v4/assets/base.css` (v3 tokens, unchanged) + `v4/assets/v4.css` (new components)
- Deploy noindex preview to Vercel: `./v4-src/deploy.sh`
- Placeholders (marked on-page): payment path, tax receipt/EIN, leader quote. "Join the list" and "Give" buttons use mailto to alyssa.dehart@utahadvocacycoalition.org until an email platform / payment processor is connected.
