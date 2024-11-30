import random
player_1 = input("Enter Player-1 name => ")
player_2 = input("Enter Player-2 name => ")
print(f"Hello {player_1.capitalize()} and {player_2.capitalize()}, time to play ^_^")
lives = int(input("Lives? => "))
secret_word = input(f"{player_1.capitalize()}, write your secret word here => ")


for i in ("|" * 30):
    print(i)
print(f"{player_2.capitalize()}, your task is finding the secret word!")
print(len(secret_word), "letters =>", len(secret_word) * "_")


character_left = len(secret_word)
word_list_have = set()
word_list_used = set()
space = [" "] * len(secret_word)
possible_hints = []
hint = {
    "Afganistan": "Kabil",
    "Almanya": "Berlin",
    "Arjantin": "Buenos Aires",
    "Arnavutluk": "Tiran",
    "Angola": "Luanda",
    "Avustralya": "Canberra",
    "Azerbaycan": "Bakü",
    "Bahreyn": "Manama",
    "Bangladeş": "Dakka",
    "Belçika": "Brüksel",
    "Birleşik Arap Emirlikleri": "Abu Dabi",
    "Brezilya": "Brasilia",
    "Bulgaristan": "Sofya",
    "Cezayir": "Cezayir",
    "Çekya": "Prag",
    "Çin": "Pekin",
    "Danimarka": "Kopenhag",
    "Dominik Cumhuriyeti": "Santo Domingo",
    "Ekvador": "Quito",
    "Endonezya": "Cakarta",
    "Ermenistan": "Erivan",
    "Estonya": "Tallinn",
    "Etiyopya": "Addis Ababa",
    "Fas": "Rabat",
    "Filipinler": "Manila",
    "Finlandiya": "Helsinki",
    "Fransa": "Paris",
    "Gana": "Akra",
    "Güney Afrika": "Pretoria",
    "Güney Kore": "Seul",
    "Gürcistan": "Tiflis",
    "Hindistan": "Yeni Delhi",
    "Hollanda": "Amsterdam",
    "Hırvatistan": "Zagreb",
    "İngiltere": "Londra",
    "İran": "Tahran",
    "İspanya": "Madrid",
    "İsrail": "Kudüs",
    "İsveç": "Stockholm",
    "İsviçre": "Bern",
    "İtalya": "Roma",
    "Jamaika": "Kingston",
    "Japonya": "Tokyo",
    "Kamboçya": "Phnom Penh",
    "Kanada": "Ottawa",
    "Katar": "Doha",
    "Kenya": "Nairobi",
    "Kırgızistan": "Bişkek",
    "Kolombiya": "Bogota",
    "Kosta Rika": "San Jose",
    "Küba": "Havana",
    "Letonya": "Riga",
    "Lübnan": "Beyrut",
    "Litvanya": "Vilnius",
    "Macaristan": "Budapeşte",
    "Meksika": "Meksiko",
    "Mısır": "Kahire",
    "Moğolistan": "Ulan Batur",
    "Nepal": "Katmandu",
    "Nijerya": "Abuja",
    "Norveç": "Oslo",
    "Pakistan": "İslamabad",
    "Panama": "Panama",
    "Peru": "Lima",
    "Polonya": "Varşova",
    "Portekiz": "Lizbon",
    "Romanya": "Bükreş",
    "Rusya": "Moskova",
    "Senegal": "Dakar",
    "Sırbistan": "Belgrad",
    "Singapur": "Singapur",
    "Slovakya": "Bratislava",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Sudan": "Hartum",
    "Suudi Arabistan": "Riyad",
    "Suriye": "Şam",
    "Şili": "Santiago",
    "Tayland": "Bangkok",
    "Tunus": "Tunus",
    "Türkiye": "Ankara",
    "Uganda": "Kampala",
    "Ukrayna": "Kiev",
    "Umman": "Maskat",
    "Uruguay": "Montevideo",
    "Ürdün": "Amman",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yemen": "Sana",
    "Yeni Zelanda": "Wellington",
    "Yunanistan": "Atina",
    "Zambiya": "Lusaka",
    "Zimbabve": "Harare"
}
index = 0


while lives > 0:
    possible_hints.clear()
    index = 0
    
    if character_left != 0:
        for country, capital in hint.items():
            if capital[0].lower() in secret_word.lower() and capital[0].lower() not in word_list_have:
                possible_hints.append(country)
        
        if not possible_hints == []:
            hint_country = random.choice(possible_hints)
            print("-" * 40)
            print(f"HINT!: First letter of the capital of {hint_country}.")

        if possible_hints == []:
            print("-" * 40)
            print("We have not a hint.")
    
        guess = input("Guess a letter: ")

        if guess in secret_word.lower():
            word_list_have.add(guess)
            character_left -= secret_word.lower().count(guess)
            print(f"{len(word_list_used)} False letters => {", ".join(list(word_list_used))}")
            
            while index < len(secret_word):
                if secret_word[index] == guess:
                    space[index] = guess
                     
                index += 1
                
            print(f"secret word => {"".join(space)}")
            print(" " * 15 + "^" * len(secret_word))
                

        else:
            word_list_used.add(guess)
            lives -= 1
            print("Wrong!")
            print(f"You have {lives} lives")
            print(f"{len(word_list_used)} False letters => {", ".join(list(word_list_used))}")
            print(f"secret word => {"".join(space)}")
            print(" " * 15 + "^" * len(secret_word))
        

    else:
        print("-" * 40)
        print(15 * " " + len(secret_word) * "v")
        print(f"secret word => {secret_word} ")
        print(15 * " " + len(secret_word) * "^")
        print(f"{player_2.capitalize()} won.")
        break
        

if lives == 0:
    print(f"{player_1.capitalize()} won, answer is {secret_word}.") 


        
            
        

       




        


      
       

        
            

   