import pickle
import numpy
import matplotlib

dictBookTitles = {106: 'Ghost Talkers', 1: 'Seveneves', 2: 'Lords and Ladies', 3: 'The Well of Ascension',
                  4: 'The Stranger', 5: 'Sex Criminals: Volume One', 6: 'Men At Arms', 7: 'The Final Empire',
                  8: 'The Year of Reading Dangerously: How Fifty Great Books (and Two Not-So-Great Ones) Saved My Life',
                  9: 'Career of Evil', 10: 'The Wise Man\'s Fear', 11: 'Harry Potter and the Cursed Child',
                  12: 'The Name of The Wind', 13: 'Acceptance', 14: 'I Don\'t Want to Kill You',
                  15: 'Pride and Prejudice', 16: 'I Am Not a Serial Killer', 17: 'Batman: Arkham Asylum',
                  18: 'All-Star Superman: Vol 1', 19: 'Silver Screen Fiend: Learning About Life from an Addiction',
                  20: 'City of Stairs', 21: 'Station Eleven', 22: 'Mr. Penumbra\'s 24 Hour Bookstore',
                  23: 'An Artist of the Floating World', 24: 'Of Mice and Men',
                  25: 'The Particular Sadness of Lemoncake',
                  26: 'On Writing', 27: 'Whiskey Tango Foxtrot', 28: 'One Hundred Years of Solitude',
                  29: 'The Goldfinch', 30: 'Moby Dick; Or, The Whale', 31: 'Proof',
                  32: 'Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch', 33: 'The Tempest',
                  34: 'Narrative of the Life of Frederick Douglass ', 35: 'The Oregon Trail: A New American Journey',
                  36: 'Collected Stories',
                  37: "Operation Mincemeat: How a Dead Man and a Bizarre Plan Fooled the Nazis and Assured an Allied Victory",
                  38: 'Bellman & Black', 39: 'The Museum of Extraordinary Things', 40: 'Gertrude', 41: 'American Gods',
                  42: 'The Eyre Affair', 43: 'If On A Winter\'s Night a Traveler', 44: 'Gone Girl',
                  45: 'People of the Book', 46: 'Green Eggs and Ham', 47: 'It\'s Kind of a Funny Story',
                  48: 'The Very Hungry Caterpillar', 49: 'The Perks of Being a Wallflower',
                  50: 'The Hitchhiker\'s Guide to the Galaxy', 51: '1984', 52: 'Looking For Alaska',
                  53: 'The Fault in Our Stars', 54: 'Eleven Minutes', 55: 'Harry Potter and the Goblet of Fire',
                  56: 'The Giver', 57: 'The Lightning Thief', 58: 'Eragon', 59: 'The Hobbit',
                  60: 'The Voyage of the Dawn Treader', 61: 'Harry Potter and the Deathly Hallows',
                  62: 'The Lion, The Witch and the Wardrobe', 63: 'Oryx and Crake', 64: 'The Andromeda Strain',
                  65: 'The Silence of the Lambs', 66: 'Jurassic Park',
                  67: 'The Devil in the White City: Murder, Magic, and Madness at the Fair that Changed America',
                  68: 'Half Magic', 69: 'The Witches', 70: 'A Light in the Attic',
                  71: 'The True Story of the Three Little Pigs', 72: 'Outliers: the Story of Success',
                  73: 'Ender\'s Game', 74: 'Artemis Fowl', 75: 'Holes', 76: 'A Wrinkle in Time',
                  77: 'The Golden Compass', 78: 'Uglies',
                  79: 'Into Thin Air: A Personal Account of the Mount Everest Disaster', 80: 'And Then There Were None',
                  81: 'Musicophilia: Tales of Music and the Brain', 82: 'Walden', 83: 'Candide', 84: 'Siddhartha',
                  85: 'Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values',
                  86: 'The Importance of Being Earnest', 87: 'A Confederacy of Dunces', 88: 'Where the Wild Things Are',
                  89: 'The Princess Bride', 90: 'Little Women', 91: 'The Miraculous Journey of Edward Tulane',
                  92: 'The Book Thief', 93: 'Fahrenheit 451', 94: 'Slaughterhouse-Five',
                  95: 'One Flew Over the Cuckoo\'s Nest', 96: 'The Great Gatsby',
                  97: 'Harry Potter and the Sorcerer\'s Stone', 98: 'The Alchemist',
                  99: 'The Curious Incident of the Dog in the Nighttime',
                  100: 'Fantastic Beasts and Where to Find Them',
                  101: 'Harry Potter and the Chamber of Secrets', 102: 'Harry Potter and the Prisoner of Azkaban',
                  103: 'Harry Potter and the Order of the Phoenix', 104: 'Harry Potter and the Half-Blood Prince',
                  105: 'Pride and Prejudice and Zombies'}
dictBookAuthors = {106: 'Mary Robinette Kowal', 1: 'Neal Stephenson', 2: 'Terry Pratchett', 3: 'Brandon Sanderson',
                   4: 'Albert Camus', 5: 'Matt Fraction', 6: 'Terry Pratchett', 7: 'Brandon Sanderson',
                   8: 'Andy Miller', 9: 'Robert Galbraith', 10: 'Patrick Rothfuss', 11: 'John Tiffany and J.K. Rowling',
                   12: 'Patrick Rothfuss', 13: 'Jeff VanderMeer', 14: 'Dan Wells', 15: 'Jane Austen', 16: 'Dan Wells',
                   17: 'Grant Morrison',
                   18: 'Grant Morrison', 19: 'Patton Oswalt', 20: 'Robert Jackson Bennett', 21: 'Emily St. John Mandel',
                   22: 'Robin Sloan', 23: 'Kazuo Ishiguro', 24: 'John Steinbeck', 25: 'Aimee Bender',
                   26: 'Stephen King', 27: 'David Shafer', 28: 'Gabriel Garcia Marquez', 29: 'Donna Tartt',
                   30: 'Herman Melville', 31: 'David Auburn', 32: 'Terry Pratchett and Neil Gaiman',
                   33: 'William Shakespere', 34: 'Frederick Douglass', 35: 'Rinker Buck', 36: 'Wallace Stegner',
                   37: 'Ben MacIntyre', 38: 'Diane Setterfield', 39: 'Alice Hoffman',
                   40: 'Hermann Hesse', 41: 'Neil Gaiman', 42: 'Jasper Fforde', 43: 'Italo Calvino',
                   44: 'Gillian Flynn', 45: 'Geraldine Brooks', 46: 'Dr. Seuss', 47: 'Ned Vizzini', 48: 'Eric Carle',
                   49: 'Stephen Chbosky', 50: 'Douglas Adams', 51: 'George Orwell', 52: 'John Green',
                   53: 'John Green', 54: 'Paolo Coelho', 55: 'J.K. Rowling', 56: 'Lois Lowry', 57: 'Rick Riordan',
                   58: 'Christopher Paolini', 59: 'J.R.R. Tolkien', 60: 'C.S. Lewis', 61: 'J.K. Rowling',
                   62: 'C.S. Lewis', 63: 'Margaret Atwood', 64: 'Michael Crichton', 65: 'Thomas Harris',
                   66: 'Michael Crichton', 67: 'Erik Larson', 68: 'Edward Eager', 69: 'Roald Dahl',
                   70: 'Shel Silverstein', 71: 'Jon Scieszka', 72: 'Malcolm Gladwell', 73: 'Orson Scott Card',
                   74: 'Eoin Colfer', 75: 'Louis Sachar', 76: 'Madeleine L\'Engle', 77: 'Philip Pullman',
                   78: 'Scott Westerfeld', 79: 'Jon Krakauer', 80: 'Agatha Christie',
                   81: 'Oliver Sacks', 82: 'Henry David Thoreau', 83: 'Voltaire', 84: 'Hermann Hesse',
                   85: 'Robert M Pirsig', 86: 'Oscar Wilde', 87: 'John Kennedy Toole', 88: 'Maurice Sendak',
                   89: 'William Goldman', 90: 'Louisa May Alcott', 91: 'Kate DiCamillo',
                   92: 'Markus Zusak', 93: 'Ray Bradbury', 94: 'Kurt Vonnegut', 95: 'Ken Kesey',
                   96: 'F. Scott Fitzgerald',
                   97: 'J.K. Rowling', 98: 'Paolo Coelho', 99: 'Mark Haddon', 100: 'J.K. Rowling', 101: 'J.K. Rowling',
                   102: 'J.K. Rowling', 103: 'J.K. Rowling', 104: 'J.K. Rowling',
                   105: 'Jane Austen and Seth Grahame-Smith'}
dictBookDescriptions = {106: 'Ginger Stuyvesant, an American heiress living in London during World War I, is engaged to '
                           'Captain Benjamin Harford, an intelligence officer. Ginger is a medium for the Spirit '
                           'Corps, a special Spiritualist force. Each soldier heading for the front is conditioned '
                           'to report to the mediums of the Spirit Corps when they die so the Corps can pass instant '
                           'information about troop movements to military intelligence. Ginger and her fellow '
                           'mediums contribute a great deal to the war efforts, so long as they pass the information '
                           'through appropriate channels. While Ben is away at the front, Ginger discovers the '
                           'presence of a traitor. Without the presence of her fiance to validate her findings, '
                           'the top brass thinks she\'s just imagining things. Even worse, it is clear that the '
                           'Spirit Corps is now being directly targeted by the German war effort. Left to her own '
                           'devices, Ginger has to find out how the Germans are targeting the Spirit Corps and stop '
                           'them. This is a difficult and dangerous task for a woman of that era, but this time both '
                           'the spirit and the flesh are willing…',
                        1: 'What would happen if the world were ending? A catastrophic event renders the earth a '
                           'ticking time bomb. In a feverish race against the inevitable, nations around the globe '
                           'band together to devise an ambitious plan to ensure the survival of humanity far beyond '
                           'our atmosphere, in outer space. But the complexities and unpredictability of human nature '
                           'coupled with unforeseen challenges and dangers threaten the intrepid pioneers, '
                           'until only a handful of survivors remain . . . Five thousand years later, '
                           'their progeny—seven distinct races now three billion strong—embark on yet another '
                           'audacious journey into the unknown . . . to an alien world utterly transformed by '
                           'cataclysm and time: Earth. A writer of dazzling genius and imaginative vision, '
                           'Neal Stephenson combines science, philosophy, technology, psychology, and literature in a '
                           'magnificent work of speculative fiction that offers a portrait of a future that is both '
                           'extraordinary and eerily recognizable. As he did in Anathem, Cryptonomicon, the Baroque '
                           'Cycle, and Reamde, Stephenson explores some of our biggest ideas and perplexing '
                           'challenges in a breathtaking saga that is daring, engrossing, and altogether brilliant.',
                        2: 'A Discworld Novel. It\'s a hot Midsummer Night. The crop circles are turning up '
                           'everywhere-even on the mustard-and-cress of Pewseyy Ogg, aged four. And Magrat Garlick, '
                           'witch, is going to be married in the morning...Everything ought to be going like a dream. '
                           'But the Lancre All-Comers Morris Team have got drunk on a fairy mound and the elves have '
                           'come back, bringing all those things traditionally associated with the magical, '
                           'glittering realm of Faerie: cruelty, kidnapping, malice and evil, evil murder.* Granny '
                           'Weatherwax and her tiny argumentative coven have really got their work cut out this '
                           'time ...With full supporting cast of dwarfs, wizards, trolls, Morris Dancers and one '
                           'orangutan. And lots. of hey-nonny-nonny and blood all over the place.',
                        3: 'From #1 New York Times bestselling author Brandon Sanderson, the Mistborn series is a '
                           'heist story of political intrigue and magical, martial-arts action.  The impossible has '
                           'been accomplished. The Lord Ruler -- the man who claimed to be god incarnate and brutally '
                           'ruled the world for a thousand years -- has been vanquished. But Kelsier, the hero who '
                           'masterminded that triumph, is dead too, and now the awesome task of building a new world '
                           'has been left to his young protégé, Vin, the former street urchin who is now the most '
                           'powerful Mistborn in the land, and to the idealistic young nobleman she loves.  As '
                           'Kelsier \'s protégé and slayer of the Lord Ruler she is now venerated by a budding new '
                           'religion, a distinction that makes her intensely uncomfortable. Even more worrying, '
                           'the mists have begun behaving strangely since the Lord Ruler died, and seem to harbor a '
                           'strange vaporous entity that haunts her.  Stopping assassins may keep Vin\'s Mistborn '
                           'skills sharp, but it\'s the least of her problems. Luthadel, the largest city of the '
                           'former empire, doesn\'t run itself, and Vin and the other members of Kelsier\'s crew, '
                           'who lead the revolution, must learn a whole new set of practical and political skills to '
                           'help. It certainly won\'t get easier with three armies – one of them composed of '
                           'ferocious giants – now vying to conquer the city, and no sign of the Lord Ruler\'s hidden '
                           'cache of atium, the rarest and most powerful allomantic metal.  As the siege of Luthadel '
                           'tightens, an ancient legend seems to offer a glimmer of hope. But even if it really '
                           'exists, no one knows where to find the Well of Ascension or what manner of power it '
                           'bestows.',
                        4: 'Through the story of an ordinary man unwittingly drawn into a senseless '
                           'murder on an Algerian beach, Camus explored what he termed "the nakedness '
                           'of man faced with the absurd." First published in English in 1946; now in '
                           'a new translation by Matthew Ward.',
                        5: 'Suzie’s just a regular gal with an irregular gift: when she has sex, she stops time. One '
                           'day she meets Jon and it turns out he has the same ability. And sooner or later they get '
                           'around to using their gifts to do what we’d ALL do: rob a couple banks. A bawdy and '
                           'brazen sex comedy for comics begins here!',
                        6: 'A Young Dwarf\'s Dream  Corporal Carrott has been promoted! He\'s now in charge of the new '
                           'recruits guarding Ankh-Morpork, Discworld\'s greatest city, from Barbarian Tribes, '
                           'Miscellaneous Marauders, unlicensed Thieves, and such. It\'s a big job, particularly for '
                           'an adopted dwarf. But an even bigger job awaits. An ancient document has just revealed '
                           'that Ankh-Morpork, ruled for decades by Disorganized crime, has a secret sovereign! And '
                           'his name is Carrott... And so begins the most awesome epic encounter of all time, '
                           'or at least all afternoon, in which the fate of a city—indeed of the universe '
                           'itself!—depends on a young man\'s courage, an ancient sword\'s magic, and a three-legged '
                           'poodle\'s bladder.',
                        7: 'In a world where ash falls from the sky, and mist dominates the night, an evil cloaks the '
                           'land and stifles all life. The future of the empire rests on the shoulders of a '
                           'troublemaker and his young apprentice. Together, can they fill the world with color once '
                           'more? In Brandon Sanderson\'s intriguing tale of love, loss, despair and hope, '
                           'a new kind of magic enters the stage — Allomancy, a magic of the metals.',
                        8: 'A working father whose life no longer feels like his own discovers the transforming '
                           'powers of great (and downright terrible) literature in this laugh-out-loud memoir. Andy '
                           'Miller had a job he quite liked, a family he loved, and no time at all for reading. Or so '
                           'he kept telling himself. But, no matter how busy or tired he was, something kept niggling '
                           'at him. Books. Books he\'d always wanted to read. Books he\'d said he\'d read that he '
                           'actually hadn\'t. Books that whispered the promise of escape from the daily grind. And '
                           'so, with the turn of a page, Andy began a year of reading that was to transform his life '
                           'completely. This book is Andy\'s inspirational and very funny account of his expedition '
                           'through literature: classic, cult, and everything in between. Beginning with a copy of '
                           'Bulgakov\'s Master and Margarita that he happens to find one day in a bookstore, '
                           'he embarks on a literary odyssey. From Middlemarch to Anna Karenina to A Confederacy of '
                           'Dunces, this is a heartfelt, humorous, and honest examination of what it means to be a '
                           'reader, and a witty and insightful journey of discovery and soul-searching that '
                           'celebrates the abiding miracle of the book and the power of reading.',
                        9: 'Cormoran Strike is back, with his assistant Robin Ellacott, in a mystery based around '
                           'soldiers returning from war. When a mysterious package is delivered to Robin Ellacott, '
                           'she is horrified to discover that it contains a woman’s severed leg. Her boss, '
                           'private detective Cormoran Strike, is less surprised but no less alarmed. There are four '
                           'people from his past who he thinks could be responsible – and Strike knows that any one '
                           'of them is capable of sustained and unspeakable brutality. With the police focusing on '
                           'the one suspect Strike is increasingly sure is not the perpetrator, he and Robin take '
                           'matters into their own hands, and delve into the dark and twisted worlds of the other '
                           'three men. But as more horrendous acts occur, time is running out for the two of them… '
                           'Career of Evil is the third in the series featuring private detective Cormoran Strike and '
                           'his assistant Robin Ellacott. A mystery and also a story of a man and a woman at a '
                           'crossroads in their personal and professional lives.',
                        10: '“There are three things all wise men fear: the sea in storm, a night with no moon, '
                            'and the anger of a gentle man.” My name is Kvothe I have stolen princesses back from '
                            'sleeping barrow kings. I burned down the town of Trehon. I have spent the night with '
                            'Felurian and left with both my sanity and my life. I was expelled from the University at '
                            'a younger age than most people are allowed in. I tread paths by moonlight that others '
                            'fear to speak of during day. I have talked to Gods, loved women, and written songs that '
                            'make the minstrels weep. You may have heard of me. So begins the tale of a hero told '
                            'from his own point of view — a story unequaled in fantasy literature. Now in The Wise '
                            'Man\'s Fear, an escalating rivalry with a powerful member of the nobility forces Kvothe '
                            'to leave the University and seek his fortune abroad. Adrift, penniless, and alone, '
                            'he travels to Vintas, where he quickly becomes entangled in the politics of courtly '
                            'society. While attempting to curry favor with a powerful noble, Kvothe uncovers an '
                            'assassination attempt, comes into conflict with a rival arcanist, and leads a group of '
                            'mercenaries into the wild, in an attempt to solve the mystery of who (or what) is '
                            'waylaying travelers on the King\'s Road. All the while, Kvothe searches for answers, '
                            'attempting to uncover the truth about the mysterious Amyr, the Chandrian, and the death '
                            'of his parents. Along the way, Kvothe is put ﻿on trial by the legendary Adem '
                            'mercenaries, is forced to reclaim the honor of the Edema Ruh, and travels into the Fae '
                            'realm. There he meets Felurian, the faerie woman no man can resist, and who no man has '
                            'ever survived...until Kvothe. In The Wise Man\'s Fear, Kvothe takes his first steps on '
                            'the path of the hero and learns how difficult life can be when a man becomes a legend in '
                            'his own time.',
                        11: 'Based on an original new story by J.K. Rowling, Jack Thorne and John Tiffany, a new play '
                            'by Jack Thorne, Harry Potter and the Cursed Child is the eighth story in the Harry '
                            'Potter series and the first official Harry Potter story to be presented on stage. The '
                            'play will receive its world premiere in London’s West End on July 30, 2016. It was '
                            'always difficult being Harry Potter and it isn’t much easier now that he is an '
                            'overworked employee of the Ministry of Magic, a husband and father of three school-age '
                            'children. While Harry grapples with a past that refuses to stay where it belongs, '
                            'his youngest son Albus must struggle with the weight of a family legacy he never wanted. '
                            'As past and present fuse ominously, both father and son learn the uncomfortable truth: '
                            'sometimes, darkness comes from unexpected places.',
                        12: 'Told in Kvothe\'s own voice, this is the tale of the magically gifted young man who '
                            'grows to be the most notorious wizard his world has ever seen.  The intimate narrative '
                            'of his childhood in a troupe of traveling players, his years spent as a near-feral '
                            'orphan in a crime-ridden city, his daringly brazen yet successful bid to enter a '
                            'legendary school of magic, and his life as a fugitive after the murder of a king form a '
                            'gripping coming-of-age story unrivaled in recent literature.  A high-action story '
                            'written with a poet\'s hand, The Name of the Wind is a masterpiece that will transport '
                            'readers into the body and mind of a wizard.',
                        13: 'It is winter in Area X, the mysterious wilderness that has defied explanation for thirty '
                            'years, rebuffing expedition after expedition, refusing to reveal its secrets. As Area X '
                            'expands, the agency tasked with investigating and overseeing it--the Southern Reach--has '
                            'collapsed on itself in confusion. Now one last, desperate team crosses the border, '
                            'determined to reach a remote island that may hold the answers they\'ve been seeking. If '
                            'they fail, the outer world is in peril. Meanwhile, Acceptance tunnels ever deeper into '
                            'the circumstances surrounding the creation of Area X--what initiated this unnatural '
                            'upheaval? Among the many who have tried, who has gotten close to understanding Area '
                            'X--and who may have been corrupted by it? In this last installment of Jeff '
                            'VanderMeer\'s Southern Reach trilogy, the mysteries of Area X may be solved, '
                            'but their consequences and implications are no less profound--or terrifying.',
                        14: 'John Cleaver has called a demon—literally called it, on the phone, and challenged it to '
                            'a fight. He’s faced two of the monsters already, barely escaping with his life, '
                            'and now he’s done running; he’s taking the fight to them. But as he wades through his '
                            'town’s darkest secrets, searching for any sign of who the demon might be, '
                            'one thing becomes all too clear: in a game of cat and mouse with a supernatural killer, '
                            'the human is always the mouse.  In I Am Not a Serial Killer we watched a budding '
                            'sociopath break every rule he had to save his town from evil. In Mr. Monster we held our '
                            'breath as he fought madly with himself, struggling to stay in control. Now John Cleaver '
                            'has mastered his twisted talents and embraced his role as a killer of killers. I Don’t '
                            'Want to Kill You brings his story to a thundering climax of suspicion, mayhem, '
                            'and death. It’s time to punish the guilty. And in a town full of secrets, everyone is '
                            'guilty of something.',
                        15: "In this historic romance, young Elizabeth Bennet strives for love, independence and "
                            "honesty in the vapid high society of 19th century England.",
                        16: 'John Wayne Cleaver is dangerous, and he knows it. He\'s spent his life doing his best '
                            'not to live up to his potential. He\'s obsessed with serial killers, but really '
                            'doesn\'t want to become one. So for his own sake, and the safety of those around him, '
                            'he lives by rigid rules he\'s written for himself, practicing normal life as if it were '
                            'a private religion that could save him from damnation. Dead bodies are normal to John. '
                            'He likes them, actually. They don\'t demand or expect the empathy he\'s unable to offer. '
                            'Perhaps that\'s what gives him the objectivity to recognize that there\'s something '
                            'different about the body the police have just found behind the Wash-n-Dry '
                            'Laundromat---and to appreciate what that difference means. Now, for the first time, '
                            'John has to confront a danger outside himself, a threat he can\'t control, a menace to '
                            'everything and everyone he would love, if only he could. Dan Wells\'s debut novel, '
                            'I Am Not a Serial Killer, is the first volume of a trilogy that will keep you awake and '
                            'then haunt your dreams',
                        17: "In this groundbreaking, painted graphic novel, the inmates of Arkham Asylum have taken "
                            "over Gotham's detention center for the criminally insane on April Fools Day, "
                            "demanding Batman in exchange for their hostages. Accepting their demented challenge, "
                            "Batman is forced to live and endure the personal hells of the Joker, Scarecrow, "
                            "Poison Ivy, Two-Face and many other sworn enemies in order to save the innocents and "
                            "retake the prison. During his run through this absurd gauntlet, the Dark Knight's own "
                            "sanity is placed in jeopardy. This special anniversary edition trade paperback also "
                            "reproduces the original script with annotations by Morrison and editor Karen Berger.",
                        18: 'The last son of the doomed planet Krypton rocketed to Earth. A sci-fi savior raised in '
                            'America\'s heartland; embracing and embraced by what\'s best in humanity. Lex Luthor, '
                            'the criminal mastermind misguided by his own personal shortcomings. Lois Lane, '
                            'the dynamic investigative reporter who reminds you that there are enigmas in life that '
                            'baffle even Superman. You\'ve seen it before. Now see it again as though for the first '
                            'time. Not an origin story, modernization, or reinvention--but instead a timeless and '
                            'iconic presentation refined by the passion and craft of master storytellers, '
                            'ALL-STAR SUPERMAN presents a unique and elegant interpretation of the original and most '
                            'recognizable of all superheroes.',
                        19: 'Between 1995 and 1999, Patton Oswalt lived with an unshakable addiction. It wasn’t '
                            'drugs, alcohol, or sex: it was film. After moving to Los Angeles, Oswalt became a huge '
                            'film buff (or as he calls it, a sprocket fiend), absorbing classics, cult hits, '
                            'and new releases at the famous New Beverly Cinema. Silver screen celluloid became '
                            'Patton’s life schoolbook, informing his notion of acting, writing, comedy, '
                            'and relationships. Set in the nascent days of LA’s alternative comedy scene, '
                            'Silver Screen Fiend chronicles Oswalt’s journey from fledgling stand-up comedian to '
                            'self-assured sitcom actor, with the colorful New Beverly collective and a cast of '
                            'now-notable young comedians supporting him all along the way.',
                        20: "Years ago, the city of Bulikov wielded the powers of the Gods to conquer the world. But "
                            "after its divine protectors were mysteriously killed, the conqueror has become the "
                            "conquered; the city's proud history has been erased and censored, progress has left it "
                            "behind, and it is just another colonial outpost of the world's new geopolitical power. "
                            "Into this musty, backward city steps Shara Thivani. Officially, the quiet woman is just "
                            "another lowly diplomat sent by Bulikov's oppressors. Unofficially, Shara is one of her "
                            "country's most accomplished spymasters — dispatched to investigate the brutal murder of "
                            "a seemingly harmless historian. As Shara pursues the mystery through the ever-shifting "
                            "physical and political geography of the city, she begins to suspect that the beings who "
                            "once protected Bulikov may not be as dead as they seem — and that her own abilities "
                            "might be touched by the divine as well.",
                        21: 'An audacious, darkly glittering novel set in the eerie days of civilization\'s collapse, '
                            'Station Eleven tells the spellbinding story of a Hollywood star, his would-be savior, '
                            'and a nomadic group of actors roaming the scattered outposts of the Great Lakes region, '
                            'risking everything for art and humanity. One snowy night Arthur Leander, '
                            'a famous actor, has a heart attack onstage during a production of King Lear. Jeevan '
                            'Chaudhary, a paparazzo-turned-EMT, is in the audience and leaps to his aid. A child '
                            'actress named Kirsten Raymonde watches in horror as Jeevan performs CPR, '
                            'pumping Arthur\'s chest as the curtain drops, but Arthur is dead. That same night, '
                            'as Jeevan walks home from the theater, a terrible flu begins to spread. Hospitals are '
                            'flooded and Jeevan and his brother barricade themselves inside an apartment, '
                            'watching out the window as cars clog the highways, gunshots ring out, '
                            'and life disintegrates around them. Twenty years later, Kirsten is an actress with the '
                            'Traveling Symphony. Together, this small troupe moves between the settlements of an '
                            'altered world, performing Shakespeare and music for scattered communities of survivors. '
                            'Written on their caravan, and tattooed on Kirsten\'s arm is a line from Star Trek: '
                            '"Because survival is insufficient." But when they arrive in St. Deborah by the Water, '
                            'they encounter a violent prophet who digs graves for anyone who dares to leave. '
                            'Spanning decades, moving back and forth in time, and vividly depicting life before and '
                            'after the pandemic, this suspenseful, elegiac novel is rife with beauty. As Arthur falls '
                            'in and out of love, as Jeevan watches the newscasters say their final good-byes, '
                            'and as Kirsten finds herself caught in the crosshairs of the prophet, we see the strange '
                            'twists of fate that connect them all. A novel of art, memory, and ambition, '
                            'Station Eleven tells a story about the relationships that sustain us, the ephemeral '
                            'nature of fame, and the beauty of the world as we know it.',
                        22: 'The Great Recession has shuffled Clay Jannon away from life as a San Francisco '
                            'web-design drone and into the aisles of Mr. Penumbra’s 24-Hour Bookstore. But after a '
                            'few days on the job, Clay discovers that the store is more curious than either its name '
                            'or its gnomic owner might suggest. The bookstore’s secrets extend far beyond its walls',
                        23: 'In An Artist of the Floating World, Kazuo Ishiguro offers readers of the English '
                            'language an authentic look at postwar Japan, "a floating world" of changing cultural '
                            'behaviors, shifting societal patterns and troubling questions. Ishiguro, who was born in '
                            'Nagasaki in 1954 but moved to England in 1960, writes the story of Masuji Ono, '
                            'a bohemian artist and purveyor of the night life who became a propagandist for Japanese '
                            'imperialism during the war. But the war is over. Japan lost, Ono\'s wife and son have '
                            'been killed, and many young people blame the imperialists for leading the country to '
                            'disaster. What\'s left for Ono? Ishiguro\'s treatment of this story earned a 1986 '
                            'Whitbread Prize.',
                        24: "The compelling story of two outsiders striving to find their place in an unforgiving "
                            "world. Drifters in search of work, George and his simple-minded friend Lennie have "
                            "nothing in the world except each other and a dream--a dream that one day they will have "
                            "some land of their own. Eventually they find work on a ranch in California’s Salinas "
                            "Valley, but their hopes are doomed as Lennie, struggling against extreme cruelty, "
                            "misunderstanding and feelings of jealousy, becomes a victim of his own strength. "
                            "Tackling universal themes such as the friendship of a shared vision, and giving voice to "
                            "America’s lonely and dispossessed, Of Mice and Men has proved one of Steinbeck’s most "
                            "popular works, achieving success as a novel, a Broadway play and three acclaimed "
                            "films.",
                        25: 'The wondrous Aimee Bender conjures the lush and moving story of a girl whose magical '
                            'gift is really a devastating curse. On the eve of her ninth birthday, unassuming Rose '
                            'Edelstein, a girl at the periphery of schoolyard games and her distracted parents’ '
                            'attention, bites into her mother’s homemade lemon-chocolate cake and discovers she has a '
                            'magical gift: she can taste her mother’s emotions in the cake. She discovers this gift '
                            'to her horror, for her mother — her cheerful, good-with-crafts, can-do mother — tastes '
                            'of despair and desperation. Suddenly, and for the rest of her life, food becomes a peril '
                            'and a threat to Rose.  The curse her gift has bestowed is the secret knowledge all '
                            'families keep hidden—her mother’s life outside the home, her father’s detachment, '
                            'her brother’s clash with the world. Yet as Rose grows up she learns to harness her gift '
                            'and becomes aware that there are secrets even her taste buds cannot discern. The '
                            'Particular Sadness of Lemon Cake is a luminous tale about the enormous difficulty of '
                            'loving someone fully when you know too much about them.',
                        26: '“Long live the King” hailed Entertainment Weekly upon the publication of Stephen King\'s '
                            'On Writing. Part memoir, part master class by one of the bestselling authors of all '
                            'time, this superb volume is a revealing and practical view of the writer\'s craft, '
                            'comprising the basic tools of the trade every writer must have. King\'s advice is '
                            'grounded in his vivid memories from childhood through his emergence as a writer, '
                            'from his struggling early career to his widely reported near-fatal accident in 1999—and '
                            'how the inextricable link between writing and living spurred his recovery. Brilliantly '
                            'structured, friendly and inspiring, On Writing will empower and entertain everyone who '
                            'reads it—fans, writers, and anyone who loves a great story well told.',
                        27: 'Three young adults grapple with the usual thirty-something problems—boredom, '
                            'authenticity, an omnipotent online oligarchy—in David Shafer\'s darkly comic debut '
                            'novel. The Committee, an international cabal of industrialists and media barons, '
                            'is on the verge of privatizing all information. Dear Diary, an idealistic online '
                            'Underground, stands in the way of that takeover, using radical politics, '
                            'classic spycraft, and technology that makes Big Data look like dial-up. Into this secret '
                            'battle stumbles an unlikely trio: Leila Majnoun, a disillusioned non-profit worker; Leo '
                            'Crane, an unhinged trustafarian; and Mark Deveraux, a phony self-betterment guru who '
                            'works for the Committee. Leo and Mark were best friends in college, but early adulthood '
                            'has set them on diverging paths. Growing increasingly disdainful of Mark\'s platitudes, '
                            'Leo publishes a withering takedown of his ideas online. But the Committee is reading—and '
                            'erasing—Leo\'s words. On the other side of the world, Leila\'s discoveries about the '
                            'Committee\'s far-reaching ambitions threaten to ruin those who are closest to her. In '
                            'the spirit of William Gibson and Chuck Palahniuk, Whiskey Tango Foxtrot is both a '
                            'suspenseful global thriller and an emotionally truthful novel about the struggle to '
                            'change the world in- and outside your head.',
                        28: 'One of the 20th century\'s enduring works, One Hundred Years of Solitude is a widely '
                            'beloved and acclaimed novel known throughout the world, and the ultimate achievement of '
                            'a Nobel Prize winning career. The novel tells the story of the rise and fall of the '
                            'mythical town of Macondo through the history of the family. It is a rich and brilliant '
                            'chronicle of life and death, and the tragicomedy of humankind. In the noble, ridiculous, '
                            'beautiful, and tawdry story of the family, one sees all of humanity, just as in the '
                            'history, myths, growth, and decay of Macondo, one sees all of Latin America. Love and '
                            'lust, war and revolution, riches and poverty, youth and senility -- the variety of life, '
                            'the endlessness of death, the search for peace and truth -- these universal themes '
                            'dominate the novel. Whether he is describing an affair of passion or the voracity of '
                            'capitalism and the corruption of government, Gabriel Garcia Marquez always writes with '
                            'the simplicity, ease, and purity that are the mark of a master. Alternately reverential '
                            'and comical, One Hundred Years of Solitude weaves the political, personal, and spiritual '
                            'to bring a new consciousness to storytelling. Translated into dozens of languages, '
                            'this stunning work is no less than an accounting of the history of the human race. ',
                        29: 'begins with a boy. Theo Decker, a thirteen-year-old New Yorker, miraculously survives an '
                            'accident that kills his mother. Abandoned by his father, Theo is taken in by the family '
                            'of a wealthy friend. Bewildered by his strange new home on Park Avenue, disturbed by '
                            'schoolmates who don\'t know how to talk to him, and tormented above all by his '
                            'unbearable longing for his mother, he clings to one thing that reminds him of her: a '
                            'small, mysteriously captivating painting that ultimately draws Theo into the underworld '
                            'of art. As an adult, Theo moves silkily between the drawing rooms of the rich and the '
                            'dusty labyrinth of an antiques store where he works. He is alienated and in love-and at '
                            'the center of a narrowing, ever more dangerous circle. The Goldfinch combines vivid '
                            'characters, mesmerizing language, and suspense, while plumbing with a philosopher\'s '
                            'calm the deepest mysteries of love, identity, and art. It is an old-fashioned story of '
                            'loss and obsession, survival and self-invention, and the ruthless machinations of '
                            'fate.',
                        30: '\'Call me Ishmael.\' So begins Herman Melville\'s masterpiece, one of the greatest '
                            'works of imagination in literary history. As Ishmael is drawn into Captain Ahab\'s '
                            'obsessive quest to slay the white whale Moby-Dick, he finds himself engaged in a '
                            'metaphysical struggle between good and evil. More than just a novel of adventure, '
                            'more than an paean to whaling lore and legend, Moby-Dick is a haunting social '
                            'commentary, populated by some of the most enduring characters in literature; the crew of '
                            'the Pequod, from stern, Quaker First Mate Starbuck, to the tattooed Polynesian harpooner '
                            'Queequeg, are a vision of the world in microcosm, the pinnacle of Melville\'s lifelong '
                            'meditation on America. Written with wonderfully redemptive humour, Moby-Dick is a '
                            'profound, poetic inquiry into character, faith, and the nature of perception. Based on '
                            'the Northwestern University Press edition, this Penguin Classics edition includes a '
                            'critical introduction by Andrew Delbanco, as well as valuable explanatory notes, maps, '
                            'illustrations and a glossary of nautical terms. Herman Melville is now regarded as one '
                            'of America\'s greatest novelists. Much of the material for his novels was drawn from his '
                            'own experience as a seaman aboard whaling ships. He wrote his masterpiece Moby-Dick in '
                            '1851, and died in 1891.',
                        31: "One of the most acclaimed plays of the 1999-2000 season, Proof is a work that explores "
                            "the unknowability of love as much as it does the mysteries of science. It focuses on "
                            "Catherine, a young woman who has spent years caring for her father, Robert, a brilliant "
                            "mathematician in his youth who was later unable to function without her help. His death "
                            "has brought into her midst both her sister, Claire, who wants to take Catherine back to "
                            "New York with her, and Hal, a former student of Catherine's father who hopes to find "
                            "some hint of Robert's genius among his incoherent scribblings. The passion that Hal "
                            "feels for math both moves and angers Catherine, who, in her exhaustion, is torn between "
                            "missing her father and resenting the great sacrifices she made for him. For Catherine "
                            "has inherited at least a part of her father's brilliance -- and perhaps some of his "
                            "instability as well. As she and Hal become attracted to each other, they push at the "
                            "edges of each other's knowledge, considering not only the unpredictability of genius but "
                            "also the human instinct toward love and trust.",
                        32: "According to The Nice and Accurate Prophecies of Agnes Nutter, Witch (the world's only "
                            "completely accurate book of prophecies, written in 1655, before she exploded), "
                            "the world will end on a Saturday. Next Saturday, in fact. Just before dinner. So the "
                            "armies of Good and Evil are amassing, Atlantis is rising, frogs are falling, tempers are "
                            "flaring. Everything appears to be going according to Divine Plan. Except a somewhat "
                            "fussy angel and a fast-living demon—both of whom have lived amongst Earth's mortals "
                            "since The Beginning and have grown rather fond of the lifestyle—are not actually looking "
                            "forward to the coming Rapture. And someone seems to have misplaced the Antichrist . . .",
                        33: "In The Tempest, long considered one of Shakespeare's most lyrical plays, Prospero—a "
                            "magician on an enchanted island—punishes his enemies, brings happiness to his daughter, "
                            "and comes to terms with human use of supernatural power. The Tempest embodies both "
                            "seemingly timeless romance and the historically specific moment in which Europe begins "
                            "to explore and conquer the New World. Its complexity of thought, its range of "
                            "characters—from the spirit Ariel and the monster Caliban to the beautiful Miranda and "
                            "her prince Ferdinand -its poetic beauty, and its exploration of difficult questions that "
                            "still haunt us today make this play wonderfully compelling. The Tempest is a play by "
                            "William Shakespeare, believed to have been written in 1610–11. It is set on a remote "
                            "island, where Prospero, the exiled Duke of Milan, plots to restore his daughter Miranda "
                            "to her rightful place, using illusion and skilful manipulation. The eponymous tempest "
                            "brings to the island Prospero's usurping brother Antonio and the complicit Alonso, "
                            "King of Naples. There, his machinations bring about the revelation of Antonio's low "
                            "nature, the redemption of Alonso, and the marriage of Miranda to Alonso's son, "
                            "Ferdinand.",
                        34: "Born into a family of slaves, Frederick Douglass educated himself through sheer "
                            "determination. His unconquered will to triumph over his circumstances makes his one of "
                            "America’s best and most unlikely success stories. Douglass’ own account of his journey "
                            "from slave to one of America’s great statesmen, writers, and orators is as fascinating "
                            "as it is inspiring. This Prestwick House Literary Touchstone Edition includes a "
                            "glossary and reader’s notes to help the modern reader contend with Douglass’ "
                            "nineteenth-century style and vocabulary",
                        35: 'In the bestselling tradition of Bill Bryson and Tony Horwitz, Rinker Buck\'s "The Oregon '
                            'Trail" is a major work of participatory history: an epic account of traveling the 2,'
                            '000-mile length of the Oregon Trail the old-fashioned way, in a covered wagon with a '
                            'team of mules--which hasn\'t been done in a century--that also tells the rich history of '
                            'the trail, the people who made the migration, and its significance to the country. '
                            'Spanning 2,000 miles and traversing six states from Missouri to the Pacific Ocean, '
                            'the Oregon Trail is the route that made America. In the fifteen years before the Civil '
                            'War, when 400,000 pioneers used it to emigrate West--historians still regard this as the '
                            'largest land migration of all time--the trail united the coasts, doubled the size of the '
                            'country, and laid the groundwork for the railroads. The trail years also solidified the '
                            'American character: our plucky determination in the face of adversity, our impetuous '
                            'cycle of financial bubbles and busts, the fractious clash of ethnic populations '
                            'competing for the same jobs and space. Today, amazingly, the trail is all but forgotten. '
                            ' Rinker Buck is no stranger to grand adventures. "The New Yorker "described his first '
                            'travel narrative, "Flight of Passage," as "a funny, cocky gem of a book," and with "The '
                            'Oregon Trail "he seeks to bring the most important road in American history back to '
                            'life. At once a majestic American journey, a significant work of history, and a personal '
                            'saga reminiscent of bestsellers by Bill Bryson and Cheryl Strayed, the book tells the '
                            'story of Buck\'s 2,000-mile expedition across the plains with tremendous humor and '
                            'heart. He was accompanied by three cantankerous mules, his boisterous brother, Nick, '
                            'and an "incurably filthy" Jack Russell terrier named Olive Oyl. Along the way, '
                            'Buck dodges thunderstorms in Nebraska, chases his runaway mules across miles of Wyoming '
                            'plains, scouts more than five hundred miles of nearly vanished trail on foot, '
                            'crosses the Rockies, makes desperate fifty-mile forced marches for water, and repairs so '
                            'many broken wheels and axels that he nearly reinvents the art of wagon travel itself. '
                            'Apart from charting his own geographical and emotional adventure, Buck introduces '
                            'readers to the evangelists, shysters, natives, trailblazers, and everyday dreamers who '
                            'were among the first of the pioneers to make the journey west. With a rare narrative '
                            'power, a refreshing candor about his own weakness and mistakes, and an extremely '
                            'attractive obsession for history and travel, "The Oregon Trail" draws readers into the '
                            'journey of a lifetime.',
                        36: "In a literary career spanning more than fifty years, Wallace Stegner created a "
                            "remarkable record of the history and culture of twentieth-century America. Each of the "
                            "thirty-one stories contained in this volume embody some of the best virtues and values "
                            "to be found in contemporary fiction, demonstrating why the author is acclaimed as one of "
                            "America's master storytellers. The traveler --Buglesong --Beyond the glass mountain --The "
                            "berry patch --The women on the wall --Balance his, swing yours --Saw gang --Goin' to "
                            "town --The view from the balcony --Volcano --Two rivers --Hostage --In the twilight "
                            "--Butcher bird --The double corner --The colt --The Chink --Chip off the old block --The "
                            "sweetness of the twisted apples --The blue-winged teal --Pop goes the alley cat --Maiden "
                            "in a tower --Impasse --The volunteer --A field guide to the western birds --Something "
                            "spurious from the Mindanao Deep --Genesis --The wolfer --Carrion spring --He who spits "
                            "at the sky --The city of the living.",
                        37: 'In 1943, from a windowless London basement office, two intelligence officers conceived a '
                            'plan that was both simple & complicated—Operation Mincemeat. Purpose? To deceive the '
                            'Nazis into thinking the Allies were planning to attack Europe by way of Greece or '
                            'Sardinia, rather than Sicily, as the Nazis had assumed & the Allies ultimately chose. '
                            'Charles Cholmondeley of MI5 & the British naval intelligence officer Ewen Montagu were '
                            'very different. Cholmondeley was a dreamer seeking adventure. Montagu was an '
                            'aristocratic, detail-oriented barrister. A perfect team, they created an ingenious plan: '
                            'equip a corpse with secret (but false) papers concerning the invasion, then drop it off '
                            'the coast of Spain where German spies would hopefully take the bait. The idea was '
                            'approved by British intelligence officials, including Ian Fleming (007\'s creator). '
                            'Winston Churchill believed it might ring true to the Axis & help bring victory. Filled '
                            'with spies, double agents, rogues, heroes & a corpse, the story of Operation Mincemeat '
                            'reads like an international thriller. Unveiling never-before-released material, '
                            'Macintyre goes into the minds of intelligence officers, their moles & spies, '
                            '& the German Abwehr agents who suffered the “twin frailties of wishfulness & '
                            'yesmanship.” He weaves together the eccentric personalities of Cholmondeley & Montagu & '
                            'their improbable feats into an adventure that saved thousands & paved the way for the '
                            'conquest of Sicily.',
                        38: 'Bellman & Black is a heart-thumpingly perfect ghost story, beautifully and irresistibly '
                            'written, its ratcheting tension exquisitely calibrated line by line. Its hero is William '
                            'Bellman, who, as a boy of 10, killed a shiny black rook with a catapult, and who grew up '
                            'to be someone, his neighbours think, who "could go to the good or the bad." And indeed, '
                            'although William Bellman\'s life at first seems blessed—he has a happy marriage to a '
                            'beautiful woman, becomes father to a brood of bright, strong children, and thrives in '
                            'business—one by one, people around him die. And at each funeral, he is startled to see a '
                            'strange man in black, smiling at him. At first, the dead are distant relatives, '
                            'but eventually his own children die, and then his wife, leaving behind only one child, '
                            'his favourite, Dora. Unhinged by grief, William gets drunk and stumbles to his wife\'s '
                            'fresh grave—and who should be there waiting, but the smiling stranger in black. The '
                            'stranger has a proposition for William—a mysterious business called "Bellman & Black" . '
                            '. .',
                        39: 'Coralie Sardie is the daughter of the sinister impresario behind The Museum of '
                            'Extraordinary Things, a Coney Island boardwalk freak show that thrills the masses. An '
                            'exceptional swimmer, Coralie appears as the Mermaid in her father’s “museum,” alongside '
                            'performers like the Wolfman, the Butterfly Girl, and a one-hundred-year-old turtle. One '
                            'night Coralie stumbles upon a striking young man taking pictures of moonlit trees in the '
                            'woods off the Hudson River. The dashing photographer is Eddie Cohen, a Russian '
                            'immigrant who has run away from his father’s Lower East Side Orthodox community and his '
                            'job as a tailor’s apprentice. When Eddie photographs the devastation on the streets of '
                            'New York following the infamous Triangle Shirtwaist Factory fire, he becomes embroiled '
                            'in the suspicious mystery behind a young woman’s disappearance and ignites the heart of '
                            'Coralie.',
                        40: "With Gertrude, Herman Hesse continues his lifelong exploration of the irreconcilable "
                            "elements of human existence. In this fictional memoir, the renowned composer Kuhn "
                            "recounts his tangled relationships with two artists--his friend Heinrich Muoth, "
                            "a brooding, self-destructive opera singer, and the gentle, self-assured Gertrude Imthor. "
                            "Kuhn is drawn to Gertrude upon their first meeting, but Gertrude falls in love with "
                            "Heinrich, to whom she is introduced when Kuhn auditions them for the leads in his new "
                            "opera. Hopelessly ill-matched, Gertrude and Heinrich have a disastrous marriage that "
                            "leaves them both ruined. Yet this tragic affair also becomes the inspiration for Kuhn's "
                            "opera, the most important success of his artistic life.",
                        41: 'Days before his release from prison, Shadow\'s wife, Laura, dies in a mysterious car '
                            'crash. Numbly, he makes his way back home. On the plane, he encounters the enigmatic Mr '
                            'Wednesday, who claims to be a refugee from a distant war, a former god and the king of '
                            'America. Together they embark on a profoundly strange journey across the heart of the '
                            'USA, whilst all around them a storm of preternatural and epic proportions threatens to '
                            'break. Scary, gripping and deeply unsettling, American Gods takes a long, '
                            'hard look into the soul of America. You\'ll be surprised by what - and who - it finds '
                            'there...',
                        42: 'Welcome to a surreal version of Great Britain, circa 1985, where time travel is routine, '
                            'cloning is a reality (dodos are the resurrected pet of choice), and literature is taken '
                            'very, very seriously. England is a virtual police state where an aunt can get lost ('
                            'literally) in a Wordsworth poem, militant Baconians heckle performances of Hamlet, '
                            'and forging Byronic verse is a punishable offense. All this is business as usual for '
                            'Thursday Next, renowned Special Operative in literary detection, until someone begins '
                            'kidnapping characters from works of literature. When Jane Eyre is plucked from the pages '
                            'of Brontë\'s novel, Thursday must track down the villain and enter the novel herself to '
                            'avert a heinous act of literary homicide.',
                        43: 'If on a Winter\'s Night a Traveler is a marvel of ingenuity, an experimental text that '
                            'looks longingly back to the great age of narration--"when time no longer seemed stopped '
                            'and did not yet seem to have exploded." Italo Calvino\'s novel is in one sense a comedy '
                            'in which the two protagonists, the Reader and the Other Reader, ultimately end up '
                            'married, having almost finished If on a Winter\'s Night a Traveler. In another, '
                            'it is a tragedy, a reflection on the difficulties of writing and the solitary nature of '
                            'reading. The Reader buys a fashionable new book, which opens with an exhortation: '
                            '"Relax. Concentrate. Dispel every other thought. Let the world around you fade." Alas, '
                            'after 30 or so pages, he discovers that his copy is corrupted, and consists of nothing '
                            'but the first section, over and over. Returning to the bookshop, he discovers the '
                            'volume, which he thought was by Calvino, is actually by the Polish writer Bazakbal. '
                            'Given the choice between the two, he goes for the Pole, as does the Other Reader, '
                            'Ludmilla. But this copy turns out to be by yet another writer, as does the next, '
                            'and the next. The real Calvino intersperses 10 different pastiches--stories of menace, '
                            'spies, mystery, premonition--with explorations of how and why we read, make meanings, '
                            'and get our bearings or fail to. Meanwhile the Reader and Ludmilla try to reach, '
                            'and read, each other. If on a Winter\'s Night is dazzling, vertiginous, and deeply '
                            'romantic. "What makes lovemaking and reading resemble each other most is that within '
                            'both of them times and spaces open, different from measurable time and space."',
                        44: 'On a warm summer morning in North Carthage, Missouri, it is Nick and Amy Dunne’s fifth '
                            'wedding anniversary. Presents are being wrapped and reservations are being made when '
                            'Nick’s clever and beautiful wife disappears. Husband-of-the-Year Nick isn’t doing '
                            'himself any favors with cringe-worthy daydreams about the slope and shape of his wife’s '
                            'head, but passages from Amy\'s diary reveal the alpha-girl perfectionist could have put '
                            'anyone dangerously on edge. Under mounting pressure from the police and the media—as '
                            'well as Amy’s fiercely doting parents—the town golden boy parades an endless series of '
                            'lies, deceits, and inappropriate behavior. Nick is oddly evasive, and he’s definitely '
                            'bitter—but is he really a killer?',
                        45: 'In 1996, Hanna Heath, an Australian rare-book expert, is offered the job of a lifetime: '
                            'analysis and conservation of the famed Sarajevo Haggadah, which has been rescued from '
                            'Serb shelling during the Bosnian war. Priceless and beautiful, the book is one of the '
                            'earliest Jewish volumes ever to be illuminated with images. When Hanna, a caustic loner '
                            'with a passion for her work, discovers a series of tiny artifacts in its ancient '
                            'binding—an insect wing fragment, wine stains, salt crystals, a white hair—she begins to '
                            'unlock the book’s mysteries. The reader is ushered into an exquisitely detailed and '
                            'atmospheric past, tracing the book’s journey from its salvation back to its creation. '
                            'In Bosnia during World War II, a Muslim risks his life to protect it from the Nazis. In '
                            'the hedonistic salons of fin-de-siècle Vienna, the book becomes a pawn in the struggle '
                            'against the city’s rising anti-Semitism. In inquisition-era Venice, a Catholic priest '
                            'saves it from burning. In Barcelona in 1492, the scribe who wrote the text sees his '
                            'family destroyed by the agonies of enforced exile. And in Seville in 1480, the reason '
                            'for the Haggadah’s extraordinary illuminations is finally disclosed. Hanna’s '
                            'investigation unexpectedly plunges her into the intrigues of fine art forgers and '
                            'ultra-nationalist fanatics. Her experiences will test her belief in herself and the man '
                            'she has come to love. Inspired by a true story, People of the Book is at once a novel '
                            'of sweeping historical grandeur and intimate emotional intensity, an ambitious, '
                            'electrifying work by an acclaimed and beloved author.',
                        46: '“Do you like green eggs and ham?” asks Sam-I-am in this Beginner Book by Dr. Seuss. In a '
                            'house or with a mouse? In a boat or with a goat? On a train or in a tree? Sam keeps '
                            'asking persistently. With unmistakable characters and signature rhymes, Dr. Seuss’s '
                            'beloved favorite has cemented its place as a children’s classic. In this most famous of '
                            'cumulative tales, the list of places to enjoy green eggs and ham, and friends to enjoy '
                            'them with, gets longer and longer. Follow Sam-I-am as he insists that this unusual treat '
                            'is indeed a delectable snack to be savored everywhere and in every way. Originally '
                            'created by Dr. Seuss, Beginner Books encourage children to read all by themselves, '
                            'with simple words and illustrations that give clues to their meaning.',
                        47: 'Ambitious New York City teenager Craig Gilner is determined to succeed at life - which '
                            'means getting into the right high school to get into the right job. But once Craig aces '
                            'his way into Manhattan\'s Executive Pre-Professional High School, the pressure becomes '
                            'unbearable. He stops eating and sleeping until, one night, he nearly kills himself. '
                            'Craig\'s suicidal episode gets him checked into a mental hospital, where his new '
                            'neighbors include a transsexual sex addict, a girl who has scarred her own face with '
                            'scissors, and the self-elected President Armelio. There, Craig is finally able to '
                            'confront the sources of his anxiety. Ned Vizzini, who himself spent time in a '
                            'psychiatric hospital, has created a remarkably moving tale about the sometimes '
                            'unexpected road to happiness.',
                        48: 'Eric Carle\'s classic, The Very Hungry Caterpillar, in board book format. A much-loved '
                            'classic, The Very Hungry Caterpillar has won over millions of readers with its vivid and '
                            'colourful collage illustrations and its deceptively simply, hopeful story. With its '
                            'die-cut pages and finger-sized holes to explore, this is a richly satisfying book for '
                            'children. Eric Carle is an internationally bestselling and award-winning author and '
                            'illustrator of books for very young children. Eric lives in Massachusetts with his wife, '
                            'Barbara. The Carles opened The Eric Carle Museum of Picture Book Art in Massachusetts in '
                            '2002.',
                        49: 'Charlie is a freshman. And while he\'s not the biggest geek in the school, he is by no '
                            'means popular. Shy, introspective, intelligent beyond his years yet socially awkward, '
                            'he is a wallflower, caught between trying to live his life and trying to run from it. '
                            'Charlie is attempting to navigate his way through uncharted territory: the world of '
                            'first dates and mix tapes, family dramas and new friends; the world of sex, drugs, '
                            'and The Rocky Horror Picture Show, when all one requires is that perfect song on that '
                            'perfect drive to feel infinite. But he can\'t stay on the sideline forever. Standing on '
                            'the fringes of life offers a unique perspective. But there comes a time to see what it '
                            'looks like from the dance floor. The Perks of Being a Wallflower is a deeply affecting '
                            'coming-of-age story that will spirit you back to those wild and poignant roller-coaster '
                            'days known as growing up.',
                        50: 'Seconds before the Earth is demolished to make way for a galactic freeway, Arthur Dent '
                            'is plucked off the planet by his friend Ford Prefect, a researcher for the revised '
                            'edition of The Hitchhiker\'s Guide to the Galaxy who, for the last fifteen years, '
                            'has been posing as an out-of-work actor. Together this dynamic pair begin a journey '
                            'through space aided by quotes from The Hitchhiker\'s Guide ("A towel is about the most '
                            'massively useful thing an interstellar hitchhiker can have") and a galaxy-full of fellow '
                            'travelers: Zaphod Beeblebrox--the two-headed, three-armed ex-hippie and totally '
                            'out-to-lunch president of the galaxy; Trillian, Zaphod\'s girlfriend (formally Tricia '
                            'McMillan), whom Arthur tried to pick up at a cocktail party once upon a time zone; '
                            'Marvin, a paranoid, brilliant, and chronically depressed robot; Veet Voojagig, '
                            'a former graduate student who is obsessed with the disappearance of all the ballpoint '
                            'pens he bought over the years.',
                        51: "The year 1984 has come and gone, but George Orwell's prophetic, nightmarish vision in "
                            "1949 of the world we were becoming is timelier than ever. 1984 is still the great modern "
                            "classic of \"negative utopia\" -a startlingly original and haunting novel that creates "
                            "an imaginary world that is completely convincing, from the first sentence to the last "
                            "four words. No one can deny the novel's hold on the imaginations of whole generations, "
                            "or the power of its admonitions -a power that seems to grow, not lessen, "
                            "with the passage of time.",
                        52: 'Before. Miles “Pudge” Halter is done with his safe life at home. His whole life has been '
                            'one big non-event, and his obsession with famous last words has only made him crave “the '
                            'Great Perhaps” even more (Francois Rabelais, poet). He heads off to the sometimes crazy '
                            'and anything-but-boring world of Culver Creek Boarding School, and his life becomes the '
                            'opposite of safe. Because down the hall is Alaska Young. The gorgeous, clever, funny, '
                            'sexy, self-destructive, screwed up, and utterly fascinating Alaska Young. She is an '
                            'event unto herself. She pulls Pudge into her world, launches him into the Great Perhaps, '
                            'and steals his heart. Then. . . .  After. Nothing is ever the same.',
                        53: '"I fell in love the way you fall asleep: slowly, then all at once." Despite the '
                            'tumor-shrinking medical miracle that has bought her a few years, Hazel has never been '
                            'anything but terminal, her final chapter inscribed upon diagnosis. But when a gorgeous '
                            'plot twist named Augustus Waters suddenly appears at Cancer Kid Support Group, '
                            'Hazel\'s story is about to be completely rewritten. Insightful, bold, irreverent, '
                            'and raw, The Fault in Our Stars is award-winning author John Green\'s most ambitious and '
                            'heartbreaking work yet, brilliantly exploring the funny, thrilling, and tragic business '
                            'of being alive and in love. "Electric . . . Filled with staccato bursts of humor and '
                            'tragedy - Jodi Picoult A novel of life and death and the people caught in between, '
                            'The Fault in Our Stars is John Green at his best. You laugh, you cry, and then you come '
                            'back for more - Markus Zusak, author of The Book Thief',
                        54: 'Eleven Minutes is the story of Maria, a young girl from a Brazilian village, whose first '
                            'innocent brushes with love leave her heartbroken. At a tender age, she becomes convinced '
                            'that she will never find true love, instead believing that “love is a terrible thing '
                            'that will make you suffer. . . .” A chance meeting in Rio takes her to Geneva, '
                            'where she dreams of finding fame and fortune. Maria’s despairing view of love is put to '
                            'the test when she meets a handsome young painter. In this odyssey of self-discovery, '
                            'Maria has to choose between pursuing a path of darkness—sexual pleasure for its own '
                            'sake—or risking everything to find her own “inner light” and the possibility of sacred '
                            'sex, sex in the context of love',
                        55: 'Harry Potter is midway through both his training as a wizard and his coming of age. '
                            'Harry wants to get away from the pernicious Dursleys and go to the International '
                            'Quidditch Cup with Hermione, Ron, and the Weasleys. He wants to dream about Cho Chang, '
                            'his crush (and maybe do more than dream). He wants to find out about the mysterious '
                            'event that supposed to take place at Hogwarts this year, an event involving two other '
                            'rival schools of magic, and a competition that hasn\'t happened for hundreds of years. '
                            'He wants to be a normal, fourteen-year-old wizard. But unfortunately for Harry Potter, '
                            'he\'s not normal - even by wizarding standards. And in his case, different can be '
                            'deadly.',
                        56: 'This haunting story centers on Jonas, who lives in a seemingly ideal, if colorless, '
                            'world of conformity and contentment. Not until he\'s given his life assignment as the '
                            'Receiver of Memory does he begin to understand the dark, complex secrets behind his '
                            'fragile community.',
                        57: 'Percy Jackson is a good kid, but he can\'t seem to focus on his schoolwork or control '
                            'his temper. And lately, being away at boarding school is only getting worse—Percy could '
                            'have sworn his pre-algebra teacher turned into a monster and tried to kill him. When '
                            'Percy\'s mom finds out, she knows it\'s time that he knew the truth about where he came '
                            'from, and that he go to the one place he\'ll be safe. She sends Percy to Camp Half '
                            'Blood, a summer camp for demigods (on Long Island), where he learns that the father he '
                            'never knew is Poseidon, God of the Sea. Soon a mystery unfolds and together with his '
                            'friends—one a satyr and the other the demigod daughter of Athena—Percy sets out on a '
                            'quest across the United States to reach the gates of the Underworld (located in a '
                            'recording studio in Hollywood) and prevent a catastrophic war between the gods.',
                        58: 'One boy. One dragon. A world of adventure. When Eragon finds a polished blue stone in '
                            'the forest, he thinks it is the lucky discovery of a poor farm boy; perhaps it will buy '
                            'his family meat for the winter. But when the stone brings a dragon hatchling, '
                            'Eragon realizes he has stumbled upon a legacy nearly as old as the Empire itself. '
                            'Overnight his simple life is shattered, and he is thrust into a perilous new world of '
                            'destiny, magic, and power. With only an ancient sword and the advice of an old '
                            'storyteller for guidance, Eragon and the fledgling dragon must navigate the dangerous '
                            'terrain and dark enemies of an Empire ruled by a king whose evil knows no bounds. Can '
                            'Eragon take up the mantle of the legendary Dragon Riders? The fate of the Empire may '
                            'rest in his hands.',
                        59: 'In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with '
                            'the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it '
                            'to sit down on or to eat: it was a hobbit-hole, and that means comfort. Written for '
                            'J.R.R. Tolkien’s own children, The Hobbit met with instant critical acclaim when it was '
                            'first published in 1937. Now recognized as a timeless classic, this introduction to the '
                            'hobbit Bilbo Baggins, the wizard Gandalf, Gollum, and the spectacular world of '
                            'Middle-earth recounts of the adventures of a reluctant hero, a powerful and dangerous '
                            'ring, and the cruel dragon Smaug the Magnificent. The text in this 372-page paperback '
                            'edition is based on that first published in Great Britain by Collins Modern Classics ('
                            '1998), and includes a note on the text by Douglas A. Anderson (2001). Unforgettable!',
                        60: 'Lucy and Edmund, with their dreadful cousin Eustace, get magically pulled into a '
                            'painting of a ship at sea. That ship is the Dawn Treader, and on board is Caspian, '
                            'King of Narnia. He and his companions, including Reepicheep, the valiant warrior mouse, '
                            'are searching for seven lost lords of Narnia, and their voyage will take them to the '
                            'edge of the world. Their adventures include being captured by slave traders, '
                            'a much-too-close encounter with a dragon, and visits to many enchanted islands, '
                            'including the place where dreams come true.',
                        61: 'It\'s no longer safe for Harry at Hogwarts, so he and his best friends, Ron and '
                            'Hermione, are on the run. Professor Dumbledore has given them clues about what they need '
                            'to do to defeat the dark wizard, Lord Voldemort, once and for all, but it\'s up to them '
                            'to figure out what these hints and suggestions really mean. Their cross-country odyssey '
                            'has them searching desperately for the answers, while evading capture or death at every '
                            'turn. At the same time, their friendship, fortitude, and sense of right and wrong are '
                            'tested in ways they never could have imagined. The ultimate battle between good and '
                            'evil that closes out this final chapter of the epic series takes place where Harry\'s '
                            'Wizarding life began: at Hogwarts. The satisfying conclusion offers shocking last-minute '
                            'twists, incredible acts of courage, powerful new forms of magic, and the resolution of '
                            'many mysteries. Above all, this intense, cathartic book serves as a clear statement of '
                            'the message at the heart of the Harry Potter series: that choice matters much more than '
                            'destiny, and that love will always triumph over death.',
                        62: '\'They say Aslan is on the move. Perhaps he has already landed,\' whispered the Beaver. '
                            'Edmund felt a sensation of mysterious horror. Peter felt brave and adventurous. Susan '
                            'felt as if some delightful strain of music had just floated by. And Lucy got that '
                            'feeling when you realize it\'s the beginning of summer. So, deep in the bewitched land '
                            'of Narnia, the adventure begins. They opened a door and entered a world--Narnia--the '
                            'land beyond the wardrobe, the secret country known only to Peter, Susan, Edmund, '
                            'and Lucy. Lucy is the first to stumble through the back of the enormous wardrobe in the '
                            'professor\'s mysterious old country house, discovering the magic world beyond. At first, '
                            'no one believes her. But soon Edmund, Peter and Susan, too, discover the magic and meet '
                            'Aslan, the Great Lion, for themselves. And in the blink of an eye, they are changed '
                            'forever.',
                        63: 'Oryx and Crake is at once an unforgettable love story and a compelling vision of the '
                            'future. Snowman, known as Jimmy before mankind was overwhelmed by a plague, '
                            'is struggling to survive in a world where he may be the last human, and mourning the '
                            'loss of his best friend, Crake, and the beautiful and elusive Oryx whom they both loved. '
                            'In search of answers, Snowman embarks on a journey–with the help of the green-eyed '
                            'Children of Crake–through the lush wilderness that was so recently a great city, '
                            'until powerful corporations took mankind on an uncontrolled genetic engineering ride. '
                            'Margaret Atwood projects us into a near future that is both all too familiar and beyond '
                            'our imagining.',
                        64: 'The United States government is given a warning by the pre-eminent biophysicists in the '
                            'country: current sterilization procedures applied to returning space probes may be '
                            'inadequate to guarantee uncontaminated re-entry to the atmosphere. Two years later, '
                            'seventeen satellites are sent into the outer fringes of space to collect organisms and '
                            'dust for study. One of them falls to earth, landing in a desolate area of Arizona. '
                            'Twelve miles from the landing site, in the town of Piedmont, a shocking discovery is '
                            'made: the streets are littered with the dead bodies of the town\'s inhabitants, '
                            'as if they dropped dead in their tracks',
                        65: 'There\'s a killer on the loose who knows that beauty is only skin deep, and a trainee '
                            'investigator who\'s trying to save her own hide. The only man that can help is locked in '
                            'an asylum. But he\'s willing to put a brave face on - if it will help him escape.',
                        66: 'A billionaire has created a technique to clone dinosaurs. From the DNA that his crack '
                            'team of scientists extract, he is able to grow the dinosaurs in his laboratories and '
                            'lock them away on an island behind electric fences, creating a sort of theme park. He '
                            'asks a group of scientists from several different fields to come and view the park, '
                            'but something goes terribly wrong when a worker on the island turns traitor and shuts '
                            'down the power.',
                        67: 'Author Erik Larson imbues the incredible events surrounding the 1893 Chicago World\'s '
                            'Fair with such drama that readers may find themselves checking the book\'s '
                            'categorization to be sure that \'The Devil in the White City\' is not, in fact, '
                            'a highly imaginative novel. Larson tells the stories of two men: Daniel H. Burnham, '
                            'the architect responsible for the fair\'s construction, and H.H. Holmes, a serial killer '
                            'masquerading as a charming doctor. Burnham\'s challenge was immense. In a short period '
                            'of time, he was forced to overcome the death of his partner and numerous other obstacles '
                            'to construct the famous "White City" around which the fair was built. His efforts to '
                            'complete the project, and the fair\'s incredible success, are skillfully related along '
                            'with entertaining appearances by such notables as Buffalo Bill Cody, Susan B. Anthony, '
                            'Nikola Tesla and Thomas Edison. The activities of the sinister Dr. Holmes, '
                            'who is believed to be responsible for scores of murders around the time of the fair, '
                            'are equally remarkable. He devised and erected the World\'s Fair Hotel, complete with '
                            'crematorium and gas chamber, near the fairgrounds and used the event as well as his own '
                            'charismatic personality to lure victims.',
                        68: 'Four children wish on a Half Magic coin that gets their mother Alison half-way home, '
                            'rescued by Mr Smith. Mark\'s wish zaps them to a desert without island, '
                            'where half-talking cat Carrie gabbles to a camel. Romantic Katherine battles Launcelot. '
                            'Eldest Jane rejects siblings for another family. Stubborn youngest, Martha, '
                            'causes a riot downtown.',
                        69: 'This is not a fairy-tale. This is about REAL WITCHES. Real witches don\'t ride around on '
                            'broomsticks. They don\'t even wear black cloaks and hats. They are vile, cunning, '
                            'detestable creatures who disguise themselves as nice, ordinary ladies. So how can you '
                            'tell when you\'re face to face with one? Well, if you don\'t know yet you\'d better find '
                            'out quickly-because there\'s nothing a witch loathes quite as much as children and '
                            'she\'ll wield all kinds of terrifying powers to get rid of them. Ronald Dahl has done it '
                            'again! Winner of the 1983 Whitbread Award, the judges\' decision was unanimous: "funny, '
                            'wise, deliciously disgusting, a real book for children. From the first paragraph to the '
                            'last, we felt we were in the hands of a master".',
                        70: 'It\'s hard to imagine a world without A Light in the Attic. This now-classic collection '
                            'of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this '
                            'special edition. Silverstein\'s humorous and creative verse can amuse the dowdiest of '
                            'readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and '
                            'laugh and smile and love that Silverstein. Need proof of his genius? Rockabye Rockabye '
                            'baby, in the treetop Don\'t you know a treetop Is no safe place to rock? And who put you '
                            'up there, And your cradle, too? Baby, I think someone down here\'s Got it in for you. '
                            'Shel, you never sounded so good.',
                        71: 'You thought you knew the story of the “The Three Little Pigs”… You thought wrong. In '
                            'this hysterical and clever fracture fairy tale picture book that twists point of view '
                            'and perspective, young readers will finally hear the other side of the story of “The '
                            'Three Little Pigs.” “In this humorous story, Alexander T. Wolf tells his own outlandish '
                            'version of what really happens during his encounter with the three pigs…. Smith\'s '
                            'simplistic and wacky illustrations add to the effectiveness of this fractured fairy '
                            'tale.” —Children’s Literature “Older kids (and adults) will find very funny.” —School '
                            'Library Journal',
                        72: 'In this stunning new book, Malcolm Gladwell takes us on an intellectual journey through '
                            'the world of "outliers"--the best and the brightest, the most famous and the most '
                            'successful. He asks the question: what makes high-achievers different? His answer is '
                            'that we pay too much attention to what successful people are like, and too little '
                            'attention to where they are from: that is, their culture, their family, '
                            'their generation, and the idiosyncratic experiences of their upbringing. Along the way '
                            'he explains the secrets of software billionaires, what it takes to be a great soccer '
                            'player, why Asians are good at math, and what made the Beatles the greatest rock band.',
                        73: 'Andrew "Ender" Wiggin thinks he is playing computer simulated war games; he is, in fact, '
                            'engaged in something far more desperate. The result of genetic experimentation, '
                            'Ender may be the military genius Earth desperately needs in a war against an alien enemy '
                            'seeking to destroy all human life. The only way to find out is to throw Ender into ever '
                            'harsher training, to chip away and find the diamond inside, or destroy him utterly. '
                            'Ender Wiggin is six years old when it begins. He will grow up fast. But Ender is not the '
                            'only result of the experiment. The war with the Buggers has been raging for a hundred '
                            'years, and the quest for the perfect general has been underway almost as long. Ender\'s '
                            'two older siblings, Peter and Valentine, are every bit as unusual as he is, but in very '
                            'different ways. While Peter was too uncontrollably violent, Valentine very nearly lacks '
                            'the capability for violence altogether. Neither was found suitable for the military\'s '
                            'purpose. But they are driven by their jealousy of Ender, and by their inbred drive for '
                            'power. Peter seeks to control the political process, to become a ruler. Valentine\'s '
                            'abilities turn more toward the subtle control of the beliefs of commoner and elite '
                            'alike, through powerfully convincing essays. Hiding their youth and identities behind '
                            'the anonymity of the computer networks, these two begin working together to shape the '
                            'destiny of Earth-an Earth that has no future at all if their brother Ender fails.',
                        74: 'Twelve-year-old Artemis Fowl is a millionaire, a genius—and, above all, a criminal '
                            'mastermind. But even Artemis doesn\'t know what he\'s taken on when he kidnaps a fairy, '
                            'Captain Holly Short of the LEPrecon Unit. These aren\'t the fairies of bedtime '
                            'stories—they\'re dangerous! Full of unexpected twists and turns, Artemis Fowl is a '
                            'riveting, magical adventure.',
                        75: 'Stanley Yelnats is under a curse. A curse that began with his '
                            'no-good-dirty-rotten-pig-stealing-great-great-grandfather and has since followed '
                            'generations of Yelnatses. Now Stanley has been unjustly sent to a boys’ detention '
                            'center, Camp Green Lake, where the boys build character by spending all day, '
                            'every day digging holes exactly five feet wide and five feet deep. There is no lake at '
                            'Camp Green Lake. But there are an awful lot of holes. It doesn’t take long for Stanley '
                            'to realize there’s more than character improvement going on at Camp Green Lake. The boys '
                            'are digging holes because the warden is looking for something. But what could be buried '
                            'under a dried-up lake? Stanley tries to dig up the truth in this inventive and darkly '
                            'humorous tale of crime and punishment—and redemption.',
                        76: 'It was a dark and stormy night; Meg Murry, her small brother Charles Wallace, and her '
                            'mother had come down to the kitchen for a midnight snack when they were upset by the '
                            'arrival of a most disturbing stranger.  "Wild nights are my glory," the unearthly '
                            'stranger told them. "I just got caught in a downdraft and blown off course. Let me be on '
                            'my way. Speaking of way, by the way, there is such a thing as a tesseract". Meg\'s '
                            'father had been experimenting with this fifth dimension of time travel when he '
                            'mysteriously disappeared. Now the time has come for Meg, her friend Calvin, and Charles '
                            'Wallace to rescue him. But can they outwit the forces of evil they will encounter on '
                            'their heart-stopping journey through space?',
                        77: 'Here lives an orphaned ward named Lyra Belacqua, whose carefree life among the scholars '
                            'at Oxford\'s Jordan College is shattered by the arrival of two powerful visitors. First, '
                            'her fearsome uncle, Lord Asriel, appears with evidence of mystery and danger in the far '
                            'North, including photographs of a mysterious celestial phenomenon called Dust and the '
                            'dim outline of a city suspended in the Aurora Borealis that he suspects is part of an '
                            'alternate universe. He leaves Lyra in the care of Mrs. Coulter, an enigmatic scholar and '
                            'explorer who offers to give Lyra the attention her uncle has long refused her. In this '
                            'multilayered narrative, however, nothing is as it seems. Lyra sets out for the top of '
                            'the world in search of her kidnapped playmate, Roger, bearing a rare truth-telling '
                            'instrument, the alethiometer. All around her children are disappearing—victims of '
                            'so-called "Gobblers"—and being used as subjects in terrible experiments that separate '
                            'humans from their daemons, creatures that reflect each person\'s inner being. And '
                            'somehow, both Lord Asriel and Mrs. Coulter are involved.',
                        78: 'Tally is about to turn sixteen, and she can\'t wait. In just a few weeks she\'ll have '
                            'the operation that will turn her from a repellent ugly into a stunning pretty. And as a '
                            'pretty, she\'ll be catapulted into a high-tech paradise where her only job is to have '
                            'fun. But Tally\'s new friend Shay isn\'t sure she wants to become a pretty. When Shay '
                            'runs away, Tally learns about a whole new side of the pretty world-- and it isn\'t very '
                            'pretty. The authorities offer Tally a choice: find her friend and turn her in, '
                            'or never turn pretty at all. Tally\'s choice will change her world forever...',
                        79: 'A bank of clouds was assembling on the not-so-distant horizon, '
                            'but journalist-mountaineer Jon Krakauer, standing on the summit of Mt. Everest, '
                            'saw nothing that "suggested that a murderous storm was bearing down." He was wrong. The '
                            'storm, which claimed five lives and left countless more--including Krakauer\'s--in '
                            'guilt-ridden disarray, would also provide the impetus for Into Thin Air, Krakauer\'s '
                            'epic account of the May 1996 disaster. ',
                        80: 'First, there were ten - a curious assortment of strangers summoned as weekend guests to '
                            'a private island off the coast of Devon. Their host, an eccentric millionaire unknown to '
                            'all of them, is nowhere to be found. All that the guests have in common is a wicked past '
                            'they\'re unwilling to reveal - and a secret that will seal their fate. For each has been '
                            'marked for murder. One by one they fall prey. Before the weekend is out, there will be '
                            'none. And only the dead are above suspicion.',
                        81: 'What goes on in human beings when they make or listen to music? What is it about music, '
                            'what gives it such peculiar power over us, power delectable and beneficent for the most '
                            'part, but also capable of uncontrollable and sometimes destructive force? Music has no '
                            'concepts, it lacks images; it has no power of representation, it has no relation to the '
                            'world. And yet it is evident in all of us–we tap our feet, we keep time, hum, sing, '
                            'conduct music, mirror the melodic contours and feelings of what we hear in our movements '
                            'and expressions. In this book, Oliver Sacks explores the power music wields over us–a '
                            'power that sometimes we control and at other times don’t. He explores, in his inimitable '
                            'fashion, how it can provide access to otherwise unreachable emotional states, '
                            'how it can revivify neurological avenues that have been frozen, evoke memories of '
                            'earlier, lost events or states or bring those with neurological disorders back to a time '
                            'when the world was much richer. This is a book that explores, like no other, the myriad '
                            'dimensions of our experience of and with music. ',
                        82: 'Walden, or, Life in the Woods, is an American book written by noted transcendentalist '
                            'Henry David Thoreau. The work is part personal declaration of independence, '
                            'social experiment, voyage of spiritual discovery, satire, and manual for self-reliance. '
                            'Published in 1854, it details Thoreau\'s experiences over the course of two years in a '
                            'cabin he built near Walden Pond, amid woodland owned by his friend and mentor Ralph '
                            'Waldo Emerson, near Concord, Massachusetts.',
                        83: 'Brought up in the household of a powerful Baron, Candide is an open-minded young man, '
                            'whose tutor, Pangloss, has instilled in him the belief that \'all is for the best\'. But '
                            'when his love for the Baron\'s rosy-cheeked daughter is discovered, Candide is cast out '
                            'to make his own way in the world. And so he and his various companions begin a '
                            'breathless tour of Europe, South America and Asia, as an outrageous series of disasters '
                            'befall them - earthquakes, syphilis, a brush with the Inquisition, murder - sorely '
                            'testing the young hero\'s optimism.',
                        84: 'In the novel, Siddhartha, a young man, leaves his family for a contemplative life, then, '
                            'restless, discards it for one of the flesh. He conceives a son, but bored and sickened '
                            'by lust and greed, moves on again. Near despair, Siddhartha comes to a river where he '
                            'hears a unique sound. This sound signals the true beginning of his life—the beginning of '
                            'suffering, rejection, peace, and, finally, wisdom.',
                        85: 'One of the most important & influential books written in the past half-century, '
                            'Robert M. Pirsig\'s Zen & the Art of Motorcycle Maintenance is a powerfully moving & '
                            'penetrating examination of how we live, a breathtaking meditation on how to live better. '
                            'Here is the book that transformed a generation, an unforgettable narration of a summer '
                            'motorcycle trip across America\'s Northwest, undertaken by a father & his young son. A '
                            'story of love & fear--of growth, discovery & acceptance--that becomes a profound '
                            'personal & philosophical odyssey into life\'s fundamental questions, this uniquely '
                            'exhilarating modern classic is both touching & transcendent, resonant with the myriad '
                            'confusions of existence & the small, essential triumphs that propel us forward.',
                        86: 'Oscar Wilde\'s madcap farce about mistaken identities, secret engagements, and lovers '
                            'entanglements still delights readers more than a century after its 1895 publication and '
                            'premiere performance. The rapid-fire wit and eccentric characters of The Importance of '
                            'Being Earnest have made it a mainstay of the high school curriculum for decades. Cecily '
                            'Cardew and Gwendolen Fairfax are both in love with the same mythical suitor. Jack '
                            'Worthing has wooed Gewndolen as Ernest while Algernon has also posed as Ernest to win '
                            'the heart of Jack\'s ward, Cecily. When all four arrive at Jack\'s country home on the '
                            'same weekend the "rivals" to fight for Ernest s undivided attention and the "Ernests" to '
                            'claim their beloveds pandemonium breaks loose. Only a senile nursemaid and an old, '
                            'discarded hand-bag can save the day! This Prestwick House Literary Touchstone Edition '
                            'includes a glossary and reader\'s notes to help the modern reader appreciate Wilde\'s '
                            'wry wit and elaborate plot twists.',
                        87: '"A green hunting cap squeezed the top of the fleshy balloon of a head. The green '
                            'earflaps, full of large ears and uncut hair and the fine bristles that grew in the ears '
                            'themselves, stuck out on either side like turn signals indicating two directions at '
                            'once. Full, pursed lips protruded beneath the bushy black moustache and, '
                            'at their corners, sank into little folds filled with disapproval and potato chip '
                            'crumbs." Meet Ignatius J. Reilly, the hero of John Kennedy Toole\'s tragicomic tale, '
                            'A Confederacy of Dunces. This 30-year-old medievalist lives at home with his mother in '
                            'New Orleans, pens his magnum opus on Big Chief writing pads he keeps hidden under his '
                            'bed, and relays to anyone who will listen the traumatic experience he once had on a '
                            'Greyhound Scenicruiser bound for Baton Rouge. ("Speeding along in that bus was like '
                            'hurtling into the abyss.") But Ignatius\'s quiet life of tyrannizing his mother and '
                            'writing his endless comparative history screeches to a halt when he is almost arrested '
                            'by the overeager Patrolman Mancuso--who mistakes him for a vagrant--and then involved in '
                            'a car accident with his tipsy mother behind the wheel. One thing leads to another, '
                            'and before he knows it, Ignatius is out pounding the pavement in search of a job. Over '
                            'the next several hundred pages, our hero stumbles from one adventure to the next. His '
                            'stint as a hotdog vendor is less than successful, and he soon turns his employers at the '
                            'Levy Pants Company on their heads. Ignatius\'s path through the working world is '
                            'populated by marvelous secondary characters: the stripper Darlene and her talented '
                            'cockatoo; the septuagenarian secretary Miss Trixie, whose desperate attempts to retire '
                            'are constantly, comically thwarted; gay blade Dorian Greene; sinister Miss Lee, '
                            'proprietor of the Night of Joy nightclub; and Myrna Minkoff, the girl Ignatius loves to '
                            'hate. The many subplots that weave through A Confederacy of Dunces are as complicated as '
                            'anything you\'ll find in a Dickens novel, and just as beautifully tied together in the '
                            'end. But it is Ignatius--selfish, domineering, and deluded, tragic and comic and larger '
                            'than life--who carries the story. He is a modern-day Quixote beset by giants of the '
                            'modern age. His fragility cracks the shell of comic bluster, revealing a deep streak of '
                            'melancholy beneath the antic humor. John Kennedy Toole committed suicide in 1969 and '
                            'never saw the publication of his novel. Ignatius Reilly is what he left behind, '
                            'a fitting memorial to a talented and tormented life.',
                        88: 'One night Max puts on his wolf suit and makes mischief of one kind and another, '
                            'so his mother calls him \'Wild Thing\' and sends him to bed without his supper. That '
                            'night a forest begins to grow in Max\'s room and an ocean rushes by with a boat to take '
                            'Max to the place where the wild things are. Max tames the wild things and crowns himself '
                            'as their king, and then the wild rumpus begins. But when Max has sent the monsters to '
                            'bed, and everything is quiet, he starts to feel lonely and realises it is time to sail '
                            'home to the place where someone loves him best of all.',
                        89: 'What happens when the most beautiful girl in the world marries the handsomest prince of '
                            'all time and he turns out to be...well...a lot less than the man of her dreams? As a '
                            'boy, William Goldman claims, he loved to hear his father read the S. Morgenstern '
                            'classic, The Princess Bride. But as a grown-up he discovered that the boring parts were '
                            'left out of good old Dad\'s recitation, and only the "good parts" reached his ears. Now '
                            'Goldman does Dad one better. He\'s reconstructed the "Good Parts Version" to delight '
                            'wise kids and wide-eyed grownups everywhere. What\'s it about? Fencing. Fighting. True '
                            'Love. Strong Hate. Harsh Revenge. A Few Giants. Lots of Bad Men. Lots of Good Men. Five '
                            'or Six Beautiful Women. Beasties Monstrous and Gentle. Some Swell Escapes and Captures. '
                            'Death, Lies, Truth, Miracles, and a Little Sex. In short, it\'s about everything.',
                        90: 'Following the lives of four sisters on a journey out of adolescence, Louisa May '
                            'Alcott\'s Little Women explores the difficulties associated with gender roles in a '
                            'Post-Civil War America.',
                        91: 'A timeless tale by the incomparable Kate DiCamillo, complete with stunning full-color '
                            'plates by Bagram Ibatoulline, honors the enduring power of love. "Someone will come for '
                            'you, but first you must open your heart. . . ." Once, in a house on Egypt Street, '
                            'there lived a china rabbit named Edward Tulane. The rabbit was very pleased with '
                            'himself, and for good reason: he was owned by a girl named Abilene, who treated him with '
                            'the utmost care and adored him completely. And then, one day, he was lost. Kate '
                            'DiCamillo takes us on an extraordinary journey, from the depths of the ocean to the net '
                            'of a fisherman, from the top of a garbage heap to the fireside of a hoboes\' camp, '
                            'from the bedside of an ailing child to the bustling streets of Memphis. And along the '
                            'way, we are shown a true miracle — that even a heart of the most breakable kind can '
                            'learn to love, to lose, and to love again.',
                        92: 'It’s just a small story really, about among other things: a girl, some words, '
                            'an accordionist, some fanatical Germans, a Jewish fist-fighter, and quite a lot of '
                            'thievery. . . . Set during World War II in Germany, Markus Zusak’s groundbreaking new '
                            'novel is the story of Liesel Meminger, a foster girl living outside of Munich. Liesel '
                            'scratches out a meager existence for herself by stealing when she encounters something '
                            'she can’t resist–books. With the help of her accordion-playing foster father, '
                            'she learns to read and shares her stolen books with her neighbors during bombing raids '
                            'as well as with the Jewish man hidden in her basement before he is marched to Dachau. '
                            'This is an unforgettable story about the ability of books to feed the soul.',
                        93: 'The terrifyingly prophetic novel of a post-literate future. Guy Montag is a fireman. '
                            'His job is to burn books, which are forbidden, being the source of all discord and '
                            'unhappiness. Even so, Montag is unhappy; there is discord in his marriage. Are books '
                            'hidden in his house? The Mechanical Hound of the Fire Department, armed with a lethal '
                            'hypodermic, escorted by helicopters, is ready to track down those dissidents who defy '
                            'society to preserve and read books. The classic dystopian novel of a post-literate '
                            'future, Fahrenheit 451 stands alongside Orwell’s 1984 and Huxley’s Brave New World as a '
                            'prophetic account of Western civilization’s enslavement by the media, drugs and '
                            'conformity. Bradbury’s powerful and poetic prose combines with uncanny insight into the '
                            'potential of technology to create a novel which, decades on from first publication, '
                            'still has the power to dazzle and shock.',
                        94: 'Kurt Vonnegut\'s absurdist classic Slaughterhouse-Five introduces us to Billy Pilgrim, '
                            'a man who becomes unstuck in time after he is abducted by aliens from the planet '
                            'Tralfamadore. In a plot-scrambling display of virtuosity, we follow Pilgrim '
                            'simultaneously through all phases of his life, concentrating on his (and Vonnegut\'s) '
                            'shattering experience as an American prisoner of war who witnesses the firebombing of '
                            'Dresden. Don\'t let the ease of reading fool you - Vonnegut\'s isn\'t a conventional, '
                            'or simple, novel. He writes, "There are almost no characters in this story, and almost '
                            'no dramatic confrontations, because most of the people in it are so sick, and so much '
                            'the listless playthings of enormous forces. One of the main effects of war, after all, '
                            'is that people are discouraged from being characters." Slaughterhouse-Five is not only '
                            'Vonnegut\'s most powerful book, it is also as important as any written since 1945. Like '
                            'Catch- 22, it fashions the author\'s experiences in the Second World War into an '
                            'eloquent and deeply funny plea against butchery in the service of authority. '
                            'Slaughterhouse-Five boasts the same imagination, humanity, and gleeful appreciation of '
                            'the absurd found in Vonnegut\'s other works, but the book\'s basis in rock-hard, '
                            'tragic fact gives it a unique poignancy - and humor. ',
                        95: '"In this classic of the 1960s, Ken Kesey\'s hero is Randle Patrick McMurphy, '
                            'a boisterous, brawling, fun-loving rebel who swaggers into the world of a mental '
                            'hospital and takes over. A lusty, life-affirming fighter, McMurphy rallies the other '
                            'patients around him by challenging the dictatorship of Nurse Ratched. He promotes '
                            'gambling in the ward, smuggles in wine and women, and openly defies the rules at every '
                            'turn. But this defiance, which starts as a sport, soon develops into a grim struggle, '
                            'an all-out war between two relentless opponents: Nurse Ratched, back by the full power '
                            'of authority, and McMurphy, who has only his own indomitable will. What happens when '
                            'Nurse Ratched uses her ultimate weapon against McMurphy provides the story\'s shocking '
                            'climax.',
                        96: 'THE GREAT GATSBY, F. Scott Fitzgerald’s third book, stands as the supreme achievement of '
                            'his career. This exemplary novel of the Jazz Age has been acclaimed by generations of '
                            'readers. The story of the fabulously wealthy Jay Gatsby and his love for the beautiful '
                            'Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted '
                            '“gin was the national drink and sex the national obsession,” it is an exquisitely '
                            'crafted tale of America in the 1920s. The Great Gatsby is one of the great classics of '
                            'twentieth-century literature.',
                        97: 'Harry Potter\'s life is miserable. His parents are dead and he\'s stuck with his '
                            'heartless relatives, who force him to live in a tiny closet under the stairs. But his '
                            'fortune changes when he receives a letter that tells him the truth about himself: he\'s '
                            'a wizard. A mysterious visitor rescues him from his relatives and takes him to his new '
                            'home, Hogwarts School of Witchcraft and Wizardry. After a lifetime of bottling up his '
                            'magical powers, Harry finally feels like a normal kid. But even within the Wizarding '
                            'community, he is special. He is the boy who lived: the only person to have ever survived '
                            'a killing curse inflicted by the evil Lord Voldemort, who launched a brutal takeover of '
                            'the Wizarding world, only to vanish after failing to kill Harry. Though Harry\'s first '
                            'year at Hogwarts is the best of his life, not everything is perfect. There is a '
                            'dangerous secret object hidden within the castle walls, and Harry believes it\'s his '
                            'responsibility to prevent it from falling into evil hands. But doing so will bring him '
                            'into contact with forces more terrifying than he ever could have imagined. Full of '
                            'sympathetic characters, wildly imaginative situations, and countless exciting details, '
                            'the first installment in the series assembles an unforgettable magical world and sets '
                            'the stage for many high-stakes adventures to come.',
                        98: 'Paulo Coelho\'s enchanting novel has inspired a devoted following around the world. This '
                            'story, dazzling in its powerful simplicity and inspiring wisdom, is about an Andalusian '
                            'shepherd boy named Santiago who travels from his homeland in Spain to the Egyptian '
                            'desert in search of a treasure buried in the Pyramids. Along the way he meets a Gypsy '
                            'woman, a man who calls himself king, and an alchemist, all of whom point Santiago in the '
                            'direction of his quest. No one knows what the treasure is, or if Santiago will be able '
                            'to surmount the obstacles along the way. But what starts out as a journey to find '
                            'worldly goods turns into a discovery of the treasure found within. Lush, evocative, '
                            'and deeply humane, the story of Santiago is an eternal testament to the transforming '
                            'power of our dreams and the importance of listening to our hearts',
                        99: 'Christopher John Francis Boone knows all the countries of the world and their capitals '
                            'and every prime number up to 7,057. He relates well to animals but has no understanding '
                            'of human emotions. He cannot stand to be touched. And he detests the color yellow. '
                            'Although gifted with a superbly logical brain, for fifteen-year-old Christopher everyday '
                            'interactions and admonishments have little meaning. He lives on patterns, rules, '
                            'and a diagram kept in his pocket. Then one day, a neighbor\'s dog, Wellington, '
                            'is killed and his carefully constructive universe is threatened. Christopher sets out to '
                            'solve the murder in the style of his favourite (logical) detective, Sherlock Holmes. '
                            'What follows makes for a novel that is funny, poignant and fascinating in its portrayal '
                            'of a person whose curse and blessing are a mind that perceives the world entirely '
                            'literally.',
                        100: "When Magizoologist Newt Scamander arrives in New York, he intends his stay to be just a "
                             "brief stopover. However, when his magical case is misplaced and some of Newt's "
                             "fantastic beasts escape, it spells trouble for everyone… Fantastic Beasts and Where to "
                             "Find Them marks the screenwriting debut of J.K. Rowling, author of the beloved and "
                             "internationally bestselling Harry Potter books. Featuring a cast of remarkable "
                             "characters, this is epic, adventure-packed storytelling at its very best. Whether an "
                             "existing fan or new to the wizarding world, this is a perfect addition to any reader's "
                             "bookshelf.",
                        101: 'The Dursleys were so mean and hideous that summer that all Harry Potter wanted was to '
                             'get back to the Hogwarts School for Witchcraft and Wizardry. But just as he\'s packing '
                             'his bags, Harry receives a warning from a strange, impish creature named Dobby who says '
                             'that if Harry Potter returns to Hogwarts, disaster will strike. And strike it does. '
                             'For in Harry\'s second year at Hogwarts, fresh torments and horrors arise, including an '
                             'outrageously stuck-up new professor, Gilderoy Lockhart, a spirit named Moaning Myrtle '
                             'who haunts the girls\' bathroom, and the unwanted attentions of Ron Weasley\'s younger '
                             'sister, Ginny. But each of these seem minor annoyances when the real trouble begins, '
                             'and someone, or something, starts turning Hogwarts students to stone. Could it be Draco '
                             'Malfoy, a more poisonous rival than ever? Could it possibly be Hagrid, whose mysterious '
                             'past is finally told? Or could it be the one everyone at Hogwarts most suspects: Harry '
                             'Potter himself?',
                        102: "Harry Potter is lucky to reach the age of thirteen, since he has already survived the "
                             "murderous attacks of the feared Dark Lord on more than one occasion. But his hopes for "
                             "a quiet term concentrating on Quidditch are dashed when a maniacal mass-murderer "
                             "escapes from Azkaban, pursued by the soul-sucking Dementors who guard the prison. It's "
                             "assumed that Hogwarts is the safest place for Harry to be. But is it a coincidence that "
                             "he can feel eyes watching him in the dark, and should he be taking Professor "
                             "Trelawney's ghoulish predictions seriously? ",
                        103: "Harry Potter is due to start his fifth year at Hogwarts School of Witchcraft and "
                             "Wizardry. His best friends Ron and Hermione have been very secretive all summer and he "
                             "is desperate to get back to school and find out what has been going on. However, "
                             "what Harry discovers is far more devastating than he could ever have expected... "
                             "Suspense, secrets and thrilling action from the pen of J.K. Rowling ensure an "
                             "electrifying adventure that is impossible to put down.",
                        104: "It is the middle of the summer, but there is an unseasonal mist pressing against the "
                             "windowpanes. Harry Potter is waiting nervously in his bedroom at the Dursleys' house in "
                             "Privet Drive for a visit from Professor Dumbledore himself. One of the last times he "
                             "saw the Headmaster was in a fierce one-to-one duel with Lord Voldemort, and Harry can't "
                             "quite believe that Professor Dumbledore will actually appear at the Dursleys' of all "
                             "places. Why is the Professor coming to visit him now? What is it that cannot wait until "
                             "Harry returns to Hogwarts in a few weeks' time? Harry's sixth year at Hogwarts has "
                             "already got off to an unusual start, as the worlds of Muggle and magic start to "
                             "intertwine... J.K. Rowling charts Harry Potter's latest adventures in his sixth year "
                             "at Hogwarts with consummate skill and in breathtaking fashion",
                        105: "The New York Times Best Seller is now a major motion picture starring Lily James and "
                             "Sam Riley, with Matt Smith, Charles Dance, and Lena Headey.  “It is a truth "
                             "universally acknowledged that a zombie in possession of brains must be in want of more "
                             "brains.” So begins Pride and Prejudice and Zombies, an expanded edition of the beloved "
                             "Jane Austen novel featuring all-new scenes of bone-crunching zombie mayhem. As our "
                             "story opens, a mysterious plague has fallen upon the quiet English village of "
                             "Meryton—and the dead are returning to life! Feisty heroine Elizabeth Bennet is "
                             "determined to wipe out the zombie menace, but she’s soon distracted by the arrival of "
                             "the haughty and arrogant Mr. Darcy. What ensues is a delightful comedy of manners with "
                             "plenty of civilized sparring between the two young lovers—and even more violent "
                             "sparring on the blood-soaked battlefield. Can Elizabeth vanquish the spawn of Satan? "
                             "And overcome the social prejudices of the class-conscious landed gentry? Complete with "
                             "romance, heartbreak, swordfights, cannibalism, and thousands of rotting corpses, "
                             "Pride and Prejudice and Zombies transforms a masterpiece of world literature into "
                             "something you’d actually want to read."}
dictBookGenres = {106: ('Historical Fiction, Sci-Fi/Fantasy'), 1: ('Speculative Fiction', 'Sci-Fi'),
                  2: ('Fantasy', 'Humor', 'Satire'),
                  3: ('Fantasy', 'Epic Fantasy'), 4: ('Existentialism', 'Classic', 'Literature'),
                  5: ('Comedy', 'Comic', 'Graphic Novel', 'Sex Comedy'), 6: ('Fantasy', 'Humor', 'Satire'),
                  7: ('Fantasy', 'Epic Fantasy'),
                  8: ('Memoir'), 9: ('Mystery', 'Crime', 'Thriller'), 10: ('Fantasy', 'Epic Fantasy'),
                  11: ('Play', 'Drama', 'Fantasy'),
                  12: ('Fantasy', 'Epic Fantasy'), 13: ('Horror', 'Psychological Thriller'),
                  14: ('Horror', 'Supernatural', 'Thriller'),
                  15: ('Classic', 'Romance', 'Literature', 'Historical Fiction'),
                  16: ('Horror', 'Supernatural', 'Thriller'),
                  17: ('Graphic Novel', 'Comic', 'Horror', 'Superhero'),
                  18: ('Graphic Novel', 'Superhero', 'Comic'),
                  19: ('Memoir', 'Comedy'), 20: ('Fantasy', 'Horror', 'Mystery'), 21: ('Literature', 'Apocalyptic'),
                  22: ('Literature', 'Mystery'), 23: ('Literature', 'Historical Fiction'),
                  24: ('Literature', 'Classic'),
                  25: ('Literature', 'Magical Realism'), 26: ('Memoir', 'Nonfiction', 'Autobiography'),
                  27: ('Humor', 'Comedy', 'Mystery', 'Thriller'), 28: ('Literature', 'Magical Realism', 'Classic'),
                  29: ('Literature', 'Coming-of-Age'), 30: ('Literature', 'Classic', 'Adventure'),
                  31: ('Play', 'Drama'),
                  32: ('Humor', 'Fantasy', 'Apocalyptic'), 33: ('Play', 'Fantasy', 'Classic'),
                  34: ('Classic', 'Autobiography', 'Nonfiction', 'Memoir'),
                  35: ('History', 'Nonfiction', 'Travel', 'Western American History'),
                  36: ('Short Stories', 'Literature', 'Western'),
                  37: ('History', 'Nonfiction', 'War'), 38: ('Literature', 'Gothic', 'Fantasy'),
                  39: ('Historical Fiction', 'Magical Realism', 'Fantasy'), 40: ('Classic', 'Literature'),
                  41: ('Fantasy', 'Urban Fantasy'),
                  42: ('Humor', 'Sci-Fi/Fantasy', 'Magical Realism', 'Literature'),
                  43: ('Magical Realism', 'Literature', 'Modern Classic'), 44: ('Mystery', 'Crime', 'Thriller'),
                  45: ('Historical Fiction', 'Literature'), 46: ('Children\'s'), 47: ('Young Adult', 'Coming-of-Age'),
                  48: ('Children\'s'), 49: ('Young Adult', 'Coming-of-Age'), 50: ('Humor', 'Satire', 'Sci-Fi'),
                  51: ('Sci-Fi', 'Dystopia', 'Classic', 'Literature'),
                  52: ('Coming-of-Age', 'Boarding School', 'Young Adult'),
                  53: ('Young Adult', 'Romance', 'Drama'), 54: ('Literature', 'Romance'),
                  55: ('Fantasy', 'Young Adult', 'Boarding School'), 56: ('Dystopia', 'Sci-Fi', 'Young Adult'),
                  57: ('Fantasy', 'Young Adult'), 58: ('Fantasy', 'Young Adult'),
                  59: ('Fantasy', 'Classic', 'Adventure'),
                  60: ('Fantasy', 'Young Adult', 'Children\'s'), 61: ('Fantasy', 'Young Adult'),
                  62: ('Fantasy', 'Young Adult', 'Children\'s'), 63: ('Apocalyptic', 'Sci-Fi', 'Dystopia'),
                  64: ('Sci-Fi', 'Thriller', 'Disaster'), 65: ('Horror', 'Thriller', 'Crime', 'Mystery'),
                  66: ('Sci-Fi', 'Disaster', 'Adventure'), 67: ('Nonfiction', 'True Crime', 'History'),
                  68: ('Fantasy', 'Children\'s', 'Classic'), 69: ('Fantasy', 'Children\'s', 'Classic'),
                  70: ('Poetry', 'Children\'s', 'Humor'), 71: ('Children\'s', 'Humor', 'Fairy Tale\'s'),
                  72: ('Nonfiction', 'Psychology', 'Economics'),
                  73: ('Sci-Fi', 'Young Adult', 'Classic', 'Military'),
                  74: ('Fantasy', 'Young Adult'), 75: ('Children\'s', 'Literature'),
                  76: ('Fantasy', 'Young Adult', 'Classic', 'Sci-Fi'), 77: ('Fantasy', 'Young Adult'),
                  78: ('Dystopia', 'Young Adult', 'Sci-Fi'),
                  79: ('Nonfiction', 'Adventure', 'Survival', 'Memoir', 'Biography', 'Travel'),
                  80: ('Mystery', 'Classic', 'Thriller'), 81: ('Psychology', 'Memoir'),
                  82: ('Classic', 'Nonfiction', 'Philosophy', 'Environmentalism'),
                  83: ('Classic', 'Literature', 'Philosophy'),
                  84: ('Classic', 'Literature', 'Philosophy', 'Religion'),
                  85: ('Philosophy', 'Literature', 'Classic'),
                  86: ('Classic', 'Play', 'Drama', 'Humor', 'Literature'), 87: ('Humor', 'Literature'),
                  88: ('Children\'s', 'Adventure'), 89: ('Fantasy', 'Humor', 'Classic', 'Romance', 'Adventure'),
                  90: ('Classic', 'Historical Fiction', 'Romance'), 91: ('Fantasy', 'Children\'s', 'Adventure'),
                  92: ('Young Adult', 'Historical Fiction', 'War'),
                  93: ('Classic', 'Sci-Fi', 'Dystopia', 'Literature'),
                  94: ('Sci-Fi', 'Absurdist', 'Classic', 'Literature', 'War'),
                  95: ('Classic', 'Literature', 'Fiction', 'Psychology'),
                  96: ('Classic', 'Literature', 'Romance', 'Historical Fiction'),
                  97: ('Children\'s', 'Fantasy', 'Young Adult', 'Boarding School', 'Adventure'),
                  98: ('Fantasy', 'Philosophy', 'Literature'), 99: ('Literature', 'Young Adult'),
                  100: ('Fantasy', 'Young Adult', 'Adventure', 'Screenplay'),
                  101: ('Mystery','Fantasy','Young Adult','Boarding School', 'Children\'s'),
                  102: ('Fantasy','Young Adult','Boarding School', 'Adventure'),
                  103: ('Fantasy','Young Adult','Boarding School','Coming-of-Age'),
                  104: ('Fantasy','Young Adult','Boarding School', 'Coming-of-Age'),
                  105: ('Horror', 'Fantasy','Humor', 'Classic', 'Romance')}
bookDict = {}
i = 1
for title in dictBookTitles:
    bookDict[i] = {'Genre': dictBookGenres[i], 'Description': dictBookDescriptions[i], 'Author': dictBookAuthors[i],
                   'Title': dictBookTitles[i]}
    print(str(i) + " " + str(bookDict[i]))
    i += 1

with open('Book_Pickles/SampleDict.pkl', 'wb') as handle:
    pickle.dump(bookDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
