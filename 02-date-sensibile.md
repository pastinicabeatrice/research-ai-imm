# 02 · Datele sensibile pe segmente și baza lor legală

> **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** ipoteză · **[V]** de validat

## 1. Cele patru regimuri juridice care se suprapun

| Regim | Ce protejează | Consecința unei scurgeri în AI public | Sursă |
|---|---|---|---|
| **GDPR, date personale obișnuite** | Orice informație despre o persoană identificată sau identificabilă | Trimiterea către un furnizor AI fără contract de prelucrare (art. 28) și fără temei legal = prelucrare nelegală. Amenzile ANSPDCP pentru firme mici sunt de ordinul miilor de euro | [F] S17, S39 |
| **GDPR art. 9, categorii speciale** | Sănătate, origine etnică, opinii politice, religie, sindicat, date genetice și biometrice, viață sexuală | Interzise în principiu, cu excepții limitate | [F] S17 (art. 9, citit prin copie) |
| **GDPR art. 10 + Legea 190/2018 art. 4** | Date penale; CNP | Garanții suplimentare obligatorii pentru CNP (minimizare, securitate) | [F] S13 |
| **Secret profesional** (avocat, medic, expert contabil) | **Tot ce a aflat profesionistul**, inclusiv informații care nu sunt date personale (strategie, sume, fapte) | Disciplinar + penal (Cod penal art. 227: 3 luni–3 ani sau amendă, la plângerea victimei; Legea 51/1995 pentru avocați) | [F] S7, S8, S10, S11, S14 |
| **Secret comercial** | Informații cu valoare economică protejate prin „măsuri rezonabile” | Dacă firma nu ia măsuri rezonabile, informația poate pierde protecția legală | [F] S15 |

**Observația cheie [I]:** secretul profesional e **mai larg** decât GDPR. Pentru un avocat, ideea că „clientul X vrea să-și vândă firma înainte de divorț” e secretă chiar dacă scoatem numele. Anonimizarea satisface GDPR (uneori), dar **nu** satisface automat secretul profesional.

Secretul comercial are o consecință surprinzătoare: legea cere „măsuri rezonabile” [F] S15. [I] Un instrument care împiedică scurgerea în AI poate deveni chiar dovada acestor măsuri. Aici avem un argument de vânzare, dar trebuie validat cu un jurist [V].

## 2. Ce se întâmplă juridic când angajatul lipește date de client în ChatGPT

1. **Cont personal gratuit sau Plus:** datele pot fi folosite la antrenare implicit [F] S26. La Claude consumer se pot păstra până la 5 ani dacă utilizatorul acceptă antrenarea [F] S27. La Gemini cu cont personal, conversațiile pot fi citite de evaluatori umani [F] S28.
2. **Cont business (ChatGPT Business, Claude for Work, Workspace):** nu se antrenează implicit [F] S26 S27 S28. [I] Probabil există un contract de prelucrare (DPA), deci firma are un împuternicit în sensul art. 28. **De verificat** pentru fiecare plan.
3. **Transfer în SUA:** e posibil prin cadrul UE–SUA de confidențialitate (DPF), menținut de Tribunalul UE în 09.2025, cu recurs posibil [F] S41.
4. **Secretul profesional:** [I] chiar și cu DPA, cine îi dă voie avocatului sau medicului să divulge unui terț? Codul CMR art. 31 spune că secretul e „opozabil terților” cu excepțiile din lege [F] S11. Art. 36 *permite* AI-ul „cu respectarea prevederilor legale” [F] S11. **Neclar**, de întrebat un jurist sau mentorii [V].

[I] **Consecință pentru produs:** pentru firmele cu cont business, riscul de antrenare dispare, dar riscul de secret profesional și cel de minimizare (art. 5 GDPR) rămân. Pentru conturile personale, toate riscurile rămân.

## 3. Date sensibile pe segmente

Legendă pentru coloana „Niciodată în AI public”: **DA** = n-ar trebui să ajungă acolo nici anonimizat; **ANON** = poate ajunge doar pseudonimizat/anonimizat.

### Contabilitate
| Dată | Bază legală | Niciodată în AI public? |
|---|---|---|
| CNP angajați și clienți persoane fizice | GDPR + Legea 190/2018 art. 4 [F] S13 | ANON (CNP-ul trădează sexul, data nașterii și județul [F] S40) |
| Salarii individuale, state de plată | GDPR + confidențialitate OG 65/1994 [F] S9 | ANON (scalare/etichete) |
| IBAN, CUI, denumiri de clienți | GDPR (IBAN-ul persoanelor fizice); confidențialitate | ANON |
| Situația fiscală a unui client identificabil (datorii, controale ANAF) | Confidențialitate OG 65/1994 [F] S9 | ANON doar dacă suma și contextul nu identifică clientul [I] |
| Rapoarte de tranzacții suspecte (AML) | Legea 129/2019 [F] S12; interdicția de a informa clientul („tipping-off”) **de verificat** | **DA** |
| Parole SPV / ANAF, certificate digitale | Securitate (GDPR art. 32) | **DA** |

### Avocatură
| Dată | Bază legală | Niciodată? |
|---|---|---|
| Identitatea clientului și a părților | Secret profesional [F] S7 + GDPR | ANON |
| Strategia procesuală, opinia juridică pe un caz concret | Secret profesional absolut [F] S7 | **DA**, dacă faptele sunt unice și recognoscibile [I] |
| Date penale ale clientului | GDPR art. 10 + secret | **DA** |
| Contract cu clauze negociate (M&A, tranzacții) | Secret profesional + secret comercial al clientului | **DA** pentru conținut; ANON pentru clauzele-tip [I] |
| Corespondența avocat–client | Inviolabilă (Legea 51/1995 art. 35) [F] S7 | **DA** |

### Clinici și cabinete medicale
| Dată | Bază legală | Niciodată? |
|---|---|---|
| Diagnostic + identitate (nume, CNP, telefon) | GDPR art. 9 + Legea 46/2003 art. 21 [F] S10 + CMR art. 30 [F] S11 | **DA** împreună; ANON separat |
| Fișa clinică / scrisoarea medicală cu boală rară, localitate mică și vârstă | Art. 9 + risc mare de reidentificare [F] S22 S23 | **DA** (reidentificabilă după context) [I] |
| Imagini medicale (radiografii, fotografii) | Art. 9; o clinică stomatologică a fost amendată pentru radiografii postate online [F] S39 | **DA** |
| Date genetice, HIV, psihiatrie | Art. 9 | **DA** |
| Programări (nume + oră), fără diagnostic | GDPR | ANON |

### Brokeri de asigurări
| Dată | Bază legală | Niciodată? |
|---|---|---|
| Chestionare medicale (asigurări de viață/sănătate) | GDPR art. 9 | **DA** |
| CNP, serie de șasiu, număr de înmatriculare, adresă | GDPR | ANON |
| Istoric de daune, sume | GDPR + confidențialitate (Legea 236/2018, **de verificat**) [F] S16 | ANON |

### Agenții imobiliare
| Dată | Bază legală | Niciodată? |
|---|---|---|
| Copie CI, CNP, stare civilă | GDPR + Legea 190/2018 | **DA** pentru copiile actelor; ANON pentru câmpuri |
| Prețul minim acceptat de vânzător, motivul vânzării | Secret comercial / mandat [I] | **DA** dacă dezvăluie poziția de negociere |
| Adresă exactă + nume proprietar | GDPR | ANON |

### Recrutare / HR
| Dată | Bază legală | Niciodată? |
|---|---|---|
| CV-uri (nume, contact, istoric) | GDPR | ANON |
| Medicina muncii, concedii medicale, dizabilitate | GDPR art. 9 | **DA** |
| Evaluări de performanță, motive de concediere | GDPR + Codul muncii | ANON doar dacă nu identifică persoana prin context [I] |
| Decizii automate de selecție a candidaților | AI Act Anexa III (risc ridicat) **de verificat** | **DA** pentru decizia automată |

### Firme IT de outsourcing
| Dată | Bază legală | Niciodată? |
|---|---|---|
| Cod sursă al clientului | NDA + secret comercial [F] S15; cazul Samsung [F] S37 | **DA** (neanonimizabil util, vezi 03) |
| Chei API, parole, certificate, `.env` | Securitate | **DA** (nici măcar pseudonimizat: nu e nevoie de ele) |
| Date de producție din bazele clienților | GDPR (firma e împuternicit) | **DA**; date sintetice în locul lor |
| Arhitectură, adrese IP interne | Secret comercial / NDA | ANON parțial |

## 4. Lista „NICIODATĂ” transversală [I]

Datele de mai jos merg pe **ROȘU** în orice segment, pentru că valoarea lor stă tocmai în conținut sau pentru că nu-i folosesc AI-ului deloc:

1. Parole, chei API, tokenuri, certificate.
2. Date de sănătate legate de o persoană identificabilă, inclusiv prin context.
3. Copii de acte de identitate.
4. Date penale.
5. Cod sursă și secrete comerciale ale clienților sub NDA.
6. Strategii juridice sau comerciale pe un caz concret și recognoscibil.
7. Rapoarte AML / ONPCSB.

[V] Lista trebuie confirmată cu câte un profesionist din fiecare segment: „ce ați considera grav să afle cineva din afară?”
