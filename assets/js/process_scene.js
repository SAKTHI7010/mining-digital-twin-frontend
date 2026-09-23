// process_scene.js
// using globally loaded THREE and OrbitControls
let scene, camera, renderer, controls;
let equipmentMeshes = {};
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

function init() {
    const container = document.getElementById('canvas-container');
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f2f6);
    
    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 30, 50);
    
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    container.appendChild(renderer.domElement);
    
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(10, 20, 10);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0x404040));
    
    createEquipment();
    
    window.addEventListener('resize', onWindowResize, false);
    window.addEventListener('mousemove', onMouseMove, false);
    
    animate();
}

function createEquipment() {
    // SAG Mill
    const sagGeo = new THREE.CylinderGeometry(5, 5, 8, 32);
    sagGeo.rotateZ(Math.PI / 2);
    const sagMat = new THREE.MeshPhongMaterial({ color: 0x2ECC71 });
    const sagMesh = new THREE.Mesh(sagGeo, sagMat);
    sagMesh.position.set(-20, 5, 0);
    sagMesh.userData = { id: 'SAG_01', name: 'SAG Mill' };
    scene.add(sagMesh);
    equipmentMeshes['SAG_01'] = sagMesh;
    
    // Ball Mill
    const bmGeo = new THREE.CylinderGeometry(4, 4, 10, 32);
    bmGeo.rotateZ(Math.PI / 2);
    const bmMat = new THREE.MeshPhongMaterial({ color: 0xF39C12 });
    const bmMesh = new THREE.Mesh(bmGeo, bmMat);
    bmMesh.position.set(-5, 4, 0);
    bmMesh.userData = { id: 'BM_01', name: 'Ball Mill' };
    scene.add(bmMesh);
    equipmentMeshes['BM_01'] = bmMesh;
    
    // Flotation
    const flGeo = new THREE.BoxGeometry(6, 4, 6);
    const flMat = new THREE.MeshPhongMaterial({ color: 0x2ECC71 });
    const flMesh = new THREE.Mesh(flGeo, flMat);
    flMesh.position.set(10, 2, 0);
    flMesh.userData = { id: 'FL_RO_01', name: 'Flotation Rougher' };
    scene.add(flMesh);
    equipmentMeshes['FL_RO_01'] = flMesh;
    
    // Thickener
    const thkGeo = new THREE.CylinderGeometry(8, 8, 2, 32);
    const thkMat = new THREE.MeshPhongMaterial({ color: 0xE74C3C });
    const thkMesh = new THREE.Mesh(thkGeo, thkMat);
    thkMesh.position.set(25, 1, 0);
    thkMesh.userData = { id: 'THK_01', name: 'Thickener' };
    scene.add(thkMesh);
    equipmentMeshes['THK_01'] = thkMesh;
    
    // Pipes
    const pipeGeo = new THREE.CylinderGeometry(0.5, 0.5, 10);
    pipeGeo.rotateZ(Math.PI / 2);
    const pipeMat = new THREE.MeshBasicMaterial({ color: 0x888888 });
    const p1 = new THREE.Mesh(pipeGeo, pipeMat);
    p1.position.set(-13, 4.5, 0);
    scene.add(p1);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function onMouseMove(event) {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

function updateColorsFromData() {
    if (window.plantData && window.plantData.units) {
        window.plantData.units.forEach(unit => {
            const mesh = equipmentMeshes[unit.unit_id];
            if (mesh) {
                if (unit.status === 'normal') mesh.material.color.setHex(0x2ECC71);
                else if (unit.status === 'caution') mesh.material.color.setHex(0xF39C12);
                else if (unit.status === 'alarm') mesh.material.color.setHex(0xE74C3C);
            }
        });
    }
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    
    // Rotate mills slowly
    if (equipmentMeshes['SAG_01']) equipmentMeshes['SAG_01'].rotation.x += 0.01;
    if (equipmentMeshes['BM_01']) equipmentMeshes['BM_01'].rotation.x += 0.02;
    
    updateColorsFromData();
    
    // Raycaster for hover
    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(Object.values(equipmentMeshes));
    const tooltip = document.getElementById('tooltip');
    
    if (intersects.length > 0) {
        const obj = intersects[0].object;
        tooltip.style.display = 'block';
        tooltip.style.left = mouse.x * window.innerWidth / 2 + window.innerWidth / 2 + 10 + 'px';
        tooltip.style.top = -mouse.y * window.innerHeight / 2 + window.innerHeight / 2 + 10 + 'px';
        tooltip.innerHTML = `<strong>${obj.userData.name}</strong><br>ID: ${obj.userData.id}`;
    } else {
        tooltip.style.display = 'none';
    }
    
    renderer.render(scene, camera);
}

init();
