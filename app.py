import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="EARTH ON TRIAL // AURELIUS-9", page_icon="🇵🇰", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');
:root{--gold:#e5b84d;--jade:#0d8065;--ink:#050a10}
html,body,[data-testid="stAppViewContainer"]{background:#050910;color:#e9f1ee}
[data-testid="stHeader"],[data-testid="stToolbar"],#MainMenu,footer{display:none}
.block-container{padding:0!important;max-width:100%!important}
div[data-testid="stVerticalBlock"]{gap:0.5rem}
.hero{padding:24px 5vw 10px;background:radial-gradient(ellipse at 50% 0%,#174b5a 0%,#0a1a27 45%,#050910 100%);border-bottom:1px solid #b48b3b66}
.brand{font:800 clamp(28px,5vw,58px) Orbitron;letter-spacing:.08em;color:#f2c45e;text-shadow:0 0 26px #d89b37aa}
.kicker{font:14px 'Share Tech Mono';letter-spacing:.24em;color:#78c8b2}
.sub{font:600 18px Rajdhani;color:#d4e4df}
.panel{background:linear-gradient(145deg,#10232d,#09141c);border:1px solid #b88f4966;border-radius:14px;padding:18px;box-shadow:0 10px 45px #0008}
.metric{font:700 28px Orbitron;color:#efc45e}
.small{font:13px 'Share Tech Mono';color:#91aaa5}
.stButton>button{background:linear-gradient(90deg,#146c59,#1a9b78);color:#fff;border:1px solid #dfbd67;border-radius:8px;font:700 16px Orbitron;letter-spacing:.07em;min-height:44px}
.stButton>button:hover{border-color:#fff;box-shadow:0 0 20px #d9b64d66;color:white}
div[data-testid="stTextInput"] input,div[data-testid="stSelectbox"] div{background:#0b1c25;color:#fff;border:1px solid #46645e}
h1,h2,h3{font-family:Orbitron!important}
</style>
""",unsafe_allow_html=True)

if "pilot" not in st.session_state:
    st.session_state.pilot={"name":"Dr. Raza Qureshi","callsign":"RAZA-01","origin":"Karachi, Pakistan","role":"Planetary Evidence Scientist"}
if "mode" not in st.session_state: st.session_state.mode="briefing"
if "evidence" not in st.session_state: st.session_state.evidence=[]
if "credits" not in st.session_state: st.session_state.credits=100
if "days" not in st.session_state: st.session_state.days=72
if "visited" not in st.session_state: st.session_state.visited=[]
if "shipname" not in st.session_state: st.session_state.shipname="SHAHPAR-E"
if "ending" not in st.session_state: st.session_state.ending=None

st.markdown("""<div class="hero">
<div class="kicker">UNITED GALACTIC TRIBUNAL // DEFENCE DIVISION // PAKISTAN</div>
<div class="brand">EARTH <span style="color:#f4eee1">ON</span> TRIAL</div>
<div class="sub">A cinematic planetary investigation // BUILD 01.0.0</div>
</div>""",unsafe_allow_html=True)

# Three.js game surface: self-contained interactive cockpit exploration with keyboard and touch.
game_html = r"""
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<style>
*{box-sizing:border-box}body{margin:0;background:#030911;color:#e8f2eb;font-family:Arial;overflow:hidden}
#wrap{position:relative;width:100%;height:590px;background:radial-gradient(ellipse at 50% 35%,#17415a 0%,#091a2c 48%,#030911 100%);overflow:hidden;border:1px solid #9b834d;border-radius:12px}
canvas{display:block;width:100%;height:100%}
.hud{position:absolute;inset:14px 16px auto;pointer-events:none;display:flex;justify-content:space-between;gap:10px;font:12px monospace;letter-spacing:1px;text-shadow:0 0 8px #54d7c1}
.tag{border:1px solid #65bda688;background:#061822bb;padding:8px 11px;border-radius:6px}
#cross{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);color:#eac75e;font-size:28px;opacity:.65;pointer-events:none}
#toast{position:absolute;bottom:72px;left:50%;transform:translateX(-50%);background:#071a22eF;border:1px solid #e0bb59;padding:10px 18px;border-radius:7px;font:13px monospace;max-width:90%;text-align:center}
#controls{position:absolute;bottom:12px;left:12px;right:12px;display:flex;justify-content:space-between;align-items:end}
.pad{display:grid;grid-template-columns:42px 42px 42px;grid-template-rows:38px 38px;gap:4px}
.pad button,.act{background:#071a22cc;color:#f4d476;border:1px solid #d2ad55;border-radius:7px;font-size:17px;touch-action:none}
.pad button:nth-child(1){grid-column:2}.pad button:nth-child(2){grid-column:1;grid-row:2}.pad button:nth-child(3){grid-column:2;grid-row:2}.pad button:nth-child(4){grid-column:3;grid-row:2}
.actions{display:flex;gap:7px}.act{padding:10px 13px;font:12px monospace}
@media(min-width:850px){#wrap{height:610px}}
</style></head><body><div id="wrap">
<div class="hud"><div class="tag">AURELIUS-9 // PAKISTANI EXPEDITION VESSEL</div><div class="tag" id="coord">SECTOR 01 // HANGAR</div></div>
<div id="cross">⊕</div><div id="toast">WELCOME ABOARD, COMMANDER. USE WASD / ARROW KEYS TO EXPLORE THE HANGAR.</div>
<div id="controls"><div class="pad"><button data-k="ArrowUp">▲</button><button data-k="ArrowLeft">◀</button><button data-k="ArrowDown">▼</button><button data-k="ArrowRight">▶</button></div><div class="actions"><button class="act" id="interact">E · INTERACT</button><button class="act" id="map">M · MAP</button></div></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
(()=>{
const root=document.getElementById('wrap'),toast=document.getElementById('toast'),coord=document.getElementById('coord');
const scene=new THREE.Scene();scene.fog=new THREE.FogExp2(0x071522,.023);
const camera=new THREE.PerspectiveCamera(68,root.clientWidth/root.clientHeight,.1,300);
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.7));renderer.setSize(root.clientWidth,root.clientHeight);renderer.shadowMap.enabled=true;root.prepend(renderer.domElement);
scene.add(new THREE.HemisphereLight(0x9ad8ed,0x15202b,2));
const key=new THREE.PointLight(0x50d4c3,35,65);key.position.set(0,9,0);scene.add(key);
const gold=new THREE.PointLight(0xe6ad4c,22,50);gold.position.set(-12,5,-10);scene.add(gold);
const floor=new THREE.Mesh(new THREE.PlaneGeometry(90,90),new THREE.MeshStandardMaterial({color:0x0a1820,metalness:.65,roughness:.45}));floor.rotation.x=-Math.PI/2;floor.position.y=-.1;scene.add(floor);
const grid=new THREE.GridHelper(80,60,0x286c69,0x193b42);grid.position.y=.01;scene.add(grid);
function box(x,y,z,sx,sy,sz,color,metal=.5){let m=new THREE.Mesh(new THREE.BoxGeometry(sx,sy,sz),new THREE.MeshStandardMaterial({color,metalness:metal,roughness:.36}));m.position.set(x,y,z);scene.add(m);return m}
function glow(x,y,z,r,color){let m=new THREE.Mesh(new THREE.SphereGeometry(r,18,14),new THREE.MeshBasicMaterial({color}));m.position.set(x,y,z);scene.add(m)}
// Hangar ribs and Pakistan truck-art inspired teal, marigold and floral ornament bands.
for(let z=-28;z<=22;z+=8){box(-17,5,z,.8,11,.8,0x24414b);box(17,5,z,.8,11,.8,0x24414b);box(0,10.5,z,35,.6,.7,0x31535a)}
for(let x=-16;x<=16;x+=4){box(x,.15,-8,.12,.08,48,0x286b63);box(x,.15,8,.12,.08,48,0x286b63)}
// central launch vessel, stylised but navigable hangar
const ship=new THREE.Group();scene.add(ship);
let hull=new THREE.Mesh(new THREE.CapsuleGeometry(1.7,6,6,12),new THREE.MeshStandardMaterial({color:0x123f43,metalness:.8,roughness:.25}));hull.rotation.x=Math.PI/2;ship.add(hull);
let nose=new THREE.Mesh(new THREE.ConeGeometry(1.7,3,12),new THREE.MeshStandardMaterial({color:0xc9a04f,metalness:.7}));nose.rotation.x=-Math.PI/2;nose.position.z=-4.3;ship.add(nose);
for(let s of [-1,1]){let wing=box(s*3,.0,1,3,.22,5,0xd2a84e,.75);ship.add(wing);let light=new THREE.PointLight(0x39ffd1,7,8);light.position.set(s*3,.2,1);ship.add(light)}
ship.position.set(0,2,-14);
for(let x of [-13,13]){box(x,2,-3,2,4,2,0x1c343c);glow(x,4,-3,.22,0xe4b94c)}
// Decor panels with floral rosettes inspired by truck-art patterns.
for(let z=-22;z<20;z+=5){for(let x of [-16.45,16.45]){glow(x,5,z,.35,0xd39b43);glow(x,5,z,.18,0x43bea4);}}
let avatar=new THREE.Group();scene.add(avatar);
let body=new THREE.Mesh(new THREE.CapsuleGeometry(.48,.9,5,10),new THREE.MeshStandardMaterial({color:0x176b56,roughness:.75}));body.position.y=1.05;avatar.add(body);
let head=new THREE.Mesh(new THREE.SphereGeometry(.34,16,12),new THREE.MeshStandardMaterial({color:0xb77e5e}));head.position.y=1.9;avatar.add(head);
let cap=new THREE.Mesh(new THREE.CylinderGeometry(.37,.37,.12,16),new THREE.MeshStandardMaterial({color:0x164f42}));cap.position.y=2.2;avatar.add(cap);
avatar.position.set(0,0,5);camera.position.set(0,4,12);
let keys={},vel=new THREE.Vector3(),yaw=0,mode='hangar',active=null,visited=[];
const missions=[
{name:'KARACHI // COASTAL FRONTIER',type:'CITY',x:-25,z:-24,desc:'Investigate coastal waste, drainage and urban resilience around Karachi.',evidence:'Karachi Coastal Resilience Dossier',value:28},
{name:'AMAZON // BIOSPHERE ARCHIVE',type:'BIOME',x:25,z:-24,desc:'Document the pressure on forest ecosystems and biodiversity.',evidence:'Amazon Biodiversity Record',value:24},
{name:'ARCTIC // CRYOSPHERE STATION',type:'POLAR',x:-25,z:18,desc:'Study ice loss and the impact of a warming climate.',evidence:'Cryosphere Observation Log',value:26},
{name:'ORBITAL // ATMOSPHERE ARRAY',type:'ORBIT',x:25,z:18,desc:'Retrieve atmospheric monitoring records.',evidence:'Atmospheric Composition Brief',value:22}
];
missions.forEach((m,i)=>{box(m.x,1.2,m.z,5,2.4,5,0x143a42,.7);box(m.x,2.5,m.z,5.2,.15,5.2,0xc69b4a);glow(m.x,4,m.z,.8,i%2?0x35d0ac:0xf0bf56);});
let mapShown=false;
function say(t){toast.textContent=t}
function interact(){let pos=avatar.position;let nearest=null,dist=1e9;
for(let m of missions){let d=Math.hypot(pos.x-m.x,pos.z-m.z);if(d<dist){dist=d;nearest=m}}
if(dist<8){active=nearest;mode='mission';say('LANDING ZONE SECURED // '+nearest.name+' // Return to the mission panel below to investigate.');window.parent.postMessage({type:'EOT_ZONE',name:nearest.name},'*')}
else if(Math.hypot(pos.x, pos.z+14)<8){say('AURELIUS-9 // SHIP SYSTEMS ONLINE. NAVIGATE TO A MISSION BEACON.')}
else{say('NO INTERACTION IN RANGE. APPROACH A GOLD MISSION BEACON OR THE SHIP.')}
}
function keydown(e){if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight',' '].includes(e.key)){e.preventDefault()}keys[e.key.toLowerCase()]=true;if(e.key.toLowerCase()==='e')interact();if(e.key.toLowerCase()==='m'){mapShown=!mapShown;say(mapShown?'MISSION BEACONS: KARACHI / AMAZON / ARCTIC / ORBIT':'MAP CLOSED');window.parent.postMessage({type:'EOT_MAP'},'*')}}
function keyup(e){keys[e.key.toLowerCase()]=false}
window.addEventListener('keydown',keydown);window.addEventListener('keyup',keyup);
document.querySelectorAll('[data-k]').forEach(b=>{let k=b.dataset.k.toLowerCase();b.addEventListener('pointerdown',e=>{e.preventDefault();keys[k]=true});['pointerup','pointerleave','pointercancel'].forEach(ev=>b.addEventListener(ev,()=>keys[k]=false))});
document.getElementById('interact').onclick=interact;document.getElementById('map').onclick=()=>{mapShown=!mapShown;interactMap()};
function interactMap(){say(mapShown?'MISSION BEACONS: KARACHI / AMAZON / ARCTIC / ORBIT':'MAP CLOSED');window.parent.postMessage({type:'EOT_MAP'},'*')}
let last=performance.now();
function animate(now){requestAnimationFrame(animate);let dt=Math.min((now-last)/1000,.04);last=now;
let f=(keys['w']||keys['arrowup']?1:0)-(keys['s']||keys['arrowdown']?1:0),side=(keys['d']||keys['arrowright']?1:0)-(keys['a']||keys['arrowleft']?1:0);
let dir=new THREE.Vector3(side,0,-f);if(dir.length()>0){dir.normalize().multiplyScalar(10*dt);avatar.position.add(dir);avatar.position.x=THREE.MathUtils.clamp(avatar.position.x,-32,32);avatar.position.z=THREE.MathUtils.clamp(avatar.position.z,-32,28);avatar.rotation.y=Math.atan2(dir.x,-dir.z)}
camera.position.lerp(new THREE.Vector3(avatar.position.x,avatar.position.y+4.2,avatar.position.z+8),.09);camera.lookAt(avatar.position.x,1.2,avatar.position.z-2);
ship.rotation.y=Math.sin(now*.0004)*.04;coord.textContent='HANGAR GRID // '+Math.round(avatar.position.x)+':'+Math.round(avatar.position.z);
renderer.render(scene,camera)}
requestAnimationFrame(animate);window.addEventListener('resize',()=>{camera.aspect=root.clientWidth/root.clientHeight;camera.updateProjectionMatrix();renderer.setSize(root.clientWidth,root.clientHeight)});
})();
</script></body></html>
"""
st.markdown('<div style="padding:14px 2vw 0"><div class="kicker">FLIGHT DECK // LIVE ENVIRONMENT</div></div>',unsafe_allow_html=True)
components.html(game_html,height=615,scrolling=False)

st.markdown('<div style="padding:10px 2vw 0">',unsafe_allow_html=True)
c1,c2,c3,c4=st.columns(4)
for col,label,val in [(c1,"GALACTIC CLOCK",f"{st.session_state.days} HRS"),(c2,"DEFENCE CREDITS",str(st.session_state.credits)),(c3,"EVIDENCE FILES",str(len(st.session_state.evidence))),(c4,"MISSIONS VISITED",str(len(st.session_state.visited)))]:
    with col: st.markdown(f'<div class="panel"><div class="small">{label}</div><div class="metric">{val}</div></div>',unsafe_allow_html=True)
st.markdown("</div>",unsafe_allow_html=True)

tabs=st.tabs(["✦ COMMAND DECK","✦ FIELD MISSIONS","✦ EVIDENCE ARCHIVE","✦ CHARACTER & SHIP","✦ THE TRIBUNAL"])
with tabs[0]:
    a,b=st.columns([1.3,1])
    with a:
        st.markdown('<div class="panel"><div class="kicker">MISSION DIRECTIVE // 001</div><h2>DEFEND THE BLUE WORLD</h2><p class="sub">The United Galactic Tribunal has charged Earth with ecological negligence. You have 72 galactic hours to gather credible evidence and prepare a defence.</p><p>Command the AURELIUS-9, an expedition vessel redesigned with Pakistani truck-art motifs, emerald enamel, brass filigree and hand-painted floral geometry.</p><div class="small">PRIMARY OBJECTIVE: BUILD A DEFENSIBLE CASE BEFORE THE CLOCK EXPIRES.</div></div>',unsafe_allow_html=True)
    with b:
        st.markdown('<div class="panel"><div class="kicker">YOUR SCIENTIST</div><div class="metric">DR. RAZA QURESHI</div><div class="sub">Planetary Evidence Scientist // Karachi, Pakistan</div><p>Former coastal systems researcher, now appointed to the Earth Defence Division.</p><div class="small">SPECIALTY: FIELD FORENSICS · CLIMATE SYSTEMS · PLANETARY POLICY</div></div>',unsafe_allow_html=True)
    if st.button("START / RESUME INVESTIGATION",use_container_width=True):
        st.session_state.mode="active";st.success("Investigation started. Explore the hangar above and approach a gold beacon. Use E to interact.")
with tabs[1]:
    st.markdown("### MISSION SELECT // FIELD OPERATIONS")
    st.caption("Approach each gold beacon in the 3D hangar, or launch a field investigation here. A field operation consumes galactic hours.")
    missions=[
      ("KARACHI — COASTAL FRONTIER","Pakistan · Coastal resilience","Investigate urban water systems, coastal waste and community adaptation.",28,18),
      ("AMAZON — BIOSPHERE ARCHIVE","Brazil · Biodiversity","Build a record of ecosystem services and biodiversity pressure.",24,16),
      ("ARCTIC — CRYOSPHERE STATION","Arctic · Climate science","Assess ice observations and climate indicators.",26,18),
      ("ORBITAL — ATMOSPHERE ARRAY","Low Earth orbit · Atmosphere","Analyse atmospheric monitoring and greenhouse-gas records.",22,14)
    ]
    for i,(name,loc,desc,reward,cost) in enumerate(missions):
        with st.container(border=True):
            x,y=st.columns([3,1])
            with x: st.markdown(f"**{name}**");st.caption(loc);st.write(desc)
            with y:
                st.metric("Evidence value",f"+{reward}")
                if st.button("INVESTIGATE",key=f"m{i}",disabled=name in st.session_state.visited or st.session_state.days<cost):
                    st.session_state.evidence.append({"mission":name,"file":["Karachi Coastal Resilience Dossier","Amazon Biodiversity Record","Cryosphere Observation Log","Atmospheric Composition Brief"][i],"value":reward,"note":desc})
                    st.session_state.visited.append(name);st.session_state.credits-=cost//3;st.session_state.days-=cost
                    st.success("Evidence secured and archived.")
with tabs[2]:
    st.markdown("### EVIDENCE ARCHIVE // COURT-ADMISSIBLE MATERIAL")
    if not st.session_state.evidence: st.info("No evidence secured yet. Complete field missions to build your defence.")
    for i,e in enumerate(st.session_state.evidence):
        st.markdown(f'<div class="panel"><div class="kicker">EXHIBIT {i+1:02d} // FIELD VERIFIED</div><h3>{e["file"]}</h3><p>{e["mission"]}</p><div class="small">DEFENCE VALUE: +{e["value"]} · {e["note"]}</div></div>',unsafe_allow_html=True)
with tabs[3]:
    st.markdown("### PERSONNEL & VESSEL CUSTOMISATION")
    left,right=st.columns(2)
    with left:
        st.markdown("#### SCIENTIST PROFILE")
        nm=st.text_input("Scientist name",value=st.session_state.pilot["name"])
        call=st.text_input("Callsign",value=st.session_state.pilot["callsign"])
        origin=st.selectbox("Home base",["Karachi, Pakistan","Lahore, Pakistan","Islamabad, Pakistan","Peshawar, Pakistan","Quetta, Pakistan","Other"],index=0)
        role=st.selectbox("Specialisation",["Planetary Evidence Scientist","Climate Systems Analyst","Oceanographer","Biodiversity Researcher","Space Systems Engineer"])
        if st.button("SAVE SCIENTIST PROFILE"): st.session_state.pilot={"name":nm,"callsign":call,"origin":origin,"role":role};st.success("Profile saved.")
    with right:
        st.markdown("#### VESSEL CONFIGURATION")
        sn=st.text_input("Spaceship name",value=st.session_state.shipname)
        theme=st.selectbox("Interior livery",["Truck-art emerald & marigold","Indus blue & copper","Desert rose & brass","Monochrome stealth"])
        st.markdown('<div class="panel"><div class="kicker">PAKISTANI DESIGN LANGUAGE</div><h3 style="color:#e7bd55">AJRAK · PHULKARI · TRUCK ART</h3><p>Hand-painted floral rosettes, mirror-work inspired light panels, emerald enamel, brass trim and geometric borders.</p></div>',unsafe_allow_html=True)
        if st.button("REFIT VESSEL"): st.session_state.shipname=sn;st.success(f"{sn} refit queued with {theme} livery.")
with tabs[4]:
    st.markdown("### UNITED GALACTIC TRIBUNAL")
    st.write("The prosecution alleges that Earth has failed its obligations to the galactic biosphere. Your task is to present a proportionate, evidence-led defence.")
    total=sum(e["value"] for e in st.session_state.evidence)
    st.metric("Current evidence strength",f"{total} / 100")
    choice=st.radio("Choose your closing strategy",["Humanity can reform: submit a binding planetary restoration plan.","The evidence is incomplete: request a monitored probation period.","Earth's record is mixed: present context and request a conditional acquittal."],index=0)
    if st.button("SUBMIT FINAL DEFENCE",use_container_width=True):
        if len(st.session_state.evidence)<2: st.warning("The court requires at least two exhibits. Complete more investigations first.")
        else:
            if total>=70: verdict="CONDITIONAL ACQUITTAL";detail="Earth is granted another chance under a binding planetary restoration charter."
            elif total>=45: verdict="PROBATION";detail="Earth must meet measurable recovery milestones under galactic observation."
            else: verdict="DEFERRED VERDICT";detail="The tribunal orders further investigation before issuing a final ruling."
            st.session_state.ending=(verdict,detail)
    if st.session_state.ending:
        st.markdown(f'<div class="panel"><div class="kicker">OFFICIAL TRIBUNAL RULING</div><div class="brand" style="font-size:clamp(24px,4vw,42px)">{st.session_state.ending[0]}</div><p class="sub">{st.session_state.ending[1]}</p></div>',unsafe_allow_html=True)

st.markdown('<div style="padding:20px 2vw;color:#76918d;font:12px monospace;text-align:center">EARTH ON TRIAL // AURELIUS-9 // A FICTIONAL STRATEGY EXPERIENCE INSPIRED BY REAL PLANETARY SCIENCE<br>PAKISTAN BUILT · EARTH DEFENCE DIVISION · BUILD 01</div>',unsafe_allow_html=True)
