# IHLab homepage — designer handoff (v2 · Final2)

## NOTES — Final2 redesign + People Pitch (v2)

**Intent:** Match `IHLab_Brand_Reference_Final2.png` faithfully. Navy/ivory section rhythm, coral badges, gold CTAs only. Visibly different from the Saprea-inspired soft-fade collage draft (v1.1).

**What changed from v1.1**
1. **Hero** is a full-width **navy** band (Final2 guide pattern): coral “Founding Cohort” pill, white Source Serif headline, white Work Sans lede, gold primary CTA + ghost secondary. Soft-fade stock hero photo removed as identity.
2. **Section rhythm** alternates **ivory** and **navy**. Pale sage-tinted bands (`#E8E9DF`) removed. Sage stays restrained (accents, muted labels on light, list markers).
3. **Labels** are gold Source Serif small-caps with wide tracking (not sage-only).
4. **Photos** kept as support only (roundtable under Why, listening split, lounge in Lab, duo in Partner). Large soft-fade collage / friends-circle full-bleed identity removed; brand pull quote sits on a clean navy band.
5. **People Pitch** section (`#pitch`) added after The Lab / before Sampler & Partners, with native A-frame posters.
6. **Gold** fixed sitewide to `#A8842B` (was `#A88428`).

**Do not** put People Pitch yellow/blue into global CSS variables — posters keep native art inside white cards; section chrome uses IHLab tokens only.

---

**Purpose:** Clickable HTML/CSS draft for Alyssa review. Rebuild or restyle freely in Hostinger Website Builder / WordPress later. This folder is the visual + copy source of truth for v2.

**Paths**
- Preview file: `site/index.html`
- Mark SVG: `site/assets/ihlab-mark.svg`
- Optional full logo SVG: `site/assets/ihlab-logo.svg` (replace when master logo lands)
- Pitch posters: `site/assets/pitch/1.png` … `12.png` (gallery uses 1, 2, 8, 12)
- Copy source: `../homepage-copy-v1.md`
- Brand reference PNG: `../IHLab_Brand_Reference_Final2.png`

**Local preview**
```bash
python3 -m http.server 8770 --directory /workspace/ihlab/site --bind 127.0.0.1
```
Open http://localhost:8770/

---

## Brand tokens (Final2 — locked)

| Token | Hex | Use |
|-------|-----|-----|
| Navy | `#0E232E` | Primary text, dark panels, hero, navy bands, logo mark |
| Sage | `#556248` | Restrained accents, muted labels on light, secondary emphasis |
| Ivory | `#F0EEE0` | Page background, light section bands |
| Gold | `#A8842B` | **Primary CTAs and key links only**; gold small-caps section labels |
| Coral | `#C86A4F` | **Badges / tags only** |

Do **not** use gold for large fills, nav text, or body links except CTAs. Do **not** use coral for buttons.

### Typography (Google Fonts)
- **Headlines / display:** Source Serif 4 — Medium / SemiBold / Italic
- **Body, nav, UI, buttons:** Work Sans — Regular / Medium / SemiBold
- **Labels:** Source Serif 4 Medium, uppercase / small-caps feel, wide tracking (~0.2em), **gold**
- **Taglines / quotes:** Source Serif 4 Italic

CDN used in `index.html`:
```
https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,500;0,600;1,500;1,600&family=Work+Sans:wght@400;500;600&display=swap
```

### Logo
- Organ-pipe mark: **9 ascending tapered bars**, navy only (no gold in the mark)
- Wordmark: Investable Humanity / Leadership Lab with a thin rule and small diamond between lines
- Swap `assets/ihlab-mark.svg` when the master SVG arrives; keep navy-only mark rule

### Guide pattern (navy band)
Navy background + coral pill badge + white serif headline + white body + gold CTA button (+ optional ghost secondary on dark). Used for Hero and reusable dark callouts.

---

## Section map (matches `index.html` v2)

1. **Sticky nav** — mark + wordmark · Why · The Lab · **Pitch** · Partners · Attend · Partner with us (gold CTA, Work Sans)
2. **Hero** — full-width navy · coral “Founding Cohort” badge · white headline/lede · gold + ghost CTAs · proof strip (no soft-fade hero photo)
3. **Why** (`#why`, ivory) — opportunity · three moves · support roundtable photo
4. **Human split** (ivory) — listening photo + italic human line
5. **Quote band** (navy) — “The earliest investment…” (no full-bleed stock photo identity)
6. **The Lab** (`#lab`, ivory) — lounge-diverse support photo · stats · Nov 3 Shriver callout (coral badge on navy inset)
7. **People Pitch** (`#pitch`, navy) — framing copy · gallery of A-frames `1`, `2`, `8`, `12` · posters keep native yellow/blue art
8. **Sampler** (`#sampler`, ivory) — partner cards (no modular photo collage)
9. **Collaborating Partners** (`#partners`, navy) — never “Founding Partners” · tagline “Independent initiative. Shared table.”
10. **Why attend** (`#attend`, ivory) — listening support photo · outcomes · interest form (mailto Alyssa)
11. **Partner** (`#partner`, ivory shell + navy panel) — duo-light · partnership form (mailto Alyssa)
12. **Footer** — quote · contact · legal line · Unsplash + Pitch credit

---

## People Pitch assets

| Frame | Path | Role in gallery |
|-------|------|-----------------|
| Left arrow | `assets/pitch/1.png` | Directional A-frame |
| Right arrow | `assets/pitch/2.png` | Directional A-frame |
| Up arrow | `assets/pitch/8.png` | Directional A-frame |
| Up arrow (alt) | `assets/pitch/12.png` | Directional A-frame |

Remaining frames `3–7`, `9–11` available for later swaps. Framing copy only — no invented event dates.

---

## Voice & framing rules (do not regress)

- Independent initiative; **Collaborating Partners** = UAC, TOSLI, Dignity.Us (never “Founding Partners”)
- No founder hero on the homepage
- No UAC tagline
- No tax-deductible / donate language (partner copy may say tax treatment is confirmed per partner)
- Table leads are dignified leaders — not merely volunteers or facilitators
- Tone: confident / optimistic / realist; no em dashes; avoid “not X, it’s Y”
- Keep story claims: Utah cohort, 50 leaders, 8 sessions, $2,500, partners, mailto Alyssa — do not invent new claims

---

## CTAs & forms

| CTA | Target |
|-----|--------|
| Request a seat | `#attend` → mailto `alyssa@ihlab.us` |
| Partner with us | `#partner` → mailto `alyssa@ihlab.us` |

Forms are simple interest captures that open the visitor’s email client. Replace with Hostinger/WordPress form plugins later if desired; keep the same fields and destination email unless Alyssa changes it.

---

## Hostinger / designer edit guide

**Easiest path:** recreate section by section in Hostinger Builder using this page as the comps + copy doc. Prefer navy/ivory bands over pale sage fills; open layouts over card grids.

**If staying on static HTML:** edit `index.html` CSS variables at the top of `<style>`:
```css
:root {
  --navy: #0E232E;
  --sage: #556248;
  --ivory: #F0EEE0;
  --gold: #A8842B;
  --coral: #C86A4F;
}
```

**Swap logos:** drop final partner logos into `assets/` and replace the text placeholders in `#partners`. Drop master IHLab logo over `assets/ihlab-mark.svg` / `ihlab-logo.svg`.

**Locked vs editable**
| Locked (ask first) | Freely editable |
|--------------------|-----------------|
| Color roles (gold = CTA/labels only, coral = badge only) | Body copy length / line breaks |
| Partner naming (“Collaborating Partners”) | Photography / optional imagery |
| Independent-initiative framing | Spacing, section order polish |
| Font pairing | Button labels if CTAs stay equivalent |
| People Pitch yellow/blue not in global tokens | Which pitch frames (1–12) appear in the gallery |

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
- [ ] Hero reads as Final2 navy guide pattern (not soft-fade photo hero)
- [ ] Both CTAs scroll to the right sections
- [ ] Pitch nav link → `#pitch`; gallery loads `assets/pitch/1,2,8,12.png`
- [ ] Mailto opens with a sensible subject
- [ ] Partners labeled Collaborating Partners
- [ ] No founder block, no UAC tagline, no donate/tax-deductible pitch
- [ ] Nov 3 callout visible on The Lab section
- [ ] Gold hex is `#A8842B` everywhere


### Pitch art (v2.1)
One hero A-frame + 3 thumbnails (not a 4-equal grid). Headline: “A taste of the pitch energy.” People Pitch yellow/blue stay in the images only.


### People Pitch section (v2.2)
Rewrote from poster gallery to **relationship copy** grounded in Alyssa’s Investable Humanity Drive docs:
- Trifecta: People Pitch = Voice; IHLab = Heart; CLPHI = Mind
- People Pitch = Dignity Fellow pipeline + funding-narrative insights in later sessions
- Brand: IHLab deliberately more elevated / separate from People Pitch marks
- Visual: **one** Power Up Reunion A-frame only (all 12 Canva exports were arrow variants of the same poster)
