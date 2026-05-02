# Job Application Assistant - Toteutussuunnitelma

## 1. Tavoite
Projektin tarkoitus on rakentaa paikallisesti ajettava Python-työkalu, joka analysoi työpaikkailmoituksen sisallon suhteessa hakijan CV:hen ja auttaa muodostamaan kohdennetumman hakemuksen. Tyokalu ei laheta dataa ulkoisiin palveluihin, vaan koko analyysi voidaan suorittaa paikallisesti yksityisyyden suojaamiseksi.

Tyokalu tuottaa kayttajalle nelja konkreettista lopputulosta:
- lista tyopaikkailmoituksesta tunnistetuista avainsanoista ja osaamisista
- vertailu siihen, miten hyvin samat teemat nakyvat CV:ssa
- suositukset siita, mita hakemuksessa kannattaa erityisesti korostaa
- luonnos osiosta "vahvuudet tahan rooliin"

## 2. Kayttajatarve ja arvo
Moni tyohakemus kaatuu siihen, etta hakija osaa paljon oikeita asioita, mutta ne eivat nay tarpeeksi selkeasti juuri kyseisen roolin kielella. Tyokalu ratkaisee taman ongelman kolmella tavalla:
- se auttaa tunnistamaan tyopaikkailmoituksen ydintermit nopeasti
- se osoittaa, missa kohtaa CV tukee roolia hyvin ja missa on katveita
- se auttaa muotoilemaan hakemuksen painotukset vakuuttavasti mutta konkreettisesti

Kayttajan saama arvo on ajansaatto, parempi osuvuus hakemuksiin ja yhtenaisempi tapa rakentaa roolikohtaisia hakemuksia.

## 3. MVP:n rajaus
Ensimmainen julkaisu kannattaa rajata selkeaksi komentorivityokaluksi. MVP:ssa keskitytaan siihen, etta ydinanalyysi toimii hyvin ilman raskaita riippuvuuksia.

MVP sisaltaa:
- tekstimuotoisen tyopaikkailmoituksen lukeminen tiedostosta tai suoraan syotteena
- tekstimuotoisen CV:n lukeminen tiedostosta tai suoraan syotteena
- avainsanojen poiminta tyopaikkailmoituksesta
- osaamisten ja teemojen osumien tunnistus CV:sta
- painotussuositusten generointi
- "vahvuudet tahan rooliin" -luonnoksen tuottaminen
- tulosten tulostus konsoliin ja tallennus Markdown-raportiksi

MVP ei viela sisalla:
- selainkayttoliittymaa
- pilvipalveluriippuvuuksia
- automaattista hakemuksen lahetysta
- monimutkaista koneoppimismallia
- PDF- tai DOCX-sisaanlukua ensimmaisessa vaiheessa, ellei se oteta erillisena laajennuksena

## 4. Toiminnalliset vaatimukset
Tyokalun tulee pystyä:
- lukemaan tyopaikkailmoituksen teksti UTF-8 TXT- tai Markdown-tiedostosta
- lukemaan CV:n teksti UTF-8 TXT- tai Markdown-tiedostosta
- puhdistamaan ja normalisoimaan tekstit analyysia varten
- tunnistamaan roolin kannalta keskeisia avainsanoja, teknologioita, pehmeita taitoja ja vastuuteemoja
- laskemaan, mitka avainsanat esiintyvat CV:ssa suoraan tai lahes vastaavina ilmaisuina
- erottelemaan vahvat osumat, osittaiset osumat ja puuttuvat teemat
- ehdottamaan 5-10 painotusta hakemustekstiin
- muodostamaan luonnoksen roolikohtaisesta vahvuusosiosta
- tallentamaan analyysin tiedostoksi jatkokayttoa varten

## 5. Ei-toiminnalliset vaatimukset
Ratkaisun tulee olla:
- paikallisesti ajettava, jotta arkaluonteinen CV-data pysyy omalla koneella
- selitettavissa, eli jokaisen ehdotuksen yhteydessa tulee olla perustelu tai viite loydettyyn tekstiin
- nopea, tavoite alle 3 sekuntia tavallisille tekstimassoille
- laajennettava, jotta uusia formaatteja ja analyysikerroksia voidaan lisata myohemmin
- testattava, jotta muutokset eivat riko analyysin peruslogiikkaa
- kielijoustava, jotta suomi- ja englanninkieliset ilmoitukset toimivat kohtuullisen hyvin

## 6. Kayttotapaukset
Keskeiset kayttotapaukset ovat:
- hakija syottaa yhden tyopaikkailmoituksen ja yhden CV:n ja pyytää analyysia
- hakija haluaa nopeasti listan ilmoituksen ydinsanoista
- hakija haluaa nahda, mitka asiat CV:ssa jo tukevat roolia
- hakija haluaa tiedon siita, mita kannattaa nostaa esiin motivaatiokirjeessa
- hakija haluaa valmiin ensiluonnoksen vahvuusosiosta, jota voi itse muokata

## 7. Ehdotettu arkkitehtuuri
Ratkaisu kannattaa jakaa kuuteen paakomponenttiin:
- ingestion: tiedostojen luku ja tekstin sisaanotto
- preprocessing: normalisointi, tokenisointi, stop-sanojen suodatus ja fraasien muodostus
- extraction: avainsanojen ja vaatimusteemojen poiminta tyopaikkailmoituksesta
- matching: vertailu CV:n sisaltoon ja osumien pisteytys
- recommendation: painotusten ja vahvuusluonnoksen generointi
- reporting: tulosten esitys konsolissa ja tiedostona

Tama rakenne mahdollistaa sen, etta analyysilogiikka, tekstinkasittely ja raportointi pysyvat erillisina ja helposti testattavina.

## 8. Tekstinkasittely ja analyysilogiikka
Perusputki toimii seuraavasti:
1. Luetaan tyopaikkailmoituksen teksti ja CV.
2. Muunnetaan teksti pienaakkosiksi ja poistetaan ylimaarainen valimerkki- ja whitespace-kohina.
3. Jaetaan teksti sanoihin ja 2-3 sanan fraaseihin.
4. Suodatetaan yleisimmat stop-sanat suomen ja englannin listoilla.
5. Tunnistetaan mahdolliset osaamistermit, teknologiat, vastuut ja pehmeat taidot.
6. Verrataan ilmoituksen termeja CV:n termeihin taysina ja lahein osumina.
7. Pisteytetaan teemat osuman vahvuuden, toistuvuuden ja kontekstin perusteella.
8. Muodostetaan suositukset ja luonnosteksti.

Avainsanojen poiminnassa kannattaa yhdistaa useita heuristiikkoja:
- taajuus suhteessa tekstin pituuteen
- esiintyminen otsikoissa ja luettelokohdissa
- tunnistetut teknologiatermit ja roolisanasto
- kaksisanaiset ja kolmisanaiset fraasit, kuten "project management" tai "asiakasrajapinta"
- ilmaukset, jotka esiintyvat vaatimusten yhteydessa, kuten "edellytamme", "toivomme", "required", "preferred"

## 9. Pisteytysmalli
Jokaiselle tunnistetulle teemalle voidaan laskea yhdistetty pistemaara esimerkiksi seuraavista osista:
- ilmoituksen relevanssipaino 0-5
- suora osuma CV:ssa 0-5
- osittainen tai synonyymiosuma 0-3
- kontekstipaino 0-2 sen mukaan, esiintyyko asia kokemuksen, saavutuksen tai vastuun yhteydessa

Tuloksena jokaiselle teemalle saadaan status:
- vahva osuma
- kohtalainen osuma
- puuttuva tai heikko osuma

Taman perusteella voidaan muodostaa myos kokonaiskuva siita, kuinka hyvin CV tukee kyseista roolia.

## 10. Suositusten muodostus
Suosituslogiikan tavoite ei ole keksia taitoja, joita CV ei sisalla. Sen sijaan sen tulee nostaa esiin asiat, joille loytyy tukea CV:sta mutta joita kannattaa korostaa paremmin hakemuksessa.

Suositukset voidaan jakaa kolmeen ryhmaan:
- korosta tata heti alussa: asiat, joissa CV tukee vaatimusta vahvasti
- konkretisoi esimerkillä: asiat, joissa osaaminen on olemassa mutta naytto kannattaa sanoittaa paremmin
- huomioi varovasti: asiat, joihin on osittainen osuma tai joista kannattaa kirjoittaa oppimishalukkuuden kautta

Jokaisen suosituksen yhteyteen tulee liittaa lyhyt perustelu, esimerkiksi mihin CV:n kohtaan ehdotus nojaa.

## 11. Vahvuudet tahan rooliin -luonnos
Luonnoksen generointi kannattaa rakentaa mallipohjaisesti. Teksti muodostuu seuraavista elementeista:
- avaava virke, joka peilaa roolin ydintarvetta
- 2-4 vahvuutta, jotka linkittyvat suoraan ilmoituksen avainteemoihin
- jokaiselle vahvuudelle lyhyt konkreettinen ankkuri CV:sta
- lopetus, joka sitoo osaamisen roolin tavoitteisiin

Esimerkkirakenne:
- Olen erityisen vahva roolissa, jossa korostuvat X, Y ja Z.
- Kokemukseni A:sta tukee tehtavan vastuualuetta B.
- Lisaksi taustani C:ssa auttaa tuomaan arvoa tilanteissa, joissa tarvitaan D:tä.
- Uskon, etta voisin tuoda rooliin sekä nopeaa kaynnistymiskykyä että kehittavaa otetta.

## 12. Ehdotettu projektirakenne
Projektin kansiorakenne kannattaa rakentaa seuraavasti:
- src/job_application_assistant/: varsinainen sovelluskoodi
- src/job_application_assistant/cli.py: komentoriviliittyma
- src/job_application_assistant/io.py: tiedostonluku ja syotteen hallinta
- src/job_application_assistant/preprocess.py: normalisointi ja tokenisointi
- src/job_application_assistant/extract.py: avainsanojen poiminta
- src/job_application_assistant/match.py: osumien laskenta ja pisteytys
- src/job_application_assistant/recommend.py: suositukset ja luonnostekstin generointi
- src/job_application_assistant/report.py: raportin muodostus
- tests/: yksikkö- ja integraatiotestit
- docs/: suunnitelmat, esimerkit ja tuotetut raportit

## 13. Komentoriviliittyman ehdotus
Ensiversioon sopiva kayttotapa:
- `python -m job_application_assistant analyze --job job.txt --cv cv.txt`
- `python -m job_application_assistant analyze --job job.md --cv cv.md --output report.md`
- `python -m job_application_assistant keywords --job job.txt`

Komentorivin tulisi tukea ainakin seuraavia valintoja:
- syotetiedostojen polut
- ulostuloraportin polku
- kieliasetus auto tai manual
- maksimiavainsanojen maara
- tulostusmuoto console tai markdown

## 14. Teknologiapaatokset
Suositeltu toteutusmalli vaiheeseen 1:
- Python 3.11+
- standardikirjasto ensisijaisena
- `argparse` tai `typer` komentoriville
- `dataclasses` tai `pydantic` rakenteisiin
- `pathlib` tiedostopolkujen hallintaan
- `re`, `collections` ja `difflib` perusanalyysiin

Vaiheen 2 mahdolliset lisat:
- `rapidfuzz` parempaan epätarkan osuman tunnistukseen
- `spacy` tai muu NLP-kirjasto, jos halutaan kehittyneempaa sanaluokka- tai entiteettitunnistusta
- `rich` raportoinnin parantamiseen konsolissa
- `jinja2` mallipohjien hallintaan

## 15. Toteutusvaiheet
Suositeltu eteneminen seitsemassa vaiheessa:
1. Projektirungon perustaminen ja CLI-sisaanmeno.
2. Tekstin luku, normalisointi ja stop-sanojen hallinta.
3. Avainsanojen ja fraasien poiminta tyopaikkailmoituksesta.
4. CV-vertailu, osumaluokittelu ja pisteytys.
5. Suosituslogiikka ja vahvuusluonnoksen generointi.
6. Markdown-raportin muodostus ja kaytettavyyden viimeistely.
7. Testit, esimerkkisyotteet ja dokumentaatio.

## 16. Testausstrategia
Testauksen tulee kattaa ainakin:
- tiedostonluku onnistuu eri tekstitiedostoilla
- normalisointi poistaa kohinaa rikkomatta merkitysta
- avainsanojen poiminta nostaa esiin odotetut termit tunnetuissa testisyotteissa
- vertailulogiikka erottaa vahvat, osittaiset ja puuttuvat osumat oikein
- suositusgeneraattori ei ehdota CV:n ulkopuolisia taitoja faktana
- luonnosteksti rakentuu ilman tyhjia tai ristiriitaisia lauseita

Lisaksi kannattaa tehda muutama integraatiotesti kokonaisilla esimerkkisyotteilla.

## 17. Tietosuoja ja turvallisuus
Koska CV ja tyohakemuksiin liittyva aineisto ovat arkaluonteisia, ratkaisu kannattaa suunnitella privacy-first-periaatteella:
- kaikki analyysi suoritetaan paikallisesti
- tiedostoja ei laheta ulkoisiin API-palveluihin oletuksena
- raportteihin ei lisata ylimaaraisia henkilötietoja automaattisesti
- mahdolliset lokit pidetaan minimaalisina
- poistettavat tai arkistoitavat raportit ovat kayttajan hallinnassa

## 18. Riskit ja hallintakeinot
Keskeiset riskit ovat:
- ilmoituksen kieli on epämääräinen tai markkinointihenkinen, jolloin oleelliset vaatimukset hukkuvat
- CV on liian lyhyt tai yleistasoinen, jolloin osumia on vaikea perustella
- synonyymit ja eri kirjoitusasut heikentavat osumatarkkuutta
- luonnosteksti alkaa kuulostaa liian geneeriselta

Hallintakeinot:
- yhdistetaan sana- ja fraasitasoinen analyysi
- kaytetaan epätarkan osuman vertailua hallitusti
- liitetaan jokaisen suosituksen yhteyteen perustelu
- pidetaan generointi mallipohjaisena ja faktasidonnaisena

## 19. Hyvaksyntakriteerit
Ensimmainen versio on valmis, kun:
- kayttaja voi antaa tyopaikkailmoituksen ja CV:n kahdesta tiedostosta
- tyokalu tuottaa listan keskeisista avainsanoista
- tyokalu tunnistaa, mitka teemat loytyvat CV:sta
- tyokalu antaa perustellut korostussuositukset
- tyokalu tuottaa kelvollisen vahvuusluonnoksen
- analyysi voidaan tallentaa Markdown-raportiksi
- ydinlogiikalle on olemassa automatisoidut testit

## 20. Jatkokehitys
Kun MVP toimii, seuraavat kehitysaskeleet ovat luontevia:
- PDF- ja DOCX-sisaanluku
- useiden CV-versioiden vertailu samaan ilmoitukseen
- useiden ilmoitusten vertailu samaan CV:hen
- selain- tai desktop-kayttoliittyma
- muokattavat kirjoitustyylit vahvuusluonnokselle
- ATS-yhteensopivuuden tarkistus
- erillinen tila suomen- ja englanninkielisille hakemuksille

## 21. Suositus seuraavaksi askeleeksi
Paras seuraava askel on rakentaa ensin toimiva CLI-MVP. Se antaa nopeasti oikeaa palautetta analyysilogiikasta ja pitaa teknisen riskin matalana. Kun ydinputki toimii hyvin tekstitiedostoilla, formaattituki ja kayttoliittyma voidaan lisata turvallisesti paalle.
