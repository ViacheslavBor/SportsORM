from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.filter(Q(first_name='Alexander')|Q(first_name='Wyatt')),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)
	return redirect("index")

# 1) Show all baseball leagues:
#		"leagues": League.objects.filter(sport__contains = "Baseball")
# 2) Show all womens' leagues:
#		"leagues": League.objects.filter(name__contains = "women")
# 3) Show all leagues where sport is any type of hockey:
#		"leagues": League.objects.filter(name__contains = "Hockey")
# 4) Show all leagues where sport is something OTHER THAN football
# 		"leagues": League.objects.exclude(sport = "Football")
# 5) Show all leagues that call themselves "conferences"
# 		"leagues": League.objects.filter(name__contains = "Conference")
# 6) Show all leagues in the Atlantic region
# 		"leagues": League.objects.filter(name__contains = "Atlantic")
# 7) Show all teams based in Dallas
# 		"teams": Team.objects.filter(location__contains = "Dallas")
# 8) Show all teams named the Raptors
# 		"teams": Team.objects.filter(team_name = "Raptors")
# 9) Show all teams whose location includes "City"
# 		"teams": Team.objects.filter(location__contains = "City")
# 10) Show all teams whose names begin with "T"
# 		"teams": Team.objects.filter(team_name__startswith="T")
# 11) Show all teams, ordered alphabetically by location
# 		"teams": Team.objects.all().order_by('location')
# 12) Show all teams, ordered by team name in reverse alphabetical order
# 		"teams": Team.objects.all().order_by('-team_name')
# 13) Show every player with last name "Cooper"
# 		"players": Player.objects.filter(last_name='Cooper')
# 14) Show every player with first name "Joshua"
# 		"players": Player.objects.filter(first_name='Joshua')
# 15) Show every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
# 		"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
# 16) Show all players with first name "Alexander" OR first name "Wyatt"
# 		"players": Player.objects.filter(Q(first_name='Alexander')|Q(first_name='Wyatt'))