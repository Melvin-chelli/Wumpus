
class Action(object):
    def __init__(self, name:str, direction:str = ''):
        self.name = name
        self.direction = direction

    def __repr__(self,) ->str :
        return str(self.name)

table_of_actions = {
    'KU': Action('move', 'N'),
    'KD': Action('move', 'S'),
    'KR': Action('move', 'L'),
    'KL': Action('move', 'O'),
    'P': Action('pickup'),
    'SR': Action('shoot', 'L'),
    'SL': Action('shoot', 'O'),
    'SU': Action('shoot', 'N'),
    'SD': Action('shoot', 'S')
}