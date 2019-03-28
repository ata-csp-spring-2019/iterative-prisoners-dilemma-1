team_name = 'R32 Gang'

strategy_name = 'Wombo Combo'

strategy_description = 'Collude first round. Collude, except in a round after getting betrayed'

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    else:
        return 'c'