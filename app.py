import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="EARTH ON TRIAL", page_icon="🇵🇰", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
html,body,[data-testid="stApp"],[data-testid="stAppViewContainer"],.main,.block-container{margin:0!important;padding:0!important;width:100%!important;height:100%!important;max-width:none!important;overflow:hidden!important;background:#03070d!important}
[data-testid="stHeader"],[data-testid="stToolbar"],#MainMenu,footer,header{display:none!important}
iframe[title="streamlit.components.v1.html"]{position:fixed!important;inset:0!important;width:100vw!important;height:100vh!important;min-height:100vh!important;border:0!important;z-index:999999!important}
</style>
""", unsafe_allow_html=True)

game = r"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');
:root{--gold:#e7bd63;--green:#29b99a;--ink:#050a11;--panel:rgba(5,13,22,.88);--line:rgba(226,184,89,.45)}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#02050b;color:#eaf0ed;font-family:Rajdhani,Arial}
#game{position:fixed;inset:0;background:#02050b}#world{position:absolute;inset:0;width:100%;height:100%;display:block}
#shade{position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(0,0,0,.42),transparent 25%,transparent 75%,rgba(0,0,0,.3)),linear-gradient(0deg,rgba(0,0,0,.42),transparent 35%,rgba(0,0,0,.12))}
#boot,#lobby,#deploy,#pause,#mission,#profilePanel{position:absolute;inset:0;z-index:5}
#boot{display:flex;align-items:center;justify-content:center;flex-direction:column;background:#030710 url('https://assets.science.nasa.gov/dynamicimage/assets/science/psd/photojournal/pia/pia18/pia18913/PIA18913.jpg?crop=faces%2Cfocalpoint&fit=clip&h=1800&w=2600') center/cover no-repeat}
#boot:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(2,6,13,.88),rgba(2,6,13,.38)),linear-gradient(0deg,#030710 0%,transparent 60%)}
.bootcontent{z-index:1;text-align:center;width:min(700px,90vw)}.eyebrow{font:12px 'Share Tech Mono';letter-spacing:.32em;color:#72d7c1}.logo{font:900 clamp(40px,8vw,88px) Orbitron;line-height:1.02;letter-spacing:.045em;color:var(--gold);text-shadow:0 0 34px #b78a3c88}.logo span{color:#f4f0e5}.sub{font:700 15px Rajdhani;letter-spacing:.18em;color:#d9e3df;margin-top:16px}.loadline{height:3px;background:#34424b;margin:34px auto 12px;width:min(390px,80vw);overflow:hidden}.loadfill{height:100%;width:0;background:linear-gradient(90deg,#1a8f7a,#f1c76a);box-shadow:0 0 18px #e9bd59;transition:width .15s}.loadtext{font:11px 'Share Tech Mono';color:#a9c1bb;letter-spacing:.18em}
#lobby{display:none;background:linear-gradient(90deg,rgba(3,8,15,.94),rgba(3,8,15,.42) 50%,rgba(3,8,15,.82)),url('https://assets.science.nasa.gov/dynamicimage/assets/science/psd/photojournal/pia/pia18/pia18913/PIA18913.jpg?crop=faces%2Cfocalpoint&fit=clip&h=1800&w=2600') center/cover}
.topbar{position:absolute;left:4vw;right:4vw;top:26px;display:flex;justify-content:space-between;align-items:center}.miniBrand{font:700 15px Orbitron;letter-spacing:.16em;color:var(--gold)}.topright{font:11px 'Share Tech Mono';color:#9eb6b0;letter-spacing:.12em}
.lobbyTitle{position:absolute;left:5vw;top:20%;max-width:460px}.lobbyTitle h1{font:800 clamp(30px,5vw,56px) Orbitron;line-height:1.08;margin:12px 0;color:#f2c96d}.lobbyTitle p{font-size:19px;max-width:390px;color:#c5d3d0;line-height:1.35}
#pilot{position:absolute;left:52%;top:51%;transform:translate(-50%,-50%);width:min(34vw,420px);height:min(70vh,620px);filter:drop-shadow(0 15px 40px #000);pointer-events:none}
.lobbyCard{position:absolute;right:5vw;top:19%;width:min(360px,36vw);padding:22px;background:linear-gradient(145deg,rgba(9,23,32,.94),rgba(4,10,17,.9));border:1px solid var(--line);box-shadow:0 18px 60px #0008;backdrop-filter:blur(12px)}
.cardHead{font:12px 'Share Tech Mono';letter-spacing:.2em;color:#7fd7c2;margin-bottom:14px}.field{display:block;margin:12px 0}.field label{display:block;color:#a9c1bb;font:11px 'Share Tech Mono';letter-spacing:.12em;margin-bottom:6px}.field input,.field select{width:100%;background:#07131c;border:1px solid #48616a;color:#f1eee4;padding:12px;font:16px Rajdhani;outline:none}.field input:focus,.field select:focus{border-color:var(--gold)}
.btn{border:1px solid var(--gold);background:linear-gradient(100deg,#176c5b,#0c9a78);color:white;padding:14px 18px;font:700 13px Orbitron;letter-spacing:.12em;cursor:pointer;transition:.2s}.btn:hover{filter:brightness(1.2);transform:translateY(-1px)}.btn.secondary{background:#101c26;border-color:#71817e;color:#dce5df}.btn.wide{width:100%;margin-top:8px}.hint{font:11px 'Share Tech Mono';color:#809992;line-height:1.5;margin-top:12px}
#deploy{display:none;background:linear-gradient(90deg,rgba(2,7,14,.97),rgba(2,7,14,.72)),url('https://assets.science.nasa.gov/dynamicimage/assets/science/psd/photojournal/pia/pia18/pia18913/PIA18913.jpg?crop=faces%2Cfocalpoint&fit=clip&h=1800&w=2600') center/cover;padding:6vh 6vw}
.deployTitle{font:800 clamp(30px,5vw,56px) Orbitron;color:var(--gold);margin:8px 0}.destinations{display:grid;grid-template-columns:repeat(3,minmax(180px,1fr));gap:14px;margin-top:30px;max-width:1100px}.dest{min-height:180px;padding:18px;background:linear-gradient(145deg,#10232de8,#071019ed);border:1px solid #b58f4b77;cursor:pointer;transition:.2s}.dest:hover,.dest.selected{border-color:#f4d178;transform:translateY(-3px);box-shadow:0 12px 35px #0008}.dest .num{font:12px 'Share Tech Mono';color:#66c9b1}.dest h3{font:700 20px Orbitron;color:#f1c86d;margin:12px 0 7px}.dest p{font-size:16px;color:#a9bfba;margin:0}.deployFoot{display:flex;gap:14px;align-items:center;margin-top:24px}
#hud{display:none;position:absolute;inset:0;pointer-events:none;z-index:3}.hudTop{position:absolute;top:18px;left:22px;right:22px;display:flex;justify-content:space-between;align-items:start}.hudBox{background:rgba(3,12,18,.72);border:1px solid #b38c4b77;padding:10px 13px;backdrop-filter:blur(8px)}.hudSmall{font:10px 'Share Tech Mono';letter-spacing:.16em;color:#80cdbb}.hudValue{font:700 15px Orbitron;color:#f1ca6d;margin-top:4px}.crosshair{position:absolute;left:50%;top:50%;width:20px;height:20px;transform:translate(-50%,-50%)}.crosshair:before,.crosshair:after{content:"";position:absolute;background:#e9d59c;box-shadow:0 0 7px #e8bd63}.crosshair:before{width:1px;height:18px;left:9px;top:1px}.crosshair:after{height:1px;width:18px;top:9px;left:1px}.bottomHud{position:absolute;bottom:22px;left:22px;right:22px;display:flex;justify-content:space-between;align-items:end}.objective{max-width:420px;background:rgba(3,12,18,.8);border-left:3px solid var(--gold);padding:12px 16px}.objective b{display:block;font:12px 'Share Tech Mono';color:var(--gold);letter-spacing:.14em}.objective span{font-size:17px;color:#e2e9e5}.controlsHint{font:11px 'Share Tech Mono';color:#b6c6c0;text-align:right;line-height:1.8;background:#030c14bb;padding:10px 14px}.interact{position:absolute;left:50%;top:58%;transform:translateX(-50%);display:none;padding:9px 14px;background:#081720e8;border:1px solid var(--gold);color:#f5d47c;font:12px 'Share Tech Mono';white-space:nowrap}
#pause,#mission,#profilePanel{display:none;background:rgba(1,5,10,.78);backdrop-filter:blur(9px);align-items:center;justify-content:center}.modal{width:min(540px,90vw);padding:28px;background:linear-gradient(145deg,#10232d,#071019);border:1px solid var(--line);box-shadow:0 20px 90px #000}.modal h2{font:800 26px Orbitron;color:var(--gold);margin:8px 0 12px}.modal p{color:#c1d1cb;font-size:17px;line-height:1.4}.modalActions{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}
#toast{position:absolute;top:82px;left:50%;transform:translateX(-50%);padding:10px 16px;background:#071720ed;border:1px solid #5e988c;color:#dcebe5;font:12px 'Share Tech Mono';display:none;z-index:8}
#touch{display:none;position:absolute;bottom:25px;left:20px;right:20px;justify-content:space-between;pointer-events:auto;z-index:4}.touchpad{display:grid;grid-template-columns:46px 46px 46px;grid-template-rows:42px 42px;gap:4px}.touchpad button,.touchAction{background:#071a24cc;color:#f3d27a;border:1px solid #b38e51;border-radius:5px;font:14px Orbitron}.touchpad button:nth-child(1){grid-column:2}.touchpad button:nth-child(2){grid-column:1;grid-row:2}.touchpad button:nth-child(3){grid-column:2;grid-row:2}.touchpad button:nth-child(4){grid-column:3;grid-row:2}.touchAction{padding:12px}
@media(max-width:800px){.lobbyTitle{top:10%;left:6vw}.lobbyTitle h1{font-size:30px}.lobbyTitle p{font-size:15px;max-width:260px}#pilot{left:42%;top:57%;width:48vw;height:50vh}.lobbyCard{top:auto;bottom:3vh;right:4vw;width:52vw;padding:12px}.field{margin:7px 0}.field input,.field select{padding:8px}.field label{font-size:9px}.btn{padding:11px;font-size:10px}.destinations{grid-template-columns:1fr 1fr;gap:8px}.dest{min-height:130px;padding:12px}.dest h3{font-size:14px}.dest p{font-size:13px}#touch{display:flex}.controlsHint{display:none}.bottomHud{bottom:120px}.hudTop{left:10px;right:10px}.hudBox{padding:7px}.hudValue{font-size:11px}}
@media(max-width:520px){.lobbyTitle{top:8%}.lobbyTitle p{display:none}.lobbyCard{width:60vw}.destinations{grid-template-columns:1fr 1fr}.deployTitle{font-size:28px}}
</style></head><body>
<div id="game"><canvas id="world"></canvas><div id="shade"></div>
<section id="boot"><div class="bootcontent"><div class="eyebrow">PAKISTAN SPACE RESEARCH DIVISION PRESENTS</div><div class="logo">EARTH <span>ON</span> TRIAL</div><div class="sub">A PLANETARY DEFENCE EXPERIENCE</div><div class="loadline"><div class="loadfill" id="loadfill"></div></div><div class="loadtext" id="loadtext">INITIALISING AURELIUS-9 SYSTEMS · 0%</div></div></section>
<section id="lobby"><div class="topbar"><div class="miniBrand">EOT // AURELIUS-9</div><div class="topright">UNITED GALACTIC TRIBUNAL · DEFENCE DIVISION</div></div>
<div class="lobbyTitle"><div class="eyebrow">PERSONNEL REGISTRATION // PAKISTAN</div><h1>YOUR PLANET.<br>YOUR DEFENCE.</h1><p>Earth has been summoned. Your evidence will decide its future. Report for deployment, scientist.</p></div>
<canvas id="pilot"></canvas>
<div class="lobbyCard"><div class="cardHead">01 / IDENTIFICATION & LOADOUT</div><div class="field"><label>SCIENTIST CALLSIGN</label><input id="callsign" maxlength="22" placeholder="e.g. RAZA-01"></div><div class="field"><label>FIELD SPECIALISATION</label><select id="speciality"><option>Planetary Evidence Scientist</option><option>Climate Systems Analyst</option><option>Oceanographer</option><option>Robotics & Survey Engineer</option><option>Biodiversity Researcher</option></select></div><div class="field"><label>EXPEDITION VESSEL</label><input id="shipname" maxlength="24" value="AURELIUS-9"></div><button class="btn wide" id="join">CONFIRM IDENTITY</button><div class="hint">PROFILE SAVED LOCALLY ON THIS DEVICE · NO PASSWORD REQUIRED</div></div></section>
<section id="deploy"><div class="eyebrow">AURELIUS-9 // DEPLOYMENT BAY</div><div class="deployTitle">SELECT DROP ZONE</div><p style="font-size:18px;color:#bdcec7">Choose a field theatre. Your mission begins on the ground.</p><div class="destinations">
<div class="dest selected" data-zone="karachi"><div class="num">01 / PAKISTAN</div><h3>KARACHI</h3><p>Coastal frontier · Port district · Lyari river basin</p></div>
<div class="dest" data-zone="lahore"><div class="num">02 / PAKISTAN</div><h3>LAHORE</h3><p>Urban systems · Ravi corridor · Historic core</p></div>
<div class="dest" data-zone="islamabad"><div class="num">03 / PAKISTAN</div><h3>ISLAMABAD</h3><p>Capital sector · Margalla foothills</p></div>
<div class="dest" data-zone="quetta"><div class="num">04 / PAKISTAN</div><h3>QUETTA</h3><p>Highland ecology · Water security</p></div>
<div class="dest" data-zone="dubai"><div class="num">05 / INTERNATIONAL</div><h3>DUBAI</h3><p>Desert megacity · Heat resilience</p></div>
<div class="dest" data-zone="amazon"><div class="num">06 / INTERNATIONAL</div><h3>AMAZON</h3><p>Rainforest frontier · Biodiversity</p></div></div><div class="deployFoot"><button class="btn" id="deployBtn">DEPLOY TO THEATRE →</button><button class="btn secondary" id="backLobby">BACK TO PERSONNEL</button></div></section>
<section id="hud"><div class="hudTop"><div class="hudBox"><div class="hudSmall">AURELIUS-9 // FIELD LINK</div><div class="hudValue" id="zoneLabel">KARACHI / PAKISTAN</div></div><div class="hudBox"><div class="hudSmall">DEFENCE FILES</div><div class="hudValue" id="evidenceCount">0 / 4</div></div></div><div class="crosshair"></div><div class="interact" id="interactPrompt">[ E ] EXAMINE EVIDENCE</div><div class="bottomHud"><div class="objective"><b>ACTIVE DIRECTIVE // FIELD INVESTIGATION</b><span id="objectiveText">Locate the highlighted evidence site.</span></div><div class="controlsHint">W A S D / ARROWS — MOVE<br>MOUSE — LOOK AROUND<br>SPACE — JUMP · E — INVESTIGATE<br>ESC — PAUSE</div></div></section>
<div id="touch"><div class="touchpad"><button data-key="w">▲</button><button data-key="a">◀</button><button data-key="s">▼</button><button data-key="d">▶</button></div><button class="touchAction" id="touchJump">JUMP</button><button class="touchAction" id="touchUse">USE</button></div>
<div id="toast"></div>
<section id="pause"><div class="modal"><div class="eyebrow">AURELIUS-9 // SYSTEM PAUSED</div><h2>MISSION PAUSED</h2><p>Field operations are on standby. Resume your investigation or return to the deployment bay.</p><div class="modalActions"><button class="btn" id="resume">RESUME FIELDWORK</button><button class="btn secondary" id="returnDeploy">CHANGE DROP ZONE</button><button class="btn secondary" id="toLobby">PERSONNEL LOBBY</button></div></div></section>
<section id="mission"><div class="modal"><div class="eyebrow">FIELD EVIDENCE // RECOVERY COMPLETE</div><h2 id="missionTitle">EVIDENCE RECOVERED</h2><p id="missionText"></p><div class="modalActions"><button class="btn" id="closeMission">CONTINUE INVESTIGATION</button></div></div></section>
</div>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
(()=> {
const $=id=>document.getElementById(id), canvas=$('world'), pilotCanvas=$('pilot');
let scene,camera,renderer,clock,player,velocityY=0,grounded=true,keys={},yaw=0,pitch=0,locked=false,active=false,zone='karachi',selected='karachi',evidence=new Set(),targets=[],nearTarget=null,profile={call:'RAZA-01',speciality:'Planetary Evidence Scientist',ship:'AURELIUS-9'};
const zones={
 karachi:{label:'KARACHI / PAKISTAN',sky:0x7895a7,ground:0x45494a,buildings:0x9b8067,accent:0x187b69,mission:['COASTAL WATER MONITOR','PORT AIR QUALITY ARRAY','LYARI WASTE SURVEY','MANGROVE RESTORATION SITE']},
 lahore:{label:'LAHORE / PAKISTAN',sky:0x9a9a8c,ground:0x696052,buildings:0xb39a78,accent:0x237d68,mission:['RAVI RIVER SAMPLER','URBAN HEAT STATION','OLD CITY AIR SENSOR','GREEN CORRIDOR SURVEY']},
 islamabad:{label:'ISLAMABAD / PAKISTAN',sky:0x8ba9b5,ground:0x626c58,buildings:0xaaa58c,accent:0x2e856b,mission:['MARGALLA BIODIVERSITY','TRAIL WATER SENSOR','SECTOR AIR MONITOR','TREE CANOPY SCAN']},
 quetta:{label:'QUETTA / PAKISTAN',sky:0xb18d70,ground:0x76624f,buildings:0xa68b70,accent:0x9b6846,mission:['KAREZ WATER STATION','HIGHLAND SOIL SCAN','DUST MONITOR','DRYLAND ECOLOGY POST']},
 dubai:{label:'DUBAI / UAE',sky:0x8a9eae,ground:0x9c805a,buildings:0x91a0a4,accent:0x1b8a8b,mission:['DESALINATION OUTLET','URBAN HEAT ARRAY','COASTAL TURBIDITY','SOLAR FIELD SURVEY']},
 amazon:{label:'AMAZON / BRAZIL',sky:0x6c9b88,ground:0x35583d,buildings:0x6c7750,accent:0x45a66e,mission:['CANOPY BIODIVERSITY','RIVER WATER STATION','FOREST LOSS OBSERVER','WILDLIFE CORRIDOR']}
};
function show(id){['boot','lobby','deploy','pause','mission'].forEach(x=>$(x).style.display='none');if(id)$(id).style.display=(id==='pause'||id==='mission')?'flex':'block';}
function toast(t){$('toast').textContent=t;$('toast').style.display='block';clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('toast').style.display='none',2800)}
function initRenderer(){
 scene=new THREE.Scene();scene.background=new THREE.Color(0x050b14);scene.fog=new THREE.Fog(0x8497a0,38,180);
 camera=new THREE.PerspectiveCamera(76,innerWidth/innerHeight,.08,700);camera.rotation.order='YXZ';
 renderer=new THREE.WebGLRenderer({canvas,antialias:true,powerPreference:'high-performance'});renderer.setPixelRatio(Math.min(devicePixelRatio||1,2));renderer.setSize(innerWidth,innerHeight);renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.15;
 clock=new THREE.Clock();scene.add(new THREE.HemisphereLight(0xc6e5f4,0x35302a,2.1));const sun=new THREE.DirectionalLight(0xffe1b0,3.2);sun.position.set(-35,70,25);sun.castShadow=true;sun.shadow.mapSize.set(2048,2048);sun.shadow.camera.left=-90;sun.shadow.camera.right=90;sun.shadow.camera.top=90;sun.shadow.camera.bottom=-90;scene.add(sun);
 createPilot();animate();
}
function makePilot(){
 const g=new THREE.Group(),suit=new THREE.MeshStandardMaterial({color:0x153f3d,metalness:.35,roughness:.55}),gold=new THREE.MeshStandardMaterial({color:0xc9a34d,metalness:.65,roughness:.28}),skin=new THREE.MeshStandardMaterial({color:0x9b684d,roughness:.8}),glass=new THREE.MeshPhysicalMaterial({color:0x172e3c,metalness:.8,roughness:.12,clearcoat:1});
 const torso=new THREE.Mesh(new THREE.CapsuleGeometry(.43,.75,8,16),suit);torso.position.y=1.25;g.add(torso);
 const head=new THREE.Mesh(new THREE.SphereGeometry(.29,24,18),skin);head.position.y=2.12;g.add(head);
 const helmet=new THREE.Mesh(new THREE.SphereGeometry(.36,28,20,0,Math.PI*2,0,Math.PI*.54),gold);helmet.position.y=2.18;g.add(helmet);
 const visor=new THREE.Mesh(new THREE.SphereGeometry(.31,24,18,0,Math.PI*2,.3,1.05),glass);visor.position.set(0,2.16,.11);g.add(visor);
 for(let side of [-1,1]){let arm=new THREE.Mesh(new THREE.CapsuleGeometry(.14,.62,5,10),suit);arm.position.set(side*.55,1.28,0);arm.rotation.z=side*.16;g.add(arm);let leg=new THREE.Mesh(new THREE.CapsuleGeometry(.17,.58,5,10),suit);leg.position.set(side*.22,.43,0);g.add(leg)}
 let chest=new THREE.Mesh(new THREE.BoxGeometry(.46,.23,.08),gold);chest.position.set(0,1.45,.39);g.add(chest);
 // Ajrak-inspired patterned shoulder panels
 for(let side of [-1,1]){let p=new THREE.Mesh(new THREE.BoxGeometry(.28,.35,.08),new THREE.MeshStandardMaterial({color:0x9c2f35,metalness:.2}));p.position.set(side*.48,1.68,0);g.add(p)}
 return g;
}
function createPilotPreview(){
 const r=new THREE.WebGLRenderer({canvas:pilotCanvas,alpha:true,antialias:true});r.setPixelRatio(Math.min(devicePixelRatio,1.7));r.setSize(pilotCanvas.clientWidth||400,pilotCanvas.clientHeight||600,false);const s=new THREE.Scene();s.add(new THREE.HemisphereLight(0xc4e8ff,0x24302d,2.5));let l=new THREE.DirectionalLight(0xffd58a,3);l.position.set(3,7,5);s.add(l);let p=makePilot();s.add(p);p.position.y=-.05;const c=new THREE.PerspectiveCamera(34,(pilotCanvas.clientWidth||400)/(pilotCanvas.clientHeight||600),.1,30);c.position.set(0,1.55,5.8);c.lookAt(0,1.3,0);function tick(){if(!$('lobby')||$('lobby').style.display==='none')return;requestAnimationFrame(tick);p.rotation.y=Math.sin(performance.now()*.0005)*.14;r.render(s,c)}tick();
}
function mat(color,rough=.85,metal=0){return new THREE.MeshStandardMaterial({color,roughness:rough,metalness:metal})}
function box(parent,x,y,z,w,h,d,color,opts={}){let m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),mat(color,opts.rough??.8,opts.metal??0));m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;parent.add(m);return m}
function cityGround(data){
 let ground=new THREE.Mesh(new THREE.PlaneGeometry(420,420),mat(data.ground));ground.rotation.x=-Math.PI/2;ground.position.y=-.12;ground.receiveShadow=true;scene.add(ground);
 // Road grid with pavements, markings and side drains
 for(let i=-4;i<=4;i++){
  let road=new THREE.Mesh(new THREE.PlaneGeometry(13,420),mat(0x252c30,.95));road.rotation.x=-Math.PI/2;road.position.set(i*42,.005,0);scene.add(road);
  let cross=new THREE.Mesh(new THREE.PlaneGeometry(420,12),mat(0x292e31,.95));cross.rotation.x=-Math.PI/2;cross.position.set(0,.01,i*42);scene.add(cross);
  for(let z=-195;z<200;z+=12)box(scene,i*42,.025,z, .22,.035,4,0xbba875);
 }
 // pavements and kerbs
 for(let i=-4;i<=4;i++)for(let j=-4;j<=4;j++){let x=i*42,z=j*42;box(scene,x+8,.14,z+8,22,.25,22,0x77766b);box(scene,x-8,.14,z-8,22,.25,22,0x77766b)}
}
function createBuilding(x,z,w,d,h,color,style=0){
 const b=new THREE.Group();b.position.set(x,0,z);scene.add(b);
 box(b,0,h/2,0,w,h,d,color);
 // roof parapet
 box(b,0,h+.35,0,w+.3,.7,d+.3,0x4b5555);
 // repeated window bays, emissive-ish warm glass
 const winmat=new THREE.MeshStandardMaterial({color:0x294956,roughness:.24,metalness:.4,emissive:0x0a1c25,emissiveIntensity:.4});
 const rows=Math.max(2,Math.floor(h/3.1)),cols=Math.max(2,Math.floor(w/2.8));
 for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){
  for(let side of [-1,1]){
   let wx=-w/2+1.1+c*(w-2.2)/Math.max(1,cols-1),wy=2+r*2.7;
   if(wy<h-.7){let win=new THREE.Mesh(new THREE.BoxGeometry(1.05,1.5,.08),winmat);win.position.set(wx,wy,side*(d/2+.045));b.add(win)}
  }
 }
 if(style===1){ // colourful Pakistani market frontage
  box(b,0,2.2,d/2+.18,w*.92,.32,.25,0x176e5b);box(b,0,1.1,d/2+.2,w*.82,.13,.25,0xd6aa4c);
  for(let n=-2;n<=2;n++){let sign=box(b,n*w*.15,3.2,d/2+.19,.65,.12,.18,n%2?0xc44e42:0xe1b44e);sign.rotation.z=.03*n}
 }
 if(style===2){ // rooftop solar
  for(let n=-1;n<=1;n++){let p=box(b,n*2,h+.78,0,2.6,.12,2,0x193a49,{metal:.7,rough:.25});p.rotation.x=-.12}
 }
 return b;
}
function makeTarget(pos,name,index){
 const g=new THREE.Group();g.position.copy(pos);scene.add(g);
 let ring=new THREE.Mesh(new THREE.TorusGeometry(1.15,.075,10,48),new THREE.MeshStandardMaterial({color:0xe6bd60,emissive:0x9b6723,emissiveIntensity:1.2,metalness:.5}));ring.rotation.x=Math.PI/2;ring.position.y=.15;g.add(ring);
 let beam=new THREE.Mesh(new THREE.CylinderGeometry(.025,.14,5,12,1,true),new THREE.MeshBasicMaterial({color:0x43d8b7,transparent:true,opacity:.28,side:THREE.DoubleSide}));beam.position.y=2.6;g.add(beam);
 let orb=new THREE.Mesh(new THREE.IcosahedronGeometry(.42,2),new THREE.MeshStandardMaterial({color:0xf2cb71,emissive:0x9a6222,emissiveIntensity:1.4,metalness:.55,roughness:.2}));orb.position.y=1.2;g.add(orb);
 let label=document.createElement('div');label.textContent='EVIDENCE '+String(index+1).padStart(2,'0');label.style.cssText='position:absolute;display:none;color:#f2d17a;font:11px monospace;letter-spacing:2px';g.userData={name,index};targets.push(g);
}
function clearWorld(){while(scene.children.length){let o=scene.children.pop();if(o.geometry)o.geometry.dispose()}targets=[]}
function buildZone(key){
 zone=key;const data=zones[key];clearWorld();scene.background=new THREE.Color(data.sky);scene.fog=new THREE.Fog(data.sky,45,210);
 scene.add(new THREE.HemisphereLight(0xe0e9ec,0x4b4030,1.4));let sun=new THREE.DirectionalLight(0xffe0b4,3);sun.position.set(-50,80,40);sun.castShadow=true;sun.shadow.mapSize.set(2048,2048);scene.add(sun);
 cityGround(data);
 // dense, varied skyline with real street scale and a walkable central plaza
 for(let x=-180;x<=180;x+=24)for(let z=-180;z<=180;z+=24){
  if(Math.abs(x%42)<8||Math.abs(z%42)<7)continue;
  let h=12+((Math.abs(Math.sin(x*2.13+z*.72))*35)|0),w=12+Math.abs(Math.sin(z+x))*7,d=12+Math.abs(Math.cos(x-z))*6;
  let palette=[data.buildings,0x777c7a,0xb09a7b,0x596b6a,0x8d7867];let c=palette[Math.abs(Math.floor(x*7+z*3))%palette.length];
  createBuilding(x,z,w,d,h,c,(Math.abs(x+z)%3)|0);
 }
 // Landmark skyline
 if(key==='karachi'){
  createBuilding(-64,-100,18,20,105,0x9a9c91,2); // tall coastal tower
  for(let i=0;i<6;i++)createBuilding(80+i*12,-100,10,12,30+i*5,0x9b8a72,1);
  // waterfront and colourful truck-art gate
  let sea=new THREE.Mesh(new THREE.PlaneGeometry(120,95),new THREE.MeshStandardMaterial({color:0x174f62,metalness:.3,roughness:.25}));sea.rotation.x=-Math.PI/2;sea.position.set(-125,-.05,-130);scene.add(sea);
  box(scene,0,4,-28,16,8,.7,0x1a4c43);for(let i=-6;i<=6;i+=2)box(scene,i,4.1,-27.5,.55,7,.16,i%4?0xd5ad50:0xc34d42);
 }else if(key==='lahore'){createBuilding(0, -95,24,24,48,0x9b8063,1);box(scene,0,6,-95,2,12,2,0xd6b76a)}
 else if(key==='islamabad'){for(let i=0;i<5;i++){let t=box(scene,-80+i*40,18,-120,5,36,5,0xb5b5a0);t.rotation.z=.15} }
 else if(key==='quetta'){for(let i=0;i<16;i++){let m=new THREE.Mesh(new THREE.ConeGeometry(18+Math.random()*14,28+Math.random()*35,5),mat(0x806d5a));m.position.set(-170+Math.random()*340,14,-190+Math.random()*90);scene.add(m)}}
 else if(key==='dubai'){createBuilding(0,-120,22,24,155,0x8caaa9,2);for(let i=0;i<8;i++)createBuilding(-130+i*35,-150,18,20,55+i*12,0x87999c,2)}
 else {for(let i=0;i<45;i++){let tree=new THREE.Group();let trunk=new THREE.Mesh(new THREE.CylinderGeometry(.35,.55,5,7),mat(0x493a2c));trunk.position.y=2.5;tree.add(trunk);let crown=new THREE.Mesh(new THREE.SphereGeometry(3+Math.random()*2,9,7),mat(i%2?0x226d43:0x347e4b));crown.position.y=6;tree.add(crown);tree.position.set(-180+Math.random()*360,0,-180+Math.random()*360);scene.add(tree)}}
 // street furniture, lamps, signal pylons
 for(let x=-170;x<=170;x+=42)for(let z=-170;z<=170;z+=42){if(Math.abs(x%42)>1||Math.abs(z%42)>1)continue;box(scene,x+9,2.5,z+9,.22,5,.22,0x303b3d);let lamp=new THREE.Mesh(new THREE.SphereGeometry(.28,10,8),new THREE.MeshBasicMaterial({color:0xf6d38a}));lamp.position.set(x+9,5.1,z+9);scene.add(lamp)}
 // Evidence sites placed on walkable streets/plaza
 let points=[new THREE.Vector3(-24,0,-18),new THREE.Vector3(26,0,-68),new THREE.Vector3(-72,0,35),new THREE.Vector3(75,0,65)];
 data.mission.forEach((n,i)=>makeTarget(points[i],n,i));
 player.position.set(0,1.7,35);yaw=0;pitch=0;camera.position.copy(player.position);camera.rotation.set(0,0,0);
 $('zoneLabel').textContent=data.label;$('evidenceCount').textContent=evidence.size+' / 4';$('objectiveText').textContent='Locate a gold evidence beacon and press E to investigate.';
}
function createWorldPlayer(){player=new THREE.Object3D();scene.add(player)}
function animate(){
 requestAnimationFrame(animate);if(!renderer||!scene)return;let dt=Math.min(clock.getDelta(),.05);
 if(active&&player){
  let forward=(keys.w||keys.arrowup?1:0)-(keys.s||keys.arrowdown?1:0),strafe=(keys.d||keys.arrowright?1:0)-(keys.a||keys.arrowleft?1:0);
  let speed=keys.shift?13:7.4;let dx=(Math.sin(yaw)*forward+Math.cos(yaw)*strafe)*speed*dt;let dz=(-Math.cos(yaw)*forward+Math.sin(yaw)*strafe)*speed*dt;
  player.position.x+=dx;player.position.z+=dz;player.position.x=Math.max(-195,Math.min(195,player.position.x));player.position.z=Math.max(-195,Math.min(195,player.position.z));
  if(!grounded){velocityY-=22*dt;player.position.y+=velocityY*dt;if(player.position.y<=1.7){player.position.y=1.7;velocityY=0;grounded=true}}
  camera.position.copy(player.position);camera.rotation.set(pitch,yaw,0,'YXZ');
  let nearest=null,dist=999;for(let t of targets){let d=player.position.distanceTo(new THREE.Vector3(t.position.x,1.7,t.position.z));if(d<dist){dist=d;nearest=t}}
  nearTarget=dist<7?nearest:null;$('interactPrompt').style.display=nearTarget?'block':'none';
 }
 // animate floating evidence
 for(let t of targets){t.children[1].rotation.y+=dt*.6;t.children[2].rotation.y+=dt*.8;t.children[2].position.y=1.2+Math.sin(performance.now()*.0018+t.userData.index)*.25}
 renderer.render(scene,camera);
}
function enterGame(){show(null);$('hud').style.display='block';active=true;buildZone(selected);if(innerWidth>800)canvas.requestPointerLock?.();toast('FIELD LINK ESTABLISHED // '+zones[zone].label)}
function interact(){if(!active)return;if(nearTarget){let idx=nearTarget.userData.index,name=zones[zone].mission[idx];if(evidence.has(zone+idx)){toast('THIS EVIDENCE FILE IS ALREADY SECURED.');return}evidence.add(zone+idx);$('evidenceCount').textContent=evidence.size+' / 4';$('missionTitle').textContent='EVIDENCE SECURED';$('missionText').textContent=name+' has been added to your defence dossier. Cross-check the observation and continue to the next field site.';$('mission').style.display='flex';document.exitPointerLock?.();}else toast('NO EVIDENCE SITE IN RANGE // FOLLOW THE GOLD BEACONS')}
function deploy(){selected=document.querySelector('.dest.selected')?.dataset.zone||'karachi';$('deploy').style.display='none';enterGame()}
function keydown(e){let k=e.key.toLowerCase();keys[k]=true;if([' ','arrowup','arrowdown','arrowleft','arrowright'].includes(k))e.preventDefault();if(k===' '&&active&&grounded){velocityY=8.2;grounded=false}if(k==='e')interact();if(k==='escape'&&active){active=false;document.exitPointerLock?.();$('pause').style.display='flex'}}
function keyup(e){keys[e.key.toLowerCase()]=false}
function mouse(e){if(!locked||!active)return;yaw-=e.movementX*.0022;pitch-=e.movementY*.0022;pitch=Math.max(-1.35,Math.min(1.35,pitch))}
document.addEventListener('keydown',keydown);document.addEventListener('keyup',keyup);document.addEventListener('mousemove',mouse);document.addEventListener('pointerlockchange',()=>{locked=document.pointerLockElement===canvas});
canvas.addEventListener('click',()=>{if(active&&!locked&&innerWidth>800)canvas.requestPointerLock?.()});
$('join').onclick=()=>{profile.call=$('callsign').value.trim()||'RAZA-01';profile.speciality=$('speciality').value;profile.ship=$('shipname').value.trim()||'AURELIUS-9';try{localStorage.setItem('eot-profile',JSON.stringify(profile))}catch(e){}$('lobby').style.display='none';$('deploy').style.display='block'};
$('backLobby').onclick=()=>{$('deploy').style.display='none';$('lobby').style.display='block';createPilotPreview()};
document.querySelectorAll('.dest').forEach(el=>el.onclick=()=>{document.querySelectorAll('.dest').forEach(x=>x.classList.remove('selected'));el.classList.add('selected');selected=el.dataset.zone});
$('deployBtn').onclick=deploy;$('resume').onclick=()=>{$('pause').style.display='none';active=true;if(innerWidth>800)canvas.requestPointerLock?.()};
$('returnDeploy').onclick=()=>{active=false;$('pause').style.display='none';$('hud').style.display='none';$('deploy').style.display='block';document.exitPointerLock?.()};
$('toLobby').onclick=()=>{active=false;$('pause').style.display='none';$('hud').style.display='none';$('lobby').style.display='block';document.exitPointerLock?.();createPilotPreview()};
$('closeMission').onclick=()=>{$('mission').style.display='none';active=true;if(innerWidth>800)canvas.requestPointerLock?.();$('objectiveText').textContent='Evidence secured. Find the next gold beacon.'};
document.querySelectorAll('[data-key]').forEach(b=>{let k=b.dataset.key;b.onpointerdown=e=>{e.preventDefault();keys[k]=true};['pointerup','pointerleave','pointercancel'].forEach(ev=>b.addEventListener(ev,()=>keys[k]=false))});
$('touchJump').onclick=()=>{if(active&&grounded){velocityY=8.2;grounded=false}};$('touchUse').onclick=interact;
window.addEventListener('resize',()=>{if(camera&&renderer){camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)}});
function boot(){
 let n=0;const t=setInterval(()=>{n=Math.min(100,n+4+Math.random()*9);$('loadfill').style.width=n+'%';$('loadtext').textContent='INITIALISING AURELIUS-9 SYSTEMS · '+Math.floor(n)+'%';if(n>=100){clearInterval(t);$('boot').style.display='none';$('lobby').style.display='block';createPilotPreview();try{let p=JSON.parse(localStorage.getItem('eot-profile')||'null');if(p){$('callsign').value=p.call||'';$('speciality').value=p.speciality||'Planetary Evidence Scientist';$('shipname').value=p.ship||'AURELIUS-9'}}catch(e){}}},100)}
initRenderer();createWorldPlayer();boot();
})();
</script></body></html>"""
components.html(game, height=1000, scrolling=False)
