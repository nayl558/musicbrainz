# Music Brainz Microservice

The Music Brainz Microservice is a Django-based application that provides an HTTP API endpoint for searching artists on the MusicBrainz.org service and retrieving information about artists and their releases.



## Installation

### Prerequisites
Before getting started, make sure you have Python and pip installed on your system. If you haven't installed them yet, you can follow these instructions:

### Install Python: 
Download and install Python from the official website. Follow the installation instructions for your operating system.
### Install pip: 
Pip is included by default with Python versions 3.4 and above. If you're using an older version of Python or need to install pip separately, follow the instructions here.

## Steps
1. Clone the repository

2. Create a virtual environment

3. Navigate to nail_musicbrainz directory
```bash
cd nail_musicbrainz
```
4. Install dependencies
```python 
pip install -r requirements.txt
```

5. Navigate to musicbrainz directory
```bash
cd musicbrainz
```

6. Start the dev server
```python
python manage.py runserver
```
## Usage

To search for artists, open your web browser and enter the following URL, replacing <artist_name> with the name of the artist you want to search for:

For example to search for Adele:
```bash
http://127.0.0.1:8000/?artist_name=adele
```
### Response

If multiple possible matches are found, the API returns a JSON response with a list of possible matches.
```bash
{"possible_matches": ["Adele", "Ad\u00e8le", "Ad\u00e8le", "Adele", "Adele", "Ad\u00e8le", "Ad\u00e8le Bloemendaal", "Ad\u00e8le Anderson", "Mortelle Ad\u00e8le", "Adele Harley", "Ad\u00e8le Charvet", "Adele Hoffmann", "Laila Ad\u00e8le", "Adele Holness", "Adele B.", "Adele Bertei", "Adele Sebastian", "Adele Addison", "Adele H", "Adele Stolte", "Adele Morgan", "Adele Madau", "Adele Astaire", "Adele Leigh", "Adele Overton"]}
```


If single artist match is found, the API returns a JSON response with information about the artist and their releases.
```bash
{"artist": "skrillex", "releases": ["More Monsters and Sprites", "Scary Monsters and Nice Sprites", "More Monsters and Sprites", "Narcissistic Cannibal", "Skrillex Presents: Free Treats, Volume: 001", "Gypsyhook EP", "2011-06-18: BBC Radio 1 Essential Mix: Rockness Festival", "Reptile\u2019s Theme", "My Name Is Skrillex", "My Name Is Skrillex", "Scary Monsters and Nice Sprites (Deluxe Tour Edition)", "My Name Is Skrillex", "Scary Monsters and Nice Sprites", "Kill Everybody (KOAN Sound remix)", "Scary Monsters and Nice Sprites", "Get Up!", "Scary Monsters and Nice Sprites", "Scary Monsters and Nice Sprites", "Gypsyhook EP", "Scary Monsters And Nice Sprites", "Weekends!!!", "Syndicate (Skrillex remix)", "Scary Monsters and Nice Sprites", "Mothership 001", "Bells"]}
```


If no artist is found, the API returns a JSON response with an error message.

```bash
{"error": "No artist found"}
```
