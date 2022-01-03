
class Action(object):
    def __init__(self, name:str, direction:str = ''):
        self.name = name
        self.direction = direction

    def __repr__(self,) ->str :
        return str(self.name)

table_of_actions = {
    'KU': Action('move', 'U'),
    'KD': Action('move', 'D'),
    'KR': Action('move', 'R'),
    'KL': Action('move', 'L'),
    'P': Action('pickup'),
    'SR': Action('shoot', 'R'),
    'SL': Action('shoot', 'L'),
    'SU': Action('shoot', 'U'),
    'SD': Action('shoot', 'D')
}