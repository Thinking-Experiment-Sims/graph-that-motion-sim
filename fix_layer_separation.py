with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update canvas height to 215
html = html.replace('<canvas id="simCanvas" width="850" height="185"></canvas>', '<canvas id="simCanvas" width="850" height="215"></canvas>')

# 2. Update trackY to 155
html = html.replace('const trackY = 125;', 'const trackY = 155;')

# 3. Update drawSpeechBubble with clean positioning and higher clearance
old_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
            ctx.save();
            ctx.font = 'bold 13px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            const metrics = ctx.measureText(text);
            const padX = 14;
            const bw = metrics.width + padX * 2;
            const bh = 30;
            const bx = Math.max(10, Math.min(simCanvas.width - bw - 10, x - bw / 2));
            // Ensure bubble never overflows the top border
            const by = Math.max(8, y - bh);

            // Bubble background
            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = type === 'success' ? '#10b981' : (type === 'error' ? '#ef4444' : '#0f7e9b');
            ctx.lineWidth = 2.5;
            ctx.shadowColor = 'rgba(0,0,0,0.18)';
            ctx.shadowBlur = 8;
            ctx.shadowOffsetY = 3;

            // Rounded rect
            ctx.beginPath();
            const r = 8;
            ctx.moveTo(bx + r, by);
            ctx.lineTo(bx + bw - r, by);
            ctx.arcTo(bx + bw, by, bx + bw, by + r, r);
            ctx.lineTo(bx + bw, by + bh - r);
            ctx.arcTo(bx + bw, by + bh, bx + bw - r, by + bh, r);
            
            // Pointer tail
            const tailX = Math.max(bx + 20, Math.min(bx + bw - 20, x));
            ctx.lineTo(tailX + 7, by + bh);
            ctx.lineTo(x, by + bh + 8);
            ctx.lineTo(tailX - 7, by + bh);

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

html = html.replace(old_bubble, new_bubble)

# 4. Update renderStage layering:
# Vector layers at trackY - 82 and trackY - 100
# Speech bubble at trackY - 116 (from y=6 to 38), totally above vectors!
old_render_end = '''            // Draw Coco the Black Pug
            let pugPx = margin + pug.x * pxPerMeter;
            drawCocoThePug(sctx, pugPx, trackY, pug.heading, pug.legPhase, Math.abs(pug.v) > 0.1);

            // Draw Coco Speech Bubble if active (above Coco's head with ample clearance)
            if (cocoBubbleText) {
                drawSpeechBubble(sctx, pugPx, trackY - 84, cocoBubbleText, cocoBubbleType);
            }

            // Live Velocity Vector (Amber)
            if (showVelocity && Math.abs(pug.v) > 0.1) {
                let vLen = pug.v * 7;
                drawVectorArrow(sctx, pugPx, trackY - 80, pugPx + vLen, trackY - 80, "#d67b19", 3.5, "v");
            }

            // Live Acceleration Vector (Teal)
            if (showAcceleration && Math.abs(pug.a) > 0.1) {
                let aLen = pug.a * 14;
                drawVectorArrow(sctx, pugPx, trackY - 96, pugPx + aLen, trackY - 96, "#0f7e9b", 3.5, "a");
            }'''

new_render_end = '''            // Draw Coco the Black Pug
            let pugPx = margin + pug.x * pxPerMeter;
            drawCocoThePug(sctx, pugPx, trackY, pug.heading, pug.legPhase, Math.abs(pug.v) > 0.1);

            // Live Velocity Vector (Amber, just above Coco's head)
            if (showVelocity && Math.abs(pug.v) > 0.1) {
                let vLen = pug.v * 7;
                drawVectorArrow(sctx, pugPx, trackY - 82, pugPx + vLen, trackY - 82, "#d67b19", 3.5, "v");
            }

            // Live Acceleration Vector (Teal, stacked neatly above velocity)
            if (showAcceleration && Math.abs(pug.a) > 0.1) {
                let aLen = pug.a * 14;
                drawVectorArrow(sctx, pugPx, trackY - 100, pugPx + aLen, trackY - 100, "#0f7e9b", 3.5, "a");
            }

            // Draw Coco Speech Bubble if active (floating at top tier, completely above all vectors)
            if (cocoBubbleText) {
                drawSpeechBubble(sctx, pugPx, trackY - 116, cocoBubbleText, cocoBubbleType);
            }'''

html = html.replace(old_render_end, new_render_end)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Layer separation updated.")
