# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #

example_input="John is connected to Bryant, Debra, Walter."\
"John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner."\
"Bryant is connected to Olive, Ollie, Freda, Mercedes."\
"Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man."\
"Mercedes is connected to Walter, Robin, Bryant."\
"Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures."\
"Olive is connected to John, Ollie."\
"Olive likes to play The Legend of Corgi, Starfleet Commander."\
"Debra is connected to Walter, Levi, Jennie, Robin."\
"Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords."\
"Walter is connected to John, Levi, Bryant."\
"Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man."\
"Levi is connected to Ollie, John, Walter."\
"Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma."\
"Ollie is connected to Mercedes, Freda, Bryant."\
"Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game."\
"Jennie is connected to Levi, John, Freda, Robin."\
"Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms."\
"Robin is connected to Ollie."\
"Robin likes to play Call of Arms, Dwarves and Swords."\
"Freda is connected to Olive, John, Debra."\
"Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

def create_data_structure(string_input):
	network = {}
	if string_input == '':
		return network
	# A list of sentences contained in string_input:
	sentences = string_input.split('.')
	# As the input string ends with '.', the last element in sentences is [''] 
	# and I remove it by this function:
	sentences.pop() 
	
	user_list = []
	# user_list is an auxiliary data structure. Contains only names of users. 
	for sentence in sentences:
		first_space = sentence.find(' ')
		user = sentence[:first_space]
		if user not in user_list:
			user_list.append(user)
	
	# the user_list is completed and the next code will create the final network.
	for user in user_list:
		user_value = {} 
		# The final network structure will be following: network = {user: user_value, ...}, 
		# where user_value = {'connections': [user_A, user_B, ...], 'games': [game_1, game_2, ...]}.
		for sentence in sentences:
			if sentence.find(user) == 0:
				find_connections = sentence.find('is connected to ')
				if find_connections != -1:
					# Create the value of the key 'connections', which is a list of user's connections:
					user_value['connections'] = sentence[find_connections+len('is connected to '):].split(', ') 
				find_games = sentence.find('likes to play ')
				if find_games != -1:
					# Create the value of the key 'games', which is a list of user's favorite games:
					user_value['games'] = sentence[find_games+len('likes to play '):].split(', ') 
				# Add user and user_value to the final network:
				network[user] = user_value 
	return network

# network = create_data_structure(example_input)

# print create_data_structure(example_input)

def get_connections(network, user):
	if user not in network:
		return None
	# The following Elif Statement isn't needed in the case 
	# of our example_input, but I entered it here for sure:
	elif 'connections' not in network[user]:
		return []
	else:
		return network[user]['connections']

# print get_connections(network, 'Levi')
# print get_connections(network, 'Stanislava')

def get_games_liked(network, user):
	if user not in network:
		return None
	# The following Elif Statement isn't needed in the case 
	# of our example_input, but I entered it here for sure:
	elif 'games' not in network[user]:
		return []
	else:
		return network[user]['games']

# print get_games(network, 'Ollie')
# print get_games(network, 'Stanislava')

def add_connection(network, user_A, user_B):
	if user_A not in network or user_B not in network:
		return False
	elif user_B not in get_connections(network, user_A):
		get_connections(network, user_A).append(user_B)
	return network

# print add_connection(network, 'Freda', 'Levi')
# print add_connection(network, 'John', 'Stanislava')

def add_new_user(network, user, games):
	if user not in network:
		network[user] = {'connections': [], 'games': games}
	return network

# add_new_user(network, 'Stanislava', ['Memory Game', 'Sudoku'])

def get_secondary_connections(network, user):
	user_connections = get_connections(network, user)
	if user_connections or user_connections == []:
		secondary_connections = []
		for friend in user_connections:
			friend_connections = get_connections(network, friend)
			# Add every secondary connection only once:
			for player in friend_connections:
				if player not in secondary_connections:
					secondary_connections.append(player)
		return secondary_connections
	
# print get_secondary_connections(network, 'John')
# print get_secondary_connections(network, 'Stanislava')


def connections_in_common(network, user_A, user_B):
	if user_A not in network or user_B not in network:
		return False
	common_list = []
	for user in get_connections(network, user_A):
		if user in get_connections(network, user_B):
			common_list.append(user)
	return len(common_list)

# print connections_in_common(network, 'John', 'Walter')


def path_to_friend(network, user_A, user_B, visited=None):
	if visited is None:
		visited = []

	user_A_connections = get_connections(network, user_A)
	
	if user_A_connections:
		path = [user_A]
		if user_B in user_A_connections:
			path.append(user_B)
			return path
		else:
			visited.append(user_A)
			for user in user_A_connections:
				if user not in visited:
					search_path = path_to_friend(network, user, user_B, visited)
					if search_path and search_path[-1] == user_B:
						path = [user_A] + search_path
						break
			if len(path) == 1:
				return None
			return path


# print path_to_friend(network, 'Robin', 'Stanislava')
# print path_to_friend(network, 'Freda', 'Jennie')


# ---------------------------------------------------------------------------- #
# Make-Your-Own-Procedure (MYOP)                                               #
# ---------------------------------------------------------------------------- #

# In my MYOP I evaluate the popularity of users and games.

# For both, users and games, I wrote 3 procedures (totally 6): One for making 
# an order (of users/games) by popularity, second for adding ranks and third  
# for evaluating a given user/game popularity.

# ---------------------------------------------------------------------------- #
# A. USERS:
# ---------------------------------------------------------------------------- #

# ----------------------------------- #
# A1. users_popularity_order(network) #
# ----------------------------------- #

# Arguments:

# - a network created by create_data_structure (dictionary)

# Return:

# - a list of tuples [(user, number), ...], where user is the name of user (string)
#   and number us the number of users that are connected to him (integer).
# - for the example_input the output will be following:
#   [('John', 5), ('Ollie', 4), ('Bryant', 4), ('Walter', 4), ('Freda', 3), ('Levi', 3), 
#    ('Robin', 3), ('Debra', 2), ('Olive', 2), ('Mercedes', 2), ('Jennie', 1)]
# - John is the most popular user - 5 users are connected to him.

def users_popularity_order(network):
	users_order = {}
	for user in network:
		users_order[user] = 0
		for player in network:
			if user in network[player]['connections']:
				users_order[user] += 1
	users_order = sorted(users_order.items(), key=lambda (user, popularity): popularity, reverse=True)
	return users_order

# print users_popularity_order(network)

# ----------------------- #
# A2. rank_users(network) #
# ----------------------- #

# The previous procedure gave us a list, where users are ordered by their popularity.
# John is the most popular, it is obvious. But how about the other users? You can see 
# that in fact, it is not the truth, that Ollie is second, Bryant third and Walter fourth. 
# They have the same popularity (4 users are connected to each of them), so they are
# all on the second place. The whole ranking list looks like this:

# 1. John
# 2. Ollie, Bryant, Walter
# 3. Freda, Levi, Robin
# 4. Debra, Olive, Mercedes
# 5. Jennie

# So, the rank_users(network) procedure adds ranks to all network users.

# Arguments:

# - a network created by create_data_structure (dictionary)

# Return:

# - a list of tuples [(user, number1, number2), ...], where user is the name of user 
#   (string), number1 us the number of users that are connected to him (integer) 
#   and number2 is the user's popularity rank in the network (integer). 

# - for the example_input the output will be following:
#   [('John', 5, 1), ('Ollie', 4, 2), ('Bryant', 4, 2), ('Walter', 4, 2), 
#    ('Freda', 3, 3), ('Levi', 3, 3), ('Robin', 3, 3), ('Debra', 2, 4), ('Olive', 2, 4), 
#    ('Mercedes', 2, 4), ('Jennie', 1, 5)]

def rank_users(network):
	network = users_popularity_order(network)
	network[0] = network[0] + (1,)
	for user in network[1:]:
		user_index = network.index(user)
		before_user = network[user_index - 1]
		if user[1] == before_user[1]:
			network[user_index] += (before_user[2],)
		else:
			network[user_index] += (before_user[2]+1,)
	return network

# print rank_users(network)

# ---------------------------------- #
# A3. user_polularity(network, user) #
# ---------------------------------- #

# Gives us iformation about popularity of a given user

# Arguments:

# - a network created by create_data_structure (dictionary)
# - the user name (string)

# Return:

# - a dictionary with 3 keys: 
#   {'fans': value_fans, 'fans in %': value_fans_in_%, 'rank': value_rank}

# - the value of 'fans' is a number of users that are connected to a given user (integer)
# - the value of 'fans in %' is how many users of all network users are connected 
#   to a given user, expressed in percentage (float)
# - the value of 'rank' is the user's popularity rank (integer)

# - e. g. for 'Walter' from the example_input the output will be following:
#   {'fans': 4, 'rank': 2, 'fans in %': 36.36}
#   There are 4 network users connected to Walter. It is 36.36% of all network users.
#   Walter is on the second place in the users popularity ranking list.

# - returnes None if user isn't in the network

def user_popularity(network, user):
	if user in network:
		user_pop = {}
		popularity_list = users_popularity_order(network)
		user_pop['fans'] = dict(popularity_list)[user]
		user_pop['rank'] = rank_users(network)[popularity_list.index((user, user_pop['fans']))][2] 
		user_pop['fans in %'] = round(100.0*user_pop['fans']/len(network), 2)
		return user_pop

# print user_popularity(network, 'Walter')

# ---------------------------------------------------------------------------- #
# B. GAMES:
# ---------------------------------------------------------------------------- #

# The following 3 procedures are very similar to the previous 3 procedures,
# but they evaluate popularity of games instead of popularity of users.

# ----------------------------------- #
# B1. games_popularity_order(network) #
# ----------------------------------- #

# Arguments:

# - a network created by create_data_structure (dictionary)

# Return:

# - a list of tuples [(game, number), ...], where game is the name of a game (string)
#   and number us the number of users that like to play the game (integer).
# - for the example_input the output will be following:
#   [('The Legend of Corgi', 4), ('Super Mushroom Man', 3), ('Seahorse Adventures', 3), 
#    ('Dwarves and Swords', 3), ('Call of Arms', 3), ('Starfleet Commander', 2), 
#    ('The Movie: The Game', 2), ('Dinosaur Diner', 2), ('Pirates in Java Island', 2), 
#    ('Seven Schemers', 2), ('City Comptroller: The Fiscal Dilemma', 2), ('Ninja Hamsters', 2)]
# - 'The Legend of Corgi' is the most popular game - 4 users like to play it.

def games_popularity_order(network):
	games_order = {}
	for user in network:
		for game in network[user]['games']:
			if game in games_order:
				games_order[game] += 1
			else:
				games_order[game] = 1
	games_order = sorted(games_order.items(), key=lambda (game, popularity): popularity, reverse=True)
	return games_order

# print games_popularity_order(network)

# ----------------------- #
# B2. rank_games(network) #
# ----------------------- #

# The previous procedure gave us a list, where games are ordered by their popularity.
# 'The Legend of Corgi' is the most popular, it is obvious. But how about the other games?  
# You can see that in fact, it is not the truth, that 'Super Mushroom Man' is second, 
# 'Seahorse Adventures' third, 'Dwarves and Swords' fourth and 'Call of Arms' fifth. 
# They have the same popularity (3 users like to play each of them), so they are
# all on the second place. The whole ranking list looks like this:

# 1. 'The Legend of Corgi'
# 2. 'Super Mushroom Man', 'Seahorse Adventures', 'Dwarves and Swords', 'Call of Arms'
# 3. 'Starfleet Commander', 'The Movie: The Game', 'Dinosaur Diner', 'Pirates in Java Island',
#    'Seven Schemers', 'City Comptroller: The Fiscal Dilemma', 'Ninja Hamsters'

# So, the rank_games(network) procedure adds ranks to all games the network users play.

# Arguments:

# - a network created by create_data_structure (dictionary)

# Return:

# - a list of tuples [(game, number1, number2), ...], where game is the name of game 
#   (string), number1 us the number of users that like to play it (integer) 
#   and number2 is the games's popularity rank (integer). 

# - for the example_input the output will be following:
#   [('The Legend of Corgi', 4, 1), ('Super Mushroom Man', 3, 2), ('Seahorse Adventures', 3, 2), 
#    ('Dwarves and Swords', 3, 2), ('Call of Arms', 3, 2), ('Starfleet Commander', 2, 3), 
#    ('The Movie: The Game', 2, 3), ('Dinosaur Diner', 2, 3), ('Pirates in Java Island', 2, 3), 
#    ('Seven Schemers', 2, 3), ('City Comptroller: The Fiscal Dilemma', 2, 3), ('Ninja Hamsters', 2, 3)]

def rank_games(network):
	network = games_popularity_order(network)
	network[0] = network[0] + (1,)
	for game in network[1:]:
		game_index = network.index(game)
		before_game = network[game_index - 1]
		if game[1] == before_game[1]:
			network[game_index] += (before_game[2],)
		else:
			network[game_index] += (before_game[2]+1,)
	return network

# print rank_games(network)

# ---------------------------------- #
# B3. game_polularity(network, game) #
# ---------------------------------- #

# Gives us iformation about popularity of a given game

# Arguments:

# - a network created by create_data_structure (dictionary)
# - the game name (string)

# Return:

# - a dictionary with 3 keys: 
#   {'fans': value_fans, 'fans in %': value_fans_in_%, 'rank': value_rank}

# - the value of 'fans' is a number of users that like to play the given game (integer)
# - the value of 'fans in %' is how many users of all network users like to play 
#   the given game, expressed in percentage (float)
# - the value of 'rank' is the game's popularity rank (integer)

# - e. g. for 'Dwarves and Swords' from the example_input the output will be following:
#   {'fans': 3, 'rank': 2, 'fans in %': 27.27}
#   There are 3 network users that like to play this game. It is 27.27% of all network users.
#   'Dwarves and Swords' is on the second place in the games popularity ranking list.

# - returns None if none of the users likes to play the game

def game_popularity(network, game):
	game_pop = {}
	popularity_list = games_popularity_order(network)
	if game in dict(popularity_list):
		game_pop['fans'] = dict(popularity_list)[game]
		game_pop['rank'] = rank_games(network)[popularity_list.index((game, game_pop['fans']))][2] 
		game_pop['fans in %'] = round(100.0*game_pop['fans']/len(network), 2)
		return game_pop

# print game_popularity(network, 'Dwarves and Swords')


