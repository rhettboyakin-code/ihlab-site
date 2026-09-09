# IHLab homepage — designer handoff (v3 · Alyssa feedback)

## NOTES — v3 light hero + forest deep + drop People Pitch

**Intent:** Respond to Alyssa DeHart feedback. Lighter first paint for a heavy topic; deep forest instead of navy; confident / generous / collaborative / knowledgeable voice with specificity; only the three participating orgs (no People Pitch).

**What changed from v2**
1. **Hero** is **ivory-led** (not navy). Forest H1, muted lede, muted forest collab line, gold primary + normal ghost secondary (no `btn-on-dark` on light hero).
2. **Deep color** `#0E232E` navy replaced by **deep forest green** `#1F3328`. CSS token name `--navy` kept for less churn; value is forest. Hardcoded rgba lines updated to `31, 51, 40`.
3. **Dark bands** (quote, partners, partner panel, launch callout) use forest so weight stays where earned, not on first paint.
4. **People Pitch** removed entirely: nav link, `#pitch` section, pitch CSS, footer Pitch credit. Pitch assets may remain on disk unused.
5. **Copy** rewritten from Alyssa’s four tone words + specificity (Bob Hoffman: specific > platitudes). No antithesis / platitudes / em dashes.
6. **Theme-color** meta → `#1F3328`.

**Kept**
- Sage `#556248`, ivory `#F0EEE0`, gold `#A8842B`, coral `#C86A4F`
- Gold CTAs, coral badges only
- 3-org sampler + Collaborating Partners (UAC, TOSLI, Dignity.Us)
- Stats, Nov 3 2026 Shriver launch callout, quote “The earliest investment…”

---

**Purpose:** Clickable HTML/CSS draft for Alyssa review. Rebuild or restyle freely in Hostinger Website Builder / WordPress later. This folder is the visual + copy source of truth for v3.

**Paths**
- Preview file: `site/index.html`
- Mark SVG: `site/assets/ihlab-mark.svg`
- Optional full logo SVG: `site/assets/ihlab-logo.svg` (replace when master logo lands)
- Copy source: `../homepage-copy-v1.md` (superseded by v3 copy in `index.html`)
- Brand reference PNG: `../IHLab_Brand_Reference_Final2.png` (v3 diverges: light hero + forest)

**Local preview**
```bash
python3 -m http.server 8770 --directory /workspace/ihlab/site --bind 127.0.0.1
```
Open http://localhost:8770/

---

## Brand tokens (v3)

| Token | Hex | Use |
|-------|-----|-----|
| Forest (`--navy`) | `#1F3328` | Primary text, dark panels, quote/partners bands, logo mark |
| Sage | `#556248` | Restrained accents, muted labels on light, secondary emphasis |
| Ivory | `#F0EEE0` | Page background, **hero**, light section bands |
| Gold | `#A8842B` | **Primary CTAs and key links only**; gold small-caps section labels |
| Coral | `#C86A4F` | **Badges / tags only** |

Do **not** use gold for large fills, nav text, or body links except CTAs. Do **not** use coral for buttons.

### Typography (Google Fonts)
- **Headlines / display:** Source Serif 4 — Medium / SemiBold / Italic
- **Body, nav, UI, buttons:** Work Sans — Regular / Medium / SemiBold
- **Labels:** Source Serif 4 Medium, uppercase / small-caps feel, wide tracking (~0.2em), **gold**
- **Taglines / quotes:** Source Serif 4 Italic

### Logo
- Organ-pipe mark: **9 ascending tapered bars**, forest/navy only (no gold in the mark)
- Wordmark: Investable Humanity / Leadership Lab with a thin rule and small diamond between lines

### Guide pattern (v3)
- **Light hero:** ivory bg + coral pill + forest serif headline + muted body + gold CTA + ghost secondary
- **Dark bands:** forest bg + ivory type + gold labels (quote, partners, partner panel)

---

## Section map (matches `index.html` v3)

1. **Sticky nav** — mark + wordmark · Why · The Lab · Partners · Attend · Partner with us (gold CTA)
2. **Hero** — ivory · coral “Founding Cohort” badge · forest headline · muted lede · gold + ghost CTAs · proof strip
3. **Why** (`#why`, ivory) — Why now · three moves · support roundtable photo
4. **Human split** (ivory) — listening photo · “In the room”
5. **Quote band** (forest) — “The earliest investment…”
6. **The Lab** (`#lab`, ivory) — lounge support photo · stats · Nov 3 Shriver callout (coral badge on forest inset)
7. **Sampler** (`#sampler`, ivory) — three partner cards
8. **Collaborating Partners** (`#partners`, forest) — never “Founding Partners” · “Independent initiative. Shared table.”
9. **Why attend** (`#attend`, ivory) — outcomes · interest form (mailto Alyssa)
10. **Partner** (`#partner`, ivory shell + forest panel) — partnership form (mailto Alyssa)
11. **Footer** — contact · legal line · Unsplash credit

---

## Voice & framing rules (do not regress)

- Tone: **confident, generous, collaborative, knowledgeable**; specific over platitudes
- Independent initiative; **Collaborating Partners** = UAC, TOSLI, Dignity.Us (never “Founding Partners”)
- No People Pitch / UAC trifecta Voice pillar on this page
- No founder hero on the homepage
- No UAC tagline
- No tax-deductible / donate language (partner copy may say tax treatment is confirmed per partner)
- No em dashes; avoid “not X, it’s Y”
- Keep story claims: Utah cohort, 50 leaders, 8 sessions, $2,500, partners, mailto Alyssa

---

## CTAs & forms

| CTA | Target |
|-----|--------|
| Request a seat | `#attend` → mailto `alyssa@ihlab.us` |
| Partner with us | `#partner` → mailto `alyssa@ihlab.us` |

---

## Hostinger / designer edit guide

**If staying on static HTML:** edit `index.html` CSS variables:
```css
:root {
  --navy: #1F3328; /* deep forest */
  --sage: #556248;
  --ivory: #F0EEE0;
  --gold: #A8842B;
  --coral: #C86A4F;
}
```

**Locked vs editable**
| Locked (ask first) | Freely editable |
|--------------------|-----------------|
| Color roles (gold = CTA/labels only, coral = badge only) | Body copy length / line breaks |
| Partner naming (“Collaborating Partners”) | Photography / optional imagery |
| Independent-initiative framing; no People Pitch | Spacing, section order polish |
| Font pairing | Button labels if CTAs stay equivalent |
| Forest deep `#1F3328` + ivory hero | |

---

## SEO / meta already set

- Title: Investable Humanity Leadership Lab · IHLab
- Description: fifty Utah leaders, eight sessions, UAC / TOSLI / Dignity.Us
- Favicon: `assets/ihlab-mark.svg`
- Theme color: forest `#1F3328`

---

## Checklist before Alyssa share

- [ ] Open on phone + desktop
- [ ] Hero reads as light ivory landing (not dark navy first paint)
- [ ] Ghost CTA readable on ivory
- [ ] Both CTAs scroll to the right sections
- [ ] No People Pitch nav / section / footer mention
- [ ] Mailto opens with a sensible subject
- [ ] Partners labeled Collaborating Partners
- [ ] Nov 3 callout visible on The Lab section
- [ ] Gold hex is `#A8842B`; forest deep is `#1F3328`
