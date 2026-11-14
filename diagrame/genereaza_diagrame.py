import sys, html
OUT = sys.argv[1]
F = 'font-family="Segoe UI, Arial, Helvetica, sans-serif"'
INK = "#14211f"; MUT = "#55706b"; EDGE = "#2f5f5a"


def esc(s):
    return html.escape(s)


def text(x, y, lines, size=13, weight=400, fill=INK, anchor="middle"):
    lh = size * 1.25
    y0 = y - (len(lines) - 1) * lh / 2
    return "".join(
        f'<text x="{x}" y="{y0 + i * lh:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}" dominant-baseline="middle" {F}>{esc(l)}</text>'
        for i, l in enumerate(lines))


def label(x, y, s, size=11.5, fill=MUT, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'dominant-baseline="middle" paint-order="stroke" stroke="#ffffff" stroke-width="5" '
            f'stroke-linejoin="round" {F}>{esc(s)}</text>')


DEFS = f'''<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{EDGE}"/></marker>
<marker id="ao" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="{EDGE}" stroke-width="1.6"/></marker>
</defs>'''


def line(x1, y1, x2, y2, dash=False, arrow=None, w=1.4):
    d = ' stroke-dasharray="6 4"' if dash else ''
    m = f' marker-end="url(#{arrow})"' if arrow else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{EDGE}" stroke-width="{w}"{d}{m}/>'


def path(d, dash=False, arrow=None, w=1.4):
    ds = ' stroke-dasharray="6 4"' if dash else ''
    m = f' marker-end="url(#{arrow})"' if arrow else ''
    return f'<path d="{d}" fill="none" stroke="{EDGE}" stroke-width="{w}"{ds}{m}/>'


# ---------------- CAZURI DE UTILIZARE ----------------
W, H = 1260, 960
RX, RY = 108, 25
A, B = 330, 640
nodes = {}


def uc(key, cx, cy, lines, auto=False):
    nodes[key] = (cx, cy)
    fill = "#e6f4f2" if auto else "#ffffff"
    st = "#4f9e95" if auto else "#2f5f5a"
    da = ' stroke-dasharray="5 3"' if auto else ''
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="{fill}" stroke="{st}" stroke-width="1.5"{da}/>'
            + text(cx, cy, lines, 12.5))


def actor(x, y, name):
    return (f'<g stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round">'
            f'<circle cx="{x}" cy="{y - 36}" r="12" fill="#0d8fa3" stroke="#0d8fa3"/>'
            f'<line x1="{x}" y1="{y - 24}" x2="{x}" y2="{y + 8}"/>'
            f'<line x1="{x - 18}" y1="{y - 12}" x2="{x + 18}" y2="{y - 12}"/>'
            f'<line x1="{x}" y1="{y + 8}" x2="{x - 14}" y2="{y + 32}"/>'
            f'<line x1="{x}" y1="{y + 8}" x2="{x + 14}" y2="{y + 32}"/></g>'
            + text(x, y + 52, [name], 14, 700))


def ext(cx, cy, lines):
    return (f'<rect x="{cx - 75}" y="{cy - 28}" width="150" height="56" rx="10" fill="#f2c14e" stroke="#c99a2a" stroke-width="1.5"/>'
            + text(cx, cy, lines, 12.5, 600, "#2a1d00"))


shapes = []
shapes.append(uc("a_send", A, 130, ["Trimite un prompt sau", "un document la AI"]))
shapes.append(uc("a_local", A, 270, ["Continuă sarcina", "în AI-ul local"]))
shapes.append(uc("a_exc", A, 340, ["Cere o excepție"]))
shapes.append(uc("a_see", A, 410, ["Vede ce date", "au fost protejate"]))
shapes.append(uc("a_recv", A, 480, ["Primește răspunsul", "cu datele reale"]))
shapes.append(uc("b_int", B, 130, ["Interceptează cererea", "către domeniile AI"], True))
shapes.append(uc("b_det", B, 200, ["Detectează", "datele sensibile"], True))
shapes.append(uc("b_cls", B, 270, ["Clasifică: VERDE,", "GALBEN sau ROȘU"], True))
shapes.append(uc("b_hide", B, 340, ["Ascunde identitatea", "și scalează sumele"], True))
shapes.append(uc("b_block", B, 410, ["Blochează parolele", "și cheile"], True))
shapes.append(uc("b_rest", B, 480, ["Pune datele reale", "la loc în răspuns"], True))
ANT_ROWS = [600, 656, 712, 768, 824, 880]
ant = [("n_inst", ["Instalează agentul pe", "calculatoarele firmei"]),
       ("n_loc", ["Pornește AI-ul local", "în birou (Qwen)"]),
       ("n_pre", ["Alege presetul", "pentru domeniul firmei"]),
       ("n_cfg", ["Adaugă date sensibile", "pe categorii"]),
       ("n_apr", ["Aprobă excepțiile"]),
       ("n_rep", ["Întreabă asistentul AI", "despre date (MCP)"])]
for (k, lines), y in zip(ant, ANT_ROWS):
    shapes.append(uc(k, A, y, lines))

L = []
for k in ["a_send", "a_local", "a_exc", "a_see", "a_recv"]:
    x, y = nodes[k]
    L.append(line(122, 300, x - RX, y))
for k, _ in ant:
    x, y = nodes[k]
    L.append(line(122, 740, x - RX, y))
# include / extend
L.append(line(A + RX, 130, B - RX - 2, 130, True, "ao")); L.append(label((A + B) / 2, 118, "«include»"))
L.append(line(B, 155, B, 173, True, "ao")); L.append(label(B - 12, 164, "«include»", 11, anchor="end"))
L.append(line(B, 225, B, 243, True, "ao")); L.append(label(B - 12, 234, "«include»", 11, anchor="end"))
L.append(line(B, 315, B, 297, True, "ao")); L.append(label(B + 62, 306, "«extinde» GALBEN", 11, anchor="start"))
L.append(path(f"M{B + RX},410 C{B + RX + 40},410 {B + RX + 40},285 {B + RX - 6},280", True, "ao"))
L.append(label(B + RX + 34, 392, "«extinde»", 11, anchor="start")); L.append(label(B + RX + 34, 406, "parolă", 11, anchor="start"))
L.append(line(A + RX, 270, B - RX - 2, 270, True, "ao")); L.append(label((A + B) / 2, 258, "«extinde» ROȘU"))
L.append(line(A + RX - 10, 333, B - RX + 8, 282, True, "ao")); L.append(label((A + B) / 2 + 4, 318, "«extinde»"))
L.append(line(A + RX, 480, B - RX - 2, 480, True, "ao")); L.append(label((A + B) / 2, 468, "«include»"))
# sisteme externe
PUB = (1172, 340); LOC = (1172, 150)
JX = 905
shapes.append(uc("b_jev", JX, 340, ["Verifică textul", "curățat cu Jev"], True))
L.append(line(B + RX, 340, JX - RX - 2, 340, True, "ao")); L.append(label((B + RX + JX - RX) / 2, 326, "«include»", 10.5))
L.append(line(JX + RX, 340, PUB[0] - 77, 340, False, "ah")); L.append(label(1040, 326, "cerere curată", 11))
L.append(line(PUB[0] - 60, 370, B + RX - 6, 470, False, "ah")); L.append(label(985, 430, "răspuns"))
JEV = (1172, 540)
L.append(path(f"M{JX + 40},363 L{JEV[0] - 77},{JEV[1] - 8}", True, "ao")); L.append(label(1010, 470, "textul curățat", 11))
L.append(path(f"M{A + 60},247 L{A + 170},235 L1010,235 L{LOC[0] - 77},165", False, "ah")); L.append(label(890, 223, "textul rămâne în firmă"))
L.append(path(f"M{A + RX},658 C{A + RX + 140},620 {A + RX + 160},500 {B},{170}", True, None))  # placeholder removed below
L.pop()
# antreprenorul aprobă excepția
L.append(path(f"M{A - RX},824 C150,740 150,400 {A - RX + 2},345", True, "ao")); L.append(label(150, 560, "răspunde la", 11))
# AI-ul local pornit de antreprenor alimentează sistemul extern AI local
L.append(path(f"M{A + RX},656 L{LOC[0]},656 L{LOC[0]},{LOC[1] + 30}", True, "ao")); L.append(label(900, 644, "pornește"))

box = (f'<rect x="215" y="30" width="870" height="905" rx="18" fill="#fbfdfd" stroke="#9fbcb7" stroke-width="1.6"/>'
       + text(637, 56, ["Agentul instalat pe calculatoarele firmei"], 15, 700)
       + text(A, 92, ["Ce face angajatul"], 12, 600, MUT) + text(B, 92, ["Ce face agentul singur"], 12, 600, MUT)
       + '<line x1="235" y1="530" x2="1040" y2="530" stroke="#c9dad6" stroke-dasharray="4 4"/>'
       + text(A, 562, ["Ce face antreprenorul"], 12, 600, MUT))
act = actor(100, 300, "Angajat") + actor(100, 740, "Antreprenor")
exts = ext(*PUB, ["ChatGPT, Claude,", "Gemini, Copilot"]) + ext(*LOC, ["AI local", "Qwen3.5-9B"]) + ext(*JEV, ["Jev (TypeSafe)", "în cloud"])
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Diagrama cazurilor de utilizare">'
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>{DEFS}{box}{"".join(L)}{"".join(shapes)}{act}{exts}</svg>')
open(OUT + "/cazuri-de-utilizare.svg", "w", encoding="utf-8", newline="\n").write(svg)

# ---------------- FLUX DE DEZVOLTARE ----------------
W, H = 1120, 1330
CX = 380; BW = 440; BH = 58
L = []; S = []


def box(key, cy, lines, fill="#ffffff", stroke="#2f5f5a", fg=INK, cx=CX, w=BW, h=BH, dash=False, weight=500):
    nodes[key] = (cx, cy, w, h)
    da = ' stroke-dasharray="6 4"' if dash else ''
    S.append(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1.6"{da}/>'
             + text(cx, cy, lines, 13, weight, fg))


def dia(key, cy, lines, cx=CX, w=230, h=96):
    nodes[key] = (cx, cy, w, h)
    S.append(f'<polygon points="{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}" fill="#fff8e6" stroke="#c99a2a" stroke-width="1.6"/>'
             + text(cx, cy, lines, 12.5, 600))


def down(a, b, lab=None):
    x, ya, _, ha = nodes[a]
    _, yb, _, hb = nodes[b]
    L.append(line(x, ya + ha / 2, x, yb - hb / 2 - 2, False, "ah"))
    if lab:
        L.append(label(x + 14, (ya + ha / 2 + yb - hb / 2) / 2, lab, 12, EDGE, "start"))


G = "#6fd99a"; GS = "#3c9d66"
box("R", 50, ["0 · Research și design", "(gata)"], G, GS, weight=700)
box("V", 140, ["1 · Interviuri: angajați,", "antreprenori, mentori"])
dia("G1", 255, ["Pun oamenii date de", "clienți în AI? (H1)"])
box("PIV", 255, ["Revizuim segmentul", "sau problema"], "#fbe5e6", "#d9787d", cx=820, w=300)
box("F", 375, ["2 · Teste de fezabilitate", "T1 proxy local · T2 QUIC · T6 aplicații desktop"])
dia("G2", 490, ["Interceptarea merge", "fără să strice nimic?"])
box("EXT", 490, ["Plan B: extensie de browser", "în loc de proxy"], "#fbe5e6", "#d9787d", cx=820, w=300)
box("D", 610, ["3 · Detectare locală + verificare Jev pe textul curățat", "CNP, IBAN, CUI, nume, lista clienților, OCR (T4, T5, T11, T12)"])
box("PS", 700, ["4 · Ascundere și restaurare în răspuns", "(T3, T7)"])
box("POL", 790, ["5 · Preseturi pe domenii, categorii proprii,", "server MCP pentru antreprenor (T13, T14)"])
box("LOC", 880, ["6 · AI local: Qwen3.5-9B", "T8 calitate · T9 viteză · T10 transfer fără URL"])
box("DEMO", 970, ["7 · Demo la hackathon", "ChatGPT web, pachetul Contabil"], "#0d8fa3", "#0d8fa3", "#ffffff", weight=700)
box("PIL", 1060, ["8 · Pilot de o săptămână", "la 1–3 firme"])
dia("G3", 1170, ["Ce a ieșit", "din pilot?"], w=200, h=90)
box("NEXT", 1285, ["9 · Mai multe firme"], G, GS, weight=700)
box("JUR", 1015, ["În paralel: juridic", "informarea angajaților · DPIA ·", "confirmare de la un jurist", "(secretul profesional)"],
    "#f3e6ff", "#b989f0", cx=820, w=300, h=110, dash=True)
down("R", "V"); down("V", "G1"); down("G1", "F", "da"); down("F", "G2"); down("G2", "D", "da")
down("D", "PS"); down("PS", "POL"); down("POL", "LOC"); down("LOC", "DEMO"); down("DEMO", "PIL"); down("PIL", "G3"); down("G3", "NEXT", "merge")
L.append(line(CX + 115, 255, 820 - 152, 255, False, "ah")); L.append(label(CX + 150, 243, "nu", 12, EDGE))
L.append(path(f"M820,{255 - 29} L820,140 L{CX + BW / 2 + 2},140", False, "ah"))
L.append(line(CX + 115, 490, 820 - 152, 490, False, "ah")); L.append(label(CX + 150, 478, "nu", 12, EDGE))
L.append(path(f"M820,{490 + 29} L820,610 L{CX + BW / 2 + 2},610", False, "ah"))
L.append(path(f"M{CX - 100},1170 L110,1170 L110,610 L{CX - BW / 2 - 2},610", False, "ah"))
L.append(label(195, 1158, "date ratate sau alarme false", 12, EDGE))
L.append(path(f"M{CX - 60},1192 L{CX - 60},1215 L150,1215 L150,790 L{CX - BW / 2 - 2},790", False, "ah"))
L.append(label(235, 1228, "reguli greșite", 12, EDGE))
L.append(line(820 - 152, 995, CX + BW / 2 + 2, 975, True, "ao"))
L.append(line(820 - 152, 1040, CX + BW / 2 + 2, 1060, True, "ao"))
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Fluxul de dezvoltare al aplicației">'
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>{DEFS}{"".join(L)}{"".join(S)}</svg>')
open(OUT + "/flux-dezvoltare.svg", "w", encoding="utf-8", newline="\n").write(svg)
print("ok")
