 # Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista luoda reseptejä, joista näkee tarkemmat speksit makroista ja samalla sovellus ehkä antaa ohjeita. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, 
joilla kaikilla on omat reseptit. Raaka-aineet lisätään yksi kerrallaan samalla, kun lisätään resepti ellei raaka-ainetta löydy jo sovelluksesta.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli peruskäyttäjä. Myöhemmin sovellukseen saatetaan lisätä laajemmat oikeudet omaava pääkäyttäjä.

## Käyttöliittymäluonnos

Sovellus koostuu viidestä eri näkymästä

![](./kuvat/kayttoliittyma-hahmotelma.png)

### Näkymä 1 Kirjautuminen

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirtyä uuden käyttäjän luomisnäkymään tai onnistuneen kirjautumisen yhteydessä kirjaantuneen käyttäjän reseptilistaan.

### Näkymä 2 Käyttäjän luonti

Voidaan luoda uusi käyttäjä ja siihen liitettävä salasana, jonka jälkeen palataan näkymään 1.

### Näkymä 3 Reseptilista

Reseptejä on 5 per sivu, sovellus luo uuden sivun joka kuudennella reseptillä. Sivuissa on sama reseptinäkymä, mutta eri reseptit riippuen sivuista. Sivuissa voi navigoida painamalla sivulinkkejä.
Uuden reseptin voi lisätä tai vanhaa reseptiä voi editoida. Molemmista napeista päästään reseptin editointinäkymään.

### Näkymä 4 Resepti

Tässä näkymässä voidaan voi lisätä/editoida raaka-aineita. Tässä näkymässä näkyy myös yhteenlasketut makrot. Näkymässä voidaan tallenaa muutokset tai poistaa resepti,
Josta päästään takaisin näkymään 3. Lisäämällä/editoimalla raaka-ainetta päästään viimeiseen näkymään.

### näkymä 5 Raaka-aineet

Tässä näkymässä voidaan lisätä/editoida valmiina asetettuihin spekseihin jokin numeraalinen luku. Näkymässä on add tai delete ingridient, jota painamalla sovellus laskee uudelleen reseptin
speksien summan, jotta näkymässä 4 olisi oikeat yhteenlasketut speksit.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ja siihen yhdistettävän salasanan.
  - Käyttäjätunnuksen täytyy olla unique ja pituudeltaan vähintään 3 merkkiä.
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, niin järjestelmä lähettää virheilmoituksen kirjautuvalle käyttäjälle.

### Kirjautumisen jälkeen

- Käyttäjä näkee omat reseptit listan muodossa. Sivua voi vaihtaa, josta päästään listan seuraavaan 5 reseptiin.
- Käyttäjä voi luoda uuden reseptin, jonka seurauksena listaan tulee uusi resepti, jota voi muokata.
  - Luotu resepti näkyy ainoastaan sen luoneelle käyttäjälle
- Käyttäjä voi kirjautua ulos näkymässä 3.
- Käyttäjä voi poistaa reseptin näkymässä 4, jolloin resepti häviää listalta.
- Käyttäjä voi muokata reseptien raaka-aineiden nimiä tai nähdä reseptin tarkemmat tiedot näkymässä 4.
- Käyttäjä voi muokata raaka-aineiden speksit laittamalla tyhjään tekstikenttään, jokin numeraalinen luku. Tekstikentän jäädeessä tyhjäksi järjestelmä sijoittaa automaattisesti siihen luvun 0
  Laskiessa yhteen reseptin speksejä. Järjestelmä ilmoittaa virheestä, jos tekstikenttään sijaitetaan muuta kuin INT.
- Käyttäjä voi lisätä/poistaa reseptiin raaka-aineen näkymässä 5, jonka seurauksena järjestelmä laskee yhteen tarkemmat speksit.

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Reseptien lähempi tarkastelu
- Reseptien jakaminen muille käyttäjille.
- Reseptien arvostelu ja kommentointi.
- Reseptien järjestely mm. aakkosjärjestykseen tai arviointiin perustuvaan.
- Aktiivisuuden mukaan, voidaan antaa eri käyttäjätasoja, jossa on laajemman oikeudet.
- Käyttäjätunnuksen poisto, jonka seurauksena poistetaan myös käyttäjään liitettävät reseptit.
