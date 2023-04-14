import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
import json
import io
import urllib, base64
import os
import sys

test_Json = {
    "business_discovery": {
      "followers_count": 64074872,
      "media_count": 5246,
      "media": {
        "data": [
          {
            "comments_count": 18505,
            "like_count": 1146993,
            "timestamp": "2023-03-13T00:01:18+0000",
            "id": "18003902401618253"
          },
          {
            "comments_count": 7726,
            "like_count": 881893,
            "timestamp": "2023-03-12T16:57:33+0000",
            "id": "18032551204458425"
          },
          {
            "comments_count": 21671,
            "like_count": 913468,
            "timestamp": "2023-03-10T14:00:08+0000",
            "id": "17965844765120498"
          },
          {
            "comments_count": 5471,
            "like_count": 2757792,
            "timestamp": "2023-03-05T19:09:23+0000",
            "id": "17924711219660941"
          },
          {
            "comments_count": 13895,
            "like_count": 827893,
            "timestamp": "2023-02-26T19:30:09+0000",
            "id": "17955301187430554"
          },
          {
            "comments_count": 5118,
            "like_count": 527993,
            "timestamp": "2023-02-25T16:11:30+0000",
            "id": "17943840116562410"
          },
          {
            "comments_count": 10516,
            "like_count": 806170,
            "timestamp": "2023-02-25T11:19:00+0000",
            "id": "17966450036247781"
          },
          {
            "comments_count": 1478,
            "like_count": 128874,
            "timestamp": "2023-02-24T20:55:24+0000",
            "id": "18034380748451251"
          },
          {
            "comments_count": 1966,
            "like_count": 150792,
            "timestamp": "2023-02-23T15:00:47+0000",
            "id": "18009669904508577"
          },
          {
            "comments_count": 5629,
            "like_count": 425084,
            "timestamp": "2023-02-21T01:45:43+0000",
            "id": "17952245936522250"
          },
          {
            "comments_count": 3353,
            "like_count": 315051,
            "timestamp": "2023-02-19T18:20:06+0000",
            "id": "17976364541012905"
          },
          {
            "comments_count": 18844,
            "like_count": 1837103,
            "timestamp": "2023-02-18T23:38:24+0000",
            "id": "17862087713886833"
          },
          {
            "comments_count": 2783,
            "like_count": 328199,
            "timestamp": "2023-02-18T19:25:21+0000",
            "id": "17861942912890105"
          },
          {
            "comments_count": 16988,
            "like_count": 1026941,
            "timestamp": "2023-02-18T14:56:37+0000",
            "id": "17957086289238659"
          },
          {
            "comments_count": 2119,
            "like_count": 66388,
            "timestamp": "2023-02-17T20:29:21+0000",
            "id": "17917525613607020"
          },
          {
            "comments_count": 14577,
            "like_count": 1171165,
            "timestamp": "2023-02-17T20:05:27+0000",
            "id": "17974691000031237"
          },
          {
            "comments_count": 5741,
            "like_count": 573368,
            "timestamp": "2023-02-16T17:21:21+0000",
            "id": "17886961112739414"
          },
          {
            "comments_count": 3922,
            "like_count": 397703,
            "timestamp": "2023-02-15T22:07:19+0000",
            "id": "17979192244841432"
          },
          {
            "comments_count": 3293,
            "like_count": 230429,
            "timestamp": "2023-02-12T02:33:03+0000",
            "id": "17954597594384438"
          },
          {
            "comments_count": 7949,
            "like_count": 682456,
            "timestamp": "2023-02-09T15:27:13+0000",
            "id": "17975973008057183"
          },
          {
            "comments_count": 15170,
            "like_count": 896320,
            "timestamp": "2023-02-06T19:56:19+0000",
            "id": "17954731571247167"
          },
          {
            "comments_count": 69370,
            "like_count": 1957945,
            "timestamp": "2023-02-05T23:34:04+0000",
            "id": "17984803276873338"
          },
          {
            "comments_count": 4150,
            "like_count": 149017,
            "timestamp": "2023-02-05T16:47:17+0000",
            "id": "17962634228501190"
          },
          {
            "comments_count": 15725,
            "like_count": 1383177,
            "timestamp": "2023-02-05T05:40:30+0000",
            "id": "17942608667424384"
          },
          {
            "comments_count": 8399,
            "like_count": 556903,
            "timestamp": "2023-02-04T22:25:08+0000",
            "id": "17875672436817386"
          }
        ],
        "paging": {
          "cursors": {
            "after": "QVFIUlVBZAjR0MFkxeE1pYjh1VzloQU04RVl1ektiQVZAtUThxSk9GbldNX19BUGROSUlNVEdyWVhpdEIzbTJWREF1aUx4TXN1eWJtbVNPU01iMWhCTTRtWHh3"
          }
        }
      },
      "id": "17841400271080416"
    },
    "id": "17841454088809121"
  }


def createGoGraphic(title , color):
    list_time = [2,3,5]
    list_likes = [34,25,44]
    #===========================================================================#
    #========================== Config do Gráfico ==============================#
    x = np.array(list_time)
    y = np.array(list_likes)
    fig, ax = plt.subplots()

    ax.set_title("My title" , fontsize=18, )#fontweight='bold'

    plt.rcParams['font.family'] = 'Roboto'
    plt.rcParams['font.weight'] = 'regular'

    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom']

    ax.tick_params(axis='y', width=0)
    ax.tick_params(axis='x', width=0)

    ax.set_xlabel('Eixo X', fontsize=14)
    ax.set_ylabel('Eixo Y', fontsize=14)

    ax.plot(x, y, color=color, 
            marker="", label="Curtidas/100 Por Tempo",
            markersize=10
            )
    
    plt.fill_between(x, y, 0, color='red', alpha=0.3)

    #ax.annotate('Maior valor', xy=(2, 4), xytext=(2.5, 4.5), 
            #arrowprops=dict(facecolor='black', shrink=0.05))

    ax.grid(axis='y', linestyle='-', linewidth=0.5, color='gray')
    #ax.text(3.5, 3.5, 'Anotação', fontsize=12)
    ax.legend(loc='upper right', fontsize=0, framealpha=1, edgecolor='black', fancybox=False)
    ax.set_facecolor('white')

    plt.show()



createGoGraphic("teste" , "red")







