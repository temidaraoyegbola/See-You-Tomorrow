# The script of the game goes in this file.

# Characters

define pov = Character("[povname]") 
define Ray = Character("Ray")
define Juno = Character("Juno")
define Tina = Character("Tina")
define Bayo = Character("Bayo")
define Principal = Character("Principal")

# Variables
default joy_points=0
default asked_clubs=False
default asked_teachers=False
default asked_rules=False



# The game starts here.

label start:
    Ray "OhmygoshIshould'vejustwokenupwhenthe13thalarmrangnotthe14thI'msostupidandsolate!!! >n<"

    "Says the girl currently sprinting past you, who also woke up late, is late to school." 
    "You know this is your FIRST DAY of school, right?"
    "Seriously? Late on your first day? "
    "Cooked. "
    "Fried even."
    #(Fade in and out when background scenes)
    "So now here you are..."
    "In the principal's office, with the girl you saw earlier."
    Principal "So… late again, Ray?"

    Ray "Gulp. Um. Hear me out."

    Principal "Go on…"

    Ray "..."

    Ray  "Never mind."

    Principal "*Sigh* And you are…?"

    $ povname= renpy.input("Name: ",length=32)
    $ povname=povname.strip()
    pov "My name is [povname]."

    if not povname:
        $ povname= "Bug"

    Principal "Ah yes, the new student."

    Principal "Let's see..."

    Principal "Ray, as punishment for your lateness…"

    Principal "... and definitely not because I ran out of tardy papers…"

    Ray "Tehee."

    Principal "Ray, give them a tour around the school."

    Ray "ABSOLU–"

    Ray "Wait a minute."

    Ray "I'll be counted absent!"

    Principal "You should have considered that before you came late."

    Ray "Awhh… well then. [povname], was it? Welcome to *insert name*"

    Ray "Come on, come on! The school may be a little small but you'll love it here!"

    Ray "Everybug is so fun and friendly! Hurry!"

    "So off you and this orange bug go. As she merrily leads you along the way, you notice that she's always saying hello to somebug in the hallways. As well as a wave when she shows you the classrooms."
    
    "Ray is correct, the school is indeed small." 

    "Small enough that if anyone embarrassed themself, the whole school would know before lunch."

    "Don't be nervous or anything."

    "No reason to be. :)"

    "Every classroom looked alive." 

    "Forgotten hoodies on chairs…"

    "Posters…"

    "A very specific 'Let's Larp' sticker that popped up out of nowhere every so often…"

    "Maybe switching school's midway wasn't so bad."

    Ray "So there is the Gym! The only fun thing about gym to me is dodgeball and open gym when we get to walk around and do whatever we want oh oh and there's the theatre room–" 

    Ray "Hello Ms. Norbury! Do you need anyone for the club?? Oh are you a theatre kid? You seem like a theatre kid–"

    Ray "This is the music room! Juno hangs in here a lot, I do too sometimes. If you ever can't find both of us, that's where we'll be!"

    Ray "We kinda take naps in there SOMETIMES so maybe don't be too loud when you walk in–"

    Ray "This room is the science room… actually lets go past that room not because I was late or anything and this–"

label tour_questions:

    menu:

        "Clubs" if not asked_clubs:
            $ asked_clubs= True
            call clubs
            jump tour_questions

        "Teachers" if not asked_teachers:
            $ asked_teachers= True
            call teachers
            jump tour_questions

        "Rules" if not asked_rules:
            $ asked_rules= True
            call rules
            jump tour_questions

        "Let's keep going" if asked_clubs and asked_teachers and asked_rules:
            jump continue_tour 

label clubs:
    Ray "Clubs! There are A BUNCH of clubs here believe it or not!"

    Ray "Art club, Gardening club, Theatre Club, Art club, Music club, Literature club, Student council, Art club, Art club, Art club… did I mention art club?"

    Ray "You should join the Art club, it's so much fun. We do more than just art!"

    "I think she likes art guys, but I'm not sure. It can't possibly be the paint stains, right?"

    return

label teachers:
    Ray  "Depending on who you get, you can go from 'I will never miss this teacher's class' to 'I hope they're not here today' teehee."

    Ray "My favorite? It's obviously Mr. Becker! Sure he's the school's music sponsor, but still! He's somebug you can talk to and be your fun, silly self around."

    Ray "Plus he taught math last year and I would get sleepy in his class sometimes… but he never scared me into waking up!! I wish more teachers did that!"

    Ray "Mrs. Rachael is my second favorite! She's the art club sponsor AND english teacher!! She is quite literally art personified."

    Ray "I wish I was art… pretty and lovely and useful…"

    Ray "L-Like pottery! I want to be a fancy teacup!"

    Ray "What would you be if you were art??"

    $ arthing= renpy.input("What would you be if you were art? ")
    $ arthing = arthing.strip()

    if arthing== "":
        $ arthing= "masterpiece" 

    Ray "A [arthing]?"

    Ray "That sounds cool! It fits you."

    Ray "Don't ask me how I know."

    Ray "I just know. :~)"

    Ray "That's so creative of you!"    

    Ray "Creative… hmmm…"

    Ray "Join art club…"

    return

label rules:
    Ray "Rules are pretty standard, common sense really. Though common sense isn't common…"

    Ray "Ah! Sorry! I'm not trying to call you an idiot!! Uh– I mean– I'm sorry I'll stop–"

    Ray "So uh rules: no cellphones in class, keep hands to yourself," 

    Ray "Be here on time…"

    Ray "..."

    Ray "Moving on!"

    Ray "The most important rule! Be yourself and be kind, don't ever change who you are to fit somebug else's mold."

    Ray "You are the mold."

    Ray "You da real mold."

return

label continue_tour:

    Ray "Glad I could answer everything!"

    Ray "If you have any questions, let me know!"

    Ray "Tehehehe I am so useful. >:3"

    Ray "Oh- hi Raeya!! That moth cape is so pretty woah…"


    "So the tour should've at least taken a good 10 minutes, 15 if you're generous right?"

    "WRONG."

    "It takes 32 minutes." 

    "Ray waved at every single person you passed."

    "Some of them twice."

    "By the time the tour was done, first period had ended. Great. Late on your first day AND completely missed first period?"

    "You must be a REAL LUCKY fellow, aren't ya?"
    Ray "Wa?! First period's already over?! Oh gosh I'm such an idiot."

menu:
    "Don't sweat it, you're not an idiot.":
        $ joy_points+=1
    "Considering you saved me from introducing myself at 8 a.m. to a bunch of teens… it's all good.":
        $ joy_points+=1
    "...":
        $ joy_points-=1

"A voice behind you laughs."

Juno "Well, well, well. No wonder I didn't hear snoring in history."

Juno "Good morning ankle biter, isn't it too early to be kidnapping new kids?"

Ray "JUNO!!! Good mor-"

Ray "HEY! Ankle biter???????? And- I do not snore!"

Ray "Don't listen to him [povname] they just hate me and want me to die."

Juno "Ouch, heartbroken. You won't even introduce me to the new kid? Cruel. I thought we were friends."

Ray "Oh! Yes! [povname] this is Juno. Juno, this is [povname]."

Juno "Heya there. You come here often?"

Ray "JUNO!"

Juno "I'm joking! I'm joking! Welcome to *insert name.* You should come sit with us at lunch."

Ray "Yes! You should! I made sugar cookies! Pony shaped!"

Juno "Sweet. Let me just…"

"Juno attempts to reach into Ray's lunchbox. Ray smacked his hand away. This is a normal experience it seems."

"The bell is ringing again."

Ray "Oh bugs the bell! I'll be late again to maths and be bonked on the head…!!"

Juno "Off she goes… What class do you have next? Physics? Same. Come on then, new kid. I brought an extra pillow. You can use it if you fall asleep."

Juno "Trust me. You will."

"Seems you won't be subjected to missing another class."

"Much to your surprise, Juno was right. As soon as the teacher opened their mouth… your eyes had closed to the world. Great first impression, am I right? The sleepy new kid."

"Look at you, already setting a record. Way to go."

"Juno DID have that extra pillow surprisingly. Placed it down the desk, the second he saw your eyes droop."

"By the time you woke up again, Juno was helping you pack up."

Juno "Finally up huh? Good morning. Welcome to the Land of the Almost Living. Almost because trust me, no one wants to be awake right now."

"To say that he'd be wrong would be a lie. It's 11 a.m. in the morning. If it were still summer, you'd still be in bed."

"Ray was waiting outside the classroom door."

Ray "Hello again!!! Sorry- I got excited thinking about the new face at our table and the sugar cookies and sharing–"

Juno "Sharing? That's what we're calling the part where you eat 5 of them and say ‘hey I baked it I get most of it'?"

Ray "I have noooooooo idea what you are talking about! I am so generous and lovable!"

Juno "Uh huh, sure. Come on [povname]."

Ray "Are we eating outside again? Please say yes! Pleasepleasepleaseplease–"

Juno "Aren't you scared a bird will eat you? For someone your height, you should be more scared of everything."

Ray "Wha– MEAN!!!"

Juno "Besides, Bayo wanted to eat inside today."

Juno "You know how she is with the sun."

Ray "True…"

#Fade out 

"At lunch…"

"You three sat at a table by the window, Juno and Ray didn't even ask if you wanted to sit with them."

"Like it was already expected."

"You were already a part of the group."

"You should probably be worried though, as they say…"

Ray "What comes in…"

Ray "Never comes in…"

Juno "You mean never comes out?"

Ray "Uh… yes!! That is exactly what I meant!!"

Ray  "I know! I just wanted to make sure… YOU know!!"

Juno "Mhm. Sure."

"Juno reached over for a sugar cookie casually."

"He hasn't touched any of his food yet. The cookie was first."

"Someone's priorities are straight."

Juno "So, new kid, tell us about yourself. I'm curious."

Ray "Yes, yes! Tell us all about it! And what you like to do!"

Ray "And what you like to eat! And what club you want to join!"

Ray "You should join Art Club!"

Juno "They pay you to say that, huh?"

Ray "Nuh-uhhhh!"

Juno "Ray is VP of that club. She's always trying to recruit  more people."

Ray "Art club is the best club ever! Of course I'm always going to try and recruit more people."

Juno "Hmmm… I think Music Club is better."

Ray "Nuh-uhhhhh. We hear you lot from across the school."

Ray "It's still really cool though… but Art Club is better!"

Juno "And why is that?"

Ray "Because I say so! Join Art Club!"

Juno "You should join Music Club to piss off Ray."

Ray "I won't be mad!"
Juno "[povname], join Muuuussssiiiiicccc Cluuuuubbbbb… you don't even have to play an instrument…"

Ray "[povname], join Arrrrrrttttt Cluuuuuubbbb…. you don't even have to like drawiiinnngggggg…"

"The cafeteria seems to quiet down the slightest bit."

"A conversation dies down."

"Then another."

"And another."

"You catch a few heads turning your way."

"Not at you."

"Past you."

"A couple of them smile."

"Some of them wave."

"A few whispered with excitement."

Bayo "At least let them decide on their own."

Bayo "You two are clearly not helping."

"Someone steps up behind your table before taking a seat beside you."

"She sets her tray beside yours with familiarity, like she's always sat next to you."

Bayo "They've been doing this for years, don't mind them."

"Just as quickly as the almost silence settled…"

"The cafeteria returned to life."

"Like it remembered how to breathe again."

"Someone laughed across the room."

"A chair scraped against the floor."

"Ray's face lit up, and Juno seemed even more relaxed."

Ray "Bayo!! You're eating with us today! It feels like it's been forever and four!"

Juno "Look what the cat dragged in. Thought we'd have to go to your little hideout room and drag you out for lunch again."

Juno "Hello, Bayo."

Bayo "Who's this? I don't recognize their face."

Ray "That's [povname]! They're new!"

Bayo "I see that."

Bayo "Welcome, it's so glad to meet you."

Bayo "Have you been given a tour yet? I would–"

Ray "I gave them a tour!"

Bayo "...Oh?"

Ray "It was… punishment for being late again…"

Bayo "Well then, I hope Ray was helpful. She does tend to… ramble on sometimes."

Juno "I'd say Ray did great. Missed the whole first period giving the tour."

Juno "Very thorough."

Ray  "T-Totally!"

Bayo "*sigh* No worries [povname], I'll have the absence cleared up for you."

Ray "You should clear up my absence too Bayo. ;)"

Bayo "You are so funny, Ray."

"The banter settled in once again."

"Bayo asked you basic questions."

"Where you are from, what school you transferred from, what made you choose this school, your most treasured memory…"

"What you value in a friend, what would the perfect day be for you…"

"What kind of people make you feel comfortable, what kind of people or situations make you nervous…"

Bayo "When a person compliments you…"

Bayo "Do you usually believe them?"

Ray "G-Geez, Bayo! A little heavy on the questions, don't ya think?"

Juno "I'm gonna have to agree with Ray on this one, as rare as it is…"

Ray "HEY!!"

Juno "Hush now Ray the adults are talking."

Ray "MEAN!!"

Bayo "Ah, I suppose you are right."

Bayo "Apologies, [povname]. I couldn't help myself."

Bayo "I like being able to understand people, it makes it easier to help them."

Bayo "If anything comes up while you're settling in, please let me know. Don't hesitate."

Juno "That's our Bayo, wants to know everything and anything about you."

Juno "She'll ask for the last 4 digits of your social security too."

Bayo "Juno-"

Ray "I think it's so sweet though!"

Ray "Don't let the questions scare ya, Bayo just wants to help you feel as comfortable as a bee."

Bayo "Exactly what Ray said. Apologies again, [povname]."

Bayo "Have you thought of joining any clubs yet?"

Bayo "I have a feeling you'd be a wonderful addition to the student council."

Juno "Pft, I thought we moved on from recruitment!"

Ray "Join…"

Juno "Don't say it…"

Ray "…"

Ray "... Art Club."

Juno "I'm waging war against the Art Club madame vice president!"

"Juno then proceeded to put Ray into a playful headlock."

Ray "Oh, merci! Merci!"

"Bayo sighed, looking utterly done with the two for a sliver of a moment before smiling again."

"An embarrassed but trying to hold it together looking smile."

Bayo "Cut it out you two…"

Ray "Anywho, I'm glad this table has more bodies! The more the merrier!"

Ray "We're going to be such best friends [povname], I just know it. >u<"

"Juno placed a sugar cookie on your tray, uncaring if you already took one."

Juno "Welcome to the group, you're never going to escape us."

Ray "Yep, we love you, so that means you're never ever ever getting rid of us."

Bayo "Beware…"

"The three broke into soft chuckles. Bayo gently patted your back."

"Ray and Juno ate while discussing everything from teachers you should look out for, to the rumor of a ghost living in the school's basement."

"Bayo continued trying to get to know you more, even taking a look at your schedule and offering to help you catch up."

Ray "Oh, has anyone heard from Tim–"

"The bell rang."

Ray "Ah!! My next class is on the other side of school!!"
Juno "Ah crap, come on Ray!"

Ray "Bye [povname], bye Bayo!"

"The two rushed off to class, which seemed to turn into a race midway."

"Bayo helped you find your next class and wished you luck." #Fade out

"…"

#Fade in  

Ray "MERRY END OF THE SCHOOL DAY!!"

"Ray ran up to you with a smile, hands faintly stained of yellow."

"Juno appeared behind you and slung an arm over your shoulder."

Juno "So, first day, tell us the tea."

Ray "Do you love it here??? Oh please please please say you do!"

Bayo "Maybe give them another day or two before they decide."

Bayo "Did you enjoy your first day here [povname]? Did you run into any troubles?"

Ray "Bayo!! I noticed you didn't eat any of the cookies I brought today. I saved one for you. :~)"

Bayo "That's sweet but… no thanks…"

Ray "Aw. :~("

Juno "It's okay Ray, I'll always be here to eat your sna–"

Ray "More for me then!"

Juno "GREEDY!"

Ray "Tehee."

Ray "June Bug, let's go visit Tim!"

Juno "Er… Tim is probably asleep…"

Juno "Best not to wake him up, yeah?"

Ray "I guess…"

Bayo "But Tim is always sleeping. Surely a visit wouldn't hurt."

Bayo "Besides, I have to talk to them about the homework they're missing and–"

Juno "Drop it. Tim will come back when they're ready."

Juno "I'm sure Tim wouldn't want to hear about homework stuff…"

Juno "*mumbles* Homework's the least of their worries…"

Bayo "Hm? I didn't hear that last part Ju–"

Ray "Juno is right. I don't think anyone would want to hear about work if I was really sick."

Ray "I am worried… but like Juno said, Tim will answer us when he's ready. There's no need to overwhelm him."

Bayo "That's… very considerate of you."

Bayo "*sigh* You're right. Let's not bother them."

pov "Who's Tim?"

Ray "Ah! [povname]! Sorry about that. You don't know who Tim is yet…"

Juno "We'll introduce you to ‘em once they come back to school."

Ray "Yeah!! It'll be so fun!! Then we'll have the band back together!"

Ray "We can go out for ice cream again, and nap in the music room, and go shopping, and stay up studying–"

Juno "--And you forget what we studied."

Bayo "--And you forget what we studied."

Ray "Guys!! That was mean! I do remember stuff! The… more important parts at least…"

Ray "Anyways, it'll be so much fun. You're going to love Tim, they're so kewl. <3"

Juno "Ouch… Ray… I thought I was the cool one…"

Ray "Eh!? You are!!"

Bayo "Oh, then what am I?"

Ray "But- you're also cool!"

Juno "Do you hear this Bayo? She thinks we're lame."

Bayo "Wow, you don't think [povname] is cool either?"

menu:
    "Wow, Ray, you are so cold hearted.":
        $ joy_points+=2
        jump tease_one
    
    "On my first day too? Just say you hate me.":
        $ joy_points+=2
        jump tease_two
    
    "Cut it out. This is lame.":
        $ joy_points-=2
        jump tease_three

label tease_one:
    Ray "W-What!? Am not!"
    jump shared_tease

label tease_two:
    Ray "H-Huh!? I don't hate you!!"
    jump shared_tease

label tease_three:
    Ray "S-sorry…"
    jump shared_tease

   
label shared_tease:
Ray "I was joking!!"

Juno "Heheh, we're just messing with ya."

Ray "Tehee. I know."

Bayo "[povname] are you confused on any topics?"

Bayo "We could have a study session tomorrow."

Ray "*gasp* Yes! That will be so much fun!"

Bayo "Eh- I was thinking just between me and–"

Ray "I can bake cookies and- oh! I have extra supplies I'd be willing to share!"

Juno "A study sesh would be cool. I could help with all the math stuff."

Ray "I can confirm! Juno is really good at math stuff!"

Bayo "I suppose it can't be helped… so. Tomorrow after school would be perfect?"

Ray "I'm in! :~D"

Bayo "Heh, we know that."

Juno "I'm in too."

Bayo "Tomorrow it is then. Hope you'll be able to make it."

Bayo "Ray, isn't this your stop?"

Ray "Ah! It is! I almost missed it!"

Ray "Huh? You live around here too [povname]?"

Ray "Oh that's right! I remember running past you this morning!"

Ray "Well then, see you in the morning! Sleep tight everybug!"

Juno "Emphasis on the sleep part, Ray."

Ray "Hey!!"

Bayo "Good night you two."







