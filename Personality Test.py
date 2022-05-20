import random
from PIL import Image
questions_list = ['''You have a day off (finally). What activity will you undoubtedly participate in? \nA) Off to see the newest movie! \nB) Catching up on a personal project. A painting? Some cool coding project?\n   I won't tell you what to do.\nC) Hitting the gym, climbing a mountain, wrestling bears or all of the above.\nD) Time to shoot the shit with some friends >:)\n''',
                  '''\nOne word to describe yourself is...\nA) Invigorating\nB) Alluring\nC) Dynamic\nD) Amicable\n''',
                  '''\nWhat is so NOT a vibe...?\nA) Time\nB) Humidity\nC) Turbulence\nD) Apex predators\n''',
                  "\nWhat is SO a vibe...?\nA) Concrete and Lime. Mortar is yummy too ^w^\nB) I would sell a kidney for a can of varnish rn.\nC) A truck-wide length of asphalt as far as the eye could see.\nD) Fresh grass to munch on and a shallow, slow-moving water source. ",
                  "\nA kid is crying after having his toy stolen by another kid. You...\nA) Whip out the popcorn. \nB) Help the child build a case and press charges.\nC) Settle the dispute by organizing an arm wrestle between the victim and perpetrator.\nD) Oh nooo Timmy :(( Let's go talk to them. Wait, they called you a butthead?\n   Alright, I'll handle it. In the meantime, let's get you another toy. :))\n",
                  "\nWhat does happiness mean to you?\nA) Parties, sight-seeing tours, concerts, movies, shows, sports\nB) Professional success, galas, Rolls Royce and Rolexes, Carribbean business trips\nC) Skyscrapers, early morning runs, styled faux cuts, leather jackets\nD) Hot chocolate, cozy blankets, baked potatoes, sunny days, hot springs" ,
                  "\nIn quantum physics, tunneling is a phenomenon in which particles penetrate a potential energy barrier with a height greater than the total energy of the particles, violating the principles of classical mechanics.\nWhy do you think this happens? \nA) Systems tends towards highest entropy. But who knows ://\nB) Radiation and potential energy to kinetic energy conversions and Einstein and Physics Words:TM:\nC) Little matter balls go zoom zoom\nD) Maybe they just politely asked the barrier to move >///<",
                  "\nLook, if you had... One shot. Or one opportunity. To seize everything you ever wanted, in one moment...\nWould you capture it? Or just let it slip? (Yo)\nA) His palms are sweaty, knees weak, arms are heavy\nB) There's vomit on his sweater already, mom's spaghetti\nC) He's nervous, but on the surface he looks calm and ready\nD) To drop bombs, but he keeps on forgettin'",
                ]
def run_test():
    print("\nWelcome to the \x1B[3mWhat Are You\x1B[0m Personality Test. \nWhat, you thought you were a human being?"
          "\nBorinnnnngggg - you are what this test says you are. Ready to start? Type y for yes, n for no and hit enter.\n")
    y_n = input()
    if y_n == 'y' or y_n == 'Y':
        pass
    else:
        print("\nAh. Well, I'll still be here when you are!")
        return

    data = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    for q in questions_list:
        answer = input(q)
        if answer == 'a' or answer == 'A':
            data['a'] += 1
        if answer == 'b' or answer == 'B':
            data['b'] += 1
        if answer == 'c' or answer == 'C':
            data['c'] += 1
        if answer == 'd' or answer == 'D':
            data['d'] += 1



#Randomizes answers if user answers the same number of times for multiple options - 3A, 3B for instance
    max_key = max(data, key=data.get)
    list = []
    for key in data:
        if data[key] == data[max_key]:
            list.append(key)
    item = random.choice(list)

#Print results:

    print("\nYou are...\n")
    if item == 'a':
        print('THE ROMAN COLOSSEUM\n')
        IMGa = Image.open("C:/Users/16476/OneDrive/Documents/PYTHON PIL IMAGE MANIPULATION/colosseum.jpg")
        IMGa.show()
        print("Lookit you! One of the Seven Wonders of the world! Hope you don't mind sitting on top of a labyrinth and being absolutely K/O'd by an earthquake in 1349. Never forget. :'(")
    if item == 'b':
        print('A COCOBOLO TABLE\n')
        IMGb = Image.open("C:/Users/16476/OneDrive/Documents/PYTHON PIL IMAGE MANIPULATION/Cocobolo.jpg")
        IMGb.show()
        print("Cocobolo wood is one of the most expensive wood materials in the world. Thus, apart from being highly durable and twice the weight of walnut, you're also bougie asf <3. Slayyy queen~ ")
    if item == 'c':
        print('LOCKHEED YF-12 FIGHTER JET')
        IMGc = Image.open("C:/Users/16476/OneDrive/Documents/PYTHON PIL IMAGE MANIPULATION/YF-12A.jpg")
        IMGc.show()
        print("Legends has it that the YF stands for Ya Fooked (for messing with this high-altitude American fighter jet). Anyway, please teach me how to reach Mach 3+ UWU")
    if item == 'd':
        print('A CAPYBARA')
        IMGd = Image.open("C:/Users/16476/OneDrive/Documents/PYTHON PIL IMAGE MANIPULATION/capybara.jpg")
        IMGd.show()
        print("Pro business idea: buy a cuddle, get a hug FREE. You are just that cute!")



''' Answers - the Colosseum (A), a Cocobolo table (B), Lockheed YF-12 Fighter Jet (C), a capybara (D) '''



if __name__ == '__main__':
    run_test()

