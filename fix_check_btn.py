with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update DOM elements binding
old_dom = '''        const diagnosticCard = document.getElementById('diagnosticCard');
        const diagTitle = document.getElementById('diagTitle');
        const diagBody = document.getElementById('diagBody');'''

new_dom = '''        const diagnosticCard = document.getElementById('diagnosticCard');
        const cocoAvatarBadge = document.getElementById('cocoAvatarBadge');
        const diagCocoQuote = document.getElementById('diagCocoQuote');
        const diagBody = document.getElementById('diagBody');'''

html = html.replace(old_dom, new_dom)

# 2. Update btnCheck listener
old_btn = '''        btnCheck.addEventListener('click', () => {
            if (!currentSelectedLetter) return;

            const targetLetter = levelAssignments[currentLevel];

            if (currentSelectedLetter === targetLetter) {
                solvedLevels.add(currentLevel);
                diagnosticCard.className = 'diagnostic-card success';
                diagTitle.innerHTML = '🎉 Good Dog, Coco! Correct Match!';
                diagBody.innerHTML = `Awesome! Motion #${currentLevel + 1} corresponds to Graph ${currentSelectedLetter}: <em>${graphs[targetLetter].desc}</em>`;
                
                updateLevelsUI();

                setTimeout(() => {
                    if (solvedLevels.size < 11) {
                        let next = (currentLevel + 1) % 11;
                        while (solvedLevels.has(next)) next = (next + 1) % 11;
                        loadLevel(next, false);
                    } else {
                        diagTitle.innerHTML = '🏆 Mastered All 11 Adventures!';
                        diagBody.innerHTML = 'Outstanding work! You have successfully mastered all 1D Kinematic graphs.';
                    }
                }, 1400);
            } else {
                health = Math.max(0, health - 10);
                updateLevelsUI();

                const diag = getDiagnosticFeedback(currentSelectedLetter, targetLetter);
                diagnosticCard.className = 'diagnostic-card error';
                diagTitle.innerHTML = diag.title;
                diagBody.innerHTML = diag.body;
            }
        });'''

new_btn = '''        btnCheck.addEventListener('click', () => {
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

html = html.replace(old_btn, new_btn)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated btnCheck logic successfully.")
