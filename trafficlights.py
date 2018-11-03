import time

class state:
	def __init__(self,next_state,state_time,ns_color,ew_color):
		self.n_state=next_state
		self.delay=state_time
		self.ns=ns_color
		self.ew=ew_color
		
states=[]
states.append(state(1,1.0,"red","red"))
states.append(state(2,4.0,"green","red"))
states.append(state(3,2.0,"yellow","red"))
states.append(state(4,1.0,"red","red"))
states.append(state(5,4.0,"red","green"))
states.append(state(6,2.0,"red","yellow"))

state_variable=0

def do_state():
	global state_variable
	print(states[state_variable].ns,states[state_variable].ew)
	time.sleep(states[state_variable].delay)
	state_variable=states[state_variable].n_state
	
for bob in range(10):
	do_state()