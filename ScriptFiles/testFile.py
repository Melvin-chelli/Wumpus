from WumpusGame import game, environment
test_env = environment.Environment(dimension=10, n_pits=9)
test_game = game.Game(test_env, gui_enabled = True)

weights = [
    1000,  # got_gold
    500,  # wumpus_died
    70,  # escaped
    -10,  # agent_died
    -0.5,  # size
    2,    # hits
    -2,   # errors
    -2,   # distance
    -2,   # fadigue
]

w1, w2, w3, w4, w5, w6, w7, w8 ,w9 = weights

# status = [
#     got_gold,
#     wumpus_died,
#     escaped,
#     agent_died,
#     size,
#     hits,
#     errors,
#     distance,
#     fatigue
# ]
#
# def FitnessFunc(status: status)->int

test_game.start()
