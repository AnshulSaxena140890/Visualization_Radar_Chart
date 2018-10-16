# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Avg
from . import models


# Create your views here.

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# plotly.tools.set_credentials_file(username='anshul.saxena140890', api_key='r4cdHL7wtJCuQgQNRIAu')

def visualisation(request):


	division_type= request.POST.get("type")
	# print(division_type)

	if division_type is None:
		division_type='topic'



	obj = models.BlackCofferData.objects.values(division_type).annotate(Avg('intensity'),Avg('likelihood'),Avg('relevance'))

	# print(obj)
	l1=[]
	l2=[]
	l3=[]
	division=[]




	for i in obj:
	    l1.append(i['intensity__avg'])
	    l2.append(i['likelihood__avg'])
	    l3.append(i['relevance__avg'])

	    division.append(i[division_type])



	data = [go.Scatterpolar(r = l1,theta = division,fill = 'toself',name = 'Intensity Graph'),go.Scatterpolar(r = l2,theta = division,fill = 'toself',name = 'Likelihood Graph'),go.Scatterpolar(r = l3,theta = division,fill = 'toself',name = 'Relevance Graph')]

	layout = go.Layout(polar = dict(radialaxis = dict(visible = True,range = [0, 30])),showlegend = False)

	fig = go.Figure(data=data, layout=layout)
	obj2 = py.plot(fig)
	# print(obj2)

	obj3=obj2+".embed"
	# print(obj3)


	division_name=division_type.capitalize()
	print(division_name)


	return render(request,'visualization.html',{'obj3':obj3,'division':division_name})