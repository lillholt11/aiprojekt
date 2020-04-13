
  <p align="center">
    Ett program som genererar opopulära åsikter som sedan postas varje timme på reddit!

## Innehållsförteckning

* [Om projektet](#Om-projektet)
* [Länkar(#Länkar)
* [Filer](#Filer)
* [Köra programmet](#Köra-programmet)
  * [Förarbete](#förarbete)
  * [Test av programmet](#Test-av-programmet)
  * [Eget dataset](#Eget-dataset)
  * [Starta programmet](#Starta-programmet)
* [Utvärdering](#Utvärdering)

## Om projektet

Projektet handlar om att först hämta ett stort dataset med opopulära åsikter. För att göra detta så behöver man webscrapea och hämta data. Sedan så tränar man en GPT-2 model (textgenererande ai). Denna model används sedan till att skapa ett antal olika opopulära åsikter. Den opopulrä åsikt som bäst passar in på reddit postas sedan till reddit. Detta görs i språket **python**. För att webscrape och posta till reddit så används biblioteket **praw**.

För att programmet ska fortsätta köras hela tiden så hostar jag det på **heroku**.

### Länkar
Nedan finns länkar listade som användts eller har varit till hjälp under projektets gång.
* [Praw tutorial](https://medium.com/@plog397/webscraping-reddit-python-reddit-api-wrapper-praw-tutorial-for-windows-a9106397d75e)
* [Twitter bot tutorial](https://www.youtube.com/watch?v=RMQ4f6YXRTM)
* [Google colab](https://colab.research.google.com/drive/1EPNe3Q8IwQDQlS3fBPO9ikSq5Dy7hWpc)
* [Heroku](https://heroku.com)

## Filer
* **Procfile** - Fil som innehåller alla dynos, behövs för att hosta på heroku
* **main.py** - kör hela programmet
* **requirements.txt** Fil som innehåller alla bibliotek, behövs för att hosta på heroku
* **scrape.py** - Fil som scrapear vald subreddit och generar ett dataset
* **server.py** - En server, behövs för att hosta till heroku

## Köra programmet
Du behöver följande program installerade på din dator.

* Python 3.7 64 bit med pip

### Förarbete
Installera följande biblotek till python

* tensorflow 1.15.0 ``` pip install tensorflow==1.15.0`````
* requests ``` pip install requests```
* gpt-2-simple ``` pip install gpt-2-simple```

Klona sedan denna github till en map på din dator. 

### Test av programmet

Om du vill använda mitt dataset så hoppa till * [Starta programmet](#Starta-programmet)

### Eget dataset

Om du vill göra ett eget dataset, modifiera och kör filen **scrape.py** för att göra ett dataset från egen vald subreddit. Det skapas då en fil **data.txt**, ladda upp den till [google colab](https://colab.research.google.com/drive/1EPNe3Q8IwQDQlS3fBPO9ikSq5Dy7hWpc) och gör en egen model som du sparar ned till google drive.

Kör filen **scrape.py**

* öppna cmd i mappen
* ``` python scrape.py``

Modifiera sedan main.py så att den hämtar rätt model från din google drive.

### Starta programmet
Kör filen **main.py**

* öppna cmd i mappen
* ``` python main.py```

## Utvärdering

### Problem

### Förbättringar
