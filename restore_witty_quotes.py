with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update the witty quotes arrays exactly as requested
quotes_block = '''        const cocoSuccessPraise = [
            "🐾 Pawsome job! You nailed the slope! Here\\'s a virtual treat! 🦴",
            "🐾 Woof! That\\'s a treat-worthy match! Coco approved! 🎾",
            "🐾 Tail-wagging brilliance! You translated my zoomies into math! ⭐",
            "🐾 Spot on! You know your velocity from your position! 🐶",
            "🐾 Bark-tastic! You decoded my run like a physics champion! 🥓"
        ];

        const cocoErrorQuotes = [
            "🐾 Ruh-roh! Barking up the wrong graph! Let\\'s paws and try again...",
            "🐾 Sniffing in the wrong direction! Replay my run and watch my pawprints! 🦴",
            "🐾 Paws and reflect! Look closely at whether that\\'s a Position or Velocity graph! 🐶",
            "🐾 Not quite! My tail says check if I was speeding up or slowing down! 🐕"
        ];'''

html = re.sub(r'const cocoSuccessPraise = \[[\s\S]*?const cocoErrorQuotes = \[[\s\S]*?\];', quotes_block, html)

# 2. Update drawSpeechBubble to cleanly handle witty quotes of any length
old_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
            ctx.save();
            ctx.font = 'bold 13px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            const metrics = ctx.measureText(text);
            const padX = 14;
            const bw = metrics.width + padX * 2;
            const bh = 32;
            const bx = Math.max(12, Math.min(simCanvas.width - bw - 12, x - bw / 2));
            const by = Math.max(6, y - bh);

            // Bubble background with high contrast drop shadow
            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = type === 'success' ? '#10b981' : (type === 'error' ? '#ef4444' : '#0f7e9b');
            ctx.lineWidth = 2.5;
            ctx.shadowColor = 'rgba(0,0,0,0.22)';
            ctx.shadowBlur = 10;
            ctx.shadowOffsetY = 4;

            // Rounded rect
            ctx.beginPath();
            const r = 8;
            ctx.moveTo(bx + r, by);
            ctx.lineTo(bx + bw - r, by);
            ctx.arcTo(bx + bw, by, bx + bw, by + r, r);
            ctx.lineTo(bx + bw, by + bh - r);
            ctx.arcTo(bx + bw, by + bh, bx + bw - r, by + bh, r);
            
            // Pointer tail pointing directly down toward Coco
            const tailX = Math.max(bx + 16, Math.min(bx + bw - 16, x));
            ctx.lineTo(tailX + 6, by + bh);
            ctx.lineTo(x, by + bh + 8);
            ctx.lineTo(tailX - 6, by + bh);

            ctx.lineTo(bx + r, by + bh);
            ctx.arcTo(bx, by + bh, bx, by + bh - r, r);
            ctx.lineTo(bx, by + r);
            ctx.arcTo(bx, by, bx + r, by, r);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();

            // Text
            ctx.shadowColor = 'transparent';
            ctx.fillStyle = '#0f172a';
            ctx.textAlign = 'left';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, bx + padX, by + bh / 2);
            ctx.restore();
        }'''

new_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
            ctx.save();
            ctx.font = 'bold 13px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            const metrics = ctx.measureText(text);
            const padX = 16;
            const maxW = simCanvas.width - 24;
            const bw = Math.min(maxW, metrics.width + padX * 2);
            const bh = 34;
            const bx = Math.max(12, Math.min(simCanvas.width - bw - 12, x - bw / 2));
            const by = Math.max(6, y - bh);

            // Bubble background with high contrast drop shadow
            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = type === 'success' ? '#10b981' : (type === 'error' ? '#ef4444' : '#0f7e9b');
            ctx.lineWidth = 2.5;
            ctx.shadowColor = 'rgba(0,0,0,0.20)';
            ctx.shadowBlur = 10;
            ctx.shadowOffsetY = 4;

            // Rounded rect
            ctx.beginPath();
            const r = 8;
            ctx.moveTo(bx + r, by);
            ctx.lineTo(bx + bw - r, by);
            ctx.arcTo(bx + bw, by, bx + bw, by + r, r);
            ctx.lineTo(bx + bw, by + bh - r);
            ctx.arcTo(bx + bw, by + bh, bx + bw - r, by + bh, r);
            
            // Pointer tail pointing directly down toward Coco
            const tailX = Math.max(bx + 18, Math.min(bx + bw - 18, x));
            ctx.lineTo(tailX + 6, by + bh);
            ctx.lineTo(x, by + bh + 8);
            ctx.lineTo(tailX - 6, by + bh);

            ctx.lineTo(bx + r, by + bh);
            ctx.arcTo(bx, by + bh, bx, by + bh - r, r);
            ctx.lineTo(bx, by + r);
            ctx.arcTo(bx, by, bx + r, by, r);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();

            // Text
            ctx.shadowColor = 'transparent';
            ctx.fillStyle = '#0f172a';
            ctx.textAlign = 'left';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, bx + padX, by + bh / 2);
            ctx.restore();
        }'''

html = html.replace(old_bubble, new_bubble)

# 3. Update btnCheck to display the witty quote in both the speech bubble and the feedback card!
old_btn_check = '''        btnCheck.addEventListener('click', () => {
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
                
                // Show the witty praise directly in the speech bubble over Coco on the track
                showCocoBubble(randomPraise, 'success', 5000);

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
                
                // Select contextual witty error quote
                let randomError = cocoErrorQuotes[0];
                if (diag.type === 'axis') randomError = cocoErrorQuotes[2]; // Paws and reflect (Position vs Velocity)
                else if (diag.type === 'dir') randomError = cocoErrorQuotes[1]; // Sniffing in the wrong direction
                else if (diag.type === 'acc') randomError = cocoErrorQuotes[3]; // Not quite (speeding up or slowing down)
                else randomError = cocoErrorQuotes[Math.floor(Math.random() * cocoErrorQuotes.length)];
                
                if (cocoAvatarBadge) cocoAvatarBadge.textContent = '💡';
                diagnosticCard.className = 'diagnostic-card error';
                if (diagCocoQuote) diagCocoQuote.innerHTML = randomError;
                if (diagBody) diagBody.innerHTML = `<strong>${diag.title}:</strong> ${diag.body}`;

                // Show the exact witty error quote directly in the speech bubble over Coco on the track
                showCocoBubble(randomError, 'error', 5000);
            }
        });'''

html = html.replace(old_btn_check, new_btn_check)

# 4. Update getDiagnosticFeedback to return type
old_diag = '''        function getDiagnosticFeedback(chosenLetter, targetLetter) {
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

new_diag = '''        function getDiagnosticFeedback(chosenLetter, targetLetter) {
            const chosen = graphs[chosenLetter];
            const target = graphs[targetLetter];

            if (chosen.type !== target.type) {
                return {
                    type: 'axis',
                    title: "⚠️ Graph Type Check",
                    body: `Graph ${chosenLetter} is a <strong>${chosen.type.toUpperCase()}</strong> graph, but Coco's current run corresponds to a <strong>${target.type.toUpperCase()}</strong> graph. Look closely at the vertical axis label.`
                };
            }

            let targetInitialDir = target.startV > 0 ? "right (+)" : (target.startV < 0 ? "left (-)" : "at rest (0)");
            let chosenInitialDir = chosen.startV > 0 ? "right (+)" : (chosen.startV < 0 ? "left (-)" : "at rest (0)");
            if (targetInitialDir !== chosenInitialDir && targetInitialDir !== "at rest (0)") {
                return {
                    type: 'dir',
                    title: "🧭 Direction Check",
                    body: `Coco starts her trot moving <strong>${targetInitialDir}</strong>, but Graph ${chosenLetter} represents motion starting <strong>${chosenInitialDir}</strong>.`
                };
            }

            if (target.stages[0].a !== 0 && chosen.stages[0].a === 0) {
                return {
                    type: 'acc',
                    title: "📈 Speed & Acceleration Check",
                    body: `Coco is <strong>accelerating</strong> (changing speed, paw prints change spacing). Graph ${chosenLetter} shows constant speed with zero acceleration.`
                };
            }

            return {
                type: 'general',
                title: "🐾 Kinematic Breakdown",
                body: `Graph ${chosenLetter} represents: <em>${chosen.desc}</em>. Replay Coco's motion and watch where she accelerates, pauses, or turns around.`
            };
        }'''

html = html.replace(old_diag, new_diag)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Exact witty praise & guidance quotes restored and synced!")
