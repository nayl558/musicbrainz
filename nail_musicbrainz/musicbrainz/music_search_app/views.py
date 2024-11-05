# Create your views here.
from django.http import JsonResponse
import requests #make sure requests library is installed through pip

def search_artist(request):
    artist_name = request.GET.get('artist_name') # Extract artist name from the query parameters

    if not artist_name:
        return JsonResponse({'error': 'Artist name is required'}, status=400)

    # Construct the URL for searching artists on MusicBrainz API
    search_url = f'http://musicbrainz.org/ws/2/artist/?query=artist:{artist_name}&fmt=json'

    response = requests.get(search_url)

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from MusicBrainz'}, status=500)

    data = response.json() # Json response parse

    # Possible artist's name matches in case more than 1 match found for the artist's name
    if data['count'] > 1:
        possible_matches = []
        for artist in data['artists']:
            possible_matches.append(artist['name'])
        return JsonResponse({'possible_matches': possible_matches}, status=200)
    
    # All releases' names in case exactly 1 match found for the artist's name
    elif data['count'] == 1:

        # since there is only 1 artist match in the list, it makes sense to return the very first element
        artist_id = data['artists'][0]['id'] 
        # Construct the URL for releases' retrieval based on the artist's id
        releases_url = f'http://musicbrainz.org/ws/2/release/?artist={artist_id}&fmt=json' 
        releases_response = requests.get(releases_url)
        releases_data = releases_response.json()
        releases = []
        for release in releases_data['releases']:
            releases.append(release['title'])
        return JsonResponse({'artist': artist_name, 'releases': releases}, status=200)
    
    else:
        return JsonResponse({'error': 'No artist found'}, status=404)
