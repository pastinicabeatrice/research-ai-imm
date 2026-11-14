# 06 · Soluția: propunerea de valoare și cum funcționează exact

> **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** ipoteză / decizie de design · **[V]** de validat (la interviuri sau prin test tehnic)
> Documentul e o specificație de produs, nu cod. Decizia de a intercepta traficul la nivel de rețea e a echipei. Mai jos e transformată în cerințe exacte, cu limitele ei.

## 1. Propoziția de valoare

### Varianta recomandată (formula „Ajutăm… să… prin…”), revizuită

Revizuită după [07-problema.md](07-problema.md): protejăm **cinci clase de date**, nu doar datele clienților.

> **Ajutăm** firmele de 1–100 de angajați care lucrează zilnic cu documente ce conțin date ale clienților, ale angajaților și cifrele firmei (facturi, balanțe, state de plată, fișe de pacient, contracte, oferte)
> **să** folosească ChatGPT, Claude, Gemini și Copilot pe aceste documente **fără ca datele clienților, ale angajaților și secretele financiare ale firmei să plece din firmă în formă identificabilă**,
> **prin** un agent instalat pe calculatoarele firmei care interceptează local ce se trimite către aplicațiile AI, ascunde identitatea persoanelor și a firmelor (și, la nevoie, scalează sumele), pune datele la loc în răspuns, blochează parolele și documentele care nu pot fi protejate și îi arată antreprenorului, în fiecare lună, ce a fost oprit la ieșire.

**Pe scurt, pentru slide:** *„AI pe documentele firmei, fără ca datele clienților și cifrele firmei să plece din firmă.”*

### De ce formularea asta, cuvânt cu cuvânt [I]
| Bucată | De ce e aleasă |
|---|---|
| „prelucrează zilnic documente cu date ale clienților” | Definește clientul după **ce face**, nu după domeniu. Testul de calificare la interviu e simplu: „ce documente cu date de clienți ați deschis ieri?” |
| „să folosească … pe aceste documente” | Valoarea e **câștigul** (AI pe munca reală), nu frica. Antreprenorul cumpără productivitate fără risc, nu un al doilea antivirus |
| „să plece din firmă în formă identificabilă” | Promisiune verificabilă și mai îngustă decât „datele sunt în siguranță”. Nu promitem anonimizare (vezi [03](03-anonimizare.md)). La cifrele firmei ascundem **a cui** sunt, nu cifrele însele (vezi [07 §4.3](07-problema.md)) |
| „interceptează local” | Diferența față de soluțiile cloud: nimic nu trece printr-un server al nostru [I] |
| „îi arată antreprenorului … ce a fost oprit” | **Valoarea percepută.** Fără raport, un produs care funcționează e invizibil. Raportul face protecția vizibilă |

### Variante alternative (de testat care rezonează) [V]
- **Unghiul vizibilitate:** „Ajutăm antreprenorii firmelor mici să **vadă** ce date ale clienților ajung în ChatGPT și să le oprească automat, prin…”
- **Unghiul conformitate:** „Ajutăm cabinetele de contabilitate, medicale și de avocatură să folosească AI-ul fără să încalce secretul profesional, prin…”

### Ce vede concret antreprenorul (valoarea percepută) [I]
Exemplu **fictiv** de raport lunar, ca să arătăm forma, nu cifre reale:

> **Octombrie · 14 calculatoare**
> 312 trimiteri către AI · 41 conțineau date de clienți · **toate protejate**
> Eliminate sau înlocuite: 58 CNP-uri · 23 IBAN-uri · 37 nume de clienți · 12 CUI-uri
> Blocate: 3 (2 fișe medicale scanate, 1 fișier cu parole)
> Angajații care au încercat cel mai des să trimită date: *(opțional, vezi §8)*

[V] Antreprenorii citesc un astfel de raport? Ce cifră îi interesează: numărul de trimiteri protejate sau numărul de blocări?

## 2. Fluxul exact, pas cu pas

### 2.1 Un prompt text în ChatGPT (cazul de bază)
1. Angajatul scrie în ChatGPT (în browser): *„Scrie-i Anei Ionescu, CNP 2850312400123, că firma Alfa Construct SRL are de plată 14.320 lei din contul RO49BTRL…”*
2. Browserul trimite cererea HTTPS. **Proxy-ul local** de pe calculator o primește, pentru că domeniul e pe lista AI (§4).
3. Proxy-ul decriptează cererea cu un certificat emis de **autoritatea de certificare locală** a dispozitivului (§3.2) și extrage textul promptului din corpul cererii.
4. **Motorul de detectare** (local) găsește: nume persoană, CNP, nume firmă, sumă, IBAN.
5. **Motorul de politică** aplică regulile categoriilor (§5):
   - CNP → **eliminat** (nu e necesar pentru sarcină);
   - nume → înlocuit cu „Maria Dobre”;
   - firma → „Beta Instal SRL”;
   - IBAN → IBAN fictiv valid;
   - suma → păstrată sau înlocuită, după configurarea firmei.
6. Corespondențele (real ↔ fictiv) se scriu în **seiful local** criptat, legat de conversație.
7. Cererea modificată pleacă la OpenAI. **Datele reale nu ies de pe calculator.**
8. Răspunsul vine în flux (bucată cu bucată). Proxy-ul îl **ține în buffer** până are cuvinte întregi, înlocuiește valorile fictive cu cele reale și îl trimite browserului.
9. Angajatul vede răspunsul cu numele real. O bulină arată *„3 date protejate”*, iar la click se vede ce a fost înlocuit.
10. Se scrie un eveniment de jurnal: **doar metadate** (oră, aplicație, categorii, acțiune), **fără text**.

### 2.2 Un document încărcat („hârtiile”)
Aici e cel mai mare risc tehnic. Fișierele binare (PDF, imagine, Excel) nu se pot modifica sigur „pe loc” [I].

| Tip fișier | Ce face agentul | De ce |
|---|---|---|
| PDF cu text, Word, Excel, CSV | Extrage textul local → detectare → **trimite textul pseudonimizat în locul fișierului**, cu confirmarea angajatului | Păstrează relațiile dintre date (utilitate) și nu lasă fișierul original să plece |
| PDF scanat, poză (JPG/PNG), poză de pe telefon | **OCR local** (pentru română) → același flux. Dacă OCR-ul are încredere scăzută → **ROȘU** | Un OCR ratat înseamnă o scurgere: în caz de îndoială, blocăm |
| Fișier cu categorii ROȘU (diagnostic, act de identitate, cod sursă) | Blocat, cu explicație și alternativă | Vezi [04](04-matrice-decizie.md) |
| Fișier mare (sute de rânduri de clienți) | ROȘU implicit; GALBEN doar dacă toate coloanele sunt recunoscute | O coloană ratată = scurgere în masă |

[V] Cum încarcă angajații documentele azi: drag-and-drop, copy-paste sau poză? Asta decide unde investim (OCR vs. extragere de text).

## 3. Arhitectura

### 3.1 Componente
| # | Componentă | Unde rulează | Ce face |
|---|---|---|---|
| 1 | **Agent** (serviciu de sistem) | Fiecare calculator Windows/macOS al firmei | Pornește proxy-ul, aplică politica, ține seiful, trimite metadate la consolă |
| 2 | **Proxy HTTPS local** | `127.0.0.1` pe calculator | Interceptează **doar** domeniile AI de pe listă; restul traficului trece neatins, necriptat de noi |
| 3 | **Autoritate de certificare locală** | Generată pe fiecare calculator la instalare, cheia privată nu iese de pe calculator | Permite decriptarea traficului către AI. Instalarea ei cere acordul administratorului |
| 4 | **Motor de detectare** | Local | Straturi: (a) tipare + cifră de control, (b) liste (clienții firmei, nume românești), (c) model NER local pentru nume și adrese, (d) cuvinte de context („diagnostic”, „parolă”) |
| 5 | **Motor de politică** | Local | Categorie × acțiune × segment → VERDE / GALBEN / ROȘU |
| 6 | **Seif de corespondențe** | Local, criptat | Real ↔ fictiv, pe conversație; se șterge după un termen configurabil |
| 7 | **Restaurare în flux** | În proxy | Pune la loc valorile reale în răspunsul primit bucată cu bucată |
| 8 | **Interfața angajatului** | Pictogramă în bara de sistem + notificări | Arată ce s-a protejat, de ce s-a blocat, cere excepții |
| 9 | **Consola antreprenorului** | Web; metadatele stau în cloud **sau** pe un calculator al firmei [V] | Categorii configurabile, raport lunar, aprobarea excepțiilor |
| 10 | **Cutie de rețea** (opțional) | Router sau mini-PC în birou | Blochează domeniile AI pentru dispozitivele **fără** agent (telefoane, oaspeți) prin DNS. Nu decriptează nimic |

### 3.2 De ce pe dispozitiv, nu doar la nivel de rețea
Ideea echipei („legare de rețea, interceptezi și rulezi local”) se poate face în două locuri. Recomandarea: **agent pe dispozitiv + cutie de rețea doar pentru blocare** [I].

| Criteriu | A. Agent pe fiecare calculator | B. Gateway în rețeaua biroului |
|---|---|---|
| Laptopul acasă sau pe 4G | ✅ protejat | ❌ iese din rețea, deci neprotejat |
| Telefoane personale | ❌ | ⚠️ doar blocare; decriptarea cere certificatul instalat pe telefon, iar telefoanele personale nu-l vor avea |
| Certificatul de decriptare | Câte unul pe dispozitiv, cheia rămâne local | Unul central: dacă e compromis, tot traficul AI al firmei e expus |
| Datele reale stau | Pe calculatorul angajatului | Pe gateway (un punct central de atac) |
| Instalare la o firmă cu 3 oameni, fără IT | Installer + 1 acord de administrator | Hardware nou și configurarea routerului |
| Cine răspunde dacă se strică | Un calculator | Tot biroul rămâne fără internet către AI |

### 3.3 Cerințe tehnice obligatorii (din documentația existentă)
- **QUIC / HTTP/3 trebuie blocat sau ocolit.** Chrome nu folosește QUIC cu certificate emise de o rădăcină care nu e publică, iar furnizorii de inspecție TLS recomandă blocarea QUIC, cu revenire automată pe TCP [F] S45 S46. Altfel o parte din trafic ocolește proxy-ul.
- **Decriptăm doar lista de domenii AI.** Băncile, e-mailul și site-urile medicale rămân netinse [I]. Asta reduce riscul juridic (monitorizarea angajaților) și riscul de a strica alte aplicații.
- **Aplicațiile cu „certificate pinning”** (acceptă doar certificatul lor) nu pot fi interceptate. Pentru ele, politica e: blocare la nivel de domeniu sau aplicație. [V] Test pe aplicația desktop ChatGPT, pe Claude desktop și pe Copilot din Windows.

## 4. Ce interceptăm (lista de pornire) [V]
Formatul exact al cererilor fiecărei aplicații **trebuie descoperit prin test** și se schimbă fără anunț. E costul de întreținere numărul 1 [I].

| Aplicație | Domenii (de confirmat prin captură de trafic) | Ce extragem |
|---|---|---|
| ChatGPT (web) | `chatgpt.com`, `*.oaiusercontent.com` (fișiere) | Textul mesajului, fișierele încărcate |
| Claude (web) | `claude.ai` | Textul mesajului, atașamentele |
| Gemini (web) | `gemini.google.com` | Textul mesajului, fișierele |
| Copilot (web) | `copilot.microsoft.com` | Textul mesajului |
| DeepSeek, Perplexity, Mistral | domeniile lor | Textul mesajului |
| API-uri (dezvoltatori) | `api.openai.com`, `api.anthropic.com`, `generativelanguage.googleapis.com` | Corpul JSON |
| **Necunoscute** | orice domeniu nou de AI | Blocare implicită până e adăugat în listă [I] |

## 5. Categoriile de entități configurabile

### 5.1 Ce înseamnă o categorie (structura exactă)
Fiecare categorie are aceleași câmpuri, editabile din consolă:

| Câmp | Valori posibile | Exemplu (CNP) |
|---|---|---|
| **Nume** | text | „CNP” |
| **Detector** | tipar + cifră de control · listă · model NER · cuvinte-cheie · combinație | 13 cifre + validarea cifrei de control |
| **Context care crește încrederea** | cuvinte din apropiere | „CNP”, „cod numeric”, „născut” |
| **Acțiune** | Permite · Pseudonimizează · Elimină · Blochează (ROȘU) | Elimină |
| **Tip de înlocuire** | valoare fictivă realistă · etichetă `[CNP_1]` · mascare · generalizare | — |
| **Prag de încredere** | sub prag → acțiunea mai strictă | 0,9 |
| **Excepții** | valori permise, aplicații permise | CNP-ul firmei (PFA) |
| **Aplicat pe** | toți / grupuri de angajați | toți |

### 5.2 Categoriile implicite
| Categorie | Detector | Acțiune implicită | Sursa detectorului |
|---|---|---|---|
| CNP | 13 cifre, structura S AA LL ZZ JJ NNN C + cifra de control | Elimină | [F] S40 |
| IBAN | `RO` + 22 caractere, validare mod 97 | Pseudonimizează (IBAN fictiv valid) | [F] S43 |
| CUI / CIF | 2–10 cifre + cifra de control (cheia 753217532) + context („CUI”, „CIF”, „RO”) | Pseudonimizează | [F] S44 (algoritmul **de verificat** pe cod de referință) |
| Serie și număr CI | 2 litere + 6 cifre + context | Elimină | [I] |
| E-mail | tipar | Pseudonimizează | [I] |
| Telefon RO | `+40` / `07xx` + 8 cifre | Pseudonimizează | [I] |
| Număr de înmatriculare | `B 123 ABC`, `CJ 12 ABC` | Pseudonimizează | [I] |
| Nume de persoane | model NER + listă de prenume și nume românești | Pseudonimizează (nume fictiv de același gen) | [V] calitate necunoscută |
| Adresă | NER + cuvinte („str.”, „bl.”, „ap.”) | Generalizează (doar orașul) | [I] |
| Sume | tipar + monedă | Permite (implicit) / **Scalează** cu factor secret pentru cifrele firmei (configurabil); nu scalează când promptul pomenește praguri legale | [I], vezi [07 §4.3](07-problema.md) |
| Numele și CUI-ul firmei proprii | listă (setată la instalare) | Pseudonimizează | [I] |
| Furnizori, produse, proiecte interne | listă importată de antreprenor | Pseudonimizează / Blochează | [I] |
| Date de sănătate | dicționar de diagnostice + cuvinte („diagnostic”, „tratament”) | **Blochează** | [I] |
| Secrete tehnice | chei API, parole, tokenuri (tipare + entropie) | **Blochează** | [I] |
| Cod sursă | detectarea limbajului de programare | Blochează (firme IT) / Permite (alții) | [I] |

### 5.3 Categoriile proprii firmei (aici e valoarea configurabilă)
- **Lista clienților:** importată din CSV sau din programul de contabilitate. Fiecare nume de client devine o entitate de pseudonimizat, inclusiv în forme declinate [I]. **Detectează ce NER-ul ratează**, pentru că firma își știe clienții.
- **Termeni interni:** coduri de proiect, nume de produse nelansate, nume de cod → Blochează.
- **Cuvinte-cheie de segment:** „dosar penal”, „partaj” (avocatură), „HIV”, „psihiatric” (medical) → Blochează.

### 5.4 Pachete de pornire pe segmente [I]
| Pachet | Ce schimbă față de implicit |
|---|---|
| **Contabil** | Sume = Permite; CUI = Pseudonimizează; termenii AML („tranzacție suspectă”, „ONPCSB”) = Blochează |
| **Medical** | Orice termen medical lângă un nume, o dată de naștere sau o localitate = Blochează; programările = Pseudonimizează |
| **Juridic** | Numele părților = Pseudonimizează; „strategie”, „partaj”, „penal” = Blochează; contractele încărcate = ROȘU |
| **General** | Doar categoriile implicite |

## 6. Restaurarea în răspuns: decizia de format [I]
| Opțiune | Avantaj | Dezavantaj |
|---|---|---|
| Etichete `[PERSOANA_1]` | Restaurare sigură, ușor de găsit | AI-ul le reformulează („Persoana 1”), iar textul arată artificial |
| **Valori fictive realiste** („Maria Dobre”) | AI-ul le tratează normal; răspunsul sună firesc | Valoarea fictivă trebuie să fie unică în conversație și să nu apară deja în text |

**Recomandare:** valori fictive realiste, consecvente pe toată conversația, și etichete ca rezervă când nu există un generator pentru categorie.
**Cerințe:** buffer pe fluxul de răspuns până la granița de cuvânt; potrivire tolerantă la declinări („Mariei Dobre” → „Anei Ionescu”) [V].

## 7. Ce NU face soluția (spus deschis la pitch)
1. **Nu protejează telefoanele personale.** Le poate doar bloca în rețeaua biroului (cutia de rețea).
2. **Nu protejează aplicațiile care refuză interceptarea** (certificate pinning). Acolo doar blocare.
3. **Nu garantează anonimizarea.** Textul liber cu fapte unice poate reidentifica o persoană (vezi [03 §3](03-anonimizare.md)). Promitem doar că **datele identificatoare detectate** nu pleacă.
4. **Nu face un document secret „sigur de trimis”.** Contractele negociate, strategiile și codul sursă rămân ROȘU.
5. **Nu înlocuiește abonamentul AI de business.** E complementar: abonamentul rezolvă antrenarea pe date, noi rezolvăm ce date pleacă.

## 8. Riscuri juridice ale soluției însăși [I] [V]
- Decriptarea traficului angajaților = **monitorizare la locul de muncă**, deci intră sub GDPR art. 88 și regulile din dreptul muncii. Probabil e nevoie de: informarea scrisă a angajaților, o evaluare de impact (DPIA), proporționalitate. **De verificat cu un jurist.**
- **Proporționalitate prin design:** decriptăm doar domeniile AI; textul nu pleacă de pe calculator; raportul antreprenorului e **pe categorii**, nu pe persoane (raportul pe persoane e opțional și dezactivat implicit).
- Seiful local conține date reale. Dacă laptopul e furat, e protejat de criptare și de termenul de ștergere.

## 9. Testele tehnice care decid fezabilitatea (înainte de orice pitch)
| # | Test | Criteriu de trecere | Ipoteza testată |
|---|---|---|---|
| T1 | Proxy local + certificat local, ChatGPT web în Chrome și Edge | Promptul e citit și modificat; site-ul funcționează normal 30 de minute | Fezabilitatea de bază |
| T2 | QUIC blocat | Zero cereri către chatgpt.com ocolesc proxy-ul (verificat cu captură de trafic) | §3.3 |
| T3 | Restaurare în flux | 20 de prompturi reale (fictivizate): răspunsul are datele reale la locul lor în ≥ 19 cazuri | §6 |
| T4 | Detectare pe română | Set de 100 de texte fictive cu CNP, IBAN, CUI, nume declinate: CNP/IBAN/CUI ≈ 100%; se măsoară câte nume sunt ratate | H3 |
| T5 | OCR pe un document scanat românesc (factură, fișă) | Toate CNP-urile și IBAN-urile găsite | §2.2 |
| T6 | Aplicațiile desktop (ChatGPT, Claude, Copilot) | Interceptabile sau nu (pinning) | §3.3 |
| T7 | Latență | Întârziere adăugată < 1 s pe un prompt obișnuit, pe un laptop de birou modest | Experiența angajatului |

Pragurile din tabel sunt propunerile noastre [I], nu standarde.

## 10. Demo-ul minim pentru hackathon [I]
Un singur calculator, Chrome, ChatGPT web, pachetul **Contabil**:
1. Lipim un e-mail cu CNP, IBAN, CUI și numele unui client: arătăm ce pleacă efectiv (captură de trafic) vs. ce vede angajatul.
2. Încărcăm un PDF de factură: se trimite textul pseudonimizat, nu fișierul.
3. Lipim o fișă medicală: ROȘU, cu explicație.
4. Arătăm raportul lunar și ecranul de categorii, unde adăugăm pe loc un client nou în listă.

## 11b. ROȘU nu mai e un capăt de drum: redirecționarea către un AI local

### Ideea
Datele care **nu pot pleca** într-un AI public (fișe medicale, contracte negociate, oferte, strategii, cod sursă) nu mai sunt doar blocate. Angajatul primește un buton **„Deschide în AI-ul local”**, iar sarcina se face pe un model (Qwen, Llama) care rulează **pe calculator sau pe un server din birou**. Datele nu ies din firmă.

Asta rezolvă două probleme din critica de până acum [I]:
1. **Paradoxul segmentelor:** avocații și medicii, unde durerea e cea mai mare, primesc acum valoare, nu doar blocări.
2. **Ocolirea pe telefon:** dacă blocarea are o alternativă care funcționează, angajatul are mai puține motive să ia telefonul personal [V].

### Noua regulă ROȘU
| Clasa de date | Înainte | Acum |
|---|---|---|
| Sănătate, contracte negociate, strategii, oferte, cod sursă (A, B, D) | Blocat | **Redirecționat către AI-ul local** (dacă firma îl are); altfel blocat |
| Parole, chei, token SPV (E) | Blocat | **Tot blocat**: nicio sarcină nu are nevoie de ele, nici local |
| Excepții motivate | Aprobare de la antreprenor | La fel |

### Fluxul exact
1. Angajatul trimite în ChatGPT o fișă medicală. Agentul o clasifică ROȘU.
2. În locul trimiterii, pe pagină apare un mesaj: *„Textul conține date de sănătate despre un pacient. Nu poate pleca în ChatGPT.”* Butoane: **Deschide în AI-ul local** · Editează textul · Cere o excepție.
3. La „Deschide în AI-ul local”, agentul deschide un tab nou cu interfața AI-ului local, **cu textul și atașamentele deja încărcate**.
   - **Textul se transferă prin agentul local** (în memoria calculatorului), **niciodată prin adresa paginii (URL)**. Altfel datele ar ajunge în istoricul browserului și în jurnale [I].
4. Tabul are un marcaj vizibil: **„AI local · datele nu părăsesc firma”**, ca angajatul să știe unde lucrează.
5. Răspunsul rămâne local. Istoricul conversațiilor e criptat pe disc și se șterge după un termen configurabil.
6. În raportul antreprenorului apare categoria: *„3 sarcini mutate în AI-ul local”*.

### Unde rulează modelul: două variante
| Criteriu | A. Pe calculatorul angajatului | B. „AI-ul biroului”: un server în rețeaua locală |
|---|---|---|
| Pentru cine | Microfirme cu 1–5 oameni și laptopuri bune | Firme de 5–100 de oameni |
| Hardware | Recomandat ≥ 16 GB RAM pentru modele de 7–8B cuantizate [F] S48 | Un calculator cu placă video, folosit de toată firma [I] |
| Viteză | Pe procesor (fără placă video): în jur de 4–10 token-uri (bucăți de cuvânt) pe secundă la 7–8B, deci un răspuns lung durează zeci de secunde [F] S48 (bloguri, nu teste controlate) | Mult mai rapidă cu placă video [F] S48 |
| Datele | Nu ies de pe calculator | Nu ies din rețeaua firmei; serverul trebuie protejat (acces doar din birou, autentificare) [I] |
| Costul hardware-ului | Zero dacă laptopul e bun | **Necunoscut**: de aflat (preț de mini-PC sau server cu placă video) |

**Recomandare [I]:** varianta B pentru firmele de 5–100 de oameni; varianta A ca rezervă pentru microfirme. Omul de IT extern instalează serverul, ceea ce se potrivește cu canalul de distribuție.

### Ce modele
| Model | Licență | Limba română | Sursă |
|---|---|---|---|
| **Qwen3** (familia) | Apache 2.0 pentru multe modele; **de verificat pe fișa fiecărui model** | Multilingv (119 limbi, după comparații); calitatea pe română **necunoscută** | [F] S49 |
| **Llama 3.1 / 3.2** | Llama Community License: liber pentru firme mici; licență separată doar peste 700 de milioane de utilizatori lunari | Bun pe engleză; română **de testat** | [F] S49 |
| **OpenLLM-Ro** (RoLlama3.1, RoGemma2, RoMistral) | Moștenită de la modelul de bază, **de verificat** | Antrenate special pentru română | [F] S50 |

### Limitele, spuse deschis
- **Modelele locale mici sunt mai slabe** decât ChatGPT sau Claude: rezumă și redactează decent, dar pot inventa articole de lege sau detalii medicale. Interfața trebuie să spună asta [I].
- **Pe calculatoare fără placă video sunt lente.** Un angajat care așteaptă 40 de secunde s-ar putea întoarce la telefon [V].
- **Documentele lungi** (un contract de 30 de pagini) pot depăși memoria de context a unui model mic [I].
- **Juridic:** prelucrarea rămâne în firmă, deci nu mai există un terț căruia să i se divulge datele. Probabil asta rezolvă problema secretului profesional, **dar trebuie confirmat cu un jurist** [V]. GDPR se aplică în continuare (scop, securitate, păstrare).

### Teste noi
| # | Test | Criteriu de trecere [I] |
|---|---|---|
| T8 | Calitate pe română: 10 sarcini ROȘU fictivizate (rezumat de fișă, rezumat de contract, e-mail către pacient) cu Qwen3, Llama 3.1 și RoLlama3.1 | Un profesionist din domeniu acceptă cel puțin 7 din 10 răspunsuri fără corecturi mari |
| T9 | Viteză pe un laptop de birou tipic (16 GB RAM, fără placă video) și pe un mini-PC cu placă video | Primul cuvânt apare în < 3 s; un răspuns de o pagină în < 30 s |
| T10 | Transferul textului din ChatGPT în tabul local | Textul ajunge complet; nu apare în URL, în istoricul browserului sau în jurnale |

### Propunerea de valoare, completată
> … blochează parolele, **mută documentele care nu pot pleca într-un AI care rulează în firmă** și îi arată antreprenorului, în fiecare lună, ce a fost oprit sau mutat.

## 11. Întrebări noi pentru interviuri (Mom Test, pe ton natural)
- „Hai să luăm ziua de ieri. Ce ați avut de lucru pe calculator care avea și date de clienți? Ce ați făcut cu el?” (calificare)
- „Ultima dată când ați vrut să folosiți AI-ul pe ceva de-al unui client, ce ați făcut până la urmă? L-ați pus așa, l-ați rescris sau ați renunțat?”
- (antreprenor) „Vă vine acum vreun raport despre calculatoarele firmei? Pe care l-ați citit ultima dată?”
- (IT) „Ați pus vreodată certificate pe calculatoarele clienților, pentru filtrare sau antivirus? Ce s-a stricat?”
- (IT) „Ce calculatoare au de obicei clienții voștri? Câtă memorie, au placă video? Are vreunul server în birou?” (fezabilitatea AI-ului local)
- (angajat) „A fost vreo dată când n-ați putut folosi AI-ul pe un document? Cum ați terminat treaba? Cât v-a luat?” (valoarea AI-ului local)
- (antreprenor) „Ați cumpărat vreodată ceva doar ca datele să rămână la voi în birou, un server sau un hard extern? Ce v-a convins?” (disponibilitatea de a investi în varianta B)
