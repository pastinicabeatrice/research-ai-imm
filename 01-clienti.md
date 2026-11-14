# 01 · Clienții: cui vindem și cine are cea mai mare durere

> Legenda: **[F]** = faptă cu sursă (ID-urile trimit la [surse.md](surse.md)) · **[I]** = ipoteza noastră · **[V]** = de validat la interviuri.

## 1. Piața în cifre

| Indicator | Valoare | Sursă |
|---|---|---|
| Întreprinderi mici (10–49 pers.) în RO, 2025 | 44.894 (4,3% din firme, 19% din angajați) | [F] S3 (estimare JRC) |
| Întreprinderi mijlocii (50–249 pers.) în RO, 2025 | 7.659 (0,7% din firme) | [F] S3 |
| Firme RO cu ≥10 angajați care folosesc AI, 2025 | **5,2%**, ultimul loc în UE (media UE 20,0%) | [F] S1 |
| Firme mici din UE care folosesc AI | 17%; mijlocii 30,36% | [F] S2 |
| Principalele motive pentru care nu folosesc AI (UE, doar firmele care s-au gândit la AI) | lipsă de expertiză 70,89%, consecințe juridice neclare 52,52%, **protecția datelor 48,83%** | [F] S2 |
| Ponderea sănătății în IMM-urile RO | 3,4% (UE 8,0%) | [F] S3 |
| Ponderea serviciilor profesionale, științifice și tehnice în IMM-urile RO | 11,4% (UE 16,7%) | [F] S3 |
| Câte firme din segmentele noastre au 10–100 de angajați | **necunoscut, de aflat** (INS TEMPO pe cod CAEN × clasă de mărime) | — |

**Ce înseamnă pentru noi.** Cifra de 5,2% măsoară utilizarea AI *declarată de firmă*. Nu măsoară utilizarea făcută de angajați pe conturi personale. Vânzătorii raportează niveluri mari de „shadow AI”:

- 78% din utilizatorii de AI își aduc propriile instrumente la muncă, conform Microsoft [F] S30, **afirmație de vânzător**;
- 32,3% din utilizarea ChatGPT trece prin conturi personale, conform Cyberhaven [F] S31, **afirmație de vânzător**.

[I] Diferența dintre utilizarea oficială (5%) și cea reală este exact problema noastră. Firmele nu știu ce fac angajații.
[V] Cât folosesc AI angajații firmelor mici din România: **necunoscut, de aflat la interviuri**. Nu avem nicio sursă cu date despre România.

## 2. Cine decide, cine plătește, cine folosește

| Rol | Ce face | Ce știm |
|---|---|---|
| **Antreprenorul / asociatul administrator** | Semnează și plătește. Răspunde personal (GDPR, secret profesional, deontologie) | [I] El e cumpărătorul în firmele de 10–50 de oameni |
| **Firma IT externă (MSP) sau „omul de IT”** | Instalează antivirusul și administrează licențele. De multe ori recomandă produsul | [F] Bitdefender își vinde noul modul AI „organizațiilor și MSP-urilor” S33. [I] MSP-ul e canalul de distribuție, nu cumpărătorul |
| **DPO / consultantul GDPR extern** | Redactează politici. Poate cere sau recomanda o soluție | [I] Influențează decizia. [V] Câte firme mici au DPO extern |
| **Contabilul extern** | Plătește facturile, nu ia decizii de securitate | [I] Rol minor în decizie. [V] |
| **Angajatul** | Folosește AI-ul. Poate ocoli controlul (telefonul personal) | [F] Pe conturile personale datele pot fi folosite la antrenare implicit (ChatGPT Free/Plus S26, Claude Free/Pro S27) |

[I] **Cumpărătorul principal:** antreprenorul unei firme de 10–100 de oameni dintr-o profesie reglementată, la recomandarea MSP-ului.
[V] Cine a cumpărat ultimul antivirus sau soft de securitate în firmă, cine l-a ales și din ce buget.

## 3. Segmentele: tabel comparativ

Durerea este estimarea noastră [I], pe baza obligațiilor legale [F] și a sarcinilor pentru care ar folosi AI [I]. Scorul **nu** e validat.

| Segment | Date folosite zilnic | Obligații de confidențialitate | Utilizări probabile ale AI [I] | Durere [I] |
|---|---|---|---|---|
| **Cabinete de contabilitate / expertiză** | CNP-uri, salarii, state de plată, IBAN, CUI, facturi, balanțe, declarații fiscale, date despre datorii | GDPR; Legea 190/2018 art. 4 (CNP) S13; confidențialitate în OG 65/1994 art. 20 S9; Codul etic CECCAR (**de verificat**); entitate raportoare AML (Legea 129/2019) S12 | E-mailuri către clienți, explicații fiscale, formule Excel, rezumate de legislație, verificarea balanțelor | **Ridicată**: volum mare de identificatori, utilitate AI mare |
| **Cabinete de avocatură** | Dosare, nume de părți, contracte, strategie procesuală, corespondență cu clientul, date penale | Secret profesional „absolut și nelimitat în timp” S7; infracțiune în Legea 51/1995 S8; Cod penal art. 227 S14; GDPR art. 10 (date penale) | Redactare și sintetizare de contracte, cereri, cercetare juridică, traduceri | **Foarte ridicată**: conținutul însuși e secretul |
| **Clinici și cabinete medicale** | Diagnostic, rezultate de analize, tratament, CNP, istoric, imagini | GDPR art. 9 (date de sănătate); Legea 46/2003 art. 21 S10; Codul CMR art. 30–31, **art. 36 AI** S11; Cod penal art. 227 S14 | Scrisori medicale, rezumate de fișe, răspunsuri către pacienți, administrativ | **Foarte ridicată**: amenzi ANSPDCP deja aplicate clinicilor mici S39 |
| **Brokeri de asigurări** | CNP, date despre vehicule și locuințe, istoric de daune, uneori date medicale (asigurări de viață/sănătate), IBAN | GDPR art. 9 pentru sănătate; Legea 236/2018 (articolul de confidențialitate **de verificat**) S16; AML | Comparații de oferte, e-mailuri, rezumate de polițe | **Medie–ridicată** |
| **Agenții imobiliare** | Date de identitate ale cumpărătorilor și vânzătorilor, prețuri, extrase CF, contracte, IBAN | GDPR; entitate raportoare AML (Legea 129/2019) S12; secret comercial pentru prețuri și mandate S15 | Anunțuri, descrieri de proprietăți, e-mailuri | **Medie**: multe sarcini AI nu cer date personale |
| **Recrutare / HR** | CV-uri, evaluări, salarii, date medicale (concedii, aptitudini), uneori date sensibile (etnie, sindicat) | GDPR art. 9 și art. 88; Codul muncii; AI Act: AI pentru recrutare e **risc ridicat** (Anexa III) **de verificat** | Filtrare de CV-uri, anunțuri, rezumate de interviuri | **Ridicată**: și risc AI Act, nu doar GDPR |
| **Firme IT de outsourcing** | Cod sursă al clienților, chei API, date de test, arhitecturi, contracte cu NDA | Secret comercial S15; NDA-uri contractuale; GDPR pentru datele clienților din baze | Asistenți de cod, depanare, documentație | **Ridicată ca volum**, dar AI-ul e de neînlocuit și codul nu se poate anonimiza (vezi 03) |

## 4. Prioritizarea noastră [I]

1. **Contabilitate**: cea mai potrivită cu GALBEN. Datele sunt structurate (CNP, IBAN, CUI, sume), deci ușor de detectat și înlocuit, iar răspunsul AI rămâne util.
2. **Clinici medicale**: durere mare și sancțiuni reale, dar o mare parte din date ajunge pe ROȘU (vezi 04).
3. **Avocatură**: durere maximă, dar conținutul e secretul. Produsul nostru ar bloca mult, așa că valoarea percepută poate fi mică.
4. **Firme IT de outsourcing**: o capcană pentru noi. Codul sursă nu se poate anonimiza util, iar dezvoltatorii vor ocoli blocarea.

[V] Ordinea de mai sus e ipoteza noastră. Interviurile o confirmă sau o răstoarnă.

## 5. Concurență și alternative (ce face deja clientul)

| Alternativă | Ce face | Pentru IMM? |
|---|---|---|
| Interdicție totală (ex. Samsung, 2023) | Interzice AI-ul generativ S37 | Gratuit, dar împinge angajații spre telefoane [I] |
| Abonament AI de business (ChatGPT Business, Claude for Work, Gemini în Workspace) | Datele nu sunt folosite la antrenare implicit S26 S27 S28 | ChatGPT Business costă ~25 $/utilizator/lună (presă, **de verificat**). **Rezolvă problema antrenării, dar nu și pe cea a secretului profesional** [I] |
| Microsoft Purview DLP pe dispozitiv | Avertizează sau blochează datele sensibile trimise către ChatGPT și Gemini în Edge S32 | Cere licențe E5 sau suplimente: scump pentru 10–100 de oameni [I] |
| Bitdefender GravityZone AI Visibility & Control | Descoperă instrumentele AI și le permite sau blochează la nivel de aplicație. **Nu** inspectează promptul S33 | Vândut prin MSP-uri; Bitdefender e firmă românească |
| ESET AI Conversation Security | Inspectează fișierele încărcate pentru conținut sensibil S34 | Integrat în ESET PROTECT |
| Harmonic, Nightfall, LayerX | Extensii de browser care inspectează prompturile, avertizează sau blochează S35 | Prețuri nepublice, vânzare directă către companii mari |
| Gateway-uri cu pseudonimizare reversibilă (WSO2, PromptScrub) | Înlocuiesc datele cu etichete și le restaurează în răspuns S36 | Pentru dezvoltatori, nu pentru utilizatorul final |

[I] **Diferențiatorul nostru real:** pseudonimizare reversibilă (GALBEN) direct în interfața web a AI-ului public, pentru utilizatorul final, la preț de IMM și în limba română (CNP, CUI, IBAN RO). Bucățile tehnice există deja separat S36. Combinația pentru IMM-uri românești n-am găsit-o, dar **absența ei nu e dovedită**.
[V] Ce folosesc azi firmele: interdicție, nimic, abonament business sau Purview?

## 6. De validat la interviuri (rezumat)

- Ultima dată când un angajat a folosit AI cu date de client: ce a introdus și de unde a aflat antreprenorul?
- Cine a ales ultimul soft de securitate și cât a costat?
- Există o politică scrisă despre AI? Cine a scris-o?
- Folosesc deja un abonament AI de business?
