# 04 · Matricea de decizie VERDE / GALBEN / ROȘU

> **[F]** faptă cu sursă ([surse.md](surse.md)) · **[I]** ipoteză (matricea întreagă e propunerea noastră și trebuie validată) · **[V]** de validat

## 1. Matricea

„Se poate anonimiza” = se poate **pseudonimiza local** astfel încât răspunsul AI să rămână util (vezi [03](03-anonimizare.md)).

| # | Tip de date | Se poate anonimiza? | Tehnica | Riscul rămas | Decizie |
|---|---|---|---|---|---|
| 1 | Text generic fără date despre persoane sau firme („explică-mi art. 25 din Codul fiscal”) | n/a | Niciuna | Neglijabil | 🟢 VERDE |
| 2 | Cod sau formule fără logică de business (o formulă `VLOOKUP`, un regex) | n/a | Niciuna | Mic | 🟢 VERDE |
| 3 | Nume de persoane în text scurt și generic | Da | Etichete reversibile `[PERSOANA_n]` | Context; declinări greșit detectate [I] | 🟡 GALBEN |
| 4 | CNP | Da, dar **de obicei nu e nevoie de el** | **Eliminare** (minimizare); etichetă doar dacă sarcina îl cere | Primele 7 cifre dezvăluie sexul și data nașterii [F] S40 | 🟡 GALBEN (eliminat implicit) |
| 5 | IBAN, număr de card | Da | Etichetă `[IBAN_n]` | Mic | 🟡 GALBEN |
| 6 | CUI, nume de firmă client | Da | Etichetă `[FIRMA_n]` | Firmele mari sau unice sunt recognoscibile din context | 🟡 GALBEN |
| 7 | E-mail, telefon, adresă | Da | Etichetă | Mic | 🟡 GALBEN |
| 8 | Număr de înmatriculare, serie de șasiu | Da | Etichetă | Mic | 🟡 GALBEN |
| 9 | Sume (facturi, salarii, datorii) | Parțial | Etichetă `[SUMA_n]` dacă AI-ul nu calculează; **scalare** dacă e nevoie de proporții | Calculele cu praguri fixe se strică [I] | 🟡 GALBEN |
| 10 | Date calendaristice legate de o persoană (data nașterii, a internării) | Parțial | Generalizare (lună/an) sau deplasare constantă | Combinate cu alte atribute, reidentifică [F] S22 | 🟡 GALBEN |
| 11 | Vârstă + localitate + profesie în același text | Parțial | Generalizare (interval, regiune) | Individualizare [F] S18 S23 | 🟡 GALBEN dacă se generalizează; altfel 🔴 |
| 12 | Tabel Excel cu date de clienți (sute de rânduri) | Parțial | Etichete pe coloane + date sintetice | Volum mare; o coloană ratată = scurgere masivă | 🔴 ROȘU implicit; 🟡 doar cu coloane recunoscute 100% [I] |
| 13 | Date de sănătate legate de o persoană (inclusiv indirect) | Nu util | — | Art. 9 + secret medical [F] S10 S11 | 🔴 ROȘU |
| 14 | Imagini medicale, copii de acte de identitate, documente scanate cu semnături | Nu | — | OCR incomplet; biometrie | 🔴 ROȘU |
| 15 | Date penale | Nu | — | GDPR art. 10 | 🔴 ROȘU |
| 16 | Strategie juridică pe un caz concret | Nu | — | Secret profesional absolut [F] S7 | 🔴 ROȘU |
| 17 | Contract negociat (M&A, cesiune, clauze de preț) | Nu | — | Conținutul e secretul [I] | 🔴 ROȘU |
| 18 | Cod sursă al clientului sau proprietar | Nu | — | Secret comercial, NDA [F] S15 S37 | 🔴 ROȘU |
| 19 | Parole, chei API, tokenuri, `.env` | Nu (și nu e nevoie) | Eliminare | — | 🔴 ROȘU |
| 20 | Strategie de preț, ofertă la licitație, plan de restructurare | Nu | — | Secret comercial | 🔴 ROȘU |
| 21 | Rapoarte AML / ONPCSB | Nu | — | Legea 129/2019 [F] S12 | 🔴 ROȘU |
| 22 | CV-uri pentru selecție automată | Parțial (identificatorii) | Etichete + eliminarea vârstei, sexului, fotografiei | Decizia automată = AI Act risc ridicat (**de verificat**) | 🟡 pentru redactare; 🔴 pentru decizia de selecție |

## 2. Politica propusă

### 🟢 VERDE: trece normal
- Niciun identificator detectat și niciun cuvânt-cheie din listele ROȘU.
- **Se înregistrează doar metadate** (oră, aplicație, categorie), **fără textul promptului**. [I] Altfel produsul nostru devine el însuși un risc GDPR, pentru că monitorizează angajații (art. 88, Codul muncii). [V]

### 🟡 GALBEN: pseudonimizare automată
1. Detectare locală, pe dispozitiv: CNP, IBAN, CUI, e-mail, telefon, nume, sume.
2. **Minimizare înainte de pseudonimizare:** ce nu e necesar pentru sarcină (CNP-ul, data nașterii) se elimină.
3. Înlocuire cu etichete; tabelul de corespondență rămâne **local, criptat, șters la finalul sesiunii**.
4. Restaurare în răspuns. Dacă restaurarea eșuează (eticheta a fost modificată de AI), angajatul vede răspunsul cu etichete și un avertisment.
5. Angajatul **vede ce s-a înlocuit** înainte de trimitere. Asta face parte din pregătirea AI cerută de AI Act art. 4 [F] S4 [I].

### 🔴 ROȘU: redirecționare către AI-ul local (sau blocare)
0. **Actualizare:** dacă firma are un AI local (Qwen, Llama pe calculator sau pe un server din birou), angajatul primește butonul **„Deschide în AI-ul local”**, cu textul deja încărcat, transferat prin agentul local, nu prin URL. Parolele și cheile rămân blocate oricum. Detalii în [06 §11b](06-solutie.md).
1. Fără AI local, trimiterea e blocată, iar angajatul vede **de ce** („conține date de sănătate legate de un pacient”) și **ce alternativă are** (instrumentul aprobat de firmă, o versiune generică a întrebării, întrebarea pusă fără date).
2. Angajatul poate cere o **excepție motivată**, aprobată de patron sau de DPO.
3. **Propunem să înlocuim regula „taie accesul la AI după ignorare”** cu o escaladare treptată:
   - prima dată: blocare + explicație;
   - repetat: notificare către responsabil;
   - abuz deliberat: suspendare temporară, decisă **de un om**, nu automat.

   Motivul: tăierea automată împinge angajații spre telefonul personal, unde nu avem niciun control (vezi critica din [00](00-rezumat.md)). [I] [V]

## 3. Reguli de prudență [I]
- **Când nu e sigur, agentul alege culoarea mai strictă.** Un fals pozitiv costă timp; un fals negativ costă o amendă sau secretul profesional.
- **Pragurile depind de segment:** o clinică pune „date de sănătate” pe ROȘU; o agenție imobiliară pune „sume” pe VERDE.
- **Fișierele încărcate** sunt cel puțin GALBEN implicit. Datele vânzătorilor arată că o parte importantă a fișierelor trimise conțin date sensibile: ~22% (T2 2025) și 26,38% (T3 2025) după Harmonic [F] S29, **afirmație de vânzător**.

## 4. Ce trebuie validat
- [V] Acceptă patronii ca un instrument să *citească* prompturile angajaților, chiar și local?
- [V] Câte trimiteri ar ajunge pe ROȘU într-o zi tipică? Dacă sunt peste ~20%, produsul e perceput ca interdicție. Pragul de 20% e o ipoteză, nu o cifră cunoscută.
- [V] Ar accepta un avocat sau un medic GALBEN pentru datele lui, sau consideră orice trimitere drept divulgare?
