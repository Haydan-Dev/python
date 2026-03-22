import re


pattern = r"[0-9]"

text = '''
Chris Redfield is a character in Resident Evil (Biohazard in Japan), a survival horror video game series created by the Japanese company Capcom. 
He was introduced as one of the two playable characters of the original Resident Evil, 
which was released on March 22, 1996, appearing with his partner Jill Valentine as members of the Raccoon Police Department's Special Tactics and Rescue Service (S.T.A.R.S.) unit. 
Chris and Jill fight against the Umbrella Corporation, 
which creates zombies and other bio-organic weapons through bioterrorism. Later, the pair become founding members of the United Nations' Bioterrorism Security Assessment Alliance (BSAA). 
Chris is the protagonist in several Resident Evil games, novels, and films, and has also appeared in other game franchises. 
In later games, his features were based on New Zealand model Geordie Dandy. Critics have been polarized in their discussions of Chris, and several publications consider him one of the sexiest video game characters. 
The World Baseball Classic concludes with Venezuela defeating the United States in the final (tournament MVP Maikel García pictured).
In association football, the Confederation of African Football overturns the 2025 Africa Cup of Nations final originally won by Senegal, declaring Morocco the winner of the tournament.
In Kazakhstan, voters approve a new constitution in a referendum.
Denis Sassou Nguesso is proclaimed the winner of the Republic of the Congo presidential election.
Ongoing: Afghanistan–Pakistan conflictIran warRusso-Ukrainian war timelineSudanese civil war timeline
Recent deaths: Rhoda RobertsMichael Bambang HartonoIlia II of GeorgiaDavid KeeneSalih MuslimLen Deighton
More current eventsNominate an article
'''
match = re.search(pattern,text)
print(match)

