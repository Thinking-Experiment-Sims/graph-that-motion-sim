with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update canvas height to 185
html = html.replace('<canvas id="simCanvas" width="850" height="150"></canvas>', '<canvas id="simCanvas" width="850" height="185"></canvas>')

# 2. Update trackY to 125
html = html.replace('const trackY = 95;', 'const trackY = 125;')

# 3. Update overlay checkboxes text (remove broken combining character glyphs)
old_overlays = '''                <!-- PER Overlays -->
                <div class="overlays-toolbar">
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkVelocity" checked>
                        <span>Velocity (<span class="math-expr"><i>v&#x20D7;</i></span>)</span>
                    </label>
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkAcceleration" checked>
                        <span>Acceleration (<span class="math-expr"><i>a&#x20D7;</i></span>)</span>
                    </label>
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkMotionDots" checked>
                        <span>Pug Pawprints / Motion Dots</span>
                    </label>
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkTracer" checked>
                        <span>Live Graph Tracer</span>
                    </label>
                </div>'''

new_overlays = '''                <!-- PER Overlays -->
                <div class="overlays-toolbar">
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkVelocity" checked>
                        <span>Velocity (<span class="math-expr"><b>v</b></span>)</span>
                    </label>
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkAcceleration" checked>
                        <span>Acceleration (<span class="math-expr"><b>a</b></span>)</span>
                    </label>
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkMotionDots" checked>
                        <span>Pug Pawprints / Motion Dots</span>
                    </label>
                    <label class="overlay-toggle">
                        <input type="checkbox" id="chkTracer" checked>
                        <span>Live Graph Tracer</span>
                    </label>
                </div>'''

html = html.replace(old_overlays, new_overlays)

# 4. Improve drawSpeechBubble clamping and font rendering
old_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
            ctx.save();
            ctx.font = 'bold 12px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            const metrics = ctx.measureText(text);
            const padX = 14;
            const padY = 8;
            const bw = metrics.width + padX * 2;
            const bh = 28;
            const bx = Math.max(10, Math.min(simCanvas.width - bw - 10, x - bw / 2));
            const by = y - bh;

            // Bubble background
            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = type === 'success' ? '#10b981' : (type === 'error' ? '#ef4444' : 'var(--primary-teal)');
            ctx.lineWidth = 2;
            ctx.shadowColor = 'rgba(0,0,0,0.15)';
            ctx.shadowBlur = 8;
            ctx.shadowOffsetY = 2;

            // Rounded rect
            ctx.beginPath();
            const r = 8;
            ctx.moveTo(bx + r, by);
            ctx.lineTo(bx + bw - r, by);
            ctx.arcTo(bx + bw, by, bx + bw, by + r, r);
            ctx.lineTo(bx + bw, by + bh - r);
            ctx.arcTo(bx + bw, by + bh, bx + bw - r, by + bh, r);
            
            // Pointer tail
            const tailX = Math.max(bx + 15, Math.min(bx + bw - 15, x));
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
            ctx.fillStyle = '#1e293b';
            ctx.textAlign = 'left';
            ctx.fillText(text, bx + padX, by + 18);
            ctx.restore();
        }'''

new_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
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

html = html.replace(old_bubble, new_bubble)

# 5. Update renderStage vector positions & speech bubble position
old_render_end = '''            // Draw Coco the Black Pug
            let pugPx = margin + pug.x * pxPerMeter;
            drawCocoThePug(sctx, pugPx, trackY, pug.heading, pug.legPhase, Math.abs(pug.v) > 0.1);

            // Draw Coco Speech Bubble if active
            if (cocoBubbleText) {
                drawSpeechBubble(sctx, pugPx, trackY - 82, cocoBubbleText, cocoBubbleType);
            }

            // Live Velocity Vector (Amber)
            if (showVelocity && Math.abs(pug.v) > 0.1) {
                let vLen = pug.v * 7;
                drawVectorArrow(sctx, pugPx, trackY - 50, pugPx + vLen, trackY - 50, "var(--accent-amber)", 3.5, "v");
            }

            // Live Acceleration Vector (Teal)
            if (showAcceleration && Math.abs(pug.a) > 0.1) {
                let aLen = pug.a * 14;
                drawVectorArrow(sctx, pugPx, trackY - 65, pugPx + aLen, trackY - 65, "var(--primary-teal)", 3.5, "a");
            }'''

new_render_end = '''            // Draw Coco the Black Pug
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

html = html.replace(old_render_end, new_render_end)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Canvas layout and speech bubble positioning updated.")
