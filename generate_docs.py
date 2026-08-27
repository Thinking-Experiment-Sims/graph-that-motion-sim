import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

HEX_TEAL = "0F7E9B"
HEX_AMBER = "D67B19"
HEX_LIGHT_BG = "E6F4F8"
HEX_LIGHT_AMBER = "FDF3E8"
HEX_BORDER = "CBD5E1"
HEX_DARK = "1E293B"

RGB_TEAL = RGBColor(15, 126, 155)
RGB_AMBER = RGBColor(214, 123, 25)
RGB_DARK = RGBColor(30, 41, 59)
RGB_MUTED = RGBColor(100, 116, 139)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGB_TEAL
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = RGB_AMBER
    return p

def format_doc_header(doc, title, subtitle):
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(2)
    run_sub = p_sub.add_run("THE THINKING EXPERIMENT | KINEMATICS STUDIO")
    run_sub.font.name = 'Arial'
    run_sub.font.size = Pt(8.5)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGB_AMBER

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run(title)
    run_title.font.name = 'Arial'
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = RGB_TEAL

    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_after = Pt(12)
    run_desc = p_desc.add_run(subtitle)
    run_desc.font.name = 'Arial'
    run_desc.font.size = Pt(10)
    run_desc.font.color.rgb = RGB_MUTED

def add_callout(doc, title, bullets, is_amber=False):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.8)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_LIGHT_AMBER if is_amber else HEX_LIGHT_BG)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(title)
    run_t.font.name = 'Arial'
    run_t.font.size = Pt(10.5)
    run_t.font.bold = True
    run_t.font.color.rgb = RGB_AMBER if is_amber else RGB_TEAL
    
    for b in bullets:
        pb = cell.add_paragraph()
        pb.paragraph_format.space_after = Pt(2)
        run_b = pb.add_run(b)
        run_b.font.name = 'Arial'
        run_b.font.size = Pt(9.5)
        run_b.font.color.rgb = RGB_DARK
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(6)

def generate_student_handout(filepath):
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)
        
    format_doc_header(doc, "Kinematics Studio: Coco's Motion Lab", "Student Inquiry & Graphical Analysis Worksheet")
    
    add_callout(doc, "🎯 Learning Objectives", [
        "• Translate between 1D dog motions, directional pawprint motion maps, Position-Time (x-t), and Velocity-Time (v-t) graphs.",
        "• Apply slope rules: Slope of x-t = Velocity (v); Slope of v-t = Acceleration (a).",
        "• Distinguish between parabolic curved trajectories (changing speed) and linear segments (constant speed).",
        "• Relate motion map pawprint density to acceleration (widening spacing = speeding up; bunching spacing = slowing down)."
    ])
    
    add_heading_1(doc, "🧭 Motion Map Interpretation Key (Pawprint Trail)")
    p_map = doc.add_paragraph()
    p_map.paragraph_format.space_after = Pt(8)
    p_map.add_run("Coco drops an amber pawprint at fixed time intervals (Δt = 0.28 s):\n").font.color.rgb = RGB_DARK
    p_map.add_run("• Constant Velocity: ").bold = True
    p_map.add_run("Pawprints are evenly spaced along the runway.\n")
    p_map.add_run("• Speeding Up: ").bold = True
    p_map.add_run("Pawprints spread progressively further apart as Coco accelerates.\n")
    p_map.add_run("• Slowing Down: ").bold = True
    p_map.add_run("Pawprints bunch progressively closer together as Coco brakes.\n")
    p_map.add_run("• Stationary (At Rest): ").bold = True
    p_map.add_run("Pawprints cluster and stack vertically at the exact rest position.")
    
    add_heading_1(doc, "📝 Part 1: Mission Matching Reference Matrix")
    p_table_intro = doc.add_paragraph("Observe Coco's 10 kinematic missions in the interactive simulator. Record the motion parameters for each card below:")
    p_table_intro.paragraph_format.space_after = Pt(6)
    
    table = doc.add_table(rows=11, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["Card", "Graph Type", "Mission Story & Motion Description", "Initial Dir", "Kinematic State"]
    col_widths = [Inches(0.7), Inches(1.2), Inches(2.6), Inches(0.9), Inches(1.1)]
    
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], HEX_TEAL)
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(title)
        run.font.name = 'Arial'
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    matrix_data = [
        ("#1", "Position-Time", "The Backyard Dash: Starts from rest at x=10m, speeds up right (+a).", "+ Right", "Accelerating"),
        ("#2", "Velocity-Time", "The Sudden Treat Pause: Sprints left fast, smoothly decelerating to a stop.", "- Left", "Decelerating"),
        ("#3", "Position-Time", "The Boundary Patrol: Trots right steadily, then doubles speed right.", "+ Right", "Piecewise Const"),
        ("#4", "Velocity-Time", "The Squirrel Hesitation: Slows to rest moving right, pauses, bolts left.", "+ then -", "Multi-Stage"),
        ("#5", "Position-Time", "The Steady Sniff Tour: Trots left at const speed, stops to sniff, resumes left.", "- Left", "Uniform w/ Rest"),
        ("#6", "Position-Time", "The Rebound Arc: Runs right slowing down, peaks, turns around left smoothly.", "+ then -", "Continuous Turn"),
        ("#7", "Velocity-Time", "Launch & Glide: Accelerates from rest right, then cruises at const speed.", "+ Right", "Accel to Const"),
        ("#8", "Velocity-Time", "Leftward Zoomies: Launches from rest at right, accelerating steadily left (-a).", "- Left", "Accelerating"),
        ("#9", "Position-Time", "The Zig-Zag Search: Const speed right → turns const speed left → turns right.", "+ / - / +", "Piecewise 3-Stage"),
        ("#10", "Velocity-Time", "The Bell-Curve Trot: Accelerates right from rest → cruises → decelerates to rest.", "+ Right", "Trapezoidal")
    ]
    
    for row_idx, row_data in enumerate(matrix_data, start=1):
        row_cells = table.rows[row_idx].cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = col_widths[col_idx]
            if row_idx % 2 == 0:
                set_cell_background(row_cells[col_idx], "F8FAFC")
            set_cell_margins(row_cells[col_idx], top=70, bottom=70, left=90, right=90)
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.name = 'Arial'
            run.font.size = Pt(9)
            run.font.color.rgb = RGB_DARK
            if col_idx == 0:
                run.font.bold = True
                run.font.color.rgb = RGB_TEAL
                
    add_heading_1(doc, "🧠 Part 2: Conceptual & Graphical Analysis")
    questions = [
        ("1. Slope Interpretation:", "Compare Mission #1 (parabolic x-t curve) and Mission #3 (straight segmented x-t lines). What does a changing slope on a Position-Time graph physically indicate about Coco's speed?"),
        ("2. Direction Reversal Analysis:", "In Mission #6 (The Rebound Arc), Coco reverses direction without ever coming to an extended stop. Describe what the peak (vertex) of this Position-Time parabola represents in terms of velocity."),
        ("3. Velocity-Time vs. Position-Time Rest:", "In Mission #4 and Mission #5, Coco comes to a complete rest (v = 0). Explain how a period of rest is represented differently on a Position-Time graph versus a Velocity-Time graph.")
    ]
    
    for q_title, q_body in questions:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(8)
        p_q.paragraph_format.space_after = Pt(2)
        run_qt = p_q.add_run(q_title + " ")
        run_qt.font.name = 'Arial'
        run_qt.font.size = Pt(10)
        run_qt.font.bold = True
        run_qt.font.color.rgb = RGB_AMBER
        
        run_qb = p_q.add_run(q_body)
        run_qb.font.name = 'Arial'
        run_qb.font.size = Pt(9.5)
        run_qb.font.color.rgb = RGB_DARK
        
        p_box = doc.add_paragraph()
        p_box.paragraph_format.space_after = Pt(8)
        run_box = p_box.add_run("Answer:\n\n\n")
        run_box.font.name = 'Arial'
        run_box.font.size = Pt(9)
        run_box.font.color.rgb = RGB_MUTED

    doc.save(filepath)
    print(f"Generated Student Handout: {filepath}")

def generate_teacher_guide(filepath):
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)
        
    format_doc_header(doc, "Kinematics Studio: Coco's Motion Lab — Teacher Guide", "Complete Answer Key, Diagnostic Taxonomy & PER Lesson Plan")
    
    add_callout(doc, "📋 Pedagogical Scope & Objectives", [
        "This module features Coco the Black Pug to address core Physics Education Research (PER) kinematics targets:",
        "1. Slope-as-Rate: Reinforces that the tangent slope of x-t is instantaneous velocity, and the slope of v-t is acceleration.",
        "2. Sign of Vector Components: Disentangles negative position (location) from negative velocity (direction) and negative acceleration (net force direction).",
        "3. Pawprint Motion Map Alignment: Bridges concrete physical space with abstract graphical coordinate spaces."
    ])
    
    add_heading_1(doc, "🔑 Complete 10-Mission Answer Key & Misconception Breakdown")
    
    table = doc.add_table(rows=11, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["Mission", "Graph", "Exact Kinematic Motion Breakdown", "Targeted Student Misconception"]
    col_widths = [Inches(0.8), Inches(0.9), Inches(2.8), Inches(2.3)]
    
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], HEX_TEAL)
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(title)
        run.font.name = 'Arial'
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    ans_data = [
        ("#1", "x-t", "x₀=10m, v₀=0, a=+1.8 m/s² (3.2s). Parabolic curve opening up from center.", "Confusing starting at x=10 with having non-zero initial speed."),
        ("#2", "v-t", "v₀=-7.5 m/s, a=+2.5 m/s² (3.0s). Straight line sloping from negative axis up to v=0.", "Believing positive acceleration must always mean speeding up."),
        ("#3", "x-t", "v=+3 m/s (2s, x=9m) then v=+6 m/s (1.8s, x=19.8m). Two connected positive linear slopes.", "Missing that steeper positive slope corresponds to greater speed."),
        ("#4", "v-t", "v: +5 to 0 m/s (2s) → rest v=0 (1s) → accelerates 0 to -5.4 m/s (1.8s).", "Confusing the v=0 horizontal segment with 'at the origin x=0'."),
        ("#5", "x-t", "v=-4 m/s (1.8s) → rest plateau at x=10.8m (1.5s) → v=-4 m/s (1.8s).", "Thinking that a horizontal flat plateau on x-t means constant speed."),
        ("#6", "x-t", "v₀=+6 m/s, a=-2.4 m/s² (4s). Parabolic arch peaking at t=2.5s (v=0), reversing left.", "Mistaking an inverted parabolic arc for a physical hill."),
        ("#7", "v-t", "a=+4 m/s² from rest to v=6 m/s (1.5s) → horizontal cruise at v=6 m/s (2.2s).", "Confusing horizontal plateau on v-t (constant speed) with rest."),
        ("#8", "v-t", "x₀=16m, v₀=0, a=-2.2 m/s² (3.5s). Straight line sloping down into negative quadrant.", "Believing downward slope on v-t always means slowing down."),
        ("#9", "x-t", "Piecewise 3-stage: +4 m/s (1.5s) → -5 m/s (2s) → +3 m/s (2s). Zig-zag N-shape.", "Assuming sharp angle corners on x-t represent infinite speed."),
        ("#10", "v-t", "Trapezoid: ramp 0 to +4.5 m/s (1.5s) → flat plateau (1.2s) → ramp down to 0 (1.5s).", "Confusing symmetrical trapezoid on v-t with a triangular Position graph.")
    ]
    
    for row_idx, row_data in enumerate(ans_data, start=1):
        row_cells = table.rows[row_idx].cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].width = col_widths[col_idx]
            if row_idx % 2 == 0:
                set_cell_background(row_cells[col_idx], "F8FAFC")
            set_cell_margins(row_cells[col_idx], top=70, bottom=70, left=90, right=90)
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text)
            run.font.name = 'Arial'
            run.font.size = Pt(9)
            run.font.color.rgb = RGB_DARK
            if col_idx == 0:
                run.font.bold = True
                run.font.color.rgb = RGB_TEAL
            elif col_idx == 1:
                run.font.bold = True
                run.font.color.rgb = RGB_AMBER

    doc.save(filepath)
    print(f"Generated Teacher Guide: {filepath}")

if __name__ == "__main__":
    base_dir = "/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace"
    student_out = os.path.join(base_dir, "motion_simulation", "Graph_That_Motion_Student_Handout.docx")
    teacher_out = os.path.join(base_dir, "motion_simulation", "Graph_That_Motion_Teacher_Guide.docx")
    
    generate_student_handout(student_out)
    generate_teacher_guide(teacher_out)
