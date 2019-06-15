from flask import make_response, abort

# Data to serve with our API
BLOCKS = {
  "0": {
    "blockname": "Центральный",
    "blockborderpoints": {
      "0": [
        "0",
        "0"
      ],
      "1": [
        "0",
        "0"
      ],
      "2": [
        "0",
        "0"
      ]
    },
    "people": {
      "m": {
        "0": {
          "population": "666",
          "activities": [
            "kidgardens",
            "parks"
          ]
        },
        "1": {
          "population": "666",
          "activities": [
            "schools",
            "colleges",
            "parks"
          ]
        },
        "2": {
          "population": "666",
          "activities": [
            "universities",
            "parks",
            "bars"
          ]
        },
        "3": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "4": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "5": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        }
      },
      "f": {
        "0": {
          "population": "666",
          "activities": [
            "kidgardens",
            "parks"
          ]
        },
        "1": {
          "population": "666",
          "activities": [
            "schools",
            "colleges",
            "parks"
          ]
        },
        "2": {
          "population": "666",
          "activities": [
            "universities",
            "parks",
            "bars"
          ]
        },
        "3": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "4": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "5": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        }
      }
    },
    "objects": {
      "kidgardens": [
        {
          "0": {
            "name": "kg0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "kg1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "kg2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "schools": [
        {
          "0": {
            "name": "s0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "s1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "s2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "parks": [
        {
          "0": {
            "name": "p0",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "p1",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "p2",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "colleges": [
        {
          "0": {
            "name": "c0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "c1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "c2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "universities": [
        {
          "0": {
            "name": "u0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "u1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "u2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "hospitals": [
        {
          "0": {
            "name": "h1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "h1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "h2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "malls": [
        {
          "0": {
            "name": "m0",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "m1",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "m2",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "leisure": [
        {
          "0": {
            "name": "l0",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "l1",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "l2",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ]
    },
    "emergencies": {
      "crime": "100",
      "fire": "50",
      "med": "25"
    },
    "generations": {
      "0": [
        "0",
        "6"
      ],
      "1": [
        "7",
        "17"
      ],
      "2": [
        "18",
        "25"
      ],
      "3": [
        "26",
        "39"
      ],
      "4": [
        "40",
        "64"
      ],
      "5": [
        "65",
        "200"
      ]
    }
  },
  "1": {
    "blockname": "Киевский",
    "blockborderpoints": {
      "0": [
        "0",
        "0"
      ],
      "1": [
        "0",
        "0"
      ],
      "2": [
        "0",
        "0"
      ]
    },
    "people": {
      "m": {
        "0": {
          "population": "666",
          "activities": [
            "kidgardens",
            "parks"
          ]
        },
        "1": {
          "population": "666",
          "activities": [
            "schools",
            "colleges",
            "parks"
          ]
        },
        "2": {
          "population": "666",
          "activities": [
            "universities",
            "parks",
            "bars"
          ]
        },
        "3": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "4": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "5": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        }
      },
      "f": {
        "0": {
          "population": "666",
          "activities": [
            "kidgardens",
            "parks"
          ]
        },
        "1": {
          "population": "666",
          "activities": [
            "schools",
            "colleges",
            "parks"
          ]
        },
        "2": {
          "population": "666",
          "activities": [
            "universities",
            "parks",
            "bars"
          ]
        },
        "3": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "4": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        },
        "5": {
          "population": "666",
          "activities": [
            "parks",
            "hospitals"
          ]
        }
      }
    },
    "objects": {
      "kidgardens": [
        {
          "0": {
            "name": "kg0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "kg1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "kg2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "schools": [
        {
          "0": {
            "name": "s0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "s1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "s2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "parks": [
        {
          "0": {
            "name": "p0",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "p1",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "p2",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "colleges": [
        {
          "0": {
            "name": "c0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "c1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "c2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "universities": [
        {
          "0": {
            "name": "u0",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "u1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "u2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "hospitals": [
        {
          "0": {
            "name": "h1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "h1",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "h2",
            "population": "10",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "malls": [
        {
          "0": {
            "name": "m0",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "m1",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "m2",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ],
      "leisure": [
        {
          "0": {
            "name": "l0",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "1": {
            "name": "l1",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        },
        {
          "2": {
            "name": "l2",
            "capacity": "15",
            "x": "0",
            "y": "0"
          }
        }
      ]
    },
    "emergencies": {
      "crime": "100",
      "fire": "50",
      "med": "25"
    },
    "generations": {
      "0": [
        "0",
        "6"
      ],
      "1": [
        "7",
        "17"
      ],
      "2": [
        "18",
        "25"
      ],
      "3": [
        "26",
        "39"
      ],
      "4": [
        "40",
        "64"
      ],
      "5": [
        "65",
        "200"
      ]
    }
  }
}


def read(blocknumber):
    if blocknumber in BLOCKS:
        return {"blockname": BLOCKS.get(blocknumber)["blockname"], "blockborderpoints": BLOCKS.get(blocknumber)["blockborderpoints"] }
    else:
        abort(
            404, "block with number {blocknumber} not found".format(blocknumber=blocknumber)
        )

    return block

def read_object_types(blocknumber):
    if blocknumber in BLOCKS:
        return sorted(BLOCKS.get(blocknumber)["objects"].keys())
    else:
        abort(
            404, "block with number {blocknumber} not found".format(blocknumber=blocknumber)
        )

def read_object(blocknumber, blockobjecttype):
    if blockobjecttype in sorted(BLOCKS.get(blocknumber)["objects"].keys()):
        return BLOCKS.get(blocknumber)["objects"][blockobjecttype]
    else:
        abort(
            404, "block object with type {blockobjecttype} not found".format(blockobjecttype=blockobjecttype)
        )

def read_emergencies(blocknumber):
    if blocknumber in BLOCKS:
        return BLOCKS.get(blocknumber)["emergencies"]
    else:
        abort(
            404, "block with number {blocknumber} not found".format(blocknumber=blocknumber)
        )

def read_generations(blocknumber):
    if blocknumber in BLOCKS:
        return BLOCKS.get(blocknumber)["generations"]
    else:
        abort(
            404, "block with number {blocknumber} not found".format(blocknumber=blocknumber)
        )

def read_people(blocknumber, sex, generation):
    if (blocknumber in BLOCKS) and (sex in sorted(BLOCKS.get(blocknumber)["people"].keys())) and (generation in sorted(BLOCKS.get(blocknumber)["people"][sex].keys())):
        return BLOCKS.get(blocknumber)["people"][sex][generation]
    else:
        abort(
            404, "block/sex/generation not found"
        )

