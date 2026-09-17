"""Build the 4 remaining capacitor-film sub-pages in Editorial style (matching ultra-thin.html)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "capacitor-films")

PAGES = [
    {
        "slug": "standard",
        "title": "Standard BOPP Capacitor Film 5–8μm | Haibin Film",
        "desc": "BOPP capacitor film 5.0 / 6.0 / 8.0 μm for power capacitors, lighting ballasts, motor-run, induction heating. Specs, TDS, free 200m sample.",
        "crumb": "5 – 8μm Standard",
        "h1": "Standard <em>5 – 8μm</em><br>BOPP capacitor film.",
        "lede": "The workhorse grade for AC power capacitors, motor-run capacitors, lighting ballasts, and induction heating capacitors — long-life, low tanδ, consistent winding behavior.",
        "intro_h2": "The workhorse grade for <em>industrial film capacitors.</em>",
        "intro_p": "Our standard 5–8μm BOPP capacitor film is the most widely used grade in industrial film capacitor production. Excellent dielectric strength (≥ 150 kV/mm), low tanδ (≤ 0.0002), and consistent winding behavior make it the obvious choice for AC power capacitors, motor-run capacitors, lighting ballasts, and induction heating capacitors.",
        "specs": [
            ("Thickness", "5.0 / 6.0 / 8.0 μm <span style='color:var(--ink-3);font-size:14px'>(custom 5–10 μm available)</span>"),
            ("Thickness tolerance", "± 3% (lot average), ± 5% (point-to-point)"),
            ("Width", "Custom, up to 1,200 mm"),
            ("Roll length / OD", "Custom, max OD 600 mm"),
            ("Tensile strength (MD/TD)", "≥ 150 / 200 MPa"),
            ("Elongation at break (MD/TD)", "≥ 80 / 60 %"),
            ("Dielectric strength", "≥ 150 kV/mm <span style='color:var(--ink-3);font-size:14px'>(DC)</span>"),
            ("Dielectric loss tanδ", "≤ 0.0002 <span style='color:var(--ink-3);font-size:14px'>(1 kHz)</span>"),
            ("Surface tension", "≥ 38 dyn/cm <span style='color:var(--ink-3);font-size:14px'>(corona side)</span>"),
            ("Heat shrinkage", "≤ 3.0% <span style='color:var(--ink-3);font-size:14px'>(120°C, 15 min, MD/TD)</span>"),
            ("Density", "0.905 ± 0.003 g/cm³"),
            ("Surface", "Plain or single-side corona-treated"),
            ("Temperature rating", "105°C continuous"),
            ("Compliance", "RoHS 2.0 · REACH SVHC"),
        ],
        "commercial": [
            ("MOQ", "1 ton (trial) · 5 tons (production)"),
            ("Lead time", "15 working days for samples · 25–35 days for production"),
            ("Incoterms", "FOB Ningbo · CIF · EXW"),
            ("Payment", "T/T 30% deposit, 70% against B/L · L/C accepted"),
            ("Sample policy", "Free 200m roll; courier cost on buyer"),
            ("Packaging", "PE-wrapped rolls on plywood pallets. 20GP ~8–10 t, 40HQ ~18–22 t"),
            ("COA", "Certificate of Analysis with every shipment"),
        ],
        "apps": [
            ("i.", "AC power capacitor", "Power factor correction · harmonic filtering"),
            ("ii.", "Motor run capacitor", "Single-phase induction motor start / run"),
            ("iii.", "Lighting ballast capacitor", "Fluorescent & HID lamp ballasts"),
            ("iv.", "Induction heating capacitor", "Industrial induction heating tanks"),
        ],
        "img": "../assets/img/work/b4.png",
        "prev_slug": "ultra-thin",
        "prev_name": "3 – 4μm Ultra-thin",
        "next_slug": "high-temperature",
        "next_name": "125°C High-Temp",
    },
    {
        "slug": "high-temperature",
        "title": "High-Temperature BOPP Capacitor Film 125°C | Patented | Haibin",
        "desc": "Patented high-temperature BOPP capacitor film (CN115458342A) for 125°C continuous operation. EV battery compartment, PV inverter, wind converter.",
        "crumb": "125°C High-Temp",
        "h1": "High-Temperature<br>BOPP capacitor film, <em>125°C.</em>",
        "lede": "China Patent No. CN115458342A — engineered for continuous operation at 125°C, 20°C above standard BOPP. The grade for EV battery compartments, next-gen PV inverters, and high-density on-board chargers.",
        "intro_h2": "When <em>105°C is not enough.</em>",
        "intro_p": "Our patented high-temperature BOPP capacitor film raises the operating envelope by 20°C. A modified biaxial orientation temperature profile delivers 125°C continuous operation, dielectric strength ≥ 170 kV/mm, thermal shrinkage ≤ 2.5% at 140°C, and stable surface treatment retention at high temperature.",
        "specs": [
            ("Thickness", "4.0 / 5.0 / 6.0 / 8.0 μm"),
            ("Thickness tolerance", "± 3% (lot average), ± 5% (point-to-point)"),
            ("Width", "Custom, up to 1,200 mm"),
            ("Roll length / OD", "Custom, max OD 600 mm"),
            ("Tensile strength (MD/TD)", "≥ 160 / 210 MPa"),
            ("Elongation at break (MD/TD)", "≥ 90 / 70 %"),
            ("Dielectric strength", "≥ 170 kV/mm <span style='color:var(--ink-3);font-size:14px'>(DC)</span>"),
            ("Dielectric loss tanδ", "≤ 0.0002 <span style='color:var(--ink-3);font-size:14px'>(1 kHz)</span>"),
            ("Surface tension", "≥ 40 dyn/cm <span style='color:var(--ink-3);font-size:14px'>(corona side)</span>"),
            ("Heat shrinkage", "≤ 2.5% <span style='color:var(--ink-3);font-size:14px'>(140°C, 15 min, MD/TD)</span>"),
            ("Density", "0.905 ± 0.003 g/cm³"),
            ("Surface", "Plain or single-side corona-treated"),
            ("Temperature rating", "<b>125°C continuous</b> <span style='color:var(--ink-3);font-size:14px'>(vs 105°C standard)</span>"),
            ("Patent", "China Patent No. CN115458342A"),
            ("Compliance", "RoHS 2.0 · REACH SVHC"),
        ],
        "commercial": [
            ("MOQ", "1 ton (trial) · 3 tons (production)"),
            ("Lead time", "20 working days for samples · 30–40 days for production"),
            ("Incoterms", "FOB Ningbo · CIF · EXW"),
            ("Payment", "T/T 30% deposit, 70% against B/L · L/C accepted"),
            ("Sample policy", "Free 200m roll; courier cost on buyer"),
            ("Packaging", "PE-wrapped rolls on plywood pallets; vacuum-sealed optional"),
            ("COA", "Certificate of Analysis with every shipment"),
        ],
        "apps": [
            ("i.", "EV battery compartment", "Ambient temperature inside battery pack enclosure"),
            ("ii.", "On-board charger (OBC)", "High-density EV on-board chargers"),
            ("iii.", "PV string inverter", "Solar inverter output filter, 125°C hotspot rating"),
            ("iv.", "Wind converter DC-link", "Wind turbine converter DC-link smoothing"),
        ],
        "img": "../assets/img/work/b5.png",
        "prev_slug": "standard",
        "prev_name": "5 – 8μm Standard",
        "next_slug": "roughened",
        "next_name": "Roughened RP / RRP",
    },
    {
        "slug": "roughened",
        "title": "Roughened BOPP Capacitor Film RP / RRP | Oil-Impregnated | Haibin",
        "desc": "Single-side (RP) and double-side (RRP) roughened BOPP capacitor film for oil-impregnated AC / DC power capacitors. Improved oil retention, dielectric stability.",
        "crumb": "Roughened RP / RRP",
        "h1": "Roughened <em>RP / RRP</em><br>BOPP capacitor film.",
        "lede": "Single-side (RP) and double-side (RRP) roughened BOPP for oil-impregnated AC / DC power capacitors. Controlled surface roughness improves oil retention and prevents oil pooling during winding.",
        "intro_h2": "For <em>oil-impregnated</em> power capacitors.",
        "intro_p": "Compatible with PXE, DPE, M/DBT and MIDEL 7131 impregnation fluids. Ra roughness 0.15–0.30 μm (RP) or 0.20–0.35 μm (RRP) gives the right capillary structure for oil retention and uniform dielectric strength under stress.",
        "specs": [
            ("Thickness", "6.0 / 8.0 / 10.0 / 12.0 μm"),
            ("Thickness tolerance", "± 3% (lot average), ± 5% (point-to-point)"),
            ("Width", "Custom, up to 1,200 mm"),
            ("Roll length / OD", "Custom, max OD 600 mm"),
            ("Tensile strength (MD/TD)", "≥ 140 / 190 MPa"),
            ("Elongation at break (MD/TD)", "≥ 80 / 60 %"),
            ("Dielectric strength", "≥ 150 kV/mm <span style='color:var(--ink-3);font-size:14px'>(DC, in oil)</span>"),
            ("Dielectric loss tanδ", "≤ 0.0002 <span style='color:var(--ink-3);font-size:14px'>(1 kHz)</span>"),
            ("Surface roughness Ra", "RP: 0.15–0.30 μm · RRP: 0.20–0.35 μm"),
            ("Heat shrinkage", "≤ 3.0% <span style='color:var(--ink-3);font-size:14px'>(120°C, 15 min, MD/TD)</span>"),
            ("Density", "0.905 ± 0.003 g/cm³"),
            ("Oil compatibility", "PXE · DPE · M/DBT · MIDEL 7131"),
            ("Temperature rating", "105°C continuous"),
            ("Compliance", "RoHS 2.0 · REACH SVHC"),
        ],
        "commercial": [
            ("MOQ", "2 tons (trial) · 5 tons (production)"),
            ("Lead time", "20 working days for samples · 30–40 days for production"),
            ("Incoterms", "FOB Ningbo · CIF · EXW"),
            ("Payment", "T/T 30% deposit, 70% against B/L · L/C accepted"),
            ("Sample policy", "Free 200m roll; courier cost on buyer"),
            ("Packaging", "PE-wrapped rolls on plywood pallets; sealed PE bag for moisture control"),
            ("COA", "Certificate of Analysis with every shipment"),
        ],
        "apps": [
            ("i.", "All-film oil-impregnated power capacitor", "Replaces kraft paper in HV AC / DC capacitors"),
            ("ii.", "HV DC-link capacitor", "Wind turbine HVDC link smoothing"),
            ("iii.", "Static VAR compensator", "Reactive power compensation"),
            ("iv.", "Rail traction capacitor", "Electric locomotive line filter"),
        ],
        "img": "../assets/img/work/b6.png",
        "prev_slug": "high-temperature",
        "prev_name": "125°C High-Temp",
        "next_slug": "metallized-base",
        "next_name": "Metallization Base",
    },
    {
        "slug": "metallized-base",
        "title": "Metallization Base BOPP Capacitor Film | Corona-Treated | Haibin",
        "desc": "Corona-treated BOPP film as substrate for Al / Zn vacuum metallization. Excellent metal adhesion, high breakdown strength. Custom width and roll length.",
        "crumb": "Metallization Base",
        "h1": "Metallization <em>base</em><br>BOPP capacitor film.",
        "lede": "Corona-treated to ≥ 38 dyn/cm and wound under clean-room conditions. Substrate for Al / Zn / Al-Zn vacuum metallization into metallized polypropylene film capacitors.",
        "intro_h2": "A clean, <em>corona-ready</em> base for vacuum metallization.",
        "intro_p": "Our metallization base BOPP film is corona-treated to ≥ 38 dyn/cm, wound under clean-room conditions, and slit on British Atlas and German Kampf slitters. It serves as the substrate for Al / Zn vacuum metallization into metallized polypropylene (MPP) film for self-healing AC / DC film capacitors.",
        "specs": [
            ("Thickness", "3.0 / 4.0 / 5.0 / 6.0 / 8.0 / 10.0 / 12.0 μm"),
            ("Thickness tolerance", "± 3% (lot average), ± 5% (point-to-point)"),
            ("Width", "Custom, up to 1,200 mm <span style='color:var(--ink-3);font-size:14px'>(narrow slit down to 30 mm)</span>"),
            ("Roll length / OD", "Custom, max OD 600 mm"),
            ("Tensile strength (MD/TD)", "≥ 150 / 200 MPa"),
            ("Elongation at break (MD/TD)", "≥ 80 / 60 %"),
            ("Dielectric strength", "≥ 150 kV/mm <span style='color:var(--ink-3);font-size:14px'>(DC)</span>"),
            ("Dielectric loss tanδ", "≤ 0.0002 <span style='color:var(--ink-3);font-size:14px'>(1 kHz)</span>"),
            ("Surface tension", "≥ 38 dyn/cm <span style='color:var(--ink-3);font-size:14px'>(single-side treated)</span>"),
            ("Wetting tension retention", "≥ 36 dyn/cm <span style='color:var(--ink-3);font-size:14px'>(after 6 months sealed storage)</span>"),
            ("Heat shrinkage", "≤ 3.0% <span style='color:var(--ink-3);font-size:14px'>(120°C, 15 min, MD/TD)</span>"),
            ("Density", "0.905 ± 0.003 g/cm³"),
            ("Pinholes", "≤ 1 per 10 m² (4μm); ≤ 0.5 per 10 m² (≥ 5μm)"),
            ("Compliance", "RoHS 2.0 · REACH SVHC"),
        ],
        "commercial": [
            ("MOQ", "1 ton (trial) · 5 tons (production)"),
            ("Lead time", "15 working days for samples · 25–35 days for production"),
            ("Incoterms", "FOB Ningbo · CIF · EXW"),
            ("Payment", "T/T 30% deposit, 70% against B/L · L/C accepted"),
            ("Sample policy", "Free 200m roll; courier cost on buyer"),
            ("Packaging", "PE-wrapped rolls on sealed plywood pallets; double-bag option for cleanroom delivery"),
            ("COA", "Certificate of Analysis with every shipment"),
        ],
        "apps": [
            ("i.", "Self-healing AC capacitor", "Air-conditioner, washing machine, motor-run"),
            ("ii.", "DC-link capacitor (metallized)", "Compact DC-link capacitors for EV / PV"),
            ("iii.", "EMI suppression (X2)", "Across-the-line X2 safety capacitor"),
            ("iv.", "Snubber capacitor", "IGBT / thyristor snubber in power electronics"),
        ],
        "img": "../assets/img/work/b2.png",
        "prev_slug": "roughened",
        "prev_name": "Roughened RP / RRP",
        "next_slug": None,
        "next_name": None,
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://hb-film.com/capacitor-films/{slug}.html">
<link rel="icon" type="image/svg+xml" href="../assets/ico/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

<div class="utility-bar"><div class="wrap">
<div>Reply within 12 working hours</div>
<div><a href="mailto:sales@hb-film.com">sales@hb-film.com</a> &nbsp;·&nbsp; <a href="tel:+8613858466830">+86 138 5846 6830</a></div>
</div></div>

<header class="site-header"><div class="wrap">
<a class="brand" href="../index.html"><span class="brand-mark">H</span><span class="brand-text"><span class="en">Haibin</span><span class="zh">BOPP FILM · SINCE 2011</span></span></a>
<nav class="nav-main">
<a href="../index.html">Index</a>
<a href="index.html" class="active">Capacitor</a>
<a href="../applications/index.html">Applications</a>
<a href="../factory/index.html">Factory</a>
<a href="../about/index.html">About</a>
<a href="../contact/index.html" class="nav-cta">Request Quote</a>
</nav>
<button class="menu-btn" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><line x1="3" y1="7" x2="21" y2="7"/><line x1="3" y1="13" x2="21" y2="13"/><line x1="3" y1="19" x2="21" y2="19"/></svg></button>
</div></header>

<section class="sub-hero">
<div class="wrap">
<div class="crumb"><a href="../index.html">Index</a> &nbsp;/&nbsp; <a href="index.html">Capacitor Film</a> &nbsp;/&nbsp; {crumb}</div>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
<div style="margin-top:32px;display:flex;gap:12px;flex-wrap:wrap">
<a href="../contact/index.html" class="btn btn-primary">Request a Quote →</a>
<a href="../contact/index.html#sample" class="btn btn-ghost">Free 200m Sample</a>
</div>
</div>
</section>

<section class="section-pad" style="padding-top:64px">
<div class="split">
<div class="imgwrap" style="margin-left:max(32px,calc((100vw - 1280px)/2 + 32px));margin-right:32px">
<img src="{img}" alt="{crumb} BOPP capacitor film roll">
</div>
<div style="padding-left:32px;padding-right:32px">
<div class="kicker">Product · {crumb}</div>
<h2 style="font-family:var(--serif);font-weight:500">{intro_h2}</h2>
<p style="font-size:17px">{intro_p}</p>
</div>
</div>
</section>

<section class="section-pad" style="padding-top:0">
<div class="wrap" style="max-width:920px">
<div class="section-head with-line">
<div class="kicker">Technical</div>
<h2>Specifications.</h2>
<p class="desc">Typical values for the standard {crumb} grade. Final TDS issued with your sample.</p>
</div>
<table class="spec-table">
{specs_rows}
</table>
</div>
</section>

<section class="section-pad" style="background:var(--bg-soft);padding:0">
<div style="padding:96px 32px;max-width:1280px;margin:0 auto">
<div class="section-head with-line" style="margin-bottom:48px">
<div class="kicker">Where It Goes</div>
<h2>Typical applications.</h2>
</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:32px">
{apps_grid}
</div>
</div>
</section>

<section class="section-pad">
<div class="wrap" style="max-width:920px">
<div class="section-head with-line">
<div class="kicker">Commercial</div>
<h2>How to order.</h2>
</div>
<table class="spec-table">
{commercial_rows}
</table>
</div>
</section>

<section class="section-pad" style="padding-top:0">
<div class="wrap" style="max-width:920px">
<div style="border-top:1px solid var(--ink);padding-top:36px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px">
{prev_link}
{next_link}
</div>
</div>
</section>

<section class="cta-banner">
<div class="wrap">
<div class="kicker" style="color:#e0945f">Begin</div>
<h2>Need a sample or <em>full TDS?</em></h2>
<p>Send us your capacitor construction and we'll dispatch a free 200m roll plus the TDS for this grade.</p>
<a href="../contact/index.html" class="btn btn-primary">Request a Sample →</a>
</div>
</section>

<footer class="site-footer">
<div class="wrap">
<div class="grid4">
<div><a class="brand" href="../index.html"><span class="brand-mark">H</span><span class="brand-text"><span class="en">Haibin</span><span class="zh">BOPP FILM · SINCE 2011</span></span></a><p style="font-size:13.5px;color:#a8a39c;margin-top:18px">Zhejiang Haibin Film Technology Co., Ltd.<br>Binhai Industrial Zone, Keqiao, Shaoxing, China 312030</p></div>
<div><h5>Capacitor Film</h5><ul><li><a href="ultra-thin.html">3 – 4μm Ultra-thin</a></li><li><a href="standard.html">5 – 8μm Standard</a></li><li><a href="high-temperature.html">125°C High-Temp</a></li><li><a href="roughened.html">Roughened RP / RRP</a></li><li><a href="metallized-base.html">Metallization Base</a></li></ul></div>
<div><h5>Company</h5><ul><li><a href="../about/index.html">About</a></li><li><a href="../factory/index.html">Factory</a></li><li><a href="../applications/index.html">Applications</a></li></ul></div>
<div><h5>Reach Us</h5><ul><li><a href="mailto:sales@hb-film.com">sales@hb-film.com</a></li><li><a href="tel:+8613858466830">+86 138 5846 6830</a></li></ul></div>
</div>
<div class="legal"><div>© 2026 Zhejiang Haibin Film Technology Co., Ltd.</div><div>FOB Ningbo · 30 min to Hangzhou Airport</div></div>
</div>
</footer>

<script src="../assets/js/main.js"></script>
</body></html>
"""


def specs_rows(specs):
    return "\n".join(f"  <tr><th>{k}</th><td>{v}</td></tr>" for k, v in specs)


def commercial_rows(items):
    return "\n".join(f"  <tr><th>{k}</th><td>{v}</td></tr>" for k, v in items)


def apps_grid(items):
    return "\n".join(
        f"""  <div>
    <div style='font-family:var(--serif);font-style:italic;font-size:32px;color:var(--accent);margin-bottom:10px'>{n}</div>
    <h3 style='font-family:var(--serif);font-size:20px;font-weight:500;margin-bottom:8px'>{t}</h3>
    <p style='font-size:15px;color:var(--ink-3);margin:0'>{d}</p>
  </div>"""
        for n, t, d in items
    )


def prev_link(p):
    if not p:
        return '<span></span>'
    return f'<a href="{p["prev_slug"]}.html" style="text-decoration:none;color:var(--ink-2);font-family:var(--serif);font-style:italic;font-size:18px">← Previous · {p["prev_name"]}</a>'


def next_link(p):
    if not p.get("next_slug"):
        return '<a href="index.html" style="text-decoration:none;color:var(--ink-2);font-family:var(--serif);font-style:italic;font-size:18px">All Capacitor Film →</a>'
    return f'<a href="{p["next_slug"]}.html" style="text-decoration:none;color:var(--ink-2);font-family:var(--serif);font-style:italic;font-size:18px">Next · {p["next_name"]} →</a>'


for p in PAGES:
    html_out = TEMPLATE.format(
        title=p["title"],
        desc=p["desc"],
        slug=p["slug"],
        crumb=p["crumb"],
        h1=p["h1"],
        lede=p["lede"],
        img=p["img"],
        intro_h2=p["intro_h2"],
        intro_p=p["intro_p"],
        specs_rows=specs_rows(p["specs"]),
        commercial_rows=commercial_rows(p["commercial"]),
        apps_grid=apps_grid(p["apps"]),
        prev_link=prev_link(p),
        next_link=next_link(p),
    )
    path = os.path.join(OUT, p["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print("wrote", path)