from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from pprint import pprint
from models import Property, Size
from forms import SearchForm
def home(request):

	#This code just moves the json to sqllite. Only should be called once for obvious reasons.
	# json_data=open('Home/IslandRentals.json')
	# data = json.load(json_data)
	# pprint(data)
	# json_data.close()
	# for prop in data["property"]:
	# 	try:
	# 		new_prop = Property()
	# 		new_prop.address = prop['address']
	# 		new_prop.price = prop["price"]
	# 		size = Size(num_bedrooms=prop["size"]["num_bedrooms"],num_bathrooms=prop["size"]["num_bathrooms"],sq_ft=prop["size"]["sq_ft"],lot_sq_ft=prop["size"]["lot_sq_ft"])
	# 		size.save()
	# 		new_prop.size = size
	# 		new_prop.proximity_to_volcanoe = prop["proximity_to_volcanoe"]
	# 		new_prop.school_rating = prop["school_rating"]
	# 		new_prop.distance_to_bar = prop["distance_to_bar"]
	# 		new_prop.image = prop["image"]
	# 		new_prop.home_type = prop["home_type"]
	# 		new_prop.distance_to_public_transit = prop["distance_to_public_transit"]
	# 		new_prop.save()
	# 	except:
	# 		print("Except")
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = SearchForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			price = form.cleaned_data['max_price']
			properties = Property.objects.filter(price__lte=price)#less than or equal
			return render(request, 'home.html', {'form': form,'data':properties})
    # if a GET (or any other method) we'll create a blank form
	else:
		form = SearchForm()#just make a new form
		properties = Property.objects.all()
		return render(request, 'home.html', {'form': form,'data':properties})
