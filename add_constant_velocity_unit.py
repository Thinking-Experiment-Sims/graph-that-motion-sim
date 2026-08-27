with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update Header Navigation Tabs to include Constant Velocity Unit & Acceleration Unit
old_nav = '''            <nav class="nav-tabs">
                <button class="tab-btn active" data-tab="lab-tab">🎮 Challenge Lab</button>
                <button class="tab-btn" data-tab="sketch-tab">✏️ Prediction Sketch</button>
                <button class="tab-btn" data-tab="builder-tab">🛠️ Scenario Sandbox</button>
            </nav>'''

new_nav = '''            <nav class="nav-tabs">
                <button class="tab-btn active" id="btnModeCV" data-mode="cv">🟢 Constant Velocity (CVPM)</button>
                <button class="tab-btn" id="btnModeAccel" data-mode="accel">🚀 Full Kinematics (CAPM)</button>
                <button class="tab-btn" data-tab="sketch-tab">✏️ Prediction Sketch</button>
                <button class="tab-btn" data-tab="builder-tab">🛠️ Sandbox</button>
            </nav>'''

html = html.replace(old_nav, new_nav)

# 2. Update JavaScript Data Structures with dedicated Constant Velocity Scenarios + Acceleration Scenarios
old_scenarios_block = '''        const scenarios = {
            '#1': {
                id: '#1',
                title: 'The Backyard Dash',
                type: 'position',
                startX: 10.0,
                startV: 0.0,
                stages: [{ d: 3.2, a: 1.8 }],
                desc: 'Coco starts from rest in the center and speeds up enthusiastically to the right.'
            },
            '#2': {
                id: '#2',
                title: 'The Sudden Treat Pause',
                type: 'velocity',
                startX: 19.0,
                startV: -7.5,
                stages: [{ d: 3.0, a: 2.5 }],
                desc: 'Coco sprints left fast, steadily decelerating with positive acceleration to a complete stop.'
            },
            '#3': {
                id: '#3',
                title: 'The Boundary Patrol',
                type: 'position',
                startX: 3.0,
                startV: 3.0,
                stages: [
                    { d: 2.0, a: 0.0 },
                    { d: 1.8, a: 0.0, vForce: 6.0 }
                ],
                desc: 'Coco trots right at steady speed, then kicks into high gear cruising twice as fast right.'
            },
            '#4': {
                id: '#4',
                title: 'The Squirrel Hesitation',
                type: 'velocity',
                startX: 2.0,
                startV: 5.0,
                stages: [
                    { d: 2.0, a: -2.5 },
                    { d: 1.0, a: 0.0, vForce: 0.0 },
                    { d: 1.8, a: -3.0, vForce: 0.0 }
                ],
                desc: 'Coco runs right slowing to rest, pauses to listen, then accelerates left.'
            },
            '#5': {
                id: '#5',
                title: 'The Steady Sniff Tour',
                type: 'position',
                startX: 18.0,
                startV: -4.0,
                stages: [
                    { d: 1.8, a: 0.0 },
                    { d: 1.5, a: 0.0, vForce: 0.0 },
                    { d: 1.8, a: 0.0, vForce: -4.0 }
                ],
                desc: 'Coco trots left at constant speed, stops completely to sniff the ground, then resumes trotting left.'
            },
            '#6': {
                id: '#6',
                title: 'The Rebound Arc',
                type: 'position',
                startX: 4.0,
                startV: 6.0,
                stages: [{ d: 4.0, a: -2.4 }],
                desc: 'Coco runs right while smoothly slowing down, turns around smoothly at the peak, and accelerates back left.'
            },
            '#7': {
                id: '#7',
                title: 'Launch & Glide',
                type: 'velocity',
                startX: 1.0,
                startV: 0.0,
                stages: [
                    { d: 1.5, a: 4.0 },
                    { d: 2.2, a: 0.0 }
                ],
                desc: 'Coco accelerates aggressively from rest to the right, then glides at a steady constant speed.'
            },
            '#8': {
                id: '#8',
                title: 'Leftward Zoomies',
                type: 'velocity',
                startX: 16.0,
                startV: 0.0,
                stages: [{ d: 3.5, a: -2.2 }],
                desc: 'Coco launches from rest on the right, speeding up with constant negative acceleration to the left.'
            },
            '#9': {
                id: '#9',
                title: 'The Zig-Zag Search',
                type: 'position',
                startX: 8.0,
                startV: 4.0,
                stages: [
                    { d: 1.5, a: 0.0 },
                    { d: 2.0, a: 0.0, vForce: -5.0 },
                    { d: 2.0, a: 0.0, vForce: 3.0 }
                ],
                desc: 'Coco jogs right at constant speed, turns abruptly to trot left fast, then turns to jog right.'
            },
            '#10': {
                id: '#10',
                title: 'The Bell-Curve Trot',
                type: 'velocity',
                startX: 2.0,
                startV: 0.0,
                stages: [
                    { d: 1.5, a: 3.0 },
                    { d: 1.2, a: 0.0 },
                    { d: 1.5, a: -3.0 }
                ],
                desc: 'Coco speeds up from rest, cruises steadily, then decelerates smoothly back to a complete stop.'
            }
        };'''

new_scenarios_block = '''        // ==========================================
        // 1. CONSTANT VELOCITY UNIT (CVPM - a = 0)
        // ==========================================
        const cvScenarios = {
            'CV-1': {
                id: 'CV-1',
                title: 'Steady Rightward Trot',
                type: 'position',
                startX: 2.0,
                startV: 3.5,
                stages: [{ d: 4.0, a: 0.0 }],
                desc: 'Coco trots to the right at a steady constant velocity (+3.5 m/s).'
            },
            'CV-2': {
                id: 'CV-2',
                title: 'Steady Leftward Trot',
                type: 'velocity',
                startX: 18.0,
                startV: -3.5,
                stages: [{ d: 4.0, a: 0.0 }],
                desc: 'Coco trots to the left at a steady constant velocity (-3.5 m/s).'
            },
            'CV-3': {
                id: 'CV-3',
                title: 'The Patient Sniff (At Rest)',
                type: 'position',
                startX: 12.0,
                startV: 0.0,
                stages: [{ d: 4.0, a: 0.0 }],
                desc: 'Coco remains completely at rest sniffing a treat at x = 12.0 m (v = 0).'
            },
            'CV-4': {
                id: 'CV-4',
                title: 'Fast Zoomie vs Slow Walk',
                type: 'velocity',
                startX: 1.0,
                startV: 7.0,
                stages: [{ d: 2.5, a: 0.0 }],
                desc: 'Coco sprints right at high constant velocity (+7.0 m/s).'
            },
            'CV-5': {
                id: 'CV-5',
                title: 'Trot, Sniff Pause, Trot',
                type: 'position',
                startX: 2.0,
                startV: 4.0,
                stages: [
                    { d: 1.8, a: 0.0 },
                    { d: 1.5, a: 0.0, vForce: 0.0 },
                    { d: 1.8, a: 0.0, vForce: 4.0 }
                ],
                desc: 'Coco trots right, stops to sniff (v = 0), then resumes trotting right at the same speed.'
            },
            'CV-6': {
                id: 'CV-6',
                title: 'Fetch & Return',
                type: 'position',
                startX: 2.0,
                startV: 4.5,
                stages: [
                    { d: 2.0, a: 0.0 },
                    { d: 1.0, a: 0.0, vForce: 0.0 },
                    { d: 2.0, a: 0.0, vForce: -4.5 }
                ],
                desc: 'Coco jogs right to get a ball, pauses to grab it, then trots back left at constant speed.'
            },
            'CV-7': {
                id: 'CV-7',
                title: 'Left Trot with Pause',
                type: 'velocity',
                startX: 18.0,
                startV: -3.5,
                stages: [
                    { d: 1.8, a: 0.0 },
                    { d: 1.4, a: 0.0, vForce: 0.0 },
                    { d: 1.8, a: 0.0, vForce: -3.5 }
                ],
                desc: 'Coco walks left, pauses at rest (v = 0), then resumes walking left at uniform speed.'
            },
            'CV-8': {
                id: 'CV-8',
                title: 'Speed Shift (Shallow to Steep)',
                type: 'position',
                startX: 1.0,
                startV: 2.5,
                stages: [
                    { d: 2.2, a: 0.0 },
                    { d: 2.0, a: 0.0, vForce: 6.0 }
                ],
                desc: 'Coco walks right at slow constant speed, then shifts to a fast constant speed.'
            }
        };

        // ==========================================
        // 2. FULL KINEMATICS / ACCELERATION UNIT (CAPM)
        // ==========================================
        const accelScenarios = {
            '#1': {
                id: '#1',
                title: 'The Backyard Dash',
                type: 'position',
                startX: 10.0,
                startV: 0.0,
                stages: [{ d: 3.2, a: 1.8 }],
                desc: 'Coco starts from rest in the center and speeds up enthusiastically to the right.'
            },
            '#2': {
                id: '#2',
                title: 'The Sudden Treat Pause',
                type: 'velocity',
                startX: 19.0,
                startV: -7.5,
                stages: [{ d: 3.0, a: 2.5 }],
                desc: 'Coco sprints left fast, steadily decelerating with positive acceleration to a complete stop.'
            },
            '#3': {
                id: '#3',
                title: 'The Boundary Patrol',
                type: 'position',
                startX: 3.0,
                startV: 3.0,
                stages: [
                    { d: 2.0, a: 0.0 },
                    { d: 1.8, a: 0.0, vForce: 6.0 }
                ],
                desc: 'Coco trots right at steady speed, then kicks into high gear cruising twice as fast right.'
            },
            '#4': {
                id: '#4',
                title: 'The Squirrel Hesitation',
                type: 'velocity',
                startX: 2.0,
                startV: 5.0,
                stages: [
                    { d: 2.0, a: -2.5 },
                    { d: 1.0, a: 0.0, vForce: 0.0 },
                    { d: 1.8, a: -3.0, vForce: 0.0 }
                ],
                desc: 'Coco runs right slowing to rest, pauses to listen, then accelerates left.'
            },
            '#5': {
                id: '#5',
                title: 'The Steady Sniff Tour',
                type: 'position',
                startX: 18.0,
                startV: -4.0,
                stages: [
                    { d: 1.8, a: 0.0 },
                    { d: 1.5, a: 0.0, vForce: 0.0 },
                    { d: 1.8, a: 0.0, vForce: -4.0 }
                ],
                desc: 'Coco trots left at constant speed, stops completely to sniff the ground, then resumes trotting left.'
            },
            '#6': {
                id: '#6',
                title: 'The Rebound Arc',
                type: 'position',
                startX: 4.0,
                startV: 6.0,
                stages: [{ d: 4.0, a: -2.4 }],
                desc: 'Coco runs right while smoothly slowing down, turns around smoothly at the peak, and accelerates back left.'
            },
            '#7': {
                id: '#7',
                title: 'Launch & Glide',
                type: 'velocity',
                startX: 1.0,
                startV: 0.0,
                stages: [
                    { d: 1.5, a: 4.0 },
                    { d: 2.2, a: 0.0 }
                ],
                desc: 'Coco accelerates aggressively from rest to the right, then glides at a steady constant speed.'
            },
            '#8': {
                id: '#8',
                title: 'Leftward Zoomies',
                type: 'velocity',
                startX: 16.0,
                startV: 0.0,
                stages: [{ d: 3.5, a: -2.2 }],
                desc: 'Coco launches from rest on the right, speeding up with constant negative acceleration to the left.'
            },
            '#9': {
                id: '#9',
                title: 'The Zig-Zag Search',
                type: 'position',
                startX: 8.0,
                startV: 4.0,
                stages: [
                    { d: 1.5, a: 0.0 },
                    { d: 2.0, a: 0.0, vForce: -5.0 },
                    { d: 2.0, a: 0.0, vForce: 3.0 }
                ],
                desc: 'Coco jogs right at constant speed, turns abruptly to trot left fast, then turns to jog right.'
            },
            '#10': {
                id: '#10',
                title: 'The Bell-Curve Trot',
                type: 'velocity',
                startX: 2.0,
                startV: 0.0,
                stages: [
                    { d: 1.5, a: 3.0 },
                    { d: 1.2, a: 0.0 },
                    { d: 1.5, a: -3.0 }
                ],
                desc: 'Coco speeds up from rest, cruises steadily, then decelerates smoothly back to a complete stop.'
            }
        };'''

html = html.replace(old_scenarios_block, new_scenarios_block)

# 3. Update computeKinematicStages to handle both sets
old_compute = '''        Object.values(scenarios).forEach(computeKinematicStages);

        // State
        const missionKeys = ['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10'];
        let missionOrder = missionKeys.slice().sort(() => 0.5 - Math.random());
        let currentMissionIdx = 0;
        let solvedMissions = new Set();
        let currentSelectedCard = null;
        let isSlowMoSpeed = 1.0;
        let showDual = false;'''

new_compute = '''        Object.values(cvScenarios).forEach(computeKinematicStages);
        Object.values(accelScenarios).forEach(computeKinematicStages);

        // Active Unit Mode ('cv' or 'accel')
        let currentUnitMode = 'cv';
        let activeScenarios = cvScenarios;
        let missionKeys = Object.keys(cvScenarios);
        let missionOrder = missionKeys.slice().sort(() => 0.5 - Math.random());
        let currentMissionIdx = 0;
        let solvedMissions = new Set();
        let currentSelectedCard = null;
        let isSlowMoSpeed = 1.0;
        let showDual = false;'''

html = html.replace(old_compute, new_compute)

# 4. Update setupTabs to support mode switching
old_setup_tabs = '''        function setupTabs() {
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
                    btn.classList.add('active');
                    document.getElementById(btn.dataset.tab).classList.add('active');
                });
            });
        }'''

new_setup_tabs = '''        function setupTabs() {
            document.getElementById('btnModeCV').addEventListener('click', () => setUnitMode('cv'));
            document.getElementById('btnModeAccel').addEventListener('click', () => setUnitMode('accel'));

            document.querySelectorAll('.tab-btn[data-tab]').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
                    btn.classList.add('active');
                    document.getElementById(btn.dataset.tab).classList.add('active');
                });
            });
        }

        function setUnitMode(mode) {
            currentUnitMode = mode;
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            
            document.getElementById('lab-tab').classList.add('active');
            if (mode === 'cv') {
                document.getElementById('btnModeCV').classList.add('active');
                activeScenarios = cvScenarios;
            } else {
                document.getElementById('btnModeAccel').classList.add('active');
                activeScenarios = accelScenarios;
            }

            missionKeys = Object.keys(activeScenarios);
            missionOrder = missionKeys.slice().sort(() => 0.5 - Math.random());
            solvedMissions.clear();
            
            buildCardsGallery();
            buildStepper();
            loadMission(0, false);
        }'''

html = html.replace(old_setup_tabs, new_setup_tabs)

# 5. Replace references to 'scenarios' with 'activeScenarios' in getDiagnosticAnalysis, checkStudentAnswer, etc.
html = html.replace('const chosen = scenarios[chosenKey];', 'const chosen = activeScenarios[chosenKey];')
html = html.replace('const target = scenarios[targetKey];', 'const target = activeScenarios[targetKey];')
html = html.replace('const target = scenarios[targetKey];', 'const target = activeScenarios[targetKey];')
html = html.replace('drawGraphPreview(scenarios[currentSelectedCard]);', 'drawGraphPreview(activeScenarios[currentSelectedCard]);')
html = html.replace('drawGraphPreview(scenarios[k]);', 'drawGraphPreview(activeScenarios[k]);')
html = html.replace('inspectBadge.textContent = `${k} (${scenarios[k].type === \'position\' ? \'Position-Time\' : \'Velocity-Time\'})`;', 'inspectBadge.textContent = `${k} (${activeScenarios[k].type === \'position\' ? \'Position-Time\' : \'Velocity-Time\'})`;')
html = html.replace('for (let i = 0; i < 10; i++) {', 'for (let i = 0; i < missionKeys.length; i++) {')
html = html.replace('scoreBadge.textContent = `Solved: ${solvedMissions.size} / 10`;', 'scoreBadge.textContent = `Solved: ${solvedMissions.size} / ${missionKeys.length}`;')
html = html.replace('let key = missionOrder[currentMissionIdx];\n            return scenarios[key];', 'let key = missionOrder[currentMissionIdx];\n            return activeScenarios[key];')
html = html.replace('if (solvedMissions.size < 10) {', 'if (solvedMissions.size < missionKeys.length) {')
html = html.replace('btnNextStep.textContent = \'🏆 All 10 Missions Mastered!\';', 'btnNextStep.textContent = `🏆 All ${missionKeys.length} Missions Mastered!`;')
html = html.replace('let next = (currentMissionIdx + 1) % 10;', 'let next = (currentMissionIdx + 1) % missionKeys.length;')

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added dedicated Constant Velocity Unit and Unit Mode Switcher successfully!")
