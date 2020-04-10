# WhatchaWannaWatch

## Tutorial
Netflix doesn't display movies ratings, probably because some intern broke the code<br><br>
Despite the inconvenience caused by having to look up each movie's rating, this app offers to generate a list of current available Netflix movies and their IMDb ratings, ordered from the highest to lowest.<br><br>
`git clone` this repo on your machine and run `python3 getMoviesSorted.py [yourPreferredGenre]` to find out what you wanna watch tonight<br>
<br>
yourPreferredGenre options as of now:
- all
- action
- children
- classics
- comedies
- crime
- cult
- documentary
- dramas
- faith
- history
- horror
- independent
- international
- LGBTQ
- musicals
- romantic
- scifi
- nature
- sports
- standup
- thriller

## Dependencies
IMDb API:<br>
http://www.omdbapi.com/<br>
Generate your own API key and place in `apikey.py` [here](http://www.omdbapi.com/apikey.aspx)<br>

Beautiful Soup:<br>
HTML Parser

## Future Improvements & Plans
iOS/Android application development

## Output Example
python3 getMoviesSorted.py thriller<br><br>
The Invisible Guest: 8.1<br>
Freaks: 7.9<br>
The Hateful Eight: 7.8<br>
Road to Perdition: 7.7<br>
El Camino: A Breaking Bad Movie: 7.4<br>
Limitless: 7.4<br>
Shot Caller: 7.3<br>
The Platform: 7.0<br>
Bird Box: 6.6<br>
Fractured: 6.3<br>
1922: 6.3<br>
93 Days: 6.1<br>
A Fall from Grace: 5.8<br>
In the Tall Grass: 5.4<br>
The Silence: 5.3<br>
The Roommate: 4.8<br>
The Ghost Who Walks: 4.5<br>
Secret Obsession: 4.3<br>
Pretty Little Stalker: 3.0<br>
