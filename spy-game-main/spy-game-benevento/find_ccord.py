TOTAL_COORDS = 40


def uno():
    coords = [[41.132516, 14.776644], [41.12807968186991, 14.773902909378782]]
    c1 = []

    lenght_of_each_interval = TOTAL_COORDS // len(coords)

    for interval in range(len(coords)-1):
        starting_point = coords[interval][0], coords[interval][1]
        ending_point = coords[interval + 1][0], coords[interval + 1][1]
        distance = [ending_point[0] - starting_point[0],
                    ending_point[0] - starting_point[0]]
        points = [(starting_point[0] + distance[0]/i, starting_point[1] +
                   distance[1]/i) for i in range(1, lenght_of_each_interval+1)]
        c1.extend(points)

    c1.append(coords[1])
    for c in c1:
        print(f"{c[0]}, {c[0]}")


def due(places):
    dictionary_of_places = {
        "A": [41.12807968186991, 14.773902909378782],
        "B": [41.124326457864505, 14.789189516724718],
        "C": [41.128, 14.777],
        "D": [41.13323250215625, 14.773070764002089],
        "E": [41.136910117128366, 14.775458068249161],
        "F": [41.12697301006923, 14.788711870098108],
        "G": [41.132516, 14.776644],
        "H": [41.121139, 14.772991],
        "I":  [41.130842, 14.787590],
        "J":  [41.12430300355027, 14.785002985102373]
    }
    for place in places:
        print(str(dictionary_of_places[place][0]) +
              ", " + str(dictionary_of_places[place][1]))



due("GADCBE")
