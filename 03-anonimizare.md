# 03 · Anonimizarea: definiții, tehnici, limite

> **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** ipoteză · **[V]** de validat

## 1. Definiții juridice

| Concept | Ce spune legea | Consecință | Sursă |
|---|---|---|---|
| **Date personale** | Orice informație despre o persoană identificată sau identificabilă | Se aplică GDPR | [F] S17 |
| **Pseudonimizare** (art. 4(5) GDPR) | Datele nu mai pot fi atribuite unei persoane **fără informații suplimentare**, păstrate separat și protejate | **Rămân date personale** pentru cine are cheia | [F] S17, S19 |
| **Anonimizare** (considerentul 26) | Persoana nu mai e identificabilă cu „toate mijloacele” pe care e probabil, în mod rezonabil, să le folosească operatorul sau altcineva (costuri, timp, tehnologie) | GDPR **nu se mai aplică** | [F] S17 |
| **Relativitatea** (CJUE C-413/23 P, 04.09.2025) | Datele pseudonimizate pot fi **nepersonale pentru destinatarul** care nu are mijloace de reidentificare, dar rămân personale pentru operatorul care deține cheia | Contează cine primește datele și ce mijloace are | [F] S20 |
| **Ghidurile EDPB 02/2026** (proiect, consultare până la 30.10.2026) | Trei criterii: (1) **nicio înregistrare izolabilă**, (2) **nicio corelare** cu alt set de date, (3) **nicio deducție** semnificativă. Abordare *contextuală* (după capacitățile fiecărui destinatar) sau *simplificată* (mai strictă) | Deducțiile obținute **interogând modele AI** pot încălca criteriul „fără deducție” | [F] S21 |

**Ce înseamnă pentru noi [I]:** sistemul nostru GALBEN înlocuiește „Ion Popescu” cu `[PERSOANA_1]` și păstrează tabelul de corespondență pe dispozitivul firmei. Asta e **pseudonimizare**, nu anonimizare:

- **Pentru firmă** (care are cheia), datele rămân personale, deci GDPR se aplică în continuare.
- **Pentru furnizorul AI** (care nu are cheia), datele *pot* fi considerate nepersonale după SRB [F] S20, **dar numai dacă textul rămas nu permite reidentificarea prin context**. Ghidurile EDPB 02/2026 cer exact testul ăsta [F] S21.
- **Concluzie:** în prezentări spunem „pseudonimizare” (corect juridic), nu „anonimizare”. Un jurist din juriu ne-ar penaliza pentru confuzia dintre ele.

## 2. Tehnici: ce sunt, ce păstrează, cât sunt de reversibile

| Tehnică | Exemplu în română | Reversibilă? | Ce rămâne util pentru AI | Riscul rămas | Referință |
|---|---|---|---|---|---|
| **Eliminare** | „Clientul ███ datorează…” | Nu | Structura frazei | Contextul poate identifica persoana | Presidio `redact` [F] S25 |
| **Mascare parțială** | IBAN `RO49 AAAA ****** 1234`; CNP `1******123456` | Nu | Formatul | Fragmentele rămase + context. Pentru CNP, **primele 7 cifre dezvăluie sexul și data nașterii** [F] S40, deci ele trebuie mascate | Presidio `mask` [F] S25 |
| **Etichete reversibile** (pseudonime) | „`[PERSOANA_1]` din `[ORAS_1]` are de plătit `[SUMA_1]` către `[FIRMA_1]`” | **Da** (tabel local) | Relațiile dintre entități: AI-ul poate redacta e-mailul corect | Contextul liber; tabelul de corespondență e date personale și trebuie protejat | Tiparul gateway-urilor [F] S36; Presidio `encrypt`/`decrypt` [F] S25 |
| **Înlocuire cu valori fictive realiste** | „Ion Popescu” → „Mihai Ionescu”; CNP real → CNP fictiv cu cifră de control validă | Da (tabel local) | Textul arată natural, AI-ul nu „simte” lipsa | Fictivul poate coincide cu o persoană reală; AI-ul poate inventa detalii pe baza lui | [I] |
| **Generalizare** | „34 de ani, Sibiu” → „30–40 de ani, Regiunea Centru” | Nu | Tendințe, încadrări | Scade utilitatea pentru sarcini precise | WP29 [F] S18 |
| **Scalarea sumelor** | Toate sumele × 1,37 („125.000 lei” → „171.250 lei”), refăcute la întoarcere | Da (factor local) | Proporțiile și calculele relative | **Calculele neliniare se strică**: praguri fiscale, plafoane TVA, impozit progresiv, comparații cu sume fixe din lege | [I] |
| **Date sintetice** | Se generează un tabel cu aceeași structură și distribuție | Nu | Testarea formulelor sau a codului | Modelele de date sintetice pot memora valori reale; criteriul EDPB „fără deducție” [F] S21 | [I] |
| **Hash** | `sha256(CNP)` | Nu | Corelarea fără valoare | Spațiul CNP-urilor e mic, deci hash-ul se poate inversa prin forță brută [I] | Presidio `hash` [F] S25 |

## 3. Limitele: de ce „scoatem numele” nu ajunge

### 3.1 Reidentificarea prin combinații de date
- 87% din populația SUA e probabil unică după **cod poștal + sex + data nașterii** [F] S22.
- Cu 15 atribute demografice, 99,98% dintre americani ar fi reidentificați corect. E o estimare de model, nu un experiment pe oameni reali [F] S23.
- WP29: nicio tehnică singură nu acoperă individualizarea, corelarea și deducția [F] S18.

**Exemplu românesc [I]:** „pacientă de 34 de ani din comuna Săliște, cu scleroză laterală amiotrofică, internată în martie”. Fără nume și fără CNP, într-o comună mică persoana e aproape sigur unică.

### 3.2 Textul liber
Detectarea entităților (NER) găsește nume, CNP-uri și IBAN-uri. Nu prinde identificatorii indirecți: fapte unice, funcții („directorul financiar al singurei fabrici de ciment din județ”), date, relații [F] S24.
[I] Româna adaugă dificultăți: declinări („lui Popescu”, „Popeștii”), diacritice lipsă, nume care sunt și substantive comune (Lupu, Mihai, Rădăcină). **Calitatea NER pe română în texte de business: necunoscută**, trebuie testată pe date reale (de exemplu corpusul RONEC) [V].

### 3.3 Documente în care conținutul însuși e secretul
| Document | De ce nu ajută pseudonimizarea [I] |
|---|---|
| **Contract M&A / de cesiune** | Clauzele, prețul și structura tranzacției sunt informația secretă. Fără ele, AI-ul nu mai are ce analiza |
| **Cod sursă** | Logica de business și algoritmii *sunt* proprietatea intelectuală. Redenumirea variabilelor nu ascunde nimic |
| **Strategie de preț / ofertă la licitație** | Cifrele sunt secretul. Scalate, AI-ul nu poate judeca dacă oferta e competitivă |
| **Strategie procesuală** | Faptele cauzei identifică speța (mai ales dacă e publică în presă) |
| **Plan de restructurare / concedieri** | Informația („concediem 20% din vânzări în martie”) e sensibilă chiar și fără nume |

### 3.4 Restaurarea în răspuns: riscuri tehnice [I]
- AI-ul poate modifica etichetele („`[PERSOANA_1]`” → „Persoana 1”, „domnul `[PERSOANA_1]`”), iar restaurarea eșuează.
- AI-ul poate inventa entități noi pe care sistemul nu le recunoaște.
- La sumele scalate, AI-ul calculează pe valori false. Un procent (cota de TVA) aplicat pe o sumă scalată dă un rezultat corect după descalare. Comparația cu un **prag fix din lege** (plafonul de TVA, plafonul de microîntreprindere) dă însă o concluzie greșită.
- Fișierele încărcate (PDF, Excel, imagini scanate) cer OCR și parsare înainte de detectare.

## 4. Exemple concrete în română

**Exemplul 1: contabilitate (GALBEN, merge bine)**
> Original: „Scrie un e-mail către Ana Ionescu (CNP 2850312400123) că firma Alfa Construct SRL (CUI 12345678) are de plată 14.320 lei TVA până pe 25 noiembrie, din contul RO49BTRL0000000000001234.”
>
> Trimis la AI: „Scrie un e-mail către `[PERSOANA_1]` că firma `[FIRMA_1]` (CUI `[CUI_1]`) are de plată `[SUMA_1]` TVA până pe 25 noiembrie, din contul `[IBAN_1]`.”
>
> Răspunsul AI restaurat: e-mailul corect, cu datele reale reintroduse local.
>
> CNP-ul nu e necesar pentru sarcină. **Regulă de minimizare: se elimină, nu se pseudonimizează.**

**Exemplul 2: medical (ROȘU)**
> „Rezumă fișa: pacient 67 ani, Comuna X, diagnostic de mielom multiplu, a refuzat chimioterapia, fiica lucrează la primărie.”
>
> Numele lipsește, dar persoana e reidentificabilă prin context. Sunt date de sănătate (art. 9) sub secret medical, deci se blochează. Alternativa: un instrument aprobat de clinică, cu contract de prelucrare.

**Exemplul 3: avocatură (ROȘU)**
> „Clientul meu, acționarul majoritar al unei rețele de farmacii din Cluj, vrea să mute activele înainte de partaj. Ce variante are?”
>
> Nu conține niciun identificator direct. Secretul e conținutul însuși, iar faptele sunt unice. Pseudonimizarea nu ajută, deci se blochează.

**Exemplul 4: HR (GALBEN cu generalizare)**
> „Evaluează CV-ul lui Andrei Pop, 52 de ani, absolvent 1997…” → vârsta și anul absolvirii **se generalizează sau se elimină**. Sunt și un risc de discriminare, deci se elimină înainte de evaluare.

## 5. Concluzii pentru produs [I]
1. Juridic, GALBEN = **pseudonimizare cu cheie locală**. Așa trebuie numit.
2. GALBEN e sigur doar pentru **identificatori structurați** (CNP, IBAN, CUI, e-mail, telefon, număr de înmatriculare) și pentru **nume în texte scurte și generice**.
3. Textul liber lung cu fapte unice nu poate fi garantat. Fie îl bifăm „ROȘU dacă e incert”, fie acceptăm un risc rezidual documentat.
4. **Minimizarea bate pseudonimizarea:** ce nu trebuie pentru sarcină (CNP-ul într-un e-mail) se elimină de tot.
