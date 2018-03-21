"""
Sample script to test ad-hoc scanning by table drive.
This accepts "term","test" and "long" words.
"""

def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	if words[pos] >= '0' and words[pos] <= '1': return '0-1'
	elif words[pos] == '2': return '2'
	elif words[pos] == '3': return '3'
	elif words[pos] >= '4' and words[pos] <= '5': return '4-5'
	elif words[pos] >= '6' and words[pos] <= '9': return '6-9'
	elif words[pos] == ':' or words[pos] == '.': return 'DOT'
	else: return 'OTHER'




def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""

	# initial state

	pos = 0
	state = 'q0'

	while True:

		c = getchar(text,pos)	# get next char

		if state in transition_table and c in transition_table[state]:

			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char


		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos


# the transition table, as a dictionary

td = {
		'q0' : {'0-1' : 'q1', '2' : 'q2', '3' : 'q3', '4-5' : 'q3', '6-9' : 'q3'},
		'q1' : {'DOT' : 'q4','0-1': 'q3', '2' : 'q3', '3' : 'q3' , '4-5' : 'q3','6-9' : 'q3'},
		'q2' : {'DOT' : 'q4', '0-1': 'q3', '2' : 'q3', '3' : 'q3' },
		'q3' : {'DOT' : 'q4'},
		'q4' : {'0-1': 'q5', '2' : 'q5', '3' : 'q5', '4-5' : 'q5'},
		'q5' : {'0-1': 'q6', '2' : 'q6', '3' : 'q6', '4-5' : 'q6', '6-9' : 'q6'}
     }

# the dictionary of accepting states and their
# corresponding token
ad = {'q6' : 'TIME_TOKEN'}

"""
inputs = ["00.00",'24:00','23:59',"123:45",'25.34','8.60','0:01']
for i in inputs :
	token,position= scan(i,td,ad)

	if token == 'ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',i)


	print("token:",token,"string:",i[:position])
#"""
# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0

	# get next token and position after last char recognized
	token,position= scan(text,td,ad)

	if token == 'ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break

	print("token:",token,"string:",text[:position])
	break

	# remaining text for next scan
text = text[position:]
