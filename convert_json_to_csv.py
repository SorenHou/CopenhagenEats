import json
import csv

json_data = '''{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    12.5404997000001,
                    55.6980997
                ],
                "type": "Point"
            },
            "properties": {
                "description": "God til hverdag og fest. Flaskeøl til billigt.",
                "name": "Friheden"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5550487,
                    55.6900892
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Friteret fisk både med og uden brød om.",
                "name": "Hooked"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.558344,
                    55.669569
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Friteret fisk både med og uden brød om.",
                "name": "Hooked"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5508952,
                    55.6931655
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Bedste durum i københavn og det er ikke noget jeg vil diskutere.",
                "name": "Dürüm Symfoni"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5552316000001,
                    55.6933884
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Småretter og lækker vermut. Der er mulighed for at sidde ude under varmelamper.",
                "name": "Paloma Vermut Café"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5572055,
                    55.6867464
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Ranee's",
                "name": "Ranee's"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5553408000001,
                    55.6905635
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Vin til 60 kr glasset og gode småretter.",
                "name": "Pompette"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5543712,
                    55.690208
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Yellow",
                "name": "Yellow"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5734348,
                    55.6770539
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Masser af dim sum og andre kinesiske retter. Hvis du er sent på den har de en madbar der er åbent til 2 under restauranten.",
                "name": "Hidden Dimsum"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5563619,
                    55.6960624
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Vin til gode priser og et par småretter.",
                "name": "Sabotøren"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5454322000001,
                    55.675355
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Hart Bageri",
                "name": "Hart Bageri"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5624041999999,
                    55.6761894
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Gasoline Grill",
                "name": "Gasoline Grill"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.585048,
                    55.683268
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Gasoline Grill",
                "name": "Gasoline Grill"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.558616,
                    55.6689392
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Tacos!",
                "name": "Hija de Sanchez"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5692127,
                    55.6836823
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Tacos!",
                "name": "Hija de Sanchez"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5672079999999,
                    55.685126
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Slurp Ramen Joint",
                "name": "Slurp Ramen Joint"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5773811,
                    55.679563
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Gasoline Grill",
                "name": "Gasoline Grill"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5876515,
                    55.6835807
                ],
                "type": "Point"
            },
            "properties": {
                "description": "District Tonkin",
                "name": "District Tonkin"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5705545000001,
                    55.6768322
                ],
                "type": "Point"
            },
            "properties": {
                "description": "District Tonkin",
                "name": "District Tonkin"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5280299,
                    55.703699
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Fovl",
                "name": "Fovl"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5599406,
                    55.6696918
                ],
                "type": "Point"
            },
            "properties": {
                "description": "H15 Cafeteria & Bar",
                "name": "H15 Cafeteria & Bar"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5580571,
                    55.6682649
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Tommi's Burger Joint",
                "name": "Tommi's Burger Joint"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5596625000001,
                    55.6878438
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Sasaa",
                "name": "Sasaa"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.6133806,
                    55.6900454
                ],
                "type": "Point"
            },
            "properties": {
                "description": "lille bakery",
                "name": "lille bakery"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.543221,
                    55.696155
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Bar Pasta Vedbækgade",
                "name": "Bar Pasta Vedbækgade"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.548185,
                    55.694375
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Tommi’s Burger Joint Nørrebro",
                "name": "Tommi’s Burger Joint Nørrebro"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5596066,
                    55.6729984
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Smagsløget",
                "name": "Smagsløget"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5967894,
                    55.6778609
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Will at the Bridge",
                "name": "Will at the Bridge"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5971418,
                    55.6777963
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Gasoline Grill",
                "name": "Gasoline Grill"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5658058,
                    55.6738059
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Chicks by Chicks",
                "name": "Chicks by Chicks"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.55885,
                    55.66897
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Kødbyens Fiskeslagter",
                "name": "Kødbyens Fiskeslagter"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5511801,
                    55.6741444
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Rouge Oysters",
                "name": "Rouge Oysters"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5492642,
                    55.6871298
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Maobao.",
                "name": "Maobao."
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5477405,
                    55.6872983
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Baka d'busk",
                "name": "Baka d'busk"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5491733,
                    55.6869172
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Depanneur",
                "name": "Depanneur"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5613188,
                    55.671337
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Bento Copenhagen",
                "name": "Bento Copenhagen"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5627552,
                    55.6716827
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Fu Hao",
                "name": "Fu Hao"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5629186,
                    55.680421
                ],
                "type": "Point"
            },
            "properties": {
                "description": "H table",
                "name": "H table"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5691319,
                    55.6837178
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Omegn & Venner",
                "name": "Omegn & Venner"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5551636,
                    55.6904494
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Poulette",
                "name": "Poulette"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5602155,
                    55.6706293
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Baan Thai Isarn",
                "name": "Baan Thai Isarn"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.541407,
                    55.6926932
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Tilda og Karl",
                "name": "Tilda og Karl"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5588577,
                    55.6670468
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Magasasa Dim Sum & Cocktails",
                "name": "Magasasa Dim Sum & Cocktails"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5736239,
                    55.697323
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Captain H Chinese BBQ & Korean Bistro",
                "name": "Captain H Chinese BBQ & Korean Bistro"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5533284,
                    55.6736492
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Miga Restaurant",
                "name": "Miga Restaurant"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5625627,
                    55.6744105
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Propaganda Kitchen & Wine",
                "name": "Propaganda Kitchen & Wine"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5510772,
                    55.7012312
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Casamadre",
                "name": "Casamadre"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5499553,
                    55.7034712
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Oberra",
                "name": "Oberra"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5485459,
                    55.7035213
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Et Cetera",
                "name": "Et Cetera"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.558026,
                    55.686169
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Diamond Slice",
                "name": "Diamond Slice"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5609516,
                    55.6938686
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Bredo",
                "name": "Bredo"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5607919,
                    55.6891844
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Villette",
                "name": "Villette"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.544143,
                    55.6960248
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Andra",
                "name": "Andra"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5439781,
                    55.6983263
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Dzidra",
                "name": "Dzidra"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5550536000001,
                    55.6698114
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Sanchez",
                "name": "Sanchez"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5962010000001,
                    55.677933
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Barr",
                "name": "Restaurant Barr"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.55625,
                    55.695877
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Omar",
                "name": "Restaurant Omar"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5523111,
                    55.6922936
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Gaarden & Gaden",
                "name": "Gaarden & Gaden"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5559149000001,
                    55.6922215
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Bæst",
                "name": "Bæst"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5561422000001,
                    55.6920921
                ],
                "type": "Point"
            },
            "properties": {
                "description": "BRUS",
                "name": "BRUS"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5562342000001,
                    55.6924342
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Mirabelle",
                "name": "Mirabelle"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.564654,
                    55.6765719
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Uformel",
                "name": "Uformel"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.6110705999999,
                    55.6894112
                ],
                "type": "Point"
            },
            "properties": {
                "description": "La Banchina",
                "name": "La Banchina"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.589218,
                    55.6778716
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant ILUKA",
                "name": "Restaurant ILUKA"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5851983,
                    55.683458
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Pluto",
                "name": "Pluto"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5843265999999,
                    55.6725402
                ],
                "type": "Point"
            },
            "properties": {
                "description": "No.2",
                "name": "No.2"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5872932,
                    55.6744944
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Kulturtårnet",
                "name": "Kulturtårnet"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5820928000001,
                    55.6776153
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Admiralgade 26",
                "name": "Admiralgade 26"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5864357,
                    55.6813628
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Geist",
                "name": "Geist"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5924081000001,
                    55.6786597
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Den Vandrette",
                "name": "Den Vandrette"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5816045,
                    55.6773037
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Ved Stranden",
                "name": "Ved Stranden"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5557647000001,
                    55.6898972
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Cicchetti",
                "name": "Cicchetti"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5666955,
                    55.6920247
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Tigermom",
                "name": "Tigermom"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5769849000001,
                    55.6772908
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Marv & Ben",
                "name": "Restaurant Marv & Ben"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5961245999999,
                    55.6878506
                ],
                "type": "Point"
            },
            "properties": {
                "description": "The Pescatarian",
                "name": "The Pescatarian"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.554357,
                    55.682049
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Radio",
                "name": "Restaurant Radio"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5426806,
                    55.6759238
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Melee",
                "name": "Restaurant Melee"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5496079,
                    55.671271
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Ancestrale",
                "name": "Ancestrale"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5587204999999,
                    55.6690881
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Fleisch",
                "name": "Fleisch"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5863821,
                    55.6825809
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Barabba",
                "name": "Barabba"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5895081,
                    55.6736966
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Donda",
                "name": "Donda"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.577572,
                    55.681653
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Naert",
                "name": "Restaurant Naert"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5575108,
                    55.6707762
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Jah Izakaya & Sake Bar",
                "name": "Jah Izakaya & Sake Bar"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5456699,
                    55.6676801
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Osteria 16",
                "name": "Osteria 16"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5610167,
                    55.6678361
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Gorilla",
                "name": "Restaurant Gorilla"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5546139,
                    55.6794139
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Anarki",
                "name": "Restaurant Anarki"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5802885,
                    55.6662939
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Il Buco",
                "name": "Il Buco"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5682149,
                    55.6851802
                ],
                "type": "Point"
            },
            "properties": {
                "description": "ARK by Souls",
                "name": "ARK by Souls"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5698386,
                    55.684666
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Selma",
                "name": "Selma"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5212776,
                    55.6750196
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Fasangården",
                "name": "Fasangården"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5461457,
                    55.6754853
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Polly",
                "name": "Polly"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5840361,
                    55.6810974
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Frank",
                "name": "Frank"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5807117,
                    55.7017222
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Hos Fischer",
                "name": "Hos Fischer"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5599168,
                    55.6868062
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Safari",
                "name": "Safari"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5798044,
                    55.6822166
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Møntergade",
                "name": "Restaurant Møntergade"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5781956,
                    55.7034791
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Le Saint Jacques",
                "name": "Restaurant Le Saint Jacques"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5434728,
                    55.6932732
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Silberbauers Bistro",
                "name": "Silberbauers Bistro"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5971201,
                    55.70782
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Hija de Sanchez Cantina",
                "name": "Hija de Sanchez Cantina"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5634124,
                    55.6818955
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Nr.30 Spisested & Vinbar",
                "name": "Nr.30 Spisested & Vinbar"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5853534,
                    55.6821885
                ],
                "type": "Point"
            },
            "properties": {
                "description": "KhunJuk",
                "name": "KhunJuk"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5742064,
                    55.6762851
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Damindra",
                "name": "Damindra"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5575438,
                    55.6682458
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Camino",
                "name": "Camino"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5554427,
                    55.6735377
                ],
                "type": "Point"
            },
            "properties": {
                "description": "LAMAR",
                "name": "LAMAR"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5864357,
                    55.6813628
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Goldfinch",
                "name": "Goldfinch"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5626438,
                    55.689345
                ],
                "type": "Point"
            },
            "properties": {
                "description": "GAIJIN",
                "name": "GAIJIN"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.611192,
                    55.690534
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Amass Restaurant",
                "name": "Amass Restaurant"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.6104808,
                    55.6828273
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Noma",
                "name": "Noma"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.559214,
                    55.6679151
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Kødbyens Fiskebar",
                "name": "Kødbyens Fiskebar"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5889561,
                    55.6723008
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Kadeau",
                "name": "Restaurant Kadeau"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5758204,
                    55.6624752
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Alouette",
                "name": "Restaurant Alouette"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5721074,
                    55.7036082
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Geranium",
                "name": "Geranium"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5890687999999,
                    55.6832052
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Aoc",
                "name": "Aoc"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5356085999999,
                    55.6707134
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Formel B",
                "name": "Formel B"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.613737,
                    55.6937129
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Alchemist",
                "name": "Alchemist"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.598607,
                    55.7067965
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Sushi Anaba",
                "name": "Sushi Anaba"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.5308566,
                    55.6747223
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Restaurant Mielcke & Hurtigkarl",
                "name": "Restaurant Mielcke & Hurtigkarl"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    12.568512,
                    55.679581
                ],
                "type": "Point"
            },
            "properties": {
                "description": "Brace",
                "name": "Brace"
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}''

data = json.loads(json_data)
features = data['features']

csv_data = [['name', 'latitude', 'longitude', 'description']]

for feature in features:
    name = feature['properties']['name']
    latitude = feature['geometry']['coordinates'][1]
    longitude = feature['geometry']['coordinates'][0]
    description = feature['properties']['description']
    csv_data.append([name, latitude, longitude, description])

with open('locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerows(csv_data)
