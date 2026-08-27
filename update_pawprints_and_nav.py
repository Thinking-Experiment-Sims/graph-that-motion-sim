with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update Paw Print vector drawing function
paw_print_func = '''        // Vector drawing of an Amber Paw Print for Motion Map
        function drawPawPrint(ctx, x, y, heading, isRest = false, restStack = 0) {
            ctx.save();
            ctx.translate(x, y);
            if (!isRest && heading < 0) {
                ctx.scale(-1, 1);
            }
            
            const scale = 0.9;
            ctx.fillStyle = '#d67b19';
            ctx.strokeStyle = '#b06210';
            ctx.lineWidth = 1;

            // Main Palm Pad
            ctx.beginPath();
            ctx.ellipse(0, 1.5 * scale, 4.2 * scale, 3.2 * scale, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();

            // 4 Toe Beans
            const toes = [
                { dx: -4.2 * scale, dy: -2.8 * scale, rx: 1.5 * scale, ry: 2.2 * scale, rot: -0.35 },
                { dx: -1.5 * scale, dy: -4.8 * scale, rx: 1.6 * scale, ry: 2.4 * scale, rot: -0.1 },
                { dx: 1.5 * scale, dy: -4.8 * scale, rx: 1.6 * scale, ry: 2.4 * scale, rot: 0.1 },
                { dx: 4.2 * scale, dy: -2.8 * scale, rx: 1.5 * scale, ry: 2.2 * scale, rot: 0.35 }
            ];

            toes.forEach(t => {
                ctx.beginPath();
                ctx.ellipse(t.dx, t.dy, t.rx, t.ry, t.rot, 0, Math.PI * 2);
                ctx.fill();
                ctx.stroke();
            });

            ctx.restore();
        }'''

# Insert paw_print_func before renderStage
html = html.replace('function renderStage() {', paw_print_func + '\n\n        function renderStage() {', 1)

# 2. Replace circle dots in renderStage with drawPawPrint
old_dot_render = '''            // Motion Map Dots (Amber Pawprint Dots)
            if (showMotionDots) {
                const dotY = trackY - 2;
                sctx.fillStyle = "var(--accent-amber)";
                motionDots.forEach(dot => {
                    let dpx = margin + dot.x * pxPerMeter;
                    let dpy = dotY - (dot.restStack * 6) + (dot.restStack % 2 === 0 ? 3 : -3);
                    if (dot.restStack === 0) dpy = dotY;

                    sctx.beginPath();
                    sctx.arc(dpx, dpy, 5, 0, Math.PI * 2);
                    sctx.fill();
                    sctx.strokeStyle = "var(--accent-amber-dark)";
                    sctx.lineWidth = 1;
                    sctx.stroke();

                    if (showVelocity && Math.abs(dot.v) > 0.3) {
                        drawVectorArrow(sctx, dpx, dpy - 10, dpx + dot.v * 3, dpy - 10, "var(--accent-amber)", 1.5);
                    }
                });
            }'''

new_dot_render = '''            // Motion Map Paw Prints (Amber Paw Prints)
            if (showMotionDots) {
                const pawY = trackY - 2;
                motionDots.forEach(dot => {
                    let dpx = margin + dot.x * pxPerMeter;
                    let dpy = pawY - (dot.restStack * 7);
                    if (dot.restStack === 0) dpy = pawY;

                    drawPawPrint(sctx, dpx, dpy, dot.v < 0 ? -1 : 1, dot.restStack > 0, dot.restStack);

                    if (showVelocity && Math.abs(dot.v) > 0.3) {
                        drawVectorArrow(sctx, dpx, dpy - 10, dpx + dot.v * 3, dpy - 10, "#d67b19", 1.5);
                    }
                });
            }'''

html = html.replace(old_dot_render, new_dot_render)

# 3. Add Next Motion button in HTML check-answer-area
old_check_area = '''                <!-- Check Answer -->
                <div class="check-answer-area">
                    <button class="btn-check" id="btnCheck" disabled>Check Answer</button>
                    <div class="diagnostic-card" id="diagnosticCard">
                        <div class="coco-avatar-badge" id="cocoAvatarBadge">🐶</div>
                        <div class="coco-dialogue-content">
                            <div class="coco-witty-quote" id="diagCocoQuote"></div>
                            <div class="diagnostic-body" id="diagBody"></div>
                        </div>
                    </div>
                </div>'''

new_check_area = '''                <!-- Check Answer & Manual Navigation -->
                <div class="check-answer-area">
                    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                        <button class="btn-check" id="btnCheck" disabled style="flex: 1;">Check Answer</button>
                        <button class="btn-ctrl" id="btnNextMotion" style="display: none; background-color: var(--primary-teal); font-size: 1.05rem; padding: 0.75rem 1.5rem; justify-content: center; flex: 1;">
                            Next Motion ➔
                        </button>
                    </div>
                    <div class="diagnostic-card" id="diagnosticCard">
                        <div class="coco-avatar-badge" id="cocoAvatarBadge">🐶</div>
                        <div class="coco-dialogue-content">
                            <div class="coco-witty-quote" id="diagCocoQuote"></div>
                            <div class="diagnostic-body" id="diagBody"></div>
                        </div>
                    </div>
                </div>'''

html = html.replace(old_check_area, new_check_area)

# 4. Update loadLevel and btnCheck logic to support manual progression
old_load_level = '''        function loadLevel(levelIndex, autoPlay = true) {
            currentLevel = levelIndex;
            updateLevelsUI();
            
            currentSelectedLetter = null;
            selectedLetterBadge.textContent = '--';
            graphCanvas.style.display = 'none';
            dualToggles.style.display = 'none';
            emptyPrompt.style.display = 'block';
            document.querySelectorAll('.letter-btn').forEach(b => b.classList.remove('active'));
            btnCheck.disabled = true;
            diagnosticCard.style.display = 'none';

            resetToStart(autoPlay);
        }'''

new_load_level = '''        function loadLevel(levelIndex, autoPlay = true) {
            currentLevel = levelIndex;
            updateLevelsUI();
            
            currentSelectedLetter = null;
            selectedLetterBadge.textContent = '--';
            graphCanvas.style.display = 'none';
            dualToggles.style.display = 'none';
            emptyPrompt.style.display = 'block';
            document.querySelectorAll('.letter-btn').forEach(b => b.classList.remove('active'));
            
            btnCheck.style.display = 'inline-flex';
            btnCheck.disabled = true;
            btnNextMotion.style.display = 'none';
            diagnosticCard.style.display = 'none';

            resetToStart(autoPlay);
        }'''

html = html.replace(old_load_level, new_load_level)

# 5. Update DOM bindings to include btnNextMotion
old_dom_btn = '''        const btnCheck = document.getElementById('btnCheck');
        const diagnosticCard = document.getElementById('diagnosticCard');'''

new_dom_btn = '''        const btnCheck = document.getElementById('btnCheck');
        const btnNextMotion = document.getElementById('btnNextMotion');
        const diagnosticCard = document.getElementById('diagnosticCard');'''

html = html.replace(old_dom_btn, new_dom_btn)

# 6. Update btnCheck event handler & getDiagnosticFeedback with self-contained hints & NO auto-advance
old_btn_check = '''        btnCheck.addEventListener('click', () => {
            if (!currentSelectedLetter) return;

            const targetLetter = levelAssignments[currentLevel];

            if (currentSelectedLetter === targetLetter) {
                solvedLevels.add(currentLevel);
                diagnosticCard.className = 'diagnostic-card success';
                
                const randomPraise = cocoSuccessPraise[Math.floor(Math.random() * cocoSuccessPraise.length)];
                if (cocoAvatarBadge) cocoAvatarBadge.textContent = '🎉';
                if (diagCocoQuote) diagCocoQuote.innerHTML = randomPraise;
                if (diagBody) diagBody.innerHTML = `<strong>Spot on!</strong> Motion #${currentLevel + 1} precisely corresponds to Graph ${currentSelectedLetter}: <em>${graphs[targetLetter].desc}</em>`;
                
                // Show speech bubble over Coco on the track
                showCocoBubble("🦴 Pawsome! You got it!", 'success', 3500);

                updateLevelsUI();

                setTimeout(() => {
                    if (solvedLevels.size < 11) {
                        let next = (currentLevel + 1) % 11;
                        while (solvedLevels.has(next)) next = (next + 1) % 11;
                        loadLevel(next, false);
                    } else {
                        if (cocoAvatarBadge) cocoAvatarBadge.textContent = '🏆';
                        if (diagCocoQuote) diagCocoQuote.innerHTML = '🐾 Paws and applause! You mastered all 11 motion graphs!';
                        if (diagBody) diagBody.innerHTML = 'Outstanding physics mastery! Coco is doing zoomies in celebration!';
                        showCocoBubble("🏆 All 11 Solved! You\\'re a Physics Pro!", 'success', 6000);
                    }
                }, 2000);
            } else {
                health = Math.max(0, health - 10);
                updateLevelsUI();

                const diag = getDiagnosticFeedback(currentSelectedLetter, targetLetter);
                const randomError = cocoErrorQuotes[Math.floor(Math.random() * cocoErrorQuotes.length)];
                
                if (cocoAvatarBadge) cocoAvatarBadge.textContent = '🐶';
                diagnosticCard.className = 'diagnostic-card error';
                if (diagCocoQuote) diagCocoQuote.innerHTML = randomError;
                if (diagBody) diagBody.innerHTML = `<strong>${diag.title}</strong>: ${diag.body}`;

                // Show speech bubble over Coco on the track
                showCocoBubble("🐾 Ruh-roh! Check the hint below!", 'error', 3500);
            }
        });'''

new_btn_check = '''        btnCheck.addEventListener('click', () => {
            if (!currentSelectedLetter) return;

            const targetLetter = levelAssignments[currentLevel];

            if (currentSelectedLetter === targetLetter) {
                solvedLevels.add(currentLevel);
                diagnosticCard.className = 'diagnostic-card success';
                
                const randomPraise = cocoSuccessPraise[Math.floor(Math.random() * cocoSuccessPraise.length)];
                if (cocoAvatarBadge) cocoAvatarBadge.textContent = '🎉';
                if (diagCocoQuote) diagCocoQuote.innerHTML = randomPraise;
                if (diagBody) diagBody.innerHTML = `<strong>Spot on!</strong> Motion #${currentLevel + 1} perfectly matches Graph ${currentSelectedLetter}: <em>${graphs[targetLetter].desc}</em><br><small style="color: #047857; margin-top: 4px; display: inline-block;">Take your time to replay the motion and study the graph. When ready, click <strong>Next Motion ➔</strong>.</small>`;
                
                // Show speech bubble over Coco on the track
                showCocoBubble("🦴 Pawsome match! Spot on!", 'success', 4000);

                updateLevelsUI();

                // Reveal Next Motion button without moving automatically
                btnCheck.style.display = 'none';
                btnNextMotion.style.display = 'inline-flex';
                
                if (solvedLevels.size < 11) {
                    let next = (currentLevel + 1) % 11;
                    while (solvedLevels.has(next)) next = (next + 1) % 11;
                    btnNextMotion.textContent = `Next Motion (#${next + 1}) ➔`;
                } else {
                    btnNextMotion.textContent = '🏆 All 11 Motions Mastered!';
                }
            } else {
                health = Math.max(0, health - 10);
                updateLevelsUI();

                const diag = getDiagnosticFeedback(currentSelectedLetter, targetLetter);
                const randomError = cocoErrorQuotes[Math.floor(Math.random() * cocoErrorQuotes.length)];
                
                if (cocoAvatarBadge) cocoAvatarBadge.textContent = '💡';
                diagnosticCard.className = 'diagnostic-card error';
                if (diagCocoQuote) diagCocoQuote.innerHTML = randomError;
                if (diagBody) diagBody.innerHTML = `<strong>${diag.title}:</strong> ${diag.body}`;

                // Show specific, actionable speech bubble over Coco
                showCocoBubble(diag.bubbleHint, 'error', 4500);
            }
        });

        // Next Motion button click handler (Manual Student Progression)
        btnNextMotion.addEventListener('click', () => {
            if (solvedLevels.size < 11) {
                let next = (currentLevel + 1) % 11;
                while (solvedLevels.has(next)) next = (next + 1) % 11;
                loadLevel(next, false);
            } else {
                alert('🏆 Outstanding achievement! You have mastered all 11 Kinematic motion scenarios!');
            }
        });'''

html = html.replace(old_btn_check, new_btn_check)

# 7. Update getDiagnosticFeedback to return bubbleHint and crystal clear physics feedback
old_diag_func = '''        function getDiagnosticFeedback(chosenLetter, targetLetter) {
            const chosen = graphs[chosenLetter];
            const target = graphs[targetLetter];

            if (chosen.type !== target.type) {
                return {
                    title: "⚠️ Graph Type Confusion",
                    body: `Graph ${chosenLetter} is a <strong>${chosen.type.toUpperCase()}</strong> graph, but Coco's motion currently corresponds to a <strong>${target.type.toUpperCase()}</strong> graph. Check the vertical axis!`
                };
            }

            let targetInitialDir = target.startV > 0 ? "right" : (target.startV < 0 ? "left" : "at rest");
            let chosenInitialDir = chosen.startV > 0 ? "right" : (chosen.startV < 0 ? "left" : "at rest");
            if (targetInitialDir !== chosenInitialDir && targetInitialDir !== "at rest") {
                return {
                    title: "🧭 Direction Mismatch",
                    body: `Coco starts by running <strong>${targetInitialDir}</strong>, but Graph ${chosenLetter} represents an object starting <strong>${chosenInitialDir}</strong>.`
                };
            }

            if (target.stages[0].a !== 0 && chosen.stages[0].a === 0) {
                return {
                    title: "📈 Acceleration Misconception",
                    body: `Coco is <strong>accelerating</strong> (changing speed). Graph ${chosenLetter} shows a straight slope with zero acceleration.`
                };
            }

            return {
                title: "❌ Misconception Check",
                body: `Graph ${chosenLetter} shows: <em>${chosen.desc}</em><br>Watch Coco's trot and observe how she accelerates and pauses.`
            };
        }'''

new_diag_func = '''        function getDiagnosticFeedback(chosenLetter, targetLetter) {
            const chosen = graphs[chosenLetter];
            const target = graphs[targetLetter];

            if (chosen.type !== target.type) {
                return {
                    title: "⚠️ Graph Type Misconception",
                    body: `Graph ${chosenLetter} is a <strong>${chosen.type.toUpperCase()}</strong> graph, but Coco's current run corresponds to a <strong>${target.type.toUpperCase()}</strong> graph. Look closely at the vertical axis label.`,
                    bubbleHint: "🐾 Check the graph's vertical axis (x vs v)!"
                };
            }

            let targetInitialDir = target.startV > 0 ? "right (+)" : (target.startV < 0 ? "left (-)" : "at rest (0)");
            let chosenInitialDir = chosen.startV > 0 ? "right (+)" : (chosen.startV < 0 ? "left (-)" : "at rest (0)");
            if (targetInitialDir !== chosenInitialDir && targetInitialDir !== "at rest (0)") {
                return {
                    title: "🧭 Direction Mismatch",
                    body: `Coco starts her trot moving <strong>${targetInitialDir}</strong>, but Graph ${chosenLetter} represents motion starting <strong>${chosenInitialDir}</strong>.`,
                    bubbleHint: "🐾 Check my trot direction: Left (-) vs Right (+)!"
                };
            }

            if (target.stages[0].a !== 0 && chosen.stages[0].a === 0) {
                return {
                    title: "📈 Acceleration Clue",
                    body: `Coco is <strong>accelerating</strong> (changing speed, pawprints change spacing). Graph ${chosenLetter} shows constant speed with zero acceleration.`,
                    bubbleHint: "🐾 Notice: Am I speeding up or trotting steady?"
                };
            }

            return {
                title: "🐾 Kinematic Breakdown",
                body: `Graph ${chosenLetter} represents: <em>${chosen.desc}</em>. Replay Coco's motion and watch where she accelerates, pauses, or turns around.`,
                bubbleHint: "🐾 Replay to watch my speed & pawprint spacing!"
            };
        }'''

html = html.replace(old_diag_func, new_diag_func)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated paw prints, manual navigation, and refined hints successfully.")
