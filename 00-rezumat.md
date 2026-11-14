# 00 · Rezumat

> Data research-ului: **2026-11-14**. **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** ipoteză · **[V]** de validat la interviuri.
> Fișiere: [01 Clienți](01-clienti.md) · [02 Date sensibile](02-date-sensibile.md) · [03 Anonimizare](03-anonimizare.md) · [04 Matrice](04-matrice-decizie.md) · [05 Interviuri](05-ipoteze-si-interviuri.md)

## Răspunsuri scurte la cele 9 întrebări

**1. Cui vindem? Cine decide și cine plătește?**
[I] Patronului unei firme de 10–100 de oameni dintr-o profesie reglementată. El plătește și răspunde. MSP-ul (firma IT externă) e canalul: instalează și recomandă. [F] Bitdefender își vinde modulul AI tocmai „organizațiilor și MSP-urilor” (S33). [V] Cine a ales ultimul soft de securitate?

**2. Ce firme au cea mai mare durere?**
[I] Ca obligație juridică: avocatură și clinici (secret profesional + art. 9). Ca potrivire cu produsul: **contabilitatea**, pentru că datele ei sunt structurate (CNP, IBAN, CUI, sume) și se pseudonimizează bine. Piața: 44.894 firme mici și 7.659 mijlocii în RO [F] S3. Doar 5,2% din firmele RO folosesc oficial AI [F] S1.

**3. Cu ce lucrează, pentru ce ar folosi AI, ce obligații au?**
Tabelul segment × date × obligații × utilizări e în [01 §3](01-clienti.md). Obligații principale [F]:
- GDPR, inclusiv art. 9 și Legea 190/2018 pentru CNP (S13);
- secret profesional: avocați S7–S8, medici S10–S11 (codul CMR are din 2026 un **articol despre AI**, art. 36), contabili S9;
- Cod penal art. 227 (S14);
- AML (Legea 129/2019) pentru contabili, avocați și agenți imobiliari (S12);
- secret comercial (S15).

**4. Ce nu trebuie să ajungă NICIODATĂ într-un AI public?**
[I] Parole și chei; date de sănătate legate de o persoană; copii de acte; date penale; cod sursă și secrete comerciale sub NDA; strategii juridice sau comerciale pe cazuri recognoscibile; rapoarte AML. Detalii în [02 §4](02-date-sensibile.md).

**5. Ce înseamnă „a anonimiza”?**
[F] Anonimizare = persoana nu mai e identificabilă cu mijloace rezonabile, iar GDPR nu se mai aplică (considerentul 26, S17). Pseudonimizare = identificarea cere informații suplimentare păstrate separat, iar datele **rămân personale** (art. 4(5); EDPB 01/2025, S19).

Două noutăți schimbă analiza:
- CJUE C-413/23 P (09.2025): datele pseudonimizate pot fi nepersonale **pentru destinatarul** care nu poate reidentifica (S20);
- EDPB Ghidurile 02/2026 (proiect): criteriile *fără izolare, fără corelare, fără deducție*, inclusiv pentru deducțiile obținute prin prompturi AI (S21).

**→ Ce facem noi la GALBEN e pseudonimizare, nu anonimizare.**

**6. Limitele anonimizării?**
[F] Combinațiile de atribute reidentifică: 87% din populația SUA după cod poștal + sex + data nașterii (S22); 99,98% cu 15 atribute, după un model (S23). Textul liber conține identificatori indirecți pe care NER nu-i prinde (S24). [I] În contracte, cod sursă, oferte și strategii, **conținutul însuși** e secretul.

**7. Ce se poate anonimiza util?**
[I] Nume (în texte scurte), IBAN, CUI, e-mail, telefon, număr de înmatriculare: etichete reversibile. CNP: **se elimină** (minimizare). Sume: etichete sau scalare (nu la praguri fixe). Date calendaristice și vârste: generalizare.

**8. Ce nu se poate anonimiza util?**
[I] Date de sănătate cu context, documente scanate, contracte negociate, cod sursă, strategii de preț, strategii procesuale, tabele mari cu date de clienți.

**9. Politica VERDE/GALBEN/ROȘU.**
În [04](04-matrice-decizie.md), 22 de tipuri de date. Două schimbări propuse față de ipoteza inițială:
- ROȘU **nu taie automat accesul**, ci escaladează treptat, cu decizie umană;
- VERDE **nu salvează textul** promptului.

## Cele mai riscante 3 ipoteze ale noastre

1. **H1: problema există la scară în IMM-urile românești.** Toate cifrele de „shadow AI” vin de la vânzători (S29–S31) și din afara RO. Adoptarea oficială în RO e 5,2% (S1). Dacă angajații firmelor mici nu folosesc AI cu date reale, n-avem client.
2. **H3: GALBEN păstrează răspunsul util pentru sarcinile reale.** În segmentele cu cea mai mare durere (avocați, medici), sarcinile valoroase sunt pe ROȘU. **Paradoxul: unde durerea e mare, produsul blochează; unde produsul ajută (contabilitate), durerea juridică e mai mică.**
3. **H2: patronii plătesc pentru asta, nu doar își fac griji.** Principalul motiv de neadoptare a AI în UE e lipsa expertizei (70,89%), nu protecția datelor (48,83%) (S2). Abonamentele AI de business rezolvă deja antrenarea pe date (S26–S28) la un preț cunoscut.

---

## Verificarea finală: critica severă

### A. Afirmații din brief care nu mai stau în picioare
- **„AI Act cere cunoștințe suficiente din februarie 2025”: parțial depășit.** Regulamentul (UE) 2026/1744 a rescris art. 4. Din 27.07.2026 obligația e să „ia măsuri pentru a sprijini” dezvoltarea cunoștințelor AI, **fără a garanta un nivel**, iar art. 4 n-a avut niciodată sancțiune proprie [F] S4. **Nu-l folosim ca argument principal de vânzare.** Rămâne cel mult un argument secundar: produsul care explică angajatului *de ce* a fost blocat poate fi o „măsură” documentabilă.
- **„Anonimizare” în pitch: greșit juridic.** E pseudonimizare (03 §1).

### B. Locuri unde soluția nu rezolvă problema
1. **Ocolirea pe telefon.** Extensia de browser și hook-urile acoperă doar dispozitivele firmei. Angajatul blocat folosește aplicația ChatGPT de pe telefonul personal, fotografiază ecranul și i-l dă AI-ului. Tăierea automată a accesului **accelerează** asta [I]. Toate soluțiile din piață au aceeași limită (Purview acoperă doar Edge și extensia, S32), deci nu e un dezavantaj față de concurență, dar trebuie spus deschis.
2. **Aplicațiile desktop și mobile.** Interceptarea traficului aplicațiilor native (ChatGPT desktop, Copilot în Office) e fragilă tehnic. Fiabilitatea hook-urilor: **necunoscută, de testat** [V].
3. **Segmentele cu durere mare primesc valoare mică** (paradoxul din H3).
4. **Produsul nostru e el însuși o prelucrare de date.** Citim toate prompturile angajaților, deci intrăm sub regulile de monitorizare a angajaților. Probabil e nevoie de o evaluare de impact (DPIA, **de verificat**), de informarea angajaților și de procesare 100% locală [I]. Dacă trimitem prompturile în cloud ca să le clasificăm, devenim noi scurgerea.
5. **Calitatea detectării pe limba română:** necunoscută. Un fals negativ (un nume ratat) anulează promisiunea. Un fals pozitiv (prea multe ROȘU) face produsul să pară o interdicție.
6. **Restaurarea în răspuns** se strică dacă AI-ul modifică etichetele sau calculează cu sume scalate (03 §3.4).

### C. Concurență subestimată
- **Bitdefender (românesc, cu canal MSP)** a lansat în 09.2026 descoperirea și blocarea instrumentelor AI (S33). **ESET** inspectează fișierele trimise la AI (S34). Microsoft Purview face avertizare și blocare (S32). Pseudonimizarea reversibilă există în gateway-uri (S36). **Diferențiatorul nostru (pseudonimizare reversibilă pentru utilizatorul final, în română, la preț de IMM) e îngust și poate fi copiat de Bitdefender.** Răspunsul nostru la întrebarea „de ce nu Bitdefender?” trebuie construit.
- **Abonamentul AI de business** e alternativa ieftină și simplă. Nu rezolvă secretul profesional și minimizarea, dar mulți patroni pot considera că e „suficient” [V].

### D. Contradicții verificate între fișiere
- 01 îl numește pe patron cumpărător, iar 05/H5 pune MSP-ul ca posibil decident. Am lăsat-o intenționat deschisă (H5).
- 02 marchează „situația fiscală a clientului” ca ANON, iar 04 (rândul 11) cere ROȘU dacă nu se poate generaliza contextul. Sunt consecvente: depinde de context.
- Cifrele Harmonic (4,37% din prompturi; ~22%–26,38% din fișiere) apar la fel în 01, 04 și surse.md.

### E. Afirmații cu sursă slabă (de reverificat înainte de pitch)
- Toate articolele de lege citite prin reproduceri sau comentarii (S7, S9, S14, S15, S17) trebuie confruntate cu legislatie.just.ro și EUR-Lex.
- AI Act Anexa III (recrutare = risc ridicat): din cunoștințe, nu verificat în această sesiune.
- Prețul ChatGPT Business (~25 $/utilizator/lună): din presă.
- Statutul amenzii Garante (suspendată?): neclar (S38).

## Întrebări deschise
1. Secretul profesional (avocat, medic, expert contabil) permite trimiterea **pseudonimizată** către un furnizor AI cu contract de prelucrare? → de întrebat un jurist sau mentorii.
2. Câte firme din cele 7 segmente au 10–100 de angajați? → INS TEMPO pe cod CAEN.
3. Cât folosesc AI, concret, angajații din firmele mici românești și pe ce conturi? → interviuri (05 B).
4. Ce procent din sarcinile reale ar ieși GALBEN vs. ROȘU? → cerem 20 de exemple reale (fictivizate) de la 3 firme.
5. Ce face MSP-ul azi când un client întreabă de AI? → interviuri (05 C).
6. Cât de bine detectează instrumentele open source (Presidio + modele pentru română) CNP, nume declinate și CUI? → test tehnic pe un set de date fictiv.
7. Acceptă patronii (și angajații) ca un instrument să citească local fiecare prompt?
8. Ce ne diferențiază de Bitdefender GravityZone AIVC dacă Bitdefender adaugă inspecția prompturilor?
