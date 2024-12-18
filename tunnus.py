#!/usr/bin/python3
import random

def keksi_tunnus():
	vokaalit= "aeiouy"
	konsonantit= "hjklmnprstv"
	# Kaksi kirjaiminen tavu keskelle
	loppu = random.choice(konsonantit) + random.choice(vokaalit)
	# Valitaan loppu joka muistuttaa suomalaista nimeä
	loppu += random.choice( [ "nen", "la", "son", "ri", "ja", "to", "lo", "si" ] )
	# Alkuun 3 tai 2 kirjaiminen tavu että pituudeksi tulee 8 merkkiä
	if len(loppu) == 5:
		return random.choice(konsonantit) + random.choice(vokaalit) + random.choice(konsonantit) + loppu
	else:
		alku= random.choice(konsonantit) + random.choice(vokaalit)
		alku+= random.choice(konsonantit) + random.choice(vokaalit)
		return alku + loppu
	fi

for i in range(8):
	print(keksi_tunnus())
