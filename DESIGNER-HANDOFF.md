# IHLab homepage — designer handoff

**Purpose:** Clickable HTML/CSS draft for Alyssa review. Rebuild or restyle freely in Hostinger Website Builder / WordPress later. This folder is the visual + copy source of truth for v1.

**Paths**
- Preview file: `site/index.html`
- Mark SVG: `site/assets/ihlab-mark.svg`
- Optional full logo SVG: `site/assets/ihlab-logo.svg` (replace when master logo lands)
- Copy source: `../homepage-copy-v1.md`
- Brand reference PNG: `../IHLab_Brand_Reference_Final2.png`

**Local preview**
```bash
python3 -m http.server 8770 --directory /workspace/ihlab/site --bind 127.0.0.1
```
Open http://localhost:8770/  
(Port 8765 was already in use on this box; 8770 is the live draft server.)

---

## Brand tokens (Final2 — locked)

| Token | Hex | Use |
|-------|-----|-----|
| Navy | `#0E232E` | Primary text, dark panels, logo mark |
| Sage | `#556248` | Subheads, muted labels, secondary emphasis |
| Ivory | `#F0EEE0` | Page background |
| Gold | `#A88428` | **Primary CTAs and key links only** |
| Coral | `#C86A4F` | **Badges / tags only** |

Do **not** use gold for large fills, nav text, or body links except CTAs. Do **not** use coral for buttons.

### Typography (Google Fonts)
- **Headlines / display:** Source Serif 4 — Medium / SemiBold / Italic
- **Body, nav, UI, buttons:** Work Sans — Regular / Medium / SemiBold
- Feel: huge serif headlines, lots of ivory air, few boxes

CDN used in `index.html`:
```
https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,500;0,600;1,500;1,600&family=Work+Sans:wght@400;500;600&display=swap
```

### Logo
- Organ-pipe mark: **9 ascending tapered bars**, navy only (no gold in the mark)
- Wordmark: Investable Humanity / Leadership Lab with a thin rule and small diamond between lines
- Swap `assets/ihlab-mark.svg` when the master SVG arrives; keep navy-only mark rule

---

## Section map (matches `index.html`)

1. **Sticky nav** — mark + wordmark · Why · The Lab · Partners · Attend · Partner with us (gold CTA)
2. **Hero** — independent-initiative eyebrow · “Utah has the heart…” · Request a seat → `#attend` · Partner with us → `#partner` · proof strip
3. **Why** (`#why`) — opportunity · three moves
4. **The Lab** (`#lab`) — stats grid · Nov 3 Shriver callout (navy panel + coral badge)
5. **Sampler** (`#sampler`) — Dignity.Us · TOSLI · UAC cards
6. **Collaborating Partners** (`#partners`) — never “Founding Partners” · tagline “Independent initiative. Shared table.”
7. **Why attend** (`#attend`) — outcomes · interest form (mailto Alyssa)
8. **Partner** (`#partner`) — navy panel · partnership form (mailto Alyssa)
9. **Footer** — quote · contact · independent-initiative legal line

---

## Voice & framing rules (do not regress)

- Independent initiative; **Collaborating Partners** = UAC, TOSLI, Dignity.Us (never “Founding Partners”)
- No founder hero on the homepage
- No UAC tagline
- No tax-deductible / donate language (partner copy may say tax treatment is confirmed per partner)
- Table leads are dignified leaders — not merely volunteers or facilitators
- Tone: confident / optimistic / realist; no em dashes; avoid “not X, it’s Y”

---

## CTAs & forms

| CTA | Target |
|-----|--------|
| Request a seat | `#attend` → mailto `alyssa@ihlab.us` |
| Partner with us | `#partner` → mailto `alyssa@ihlab.us` |

Forms are simple interest captures that open the visitor’s email client. Replace with Hostinger/WordPress form plugins later if desired; keep the same fields and destination email unless Alyssa changes it.

---

## Hostinger / designer edit guide

**Easiest path:** recreate section by section in Hostinger Builder using this page as the comps + copy doc. Match spacing generously; prefer open layouts over card grids.

**If staying on static HTML:** edit `index.html` CSS variables at the top of `<style>`:
```css
:root {
  --navy: #0E232E;
  --sage: #556248;
  --ivory: #F0EEE0;
  --gold: #A88428;
  --coral: #C86A4F;
}
```

**Swap logos:** drop final partner logos into `assets/` and replace the text placeholders in `#partners`. Drop master IHLab logo over `assets/ihlab-mark.svg` / `ihlab-logo.svg`.

**Locked vs editable**
| Locked (ask first) | Freely editable |
|--------------------|-----------------|
| Color roles (gold = CTA only, coral = badge only) | Body copy length / line breaks |
| Partner naming (“Collaborating Partners”) | Photography / optional imagery |
| Independent-initiative framing | Spacing, section order polish |
| Font pairing | Button labels if CTAs stay equivalent |

---

## SEO / meta already set

- Title: Investable Humanity Leadership Lab · IHLab
- Description: dignity-centered cohort one-liner
- Favicon: `assets/ihlab-mark.svg`
- Theme color: navy

Add OG image later when photography / brand lockup is final.

---

## Checklist before Alyssa share

- [ ] Open on phone + desktop
- [ ] Both CTAs scroll to the right sections
- [ ] Mailto opens with a sensible subject
- [ ] Partners labeled Collaborating Partners
- [ ] No founder block, no UAC tagline, no donate/tax-deductible pitch
- [ ] Nov 3 callout visible on The Lab section
