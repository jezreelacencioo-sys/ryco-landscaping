"""All site text and business facts. Edit here, then run: python3 _build/build.py"""

# Change this when the site moves to its own domain (no trailing slash).
SITE = 'https://jezreelacencioo-sys.github.io/ryco-landscaping'

BUSINESS = {
    'name': 'Carolina Premier Lawn & Tree Services LLC',
    'short': 'Carolina Premier',
    'phone': '(984) 381-8731',
    'phone_e164': '+19843818731',
    'city': 'Apex',
    'state': 'NC',
    'rating': '5.0',
    'review_count': 24,
    'google_url': 'https://www.google.com/search?q=Carolina+Premier+Lawn+%26+Tree+Services+LLC',
}

# ---------------------------------------------------------------- Services
# img: file in images/ (without .jpg). Placeholder photos until real job photos arrive.
SERVICES = [
    {
        'slug': 'lawn-mowing',
        'name': 'Lawn Mowing & Maintenance',
        'short': 'Weekly or bi-weekly mowing, edging, trimming and blowing so your yard looks sharp all season.',
        'img': 'lawn',
        'title': 'Lawn Mowing & Lawn Care in Apex, NC',
        'desc': 'Reliable weekly and bi-weekly lawn mowing, edging and trimming in Apex, Cary, Holly Springs and the Triangle. 5-star rated. Free estimates: (984) 381-8731.',
        'h1': 'Lawn Mowing &amp; Maintenance in <span class="hl">Apex, NC</span>',
        'lead': 'A clean cut, sharp edges and a yard you never have to think about. We keep Triangle lawns looking their best on a schedule that fits your property.',
        'intro': [
            'Regular mowing is the single biggest thing you can do for how your yard looks, and doing it right is the biggest thing you can do for how healthy it stays. Our maintenance visits cover the full job: mowing, edging, trimming and cleanup, so the whole property looks finished when we drive away.',
            'We set the mowing height for your grass type and the season instead of cutting every lawn the same way. That means thicker turf, fewer weeds and a lawn that holds up better through a hot North Carolina summer.',
        ],
        'includes': [
            'Mowing at the right height for your grass type',
            'Edging along driveways, sidewalks and curbs',
            'String trimming around beds, fences and mailboxes',
            'Clippings blown off every hard surface',
            'Weekly or bi-weekly visits through the growing season',
        ],
        'local_title': 'Mowing for Triangle lawns',
        'local': [
            'Most lawns in Apex and the surrounding towns are tall fescue, a cool-season grass that stays healthiest when it is mowed tall, around 3 to 4 inches, especially in July and August. Cutting fescue short in summer is one of the most common reasons it thins out and lets crabgrass take over.',
            'Bermuda and zoysia lawns in full sun are a different story. They do best kept much shorter and grow fastest in the heat. Whichever you have, we cut it the way that grass wants to be cut.',
        ],
        'faqs': [
            ('How often should my lawn be mowed?', 'During peak growing season most lawns look best mowed every week. In slower stretches, like the heat of late summer for fescue, every other week can be enough. We can set a schedule that fits your yard and budget.'),
            ('What height should tall fescue be mowed in summer?', 'Keep tall fescue on the high side, around 3 to 4 inches, during the summer. Taller grass shades the soil, holds moisture and crowds out weeds. Avoid removing more than about a third of the blade in a single cut.'),
            ('Should grass clippings be bagged?', 'Usually not. Clippings left on the lawn break down quickly and return nutrients to the soil. Bagging mostly makes sense when the grass has gotten very tall or before an event when you want a spotless look.'),
        ],
        'related': ['seasonal-cleanups', 'aeration-overseeding', 'mulch-pine-straw'],
    },
    {
        'slug': 'tree-trimming-removal',
        'name': 'Tree Trimming & Removal',
        'short': 'Pruning, limb removal and safe takedowns for overgrown, dead or storm-damaged trees.',
        'img': 'trees',
        'title': 'Tree Trimming & Tree Removal in Apex, NC',
        'desc': 'Tree trimming, limb removal and safe tree removal in Apex, Cary, Holly Springs and the Triangle. Storm cleanup and debris haul-away. Free estimates: (984) 381-8731.',
        'h1': 'Tree Trimming &amp; <span class="hl">Tree Removal</span> in Apex, NC',
        'lead': 'Overhanging limbs, dead trees and storm damage handled safely, with the mess cleaned up before we leave.',
        'intro': [
            'Trees are a big part of what makes Triangle neighborhoods beautiful, but a limb over the roof or a dead pine next to the house is a risk you should not have to live with. We trim, thin and remove trees so your property is safer and your yard gets the light it needs.',
            'Every job ends with cleanup. Limbs, branches and debris are hauled away so you are left with a clean yard, not a brush pile.',
        ],
        'includes': [
            'Pruning and thinning to improve shape and light',
            'Limbs cut back from roofs, gutters and driveways',
            'Removal of dead, dying or leaning trees',
            'Storm damage cleanup',
            'Debris and brush haul-away',
        ],
        'local_title': 'Trees in the Triangle',
        'local': [
            'Wake County is full of tall loblolly pines, oaks, maples and sweetgums, and many homes in Apex and Cary were built right among them. Summer thunderstorms and the remnants of tropical storms regularly bring down limbs and whole trees across the area.',
            'The best time to prune most hardwoods is late fall through winter when they are dormant: you can see the branch structure and the tree heals well in spring. Dead limbs and hazardous trees, though, should be dealt with as soon as you notice them.',
        ],
        'faqs': [
            ('When is the best time to trim trees in North Carolina?', 'For most shade trees, late fall through late winter is ideal because the tree is dormant and the branch structure is easy to see. Dead, broken or hazardous limbs can and should be removed any time of year.'),
            ('How do I know if a tree is dangerous?', 'Warning signs include a tree that has started leaning recently, cracked or heaving soil at the base, large dead limbs, mushrooms growing on the trunk or roots, and deep cracks in the trunk. If you see any of these near your home, have it looked at soon.'),
            ('Do I need a permit to remove a tree?', 'It depends on where you live. Many trees on private residential lots can be removed without a permit, but towns can have rules for buffers and certain properties, and many HOAs require approval. Check with your town and HOA before removing a large tree.'),
        ],
        'related': ['seasonal-cleanups', 'lawn-mowing', 'mulch-pine-straw'],
    },
    {
        'slug': 'aeration-overseeding',
        'name': 'Aeration & Overseeding',
        'short': 'Fall core aeration and overseeding to bring thin, patchy fescue lawns back thick and green.',
        'img': 'garden',
        'title': 'Lawn Aeration & Overseeding in Apex, NC',
        'desc': 'Core aeration and overseeding for tall fescue lawns in Apex, Cary, Holly Springs and the Triangle. Loosen compacted clay and thicken thin turf. Free estimates.',
        'h1': 'Aeration &amp; <span class="hl">Overseeding</span> in Apex, NC',
        'lead': 'The best thing you can do for a thin fescue lawn, done at the right time of year.',
        'intro': [
            'Core aeration pulls thousands of small plugs of soil out of your lawn. That relieves compaction and lets air, water and fertilizer reach the roots. Overseeding right after aeration drops new seed into those holes, where it has great contact with the soil and the best chance to grow.',
            'Together they are the most effective way to thicken a thin or patchy fescue lawn and keep it from slowly wearing out year after year.',
        ],
        'includes': [
            'Core aeration across the whole lawn',
            'Overseeding with quality tall fescue seed',
            'Extra seed on thin and bare spots',
            'Watering instructions so the new seed takes',
        ],
        'local_title': 'Why Apex lawns need it',
        'local': [
            'Much of the Triangle sits on dense red clay, and it compacts easily, especially in newer neighborhoods where the topsoil was scraped away during construction. Compacted soil means shallow roots, puddles after rain and grass that struggles every summer.',
            'For tall fescue, early fall is the best window: roughly late August through mid-October, with September ideal. The soil is still warm enough for fast germination and the cooler weather that follows lets young grass establish before winter. Warm-season lawns like Bermuda and zoysia are aerated in late spring or early summer instead.',
        ],
        'faqs': [
            ('When should I aerate and overseed in Apex?', 'For tall fescue lawns, early fall is best, roughly late August through mid-October, with September being ideal. Spring seeding is possible but the young grass has less time to establish before summer heat.'),
            ('How should I water after overseeding?', 'Keep the top of the soil consistently moist until the seed sprouts, usually with light watering once or twice a day for the first one to two weeks. Once the new grass is up, water less often but more deeply.'),
            ('What do I do with the soil plugs?', 'Leave them. The plugs break down on their own within a couple of weeks, especially after rain and mowing, and return that soil to the lawn.'),
        ],
        'related': ['lawn-mowing', 'seasonal-cleanups', 'mulch-pine-straw'],
    },
    {
        'slug': 'mulch-pine-straw',
        'name': 'Mulch, Pine Straw & Beds',
        'short': 'Fresh mulch or pine straw, crisp bed edges and weeding that make the whole property look finished.',
        'img': 'garden-path',
        'title': 'Mulch & Pine Straw Installation in Apex, NC',
        'desc': 'Mulch and pine straw installation, bed edging and weeding in Apex, Cary, Holly Springs and the Triangle. Clean, finished landscape beds. Free estimates.',
        'h1': 'Mulch, Pine Straw &amp; <span class="hl">Bed Care</span>',
        'lead': 'Nothing freshens up a property faster than clean beds, sharp edges and a new layer of mulch or pine straw.',
        'intro': [
            'Fresh mulch or pine straw instantly makes a yard look cared for. It also does real work: it holds moisture in the soil, keeps roots cooler in summer and helps keep weeds down.',
            'We prep every bed before anything goes down. Weeds are pulled, edges are cut clean and old material is leveled out so the new layer goes on smooth and even.',
        ],
        'includes': [
            'Weeding beds before every install',
            'Hand-cut, crisp bed edges',
            'Hardwood mulch or long-leaf pine straw',
            'Spread at the right depth, kept off trunks and siding',
            'Cleanup of walks and driveways when we finish',
        ],
        'local_title': 'Mulch or pine straw?',
        'local': [
            'Pine straw is a Carolina classic. It is light, knits together so it stays put on slopes, and suits the azaleas, camellias and hollies found in so many Triangle yards. Hardwood mulch gives a darker, more finished look and breaks down into the soil over time.',
            'Either way, more is not better. About 2 to 3 inches of mulch is plenty, and it should never be piled up against tree trunks. Those "mulch volcanoes" trap moisture against the bark and can slowly damage the tree.',
        ],
        'faqs': [
            ('Is mulch or pine straw better?', 'Both work well. Pine straw is lighter, stays put on slopes and is popular in the Carolinas. Hardwood mulch looks darker and more formal and adds organic matter as it breaks down. Many homeowners choose based on the look they like.'),
            ('How deep should mulch be?', 'About 2 to 3 inches is right for most beds. Thicker layers can keep water from reaching the soil, and mulch should always be pulled back a few inches from tree trunks and the house.'),
            ('How often should beds be refreshed?', 'Most beds look best with a fresh layer once a year, often in spring. Pine straw fades faster, so some homeowners refresh it in both spring and fall.'),
        ],
        'related': ['seasonal-cleanups', 'lawn-mowing', 'hardscaping'],
    },
    {
        'slug': 'seasonal-cleanups',
        'name': 'Seasonal Cleanups',
        'short': 'Spring and fall cleanups, leaf removal and shrub trimming to get your yard ready for the season.',
        'img': 'planting',
        'title': 'Leaf Removal & Yard Cleanups in Apex, NC',
        'desc': 'Fall leaf removal, spring yard cleanups and shrub trimming in Apex, Cary, Holly Springs and the Triangle. Debris hauled away. Free estimates: (984) 381-8731.',
        'h1': 'Leaf Removal &amp; <span class="hl">Seasonal Cleanups</span>',
        'lead': 'Start every season with a clean slate. We clear the leaves, trim the shrubs and haul it all away.',
        'intro': [
            'A good cleanup resets the whole property. In the fall that means clearing leaves before they smother the lawn. In the spring it means clearing winter debris, cutting back beds and trimming shrubs so everything grows in clean.',
            'Everything we clear is hauled away, so you are not left with piles of bags at the curb.',
        ],
        'includes': [
            'Leaf removal from lawns and beds',
            'Shrub and hedge trimming',
            'Bed cleanup and perennial cutbacks',
            'Storm debris and fallen limb pickup',
            'Haul-away of everything we clear',
        ],
        'local_title': 'Why fall leaf removal matters here',
        'local': [
            'Triangle oaks, maples and sweetgums drop most of their leaves from late October into December. That is exactly when tall fescue is doing most of its growing, and when newly seeded lawns are trying to establish.',
            'A thick layer of wet leaves blocks sunlight and can smother fescue in just a few weeks. Clearing leaves regularly through the fall protects your lawn and any seed you put down in September.',
        ],
        'faqs': [
            ('When should I schedule a fall cleanup?', 'Most Triangle properties benefit from a cleanup once the bulk of the leaves have dropped, usually late November into December. Yards with lots of trees or new seed often do better with two visits: one mid-fall and one once the trees are bare.'),
            ('Why is it bad to leave leaves on the lawn?', 'A thick layer of leaves blocks sunlight and traps moisture, which can smother grass and encourage disease. Fescue lawns are actively growing in the fall, so they suffer the most.'),
            ('What is included in a spring cleanup?', 'Typically clearing winter debris from lawns and beds, cutting back ornamental grasses and perennials, trimming shrubs, edging beds and getting everything ready for fresh mulch or pine straw.'),
        ],
        'related': ['mulch-pine-straw', 'tree-trimming-removal', 'lawn-mowing'],
    },
    {
        'slug': 'hardscaping',
        'name': 'Hardscaping',
        'short': 'Patios, walkways and retaining walls built to stand up to North Carolina clay and heavy rain.',
        'img': 'hero-home',
        'title': 'Patios, Walkways & Retaining Walls in Apex, NC',
        'desc': 'Paver patios, walkways and retaining walls in Apex, Cary, Holly Springs and the Triangle. Built on a solid base with proper drainage. Free estimates.',
        'h1': 'Patios, Walkways &amp; <span class="hl">Retaining Walls</span>',
        'lead': 'Outdoor living spaces built on a solid base, so they look great on day one and for years after.',
        'intro': [
            'A patio, walkway or retaining wall can completely change how you use your yard. What makes it last is everything you never see: a properly excavated and compacted base, and a plan for where the water goes.',
            'We build hardscapes to handle Triangle conditions, and we can tie them in with the lawn, beds and plantings around them so the whole space looks like it belongs together.',
        ],
        'includes': [
            'Paver patios',
            'Walkways and stepping paths',
            'Retaining walls',
            'Compacted gravel base and proper drainage',
            'Finishing landscaping around the new space',
        ],
        'local_title': 'Built for clay and rain',
        'local': [
            'Red clay holds water and moves as it gets wet and dries out. Combined with heavy summer downpours, that is hard on anything built on top of it. Pavers laid on a thin or poorly compacted base settle and shift, and retaining walls without drainage behind them can bulge or fail.',
            'A properly compacted base under patios and walkways, and gravel backfill with drainage behind walls, is what keeps a hardscape level and solid for the long run.',
        ],
        'faqs': [
            ('How long does a paver patio last?', 'Built on a properly excavated and compacted base, a paver patio can last for decades. Individual pavers can also be lifted and reset if needed, which makes repairs much easier than with poured concrete.'),
            ('Do retaining walls need drainage?', 'Yes. Water building up behind a wall pushes against it and is a leading cause of wall failure. Gravel backfill and a drain line behind the wall let water escape instead of building pressure.'),
            ('Can you do the landscaping around a new patio too?', 'Yes. We handle lawn, beds, mulch and pine straw too, so the area around your new patio or walkway can be finished at the same time.'),
        ],
        'related': ['mulch-pine-straw', 'lawn-mowing', 'seasonal-cleanups'],
    },
]

# ---------------------------------------------------------------- Towns
TOWNS = [
    {
        'slug': 'apex-nc',
        'name': 'Apex',
        'img': 'hero-home',
        'lead': 'Apex is home base. We take care of lawns, trees and landscapes all over town, from established streets near downtown to the newest neighborhoods.',
        'intro': [
            'Known as "The Peak of Good Living," Apex has grown fast while keeping its small-town feel, from historic Salem Street downtown to newer neighborhoods spreading toward Jordan Lake and Holly Springs. Being based right here means we know these yards and can get to you quickly.',
            'Whether you are in an established neighborhood like Scotts Mill or Beaver Creek, or a brand-new home still trying to grow its first real lawn, we can keep your yard looking its best all year.',
        ],
        'challenges': [
            ('Thin lawns on new construction', 'Many newer Apex homes have only a thin layer of topsoil over hard clay. Fall aeration and overseeding are the best way to build a thicker lawn over time.'),
            ('Summer heat on fescue', 'Tall fescue is the most common lawn here and it struggles in July and August. Mowing high through summer keeps it from thinning out.'),
            ('HOA standards', 'Many Apex neighborhoods have HOA rules for lawn height, edging and beds. Regular maintenance keeps you clear of violation letters.'),
        ],
        'faqs': [
            ('Do you serve all of Apex?', 'Yes. Apex is our home base and we work throughout town, including neighborhoods near downtown, along US-64 and out toward Jordan Lake and Holly Springs.'),
            ('What grass is most common in Apex?', 'Tall fescue is the most common lawn grass in Apex and across the Triangle. Some sunny yards have Bermuda or zoysia, which are warm-season grasses that need different care.'),
        ],
        'nearby': ['cary-nc', 'holly-springs-nc', 'fuquay-varina-nc'],
    },
    {
        'slug': 'cary-nc',
        'name': 'Cary',
        'img': 'trees',
        'lead': 'Lawn care, tree trimming and landscaping for Cary homeowners, right next door to our Apex home base.',
        'intro': [
            'Cary is known for well-kept neighborhoods and beautiful mature trees. Communities like Preston, Lochmere and MacGregor Downs have big oaks, maples and pines that give the town its character, and that also means a lot of leaves and limbs to manage.',
            'We help Cary homeowners keep lawns healthy under those trees, keep limbs off roofs and driveways, and keep beds and lawns up to the standard their neighborhood expects.',
        ],
        'challenges': [
            ('Mature trees and shade', 'Big trees mean shaded lawns, heavy leaf drop every fall and limbs growing over rooftops. Regular trimming and fall cleanups keep things under control.'),
            ('Neighborhood standards', 'Many Cary neighborhoods have HOAs with clear expectations for lawns, edging and beds. Consistent maintenance takes that off your plate.'),
            ('Compacted, tired lawns', 'Older lawns on clay soil get compacted over the years. Fall aeration and overseeding bring them back thick and green.'),
        ],
        'faqs': [
            ('Do you offer tree trimming in Cary?', 'Yes. We trim, thin and remove trees for Cary homeowners, including limbs over roofs and driveways and storm-damaged trees.'),
            ('Can you help with heavy leaf drop under big trees?', 'Yes. Fall leaf removal is one of our most popular services in Cary. Yards with many trees often do best with two visits during the fall.'),
        ],
        'nearby': ['apex-nc', 'morrisville-nc', 'raleigh-nc'],
    },
    {
        'slug': 'holly-springs-nc',
        'name': 'Holly Springs',
        'img': 'garden',
        'lead': 'Helping Holly Springs homeowners turn young lawns into thick, healthy ones, and keep them that way.',
        'intro': [
            'Holly Springs is one of the fastest-growing towns in the Triangle, with new neighborhoods going up all the time alongside established communities like 12 Oaks and Sunset Ridge. A lot of those homes have lawns that are only a few years old.',
            'Young lawns on clay soil need help to fill in. We combine regular mowing with fall aeration and overseeding to build thicker turf year after year, plus clean beds and seasonal cleanups to keep the whole property sharp.',
        ],
        'challenges': [
            ('Young lawns that have not filled in', 'Sod or seed on new construction often struggles in the first few years. Aeration, overseeding and mowing at the right height help it thicken up.'),
            ('Bare beds on new homes', 'New homes often come with thin landscaping. Fresh mulch or pine straw and clean edges make a big difference fast.'),
            ('Drainage on clay lots', 'Graded clay lots can shed water fast. Healthy turf and well-built hardscapes help manage runoff.'),
        ],
        'faqs': [
            ('My new lawn is thin. What should I do?', 'Fall core aeration and overseeding is the most effective fix for thin fescue lawns. Mowing high and watering deeply but less often also helps roots grow deeper.'),
            ('Do you work in newer Holly Springs neighborhoods?', 'Yes. We serve neighborhoods across Holly Springs, both new and established.'),
        ],
        'nearby': ['apex-nc', 'fuquay-varina-nc', 'cary-nc'],
    },
    {
        'slug': 'fuquay-varina-nc',
        'name': 'Fuquay-Varina',
        'img': 'garden-path',
        'lead': 'Lawn and tree care for Fuquay-Varina homes, from bigger lots to brand-new subdivisions.',
        'intro': [
            'Fuquay-Varina mixes small-town history, like the downtown area around the Fuquay Mineral Spring, with fast growth and plenty of new subdivisions. Many properties here also have bigger lots and more trees than you find closer to Raleigh.',
            'More yard means more to keep up with. We handle the mowing, trimming, tree work and cleanups so you can enjoy the space instead of spending every weekend maintaining it.',
        ],
        'challenges': [
            ('Larger lots', 'Bigger yards take real time to keep up. A regular mowing and maintenance schedule keeps them looking sharp without eating your weekends.'),
            ('Trees along property lines', 'Wooded edges and tree lines drop limbs and leaves into the yard. Trimming and seasonal cleanups keep them in check.'),
            ('Establishing new lawns', 'New-construction lawns on clay benefit from fall aeration and overseeding to fill in.'),
        ],
        'faqs': [
            ('Do you mow larger properties in Fuquay-Varina?', 'Yes. We mow and maintain properties of many sizes in Fuquay-Varina. Call or text for a free estimate based on your lot.'),
            ('Can you clear limbs and brush along a tree line?', 'Yes. We trim back trees along property lines and clear fallen limbs and debris, and haul it all away.'),
        ],
        'nearby': ['holly-springs-nc', 'apex-nc', 'cary-nc'],
    },
    {
        'slug': 'morrisville-nc',
        'name': 'Morrisville',
        'img': 'lawn',
        'lead': 'Dependable lawn care and landscaping for busy Morrisville homeowners.',
        'intro': [
            'Sitting between Research Triangle Park and RDU, Morrisville is full of busy professionals and families, with many homes in HOA communities like Breckenridge. Lots tend to be smaller, but expectations for how they look are high.',
            'We keep Morrisville yards neat and consistent with regular mowing, edging, bed care and seasonal cleanups, so your lawn always looks good without you having to think about it.',
        ],
        'challenges': [
            ('No time for yard work', 'Between work and family, weekends fill up fast. A set maintenance schedule means the lawn is always handled.'),
            ('HOA requirements', 'Many Morrisville communities have rules for lawns and beds. Regular care keeps you compliant.'),
            ('Small yards, high visibility', 'In tighter neighborhoods, every edge and bed is on display. Crisp edging and fresh mulch make a big difference.'),
        ],
        'faqs': [
            ('Do you work in Morrisville HOA communities?', 'Yes. We maintain lawns and beds for homeowners in many Morrisville neighborhoods and can work to your HOA standards.'),
            ('Can I set up a regular mowing schedule?', 'Yes. Weekly and bi-weekly schedules are available through the growing season. Call or text for a free estimate.'),
        ],
        'nearby': ['cary-nc', 'raleigh-nc', 'apex-nc'],
    },
    {
        'slug': 'raleigh-nc',
        'name': 'Raleigh',
        'img': 'planting',
        'lead': 'Lawn care, tree work and landscaping for Raleigh homeowners, especially in the southwest part of the city.',
        'intro': [
            'Raleigh is called the "City of Oaks" for good reason. Big hardwoods shade many of its neighborhoods, especially the established areas in southwest Raleigh closest to Apex and Cary.',
            'Those trees are beautiful, but they bring heavy leaf drop, shaded lawns and limbs that need regular attention. We help Raleigh homeowners keep trees trimmed, leaves cleared and lawns healthy underneath.',
        ],
        'challenges': [
            ('Big oaks and heavy leaf drop', 'The City of Oaks earns its name every fall. Regular leaf removal keeps lawns from being smothered.'),
            ('Limbs over homes', 'Mature trees grow over roofs, gutters and driveways. Periodic trimming keeps them safe and clear.'),
            ('Shady, thin lawns', 'Shade-tolerant fescue blends and fall overseeding help lawns hold on under big trees.'),
        ],
        'faqs': [
            ('Which parts of Raleigh do you serve?', 'We mainly serve southwest Raleigh, the side of the city closest to our Apex base. If you are elsewhere in Raleigh, call or text and we will let you know if we can help.'),
            ('Can grass grow under big oak trees?', 'It can be tough. Shade-tolerant fescue blends, fall overseeding, mowing high and thinning tree canopies to let in more light all help.'),
        ],
        'nearby': ['cary-nc', 'apex-nc', 'morrisville-nc'],
    },
]

# ---------------------------------------------------------------- Guides
GUIDES = [
    {
        'slug': 'fall-lawn-care-apex-nc',
        'title': 'Fall Lawn Care Guide for Apex & the Triangle',
        'desc': 'A simple fall lawn care plan for tall fescue lawns in Apex, Cary and the Triangle: when to aerate, overseed, fertilize and clear leaves.',
        'h1': 'Fall Lawn Care Guide for <span class="hl">Apex &amp; the Triangle</span>',
        'img': 'lawn',
        'summary': 'Fall is the most important season for tall fescue lawns. Here is what to do and when.',
        'body': '''
<p>If you have a tall fescue lawn, and most homes in Apex and the Triangle do, fall is the season that matters most. Fescue is a cool-season grass. It struggles through the summer heat and does most of its real growing and recovering when temperatures drop in September and October. What you do now decides how your lawn looks next spring.</p>

<h2>1. Aerate and overseed in September</h2>
<p>Early fall is the best time of year to aerate and overseed fescue. The window runs roughly from late August to mid-October, and September is ideal. Soil is still warm, so seed sprouts quickly, and the cooler weather that follows gives young grass time to establish before winter and, more importantly, before next summer.</p>
<p>Core aeration pulls plugs of soil out of the lawn, which relieves compaction in our heavy clay and gives new seed a protected spot with good soil contact. Leave the plugs on the lawn. They break down on their own in a couple of weeks.</p>

<h2>2. Water new seed the right way</h2>
<p>New seed needs the top of the soil to stay moist until it sprouts. That usually means light watering once or twice a day for the first one to two weeks. Once the new grass is up and growing, switch to deeper, less frequent watering so roots grow down instead of staying near the surface.</p>

<h2>3. Fertilize in fall, not summer</h2>
<p>Fescue makes the best use of fertilizer in the fall. A common schedule for the Triangle is to feed in September and again in November. Avoid heavy fertilizing in late spring and summer, which pushes growth when fescue is most stressed and invites disease. A soil test, available through the NC Department of Agriculture, tells you exactly what your lawn needs.</p>

<h2>4. Keep the leaves off</h2>
<p>Our oaks, maples and sweetgums drop most of their leaves from late October into December, right when fescue is growing and new seed is trying to establish. A thick layer of wet leaves blocks sunlight and can smother grass in a few weeks. Clear leaves regularly through the fall instead of waiting for one big cleanup at the end.</p>

<h2>5. Keep mowing</h2>
<p>Fescue keeps growing well into the fall. Keep mowing at about 3 to 3.5 inches, and wait until new seedlings are a few inches tall before mowing them for the first time. Mowing over a light layer of leaves can also chop them up and help them break down.</p>

<h2>Quick fall checklist</h2>
<ul class="checks">
<li>September: core aerate and overseed</li>
<li>September: first fall fertilizer application</li>
<li>Through October: keep new seed moist, then water deeply</li>
<li>October to December: clear leaves regularly</li>
<li>November: second fertilizer application</li>
</ul>
''',
        'related_services': ['aeration-overseeding', 'seasonal-cleanups', 'lawn-mowing'],
    },
    {
        'slug': 'mulch-vs-pine-straw',
        'title': 'Mulch vs. Pine Straw: Which Is Better?',
        'desc': 'Hardwood mulch or pine straw? Compare look, cost, how long each lasts, and which works best for North Carolina landscape beds.',
        'h1': 'Mulch vs. Pine Straw: <span class="hl">Which Is Better?</span>',
        'img': 'garden-path',
        'summary': 'Both are great choices for Carolina landscapes. Here is how to pick.',
        'body': '''
<p>Walk through any neighborhood in Apex or Cary and you will see both: dark hardwood mulch in some beds and golden pine straw in others. Both protect your plants and make the yard look finished. The right choice comes down to the look you want and the beds you have.</p>

<h2>What both of them do</h2>
<ul class="checks">
<li>Hold moisture in the soil through hot summers</li>
<li>Keep roots cooler in summer and protected in winter</li>
<li>Help keep weeds from sprouting</li>
<li>Give beds a clean, cared-for look</li>
</ul>

<h2>Pine straw</h2>
<p>Pine straw is a Southern classic. The long needles knit together into a mat, so it stays put on slopes and in heavy rain where mulch tends to wash out. It is light, easy to spread and suits the azaleas, camellias and hollies common in Triangle yards. The tradeoff is that it fades from rich brown to gray faster, so many homeowners refresh it twice a year.</p>

<h2>Hardwood mulch</h2>
<p>Hardwood mulch gives beds a darker, more formal look and holds its color longer. As it breaks down it adds organic matter to the soil, which our clay can use. It is heavier and can wash out of sloped beds in a hard storm, so it works best on flat or gently sloped areas.</p>

<h2>How much to use</h2>
<p>Whichever you pick, don't overdo it. About 2 to 3 inches of mulch, or a few inches of loose pine straw that settles down, is plenty. Thicker layers can keep water from reaching the soil. Always keep material pulled back from tree trunks and the side of the house. Mulch piled up against trunks, sometimes called a "mulch volcano," traps moisture against the bark and can slowly damage the tree.</p>

<h2>The quick answer</h2>
<p><strong>Choose pine straw</strong> for slopes, natural-looking beds and a classic Carolina look. <strong>Choose hardwood mulch</strong> for a darker, more formal look on flat beds where you want color that lasts.</p>
''',
        'related_services': ['mulch-pine-straw', 'seasonal-cleanups', 'hardscaping'],
    },
    {
        'slug': 'when-to-trim-trees-nc',
        'title': 'When to Trim Trees in North Carolina',
        'desc': 'The best time to trim trees in North Carolina, when to act right away, and warning signs that a tree near your home may be dangerous.',
        'h1': 'When to Trim Trees in <span class="hl">North Carolina</span>',
        'img': 'trees',
        'summary': 'Timing matters for healthy trees. Safety problems should never wait.',
        'body': '''
<p>Trees are a huge part of what makes the Triangle beautiful, and a big responsibility when they are growing over your house. Trimming at the right time keeps trees healthy. Knowing the warning signs keeps your family and your home safe.</p>

<h2>The best time: late fall through winter</h2>
<p>For most shade trees, the ideal time to prune is during dormancy, from late fall through late winter. With the leaves off you can clearly see the branch structure, there is less stress on the tree, and pruning cuts heal quickly once growth starts in spring.</p>

<h2>Anytime: dead, broken and dangerous limbs</h2>
<p>Some trimming should not wait for the right season. Dead branches, limbs cracked in a storm and branches rubbing on your roof should be dealt with as soon as you notice them. Summer thunderstorms and the remnants of tropical storms bring down limbs across Wake County every year.</p>

<h2>Warning signs a tree may be dangerous</h2>
<ul class="checks">
<li>The tree has started leaning recently</li>
<li>Soil is cracked or lifting at the base</li>
<li>Large dead limbs, especially over the house or driveway</li>
<li>Mushrooms growing on the trunk or roots</li>
<li>Deep cracks or splits in the trunk</li>
<li>Bare branches in the canopy when the rest of the tree has leaves</li>
</ul>
<p>If a tree near your home shows any of these signs, have it looked at soon, before the next storm.</p>

<h2>Avoid "topping"</h2>
<p>Cutting the top off a tree to make it shorter may seem like a quick fix, but it usually backfires. Topping leads to weak, fast-growing sprouts that break easily, and it can leave the tree open to decay. Proper trimming thins and shapes the tree instead.</p>

<h2>Check before you remove</h2>
<p>Many trees on private residential lots can be removed without a permit, but rules vary by town and property, and many HOAs require approval first. Check with your town and HOA before taking down a large tree.</p>
''',
        'related_services': ['tree-trimming-removal', 'seasonal-cleanups', 'lawn-mowing'],
    },
]

HOME_FAQS = [
    ('Do you offer free estimates?', 'Yes. Call, text or use the form on our contact page with your address and what you need, and we will get back to you with a price.'),
    ('What areas do you serve?', 'We are based in Apex, NC and serve Cary, Holly Springs, Fuquay-Varina, Morrisville and southwest Raleigh. Not sure if you are in range? Just ask.'),
    ('Do you handle both lawn care and tree work?', 'Yes. From weekly mowing to tree trimming and removal, one call covers everything outside your home.'),
    ('When is the best time to aerate and overseed?', 'For tall fescue lawns, the most common type in the Triangle, early fall is best, roughly late August through mid-October, with September ideal.'),
]

# ---------------------------------------------------------------- Reviews & projects
# Add real Google reviews here, copied word for word. Leave empty to hide the section.
# Example: {'name': 'Jane D.', 'text': 'Great work...', 'service': 'Lawn Mowing'}
REVIEWS = []

# Add real job photos here (files in images/projects/). Leave empty to show the
# "coming soon" message. 'before' is optional; when present a before/after slider is shown.
# Example: {'title': 'Backyard cleanup', 'town': 'Apex', 'service': 'seasonal-cleanups',
#           'after': 'projects/cleanup-after.jpg', 'before': 'projects/cleanup-before.jpg',
#           'text': 'Overgrown beds cleared, edged and finished with pine straw.'}
PROJECTS = []
