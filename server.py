from flask import Flask
from requests import post
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from http.client import responses

app = Flask(__name__)

@app.route('/')
def home():
	#variables
	content=[]
	categories = ['genres', 'release_dates', 'platforms', 'rating']	
	urls = {
			'genres': 'fields name; where id =',
			'release_dates': 'fields human; where id =',
			'platforms': 'fields abbreviation,alternative_name,category,checksum,created_at,generation,name,platform_family,platform_logo,slug,summary,updated_at,url,versions,websites; where id = '
		}
	#root post request
	response = post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },'data': 'fields *; limit 5;' })
	
 
	for i in range(len(response.json())):
		arrayGenres = []
		arrayRelease = []
		plataforma = []
		Ratings = []
		content.append(response.json()[i])
		print(response.json()[i])
		responseImages = post(
	  'https://api.igdb.com/v4/covers',
      **{'headers': 
          {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },
          'data': f'fields alpha_channel,animated,checksum,game,game_localization,height,image_id,url,width; where game = {str(response.json()[i]["id"])};' })

    
		try:
			content[i]['cubierta'] = responseImages.json()[0]['url']
		except:
			pass
		responseScreens = post(
			'https://api.igdb.com/v4/screenshots',
      **{'headers': 
          {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },
          'data': f'fields alpha_channel,animated,checksum,game,game_localization,height,image_id,url,width; where game = {str(response.json()[i]["id"])};' })
		try:
			content[i]['imageness'] = responseImages.json()[0]['url']
		except:
			pass		
		for category in categories:
			if response.json()[i].get(category) is None:
				continue
			for cat in response.json()[i].get(category):
				print(cat)
				
				responsePerCategory = post(f'https://api.igdb.com/v4/{category}', 
                               **{'headers': {'Client-ID': 'rpx9sjp7kxzp4nzk2v5qjpg2scl8cw', 'Authorization': 'Bearer ivv1gvdyi46udh4ow9xx9lstyepek3' },
                                  'data': f'{urls[category]} {str(cat)};' })			
				match category:
					case "genres":					
						arrayGenres.append(responsePerCategory.json()[0]['name'])
					case "release_dates":
						arrayRelease.append(responsePerCategory.json()[0]['human'])
					case "platforms":
						plataforma.append(responsePerCategory.json()[0]['name'])
					case _:
						pass
			match category:
				case "genres":
					content[i][category] = arrayGenres
				case "release_dates":
					content[i][category] = arrayRelease
				case "platforms":
					content[i][category] = plataforma
				case _:
					pass
				

	#print(content)

	return render_template('main.html', content=content)




@app.route('/Recommendations', methods=['GET', 'POST'])
def Recommendations():
	if request.method == 'POST':
		return redirect(url_for('home'))

	return render_template('Recommendations.html')


if __name__ == '__main__':
	app.run(port=8000)
	app.run(debug=True)
