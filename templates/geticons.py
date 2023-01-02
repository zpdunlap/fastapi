import requests

def save_icons(json_obj):
    # print("fuck")
    # print(json_obj)
    # for category, icons in json_obj['armada'].items():
    #     # print("test")
    #     for icon_name, icon_data in icons.items():
            # try:
                icon_url = "json/systems.geojson"#icon_data['iconUrl']
                icon_path = "json/systems.geojson"#'icon'+icon_data['iconUrl']
                response = requests.get('https://stfcmap.org/assets/'+icon_url)
                # print(response.content)
                # print('https://stfcmap.org/assets/icon/'+icon_url)
                if response.status_code == 200:
                    with open('./'+icon_path, 'wb') as f:
                        f.write(response.content)
            # except:
            #     print(" error on this icon!")
                # continue

# example usage
json_obj = {
    "misc": {
        "Station Hub": {
            "iconSize": [40, 40],
            "iconUrl": "/base-icon.png",
            "className": "station-hub"
        },
        "pathArrow": {
            "iconSize": [43, 25],
            "iconUrl": "/path/path-arrow.png",
            "className": "path-arrow"
        },
        "missions": {
            "iconSize": [20, 24],
            "iconUrl": "/ui/missions-available.png",
            "className": "missions"
        }
    },
    "mines": {
        "Parsteel": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/parsteel.png",
            "className": "parsteel"
        },
        "Tritanium": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/tritanium.png",
            "className": "tritanium"
        },
        "Dilithium": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/dilithium.png",
            "className": "dilithium"
        },
        "Raw Latinum": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-latinum.png",
            "className": "latinum"
        },
        "Concentrated Latinum": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/concentrated-latinum.png",
            "className": "latinum"
        },
        "2* Raw Crystal": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-crystal-2.png",
            "className": "crystal2"
        },
        "3* Raw Crystal": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-crystal-3.png",
            "className": "crystal3"
        },
        "4* Raw Crystal": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-crystal-4.png",
            "className": "crystal4"
        },
        "2* Raw Gas": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-gas-2.png",
            "className": "gas2"
        },
        "3* Raw Gas": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-gas-3.png",
            "className": "gas3"
        },
        "4* Raw Gas": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-gas-4.png",
            "className": "gas4"
        },
        "2* Raw Ore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-ore-2.png",
            "className": "ore2"
        },
        "3* Raw Ore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-ore-3.png",
            "className": "ore3"
        },
        "4* Raw Ore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-ore-4.png",
            "className": "ore4"
        },
        "1* Raw Isogen": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-isogen-1.png",
            "className": "isogen1"
        },
        "2* Raw Isogen": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-isogen-2.png",
            "className": "isogen2"
        },
        "3* Raw Isogen": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/raw-isogen-3.png",
            "className": "isogen3"
        },
        "Corrupted Data": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/corrupted-data.png",
            "className": "corrupted-data"
        },
        "Decoded Data": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/decoded-data.png",
            "className": "decoded-data"
        },
        "Tribble": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/tribble.png",
            "className": "tribble"
        },
        "Mycelium Spore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/mycelium-spore.png",
            "className": "mycelium"
        },
        "Phantom Particles": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/particle-phantom.png",
            "className": "particle-phantom"
        },
        "Quantum Particles": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/particle-quantum.png",
            "className": "particle-quantum"
        },
        "Surax Particles": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/particle-surax.png",
            "className": "particle-surax"
        }
    },
    "other_rss": {
        "2* Refined Crystal": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-crystal-2.png",
            "className": "ref-crystal2"
        },
        "3* Refined Crystal": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-crystal-3.png",
            "className": "ref-crystal3"
        },
        "4* Refined Crystal": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-crystal-4.png",
            "className": "ref-crystal4"
        },
        "2* Refined Gas": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-gas-2.png",
            "className": "ref-gas2"
        },
        "3* Refined Gas": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-gas-3.png",
            "className": "ref-gas3"
        },
        "4* Refined Gas": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-gas-4.png",
            "className": "ref-gas4"
        },
        "2* Refined Ore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-ore-2.png",
            "className": "ref-ore2"
        },
        "3* Refined Ore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-ore-3.png",
            "className": "ref-ore3"
        },
        "4* Refined Ore": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-ore-4.png",
            "className": "ref-ore4"
        },
        "Common Plutonium": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/common-plutonium.png",
            "className": "com-plutonium"
        },
        "Uncommon Plutonium": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/uncommon-plutonium.png",
            "className": "unc-plutonium"
        },
        "Rare Plutonium": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/rare-plutonium.png",
            "className": "rare-plutonium"
        },
        "Swarm": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/swarm-biominerals.png",
            "className": "swarm"
        },
        "Separatist": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/separatists-fake.png",
            "className": "swarm"
        },
        "Doomsday": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/doomsdayworm.png",
            "className": "swarm"
        },
        "Frequency Modulator": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/frequency-modulator.png",
            "className": "freq-modulator"
        },
        "Inert Nanoprobe": {
            "iconSize": [40, 40],
            "iconUrl": "/borg/inert-nanoprobe.png",
            "className": "inert-nanoprobe"
        },
        "Active Nanoprobe": {
            "iconSize": [40, 40],
            "iconUrl": "/borg/active-nanoprobe.png",
            "className": "active-nanoprobe"
        },
        "Charged Nanoprobe": {
            "iconSize": [40, 40],
            "iconUrl": "/borg/charged-nanoprobe.png",
            "className": "charged-nanoprobe"
        },
        "Uncommon Armada": {
            "iconSize": [40, 40],
            "iconUrl": "/credit/uncommon-armada-credit.png",
            "className": "u-armada-credit"
        },
        "Rare Armada": {
            "iconSize": [40, 40],
            "iconUrl": "/credit/rare-armada-credit.png",
            "className": "r-armada-credit"
        },
        "Epic Armada": {
            "iconSize": [40, 40],
            "iconUrl": "/credit/epic-armada-credit.png",
            "className": "e-armada-credit"
        },
        "Refined Mycelium": {
            "iconSize": [40, 40],
            "iconUrl": "/resource/refined-mycelium.png",
            "className": "ref-mycelium"
        }
    },
    "armada": {
        "normal": {
            "Uncommon Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/u-directive.png",
                "className": "u-directive"
            },
            "Rare Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/r-directive.png",
                "className": "r-directive"
            },
            "Epic Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/e-directive.png",
                "className": "e-directive"
            }
        },
        "doomsday": {
            "Uncommon Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/u-directive.png",
                "className": "u-directive"
            },
            "Rare Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/r-directive.png",
                "className": "r-directive"
            },
            "Epic Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/e-directive.png",
                "className": "e-directive"
            }
        },
        "borg": {
            "Uncommon Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/u-borg-directive.png",
                "className": "u-borg-directive"
            },
            "Rare Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/r-borg-directive.png",
                "className": "r-borg-directive"
            },
            "Epic Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/e-borg-directive.png",
                "className": "e-borg-directive"
            },
            "Borg Megacube": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/mc-borg-directive.png",
                "className": "mc-borg-directive"
            }
        },
        "eclipse": {
            "Uncommon Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/u-outlaw-directive.png",
                "className": "u-outlaw-directive"
            },
            "Rare Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/r-outlaw-directive.png",
                "className": "r-outlaw-directive"
            },
            "Epic Armada": {
                "iconSize": [40, 40],
                "iconUrl": "/armada/e-outlaw-directive.png",
                "className": "e-outlaw-directive"
            }
        }
    },
    "factions": {
        "Federation": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/federation.png",
            "className": "federation"
        },
        "Klingon": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/klingon.png",
            "className": "klingon"
        },
        "Romulan": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/romulan.png",
            "className": "romulan"
        },
        "Independent": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/independent.png",
            "className": "independent"
        },
        "Augment": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/augment.png",
            "className": "augment"
        },
        "Rogue": {
            "iconSize": [40, 40],
            "iconUrl": "/faction/rogue.png",
            "className": "rogue"
        }
    },
    "ship_types": {
        "Battleship": {
            "iconSize": [30, 30],
            "iconUrl": "/ship/battleship-icon.png",
            "className": "battleship"
        },
        "Explorer": {
            "iconSize": [30, 30],
            "iconUrl": "/ship/explorer-icon.png",
            "className": "explorer"
        },
        "Interceptor": {
            "iconSize": [30, 30],
            "iconUrl": "/ship/interceptor-icon.png",
            "className": "interceptor"
        },
        "Survey": {
            "iconSize": [30, 30],
            "iconUrl": "/ship/survey-icon.png",
            "className": "survey"
        },
        "Scout": {
            "iconSize": [30, 30],
            "iconUrl": "/ship/scout-icon.png",
            "className": "scout"
        }
    },
    "ship_parts": {
        "Battleship": {
            "iconSize": [40, 40],
            "iconUrl": "/ship/battleship-parts.png",
            "className": "battleship"
        },
        "Explorer": {
            "iconSize": [40, 40],
            "iconUrl": "/ship/explorer-parts.png",
            "className": "explorer"
        },
        "Interceptor": {
            "iconSize": [40, 40],
            "iconUrl": "/ship/interceptor-parts.png",
            "className": "interceptor"
        },
        "Survey": {
            "iconSize": [40, 40],
            "iconUrl": "/ship/survey-parts.png",
            "className": "survey"
        }
    },
    "travel_paths": {
        "lock":{
            "iconSize": [18, 24],
            "iconUrl": "/path/lock-path.png",
            "className": "lock"
        },
        "toll":{
            "iconSize": [18, 18],
            "iconUrl": "/path/toll-path.png",
            "className": "toll"
        },
        "borg":{
            "iconSize": [18, 18],
            "iconUrl": "/path/toll-path.png",
            "className": "borg"
        },
        "transwarp":{
            "iconSize": [18, 18],
            "iconUrl": "/path/toll-path.png",
            "className": "transwarp"
        },
        "borgtranswarp":{
            "iconSize": [18, 18],
            "iconUrl": "/path/toll-path.png",
            "className": "borgtranswarp"
        },
        "roguetranswarp":{
            "iconSize": [18, 18],
            "iconUrl": "/path/toll-path.png",
            "className": "roguetranswarp"
        },
        "arena":{
            "iconSize": [18, 18],
            "iconUrl": "/path/toll-path.png",
            "className": "arena"
        }
    }
}

save_icons(json_obj)

