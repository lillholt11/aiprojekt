
  <p align="center">
    Ett program som genererar opopulära åsikter som sedan postas varje timme på reddit!

## Innehållsförteckning

* [Om Projektet](#om-projektet)
  * [Byggd Med](#byggd-med)
* [Börja](#börja)
  * [Förarbete](#förarbete)
  * [Drive](#drive)
  * [Träning](#träning)
  * [Träning från början](#träning-från-början)
  * [Träning från påbörjad träning](#träning-från-påbörjad-träning)
* [Användning](#användning)
* [Problem](#problem)

## Om Projektet

Projektet handlar om att först hämta ett stort dataset med opopulära åsikter. För att göra detta så behöver man webscrapea och hämta data. Sedan så tränar man en GPT-2 model (textgenererande ai). Denna model används sedan till att skapa ett antal olika opopulära åsikter. Den opopulrä åsikt som bäst passar in på reddit postas sedan till reddit. Detta görs i språket **python**. För att webscrape och posta till reddit så används biblioteket **praw**.

### Länkar
Nedan finns länkar listade som användts eller har varit till hjälp under projektets gång.
* [Praw tutorial](https://medium.com/@plog397/webscraping-reddit-python-reddit-api-wrapper-praw-tutorial-for-windows-a9106397d75e)
* [Twitter bot tutorial](https://www.youtube.com/watch?v=RMQ4f6YXRTM)
* [Google colab](https://colab.research.google.com/drive/1EPNe3Q8IwQDQlS3fBPO9ikSq5Dy7hWpc)
* [Heroku](https://heroku.com)

## Köra programmet

### Förarbete

Börja med att ladda ned alla filer från githuben
```sh
%cd /content/
!git clone https://github.com/abbbringu/Project_Edward
!mkdir Music
!mkdir Raw
!mkdir Images
%tensorflow_version 1.x
```

### Drive

För att koppla colab med drive använder vi:
```sh
from google.colab import drive
drive.mount('/content/drive')
# drive.mount("/content/drive", force_remount=True)
%cd /content/drive/My Drive/
!mkdir STYLE-GAN
%ls
%cd /content

!ln -s "/content/drive/My Drive/STYLE-GAN" /STYLE-GAN
%cd /STYLE-GAN
%ls
```
Samtidigt skapar vi en mapp "STYLE-GAN" och gör en förkorning från /content/drive/My Drive/STYLE-GAN till /STYLE-GAN

### Eget Dataset

För att göra vårt eget dataset måste vi först ha bilder. Gör en mapp i STYLE-GAN som heter "Music" i google drive. Ta bort filer som slutar på ".MID" eller (".MIDI"). Koden kan endast ta in ".mid" filer. Sedan kör vi koden midi2img-py. Alla bilder borde ligga i /content/Raw. Bilderna i /Raw kommer ut i storlek 100x106 och därför behöver vi resize_img.py vilket gör om de till 256x256. Bilderna hamnar då i Images. 

När vi har bilderna använder vi:
```sh
%cd /content/Project_Edward/Stlye-Gan
!python dataset_tool.py create_from_images (Path till vart datan ska sparas) (/content/Images/)
```
Eftersom stylegan använder sig utav tfrecord måste vi konvertera bilderna. (Startkt rekomenerat att bilderna sparas i driven i en mapp som heter data)

### Träning

Träningen är från början inställd på att träna en ny model i res 256x256. Den är även inställd på att ta ocn spara datan på driven. Det kan anändras beroende på vart du vill ta och spara filerna. Allt finns i /content/Stlye-Gan/config.py
```sh
result_dir = '/STYLE-GAN/results' #Där resultaten sparas
data_dir = '/STYLE-GAN' #Där mappen med tfrecord filerna finns
```
I /content/Stlye-Gan/Train.py Måste det om du inte har en map i drive/STYLE-GAN som heter "data", inte har bilder i 256x256, vill träna med mirror eller vill använda mer än 1 gpu. Om inte kan du ignorera det här stycket.
Du kan hita koden under vid rad 35-36
```sh
35  # Dataset.
36  desc += '-custom';     dataset = EasyDict(tfrecord_dir='data', resolution=256);              train.mirror_augment = False
```
#### Träning från början
Om du vill träna från början kan du lämna content/Style-Gan/training/training_loop.py för det mesta i fred. Men en sak kan som kan ändras är totala träningar. Du hittar det vid rad 129:
```sh
   129    total_kimg = 15000,    # Total length of the training, measured in thousands of real images.
```
Det finns även andra inställningar som kan vara bra att ha på eller av beroende på anvädningen.

#### Träning från påbörjad träning
För att starta en träning från en påbörjad träning behöver du ändra 2 saker i content/Style-Gan/training/training_loop.py Du måste först ange vart din senaste pkl fil är. De lär vara någon stans (driven) STYLE-GAN/results/00009-sgan-custom-1gpu/network-snapshot-003765.pkl
Du lägger pathen i:
```sh
   136    resume_run_id = STYLE-GAN/results/00009-sgan-custom-1gpu/network-snapshot-003765.pkl
```
Och sedan måste du även ändra hur långt den kom (I det här fallet 3765):
```sh
   138    resume_kimg = 3765,      # Assumed training progress at the beginning. Affects reporting and training schedule.
```



<!-- USAGE EXAMPLES -->
## Användning

För att använda ai och för att producera en genererad bild använder vi invoke scriptet från stylegan. Det som behövs är pathen till apk filen.


```sh
%cd /content/Project_Edward/Stlye-Gan
!python invoke.py \
    --model_file '/content/stylegan-pokemon/Weights/MichaelFriese10_pokemon.pkl'
```

Bilderna vi får ut måste vi ändra till 100x106 och sedan köra in den i img2midi sciptet. Vi måste även justrera  bilderna så vi får svarta och via pixlar. Vi måste sätta en treshold för att sätta pixlarna till antingen vit eller svart. (Koden finns inte)
Sists ändrar vi midi till mp3:

```sh
!sudo apt-get install timidity
!timidity test.mid -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k test.mp3
```


## Problem
Scripten img2midi, midi2img och resize_img fungerar inte i google colab. 
För tillfället fungerar det inte att generera bilder från vikterna.

