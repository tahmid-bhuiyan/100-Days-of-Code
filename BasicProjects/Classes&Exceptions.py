
#creates the class Move
class Move:
#creates an object instance self.cooperate
	def __init__(self, cooperate=True):
		self.cooperate = cooperate
#depending on if player cooperates,'x' for yes, 'x' for no coop
	def __str__ (self):
		if self.cooperate == True:
			return '.'
		if self.cooperate == False:
			return 'x'
#returns a string with Move and self.cooperate
	def __repr__(self):
		str = "Move(%s)" % (self.cooperate)
		return str
#if both player's moves are the same,both either get 2 or no pts(future defs)
	def __eq__ (self, other):
		if self.cooperate == other.cooperate:
			return True
		else:
			return False
#sets the cooperation status to the opposite true -> false vice versa			
	def change (self):
		self.cooperate = not(self.cooperate)
#returns a created move object that has the same coop status given
	def copy (self):
		mov = self.cooperate
		return Move(mov)
#creates the class PlayerException
class PlayerException(Exception):
#object instance of msg created
	def __init__(self, msg):
		self.msg = msg
#returns object instance msg
	def __str__ (self):
		return self.msg
#returns a string to be used for future raised exceptions
	def __repr__(self):
		return "PlayerException('%s')" % (self.msg)
#creates the class Player
class Player:
#first checks if style is one of the ones that are accepted
#if not, raises an exceptions
#otherwise creates obj instances for points and history
	def __init__(self, style, points=0, history=None):
		sty = ('previous', 'friend', 'cheater', 'grudger', 'detective')
		self.style = style
		if self.style not in sty:
			s = "no style '%s'." % self.style
			raise PlayerException(s)
		self.points = points
		self.history = history
#if no hist is given, set it equal to empty list
		if self.history == None:
			self.history = []
		else:
			self.history = history
#creates a string and adds a . or x depending on cooper
	def __str__(self):
		base = "%s(%s)" % (self.style, self.points)
		for x in self.history:
			if x == Move(True):
				base += '.'
			else:
				base += 'x'
		return base
#returns a statement with 3 object instances sty pts and hist
	def __repr__(self):
		s = "Player('%s', %s, %s)" % (self.style, self.points, self.history)
		return s
#resets the history of a player
	def reset_history(self): 
		self.history = []
#creates the object instance of history and resets points
	def reset (self):
		self.history = []
		self.points = 0
#after a turn is made, adds/removes the points
	def update_points(self, amount):
		self.points += amount
#executes whether or not the opponent has ever not cooperated
	def ever_betrayed(self):
		if Move(False) in self.history:
			return True
		else:
			return False
#adds the last move conducted by the player to its history
	def record_opponent_move(self, move): 
		self.move = move
		self.history += [self.move]
#creates a copy with the given style but default vals for parameters
	def copy_with_style(self):
		copy = Player(self.style, 0, [])
		return copy
#determines the next move depending on the style of the player
#if its the first move for previous,cooperats,then copy last move of opponent
#friend always cooperates no matter what the opponent does
#cheater never cooperates no matter what the opponent does
#grudger cooperates until its opponent doesnt cooperate, then never cooperates
#detective follows specified pattern, then if never betrayed, cheats
#otherwise acts like the previous
	def choose_move(self):
		i = len(self.history) - 1
		if self.style == 'previous':
			if self.history == []:
				return Move(True)
			else:
				return self.history[i]
		if self.style == 'friend':
			return Move(True)
		if self.style == 'cheater':
			return Move(False)
		if self.style == 'grudger':
			if self.history == []:
				return Move(True)
			elif Move(False) in self.history:
				return Move(False)
			else:
				return Move(True)
		if self.style == 'detective':
			if len(self.history) == 0:
				return Move(True)
			elif len(self.history) == 1:
				return Move(False)
			elif len(self.history) == 2:
				return Move(True)
			elif len(self.history) == 3:
				return Move(False)
			elif Move(False) not in self.history:
				return Move(False)
			else:
				return self.history[i]
#if both players have the same cooperation status, executes
#if both chose to cooperate, both get 2 pts
#otherwise neither gets any points
#if one player cheated but the other cooperated,
#the player that cheated gets 3 points while the other loses a point
def turn_payouts(move_a, move_b):
	if Move.__eq__(move_a, move_b) == True:
		if move_a == Move(True):
			return (2,2)
		else:
			return (0,0)
	else:
		if move_a == Move(True):
			return (-1,3)
		else:
			return (3,-1)
#first checks if the given initial is one of the styles
#if the given initial is one of the accepted styles,
#the matching style gets put into a statement with default parameters,
#which is then appended to the list
#if the initial is not one of the represted styles,
#raises a playerexception with a message for the reader
def build_players(initials):
	ini = 'pfcgd'
	list = []
	for char in initials:
		if char in ini:
			if char == 'p':
				list.append(Player('previous', 0, []))
			if char == 'f':
				list.append(Player('friend', 0, []))
			if char == 'c':
				list.append(Player('cheater', 0, []))
			if char == 'g':
				list.append(Player('grudger', 0, []))
			if char == 'd':
				list.append(Player('detective', 0, []))
		else:
			raise PlayerException("no style with initial '%s'." % (char))
	return list

#sets the amount of each style in the list of players to 0
def composition(players):
	f = 0
	p = 0
	c = 0
	g = 0
	d = 0
	dict = {'friend':f, 'previous':p, 'cheater':c, 'grudger':g, 'detective':d}
#iterates through each player attribute
	for x in players:
		play = x
#adds that player's style to the dict and adds 1 to its quantity
		dict[play.style] += 1
#created a copy of the dictionary so theres no error in iterating when i,
#delete the styles with 0 occurance in list of players
	copy = dict.copy()
	for st in dict:
		if dict[st] == 0:
			del copy[st] 
	return copy

def run_turn(player_a, player_b):
	p1 = player_a
	p2 = player_b
#if both players have the same id(same style), raises an exception
	if id(player_a) == id(player_b):
		raise PlayerException("players must be distinct.")
	else:
#both players lose a point for playing once
		p1.points -= 1
		p2.points -= 1
#each players gets their next move depending on style and other player hist
		x = p1.choose_move()
		y = p2.choose_move()
#records the move into each player's history
		p1.record_opponent_move(y)
		p2.record_opponent_move(x)
#if both players cooperate, both get two points
#otherwise no change in points happen
		if Move.__eq__(x, y) == True:
			if x == Move(True):
				p1.points += 2
				p2.points += 2
		else:
#if one player cheats and other cooperates
#the player who cheated gets 3 points while other loses 1 point
			if x == Move(True):
				p1.points -= 1
				p2.points += 3
			else:
				p2.points -= 1
				p1.points += 3

def run_game(player_a, player_b, num_turns=5):
	p1 = player_a
	p2 = player_b
#resets histories of both players
	p1.history = []
	p2.history = []
	i = 0
#if both players have the same id, returns an exception
	if id(player_a) == id(player_b):
		return PlayerException
#the players play against eachother until the i reaches the number of turns
	while i < num_turns:
		run_turn(player_a, player_b)
		i += 1