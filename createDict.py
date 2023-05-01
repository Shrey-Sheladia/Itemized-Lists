import json
from Utils import *


with open("info.txt") as f:
    info = f.readlines()

# lines = f.split("\n")

actualNames, topicandcounts = {}, {}

for l in info:
    line = (l.strip())
    # print(line)
    index, topic, count = line.split("\t")
    if "'" in topic or '"' in topic:
        print(topic)

    cleanTopic = cleanName(topic)

    actualNames[cleanTopic] = topic
    topicandcounts[cleanTopic] = count


with open('actualNames.json', 'w') as f:
    json.dump(actualNames, f)
    
with open('topic_and_count.json', 'w') as f:
    json.dump(topicandcounts, f)
    
