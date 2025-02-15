from flask import Flask
from requests import post
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
	content=[]
	#response = post('https://id.twitch.tv/oauth2/token?client_id=rpx9sjp7kxzp4nzk2v5qjpg2scl8cw&client_secret=wh2d0n6ougtktl21dnodzgcxhz747t&grant_type=client_credentials')
	#print ("response: %s" % str(response.json())) 
	#response = post('https://api.igdb.com/v4/genres', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': 'fields name; where id = 8;' })
	response = post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': 'fields *; limit 10;' })
	
    #print(response.json())

	for i in range(len(response.json())):
		responseImages = post('https://api.igdb.com/v4/covers', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': f'fields alpha_channel,animated,checksum,game,game_localization,height,image_id,url,width; where game = {str(response.json()[i]['id'])};' })
    
		cover_images_url = []
		for image_url in responseImages.json():
			print(image_url['url'])
			cover_images_url.append(image_url['url'])
									
		# content[i]['cubiertas'] = cover_images_url



		content.append(response.json()[i])

		# aqui va el recorrido de los generos con base en el id de cada uno
		if response.json()[i].get('genres') is None:
			continue
		arrayGenres = []
		for genre in response.json()[i].get('genres'):
			genre_id = str(genre)
			responseGenres = post('https://api.igdb.com/v4/genres', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': f'fields name; where id = {genre_id};' })
			arrayGenres.append(responseGenres.json()[0]['name'])
		content[i]['genero'] = arrayGenres

        # aqui va el recorrido de las fechas de lanzamiento con base en el id de cada una#
		if response.json()[i].get('release_dates') is None:
			continue
		arrayRelease = []
		for release in response.json()[i].get('release_dates'):
			relase_date_id = str(release)
			responseRelease = post('https://api.igdb.com/v4/release_dates', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': f'fields human; where id = {relase_date_id};' })
			arrayRelease.append(responseRelease.json()[0]['human'])
			#print(response.json()[i]['cover']) 
		content[i]['fecha'] = arrayRelease
        
               

		# Imagenes = []
		# for image in response.json()[i]['cover']:
		# 	cover_id = str(image)
		# 	responseImages = post('https://api.igdb.com/v4/covers', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': f'fields alpha_channel,animated,checksum,game,game_localization,height,image_id,url,width; where id = {cover_id};' })
		# 	#Imagenes.append(responseImages.json()[0]['url'])
		# 	print(responseImages.json()[i])
		# content[i]['imagen'] = Imagenes

		# if response.json()[i].get('screenshots') is None:
		# 	continue
		# Screenshots = []
		# for screenshot in response.json()[i].get('screenshots'):
		# 	valor = str(screenshot)
		# 	responseScreenshots = post('https://api.igdb.com/v4/screenshots', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': f'fields alpha_channel,animated,checksum,game,height,image_id,url,width; where id = {valor};' })
		# 	Screenshots.append(responseScreenshots.json()[0]['url'])
		# content[i]['screenshots'] = Screenshots

		if response.json()[i].get('platforms') is None:
			continue
		plataforma = []
		for platform in response.json()[i].get('platforms'):
			platform_id = str(platform)
			responsePlataforma = post('https://api.igdb.com/v4/platforms', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': f'fields abbreviation,alternative_name,category,checksum,created_at,generation,name,platform_family,platform_logo,slug,summary,updated_at,url,versions,websites; where id = {platform_id};' })
			plataforma.append(responsePlataforma.json()[0]['name'])
		content[i]['plataforma'] = plataforma
  	
	

	return render_template('main.html', content=content)

@app.route('/Recommendations', methods=['GET', 'POST'])
def Recommendations():
	if request.method == 'POST':
		return redirect(url_for('home'))

	return render_template('Recommendations.html')



#aqui va ruta de fotos


#aqui va ruta de lo que sea


if __name__ == '__main__':
	app.run(port=8000)
	app.run(debug=True)

