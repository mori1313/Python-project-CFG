import random
import requests

my_score = 0
computer_score = 0

stat_options = ["id","height","weight"]

games = 0

print("Welcome to Top Trumps- Pokemon style.")
player_mode = input("Would you like to play singleplayer or multiplayer mode?")
print("You have selected {} mode".format(player_mode))

if player_mode == "singleplayer":
    while games < 5:

        def chosen_pokemon():
            chosen_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(my_pokemon_name)
            chosen_response = requests.get(chosen_url)
            chosen_pokemon_info = chosen_response.json()

            return {
                'name': chosen_pokemon_info['name'],
                'id': chosen_pokemon_info['id'],
                'height': chosen_pokemon_info['height'],
                'weight': chosen_pokemon_info['weight'],
            }

        def random_pokemon():
            opp_pokemon_number = random.randint(1, 151)
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opp_pokemon_number)
            opp_response = requests.get(url)
            opp_pokemon = opp_response.json()
            return {
                'name': opp_pokemon['name'],
                'id': opp_pokemon['id'],
                'height': opp_pokemon['height'],
                'weight': opp_pokemon['weight'],   
            }

        opponent_pokemon = random_pokemon()

        if games == 0:
            pokemon_hand = []
            cards = 0
            while cards < 5 :
                pokemon_number = random.randint(1, 151)
                url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
                response = requests.get(url)
                pokemon = response.json()

                if pokemon['name'] not in pokemon_hand and pokemon['name'] != opponent_pokemon['name']:
                    pokemon_hand.append(pokemon['name'])
                    cards+=1

            print("CHOOSE YOUR FIGHTER. You have been given:")
            print(*pokemon_hand, sep="\n")
        else:
            pokemon_hand.remove(my_pokemon_name)
            cards = 4
            while cards < 5 :
                pokemon_number = random.randint(1, 151)
                url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
                response = requests.get(url)
                pokemon = response.json()

                if pokemon['name'] not in pokemon_hand and pokemon['name'] != opponent_pokemon['name']:
                    pokemon_hand.append(pokemon['name'])
                    cards+=1

            print("CHOOSE YOUR FIGHTER. Your new hand is:")
            print(*pokemon_hand, sep="\n")

            

        while 1:
            my_pokemon_name = input("Which Pokemon would you like to select?")

            if my_pokemon_name in pokemon_hand:
                my_pokemon = chosen_pokemon()
                print("Great,you have chosen: {}".format(my_pokemon_name))
                break
            else:
                print("Sorry, that pokemon is not an option, please choose another!")


        print('The opponent chose {}'.format(opponent_pokemon['name']))

        while 1:
            stat_choice = input("Which stat would you like to use? (id,height,weight)")

            if stat_choice in stat_options:
                my_stat = my_pokemon[stat_choice]
                opponent_stat = opponent_pokemon[stat_choice]
                break
            else:
                print("Sorry, that pokemon is not an option, please choose another!")



        if my_stat > opponent_stat:
            my_score+=1
            print("You Win this round! The opponents {} is {} but your's is {}.".format(stat_choice,opponent_stat,my_stat))
        elif my_stat < opponent_stat:
            computer_score+=1
            print("You Lose this round! The opponents {} is {} but your's is {}.".format(stat_choice,opponent_stat,my_stat))
        else:
            print("It's a draw! Both you and the opponent have a {} of {}.".format(stat_choice,my_stat))

        print("The overall scores are \n You: {} Opponent: {}".format(my_score,computer_score))
        games+=1


    if my_score > computer_score:
        print("Congratulations you won!!! In the end you scored {} and your opponent scored {}".format(my_score,computer_score))
    elif my_score < computer_score:
        print("Sorry, you lost!!! In the end you scored {} and your opponent scored {}. Better luck next time!".format(my_score,computer_score))
elif player_mode == "multiplayer":
    p1_score = 0
    p2_score = 0

    p1_name = input("Player 1, what is your name?")
    p2_name = input("Player 2, what is your name?")

    while games < 5:

        def p1_pokemon():
            chosen_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(p1_pokemon_name)
            chosen_response = requests.get(chosen_url)
            chosen_pokemon_info = chosen_response.json()

            return {
                'name': chosen_pokemon_info['name'],
                'id': chosen_pokemon_info['id'],
                'height': chosen_pokemon_info['height'],
                'weight': chosen_pokemon_info['weight'],
            }

        def p2_pokemon():
            chosen_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(p2_pokemon_name)
            chosen_response = requests.get(chosen_url)
            chosen_pokemon_info = chosen_response.json()

            return {
                'name': chosen_pokemon_info['name'],
                'id': chosen_pokemon_info['id'],
                'height': chosen_pokemon_info['height'],
                'weight': chosen_pokemon_info['weight'],
            }

        if games == 0:
            print("\n Round 1:")
            pokemon_hand1 = []
            cards1 = 0
            
            while cards1 < 5 :
                pokemon_number1 = random.randint(1, 151)
                url1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number1)
                response1 = requests.get(url1)
                pokemon1 = response1.json()

                if pokemon1['name'] not in pokemon_hand1:
                    pokemon_hand1.append(pokemon1['name'])
                    cards1+=1

            print("{} CHOOSE YOUR FIGHTER. You have been given:".format(p1_name.upper()))
            print(*pokemon_hand1, sep="\n")

            while 1:
                p1_pokemon_name = input("Which Pokemon would you like to select?")

                if p1_pokemon_name in pokemon_hand1:
                    p1_pokemon = p1_pokemon()
                    print("Great, you have chosen: {}".format(p1_pokemon_name))
                    break
                else:
                    print("Sorry, that pokemon is not an option, please choose another!")

            pokemon_hand2 = []
            cards2 = 0
            while cards2 < 5 :
                pokemon_number2 = random.randint(1, 151)
                url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number2)
                response2 = requests.get(url2)
                pokemon2 = response2.json()

                if pokemon2['name'] not in pokemon_hand2 and pokemon2['name'] not in pokemon_hand1:
                    pokemon_hand2.append(pokemon2['name'])
                    cards2+=1

            print("{} CHOOSE YOUR FIGHTER. You have been given:".format(p2_name.upper()))
            print(*pokemon_hand2, sep="\n")

            while 1:
                p2_pokemon_name = input("Which Pokemon would you like to select?")

                if p2_pokemon_name == p1_pokemon:
                    print("Sorry, that pokemon is not an option, please choose another!")
                    break
                elif p2_pokemon_name in pokemon_hand2:
                    p2_pokemon = p2_pokemon()
                    print("Great, you have chosen: {}".format(p2_pokemon_name))
                    break
                else:
                    print("Sorry, that pokemon is not an option, please choose another!")
        else:
            pokemon_hand1.remove(p1_pokemon_name)
            pokemon_hand2.remove(p2_pokemon_name)
            cards1 = 4
            cards2 = 4
            while cards1 < 5 :
                pokemon_number1 = random.randint(1, 151)
                url1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number1)
                response1 = requests.get(url1)
                pokemon = response1.json()

                if pokemon['name'] not in pokemon_hand1:
                    pokemon_hand1.append(pokemon['name'])
                    cards1+=1
            
            while cards2 < 5 :
                pokemon_number2 = random.randint(1, 151)
                url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number2)
                response2 = requests.get(url2)
                pokemon = response2.json()

                if pokemon['name'] not in pokemon_hand1 and pokemon['name'] not in pokemon_hand2:
                    pokemon_hand2.append(pokemon['name'])
                    cards2+=1

            print("{} CHOOSE YOUR FIGHTER. Your new hand is:".format(p1_name))
            print(*pokemon_hand1, sep="\n")

            while 1:
                p1_pokemon_name = input("Which Pokemon would you like to select?")

                if p1_pokemon_name in pokemon_hand1:
                    p1_pokemon = p1_pokemon()
                    print("Great, you have chosen: {}".format(p1_pokemon_name))
                    break
                else:
                    print("Sorry, that pokemon is not an option, please choose another!")

            print("{} CHOOSE YOUR FIGHTER. Your new hand is:".format(p2_name))
            print(*pokemon_hand2, sep="\n")

            while 1:
                p2_pokemon_name = input("Which Pokemon would you like to select?")

                if p2_pokemon_name == p1_pokemon:
                    print("Sorry, that pokemon is not an option, please choose another!")
                    break
                elif p2_pokemon_name in pokemon_hand2:
                    p2_pokemon = p2_pokemon()
                    print("Great, you have chosen: {}".format(p2_pokemon_name))
                    break
                else:
                    print("Sorry, that pokemon is not an option, please choose another!")


        stat_choices = ['id', 'height', 'weight']
        ran_stat_choice = stat_choices[random.randint(0,2)]
        print('The stat chosen to compete is: {}'.format(ran_stat_choice))

        p1_stat = p1_pokemon[ran_stat_choice]
        p2_stat = p2_pokemon[ran_stat_choice]

        if p1_stat > p2_stat:
            p1_score+=1
            print("{} wins this round! {}'s {} is {} and {}'s is {}.".format(p1_name,p1_name,ran_stat_choice,p1_stat,p2_name,p2_stat))
        elif p1_stat < p2_stat:
            p2_score+=1
            print("{} wins this round! {}'s {} is {} and {}'s is {}.".format(p2_name,p2_name,ran_stat_choice,p2_stat,p1_name,p1_stat))
        else:
            print("It's a draw! Both {} and the {} have a {} of {}.".format(p1_name, p2_name,ran_stat_choice,p1_stat))

        print("The scores are now: \n{}: {} \n{}: {}".format(p1_name,p1_score,p2_name,p2_score))

        advance = input("Would you like to continue to the next round? (y/n")
        if advance == 'y':
            games+=1
            print('next round loading...')
            print("\n")
        else:
            if p1_score > p2_score:
                print("Congratulations {} you won!!! In the end you scored {} and {} scored {}. \n Better luck next time {}!".format(p1_name,p1_score,p2_name,p2_score, p2_name))
                break
            elif my_score < computer_score:
                print("Congratulations {} you won!!! In the end you scored {} and {} scored {}. \n Better luck next time {}!".format(p2_name,p2_score,p1_name,p1_score, p1_name))
                break
            else:
                print("It's a draw!!! In the end you both scored {}.".format(p1_score))
                break
else:
    "Sorry that's not an option, please refresh and try again!"       

print('You have finished the game. Thank you for playing Top Trumps Pokemon Edition!')
