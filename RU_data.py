# source: Wikipedia

# List of regions of Russian federation
regions = ['Adygea', 'Altai Krai', 'Altai Republic', 'Amur Oblast',
       'Arkhangelsk Oblast', 'Astrakhan Oblast', 'Bashkorstan',
       'Belgorod Oblast', 'Bryansk Oblast', 'Buryatia', 'Chechnya',
       'Chelyabinsk Oblast', 'Chukotka', 'Chuvashia', 'Dagestan',
       'Ingushetia', 'Irkutsk Oblast ', 'Ivanovo Oblast',
       'Jewish Autonomous Oblast', 'Kabardino-Balkaria',
       'Kaliningrad Oblast', 'Kalmykia', 'Kaluga Oblast',
       'Kamchatka Krai', 'Karachay-Cherkessia', 'Karelia',
       'Kemerovo Oblast', 'Khabarovsk Krai', 'Khakassia',
       'Khanty-Mansi Autonomous Okrug', 'Kirov Oblast', 'Kostroma Oblast',
       'Kranodar Krai', 'Krasnoyarsk Krai', 'Kurgan Oblast',
       'Kursk Oblast', 'Leningrad Oblast', 'Lipetsk Oblast',
       'Magadan Oblast', 'Mari El', 'Mordovia', 'Moscow', 'Moscow Oblast',
       'Murmansk Oblast', 'Nenets Autonomous Okrug',
       'Nizhny Novgorod Oblast', 'North Ossetia-Alania',
       'Novgorod Oblast', 'Novosibirsk Oblast', 'Omsk Oblast',
       'Orenburg Oblast', 'Oryol Oblast', 'Penza Oblast', 'Perm Krai',
       'Primorsky Krai', 'Pskov Oblast', 'Rostov Oblast', 'Ryazan Oblast',
       'Saint Petersburg', 'Sakha', 'Sakhalin Oblast', 'Samara Oblast',
       'Saratov Oblast', 'Smolensk Oblast', 'Stavropol Krai',
       'Sverdlovsk Oblast', 'Tambov Oblast', 'Tatarstan', 'Tomsk Oblast',
       'Tula Oblast', 'Tuva', 'Tver Oblast', 'Tymen Oblast', 'Udmurtia',
       'Ulyanovsk Oblast', 'Vladimir Oblast', 'Volgograd Oblast',
       'Vologda Oblast', 'Voronezh Oblast',
       'Yamalo-Nenets Autonomous Okrug', 'Yaroslavl Oblast',
       'Zabaykalsky Krai', 'Komi Republic', 'Crimea Republic', 'Sevastopol']

# Colors in dependency of economic region of Russia
""" Colors of regions:
    red - Central 
    yellow - Ural
    green - North Caucasus 
    blue - Volga
    purple - West Siberian
    turquoise - East Siberian
    orange - Volga-Vyatka
    orchid - Northwestern
    olive - Central Black Earth
    coral - Far Eastern
    gray - Northern
    navy - Kaliningrad"""
col = ['turquoise', 'gray', 'gray', 'blue','purple', 'orchid', 'olive','yellow', 'red', 
       'green', 'turquoise','olive', 'blue', 'coral', 'turquoise','turquoise', 'green', 
       'red','blue', 'turquoise', 'navy', 'orchid', 'red','blue', 'turquoise', 'purple',
       'gray', 'blue', 'green','gray', 'coral', 'red','turquoise', 'green', 'olive',
       'yellow', 'orange', 'yellow','blue', 'coral', 'coral', 'red', 'red','purple', 
       'purple', 'coral', 'turquoise','orange', 'gray', 'gray','olive', 'red', 'orchid', 
       'olive','blue', 'orange', 'turquoise', 'red', 'orange', 'blue', 'blue', 'orchid',
       'orchid', 'red', 'turquoise','olive', 'yellow', 'orchid', 'gray','red', 'green', 
       'red', 'gray', 'olive','orchid', 'red', 'orchid','purple', 'yellow','gray', 'red',
       'green', 'purple','turquoise', 'turquoise']

# Life expectancy for regions of Russia (2016)
life_exp = [73.25, 71.1 , 71.15, 69.06, 71.94, 73.35, 71.73, 73.67, 71.27,
       70.69, 74.84, 71.53, 66.1 , 72.73, 77.79, 81.59, 69.19, 71.47,
       68.83, 75.81, 72.62, 73.54, 71.87, 70.06, 75.94, 70.65, 69.35,
       69.74, 70.21, 73.87, 72.72, 71.81, 73.42, 70.61, 70.8 , 71.74,
       72.54, 72.46, 69.37, 72.24, 73.4 , 77.87, 73.34, 71.67, 71.52,
       71.88, 75.51, 69.68, 71.57, 71.49, 70.94, 71.63, 73.34, 70.79,
       70.36, 69.95, 73.03, 72.7 , 75.45, 71.68, 70.19, 71.73, 72.88,
       71.14, 74.19, 71.23, 73.21, 74.2 , 72.02, 71.18, 66.29, 70.45,
       72.06, 72.06, 72.34, 71.27, 73.54, 71.26, 73.03, 73.53, 71.85,
       68.33, 69.4, 69.35, 70.67]

# GDP per capita for regions of Russia (2016)
gdp_cap = [ 201.9,  210.4,  213.5,  357.8,  380. ,  332.4,  330.4,  470.9,
        233.7,  202.6,  118.7,  360. , 1323.2,  211.6,  197.1,  106.8,
        443.3,  175. ,  283.8,  153.7,  390.4,  201.4,  368.9,  628.1,
        156.6,  371.5,  316.3,  478. ,  339.6, 1852.3,  224.8,  247.3,
        363.7,  615.8,  226. ,  325.1,  511.8,  406.7, 1006.6,  234.2,
        245.2, 1157.4,  483.7,  560.4, 5821.6,  363.3,  178.4,  398.1,
        391.4,  316.8,  387.6,  282.5,  251.7,  414.4,  382.6,  224.2,
        300.2,  298.6,  712.3,  903.6, 1575.6,  397.9,  263.8,  274.4,
        232.6,  456.9,  297.9,  499.8,  451.8,  344.5,  164.7,  276.3,
        632.2,  356. ,  261.5,  281.4,  292.6,  410. ,  360.4, 3670.3,
        369.5,  243.1, 640.6, 165.4, 151.9]

# Population of regions of Russia (2016)
pop = [  453052,  2350361,   218039,   798003,  1154856,  1017052,
        4063676,  1550026,  1210912,   984870,  1435733,  3492740,
          48895,  1230479,  3064394,   487836,  2403643,  1014620,
         162099,      865,   994708,   275390,  1011069,    31442,
         466056,   622433,  2695028,  1327670,   537404,  1654942,
        1283400,   643330,  5600893,  2876360,   845597,  1116021,
        1813677,  1150630,   144375,   682202,   803726, 12500123,
        7504339,   753226,    44058,  3234676,   701940,   606305,
        2789095,  1959622,  1977445,   747034,  1331621,  2623155,
        1912118,   636240,  4219732,  1121316,  5356755,   964252,
         490595,  3193189,  2463223,   949250,  2799951,  4325318,
        1034269,  3893756,  1077896,  1492018,   321597,  1283754,
        3691802,  1513288,  1246289,  1378528,  2520516,  1176678,
        2345520,   538026,  1265247,  1072579, 850554, 1913731, 436670]