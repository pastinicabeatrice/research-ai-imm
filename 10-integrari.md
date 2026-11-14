# 10 · Integrări: preseturi și categorii proprii, Jev, modelul local, MCP pentru antreprenor

> **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** decizie de design / ipoteză · **[V]** de validat
> Completează [06-solutie.md](06-solutie.md). Nimic nu e construit încă.

## 1. Preseturi cu date sensibile + categorii adăugate de firmă

### 1.1 Ce primește firma la instalare: preseturi pe domenii
La instalare, antreprenorul alege domeniul. Firma primește un **preset**: un set de categorii de date sensibile, fiecare cu o acțiune deja setată (VERDE, GALBEN sau ROȘU). Presetul pornește de la matricea din [04](04-matrice-decizie.md).

| Preset | Ce conține în plus față de „General” |
|---|---|
| **General** (pentru oricine) | CNP, IBAN, CUI, serie CI, e-mail, telefon, adresă, nume de persoane, sume, parole și chei |
| **Contabilitate** | Balanțe și state de plată (sume scalate), CUI-urile clienților, termeni AML („tranzacție suspectă”, „ONPCSB”) pe ROȘU |
| **Medical** | Diagnostice, tratamente, rezultate de analize, imagini medicale pe ROȘU (mutate în AI-ul local) |
| **Juridic** | Numele părților, numere de dosar, „partaj”, „penal”, „strategie”; contractele încărcate pe ROȘU |
| **Asigurări** | Chestionare medicale pe ROȘU, serii de șasiu, numere de înmatriculare, daune |
| **Imobiliare** | Copii CI pe ROȘU, extrase CF, prețul minim al vânzătorului |
| **Resurse umane** | CV-uri, evaluări, salarii individuale, concedii medicale pe ROȘU |
| **IT** | Cod sursă al clienților, chei API, fișiere `.env`, adrese IP interne |

Presetul e un **punct de pornire**, nu o regulă fixă. Firma îl poate schimba, cu limitele din §1.3.

### 1.2 Ce poate adăuga firma: date sensibile proprii, pe categorii
Antreprenorul adaugă ce e sensibil **pentru firma lui**, în categoria potrivită. Sunt patru feluri de a descrie o dată sensibilă, toate fără cunoștințe tehnice:

| Fel | Exemplu | Cum se introduce | În ce categorie |
|---|---|---|---|
| **Listă de valori** | Numele celor 140 de clienți, ale furnizorilor, ale produselor | Import din Excel/CSV sau din programul de contabilitate | Clienți · Furnizori · Produse |
| **Cuvinte-cheie** | „Proiectul Orion”, „fuziune”, „licitația CJ Cluj” | Le scrie într-o listă | Secrete comerciale · Proiecte interne |
| **Format** | Coduri interne „PRJ-0000”, numere de contract „CTR/2026/…” | Alege dintr-un șablon: „litere fixe + cifre” (fără expresii regulate) | Documente interne |
| **Categorie nouă** | „Rețete de producție”, „Liste de prețuri pentru parteneri” | Nume + acțiune (VERDE, GALBEN, ROȘU) + cuvintele sau valorile ei | Orice nume ales de firmă |

Pentru fiecare valoare sau categorie, antreprenorul alege și **acțiunea**: permite · ascunde (pseudonimizează) · scalează (pentru sume) · mută în AI-ul local · blochează.

Exemplu, cabinet de contabilitate: presetul **Contabilitate** + lista celor 140 de clienți (import CSV) + cuvântul-cheie „control ANAF” pe ROȘU + formatul „DOS-0000” pentru numerele interne de dosar.

### 1.3 Reguli care nu se pot relaxa [I]
Firma poate face orice categorie **mai strictă**. **Nu** poate relaxa sub minimul legal:
- clasa A (date personale ale clienților persoane fizice: CNP, sănătate, acte);
- clasa C (date ale angajaților);
- clasa E (parole și chei).

Pentru clasa B (date ale firmelor-client), relaxarea cere o bifă care confirmă acordul clientului. Clasele sunt descrise în [07](07-problema.md).

### 1.4 Unde stau datele adăugate [I]
- **Doar local**, criptate, pe calculatoare sau pe serverul din birou. Lista clienților e ea însăși o dată sensibilă: nu pleacă la noi și nu pleacă la niciun AI din cloud (vezi §4.3).
- Pentru potrivire, agentul folosește și formele declinate ale numelor („Popescu”, „lui Popescu”) [V: de testat cum se comportă detectarea pe română].

## 2. Jev (TypeSafe) și jev-agent.com

### 2.1 Ce este [F]
- **Jev** e modelul de decizie al TypeSafe AI, primul model „System One”, în acces timpuriu din septembrie 2026. Primește o „stare” (contextul) și întrebări despre ea; antrenat prin „reinforcement learning for calibrated decisions” (RLCD) [F] S56. Nu scrie text: primește date și întrebări declarate și răspunde cu **decizii tipizate și probabilități**. Întrebările pot fi de trei feluri: alegere dintre opțiuni, scor pe o grilă, da/nu. Ca latență, TypeSafe declară 70–500 ms. [F] S52, **afirmație de vânzător, relatată de o recenzie**.
- Recenzia avertizează: un răspuns „tipizat” nu e neapărat corect. Jev e probabilistic. [F] S52
- Jev rulează **în cloud**, accesat printr-un SDK. Nu am găsit o versiune care să ruleze local. [F] S52, S54
- Despre date, TypeSafe declară că cererile nu sunt folosite la antrenare și că păstrarea zero e disponibilă pentru clienții enterprise. Regiunea de procesare nu e precizată. [F] S52
- **jev-agent.com** e „o platformă independentă” care **„nu e afiliată cu TypeSafe AI”**. Cine o operează nu e cunoscut. Planul gratuit are 5 credite pe lună, adică ~5.000 de token-uri de intrare. [F] S53. Site-ul nu s-a deschis la verificarea noastră (14.11.2026).
- Există și un server MCP comunitar, „jev-use”, care trimite decizii simple către Jev. Nu e clar dacă e oficial. [F] S54

### 2.2 Cum îl integrăm fără să încălcăm promisiunea [I]
Jev e în cloud, deci **nu primește niciodată textul brut**. Îl folosim ca **a doua verificare, pe textul deja curățat local**, înainte să plece spre ChatGPT, Claude sau Gemini. Jev nu vede nimic în plus față de ce ar primi oricum AI-ul public.

```
text brut ──► detectare locală + ascundere (pe calculator)
                 │
                 ▼
        text curățat ──► Jev: 3 întrebări ──► dacă e risc: ROȘU, mutat în AI-ul local
                 │                                   
                 ▼ (dacă e în regulă)
            ChatGPT / Claude / Gemini
```

Întrebările puse lui Jev:
| Tip | Întrebarea | Ce face agentul cu răspunsul |
|---|---|---|
| Da/nu | „Textul rămas permite recunoașterea unei persoane sau a unei firme?” | Peste prag → ROȘU (AI local) |
| Alegere | „Ce fel de document e: e-mail · contract · fișă medicală · cod sursă · ofertă · altul?” | Contract, fișă medicală sau ofertă → ROȘU, după preset |
| Scor | „Cât de sensibil e conținutul, de la 1 la 5?” | 4–5 → cere confirmarea angajatului |

**Cum arată cererea** (după formatul din documentația TypeSafe, primit de la echipă [F] S56). Trimitem **o singură cerere** cu toate întrebările, pentru că Jev le evaluează în paralel. În cerere, „state” e textul **deja curățat** pe calculator:

```json
{
  "model": "jev-latest",
  "state": "Scrie-i Mariei Dobre că firma Beta Instal SRL are de plată TVA până pe 25 noiembrie.",
  "questions": {
    "recognoscibil": {
      "type": "noul",
      "instructions": "Textul permite recunoașterea unei persoane sau a unei firme anume, chiar fără nume reale"
    },
    "date_sanatate": {
      "type": "noul",
      "instructions": "Textul conține informații despre sănătatea unei persoane"
    }
  }
}
```

Răspunsul are forma `{"recognoscibil": {"type": "noul", "noul": 0.04}, …}`: probabilitatea ca afirmația să fie adevărată. Agentul compară cu un prag pus de noi (de exemplu 0,5 pentru „recognoscibil” și 0,3 pentru „date_sanatate”, mai strict) [I, praguri de calibrat în T11].

Întrebările de tip **choice** („ce fel de document e”) și **score** („cât de sensibil, de la scăzut la ridicat”) au alte câmpuri decât `noul`. Le luăm exact din documentația TypeSafe când le implementăm [V]. Dacă agentul e scris în Python, există și integrarea LangChain (`langchain-typesafe`, clasa `TypeSafeClassifier`) [F] S56. Altfel, apelăm direct API-ul.

**De ce merită** [I]: prinde exact ce scapă detectării locale (cazul din [03](03-anonimizare.md): „pacient de 67 de ani din comuna X…”, fără niciun nume). E ieftin și rapid, după cifrele vânzătorului. Un model local mic ar face același lucru mai încet.

**Condiții:**
1. **Pentru producție:** contract direct cu TypeSafe, cu acord de prelucrare (DPA) și păstrare zero. **Nu** printr-un revânzător neoficial cu operator necunoscut.
2. **Pentru demo:** jev-agent.com sau contul direct TypeSafe, doar cu texte fictive. Cele 5.000 de token-uri pe lună ale planului gratuit ajung doar pentru câteva zeci de verificări scurte [I].
3. **Dacă Jev nu răspunde** (rețea, cotă), agentul nu așteaptă. Decide singur, mai strict.
4. **Opțiune fără cloud:** aceleași 3 întrebări le poate pune modelul local (§3). E mai lent, dar nimic nu iese din firmă. Antreprenorul alege.

**Teste noi:**
| # | Test | Criteriu [I] |
|---|---|---|
| T11 | 50 de texte fictive deja curățate, jumătate încă recognoscibile prin context | Jev prinde ≥ 80% din cele recognoscibile, cu ≤ 10% alarme false |
| T12 | Latența reală a verificării Jev din România | < 500 ms în 9 din 10 cazuri |

## 3. Modelul AI local: Qwen

**Ce ai cerut:** „Qwen 3.8 de 8B”. **Ce există** [F] S51: pagina oficială Qwen3.8 listează doar două modele, **Qwen3.8-27B** (14.08.2026) și **Qwen3.8-2.4T-A95B** (12.08.2026). **Nu există un Qwen3.8 de 8B.** Modelele mici sunt din seria Qwen3.5: 9B, 4B, 2B și 0.8B (02.03.2026), cu suport pentru „201 limbi și dialecte”.

| Variantă | Pentru cine | Ce cere | Licență |
|---|---|---|---|
| **Qwen3.5-9B** (cel mai apropiat de „8B”) | Laptop bun sau un calculator obișnuit din birou | Un model de mărimea asta merge cuantizat cu ~16 GB RAM [F] S48 (bloguri); fără placă video e lent | De verificat pe fișa modelului [V] |
| **Qwen3.8-27B** | Server în birou, cu placă video | Exemplele oficiale de rulare folosesc mai multe plăci video; varianta cuantizată pe o singură placă **de testat** (T9) | Apache-2.0 pentru repo; licența ponderilor e pe fișa modelului [F] S51 [V] |

**Recomandare [I]:** **Qwen3.5-9B** implicit, pentru că rulează pe ce au firmele mici. **Qwen3.8-27B** ca variantă „AI-ul biroului” pentru firmele care au sau cumpără un server cu placă video. Agentul vorbește cu modelul printr-o interfață standard, așa că schimbarea modelului e o setare, nu o rescriere.

Pentru română: Qwen3.5 declară 201 limbi, dar calitatea pe documente românești de business **nu e cunoscută** (T8).

## 4. „Dashboard-ul” antreprenorului ca server MCP

### 4.1 Ideea
În loc de o consolă web în plus, antreprenorul **își întreabă propriul asistent AI** (Claude, ChatGPT sau AI-ul local) despre ce se întâmplă în firmă. Datele vin printr-un server **MCP** (Model Context Protocol), un standard deschis prin care un asistent AI primește acces la „unelte” externe [F] S55.

> Antreprenorul: „Ce s-a oprit luna asta și cine a cerut excepții?”
> Asistentul (apelează `raport_lunar` și `exceptii_in_asteptare`): „În octombrie: 41 de trimiteri cu date de clienți, toate protejate; 3 mutate în AI-ul local (fișe medicale). Două excepții așteaptă aprobare, ambele de la Angajatul 4…”

### 4.2 Uneltele serverului MCP
| Unealtă | Ce face | Ce date întoarce |
|---|---|---|
| `raport_lunar(luna)` | Raportul lunii | Numere pe categorii și acțiuni, pe aplicații, comparat cu luna trecută |
| `evenimente(zile, categorie?)` | Ce s-a întâmplat recent | Oră, aplicație, categorie, acțiune, angajat **cu pseudonim** („Angajatul 4”). **Niciodată textul** |
| `exceptii_in_asteptare()` | Cererile de excepție | Categoria, aplicația, motivul ales din listă |
| `aproba_exceptie(id)` / `respinge_exceptie(id)` | Decizia antreprenorului | Confirmare |
| `categorii()` | Presetul și categoriile firmei | Nume, acțiune, câte valori are fiecare (nu valorile) |
| `seteaza_actiune(categorie, actiune)` | Schimbă regula unei categorii | Confirmare; refuză relaxarea sub minimul legal (§1.3) |
| `adauga_date_sensibile(categorie, valori)` | Adaugă cuvinte, valori sau formate | **Doar în modul local** (§4.3) |

### 4.3 Regula de bază: ce vede AI-ul antreprenorului [I]
Dacă antreprenorul conectează serverul MCP la un **AI din cloud** (Claude, ChatGPT), tot ce întorc uneltele ajunge la furnizorul acelui AI. De aceea serverul are două moduri:

| Mod | Când | Ce e permis |
|---|---|---|
| **Cloud** | Serverul e conectat la Claude, ChatGPT etc. | Doar date agregate și pseudonimizate: numere, categorii, „Angajatul 4”. **Fără** text de prompt, fără nume de clienți, fără numele angajaților. `adauga_date_sensibile` e **oprită**: ar trimite lista clienților în cloud |
| **Local** | Serverul e conectat la AI-ul local (Qwen) | Toate uneltele, inclusiv adăugarea de clienți și cuvinte-cheie prin conversație |

Numele reale ale angajaților **nu** apar implicit nici în modul local. Raportarea pe persoană e o monitorizare mai invazivă, așa că o pornește antreprenorul explicit, după informarea angajaților (vezi [06 §8](06-solutie.md)) [V: de confirmat cu un jurist].

### 4.4 Unde rulează
Serverul MCP rulează **în firmă**, pe calculatorul antreprenorului sau pe serverul din birou, lângă baza de date cu evenimente. Nu e un serviciu al nostru în cloud [I]. Ce aplicații AI acceptă servere MCP locale și cum se conectează, **de verificat** pe documentația fiecăreia [V].

### 4.5 Teste noi
| # | Test | Criteriu [I] |
|---|---|---|
| T13 | Antreprenorul pune 10 întrebări obișnuite asistentului lui | Primește răspuns corect la cel puțin 9 |
| T14 | În modul cloud, căutăm în tot ce întoarce serverul MCP nume de clienți, nume de angajați și text de prompt | Zero apariții |

## 5. Ce s-a schimbat în diagrame
- **Cazurile de utilizare:**
  - antreprenorul „alege presetul” și „adaugă date sensibile pe categorii”;
  - „vede raportul lunar” devine „întreabă asistentul AI (prin MCP)”;
  - agentul are un pas nou, „verifică textul curățat cu Jev”;
  - AI-ul local e Qwen3.5-9B (sau Qwen3.8-27B pe server).
- **Fluxul de dezvoltare:** etapa 3 include verificarea Jev (T11, T12). Etapa 5 devine „preseturi, categorii proprii, server MCP” (T13, T14).
