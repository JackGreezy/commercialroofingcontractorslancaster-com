#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import quote
import json, re, sys
from bs4 import BeautifulSoup

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
PUBLIC = ROOT / "public"
FAKE = re.compile(r"(?:\+?1[\s.-]?)?\(?555\)?[\s.-]?555[\s.-]?\d{4}")
MAP_SRC = "https://www.google.com/maps?q=" + quote("101 N Queen St, Suite 400, Lancaster, PA 17603") + "&output=embed"

HOME = '''<main class="rr-lc-main" data-main-content-parent="true" id="PAGE_SECTIONStjzwo">
<section class="rr-lc-hero"><div class="rr-lc-shell"><div class="rr-lc-hero-copy"><p class="rr-lc-kicker">Commercial Roofing Contractors of Lancaster</p><h1>Commercial Roof Help for Lancaster Buildings</h1><p>Active leak, aging flat roof, recurring repair, or a capital project coming up? Start with a clear roof assessment. Get practical direction on repair, coating, replacement, and long-term service.</p><div class="rr-lc-actions"><a class="rr-lc-btn" href="/contact?need=Emergency%20Roof%20Repair">Get Emergency Roof Help</a><a class="rr-lc-btn rr-lc-btn--light" href="/contact?need=Flat%20Roof%20Replacement%20Inspection">Schedule a Roof Inspection</a></div></div></div></section>
<section class="rr-lc-alert"><div class="rr-lc-shell"><strong>Water is getting in now?</strong><p>Send the building address, leak area, roof access details, and photos if available. We will help move the request forward quickly.</p><a href="/contact?need=Emergency%20Roof%20Repair">Request emergency service</a></div></section>
<section class="rr-lc-split"><div class="rr-lc-split-media" style="background-image:url('/ours/services/commercial-roof-inspection-commercial-roofing-contractors-lancaster-pa.webp')"></div><div class="rr-lc-split-copy"><div><p class="rr-lc-kicker">Flat Roof Replacement Inspection</p><h2>Know what the roof needs before you fund the project.</h2><p>A replacement decision should start with the roof in front of you, not a generic price per square foot. We inspect the membrane, seams, flashing, penetrations, drainage, visible moisture concerns, repair history, and roof access.</p><ul class="rr-lc-checks"><li>Document current condition and active problem areas</li><li>Separate repairable defects from broader system failure</li><li>Compare repair, restoration, recover, and replacement paths</li><li>Give ownership a clearer basis for scope and budget planning</li></ul><a class="rr-lc-btn" href="/contact?need=Flat%20Roof%20Replacement%20Inspection">Request an inspection</a></div></div></section>
<section class="rr-lc-services"><div class="rr-lc-shell"><div class="rr-lc-heading-row"><div><p class="rr-lc-kicker">Start With the Immediate Need</p><h2>One commercial roofing resource from first leak to full replacement.</h2></div><p>Every call does not need to become a reroof. The right first step is the one that protects the building and gives the owner a sound next decision.</p></div><nav class="rr-lc-explore" aria-label="Explore commercial roofing resources"><a href="/roof-systems">Roof Systems</a><a href="/industries">Industries</a><a href="/project-types">Project Types</a><a href="/manufacturers">Manufacturers</a><a href="/about">Our Approach</a></nav><div class="rr-lc-service-grid"><a class="rr-lc-service-card" href="/services/commercial-roof-leak-repair"><span>Urgent response</span><h3>Commercial Roof Repair</h3><p>Find the source, protect the interior, and address the failure with a repair scope that makes sense.</p><b>Get roof repair help</b></a><a class="rr-lc-service-card" href="/services/commercial-roof-inspection"><span>Condition clarity</span><h3>Roof Inspections and Reports</h3><p>See what is failing, what still has useful life, and what ownership should plan for next.</p><b>Schedule an inspection</b></a><a class="rr-lc-service-card" href="/services/silicone-roof-coatings"><span>Restore useful life</span><h3>Roof Coatings</h3><p>Evaluate whether a coating can seal, protect, and extend a suitable existing roof system.</p><b>Explore roof coatings</b></a><a class="rr-lc-service-card" href="/services/commercial-reroofing"><span>Capital project</span><h3>Commercial Reroofing</h3><p>Plan tear-off, recover, phasing, drainage, insulation, and system selection around the real building.</p><b>Plan a roof replacement</b></a></div></div></section>
<section class="rr-lc-decision"><div class="rr-lc-shell"><div class="rr-lc-decision-head"><p class="rr-lc-kicker">Repair, Restore, or Replace</p><h2>Make the next roof dollar count.</h2><p>Condition, moisture, attachment, drainage, age, repair history, operations, and ownership goals all matter. We help put those facts into one decision.</p></div><div class="rr-lc-decision-grid"><article class="rr-lc-decision-card"><h3>Repair</h3><p>Best when failures are isolated and the surrounding roof remains serviceable.</p><a href="/contact?need=Commercial%20Roof%20Repair">Discuss a repair</a></article><article class="rr-lc-decision-card"><h3>Restore</h3><p>Worth evaluating when the roof is dry and stable enough for a coating or restoration system.</p><a href="/contact?need=Roof%20Coating">Review coating options</a></article><article class="rr-lc-decision-card"><h3>Replace</h3><p>Necessary when failures are widespread, trapped moisture is significant, or the system is at the end of its useful life.</p><a href="/contact?need=Commercial%20Roof%20Replacement">Plan replacement</a></article></div></div></section>
<section class="rr-lc-agreement"><div class="rr-lc-shell"><div class="rr-lc-agreement-copy"><p class="rr-lc-kicker">Commercial Roof Service Agreements</p><h2>Stay ahead of leaks instead of reacting to them.</h2><p>Scheduled inspections and preventive maintenance help facility teams catch small defects, protect drainage, document conditions, and plan capital work before a surprise shutdown or interior loss.</p><ul class="rr-lc-checks"><li>Routine roof inspections</li><li>Preventive maintenance and minor repairs</li><li>Condition records for ownership and budgeting</li><li>A familiar service path when problems appear</li></ul><a class="rr-lc-btn" href="/contact?need=Roof%20Service%20Agreement">Ask about a service agreement</a></div></div></section>
<section class="rr-lc-markets"><div class="rr-lc-shell"><div class="rr-lc-market-grid"><div><p class="rr-lc-kicker">Lancaster County Coverage</p><h2>Commercial roofs across the city, county, and Susquehanna Valley.</h2><p>We help owners and facility teams responsible for warehouses, manufacturing plants, retail centers, schools, healthcare properties, offices, hospitality buildings, and multi-site portfolios.</p><div class="rr-lc-actions"><a class="rr-lc-btn" href="/service-areas">View service areas</a><a class="rr-lc-btn rr-lc-btn--light" style="border-color:#0666bb;color:#0666bb!important" href="/contact">Start a roof request</a></div></div><div class="rr-lc-market-list"><a href="/service-areas/downtown-lancaster">Downtown Lancaster</a><a href="/service-areas/manheim-township">Manheim Township</a><a href="/service-areas/lititz">Lititz</a><a href="/service-areas/ephrata">Ephrata</a><a href="/service-areas/columbia">Columbia</a><a href="/service-areas/mount-joy">Mount Joy</a><a href="/service-areas/new-holland">New Holland</a><a href="/service-areas/willow-street">Willow Street</a></div></div></div></section>
<section class="rr-lc-faq"><div class="rr-lc-shell"><div><p class="rr-lc-kicker">Straight Answers</p><h2>Commercial roofing questions owners ask first.</h2></div><div class="rr-lc-faq-list"><details><summary>Can a commercial flat roof be repaired instead of replaced?</summary><p>Often, yes. Localized membrane, flashing, penetration, seam, and drainage defects may be repairable when the broader roof remains sound. An inspection helps determine whether repair is a reasonable use of money.</p></details><details><summary>When should a flat roof replacement inspection be scheduled?</summary><p>Schedule one when leaks keep returning, the roof is near the end of its expected service life, a major repair is proposed, a property transaction is underway, or ownership needs a dependable capital plan.</p></details><details><summary>Is a coating always cheaper than replacement?</summary><p>A coating can cost less than replacement, but only a suitable roof should be coated. Moisture, adhesion, drainage, membrane condition, repairs, and manufacturer requirements need review first.</p></details><details><summary>What does a commercial roof service agreement cover?</summary><p>Programs vary, but the goal is consistent: inspect the roof, clear or flag drainage concerns, document conditions, handle agreed maintenance items, and create a clear path for follow-up repairs.</p></details><details><summary>Can roofing work continue while the building is occupied?</summary><p>Many projects can be phased around occupied operations. Access, odor, noise, interior protection, loading, rooftop equipment, safety, and business schedules should be discussed before the scope is finalized.</p></details></div></div></section>
<section class="rr-lc-close"><div class="rr-lc-shell"><p class="rr-lc-kicker" style="color:#d7efff">Bring Us the Roof Problem</p><h2>Get a clear next step for your Lancaster commercial roof.</h2><p>Send the building address, what you are seeing, and when the issue needs attention. We will help start the right conversation.</p><a class="rr-lc-btn rr-lc-btn--light" href="/contact">Request commercial roof help</a></div></section>
</main>'''

def add_asset(soup, tag, attr, value, marker):
    if soup.find(attrs={marker: True}): return
    node = soup.new_tag(tag)
    node[attr] = value
    node[marker] = "true"
    soup.head.append(node)

def patch_json_schema(soup):
    for node in soup.find_all("script", type="application/ld+json"):
        try: data=json.loads(node.string or "{}")
        except Exception: continue
        def clean(value):
            if isinstance(value, dict):
                value.pop("telephone", None)
                for item in value.values(): clean(item)
            elif isinstance(value, list):
                for item in value: clean(item)
        clean(data); node.string=json.dumps(data, ensure_ascii=False)

for path in sorted(PUBLIC.rglob("*.html")):
    soup=BeautifulSoup(path.read_text(errors="ignore"), "html.parser")
    if not soup.head or not soup.body: continue
    add_asset(soup,"link","href","/lancaster-conversion.css","data-lancaster-css"); soup.find(attrs={"data-lancaster-css":True})["rel"]="stylesheet"
    add_asset(soup,"script","src","/lancaster-conversion.js","data-lancaster-js"); soup.find(attrs={"data-lancaster-js":True})["defer"]=""
    patch_json_schema(soup)
    for node in soup.find_all(class_=True):
        node["class"] = ["rr-hp-field" if token == "hp-field" else "rr-form-status" if token == "form-status" else token for token in node.get("class", [])]
    for a in list(soup.find_all("a", href=re.compile(r"^tel:"))):
        if FAKE.search((a.get_text(" ",strip=True)+" "+a.get("href",""))): a.decompose()
    for text in list(soup.find_all(string=FAKE)):
        text.replace_with(FAKE.sub("", str(text)))
    for node in soup.select(".rr-footer-map"):
        node.clear()
        iframe=soup.new_tag("iframe",title="Commercial Roofing Contractors of Lancaster office map",src=MAP_SRC,loading="lazy",referrerpolicy="no-referrer-when-downgrade",allowfullscreen="")
        node.append(iframe)
    for old in list(soup.select("body > [data-rh-map='true'], main + [data-rh-map='true']")): old.decompose()
    route="/" + str(path.relative_to(PUBLIC)).replace("index.html","").replace("home.html","").replace(".html","").strip("/")
    if path.name in {"home.html","index.html"}:
        main=soup.find("main")
        if main: main.replace_with(BeautifulSoup(HOME,"html.parser").main)
    if route.rstrip("/") in {"/contact","/contact-us"}:
        form=soup.find("form",attrs={"data-contact-form":True})
        for stale in list(soup.select(".rr-lc-roof-need")):
            if form and stale.find_parent("form") is not form:
                stale.decompose()
        if form and not form.find("select",attrs={"name":"roofNeed"}):
            label=BeautifulSoup('''<label class="rr-contact-field rr-contact-field--full rr-lc-roof-need">What does the roof need?<select name="roofNeed" required><option value="">Choose the closest match</option><option>Emergency Roof Repair</option><option>Commercial Roof Repair</option><option>Flat Roof Replacement Inspection</option><option>Roof Coating</option><option>Commercial Roof Replacement</option><option>Roof Service Agreement</option><option>Not Sure Yet</option></select></label>''',"html.parser").label
            timeline=form.find(attrs={"name":"timeline"})
            roofing_need=form.find(attrs={"name":re.compile(r"^roofingNeed$",re.I)})
            target=(timeline.find_parent("label") if timeline and timeline.find_parent("label") else None) or (roofing_need.find_parent(["label","div"]) if roofing_need else None) or form.find("textarea") or form.find("button")
            if target:
                target.insert_before(label)
            else:
                form.append(label)
    if not soup.select_one(".rr-lc-contact-float"):
        sticky=BeautifulSoup('''<a class="rr-lc-contact-float" href="/contact?need=Emergency%20Roof%20Repair" aria-label="Request commercial roof help"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm3 6v2h10V9H7zm0 4v2h7v-2H7z"/></svg></a>''',"html.parser").a
        soup.body.append(sticky)
    output=str(soup).replace("—","-").replace("–","-")
    path.write_text(output)
print(f"Lancaster conversion pass: {len(list(PUBLIC.rglob('*.html')))} pages")
