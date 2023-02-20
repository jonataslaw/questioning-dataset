import re

text = """
Question: When was the American Civil War?
Answer: The American Civil War was fought from 1861 to 1865.
''''
Question: When was the French Revolution?
Answer: The French Revolution began in 1789 and ended in 1799.
''''
Question: When was the first World War?
Answer: The First World War began in 1914 and ended in 1918.
''''
Question: When was the United Nations founded?
Answer: The United Nations was founded on October 24, 1945.
''''
Question: When was the first Olympic Games?
Answer: The first Olympic Games were held in ancient Greece in 776 BC.
''''
Question: When was the first successful human landing on the moon?
Answer: The first successful human landing on the moon was on July 20, 1969, as part of the Apollo 11 mission.
''''
Question: When was the first computer invented?
Answer: The first electronic computer, called the Electronic Numerical Integrator And Computer (ENIAC), was invented in 1945 by John W. Mauchly and J. Presper Eckert.
''''
Question: When was the first smartphone invented?
Answer: The first smartphone, IBM Simon, was invented in 1992.
''''
Question: When was the first iPhone released?
Answer: The first iPhone was released on June 29, 2007.
''''
Question: When was the internet first introduced?
Answer: The first message was sent over the internet on October 29, 1969. It was sent from a computer at UCLA to a computer at SRI International in Menlo Park, California.
''''
Question: Where is Mount Everest located?
Answer: Mount Everest is located on the border of Nepal and Tibet, in the Himalayas mountain range.
''''
Question: Where is the Great Wall of China located?
Answer: The Great Wall of China is located in northern China, stretching across several provinces including Liaoning, Hebei, Tianjin, Beijing, Inner Mongolia, Shanxi, Shaanxi, Ningxia, and Gansu.
''''
Question: Where is the Louvre Museum located?
Answer: The Louvre Museum is located in Paris, France.
''''
Question: Where is the Victoria Falls located?
Answer: The Victoria Falls is located on the border of Zambia and Zimbabwe, in southern Africa.
''''
Question: Where is the Amazon Rainforest located?
Answer: The Amazon Rainforest is located in South America, spanning across several countries including Brazil, Peru, Colombia, Ecuador, Bolivia, and Venezuela.
''''
Question: Where is the Great Barrier Reef located?
Answer: The Great Barrier Reef is located off the coast of northeastern Australia, in the Coral Sea.
''''
Question: Where is the Grand Canyon located?
Answer: The Grand Canyon is located in Arizona, USA.
''''
Question: Where is the Niagara Falls located?
Answer: The Niagara Falls is located on the border of Ontario, Canada and New York, USA.
''''
Question: Who discovered the structure of DNA?
Answer: James Watson and Francis Crick, with the assistance of Rosalind Franklin and Maurice Wilkins, discovered the structure of DNA in 1953. They proposed a double helix model, which was later confirmed through X-ray crystallography.
''''
Question: Who invented the telephone?
Answer: Alexander Graham Bell is credited with inventing the telephone in 1876. He was awarded the first US patent for an "improvement in telegraphy" which described an "electrical speech circuit."
''''
Question: Who wrote the Declaration of Independence?
Answer: Thomas Jefferson is credited as the primary author of the Declaration of Independence, which was adopted by the Continental Congress on July 4th, 1776.
''''
Question: Who painted the Mona Lisa?
Answer: The Mona Lisa was painted by the Italian artist Leonardo da Vinci in the early 16th century.
''''
Question: Who discovered the law of gravitation?
Answer: Sir Isaac Newton formulated the law of gravitation in 1687. He published his laws of motion and universal gravitation in the "Philosophiæ Naturalis Principia Mathematica"
''''
Question: Who wrote the Harry Potter series?
Answer: The Harry Potter series was written by British author J.K. Rowling.
''''
Question: Who discovered America?
Answer: The land that is now known as America was first discovered by the indigenous peoples who lived there long before the arrival of Europeans. Christopher Columbus, who was sponsored by the Catholic Monarchs of Spain, is often credited with the "discovery" of America in 1492, however, he was not the first European to reach America, nor was he the first to realize that it was a new continent.
''''
Question: Who is the current President of the United States?
Answer: As of my knowledge cut off date in 2021, the current President of the United States is Joe Biden.
''''
Question: Who discovered the smallpox vaccine?
Answer: The smallpox vaccine was discovered by Edward Jenner in 1796. He observed that milkmaids who had contracted cowpox, a similar but less deadly disease, did not contract smallpox. He hypothesized that cowpox protected against smallpox, and he successfully tested this by infecting a young boy with cowpox and then exposing him to smallpox.
''''
Question: Who was the first man to walk on the moon?
Answer: Neil Armstrong was the first man to walk on the moon on July 20, 1969, as part of the Apollo 11 mission.
''''
Question: Who invented the steam engine?
Answer: James Watt is credited with inventing the steam engine in the late 18th century. He made several improvements to the existing design, which made it more efficient and practical for use in industry.
''''
Question: Who wrote the novel "Pride and Prejudice"?
Answer: The novel "Pride and Prejudice" was written by the English author Jane Austen in 1813.
''''
Question: Who composed the opera "The Barber of Seville"?
Answer: The opera "The Barber of Seville" was composed by the Italian composer Gioachino Rossini in 1816.
''''
Question: Who was the first president of the United States?
Answer: George Washington was the first President of the United States, serving from 1789 to 1797.
''''
Question: Who discovered the structure of the atom?
Answer: The structure of the atom was discovered by several scientists throughout history, including John Dalton in the early 19th century, J.J. Thomson in the late 19th century, and Niels Bohr in the early 20th century.
''''
Question: Who discovered the polio vaccine?
Answer: The polio vaccine was developed by American physician and virologist Jonas Salk in the 1950s.
''''
Question: Who wrote the novel "The Great Gatsby"?
Answer: The novel "The Great Gatsby" was written by the American author F. Scott Fitzgerald in 1925.
''''
Question: Who composed the music for the opera "La Traviata"?
Answer: The opera "La Traviata" was composed by the Italian composer Giuseppe Verdi in 1853.
''''
Question: Who wrote the novel "To Kill a Mockingbird"?
Answer: The novel "To Kill a Mockingbird" was written by American author Harper Lee and published in 1960.
''''
Question: Who painted the painting "The Scream"?
Answer: The painting "The Scream" was painted by the Norwegian artist Edward Munch in the 1890s.
''''
Question: Who discovered the cause of yellow fever?
Answer: The cause of yellow fever was discovered by American physician Walter Reed and his team in the early 1900s, who identified the disease was transmitted by mosquitoes.
''''
Question: Who discovered the element Helium?
Answer: The element Helium was discovered by French astronomer Jules Janssen and British astronomer Joseph Norman Lockyer in 1868, independently of each other.
''''
Question: Who was the first woman to win the Nobel Prize?
Answer: The first woman to win the Nobel Prize was Marie Curie, who won the Physics Prize in 1903 and the Chemistry Prize in 1911.
''''
Question: Who was the first African American to win the Nobel Prize?
Answer: The first African American to win the Nobel Prize was Ralph Bunche, who won the Peace Prize in 1950.
''''
Question: What is the largest planet in the solar system?
Answer: The largest planet in the solar system is Jupiter.
''''
Question: What is the currency of Ireland?
Answer: The currency of Ireland is the Euro.
''''
Question: What is the capital of France?
Answer: The capital of France is Paris.
''''
Question: What is the highest mountain in the world?
Answer: The highest mountain in the world is Mount Everest, which is located in the Himalayas and stands at 29,029 feet (8,848 meters) above sea level.
''''
Question: What is the largest ocean in the world?
Answer: The largest ocean in the world is the Pacific Ocean.
''''
Question: How many planets are in the Solar System?
Answer: There are 8 planets in the Solar System.
''''
Question: What is the capital of China?
Answer: The capital of China is Beijing.
''''
Question: What is the largest animal on Earth?
Answer: The largest animal on Earth is the blue whale.
''''
Question: What is the longest river in the world?
Answer: The longest river in the world is the Nile River, which runs through Egypt and Sudan.
''''
Question: What is the capital of Australia?
Answer: The capital of Australia is Canberra.
''''
Question: What is the highest waterfall in the world?
Answer: The highest waterfall in the world is Angel Falls, which is located in Venezuela and stands at 3,212 feet (979 meters) tall.
''''
Question: What is the smallest country in the world by land area?
Answer: The smallest country in the world by land area is Vatican City, with an area of approximately 44 hectares.
''''
Question: What is the largest desert in the world?
Answer: The largest desert in the world is the Antarctic Desert.
''''
Question: What is the longest mountain range in the world?
Answer: The longest mountain range in the world is the Andes, which stretches for over 7,000 km (4,350 mi) through South America.
''''
Question: What is the capital of Brazil?
Answer: The capital of Brazil is Brasília.
''''
Question: What is the largest bird in the world?
Answer: The largest bird in the world is the ostrich.
''''
Question: What is the largest mammal in the world?
Answer: The largest mammal in the world is the blue whale.
''''
Question: What is the largest flower in the world?
Answer: The largest flower in the world is the Rafflesia arnoldii, also known as the "corpse flower".
''''
Question: What is the capital of Mexico?
Answer: The capital of Mexico is Mexico City.
''''
Question: What is the largest island in the world?
Answer: The largest island in the world is Greenland.
''''
Question: What is the tallest mammal in the world?
Answer: The tallest mammal in the world is the giraffe, which can grow up to 18 feet (5.5 meters) tall.
''''
Question: What is the largest volcano in the world?
Answer: The largest volcano in the world is Mauna Loa, which is located in Hawaii and is part of the Hawaiian-Emperor seamount chain.
''''
Question: What is the largest lake in the world by area?
Answer: The largest lake in the world by area is the Caspian Sea.
''''
Question: What is the capital of Russia?
Answer: The capital of Russia is Moscow.
''''
Question: What is the largest reptile in the world?
Answer: The largest reptile in the world is the saltwater crocodile.
''''
Question: What is the largest amphibian in the world?
Answer: The largest amphibian in the world is the Chinese giant salamander.
''''
Question: What is the largest fish in the world?
Answer: The largest fish in the world is the whale shark.
''''
Question: What is the largest insect in the world?
Answer: The largest insect in the world is the Goliath Beetle.
''''
Question: What is the capital of Canada?
Answer: The capital of Canada is Ottawa.
''''
Question: What is the largest mammal that can fly?
Answer: The largest mammal that can fly is the bat, specifically the Giant Golden-crowned Flying Fox.
''''
Question: What is the largest predator in the world?
Answer: The largest predator in the world is the Polar Bear
''''
Question: What is the largest city in the world by population?
Answer: The largest city in the world by population is Tokyo, Japan
''''
Question: What is the oldest university in the world?
Answer: The oldest university in the world is the University of Bologna, which was founded in 1088.
''''
Question: What is the largest country in the world by land area?
Answer: The largest country in the world by land area is Russia.
''''
Question: What is the largest freshwater lake in the world?
Answer: The largest freshwater lake in the world is Lake Superior.
''''
Question: What is the largest living organism in the world?
Answer: The largest living organism in the world is the Great Barrier Reef, which is an ecosystem of coral reefs.
''''
Question: What is the largest man-made structure in the world?
Answer: The largest man-made structure in the world is the Great Wall of China.
''''
Question: What is the largest mammal that lives in the ocean?
Answer: The largest mammal that lives in the ocean is the Blue Whale.
''''
Question: What is the largest country in the world by population?
Answer: The largest country in the world by population is China.
''''
Question: What is the largest mammal that lives on land?
Answer: The largest mammal that lives on land is the African Elephant
''''
Question: What is the largest delta in the world?
Answer: The largest delta in the world is the Ganges-Brahmaputra Delta.
''''
Question: What is the largest cave system in the world?
Answer: The largest cave system in the world is the Mammoth Cave System.
''''
Question: What is the largest artificial lake in the world?
Answer: The largest artificial lake in the world is Lake Kariba.
''''
Question: What is the largest island that belongs to Europe?
Answer: The largest island that belongs to Europe is Great Britain.
''''
Question: What is the largest glacier in the world?
Answer: The largest glacier in the world is the Lambert Glacier.
''''
Question: What is the largest flower in the world by diameter?
Answer: The largest flower in the world by diameter is the Rafflesia arnoldii.
''''
Question: What is the largest country in the world by GDP?
Answer: The largest country in the world by GDP is the United States.
''''
Question: What is the largest continent in the world?
Answer: The largest continent in the world is Asia.
''''
Question: What is the largest volcano in the world by volume?
Answer: The largest volcano in the world by volume is Mauna Loa.
''''
Question: What is the largest waterfall in the world by volume?
Answer: The largest waterfall in the world by volume is the Angel Falls.
''''
Question: What is the largest river in the world by discharge?
Answer: The largest river in the world by discharge is the Amazon River.
''''
Question: What is the largest desert in the world by area?
Answer: The largest desert in the world by area is the Antarctic Desert.
''''
Question: What is the largest jungle in the world?
Answer: The largest jungle in the world is the Amazon Rainforest.
''''
Question: What is the largest animal that has ever existed?
Answer: The largest animal that has ever existed is the Blue Whale.
''''
Question: What is the largest country in the world by area?
Answer: The largest country in the world by area is Russia.
''''
Question: What is the largest coral reef system in the world?
Answer: The largest coral reef system in the world is the Great Barrier Reef.
''''
Question: What is the largest island chain in the world?
Answer: The largest island chain in the world is the Malay Archipelago.
''''
Question: What is the largest lake in the world by volume?
Answer: The largest lake in the world by volume is Lake Baikal.
''''
Question: What is the largest country in the world by population density?
Answer: The largest country in the world by population density is Bangladesh.
''''
Question: What is the largest animal to ever walk the Earth?
Answer: The largest animal to ever walk the Earth is the Indricotherium, which was a giant mammal that lived during the Eocene epoch.
''''
Question: What is the largest country in South America by area?
Answer: The largest country in South America by area is Brazil.
''''
Question: What is the largest city in Africa by population?
Answer: The largest city in Africa by population is Lagos, Nigeria.
''''
Question: What is the largest country in Europe by area?
Answer: The largest country in Europe by area is Russia.
''''
Question: What is the largest city in North America by population?
Answer: The largest city in North America by population is Mexico City, Mexico.
''''
Question: What is the largest country in Oceania by area?
Answer: The largest country in Oceania by area is Australia.
''''
Question: What is the largest city in Asia by population?
Answer: The largest city in Asia by population is Tokyo, Japan.
''''
Question: What is the largest country in the world by coastline?
Answer: The largest country in the world by coastline is Canada.
''''
Question: What is the largest city in the world by urban area?
Answer: The largest city in the world by urban area is Tokyo, Japan.
''''
Question: What is the largest desert in Africa by area?
Answer: The largest desert in Africa by area is the Sahara Desert.
''''
Question: What is the largest country in the world by forest area?
Answer: The largest country in the world by forest area is Russia.
''''
Question: What is the largest country in the world by total renewable water resources?
Answer: The largest country in the world by total renewable water resources is Brazil.
''''
Question: What is the largest country in the world by total area of protected land?
Answer: The largest country in the world by total area of protected land is Russia.
''''
Question: What is the largest country in the world by total renewable energy production?
Answer: The largest country in the world by total renewable energy production is China.
''''
Question: What is the largest country in the world by total number of airports?
Answer: The largest country in the world by total number of airports is the United States.
''''
Question: What is the largest country in the world by total length of highways?
Answer: The largest country in the world by total length of highways is the United States.
''''
Question: What is the largest country in the world by total number of universities?
Answer: The largest country in the world by total number of universities is China.
''''
Question: What is the largest country in the world by total number of tourist arrivals?
Answer: The largest country in the world by total number of tourist arrivals is France.
''''
Question: What is the largest country in the world by total GDP per capita?
Answer: The largest country in the world by total GDP per capita is Luxembourg.
''''
Question: What is the largest country in the world by total number of Internet users?
Answer: The largest country in the world by total number of Internet users is China.
''''
Question: What is the largest country in the world by total number of mobile phone users?
Answer: The largest country in the world by total number of mobile phone users is China.
''''
Question: What is the largest country in the world by total number of airports?
Answer: The largest country in the world by total number of airports is the United States.
''''
Question: How many states are there in the United States?
Answer: There are 50 states in the United States.
''''
Question: How does the human heart pump blood?
Answer: The human heart pumps blood through a series of coordinated contractions of the atria and ventricles. The atria contract first, pushing blood into the ventricles, then the ventricles contract, pushing blood out of the heart and into the arteries.
''''
Question: How do plants make food?
Answer: Plants make food through a process called photosynthesis, which converts light energy from the sun into chemical energy stored in glucose and other sugars. Carbon dioxide and water are taken in by the plant and with the help of chlorophyll, the light energy is used to convert these substances into glucose and oxygen is released as a by-product.
''''
Question: How do earthquakes occur?
Answer: Earthquakes occur due to the movement of tectonic plates. The Earth's crust is made up of several large tectonic plates that move and interact with one another. When these plates suddenly shift, it causes the release of energy in the form of seismic waves, resulting in an earthquake.
''''
Question: How do tornadoes form?
Answer: Tornadoes form when warm, moist air collides with cold, dry air. This causes the warm air to rise rapidly and create a rotating column of air. As the column of air continues to rotate and gain strength, it can develop into a tornado.
''''
Question: How do volcanoes erupt?
Answer: Volcanoes erupt when pressure from molten rock, ash, and gas inside the volcano builds up and eventually forces its way to the surface. This can happen through a volcano's central vent or through fissures on its slopes.
''''
Question: How do airplanes fly?
Answer: Airplanes fly through the principles of lift, weight, thrust, and drag. Lift is the upward force that opposes the weight of the airplane and allow it to take off and remain in the air. thrust is the force that propels the airplane forward, and drag is the force that opposes the thrust and slows the airplane down.
''''
Question: How do computers work?
Answer: Computers work by processing data through a series of instructions called software. These instructions are executed by the computer's central processing unit (CPU) using binary code (1s and 0s) to perform tasks such as arithmetic calculations, logical operations, and data storage.
''''
Question: How do batteries work?
Answer: Batteries work by converting chemical energy into electrical energy. Inside a battery, there are two electrodes, a positive electrode (anode) and a negative electrode (cathode), separated by an electrolyte. When a circuit is connected to the battery, electrons flow from the anode to the cathode, creating an electrical current.
''''
Question: How do plants adapt to different environments?
Answer: Plants adapt to different environments through a variety of mechanisms. Some examples include developing deep roots to access water in dry regions, growing smaller leaves to reduce water loss in hot regions, or producing chemicals to deter herbivores in regions with high herbivore populations.
''''
Question: How do animals adapt to different environments?
Answer: Animals adapt to different environments through a variety of mechanisms such as camouflage, migration, hibernation, and behavioral changes. Some examples include polar bears growing thick fur to survive in cold climates, desert animals developing the ability to conserve water, or birds developing migratory patterns to find food in different seasons.
''''
Question: How many states are there in the United States?
Answer: There are 50 states in the United States.
''''
Question: How many elements are in the periodic table?
Answer: There are currently 118 known elements in the periodic table.
''''
Question: How many players are on a standard soccer team?
Answer: A standard soccer team has 11 players.
''''
Question: How many oceans are there in the world?
Answer: There are five oceans in the world: the Atlantic, Pacific, Indian, Arctic, and Southern Ocean.
''''
Question: How many bones are there in the human body?
Answer: There are 206 bones in the human body.
''''
Question: How many planets are visible to the naked eye?
Answer: Five planets are visible to the naked eye: Mercury, Venus, Mars, Jupiter, and Saturn.
''''
Question: How many months are there in a year?
Answer: There are 12 months in a year.
''''
Question: How much does the average human brain weigh?
Answer: The average human brain weighs about 3 pounds (1.4 kg).
''''
Question: How much time does it take for light to travel from the sun to the earth?
Answer: It takes about 8 minutes and 20 seconds for light to travel from the sun to the earth.
''''
Question: How much money is needed to be considered a millionaire?
Answer: To be considered a millionaire, one would need to have net assets of at least one million dollars.
''''
Question: How much does a gallon of gasoline weigh?
Answer: A gallon of gasoline weighs about 6.3 pounds (2.9 kg).
''''
Question: Why the sky is blue?
Answer: The sky appears blue because of a phenomenon known as Rayleigh scattering. This occurs when light from the sun is scattered in all directions by the gases and tiny particles in the Earth's atmosphere. Blue light has a shorter wavelength and is scattered more easily than other colors, making it appear more present in the sky and giving it a blue color.
''''
Question: Why is the ocean salty?
Answer: The ocean is salty because it contains dissolved salts, primarily sodium chloride (NaCl). These salts come from various sources, including the weathering of rocks on land and the erosion of mineral deposits. They are then carried to the ocean by rivers and streams and eventually become part of the seawater. Over time, the ocean has become increasingly salty as it continues to receive more salt than it loses through evaporation.
''''
Question: Why is the Earth round?
Answer: The Earth is round due to the force of gravity. The Earth is a sphere because gravity pulls matter towards the center of the planet, causing it to take on a rounded shape. This is known as the hydrostatic equilibrium, where the gravity pulls down the material of the planet, but the planet's rotation causes it to bulge out at the equator and flatten at the poles.
''''
Question: Why do we have seasons?
Answer: Seasons are caused by the tilt of the Earth's axis. The Earth's axis is tilted at an angle of about 23.5 degrees relative to its orbit around the sun. As the Earth orbits the sun, different parts of the planet receive different amounts of sunlight depending on the season. This causes the temperature and weather patterns to change, resulting in the four seasons: spring, summer, fall, and winter.
''''
Question: Why do leaves change color in the fall?
Answer: Leaves change color in the fall because of changes in the levels of pigments in the leaves. During the spring and summer, leaves contain chlorophyll, which gives them their green color. As the days shorten in the fall, the chlorophyll breaks down, revealing other pigments such as carotenoids and anthocyanins. These pigments give leaves their yellow, orange, and red colors.
''''
Question: Why do we have day and night?
Answer: We have day and night due to the rotation of the Earth on its axis. The Earth rotates, or spins, on an imaginary line that runs through the North and South Poles. This rotation causes different parts of the Earth to face the sun at different times, creating day and night. The side of the Earth facing the sun experiences daylight, while the side facing away from the sun experiences darkness.
''''
Question: Why is the Great Wall of China visible from space?
Answer: The Great Wall of China is visible from space because of its size and the materials used to construct it. The Great Wall is the longest wall in the world, stretching over 13,000 miles. It was constructed using materials such as brick, tamped earth, stone, and wood, which are much more durable and long-lasting than the surrounding natural materials. This makes it stand out as a man-made structure when viewed from space.
''''
Question: Why is the sunset red?
Answer: The sunset is red due to a phenomenon known as Rayleigh scattering. During sunset, the sun's light has to pass through more of the Earth's atmosphere, which scatters the shorter-wavelength blue and green light. This leaves the longer-wavelength red light, which is why the sun appears red during sunset.
''''
Question: Why do volcanoes erupt?
Answer: Volcanoes erupt because of the movement of molten rock, ash, and gas beneath the Earth's surface. Volcanoes are formed when magma, or molten rock, rises to the surface and erupts. The eruption is caused by the pressure of the gas and ash inside the volcano building up until it can no longer be contained.
''''
Question: Why is the atmosphere important for life on Earth?
Answer: The atmosphere is important for life on Earth because it provides the necessary conditions for life to exist. The atmosphere protects the planet from harmful solar radiation, regulates temperature, and provides the necessary gases for living organisms to breathe. Without the atmosphere, the Earth would be uninhabitable for most forms of life.
''''
Question: Why do we have tides?
Answer: Tides are caused by the gravitational pull of the Moon and the Sun on the Earth's oceans. The gravitational force of the Moon and the Sun creates a bulge in the ocean on the side closest to them, and a corresponding dip on the opposite side. This causes the rise and fall of the ocean's surface, creating tides.
''''
Question: Why is the Arctic region so cold?
Answer: The Arctic region is so cold because of its location near the Earth's poles. The poles receive less direct sunlight than the equator, causing the temperatures to be much colder. Additionally, the Arctic is covered by ice and snow, which reflects sunlight and further reduces temperatures.
''''
Question: Why is the sky black at night?
Answer: The sky is black at night because of the absence of sunlight. During the day, sunlight reflects off the atmosphere and illuminates the sky, making it appear blue. At night, when the sun is below the horizon, the sky is not illuminated by sunlight and appears black.
''''
Question: Why do plants need sunlight?
Answer: Plants need sunlight to perform photosynthesis, a process in which they convert sunlight, carbon dioxide, and water into energy and oxygen. Photosynthesis is essential for the growth and survival of plants as it provides them with the energy they need to carry out life processes.
''''
Question: Why do we have different time zones?
Answer: Different time zones are necessary to ensure that all locations on Earth have approximately the same amount of daylight during a 24-hour period. Since the Earth is spherical, the amount of daylight varies depending on the location, and to keep the same time for all would mean that some places would have too much daylight and others would have too little.
''''
Question: Why do we have different climates?
Answer: Different climates exist because of variations in the Earth's surface and atmosphere. Factors such as latitude, altitude, and proximity to bodies of water all affect the climate of an area. Additionally, the Earth's rotation and the tilt of its axis also contribute to the variation in climates.
''''
Question: Why is the ocean blue?
Answer: The ocean appears blue because water absorbs colors in the red part of the light spectrum and reflects colors in the blue part of the spectrum. This is due to the properties of water molecules, which scatter light differently depending on its wavelength.
''''
Question: Why do we have different seasons?
Answer: Seasons occur due to the tilt of the Earth's axis in relation to its orbit around the sun. When the Earth is tilted towards the sun, it experiences summer, and when it is tilted away from the sun, it experiences winter. The change in the angle of the sun's rays and the duration of daylight hours causes the variation in seasons.
''''
Question: Why is the Earth's temperature changing?
Answer: The Earth's temperature is changing due to human activities that release greenhouse gases, such as carbon dioxide and methane, into the atmosphere. These gases trap heat from the sun, causing the Earth's temperature to rise, leading to global warming.
''''
Question: Why do some animals hibernate?
Answer: Some animals hibernate as a survival strategy to conserve energy during the winter when food is scarce. During hibernation, their body temperature, metabolism, and heart rate slow down significantly, allowing them to survive on stored energy until conditions improve.
''''
Question: Why do we have different types of soil?
Answer: Different types of soil exist due to variations in climate, topography, and the types of rock and minerals present in a given area. The weathering and erosion of these rocks and minerals, along with organic matter and living organisms, all contribute to the formation of different types of soil.
''''
Question: Why do we have different types of natural disasters?
Answer: Different types of natural disasters occur due to various geophysical and meteorological processes. For example, earthquakes happen due to the movement of tectonic plates, hurricanes happen due to the formation of low-pressure systems over warm ocean waters, and wildfires happen due to dry conditions and strong winds.
''''
Question: Why is the ozone layer important?
Answer: The ozone layer is important because it protects the Earth from harmful ultraviolet radiation from the sun. Ozone molecules absorb UV radiation, preventing it from reaching the Earth's surface and causing damage to living organisms. Without the ozone layer, the Earth would be uninhabitable for most forms of life.
''''
Question: Why do we have different types of clouds?
Answer: Different types of clouds form due to variations in temperature, humidity, and altitude. For example, cumulus clouds form when warm, moist air rises and cools, while cirrus clouds form at high altitudes where the air is cold and dry. The different types of clouds are indicative of different weather patterns.
''''
Question: Why do some animals have camouflage?
Answer: Some animals have camouflage to blend in with their surroundings and avoid predators. This helps them to survive by making it more difficult for predators to spot them. Camouflage also allows them to sneak up on prey and hunt more effectively.
''''
Question: Why are some animals endangered?
Answer: Some animals are endangered due to human activities such as habitat destruction, hunting, and pollution. As human populations continue to grow and expand, wild animals are losing their natural habitats and being forced to compete for resources. Additionally, hunting and poaching for animal parts and illegal wildlife trade also contributes to the decline of certain species.
''''
Question: Why do some animals have bright colors?
Answer: Some animals have bright colors for a variety of reasons. Some use them for communication, to attract a mate, or to warn predators that they are toxic or dangerous. Additionally, bright colors can also serve as camouflage, helping them to blend in with their surroundings and avoid predators.
''''
Question: Why do some animals have venom?
Answer: Some animals have venom as a defense mechanism to protect themselves from predators or to subdue their prey. Venom can be used to incapacitate, kill or deter predators, or to aid in capturing and digesting prey.
''''
Question: Why do we have different types of rocks?
Answer: Different types of rocks form due to various geological processes such as heat and pressure, erosion, and the weathering of existing rock. The composition, texture, and structure of the rock are all factors that determine the type of rock.
''''
Question: Why is the Gulf Stream important?
Answer: The Gulf Stream is an ocean current that carries warm water from the Gulf of Mexico up to the Atlantic coast of North America, then across the Atlantic to Western Europe. This current has a significant impact on the climate in these regions, making it warmer and milder than it would be otherwise.
''''
Question: Why do we have different types of forests?
Answer: Different types of forests exist due to variations in climate, soil, and altitude. Temperate forests, for example, are found in regions with moderate temperatures and rainfall, while tropical rainforests are found in regions with high temperatures and rainfall. Additionally, the types of trees and other vegetation found in a given forest can also determine the type of forest.
''''
Question: Why do we have different types of ecosystems?
Answer: Different types of ecosystems exist due to variations in climate, geology, and the types of plants and animals present in a given area. For example, a desert ecosystem is characterized by little rainfall and high temperatures, while a rainforest ecosystem is characterized by high rainfall and a wide variety of plant and animal life.
''''
Question: Why do some animals have a symbiotic relationship?
Answer: Some animals have a symbiotic relationship because it benefits both parties involved. For example, bees and flowers have a symbiotic relationship where bees gather nectar from the flowers, and in return, the bees help to pollinate the flowers. Similarly, clownfish and sea anemones have a symbiotic relationship where the clownfish lives among the tentacles of the sea anemone for protection and in return, the clownfish provides food for the sea anemone.
''''
Question: Why do we have different types of weather patterns?
Answer: Different types of weather patterns occur due to variations in temperature, humidity, and atmospheric pressure. For example, a high-pressure system is associated with clear, sunny weather, while a low-pressure system is associated with stormy weather. Additionally, the Earth's rotation and the tilt of its axis also contribute to the formation of different weather patterns.
''''
Question: 4+93
Answer: The sum of 4 and 93 is 97.
''''
Question: 3-5
Answer: The difference of 3 and 5 is -2.
''''
Question: 10x10
Answer: The product of 10 and 10 is 100.
''''
Question: 49-4
Answer: The difference of 49 and 4 is 45.
''''
Question: 12/3
Answer: The result of 12 divided by 3 is 4.
''''
Question: Why we are made of stardust?
Answer: The elements that make up our bodies, such as carbon, nitrogen, and oxygen, were formed in stars through nuclear fusion. When stars die, they explode and send these elements into space, where they can eventually come together to form new stars and planets. This process is known as stellar nucleosynthesis. So, we are made of stardust because the elements that make up our bodies were formed in stars and then were spread throughout the universe through supernovae.
''''
Question: How do stars work?
Answer: Stars work through a process called nuclear fusion. Nuclear fusion is the process of combining atomic nuclei to form a heavier nucleus, releasing a tremendous amount of energy in the process. In stars, this process primarily occurs in the core, where the temperatures and pressures are high enough to overcome the electrostatic repulsion of the positively charged nuclei. Hydrogen nuclei, which are the most abundant element in the universe, fuse together to form helium. This process releases a large amount of energy in the form of light and heat, which causes the star to shine. The energy also generates pressure that supports the star against the force of gravity. This process continues as long as there is fuel available, and once the fuel is exhausted, the star will die.
''''
Question: What is the formula for water?
Answer: The chemical formula for water is H2O, which means it is composed of two hydrogen atoms and one oxygen atom.
''''
Question: What is photosynthesis?
Answer: Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy in the form of glucose (a sugar). This process occurs in the chloroplasts of the cells and involves the conversion of carbon dioxide and water into glucose and oxygen. The oxygen is released into the air as a by-product of photosynthesis, while the glucose is used by the plant for energy and as a building block for other molecules. Photosynthesis is a crucial process for life on Earth, as it provides the energy source for almost all living organisms and helps to regulate the levels of carbon dioxide and oxygen in the atmosphere.
''''
Question: Who wrote the novel "To Kill a Mockingbird"?
Answer: The novel "To Kill a Mockingbird" was written by Harper Lee.
''''
Question: Who invented the telephone?
Answer: Alexander Graham Bell is credited with inventing the telephone.
''''
Question: Why is it so hard to predict earthquakes?
Answer: It's difficult to predict earthquakes because they are complex natural phenomena that occur deep within the Earth's crust. There are many factors that can influence an earthquake, including the type of fault, the level of stress on the fault, and the surrounding geological conditions. \nDespite advances in technology and the study of earthquakes, predicting when and where an earthquake will occur is still a major challenge for seismologists. This is because earthquakes are not regular, predictable events like the tides or the sunrise. They are instead driven by complex, unpredictable processes that are not fully understood. \nAdditionally, the tools and methods used to study earthquakes are limited by our current technology. Seismographs, for example, can detect earthquakes after they have happened, but they do not provide enough information to accurately predict when and where an earthquake will occur. \nIn conclusion, predicting earthquakes is challenging because they are complex and poorly understood natural phenomena that occur deep within the Earth's crust. Despite ongoing efforts by scientists and researchers, the prediction of earthquakes remains an area of active research and a major challenge.
''''
Question: Is the sun on fire?
Answer: No, the sun is not on fire in the traditional sense. The sun is a massive ball of hot plasma that gives off light and heat due to nuclear reactions taking place in its core. These reactions convert hydrogen into helium and release a tremendous amount of energy in the process. This energy is what makes the sun shine, but it's not burning in the way that a fire burns on Earth. Instead, the sun is undergoing nuclear fusion, which is a completely different process.
''''
Question: What is the study of living organisms and their interactions with each other and their environment?
Answer: The study of living organisms and their interactions with each other and their environment is called Ecology. It is a branch of biology that deals with the relationships between organisms and their biotic and abiotic environments. This includes the distribution and abundance of species, the dynamics of populations, the exchange of energy and matter within and between ecosystems, and the impact of human activities on the natural world.
''''
Question: What is ecology?
Answer: Ecology is a scientific discipline concerned with the study of the interactions of living organisms with each other and with their non-living environment. It encompasses the study of the distribution and abundance of organisms, their physiological and behavioral adaptations, and the flow of energy and materials through ecosystems. The field of ecology seeks to understand how ecosystems function and how they are affected by changes in the environment, such as climate change, deforestation, pollution, and the introduction of non-native species. Ultimately, the goal of ecology is to help inform decision-making in order to promote the sustainable use of natural resources and the preservation of biodiversity.
''''
Question: What is the speed of light?
Answer: The speed of light in a vacuum is approximately 299,792,458 meters per second (m/s). It is considered as the highest speed limit in the universe, and nothing can exceed or travel faster than the speed of light.
"""



# split the text into lines
lines = text.split("""
''''
""")

# remove leading/trailing whitespace from each line
lines = [line.strip() for line in lines]

# remove empty lines
lines = [line for line in lines if line != ""]

# create a new list to store the csv data
csv_lines = []

def replace_double_quotes(text):
    return text.replace('"', '""')

# iterate over the lines of the original text
for line in lines:
    # use regular expressions to extract the question and answer
    match = re.match("Question: (.*)\nAnswer: (.*)", line)
    if match:
        question, answer = match.groups()
        answer = replace_double_quotes(answer)
        # add the question and answer to the csv_lines list
        csv_lines.append(f"{question},\"{answer}\"")

# create the csv data string
csv_data = "Question, Answer\n" + "\n".join(csv_lines)

# print the csv data
print(csv_data)

with open("questioning.csv", "w") as f:
    f.write(csv_data)