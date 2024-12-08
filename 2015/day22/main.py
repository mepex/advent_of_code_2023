from itertools import combinations
import logging

# Configure the logger
logging.basicConfig(filename='my_log.log', level=logging.DEBUG, filemode='w',
                    format='%(levelname)s - %(message)s')


# cost, damage, armor, health, mana
spells = {'M': (53, 4, 0, 0, 0),
          'D': (73, 2, 0, 2, 0),
          'S': (113, 0, 7, 0, 0),
          'P': (173, 3, 0, 0, 0),
          'R': (229, 0, 0, 0, 101)}

start_timer = {'S': 6, 'P': 6, 'R': 5}

#state = {'turn': 0, 'p_hp': 10, 'p_mana': 250, 'b_hp': 13, 'b_d': 8, 'mana_spent': 0}
state = {'turn': 0, 'p_hp': 50, 'p_mana': 500, 'b_hp': 51, 'b_d': 9, 'mana_spent': 0}

spell_timer = start_timer.copy()
spell_active = {'S': False, 'P': False, 'R': False}

# if we only cast recharge, then 2xmissile, then recharge, then 2xmissle, this maximizes mana
# and we get to turn 11 where we have 563 mana.  So the max we could possibly spend is
# 3 * 229 + 3 * 53 + 10 * 101 = 1856
# if we only cast shield we last a lot longer, but run out of mana quickly
# basically impossible to have more than 15 turns
def sim(actions):
    boss_hp, boss_dmg = 51, 9
    hp, mana, armor = 50, 500, 0
    turn = 0
    mana_spent = 0
    poison_left, shield_left, recharge_left = 0, 0, 0
    spell_cost = {'M': 53, 'D': 73, 'S': 113, 'P': 173, 'R': 229}

    while True:
        if not len(actions):
            print("out of moves")
            return 0
        if poison_left:
            poison_left = max(poison_left - 1, 0)
            boss_hp -= 3
        if shield_left:
            shield_left = max(shield_left -1, 0)
            armor = 7
        else:
            armor = 0
        if recharge_left:
            recharge_left = max(recharge_left - 1, 0)
            mana += 101
        if turn % 2:
            act = actions[turn // 2]
            mana -= spell_cost[act]
            if mana < 0:
                return 0
            mana_spent += spell_cost[act]
            if act == "M":
                boss_hp -= 4
            elif act == 'D':
                boss_hp -= 2
                hp += 2
            elif act == 'S'
                if shield_left:
                    return 0
                shield_left = 6
            elif act == 'P':
                if poison_left:
                    return 0
                poison_left = 6
            elif act == 'R':
                if recharge_left:
                    return 0
                recharge_left = 5
        if boss_hp <= 0:
            return mana_spent
        if not turn % 2:
            hp -= max(boss_dmg - armor, 1)
            if hp <= 0
                return 0
        turn += 1


def iterate_actions(pos):
    actions[pos] = 'DSPRM'['MDSPR'.index(actions[pos])]
    if actions[pos] == 'M':
        if pos + 1 <= len(actions):
            iterate_actions(pos + 1)

actions = ['M'] * 15
min_spent = 1e6
for i in range(1e6):
    result = sim(actions)
    if result:
        min_spent = min(result, min_spent)



















def play(state, spell_active, spell_timer, history):
    global spells, start_timer, best_spend
    if state['p_mana'] < 53:
        logging.info(f"**LOSE BY MANA**")
        return False, -1
    armor = 0
    has_win = False

    while True:
        if state['mana_spent'] >= best_spend:
            logging.info(f"**BETTER WIN EXISTS {state['mana_spent']}")
            return False, -2
        for k,v in spell_active.items():
            if v:
                act = spells[k]
                state['b_hp'] -= act[1]
                armor = act[2]
                state['p_mana'] += act[4]
                spell_timer[k] -= 1
                if spell_timer[k] == 0:
                    spell_active[k] = False
                    spell_timer[k] = start_timer[k]
                logging.info(f"{state['turn']} : {k} {spell_timer[k]}")
                if state['b_hp'] <= 0:
                    logging.info(f"**WIN BY KILL {state['mana_spent']} {history}")
                    return True, state['mana_spent']
        if not state['turn'] % 2:
            for k,v in spells.items():
                next_state = state.copy()
                # immediate spell
                if k not in start_timer.keys():
                    next_state['p_mana'] -= v[0]
                    next_state['mana_spent'] += v[0]
                    next_state['b_hp'] -= v[1]
                    next_state['p_hp'] += v[3]
                    next_state['turn'] += 1
                    if next_state['b_hp'] <= 0:
                        best_spend = state['mana_spent']
                        logging.info(f"**WIN BY KILL {state['mana_spent']} {history}")
                        return True, best_spend
                    if next_state['mana_spent'] >= best_spend:
                        logging.info(f"**BETTER WIN EXISTS {best_spend} {next_state['mana_spent']}")
                        return False, -2
                    logging.info(f"{state['turn']} : Cast {k} {next_state}")
                    history.append((k, state['turn']))
                    win, mana_spent = play(next_state, spell_active, spell_timer, history)
                    best_spend = mana_spent if win and mana_spent < best_spend else best_spend
                    # if we've already spent more than the win, can trim this branch
                    if win and best_spend < state['mana_spent']:
                        logging.info(f"**WIN {mana_spent}")
                        return win, best_spend
                    has_win = win
                    history.pop()
                else:
                    next_spell_active = spell_active.copy()
                    if not spell_active[k]:
                        next_spell_active[k] = True
                        next_state['mana_spent'] += spells[k][0]
                        history.append((k, state['turn']))
                        next_state['turn'] += 1
                        if next_state['mana_spent'] >= best_spend:
                            logging.info(f"**BETTER WIN EXISTS {best_spend} {next_state['mana_spent']}")
                            return False, -2
                        logging.info(f"{state['turn']} : Cast {k} {next_state}")
                        win, mana_spent = play(next_state, next_spell_active, spell_timer, history)
                        best_spend = mana_spent if win and mana_spent < best_spend else best_spend
                        if win and mana_spent < state['mana_spent']:
                            logging.info(f"**WIN {mana_spent}")
                            return win, best_spend
                        has_win = win
                        history.pop()
            if has_win and best_spend < state['mana_spent']:
                logging.info(f"**WIN {best_spend}")
                return win, best_spend
            state['turn'] += 1
        else:
            dam = 1 if state['b_d'] - armor <= 0 else state['b_d'] - armor
            state['p_hp'] -= dam
            if state['p_hp'] <= 0:
                logging.info(f"**LOSE BY DEATH**")
                return False, 0
            state['turn'] += 1


best_spend = 1e6
win, mana_spent = play(state, spell_active, spell_timer, [])

print(f"part 1: {best_spend}")
