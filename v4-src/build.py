#!/usr/bin/env python3
"""Builds the static v4 preview into ../v4/. Edit copy here, then run: python3 v4-src/build.py"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent / "v4"
LUMA = "https://luma.com/up0d529v"
CONTACT = "alyssa.dehart@utahadvocacycoalition.org"

def mailto(subject):
    from urllib.parse import quote
    return f"mailto:{CONTACT}?subject={quote(subject)}"

def head(P, title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex, nofollow" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#1C3538" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,500;0,600;1,500;1,600&family=Work+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="icon" href="{P}assets/ihlab-mark.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="{P}assets/base.css" />
  <link rel="stylesheet" href="{P}assets/v4.css" />
</head>
<body>
"""

def brand(P):
    return f"""<a class="brand" href="{P}" aria-label="IHLab home">
        <img class="brand-mark" src="{P}assets/ihlab-mark.svg" width="42" height="28" alt="" />
        <span class="brand-text">
          <span class="top">Investable Humanity</span>
          <span class="brand-rule" aria-hidden="true"><span class="diamond"></span></span>
          <span class="bottom">Leadership Lab</span>
        </span>
      </a>"""

def nav(P, current=""):
    def cur(k): return ' aria-current="page"' if k == current else ""
    launch = "#launch" if current == "home" else f"{P}#launch"
    return f"""  <header class="nav">
    <div class="wrap nav-inner">
      {brand(P)}
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" id="nav-toggle">Menu</button>
      <ul class="nav-links" id="nav-menu">
        <li><a href="{launch}">Launch</a></li>
        <li><a href="{P}lab/"{cur('lab')}>Cohort</a></li>
        <li><a href="{P}give/"{cur('give')}>Give</a></li>
        <li><a href="{P}about/"{cur('about')}>About</a></li>
        <li><a class="nav-cta" href="{LUMA}" target="_blank" rel="noopener">Request your seat</a></li>
      </ul>
    </div>
  </header>
"""

def footer(P, mobile_cta):
    return f"""  <footer class="footer">
    <div class="wrap">
      {brand(P)}
      <ul class="footer-nav">
        <li><a href="{P}#launch">Launch</a></li>
        <li><a href="{P}lab/">Cohort</a></li>
        <li><a href="{P}give/">Give</a></li>
        <li><a href="{P}about/">About</a></li>
        <li><a href="#join">Join the list</a></li>
        <li><a href="{LUMA}" target="_blank" rel="noopener">Request your seat</a></li>
      </ul>
      <div class="footer-meta">
        <div><a href="mailto:{CONTACT}">{CONTACT}</a></div>
        <div>© <span id="year">2026</span> Investable Humanity Leadership Lab</div>
      </div>
      <p class="footer-legal">An independent initiative · In collaboration with Utah Advocacy Coalition, The Other Side Leadership Institute, and Dignity.Us</p>
      <p class="photo-credit">Photos via Unsplash (stock placeholders until IHLab shoot).</p>
    </div>
  </footer>
{mobile_cta}
  <script src="{P}assets/site.js" defer></script>
</body>
</html>
"""

def mobile_cta(text_b, text_s, label, href, external=False):
    ext = ' target="_blank" rel="noopener"' if external else ""
    return f"""  <div class="mobile-cta" aria-hidden="false">
    <span class="mc-text"><b>{text_b}</b>{text_s}</span>
    <a class="btn btn-primary" href="{href}"{ext}>{label}</a>
  </div>"""

# Speaker names/titles match Alyssa's official event poster & invitation (IHLL_Event_Poster.pdf).
SPEAKER_LIST = [
    ("timothy-shriver", "Keynote", "Dr. Timothy Shriver", ["University of Utah Impact Scholar", "Co-Founder &amp; CEO, Dignity.Us"]),
    ("jody-olsen", "Featured speaker", "Dr. Jody Olsen", ["Former Director, Peace Corps", "UAC Advisory Board"]),
    ("preston-cochrane", "Featured speaker", "Preston Cochrane", ["CEO, The Other Side Village"]),
]

def speakers(P):
    out = ['<ul class="speakers">']
    for slug, role, name, lines in SPEAKER_LIST:
        src = f"{P}assets/speakers/{slug}"
        title = "".join(f"<span>{l}</span>" for l in lines)
        out.append(f"""            <li class="speaker">
              <img class="speaker-photo" src="{src}-360.jpg" srcset="{src}-360.jpg 360w, {src}.jpg 640w" sizes="(max-width: 639px) 76px, (max-width: 939px) 104px, 144px" width="360" height="360" alt="Headshot of {name}" loading="lazy" decoding="async" />
              <span class="role-tag">{role}</span>
              <h3>{name}</h3>
              <p class="speaker-title">{title}</p>
            </li>""")
    out.append("          </ul>")
    return "\n".join(out)

SCARCITY_LAUNCH = """<div class="scarcity" role="note" aria-label="Limited seating">
            <span class="badge">Limited seating</span>
            <p class="primary">Seating in the Founder’s Room is strictly limited to 100 leaders to ensure high-impact networking and dialog. Seats are expected to fill quickly.</p>
            <p class="supporting">Seating is limited and by approval. The first leaders will shape what it becomes, and many of them are meeting at this table. If you're not there, you'll hear about it from someone who was.</p>
          </div>"""

SNAPSHOT = f"""<aside class="snapshot" aria-label="Event snapshot">
          <p class="snap-title">Event snapshot</p>
          <dl>
            <div class="row"><dt>Date &amp; time</dt><dd>November 3, 2026<small>11:00 AM – 1:00 PM MT</small></dd></div>
            <div class="row"><dt>Location</dt><dd>Zions Bank Founder’s Room, 18th Floor<small>One South Main Street, Salt Lake City, UT 84133</small></dd></div>
            <div class="row"><dt>Format</dt><dd>Lunch · Keynote · Panel Discussion</dd></div>
          </dl>
          <a class="btn btn-primary btn-lg" href="{LUMA}" target="_blank" rel="noopener">Request your seat <span class="arrow" aria-hidden="true">→</span></a>
          <p class="fine">Opens registration on Luma</p>
        </aside>"""

GAINS = """<ul class="gains">
            <li><strong>A practice for hard conversations.</strong> Implement the <em>Dignity Index</em> framework to turn conflict into clarity. Navigate a tense boardroom, community resistance, or team misalignment without losing relationships and trust.</li>
            <li><strong>Capital and mission alignment.</strong> Learn to structure operations so every dollar directly expands your operational capacity and community yield.</li>
            <li><strong>A cabinet of peers who know you and your work.</strong> Working alongside 50 executive leaders and IHLab Dignity Fellows who learn your organization and stay in your corner.</li>
            <li><strong>A playbook for your organization.</strong> Jumpstart planning for immediate 3&#8209;year growth with practical tools you can use on Monday.</li>
            <li><strong>A view around the corner.</strong> Alumni of IHLab have the opportunity to bring a full partner program inside their organization.</li>
          </ul>"""

COHORT_SCARCITY = """<div class="scarcity" role="note" aria-label="One founding cohort">
              <span class="badge">One founding cohort</span>
              <p class="primary">Fifty seats, one founding cohort, and no second chance to be a founder.</p>
              <p class="supporting">Seats open this December. Those who save a seat and join the list are there when the gates open!</p>
            </div>"""

TIERS = [
    ("$2,500", "Scholarship Seat", "Fully funds one leader's place in the 2027 Founding Cohort.", False),
    ("$10,000", "Cohort Partner", "Underwrites a full peer table of leaders &amp; gains advisory seat access during cohort working sessions.", True),
    ("$25,000", "Founding Partner", "Helps shape Cohort I at the strategic rollout of the IHLab model with Utah's consequential leaders.", False),
]

def tiers(with_buttons):
    out = ['<div class="tiers">']
    for amt, name, does, feat in TIERS:
        btn = ""
        if with_buttons:
            plain = name
            btn = f'<a class="btn btn-primary" href="{mailto(f"IHLab gift: {plain} ({amt})")}">Give {amt}</a>'
        else:
            btn = '<span class="spacer"></span>'
        out.append(f"""          <article class="tier{' featured' if feat else ''}">
            <div class="amount">{amt}</div>
            <h3 class="tier-name">{name}</h3>
            <p class="does-label">What your gift does</p>
            <p>{does}</p>
            {btn}
          </article>""")
    out.append("        </div>")
    return "\n".join(out)

TAX_LINE = "<strong>Your gift is tax-deductible</strong>, and its impact multiplies: one leader, one organization, limitless communities and every individual that organization serves."

ORGS = [
    ("Convener &amp; Strategy Hub", "Utah Advocacy Coalition", "UAC", "Convenes leaders in policy, advocacy, and state-wide civic initiatives to keep momentum moving. Through this experience, UAC is the driver to keep each IHLab cohort progressing between sessions.", "https://utahadvocacy.org", "utahadvocacy.org"),
    ("Experiential Civic Leadership", "The Other Side Leadership Institute", "TOSLI", "The Other Side Leadership Institute teaches civic leadership grounded in lived experience at The Other Side Village, bringing radical accountability and operational discipline.", "https://theothersidevillage.com/the-other-side-leadership-institute/", "theothersidevillage.com"),
    ("Communication &amp; Cultural Frameworks", "Dignity.Us", "", "Dignity.Us deploys the Dignity Index into the room: less contempt, better conversation, even when the stakes are high.", "https://dignity.us", "dignity.us"),
]

def trio(links):
    out = ['<ul class="trio">']
    for role, name, abbr, desc, url, label in ORGS:
        small = f"<small>{abbr}</small>" if abbr else ""
        link = f'<a class="org-link" href="{url}" target="_blank" rel="noopener noreferrer">Visit {label} ↗</a>' if links else ""
        out.append(f"""          <li class="org">
            <p class="org-role">{role}</p>
            <h3>{name}{small}</h3>
            <p>{desc}</p>
            {link}
          </li>""")
    out.append("        </ul>")
    return "\n".join(out)

ROLES = ["Nonprofit leader", "Board member", "Funder", "Just curious"]

def join(header="Be first to know.", sub=None, preselect=None, kicker=None):
    sub = sub or "Get launch updates, executive insights, dignity-index tools, and priority notifications when Cohort I applications open in December 2026."
    chips = "\n".join(
        f'<label class="chip"><input type="radio" name="role" value="{r}"{" checked" if r == preselect else ""} required /><span>{r}</span></label>'
        for r in ROLES)
    k = f'<p class="section-label">{kicker}</p>' if kicker else ""
    return f"""    <section id="join" class="band-ivory join-panel">
      <div class="wrap">
        <div class="panel">
          <div class="panel-grid">
            <div>
              {k}
              <h2>{header}</h2>
              <p class="lede">{sub}</p>
            </div>
            <form class="form join-form" novalidate>
              <label>First &amp; last name
                <input type="text" name="name" required autocomplete="name" />
              </label>
              <label>Email
                <input type="email" name="email" required autocomplete="email" />
              </label>
              <fieldset class="role-group">
                <legend>I'm a…</legend>
                <div class="chips">
                {chips}
                </div>
              </fieldset>
              <button class="btn btn-primary btn-lg" type="submit">Join the list <span class="arrow" aria-hidden="true">→</span></button>
              <p class="micro">No spam. Just the launch, the cohort, relevant learnings, and the opportunities to be part of IHLab.</p>
              <p class="form-status" aria-live="polite"></p>
            </form>
          </div>
        </div>
      </div>
    </section>
"""

def page_hero(P, crumb, badge, eyebrow, h1, lede, actions):
    b = f'<span class="badge">{badge}</span>' if badge else ""
    e = f'<p class="hero-eyebrow">{eyebrow}</p>' if eyebrow else ""
    return f"""    <section class="page-hero">
      <div class="wrap">
        <p class="crumbs"><a href="{P}">Home</a> / {crumb}</p>
        <div class="hero-kicker">{b}{e}</div>
        <h1>{h1}</h1>
        <p class="lede">{lede}</p>
        <div class="cta-row">{actions}</div>
      </div>
    </section>
"""

# ------------------------------------------------------------------ HOME
def home():
    P = ""
    h = head(P, "Investable Humanity Leadership Lab · IHLab", "Utah has the heart. Now it needs the people and playbook to scale it. Join the IHLab launch on November 3, 2026 in Salt Lake City.")
    h += nav(P, "home")
    h += f"""  <main id="top">
    <section class="hero" aria-label="Introduction">
      <div class="wrap">
        <div class="hero-kicker">
          <span class="badge">Founding Cohort 2027 · Salt Lake City</span>
          <p class="hero-eyebrow">Bridging the Divide in Community Impact</p>
        </div>
        <h1>Utah has the heart. <span class="line2">Now it needs the people and playbook to scale it.</span></h1>
        <p class="lede">Utah's funders, founders, and nonprofit leaders care deeply, but they rarely get to learn alongside each other in a way that brings the best parts together. The Investable Humanity Leadership Lab brings fifty leaders into one room to master dignity-centered conflict resolution, align capital with mission, and lead organizations that turn good intentions into lasting change.</p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="{LUMA}" target="_blank" rel="noopener">Request your seat <span class="arrow" aria-hidden="true">→</span></a>
        </div>
        <div class="cred-bar">
          <p class="cred-orgs"><span class="cred-label">Built by</span><span>The Other Side Leadership Institute</span><span class="dot" aria-hidden="true">·</span><span>Dignity.Us</span><span class="dot" aria-hidden="true">·</span><span>Utah Advocacy Coalition</span></p>
          <a class="keynote-callout" href="#launch">
            <span class="k-date"><b>3</b><span>Nov</span></span>
            <span>Launching with keynote <strong>Dr. Timothy Shriver</strong>, Co-Founder &amp; CEO of Dignity.Us</span>
          </a>
        </div>
      </div>
    </section>

    <section id="launch" class="band-ivory">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">November 3, 2026 · Salt Lake City</p>
          <h2>Be in the room where it all begins.</h2>
          <p class="lede">The Investable Humanity Leadership Lab launches over lunch with the people shaping how Utah leads. Join fellow civic pioneers, funders, and executive directors to hear it first, meet the minds behind the magic, and see why this cohort is the one to be part of.</p>
        </div>
        <p class="speakers-label">Featured speakers</p>
        {speakers(P)}
        <div class="launch-grid">
          {SCARCITY_LAUNCH}
          {SNAPSHOT}
        </div>
      </div>
    </section>

    <section id="cohort" class="band-paper">
      <div class="wrap">
        <div class="cohort-grid">
          <div>
            <p class="section-label">For the leaders carrying the mission</p>
            <h2>You've carried the mission. Now build the leadership that transforms your organization.</h2>
            <div class="body-copy">
              <p>Your determination and passion got you here, oftentimes on a road less traveled, alone. And now you've outgrown the advice that got you here. The next stage of leading your organization takes sharper judgment under pressure, a stronger board, and a team who understands the weight of what you do.</p>
              <p class="strong">The IHLab Founding Cohort is an intensive, 8-session leadership incubator designed to give you the exact playbook, frameworks, and robust peer network required to lead your organization to its next evolution.</p>
            </div>
            <h3 class="gain-title">What You Gain</h3>
            {GAINS}
          </div>
          <aside class="snap-card" aria-label="Cohort snapshot">
            <figure class="snap-media"><img src="assets/photos/table-dialogue.jpg" alt="Peers in focused dialogue around a shared table" width="1400" height="933" loading="lazy" decoding="async" /></figure>
            <p class="snap-title">Cohort snapshot</p>
            <dl class="stats">
              <div class="stat"><dt>What</dt><dd>8 biweekly master sessions, 3.5 hours each</dd></div>
              <div class="stat"><dt>Where</dt><dd>The Other Side Village, Salt Lake City, UT</dd></div>
              <div class="stat"><dt>Who</dt><dd>Capped at 50 leaders</dd></div>
              <div class="stat"><dt>When</dt><dd>Early 2027 (applications open December 2026)</dd></div>
              <div class="stat"><dt>How much</dt><dd>$2,500 per participant</dd></div>
            </dl>
            <a class="btn btn-primary btn-lg" href="lab/">Save my spot <span class="arrow" aria-hidden="true">→</span></a>
            {COHORT_SCARCITY}
          </aside>
        </div>
      </div>
    </section>

    <section id="give" class="band-navy">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">For those who’ve always wanted to move the mission forward</p>
          <h2>Fund the leader who's ready to shape the future, and just needs the seat.</h2>
          <p class="lede">Utah's most promising frontline leaders are ready but have the tightest budget and can't afford the cost. A single gift changes that. By sponsoring a leader or backing the IHLab initiative, you directly fund the tools that strengthen a leader and their whole organization, sending them back to the community with more capacity to serve.</p>
        </div>
        <p class="speakers-label" style="color:var(--ivory);">Specific ways to give</p>
        {tiers(False)}
        <p class="give-note">{TAX_LINE}</p>
        <div class="cta-row"><a class="btn btn-primary btn-lg" href="give/">Give today <span class="arrow" aria-hidden="true">→</span></a></div>
      </div>
    </section>

    <section id="coalition" class="band-ivory">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">Three organizations. Decades of experience. One table.</p>
          <h2>Advocacy, lived experience, and dignity: all under one roof.</h2>
          <p class="lede">Investable Humanity is born from a unified vision to combine policy advocacy, lived-experience leadership, and dignity-centered communication into a single, high-impact leadership experience.</p>
        </div>
        {trio(False)}
        <p class="coalition-close">Each has its own mission and track record. Together, they give Utah's leaders something none could offer alone.</p>
        <div class="cta-row"><a class="btn btn-ghost" href="about/">Meet the organizations <span class="arrow" aria-hidden="true">→</span></a></div>
      </div>
    </section>

{join()}  </main>
"""
    h += footer(P, mobile_cta("Nov 3 · Launch luncheon", "Limited to 100 leaders", "Request your seat", LUMA, True))
    return h

# ------------------------------------------------------------------ LAB
def lab():
    P = "../"
    h = head(P, "The Founding Cohort · IHLab", "The IHLab Founding Cohort: 8 biweekly master sessions at The Other Side Village for 50 Utah nonprofit leaders, board members, and funders. Applications open December 2026.")
    h += nav(P, "lab")
    h += page_hero(P, "The Cohort", "Founding Cohort 2027", "For the leaders carrying the mission",
        "You've carried the mission. Now build the leadership that transforms your organization.",
        "The IHLab Founding Cohort is an intensive, 8-session leadership incubator designed to give you the exact playbook, frameworks, and robust peer network required to lead your organization to its next evolution.",
        f'<a class="btn btn-primary btn-lg" href="#join">Join the list <span class="arrow" aria-hidden="true">→</span></a><a class="btn btn-ghost btn-on-dark" href="#investment">See the details</a>')
    h += f"""  <main>
    <section id="why" class="band-ivory">
      <div class="wrap">
        <div class="two-col">
          <div>
            <p class="section-label">Why</p>
            <h2>Utah's generosity is outpacing its shared leadership skills.</h2>
          </div>
          <div class="body-copy">
            <p>Utah's funders, founders, and nonprofit leaders care deeply, but they rarely get to learn alongside each other in a way that brings the best parts together.</p>
            <p>Your determination and passion got you here, oftentimes on a road less traveled, alone. And now you've outgrown the advice that got you here. The next stage of leading your organization takes sharper judgment under pressure, a stronger board, and a team who understands the weight of what you do.</p>
            <p class="strong">What's at stake when leaders learn alone: the hard conversation that costs a relationship, the dollar that never builds capacity, the board that never quite aligns.</p>
          </div>
        </div>
        <figure class="support-photo"><img src="../assets/photos/coffee-talk.jpg" alt="Diverse colleagues collaborating around a shared table" width="1600" height="1067" loading="lazy" decoding="async" /></figure>
      </div>
    </section>

    <section id="who" class="band-paper">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">Who it's for</p>
          <h2>Nonprofit executives, board members, and the funders and executives who stand beside them.</h2>
          <p class="lede">The Founding Cohort is capped at 50 leaders.</p>
        </div>
        <p class="speakers-label">This is for you if…</p>
        <ul class="for-you">
          <li>You lead a nonprofit as an executive director or founder, and you've outgrown the advice that got you here.</li>
          <li>You serve on a board and want it to be stronger.</li>
          <li>You fund or advise nonprofit leaders and want to learn alongside them.</li>
          <li>A tense boardroom, community resistance, or team misalignment is costing you relationships and trust.</li>
          <li>You want every dollar to expand your operational capacity and community yield.</li>
          <li>You want a cabinet of peers who know you and your work.</li>
        </ul>
      </div>
    </section>

    <section id="what" class="band-ivory">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">What you'll practice</p>
          <h2>Three moves.</h2>
        </div>
        <ol class="moves" style="margin-top:0;">
          <li><div class="num">01</div><strong>See people as worth investing in.</strong><p>Fund and manage as partners, not as cases.</p></li>
          <li><div class="num">02</div><strong>Lead with dignity when conflict is costly.</strong><p>Use the Dignity Index in the room where it matters.</p></li>
          <li><div class="num">03</div><strong>Align money, people, and mission.</strong><p>So care builds capacity inside your organization.</p></li>
        </ol>
        <h3 class="gain-title">What You Gain</h3>
        <div style="max-width:46rem;">{GAINS}</div>
      </div>
    </section>

    <section id="how" class="band-paper">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">How it works</p>
          <h2>A focused talk, then table work.</h2>
        </div>
        <div class="how-grid">
          <div class="how"><h3>Session format</h3><p>Each 3.5-hour master session opens with a focused talk, then moves into table work on your own organization.</p></div>
          <div class="how"><h3>Peer tables</h3><p>Work alongside 50 executive leaders, with peers who learn your organization and stay in your corner.</p></div>
          <div class="how"><h3>Dignity Fellows</h3><p>IHLab Dignity Fellows join the table work, learn your organization, and bring the Dignity Index into the conversation.</p></div>
          <div class="how"><h3>The playbook</h3><p>Jumpstart planning for immediate 3&#8209;year growth with practical tools you can use on Monday.</p></div>
        </div>
      </div>
    </section>

    <section id="investment" class="band-ivory">
      <div class="wrap">
        <div class="two-col">
          <div>
            <p class="section-label">When &amp; where</p>
            <h2>Early 2027 at The Other Side Village.</h2>
            <dl class="stats">
              <div class="stat"><dt>Sessions</dt><dd>8 biweekly master sessions, 3.5 hours each</dd></div>
              <div class="stat"><dt>Venue</dt><dd>The Other Side Village, Salt Lake City, UT</dd></div>
              <div class="stat"><dt>Starts</dt><dd>Early 2027 (session dates to be announced)</dd></div>
              <div class="stat"><dt>Applications</dt><dd>Seats open December 2026</dd></div>
              <div class="stat"><dt>Cohort size</dt><dd>Capped at 50 leaders</dd></div>
            </dl>
          </div>
          <div class="contact-card">
            <p class="section-label">Investment</p>
            <p class="price">$2,500</p>
            <p class="price-sub">per participant</p>
            <ul class="inc">
              <li>8 biweekly master sessions, 3.5 hours each</li>
              <li>A seat at a peer table with IHLab Dignity Fellows</li>
              <li>Dignity Index practice for hard conversations</li>
              <li>Practical tools and a playbook for your organization</li>
            </ul>
            <p><strong>Scholarships.</strong> Donors can fully fund a leader's place through a $2,500 Scholarship Seat. <a href="{mailto('IHLab scholarship seat inquiry')}">Ask us about scholarship availability</a>.</p>
            <a class="btn btn-primary" href="#join">Join the list <span class="arrow" aria-hidden="true">→</span></a>
          </div>
        </div>
      </div>
    </section>

    <section id="after" class="band-navy">
      <div class="wrap">
        <div class="section-head" style="margin-bottom:0;">
          <p class="section-label">After the cohort</p>
          <h2>A view around the corner.</h2>
          <p class="lede">Alumni of IHLab have the opportunity to bring a full partner program inside their organization: Dignity.Us, Trauma-Informed Utah, or another lab that fits.</p>
        </div>
      </div>
    </section>

    <section id="faq" class="band-ivory">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">FAQ</p>
          <h2>Questions, answered.</h2>
        </div>
        <div class="faq">
          <details open><summary>Who is the Founding Cohort for?</summary><p>Nonprofit executives, founders, and board members, plus the funders and executives who stand beside them. The cohort is capped at 50 leaders.</p></details>
          <details><summary>When do applications open?</summary><p>December 2026. Join the list and you'll be among the first to know when the gates open.</p></details>
          <details><summary>When and where does the cohort meet?</summary><p>Early 2027 at The Other Side Village in Salt Lake City: 8 biweekly master sessions, 3.5 hours each. Session dates will be shared with the cohort.</p></details>
          <details><summary>What does it cost?</summary><p>$2,500 per participant. Donors can fully fund a leader's seat through a Scholarship Seat, so ask us about scholarship availability.</p></details>
          <details><summary>How is the November 3 launch related to the cohort?</summary><p>The launch luncheon on November 3, 2026 at the Zions Bank Founder’s Room introduces the Lab, with keynote Dr. Timothy Shriver. Cohort sessions begin in early 2027. <a href="{LUMA}" target="_blank" rel="noopener">Request your seat at the launch</a>.</p></details>
          <details><summary>Who is behind IHLab?</summary><p>Utah Advocacy Coalition, The Other Side Leadership Institute, and Dignity.Us. <a href="../about/">Meet the organizations</a>.</p></details>
          <details><summary>What happens after the cohort?</summary><p>Alumni have the opportunity to bring a full partner program inside their organization, such as Dignity.Us, Trauma-Informed Utah, or another lab that fits.</p></details>
        </div>
      </div>
    </section>

    <section class="band-paper" style="padding-bottom:0;">
      <div class="wrap">
        {COHORT_SCARCITY.replace('class="scarcity"', 'class="scarcity" style="margin-top:0;"')}
      </div>
    </section>
{join("Join the list now. Apply in December.", preselect="Nonprofit leader")}  </main>
"""
    h += footer(P, mobile_cta("Founding Cohort 2027", "Applications open December", "Join the list", "#join"))
    return h

# ------------------------------------------------------------------ GIVE
def give():
    P = "../"
    h = head(P, "Give · IHLab", "Fund a leader's seat in the IHLab 2027 Founding Cohort: Scholarship Seat $2,500, Cohort Partner $10,000, Founding Partner $25,000.")
    h += nav(P, "give")
    h += page_hero(P, "Give", None, "For those who’ve always wanted to move the mission forward",
        "Fund the leader who's ready to shape the future, and just needs the seat.",
        "Utah's most promising frontline leaders are ready but have the tightest budget and can't afford the cost. A single gift changes that. By sponsoring a leader or backing the IHLab initiative, you directly fund the tools that strengthen a leader and their whole organization, sending them back to the community with more capacity to serve.",
        f'<a class="btn btn-primary btn-lg" href="#tiers">Choose your gift <span class="arrow" aria-hidden="true">→</span></a><a class="btn btn-ghost btn-on-dark" href="{mailto("IHLab: larger gift conversation")}">Talk to us about a larger gift</a>')
    h += f"""  <main>
    <section id="tiers" class="band-ivory">
      <div class="wrap">
        <div class="section-head" style="margin-bottom:0;">
          <p class="section-label">Choose your gift</p>
          <h2>Specific Ways to Give</h2>
        </div>
        {tiers(True)}
        <p class="give-note" style="color:var(--muted);">{TAX_LINE.replace('<strong>', '<strong style="color:var(--navy);">')}</p>
      </div>
    </section>

    <section id="how-to-give" class="band-paper">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">Payment or pledge</p>
          <h2>How to give</h2>
        </div>
        <ol class="steps">
          <li><strong>Choose your gift</strong><p>Pick a Scholarship Seat, Cohort Partner, or Founding Partner gift above.</p></li>
          <li><strong>Give or pledge</strong><p>Tap your gift's button to reach us by email and let us know whether you'd like to give now or pledge.</p></li>
          <li><strong>We follow up</strong><p>We reply with payment details and the next steps for your gift.</p></li>
        </ol>
        <div class="placeholder" style="margin-top:2rem;">
          <span class="ph-tag">Placeholder · Payment path</span>
          <p>No payment processor is connected yet. Every "Give" button currently opens an email to {CONTACT} with the tier in the subject line. Swap in the online give / pledge form when it's ready.</p>
        </div>
        <div class="placeholder" style="margin-top:1rem;">
          <span class="ph-tag">Placeholder · Tax receipt &amp; EIN</span>
          <p>Tax receipt process, legal entity name, and EIN go here once IHLab's giving entity is confirmed. Not yet provided.</p>
        </div>
      </div>
    </section>

    <section id="larger-gifts" class="band-ivory">
      <div class="wrap">
        <div class="two-col">
          <div class="contact-card">
            <p class="section-label">Larger gifts</p>
            <h3>Talk to us about a larger gift</h3>
            <p>Thinking beyond these tiers, or want to talk through what fits? Reach out directly.</p>
            <p style="margin-bottom:1.25rem;"><strong>Alyssa DeHart</strong><br />Utah Advocacy Coalition<br /><a href="mailto:{CONTACT}">{CONTACT}</a></p>
            <a class="btn btn-primary" href="{mailto("IHLab: larger gift conversation")}">Email Alyssa <span class="arrow" aria-hidden="true">→</span></a>
          </div>
          <div class="placeholder">
            <span class="ph-tag">Placeholder · Leader quote</span>
            <p><strong>A short story or quote from a leader a gift would reach.</strong></p>
            <p>To be supplied by IHLab: a real, approved quote with name, title, and organization (and permission to publish). Nothing has been written here on purpose.</p>
          </div>
        </div>
      </div>
    </section>

{join(preselect="Funder")}  </main>
"""
    h += footer(P, mobile_cta("Fund a leader's seat", "Scholarship Seat · $2,500", "Give", "#tiers"))
    return h

# ------------------------------------------------------------------ ABOUT
def about():
    P = "../"
    h = head(P, "About the Coalition · IHLab", "Investable Humanity Leadership Lab brings together Utah Advocacy Coalition, The Other Side Leadership Institute, and Dignity.Us.")
    h += nav(P, "about")
    h += page_hero(P, "About", None, "Three organizations. Decades of experience. One table.",
        "Advocacy, lived experience, and dignity: all under one roof.",
        "Investable Humanity is born from a unified vision to combine policy advocacy, lived-experience leadership, and dignity-centered communication into a single, high-impact leadership experience.",
        f'<a class="btn btn-primary btn-lg" href="{LUMA}" target="_blank" rel="noopener">Request your seat <span class="arrow" aria-hidden="true">→</span></a><a class="btn btn-ghost btn-on-dark" href="../lab/">Explore the cohort</a>')
    h += f"""  <main>
    <section id="coalition" class="band-ivory">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">The coalition</p>
          <h2>Each has its own mission and track record.</h2>
          <p class="lede">Together, they give Utah's leaders something none could offer alone.</p>
        </div>
        {trio(True)}
      </div>
    </section>

    <section id="together" class="band-paper">
      <div class="wrap">
        <div class="split">
          <figure class="split-media"><img src="../assets/photos/lounge-diverse.jpg" alt="Workshop group collaborating with shared notes and dialogue" width="1600" height="1067" loading="lazy" decoding="async" /></figure>
          <div class="split-copy">
            <p class="section-label">How it comes together</p>
            <p class="human-line">One cohort. Three partners in the room.</p>
            <p>Each session draws on what Utah Advocacy Coalition, The Other Side Leadership Institute, and Dignity.Us already teach well, so you can feel the difference and decide what belongs inside your organization next.</p>
            <ol class="moves" style="grid-template-columns:1fr;gap:1.1rem;margin-top:1.75rem;">
              <li><div class="num">Between sessions</div><p>UAC keeps each IHLab cohort progressing.</p></li>
              <li><div class="num">In the room</div><p>Sessions meet at The Other Side Village, where TOSLI teaches civic leadership grounded in lived experience.</p></li>
              <li><div class="num">In every conversation</div><p>Dignity.Us brings the Dignity Index: less contempt, better conversation.</p></li>
            </ol>
          </div>
        </div>
      </div>
    </section>

    <section id="speakers" class="band-ivory">
      <div class="wrap">
        <div class="section-head">
          <p class="section-label">November 3, 2026 · Salt Lake City</p>
          <h2>Be in the room where it all begins.</h2>
          <p class="lede">Leaders from across the coalition open the Lab over lunch at the Zions Bank Founder’s Room.</p>
        </div>
        {speakers(P)}
        <div class="cta-row"><a class="btn btn-primary btn-lg" href="{LUMA}" target="_blank" rel="noopener">Request your seat <span class="arrow" aria-hidden="true">→</span></a><span style="color:var(--muted);font-size:0.95rem;">Strictly limited to 100 leaders.</span></div>
      </div>
    </section>

    <section id="contact" class="band-paper">
      <div class="wrap">
        <div class="contact-card" style="max-width:40rem;">
          <p class="section-label">Contact</p>
          <h3>Questions about IHLab?</h3>
          <p>Reach Alyssa DeHart at Utah Advocacy Coalition.</p>
          <a class="btn btn-ghost" href="{mailto('IHLab question')}">{CONTACT}</a>
        </div>
      </div>
    </section>

{join()}  </main>
"""
    h += footer(P, mobile_cta("Nov 3 · Launch luncheon", "Limited to 100 leaders", "Request your seat", LUMA, True))
    return h

import re as _re
def smart(html):
    """Curly apostrophes in visible text only (skips tags, attributes, scripts)."""
    parts = _re.split(r"(<script.*?</script>|<[^>]+>)", html, flags=_re.S)
    return "".join(x if x.startswith("<") else _re.sub(r"(?<=\w)'(?=\w)", "\u2019", x) for x in parts)

for path, fn in [("index.html", home), ("lab/index.html", lab), ("give/index.html", give), ("about/index.html", about)]:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(smart(fn()))
(ROOT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
(ROOT / "vercel.json").write_text('''{
  "headers": [
    { "source": "/(.*)", "headers": [
      { "key": "X-Robots-Tag", "value": "noindex, nofollow, noarchive, noimageindex" },
      { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
      { "key": "X-Content-Type-Options", "value": "nosniff" }
    ]}
  ]
}
''')
print("built", ROOT)
