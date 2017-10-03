# Python 3.6.1
import praw
import os
import random


reddit = praw.Reddit(client_id=os.environ['client_id'],
					 client_secret=os.environ['client_secret'],
					 password=os.environ['password'],
					 user_agent=os.environ['user_agent'],
					 username=os.environ['username'])

lyrics = """Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mondo.
Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mond'.

Lundo, merkredo, sabato, mardo, ĵaŭdo kaj dimanĉo
jen milito, jen la paco, jen infano kun malsato.
La misiloj preskaŭ falas, la kolomboj malkonsentas,
estas tiel, estas tiel.

Jen virino kiu ne sidas, ĉar laboro ĉiam estas,
kaj la patro kiu ne alvenas, ĉar la poŝo estas malplena.
Tiom da manoj kiuj konstruas, kaj la aliaj kiuj detruas,
estas tiel, estas tiel.

Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mondo.
Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mond'.

Dekses horoj kiuj sonoras kaj ok horoj kiuj silentas
Multaj homoj kiuj rapidas, jam la alia tago venas.
Ni profitu la momenton, ĉar la vivo ne atendas,
estas tiel, estas tiel

Lundo, merkredo, sabato, mardo, jaŭdo kaj dimanĉo
jen milito, jen la paco, jen infano kun malsato.
La misiloj preskaŭ falas, la kolomboj malkonsentas,
estas tiel, estas tiel.

Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mondo.
Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mond'.

Iras por mi, iras por vi,
iras por ŝi, iras por li, tiel la mondo
Iras por mi, iras por vi,
iras por ŝi, iras por li, tiel la mondo

Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mondo.
Tiel la mondo iras, tiel la mondo iras.
Tiel la mondo iras, tiel la mond-ooo iiirrrr-aaass""".split('\n')
lyrics = [line for line in lyrics if len(line) > 0]

print(f"Logged in as {reddit.user.me()}")

safe_subreddits = []

for subreddit in reddit.user.moderator_subreddits():
	safe_subreddits.append(subreddit.display_name)

print(f"Will not overwrite comments in: {safe_subreddits}")

for comment in reddit.user.me().comments.new(limit=None):
	if comment.subreddit in safe_subreddits:
		continue
	random_lyric = random.SystemRandom().choice(lyrics)
	print(f"Changing ({comment}) in {comment.subreddit}:\nOriginally:\n{comment.body}\nAnd is now:\n{random_lyric}\n")
	comment.edit(random_lyric)
