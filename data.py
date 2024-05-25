import pandas as pd

##d

data = pd.read_csv("csv/animes.csv")
def getData(title: str):
    filtered_data = data[data["title"] == title]

    sorted_data = filtered_data.iloc[0]

    api_end = {
        "title": sorted_data['title'],
        "genre": sorted_data['genre'],
        "episodes": sorted_data['episodes'],
        "image": sorted_data['img_url'],
        "url":  sorted_data['link'],
        "rank": sorted_data["ranked"],
        "synopsis:" : sorted_data['synopsis'],
        "aired:" : sorted_data['aired']
    }

    return api_end

def getAll():
    global_Num = 20
    all_data = data
    api_data = {
        "title": all_data["title"][:global_Num],
        "genre": all_data["genre"][:global_Num],
        "episodes": all_data["episodes"][:global_Num],
        "score": all_data["score"][:global_Num],
        "image": all_data['img_url'][:global_Num],
    }

    return api_data


def getBranched():
    new_data  = data[:500]
    cool = {}
    for index, row in new_data.iterrows():
        Krooz = {
            "title": row["title"],
            "image": row["img_url"],
        }

        cool[index] = Krooz

    return cool





