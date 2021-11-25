import sys
import discogs_client
import requests
d = discogs_client.Client('MusicMatch/0.1', user_token = 'JMXkonQHZuPUndexjVLrBGimDewLyrNzGxjFjpkL')

nr = int(sys.argv[1]) - 1

song_names = sys.argv[2].split('-')
song = ''
if(len(song_names) > 1):
	song = song_names[1]
else:
	song = song_names[0]

new_songs = song.split('(')
song = new_songs[0]
if(len(sys.argv)>3):
 search_artist = d.search(song, artist= sys.argv[3] , type='release', key='gNkpWFrqcDaUTkxhoHoX',secret='szvFyRTePSBirdnrqSaKgCTmGvphsJLm')
else:
 search_artist = d.search(song, type='release', key='gNkpWFrqcDaUTkxhoHoX',secret='szvFyRTePSBirdnrqSaKgCTmGvphsJLm')
genre1 = search_artist[0].genres
year = search_artist[0].year
artist = search_artist[0].artists[0]
'''#print(year)
#print(artist.name)
#print(search_artist[0].videos[0].url)
#print()'''
artist_n = artist.name
count =0

releaseList=[]
youtubeLink = []
imgList = []
genreList=[]
artistList=[]
i=0
curr_year = year
prev_year = year-1
next_year = year+1
art = set()

#same artist
result = d.search(artist=artist_n, genre=genre1[0], year = curr_year)

if(len(result)!=0):
	x = []
	j=0
	while (count<=500) :
		count = count +1
		if(j<len(result)):		
			x = result[j].videos
			img = result[j].images
			#print(str(len(x))+"  "+str(len(img)))
			#print()
			if(len(x)>0):
				for u in range(len(x)):
					genreList.append(genre1[0])
					artistList.append(artist_n)
					imgList.append(img[0]['uri'])
					youtubeLink.append(x[u].url)
					releaseList.append(x[u].title)
					if(len(releaseList) > 3):
						break
		else:
			break
		if(len(releaseList) > 3):
			break
		j=j+1

while(len(releaseList) <=3):
	result = d.search(artist=artist_n, genre=genre1[0], year = prev_year)
	if(len(result)==0):
		continue
	x = []
	j=0
	while (count<=500) :
		count = count +1
		if(len(result)>0 and j < len(result)):		
			x = result[j].videos
			img = result[j].images
			#print(str(len(x))+"  "+str(len(img)))
			#print()
			if(len(x)>0):
				for u in range(len(x)):
					genreList.append(genre1[0])
					artistList.append(artist_n)
					imgList.append(img[0]['uri'])
					youtubeLink.append(x[u].url)
					releaseList.append(x[u].title)
					if(len(releaseList) > 3):
						break
		else:
			break
		if(len(releaseList) > 3):
			break
		j=j+1

	result = d.search(artist=artist_n, genre=genre1[0], year = next_year)
	if(len(result)==0):
		continue
	x = []
	j=0
	while (count<=500) :
		count = count +1
		if(len(result)>0 and j<len(result)):		
			x = result[j].videos
			img = result[j].images
			#print(str(len(x))+"  "+str(len(img)))
			#print()
			if(len(x)>0):
				for u in range(len(x)):
					genreList.append(genre1[0])
					artistList.append(artist_n)
					imgList.append(img[0]['uri'])
					youtubeLink.append(x[u].url)
					releaseList.append(x[u].title)
					if(len(releaseList) > 3):
						break
		else:
			break
		if(len(releaseList) > 3):
			break
		j=j+1
	prev_year = prev_year - 1
	next_year = next_year + 1

art.add(artist_n)

#Other Artist same genre
curr_year = year
prev_year = year-1
next_year = year+1

result = d.search(genre=genre1[0], year = curr_year)

result_j = result[0]

if(len(result)!=0):
	x = []
	j=0
	while (count<=500) :
		count = count +1
		if(j<len(result)):
			if(  isinstance(result[j], discogs_client.models.Master )):  
				if(len(result[j].main_release.artists)):	
					artist_r = result[j].main_release.artists[0].name	
					x = result[j].videos
					img = result[j].images
					#print(str(len(x))+"  "+str(len(img)))
					#print()
					if(len(x)>0):
						for u in range(len(x)):
							if not(artist_r in art) :
								genreList.append(genre1[0])
								artistList.append(artist_r)
								imgList.append(img[0]['uri'])
								youtubeLink.append(x[u].url)
								releaseList.append(x[u].title)
								art.add(artist_r)
								if(len(releaseList) > nr):
									break
			if(  isinstance(result[j], discogs_client.models.Release )):
				if(len(result[j].artists)):	
					artist_r = result[j].artists[0].name	
					x = result[j].videos
					img = result[j].images
					#print(str(len(x))+"  "+str(len(img)))
					#print()
					if(len(x)>0):
						for u in range(len(x)):
							if not(artist_r in art) :
								genreList.append(genre1[0])
								artistList.append(artist_r)
								imgList.append(img[0]['uri'])
								youtubeLink.append(x[u].url)
								releaseList.append(x[u].title)
								art.add(artist_r)
								if(len(releaseList) > nr):
									break
										
		else:
			break
		if(len(releaseList) > nr):
			break
		j=j+1

while(len(releaseList) <= nr):
	result = d.search(genre=genre1[0], year = prev_year)
	if(len(result)==0):
		continue
	x = []
	j=0
	while (count<=500):
		count = count +1
		if(len(result)>0 and j < len(result)):
			if(  isinstance(result[j], discogs_client.models.Master )):  
				if(len(result[j].main_release.artists)):	
					artist_r = result[j].main_release.artists[0].name	
					x = result[j].videos
					img = result[j].images
					#print(str(len(x))+"  "+str(len(img)))
					#print()
					if(len(x)>0):
						for u in range(len(x)):
							if not(artist_r in art) :
								genreList.append(genre1[0])
								artistList.append(artist_r)
								imgList.append(img[0]['uri'])
								youtubeLink.append(x[u].url)
								releaseList.append(x[u].title)
								art.add(artist_r)
								if(len(releaseList) > nr):
									break
			if(  isinstance(result[j], discogs_client.models.Release )):
				if(len(result[j].artists)):	
					artist_r = result[j].artists[0].name	
					x = result[j].videos
					img = result[j].images
					#print(str(len(x))+"  "+str(len(img)))
					#print()
					if(len(x)>0):
						for u in range(len(x)):
							if not(artist_r in art) :
								genreList.append(genre1[0])
								artistList.append(artist_r)
								imgList.append(img[0]['uri'])
								youtubeLink.append(x[u].url)
								releaseList.append(x[u].title)
								art.add(artist_r)
								if(len(releaseList) > nr):
									break
		else:
			break
		if(len(releaseList) > nr):
			break
		j=j+1

	result = d.search(genre=genre1[0], year = next_year)
	if(len(result)==0):
		continue
	x = []
	j=0
	while (count<=500):
		count = count +1
		if(len(result)>0 and j<len(result)):
			if(  isinstance(result[j], discogs_client.models.Master )):  
				if(len(result[j].main_release.artists)):	
					artist_r = result[j].main_release.artists[0].name	
					x = result[j].videos
					img = result[j].images
					#print(str(len(x))+"  "+str(len(img)))
					#print()
					if(len(x)>0):
						for u in range(len(x)):
							if not(artist_r in art) :
								genreList.append(genre1[0])
								artistList.append(artist_r)
								imgList.append(img[0]['uri'])
								youtubeLink.append(x[u].url)
								releaseList.append(x[u].title)
								art.add(artist_r)
								if(len(releaseList) > nr):
									break
			if(  isinstance(result[j], discogs_client.models.Release )):
				if(len(result[j].artists)):	
					artist_r = result[j].artists[0].name	
					x = result[j].videos
					img = result[j].images
					#print(str(len(x))+"  "+str(len(img)))
					#print()
					if(len(x)>0):
						for u in range(len(x)):
							if not(artist_r in art) :
								genreList.append(genre1[0])
								artistList.append(artist_r)
								imgList.append(img[0]['uri'])
								youtubeLink.append(x[u].url)
								releaseList.append(x[u].title)
								art.add(artist_r)
								if(len(releaseList) > nr):
									break
		else:
			break
		if(len(releaseList) > nr):
			break
		j=j+1
	prev_year = prev_year - 1
	next_year = next_year + 1
for k in range(len(releaseList)):
	print(str(releaseList[k])+ "..." + str(artistList[k])+ "..." + str(genreList[k]) + "..." + str(youtubeLink[k]) + "..." + str(imgList[k]))
"""with open('data.json', 'w') as f:
	for i in range(len(releaseList)):
		json.dump(releaseList[i], f)
		json.dump(imgList[i],f)	
		json.dump(releaseList[i],f)
"""
