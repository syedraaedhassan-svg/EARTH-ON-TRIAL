import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="EARTH ON TRIAL // AURELIUS-9", page_icon="🇵🇰", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@500;700&family=Share+Tech+Mono&display=swap');
[data-testid="stAppViewContainer"]{background:#050910;color:#e9f1ee}
[data-testid="stHeader"],#MainMenu,footer{display:none}
.block-container{padding:0!important;max-width:100%!important}
.hero{padding:25px 5vw;background:radial-gradient(ellipse at 50% 0%,#174b5a,#0a1a27 55%,#050910);border-bottom:1px solid #b48b3b66}
.brand{font:900 clamp(30px,5vw,58px) Orbitron;letter-spacing:.08em;color:#f2c45e;text-shadow:0 0 26px #d89b37aa}
.kicker{font:13px 'Share Tech Mono';letter-spacing:.2em;color:#78c8b2}
.panel{background:linear-gradient(145deg,#10232d,#09141c);border:1px solid #b88f4966;border-radius:14px;padding:16px}
.metric{font:700 26px Orbitron;color:#efc45e}
.stButton>button{background:linear-gradient(90deg,#146c59,#1a9b78);color:white;border:1px solid #dfbd67;border-radius:8px;font:700 15px Orbitron;min-height:42px}
</style>""",unsafe_allow_html=True)
if "profile" not in st.session_state: st.session_state.profile={"name":"Dr. Raza Qureshi","call":"RAZA-01","origin":"Karachi, Pakistan","speciality":"Planetary Evidence Scientist"}
if "evidence" not in st.session_state: st.session_state.evidence=[]
if "hours" not in st.session_state: st.session_state.hours=72
if "credits" not in st.session_state: st.session_state.credits=100
if "visited" not in st.session_state: st.session_state.visited=[]
if "ship" not in st.session_state: st.session_state.ship="SHAHPAR-E"
if "verdict" not in st.session_state: st.session_state.verdict=None
st.markdown('<div class="hero"><div class="kicker">UNITED GALACTIC TRIBUNAL // DEFENCE DIVISION // PAKISTAN</div><div class="brand">EARTH <span style="color:#f4eee1">ON</span> TRIAL</div><div style="font:700 18px Rajdhani;color:#d4e4df">A CINEMATIC PLANETARY INVESTIGATION // BUILD 01</div></div>',unsafe_allow_html=True)

game = r"""<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><style>
*{box-sizing:border-box}body{margin:0;background:#030911;color:#e8f2eb;font-family:Arial;overflow:hidden}
#wrap{position:relative;width:100%;height:570px;background:radial-gradient(ellipse at 50% 35%,#17415a,#091a2c 48%,#030911);overflow:hidden;border:1px solid #9b834d;border-radius:12px}
canvas{display:block;width:100%;height:100%}.hud{position:absolute;inset:12px 14px auto;display:flex;justify-content:space-between;gap:8px;font:12px monospace;pointer-events:none}
.tag{border:1px solid #65bda688;background:#061822dd;padding:8px;border-radius:6px}
#toast{position:absolute;bottom:66px;left:50%;transform:translateX(-50%);background:#071a22ef;border:1px solid #e0bb59;padding:10px 14px;border-radius:7px;font:12px monospace;text-align:center;width:90%}
#controls{position:absolute;bottom:9px;left:10px;right:10px;display:flex;justify-content:space-between;align-items:end}
.pad{display:grid;grid-template-columns:40px 40px 40px;grid-template-rows:36px 36px;gap:4px}
button{background:#071a22ed;color:#f4d476;border:1px solid #d2ad55;border-radius:7px;touch-action:none}
.pad button:nth-child(1){grid-column:2}.pad button:nth-child(2){grid-column:1;grid-row:2}.pad button:nth-child(3){grid-column:2;grid-row:2}.pad button:nth-child(4){grid-column:3;grid-row:2}
.act{padding:11px;font:12px monospace}
</style></head><body><div id="wrap"><div class="hud"><div class="tag">AURELIUS-9 // PAKISTANI EXPEDITION VESSEL</div><div class="tag" id="coord">HANGAR // DECK 01</div></div><div id="toast">WELCOME ABOARD. WASD / ARROW KEYS TO EXPLORE. APPROACH A GOLD BEACON AND PRESS E.</div><div id="controls"><div class="pad"><button data-k="ArrowUp">▲</button><button data-k="ArrowLeft">◀</button><button data-k="ArrowDown">▼</button><button data-k="ArrowRight">▶</button></div><button class="act" id="interact">E · INTERACT</button></div></div>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script><script>
(()=>{const root=document.getElementById('wrap'),toast=document.getElementById('toast'),coord=document.getElementById('coord');
const scene=new THREE.Scene();scene.fog=new THREE.FogExp2(0x071522,.023);const camera=new THREE.PerspectiveCamera(68,root.clientWidth/root.clientHeight,.1,300);
const renderer=new THREE.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.7));renderer.setSize(root.clientWidth,root.clientHeight);root.prepend(renderer.domElement);
scene.add(new THREE.HemisphereLight(0x9ad8ed,0x15202b,2));let light=new THREE.PointLight(0x50d4c3,35,65);light.position.set(0,9,0);scene.add(light);
function box(x,y,z,sx,sy,sz,color){let m=new THREE.Mesh(new THREE.BoxGeometry(sx,sy,sz),new THREE.MeshStandardMaterial({color,metalness:.65,roughness:.35}));m.position.set(x,y,z);scene.add(m);return m}
function orb(x,y,z,r,c){let m=new THREE.Mesh(new THREE.SphereGeometry(r,18,14),new THREE.MeshBasicMaterial({color:c}));m.position.set(x,y,z);scene.add(m)}
let floor=new THREE.Mesh(new THREE.PlaneGeometry(90,90),new THREE.MeshStandardMaterial({color:0x0a1820,metalness:.65}));floor.rotation.x=-Math.PI/2;floor.position.y=-.1;scene.add(floor);let grid=new THREE.GridHelper(80,60,0x286c69,0x193b42);grid.position.y=.01;scene.add(grid);
for(let z=-28;z<=22;z+=8){box(-17,5,z,.8,11,.8,0x24414b);box(17,5,z,.8,11,.8,0x24414b);box(0,10.5,z,35,.6,.7,0x31535a)}
for(let z=-22;z<20;z+=5)for(let x of [-16.4,16.4]){orb(x,5,z,.34,0xd39b43);orb(x,5,z,.17,0x43bea4)}
const ship=new THREE.Group();scene.add(ship);let hull=new THREE.Mesh(new THREE.CapsuleGeometry(1.7,6,6,12),new THREE.MeshStandardMaterial({color:0x123f43,metalness:.8}));hull.rotation.x=Math.PI/2;ship.add(hull);let nose=new THREE.Mesh(new THREE.ConeGeometry(1.7,3,12),new THREE.MeshStandardMaterial({color:0xc9a04f}));nose.rotation.x=-Math.PI/2;nose.position.z=-4.3;ship.add(nose);
for(let s of [-1,1]){let wing=new THREE.Mesh(new THREE.BoxGeometry(3,.22,5),new THREE.MeshStandardMaterial({color:0xd2a84e}));wing.position.set(s*3,0,1);ship.add(wing)}ship.position.set(0,2,-14);
let avatar=new THREE.Group();scene.add(avatar);let body=new THREE.Mesh(new THREE.CapsuleGeometry(.48,.9,5,10),new THREE.MeshStandardMaterial({color:0x176b56}));body.position.y=1.05;avatar.add(body);let head=new THREE.Mesh(new THREE.SphereGeometry(.34,16,12),new THREE.MeshStandardMaterial({color:0xb77e5e}));head.position.y=1.9;avatar.add(head);let cap=new THREE.Mesh(new THREE.CylinderGeometry(.37,.37,.12,16),new THREE.MeshStandardMaterial({color:0x164f42}));cap.position.y=2.2;avatar.add(cap);avatar.position.set(0,0,5);
let missions=[{name:'KARACHI // COASTAL FRONTIER',x:-25,z:-24},{name:'AMAZON // BIOSPHERE ARCHIVE',x:25,z:-24},{name:'ARCTIC // CRYOSPHERE STATION',x:-25,z:18},{name:'ORBITAL // ATMOSPHERE ARRAY',x:25,z:18}];
missions.forEach((m,i)=>{box(m.x,1.2,m.z,5,2.4,5,0x143a42);box(m.x,2.5,m.z,5.2,.15,5.2,0xc69b4a);orb(m.x,4,m.z,.8,i%2?0x35d0ac:0xf0bf56)});
let keys={};function say(t){toast.textContent=t}function interact(){let p=avatar.position,n=null,d=999;for(let m of missions){let q=Math.hypot(p.x-m.x,p.z-m.z);if(q<d){d=q;n=m}}if(d<8){say('LANDING ZONE SECURED // '+n.name+' // LAUNCH THE FIELD MISSION BELOW.');window.parent.postMessage({type:'EOT_ZONE',name:n.name},'*')}else if(Math.hypot(p.x,p.z+14)<8)say('AURELIUS-9 SYSTEMS ONLINE. NAVIGATE TO A GOLD BEACON.');else say('NO INTERACTION IN RANGE. APPROACH A GOLD MISSION BEACON.')}
function kd(e){if(e.key.startsWith('Arrow'))e.preventDefault();keys[e.key.toLowerCase()]=true;if(e.key.toLowerCase()==='e')interact()}function ku(e){keys[e.key.toLowerCase()]=false}window.addEventListener('keydown',kd);window.addEventListener('keyup',ku);
document.querySelectorAll('[data-k]').forEach(b=>{let k=b.dataset.k.toLowerCase();b.onpointerdown=e=>{e.preventDefault();keys[k]=true};['pointerup','pointerleave','pointercancel'].forEach(ev=>b.addEventListener(ev,()=>keys[k]=false))});document.getElementById('interact').onclick=interact;
let last=performance.now();function animate(now){requestAnimationFrame(animate);let dt=Math.min((now-last)/1000,.04);last=now;let f=(keys['w']||keys['arrowup']?1:0)-(keys['s']||keys['arrowdown']?1:0),side=(keys['d']||keys['arrowright']?1:0)-(keys['a']||keys['arrowleft']?1:0);let dir=new THREE.Vector3(side,0,-f);if(dir.length()){dir.normalize().multiplyScalar(10*dt);avatar.position.add(dir);avatar.position.x=THREE.MathUtils.clamp(avatar.position.x,-32,32);avatar.position.z=THREE.MathUtils.clamp(avatar.position.z,-32,28);avatar.rotation.y=Math.atan2(dir.x,-dir.z)}camera.position.lerp(new THREE.Vector3(avatar.position.x,4.2,avatar.position.z+8),.09);camera.lookAt(avatar.position.x,1.2,avatar.position.z-2);ship.rotation.y=Math.sin(now*.0004)*.04;coord.textContent='GRID '+Math.round(avatar.position.x)+' / '+Math.round(avatar.position.z);renderer.render(scene,camera)}requestAnimationFrame(animate);
window.addEventListener('resize',()=>{camera.aspect=root.clientWidth/root.clientHeight;camera.updateProjectionMatrix();renderer.setSize(root.clientWidth,root.clientHeight)});})();
</script></body></html>"""

# Render the game component and all Streamlit controls below it.
components.html(game, height=590, scrolling=False)

st.markdown('<div style="padding:12px 2vw 0">', unsafe_allow_html=True)
cols=st.columns(4)
for col,label,value in zip(cols,["GALACTIC CLOCK","DEFENCE CREDITS","EVIDENCE FILES","MISSIONS VISITED"],[f"{st.session_state.hours} HRS",st.session_state.credits,len(st.session_state.evidence),len(st.session_state.visited)]):
    with col:
        st.markdown(f'<div class="panel"><div class="kicker">{label}</div><div class="metric">{value}</div></div>',unsafe_allow_html=True)
st.markdown("</div>",unsafe_allow_html=True)

tabs=st.tabs(["COMMAND DECK","FIELD MISSIONS","EVIDENCE ARCHIVE","SCIENTIST & SHIP","THE TRIBUNAL"])
missions=[
("KARACHI — COASTAL FRONTIER","Pakistan · Coastal resilience","Investigate urban water systems, coastal waste and community adaptation.",28,18,"Karachi Coastal Resilience Dossier"),
("AMAZON — BIOSPHERE ARCHIVE","Brazil · Biodiversity","Build a record of ecosystem services and biodiversity pressure.",24,16,"Amazon Biodiversity Record"),
("ARCTIC — CRYOSPHERE STATION","Arctic · Climate science","Assess ice observations and climate indicators.",26,18,"Cryosphere Observation Log"),
("ORBITAL — ATMOSPHERE ARRAY","Low Earth orbit · Atmosphere","Analyse atmospheric monitoring and greenhouse-gas records.",22,14,"Atmospheric Composition Brief")]
with tabs[0]:
    left,right=st.columns([1.4,1])
    with left:
        st.markdown('<div class="panel"><div class="kicker">MISSION DIRECTIVE // 001</div><h2>DEFEND THE BLUE WORLD</h2><p class="sub">The United Galactic Tribunal has charged Earth with ecological negligence. You have 72 galactic hours to gather evidence and prepare a defence.</p><p>Explore the AURELIUS-9, a Pakistani expedition vessel decorated with truck-art motifs, emerald enamel, brass filigree and hand-painted floral geometry.</p><div class="kicker">PRIMARY OBJECTIVE: BUILD A DEFENSIBLE CASE.</div></div>',unsafe_allow_html=True)
    with right:
        st.markdown('<div class="panel"><div class="kicker">YOUR SCIENTIST</div><div class="metric">DR. RAZA QURESHI</div><p class="sub">Planetary Evidence Scientist · Karachi, Pakistan</p><p>Coastal systems researcher appointed to the Earth Defence Division.</p></div>',unsafe_allow_html=True)
with tabs[1]:
    st.markdown("### FIELD OPERATIONS // SELECT A LANDING ZONE")
    st.caption("Explore the hangar above, then launch a field investigation here.")
    for i,(name,loc,desc,reward,cost,file) in enumerate(missions):
        with st.container(border=True):
            c1,c2=st.columns([3,1])
            with c1:
                st.markdown(f"**{name}**")
                st.caption(loc)
                st.write(desc)
            with c2:
                st.metric("Evidence value",f"+{reward}")
                if st.button("INVESTIGATE",key=f"mission{i}",disabled=name in st.session_state.visited or st.session_state.hours<cost):
                    st.session_state.evidence.append({"mission":name,"file":file,"value":reward,"note":desc})
                    st.session_state.visited.append(name)
                    st.session_state.credits-=cost//3
                    st.session_state.hours-=cost
                    st.success("Evidence secured and archived.")
                    st.rerun()
with tabs[2]:
    st.markdown("### EVIDENCE ARCHIVE // COURT-ADMISSIBLE MATERIAL")
    if not st.session_state.evidence:
        st.info("No evidence secured yet. Complete field investigations to build your defence.")
    for i,e in enumerate(st.session_state.evidence):
        st.markdown(f'<div class="panel"><div class="kicker">EXHIBIT {i+1:02d} // FIELD VERIFIED</div><h3>{e["file"]}</h3><p>{e["mission"]}</p><div class="kicker">DEFENCE VALUE: +{e["value"]} · {e["note"]}</div></div>',unsafe_allow_html=True)
with tabs[3]:
    left,right=st.columns(2)
    with left:
        st.markdown("### SCIENTIST PROFILE")
        name=st.text_input("Scientist name",st.session_state.profile["name"])
        call=st.text_input("Callsign",st.session_state.profile["call"])
        origin=st.selectbox("Home base",["Karachi, Pakistan","Lahore, Pakistan","Islamabad, Pakistan","Peshawar, Pakistan","Quetta, Pakistan"])
        speciality=st.selectbox("Specialisation",["Planetary Evidence Scientist","Climate Systems Analyst","Oceanographer","Biodiversity Researcher","Space Systems Engineer"])
        if st.button("SAVE SCIENTIST PROFILE"):
            st.session_state.profile={"name":name,"call":call,"origin":origin,"speciality":speciality}
            st.success("Profile saved.")
    with right:
        st.markdown("### VESSEL CONFIGURATION")
        ship=st.text_input("Spaceship name",st.session_state.ship)
        livery=st.selectbox("Interior livery",["Truck-art emerald & marigold","Indus blue & copper","Desert rose & brass","Monochrome stealth"])
        st.markdown('<div class="panel"><div class="kicker">PAKISTANI DESIGN LANGUAGE</div><h3 style="color:#e7bd55">AJRAK · PHULKARI · TRUCK ART</h3><p>Painted floral rosettes, mirror-work-inspired lighting, emerald enamel, brass trim and geometric borders.</p></div>',unsafe_allow_html=True)
        if st.button("REFIT VESSEL"):
            st.session_state.ship=ship
            st.success(f"{ship} refit queued with {livery} livery.")
with tabs[4]:
    st.markdown("### UNITED GALACTIC TRIBUNAL")
    st.write("The prosecution alleges that Earth has failed its obligations to the galactic biosphere. Present a proportionate, evidence-led defence.")
    total=sum(e["value"] for e in st.session_state.evidence)
    st.metric("Current evidence strength",f"{total} / 100")
    st.radio("Choose your closing strategy",["Humanity can reform: submit a binding restoration plan.","The evidence is incomplete: request monitored probation.","Present context and request a conditional acquittal."])
    if st.button("SUBMIT FINAL DEFENCE",use_container_width=True):
        if len(st.session_state.evidence)<2:
            st.warning("The tribunal requires at least two exhibits.")
        else:
            if total>=70:
                st.session_state.verdict=("CONDITIONAL ACQUITTAL","Earth is granted another chance under a planetary restoration charter.")
            elif total>=45:
                st.session_state.verdict=("PROBATION","Earth must meet measurable recovery milestones under galactic observation.")
            else:
                st.session_state.verdict=("DEFERRED VERDICT","The tribunal orders further investigation.")
    if st.session_state.verdict:
        st.markdown(f'<div class="panel"><div class="kicker">OFFICIAL TRIBUNAL RULING</div><div class="brand" style="font-size:clamp(24px,4vw,42px)">{st.session_state.verdict[0]}</div><p>{st.session_state.verdict[1]}</p></div>',unsafe_allow_html=True)
st.markdown('<div style="padding:20px;color:#76918d;font:12px monospace;text-align:center">EARTH ON TRIAL // AURELIUS-9 // PAKISTAN BUILT · EARTH DEFENCE DIVISION</div>',unsafe_allow_html=True)
