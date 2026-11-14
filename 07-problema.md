# 07 · Problema, descrisă exact

> **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** ipoteză / decizie de design · **[V]** de validat la interviuri

## 1. Problema într-o frază

În firmele de 1–100 de angajați, oamenii lipesc în ChatGPT, Claude, Gemini sau Copilot documente de lucru care conțin **cinci feluri de date protejate**:
- datele clienților persoane fizice;
- datele firmelor-client;
- datele angajaților;
- **secretele financiare și comerciale ale firmei însăși**;
- parole.

Antreprenorul nu vede ce pleacă. Are de ales doar între a interzice AI-ul (și a pierde productivitate) și a spera că nu se întâmplă nimic (și a risca amenzi, încălcarea secretului profesional și scurgeri către concurență).

[V] Partea „oamenii lipesc” e ipoteza cea mai riscantă (H1 din [05](05-ipoteze-si-interviuri.md)). În RO nu avem date, doar cifre de la vânzători din alte țări: [F] S29 S30 S31, **afirmație de vânzător**.

## 2. Ce firme, exact

### 2.1 Criteriile de calificare (toate patru)
1. **1–100 de angajați** care lucrează la calculator.
2. **Prelucrează documente cu date ale altora** (clienți, pacienți, angajați) sau **cu cifre ale firmei pe care concurența n-ar trebui să le vadă**.
3. **Au o obligație de confidențialitate**: GDPR, secret profesional, contracte cu NDA sau secret comercial.
4. **N-au un departament de IT sau securitate.** Cel mult un om de IT sau o firmă IT externă.

[V] Întrebarea de calificare la interviu: *„Ce document cu date de clienți sau cu cifre ale firmei ați deschis ieri la calculator?”* Dacă răspunsul e „niciunul”, nu e client.

### 2.2 Cât de mare e piața (doar cifre găsite)
| Clasă de mărime | Firme în RO, 2025 | Ce înseamnă pentru noi | Sursă |
|---|---|---|---|
| Micro (0–9) | 987.671 | Nu au IT. **Antreprenorul instalează singur**, deci produsul trebuie să fie self-service [I] | [F] S3 |
| Mici (10–49) | 44.894 | Au de obicei o firmă IT externă (**de verificat**) | [F] S3 |
| Mijlocii (50–100) | parte din cele 7.659 de firme cu 50–249 de angajați; **cifra exactă pentru 50–100 e necunoscută** | Au om de IT, uneori DPO | [F] S3 |

Câte dintre ele sunt în segmentele de mai jos: **necunoscut** (de aflat din INS TEMPO, pe cod CAEN).

### 2.3 Segmentele și documentele concrete cu care lucrează
| Segment | Documente zilnice (exemple concrete) | Ce clase de date conțin (vezi §3) |
|---|---|---|
| **Cabinet de contabilitate** | Balanțe de verificare, state de plată, declarații D112/D300, extrase bancare, facturi | **B** (cifrele firmelor-client), A (CNP-uri din state), C, D (onorariile proprii), E (acces SPV) |
| **Cabinet medical / clinică** | Fișe de consultație, scrisori medicale, rezultate de analize, programări | **A** (date de sănătate), C, D |
| **Cabinet de avocatură** | Contracte, cereri de chemare în judecată, corespondență cu clientul, acte de identitate | **A** și **B** (sub secret profesional), D |
| **Broker de asigurări** | Cereri de ofertă, chestionare medicale, dosare de daună, copii CI și talon | A (inclusiv sănătate), B, D (comisioanele negociate) |
| **Agenție imobiliară** | Contracte de intermediere, extrase CF, copii CI, oferte de preț | A, D (prețul minim al vânzătorului, comisioane) |
| **Recrutare / HR** | CV-uri, evaluări, grile de salarizare, contracte de muncă | A (candidați), **C**, D (tarifele către clienți) |
| **Firmă IT de outsourcing** | Cod sursă al clienților, specificații, chei de acces, oferte | **B** (cod și date sub NDA), D, **E** |
| **Orice firmă mică (transversal)** | Situații financiare, oferte către clienți, contracte cu furnizori, salarii, cash-flow | **C**, **D** |

Ultimul rând contează: **orice** firmă are clasele C și D, chiar și cele care nu lucrează cu date de clienți [I].

## 3. Ce tip de date: cele cinci clase

| Clasa | Ce e | Exemple concrete | Cine e prejudiciat | Baza legală | Obligația e a… |
|---|---|---|---|---|---|
| **A. Date personale ale clienților** (persoane fizice, pacienți, candidați) | Orice informație despre o persoană identificabilă | Nume + CNP, diagnostic, adresă, IBAN personal, istoric de daune | Persoana, apoi firma (amendă) | GDPR, inclusiv art. 9 pentru sănătate; Legea 190/2018 pentru CNP; secret profesional | **Legii** [F] S13 S17 S10 S11 |
| **B. Date ale firmelor-client** (clienți persoane juridice) | Cifrele și documentele unei alte firme | Balanța unui SRL-client, contractul lui, codul lui sursă, datoriile lui la ANAF | Firma-client, apoi noi (răspundere contractuală) | Secret profesional (contabil, avocat); NDA; **nu GDPR**, cu excepția persoanelor numite în documente | **Legii profesiei și a contractului** [F] S7 S9 |
| **C. Date ale angajaților proprii** | Date personale ale echipei | Salarii individuale, CNP-uri, concedii medicale, evaluări | Angajatul, apoi firma | GDPR, Codul muncii | **Legii** [F] S17 |
| **D. Secretele firmei însăși** | Informații cu valoare economică pe care firma le ține secrete | Cifra de afaceri reală, **marje**, prețuri și oferte, lista și tarifele clienților, contracte cu furnizori, datorii, planuri de investiții sau concedieri | **Firma** (pierdere în fața concurenței) | Secret comercial: protejat **doar dacă firma ia „măsuri rezonabile”** [F] S15. Nu e GDPR | **Antreprenorului**: el decide ce e secret |
| **E. Date de acces** | Ce deschide sisteme | Parole, chei API, token SPV, coduri de autentificare bancară, certificate | Toți | GDPR art. 32 (securitate); bun-simț | Nimeni nu are nevoie să le trimită la AI |

## 4. Răspunsul la întrebare: protejăm doar datele clienților?

**Nu.** Protejăm toate cele cinci clase, dar **diferit**, pentru că diferă cine decide și ce se poate pseudonimiza.

### 4.1 De ce nu doar clienții [I]
1. **La firmele B2B, „datele clientului” sunt chiar secretele lui financiare.** Pentru un cabinet de contabilitate, balanța unui client e clasa B, nu A. Dacă am proteja doar datele personale, n-am proteja nimic din ce contează în contabilitate.
2. **Antreprenorul plătește, iar secretele lui îl dor mai tare decât GDPR-ul.** Ipoteza noastră: un antreprenor se teme mai mult că marjele sau oferta lui ajung la concurență decât de o amendă ANSPDCP. **Trebuie validat** [V]: dacă e adevărat, propunerea de valoare se schimbă.
3. **Legea secretului comercial cere „măsuri rezonabile”** [F] S15. Un instrument care oprește scurgerea în AI poate deveni dovada acestor măsuri. E un argument de vânzare pentru clasa D [I], de confirmat cu un jurist [V].
4. **Toate firmele au clasa D.** Inclusiv cele fără date de clienți sensibile, deci piața e mai largă [I].

### 4.2 Regula de bază: cine decide pentru fiecare clasă
| Clasa | Implicit | Poate antreprenorul să relaxeze regula? | De ce |
|---|---|---|---|
| A. Clienți persoane fizice | **Pornit** | **Nu, sub un minim legal** (CNP, sănătate, acte rămân protejate) | Obligația e a legii, nu a antreprenorului |
| B. Firme-client | **Pornit** | Doar cu acordul clientului (de exemplu o clauză în contract) | Obligația e față de client |
| C. Angajați | **Pornit** | Nu, sub minimul legal | Obligație legală |
| D. Secretele firmei | **Pornit, configurabil** | **Da, complet**: e informația lui | Antreprenorul decide ce e secret |
| E. Date de acces | **Blocat mereu** | Nu | Nu există sarcină AI care să ceară o parolă |

### 4.3 Cum protejăm concret secretele financiare (clasa D, dar și B)
Problema specială: **la cifrele financiare, cifrele sunt chiar conținutul.** Dacă le ascundem, AI-ul n-are ce analiza. Soluția: **ascundem identitatea, nu structura** [I].

| Ce ascundem | Tehnica | Ce rămâne util pentru AI | Ce se strică |
|---|---|---|---|
| **Numele firmei, CUI-ul, numele clienților, furnizorilor, produselor** | Pseudonimizare cu nume fictive, din lista importată de firmă (§5.3 din [06](06-solutie.md)) | Toată analiza | Nimic. AI-ul nu mai știe **a cui** e balanța |
| **Sume absolute** (cifra de afaceri, datorii, prețuri) | **Scalare cu un factor secret**, același pe toată conversația (×1,37), refăcută la întoarcere | Procentele, marjele, creșterile, proporțiile, comparațiile între perioade | Comparațiile cu **praguri fixe din lege** (plafon TVA, plafon micro): AI-ul ar compara o sumă falsă cu pragul real |
| **Contextul care identifică** (oraș + domeniu + mărime) | Generalizare („firmă de construcții din Regiunea Centru”) | Încadrarea pe industrie | Detaliile locale |
| **Documente în care secretul e chiar conținutul** (ofertă la licitație, strategie de preț, plan de concedieri) | **ROȘU** implicit; antreprenorul poate permite | — | — |

**Exemplu (fictiv), cabinet de contabilitate:**
> Original: *„Analizează balanța Alfa Construct SRL (CUI 12345678) pe T3: cifră de afaceri 2.340.000 lei, profit 312.000 lei, 41% din vânzări către Dedeman. Merită să treacă pe impozit pe profit?”*
>
> Trimis la AI: *„Analizează balanța Beta Instal SRL (CUI [fictiv]) pe T3: cifră de afaceri 3.205.800 lei, profit 427.440 lei, 41% din vânzări către Client_A. Merită să treacă pe impozit pe profit?”*
>
> Marja (13,3%) și concentrarea pe un client (41%) rămân corecte, deci analiza AI e utilă.
> **Problemă:** întrebarea „merită să treacă pe impozit pe profit?” depinde de **plafoane fixe din lege**. Pe sume scalate, AI-ul poate trage o concluzie greșită. **Regula** [I]: când promptul conține cuvinte de prag („plafon”, „limită”, „micro”, „TVA la încasare”), agentul **nu scalează**. Pseudonimizează doar identitatea și îl avertizează pe angajat că sumele pleacă reale (fără nume).

### 4.4 Ce nu putem promite pentru secretele firmei
- **Firmele mari sau unice se recunosc din cifre și context** chiar și fără nume (singurul producător de X din județ). Pseudonimizarea reduce riscul, dar nu îl anulează [I].
- **Agentul nu știe singur ce e secret pentru o firmă.** Cifrele, numele și cuvintele-cheie le detectează. Faptul că „proiectul Orion” e secret îl află doar dacă antreprenorul îl adaugă la termenii interni ([06 §5.3](06-solutie.md)).
- **Dacă antreprenorul relaxează clasa D**, decizia e a lui. Nu se poate relaxa însă sub minimul legal pentru A și C.

## 5. Propunerea de valoare, revizuită

Varianta din [06](06-solutie.md) spunea „datele care identifică un client”. Acum e prea îngustă. **Varianta corectată:**

> **Ajutăm** firmele de 1–100 de angajați care lucrează zilnic cu documente ce conțin date ale clienților, ale angajaților și cifrele firmei (facturi, balanțe, state de plată, fișe de pacient, contracte, oferte), dar care nu-și permit o soluție enterprise de la producătorii licențiați de AI,
> **să** folosească ChatGPT, Claude, Gemini și Copilot pe aceste documente **fără ca datele clienților, ale angajaților și secretele financiare ale firmei să plece din firmă în formă identificabilă**,
> **prin** un agent instalat pe calculatoarele firmei care interceptează local ce se trimite către aplicațiile AI, ascunde identitatea persoanelor și a firmelor (și, la nevoie, scalează sumele), pune datele la loc în răspuns, blochează parolele, mută documentele care nu pot pleca într-un AI care rulează local în firmă și îi arată antreprenorului, în fiecare lună, ce a fost oprit sau mutat și totodată îi dă libertatea angajatului de a-și automatiza rezolvarea unui task.

**Pe slide:** *„AI pe documentele firmei, fără ca datele clienților și cifrele firmei să plece din firmă.”*

## 6. Ce trebuie validat (întrebări Mom Test, pe ton natural)
| # | Întrebare | Ce decide |
|---|---|---|
| 1 | „Ce informații de-ale firmei țineți cel mai ascunse? A ajuns vreodată ceva din ele unde nu trebuia?” | Dacă clasa D doare mai tare decât A |
| 2 | „Ultima dată când ați trimis cifrele firmei cuiva din afară, la bancă, la un consultant sau la contabil, ați scos ceva din ele înainte? Ce?” | Dacă antreprenorii protejează deja clasa D, deci dacă au nevoia |
| 3 | (contabil) „Ultima dată când ați lucrat pe balanța unui client în afara programului de contabilitate, de exemplu în Excel sau pe mail, ce ați făcut cu ea?” | Clasa B în practică |
| 4 | „Ați semnat anul ăsta vreun contract cu clauză de confidențialitate? Zicea ceva despre programele pe care aveți voie să le folosiți?” | Dacă clasa B e și obligație contractuală |
| 5 | (antreprenor) „Cine din firmă vede cifrele reale, marjele, cifra de afaceri? Cum le trimiteți între voi?” | Câți angajați au acces la clasa D |
