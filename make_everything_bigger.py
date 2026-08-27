with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Update CSS for wider max-width and enlarged components
old_css_workspace = '''.workspace {
            max-width: 1360px;
            margin: 1.5rem auto;
            padding: 0 1.25rem;
        }

        .lab-layout {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 1.5rem;
            align-items: start;
        }'''

new_css_workspace = '''.workspace {
            max-width: 1680px;
            width: 95%;
            margin: 1.5rem auto;
            padding: 0 1rem;
        }

        .header-content {
            max-width: 1680px;
            width: 95%;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .lab-layout {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 1.75rem;
            align-items: start;
        }'''

html = html.replace(old_css_workspace, new_css_workspace)

# 2. Update panel-card, telemetry, cards gallery, buttons in CSS
old_css_components = '''.panel-card {
            background-color: var(--bg-white);
            border-radius: 12px;
            padding: 1.4rem;
            box-shadow: var(--card-shadow);
            border: 1px solid var(--border-light);
        }

        /* Arena Stage Header */
        .stage-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .scenario-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background-color: var(--primary-teal-light);
            color: var(--primary-teal);
            font-weight: 700;
            font-size: 0.9rem;
            padding: 0.3rem 0.75rem;
            border-radius: 20px;
            border: 1px solid rgba(15, 126, 155, 0.2);
        }

        .direction-bar {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-weight: 700;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .direction-bar span.sign {
            color: var(--primary-teal);
            font-weight: 800;
        }

        /* Track Container */
        .track-canvas-wrap {
            width: 100%;
            background: #ffffff;
            border: 2px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            box-shadow: inset 0 2px 8px rgba(0,0,0,0.04);
        }

        canvas#simCanvas {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Live Telemetry HUD */
        .telemetry-hud {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.6rem;
            margin-top: 0.85rem;
            padding: 0.6rem 0.85rem;
            background: var(--bg-page);
            border-radius: 8px;
            border: 1px solid var(--border-light);
        }

        .hud-item {
            text-align: center;
        }

        .hud-label {
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .hud-val {
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--primary-teal);
            font-variant-numeric: tabular-nums;
        }

        /* Sleek Playback Toolbar */
        .playback-dock {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-top: 0.85rem;
            flex-wrap: wrap;
            padding: 0.6rem 1rem;
            background: #ffffff;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .btn-action {
            background-color: var(--accent-amber);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.88rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.15s ease;
        }'''

new_css_components = '''.panel-card {
            background-color: var(--bg-white);
            border-radius: 14px;
            padding: 1.65rem;
            box-shadow: var(--card-shadow);
            border: 1px solid var(--border-light);
        }

        /* Arena Stage Header */
        .stage-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.85rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .scenario-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background-color: var(--primary-teal-light);
            color: var(--primary-teal);
            font-weight: 800;
            font-size: 1.05rem;
            padding: 0.4rem 1rem;
            border-radius: 24px;
            border: 1.5px solid rgba(15, 126, 155, 0.25);
        }

        .direction-bar {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            font-weight: 800;
            font-size: 1rem;
            color: var(--text-muted);
        }

        .direction-bar span.sign {
            color: var(--primary-teal);
            font-weight: 800;
        }

        /* Track Container */
        .track-canvas-wrap {
            width: 100%;
            background: #ffffff;
            border: 2px solid var(--border-color);
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);
        }

        canvas#simCanvas {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Live Telemetry HUD */
        .telemetry-hud {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.85rem;
            margin-top: 1rem;
            padding: 0.85rem 1.25rem;
            background: var(--bg-page);
            border-radius: 10px;
            border: 1px solid var(--border-light);
        }

        .hud-item {
            text-align: center;
        }

        .hud-label {
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }

        .hud-val {
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--primary-teal);
            font-variant-numeric: tabular-nums;
            margin-top: 0.15rem;
        }

        /* Sleek Playback Toolbar */
        .playback-dock {
            display: flex;
            align-items: center;
            gap: 0.85rem;
            margin-top: 1rem;
            flex-wrap: wrap;
            padding: 0.75rem 1.25rem;
            background: #ffffff;
            border-radius: 10px;
            border: 1px solid var(--border-color);
        }

        .btn-action {
            background-color: var(--accent-amber);
            color: white;
            border: none;
            padding: 0.65rem 1.25rem;
            border-radius: 8px;
            font-weight: 800;
            font-size: 0.95rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.15s ease;
        }'''

html = html.replace(old_css_components, new_css_components)

# 3. Update cards gallery CSS
old_cards_css = '''.cards-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(88px, 1fr));
            gap: 0.55rem;
            margin-bottom: 1rem;
        }

        .graph-card-btn {
            background: #ffffff;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            padding: 0.5rem 0.3rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.2rem;
        }'''

new_cards_css = '''.cards-gallery {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 0.75rem;
            margin-bottom: 1.15rem;
        }

        .graph-card-btn {
            background: #ffffff;
            border: 2px solid var(--border-color);
            border-radius: 10px;
            padding: 0.75rem 0.4rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.3rem;
        }'''

html = html.replace(old_cards_css, new_cards_css)

# 4. Update canvas sizes in HTML
html = html.replace('<canvas id="simCanvas" width="850" height="215"></canvas>', '<canvas id="simCanvas" width="1100" height="280"></canvas>')
html = html.replace('<canvas id="graphCanvas" width="340" height="210" style="display: none;"></canvas>', '<canvas id="graphCanvas" width="480" height="300" style="display: none;"></canvas>')

# 5. Update Javascript canvas coordinate constants and drawing functions
old_js_constants = '''        let pawprintsList = [];
        const pawInterval = 0.28;
        const trackLength = 20;
        const trackY = 155;
        const pug = { x: 0, v: 0, a: 0, heading: 1, legPhase: 0 };'''

new_js_constants = '''        let pawprintsList = [];
        const pawInterval = 0.26;
        const trackLength = 20;
        const trackY = 205;
        const pug = { x: 0, v: 0, a: 0, heading: 1, legPhase: 0 };'''

html = html.replace(old_js_constants, new_js_constants)

# 6. Update drawSpeechBubble for larger canvas
old_js_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
            ctx.save();
            ctx.font = 'bold 13px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            const metrics = ctx.measureText(text);
            const padX = 16;
            const maxW = simCanvas.width - 24;
            const bw = Math.min(maxW, metrics.width + padX * 2);
            const bh = 34;
            const bx = Math.max(12, Math.min(simCanvas.width - bw - 12, x - bw / 2));
            const by = Math.max(6, y - bh);

            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = type === 'success' ? '#10b981' : (type === 'error' ? '#ef4444' : '#0f7e9b');
            ctx.lineWidth = 2.5;
            ctx.shadowColor = 'rgba(0,0,0,0.18)';
            ctx.shadowBlur = 10;
            ctx.shadowOffsetY = 4;

            ctx.beginPath();
            const r = 8;
            ctx.moveTo(bx + r, by);
            ctx.lineTo(bx + bw - r, by);
            ctx.arcTo(bx + bw, by, bx + bw, by + r, r);
            ctx.lineTo(bx + bw, by + bh - r);
            ctx.arcTo(bx + bw, by + bh, bx + bw - r, by + bh, r);
            
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

            ctx.shadowColor = 'transparent';
            ctx.fillStyle = '#0f172a';
            ctx.textAlign = 'left';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, bx + padX, by + bh / 2);
            ctx.restore();
        }'''

new_js_bubble = '''        function drawSpeechBubble(ctx, x, y, text, type) {
            ctx.save();
            ctx.font = 'bold 15px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            const metrics = ctx.measureText(text);
            const padX = 20;
            const maxW = simCanvas.width - 30;
            const bw = Math.min(maxW, metrics.width + padX * 2);
            const bh = 42;
            const bx = Math.max(16, Math.min(simCanvas.width - bw - 16, x - bw / 2));
            const by = Math.max(8, y - bh);

            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = type === 'success' ? '#10b981' : (type === 'error' ? '#ef4444' : '#0f7e9b');
            ctx.lineWidth = 3;
            ctx.shadowColor = 'rgba(0,0,0,0.18)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 5;

            ctx.beginPath();
            const r = 10;
            ctx.moveTo(bx + r, by);
            ctx.lineTo(bx + bw - r, by);
            ctx.arcTo(bx + bw, by, bx + bw, by + r, r);
            ctx.lineTo(bx + bw, by + bh - r);
            ctx.arcTo(bx + bw, by + bh, bx + bw - r, by + bh, r);
            
            const tailX = Math.max(bx + 24, Math.min(bx + bw - 24, x));
            ctx.lineTo(tailX + 8, by + bh);
            ctx.lineTo(x, by + bh + 10);
            ctx.lineTo(tailX - 8, by + bh);

            ctx.lineTo(bx + r, by + bh);
            ctx.arcTo(bx, by + bh, bx, by + bh - r, r);
            ctx.lineTo(bx, by + r);
            ctx.arcTo(bx, by, bx + r, by, r);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();

            ctx.shadowColor = 'transparent';
            ctx.fillStyle = '#0f172a';
            ctx.textAlign = 'left';
            ctx.textBaseline = 'middle';
            ctx.fillText(text, bx + padX, by + bh / 2);
            ctx.restore();
        }'''

html = html.replace(old_js_bubble, new_js_bubble)

# 7. Update renderStage coordinate layers for larger canvas
old_render_stage = '''        function renderStage() {
            const w = simCanvas.width;
            const h = simCanvas.height;
            const margin = 45;
            const trackW = w - 2 * margin;
            const pxPerMeter = trackW / trackLength;

            sctx.clearRect(0, 0, w, h);

            // Runway Boundary Line
            sctx.beginPath();
            sctx.moveTo(margin, trackY);
            sctx.lineTo(w - margin, trackY);
            sctx.strokeStyle = "#94a3b8";
            sctx.lineWidth = 3;
            sctx.stroke();

            // Coordinate Ticks
            sctx.fillStyle = "#64748b";
            sctx.font = "bold 11px sans-serif";
            sctx.textAlign = "center";
            for (let m = 0; m <= trackLength; m += 2) {
                let px = margin + m * pxPerMeter;
                sctx.beginPath();
                sctx.moveTo(px, trackY);
                sctx.lineTo(px, trackY + 7);
                sctx.strokeStyle = "#94a3b8";
                sctx.lineWidth = 1.5;
                sctx.stroke();
                sctx.fillText(m + "m", px, trackY + 22);
            }

            // Pawprint Motion Map
            if (showPawprints) {
                const pawY = trackY - 2;
                pawprintsList.forEach(dot => {
                    let dpx = margin + dot.x * pxPerMeter;
                    let dpy = pawY - (dot.restStack * 7);
                    if (dot.restStack === 0) dpy = pawY;

                    drawPawPrint(sctx, dpx, dpy, dot.v < 0 ? -1 : 1, dot.restStack > 0, dot.restStack);

                    if (showVelocity && Math.abs(dot.v) > 0.3) {
                        drawVectorArrow(sctx, dpx, dpy - 10, dpx + dot.v * 3, dpy - 10, "#d67b19", 1.5);
                    }
                });
            }

            // Draw Coco the Black Pug
            let pugPx = margin + pug.x * pxPerMeter;
            drawCocoThePug(sctx, pugPx, trackY, pug.heading, pug.legPhase, Math.abs(pug.v) > 0.1);

            // Live Velocity Vector (Amber)
            if (showVelocity && Math.abs(pug.v) > 0.1) {
                let vLen = pug.v * 7;
                drawVectorArrow(sctx, pugPx, trackY - 82, pugPx + vLen, trackY - 82, "#d67b19", 3.5, "v");
            }

            // Live Acceleration Vector (Teal)
            if (showAcceleration && Math.abs(pug.a) > 0.1) {
                let aLen = pug.a * 14;
                drawVectorArrow(sctx, pugPx, trackY - 100, pugPx + aLen, trackY - 100, "#0f7e9b", 3.5, "a");
            }

            // Draw Coco Speech Bubble
            if (cocoBubbleText) {
                drawSpeechBubble(sctx, pugPx, trackY - 116, cocoBubbleText, cocoBubbleType);
            }
        }'''

new_render_stage = '''        function renderStage() {
            const w = simCanvas.width;
            const h = simCanvas.height;
            const margin = 55;
            const trackW = w - 2 * margin;
            const pxPerMeter = trackW / trackLength;

            sctx.clearRect(0, 0, w, h);

            // Runway Boundary Line
            sctx.beginPath();
            sctx.moveTo(margin, trackY);
            sctx.lineTo(w - margin, trackY);
            sctx.strokeStyle = "#64748b";
            sctx.lineWidth = 3.5;
            sctx.stroke();

            // Coordinate Ticks & Numbers
            sctx.fillStyle = "#475569";
            sctx.font = "bold 13px sans-serif";
            sctx.textAlign = "center";
            for (let m = 0; m <= trackLength; m += 2) {
                let px = margin + m * pxPerMeter;
                sctx.beginPath();
                sctx.moveTo(px, trackY);
                sctx.lineTo(px, trackY + 9);
                sctx.strokeStyle = "#64748b";
                sctx.lineWidth = 2;
                sctx.stroke();
                sctx.fillText(m + "m", px, trackY + 26);
            }

            // Pawprint Motion Map
            if (showPawprints) {
                const pawY = trackY - 3;
                pawprintsList.forEach(dot => {
                    let dpx = margin + dot.x * pxPerMeter;
                    let dpy = pawY - (dot.restStack * 10);
                    if (dot.restStack === 0) dpy = pawY;

                    drawPawPrint(sctx, dpx, dpy, dot.v < 0 ? -1 : 1, dot.restStack > 0, dot.restStack);

                    if (showVelocity && Math.abs(dot.v) > 0.3) {
                        drawVectorArrow(sctx, dpx, dpy - 14, dpx + dot.v * 4.5, dpy - 14, "#d67b19", 2);
                    }
                });
            }

            // Draw Coco the Black Pug (Enlarged and centered)
            let pugPx = margin + pug.x * pxPerMeter;
            drawCocoThePug(sctx, pugPx, trackY, pug.heading, pug.legPhase, Math.abs(pug.v) > 0.1);

            // Live Velocity Vector (Amber, prominent)
            if (showVelocity && Math.abs(pug.v) > 0.1) {
                let vLen = pug.v * 9;
                drawVectorArrow(sctx, pugPx, trackY - 112, pugPx + vLen, trackY - 112, "#d67b19", 4.5, "v");
            }

            // Live Acceleration Vector (Teal, prominent above velocity)
            if (showAcceleration && Math.abs(pug.a) > 0.1) {
                let aLen = pug.a * 18;
                drawVectorArrow(sctx, pugPx, trackY - 138, pugPx + aLen, trackY - 138, "#0f7e9b", 4.5, "a");
            }

            // Draw Coco Speech Bubble (Floating high with plenty of room)
            if (cocoBubbleText) {
                drawSpeechBubble(sctx, pugPx, trackY - 158, cocoBubbleText, cocoBubbleType);
            }
        }'''

html = html.replace(old_render_stage, new_render_stage)

# 8. Update drawPawPrint for larger scale
old_draw_paw = '''        function drawPawPrint(ctx, x, y, heading, isRest = false, restStack = 0) {
            ctx.save();
            ctx.translate(x, y);
            if (!isRest && heading < 0) ctx.scale(-1, 1);
            
            const scale = 0.9;
            ctx.fillStyle = '#d67b19';
            ctx.strokeStyle = '#b06210';
            ctx.lineWidth = 1;

            ctx.beginPath();
            ctx.ellipse(0, 1.5 * scale, 4.2 * scale, 3.2 * scale, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();

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

new_draw_paw = '''        function drawPawPrint(ctx, x, y, heading, isRest = false, restStack = 0) {
            ctx.save();
            ctx.translate(x, y);
            if (!isRest && heading < 0) ctx.scale(-1, 1);
            
            const scale = 1.35;
            ctx.fillStyle = '#d67b19';
            ctx.strokeStyle = '#b06210';
            ctx.lineWidth = 1.2;

            ctx.beginPath();
            ctx.ellipse(0, 1.5 * scale, 4.2 * scale, 3.2 * scale, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();

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

html = html.replace(old_draw_paw, new_draw_paw)

# 9. Update drawCocoThePug dimensions for enlarged sprite
old_draw_coco = '''            const bounce = isMoving ? Math.abs(Math.sin(legPhase)) * 3.5 : 0;
            const w = 55;
            const h = 76;'''

new_draw_coco = '''            const bounce = isMoving ? Math.abs(Math.sin(legPhase)) * 4.5 : 0;
            const w = 75;
            const h = 104;'''

html = html.replace(old_draw_coco, new_draw_coco)

# 10. Update renderSingleGraph for larger graph canvas (480x300)
old_graph_render = '''        function drawGraphPreview(scen) {
            const w = graphCanvas.width;
            const h = graphCanvas.height;
            const m = 40;

            gctx.clearRect(0, 0, w, h);

            if (!showDual) {
                renderSingleGraph(gctx, scen, scen.type, m, 15, w - m - 20, h - m - 20, true);
            } else {
                let subH = (h - 2 * m) / 2;
                renderSingleGraph(gctx, scen, 'position', m, 10, w - m - 20, subH, false, "position (x)");
                renderSingleGraph(gctx, scen, 'velocity', m, subH + 35, w - m - 20, subH, true, "velocity (v)");
            }
        }

        function renderSingleGraph(ctx, scen, type, ox, oy, plotW, plotH, showTimeLabel, customYLabel = null) {
            ctx.strokeStyle = "#000000";
            ctx.lineWidth = 2;

            // Y-Axis
            ctx.beginPath();
            ctx.moveTo(ox, oy);
            ctx.lineTo(ox, oy + plotH);
            ctx.stroke();

            // X-Axis
            let xAxisY = oy + plotH;
            if (type === 'velocity') xAxisY = oy + plotH / 2;
            ctx.beginPath();
            ctx.moveTo(ox, xAxisY);
            ctx.lineTo(ox + plotW, xAxisY);
            ctx.stroke();

            // Labels
            ctx.fillStyle = "#000000";
            ctx.font = "bold 11px sans-serif";
            if (showTimeLabel) {
                ctx.textAlign = "center";
                ctx.fillText("time (s)", ox + plotW / 2, oy + plotH + 16);
            }

            ctx.save();
            ctx.translate(ox - 24, oy + plotH / 2);
            ctx.rotate(-Math.PI / 2);
            ctx.textAlign = "center";
            ctx.fillText(customYLabel || (type === 'position' ? 'position (x)' : 'velocity (v)'), 0, 0);
            ctx.restore();

            if (type === 'velocity') {
                ctx.font = "bold 10px sans-serif";
                ctx.textAlign = "right";
                ctx.fillText("+", ox - 4, oy + 12);
                ctx.fillText("0", ox - 4, xAxisY + 3);
                ctx.fillText("-", ox - 4, oy + plotH - 2);
            }

            // Curve
            ctx.strokeStyle = type === 'position' ? "#0f7e9b" : "#d67b19";
            ctx.lineWidth = 3;'''

new_graph_render = '''        function drawGraphPreview(scen) {
            const w = graphCanvas.width;
            const h = graphCanvas.height;
            const m = 50;

            gctx.clearRect(0, 0, w, h);

            if (!showDual) {
                renderSingleGraph(gctx, scen, scen.type, m, 20, w - m - 25, h - m - 30, true);
            } else {
                let subH = (h - 2 * m) / 2;
                renderSingleGraph(gctx, scen, 'position', m, 12, w - m - 25, subH, false, "position (x)");
                renderSingleGraph(gctx, scen, 'velocity', m, subH + 45, w - m - 25, subH, true, "velocity (v)");
            }
        }

        function renderSingleGraph(ctx, scen, type, ox, oy, plotW, plotH, showTimeLabel, customYLabel = null) {
            ctx.strokeStyle = "#1e293b";
            ctx.lineWidth = 2.5;

            // Y-Axis
            ctx.beginPath();
            ctx.moveTo(ox, oy);
            ctx.lineTo(ox, oy + plotH);
            ctx.stroke();

            // X-Axis
            let xAxisY = oy + plotH;
            if (type === 'velocity') xAxisY = oy + plotH / 2;
            ctx.beginPath();
            ctx.moveTo(ox, xAxisY);
            ctx.lineTo(ox + plotW, xAxisY);
            ctx.stroke();

            // Labels
            ctx.fillStyle = "#1e293b";
            ctx.font = "bold 13px sans-serif";
            if (showTimeLabel) {
                ctx.textAlign = "center";
                ctx.fillText("time (s)", ox + plotW / 2, oy + plotH + 22);
            }

            ctx.save();
            ctx.translate(ox - 30, oy + plotH / 2);
            ctx.rotate(-Math.PI / 2);
            ctx.textAlign = "center";
            ctx.fillText(customYLabel || (type === 'position' ? 'position (x)' : 'velocity (v)'), 0, 0);
            ctx.restore();

            if (type === 'velocity') {
                ctx.font = "bold 12px sans-serif";
                ctx.textAlign = "right";
                ctx.fillText("+", ox - 6, oy + 14);
                ctx.fillText("0", ox - 6, xAxisY + 4);
                ctx.fillText("-", ox - 6, oy + plotH - 2);
            }

            // Curve
            ctx.strokeStyle = type === 'position' ? "#0f7e9b" : "#d67b19";
            ctx.lineWidth = 4;'''

html = html.replace(old_graph_render, new_graph_render)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Scaled up UI and canvas dimensions successfully!")
