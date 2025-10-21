# Operators
def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"

# Initial State
initial_state = {
    'monkeyAt': 0,
    'monkeyLevel': 'Down',
    'bananaAt': 1,
    'boxAt': 2
}

# Goal State
goal_state = {
    'GetBanana': True,
    'monkeyAt': 1
}

# Planning Algorithm
def plan_actions(initial_state, goal_state):
    actions = []
    
    # Step 1: Move monkey to banana location
    if initial_state['monkeyAt'] != goal_state['monkeyAt']:
        actions.append(move('Monkey', initial_state['monkeyAt'], goal_state['monkeyAt']))
        initial_state['monkeyAt'] = goal_state['monkeyAt']  # Update state

    # Step 2: Move box to banana location if it's not already there
    if initial_state['boxAt'] != initial_state['bananaAt']:
        actions.append(push_box(initial_state['boxAt'], initial_state['bananaAt']))
        initial_state['boxAt'] = initial_state['bananaAt']

    # Step 3: Climb box
    if initial_state['monkeyLevel'] == 'Down':
        actions.append(climb_box(initial_state['boxAt'], 'Up'))
        initial_state['monkeyLevel'] = 'Up'

    # Step 4: Grab banana
    if initial_state['monkeyLevel'] == 'Up' and initial_state['monkeyAt'] == initial_state['bananaAt']:
        actions.append(have_banana(initial_state['bananaAt']))
        initial_state['GetBanana'] = True

    return actions

# Execute the planning algorithm
actions = plan_actions(initial_state, goal_state)

# Print the actions in the plan
print("Plan:")
for action in actions:
    print(action)
