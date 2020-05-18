# WhatchaWannaWatch
## Live Site [Update]
https://whatcha-wanna-watch.herokuapp.com/


## Tutorial
Netflix doesn't display movies ratings, probably because some intern broke the code<br><br>
Despite the inconvenience caused by having to look up each movie's rating, this app offers to generate a list of current available Netflix movies and their IMDb ratings, ordered from the highest to lowest.<br><br>
`git clone` this repo on your machine and run `python3 getMoviesSorted.py [yourPreferredGenre]` to find out what you wanna watch tonight<br>
<br>
yourPreferredGenre options:
- all
- action
- children
- classics
- comedies
- dramas
- faith
- horror
- musicals
- romantic
- scifi
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
fetch movie posters for visual convenience<br>
iOS/Android application development<br>

## Output Example
python3 getMoviesSorted.py action<br><br>
Inception: 8.8<br>
The Good, the Bad and the Ugly: 8.8<br>
The Matrix: 8.7<br>
Avengers: Infinity War: 8.5<br>
Spider-Man: Into the Spider-Verse: 8.4<br>
Inglourious Basterds: 8.3<br>
Kung Fu Hustle: 7.7<br>
Lethal Weapon: 7.6<br>
End of Watch: 7.6<br>
Sherlock Holmes: 7.6<br>
Train to Busan: 7.5<br>
Ala Vaikunthapurramuloo: 7.2<br>
The Foreigner: 7.0<br>
Paid in Full: 7.0<br>
Bad Boys: 6.9<br>
What Happened to Monday: 6.9<br>
A.X.L.: 6.9<br>
Bloodsport: 6.8<br>
The Decline: 6.7<br>
Lethal Weapon 3: 6.7<br>

