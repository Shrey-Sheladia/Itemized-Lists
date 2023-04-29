import streamlit as st
import pandas as pd
import json
import re

def create_dataframe_from_dict(actualNames, topic_and_count):
    data_list = []

    for topic in topic_and_count:
        data_list.append((actualNames[topic], topic_and_count[topic]))

    df = pd.DataFrame(data_list, columns=['Topic', 'Count'])

    return df

def cleanName(name):
    name = name.lower()
    name = re.sub(r'\W+', '', name)
    return name

def update_topic_counts(topic):
    with open("actualNames.json") as file1:
        actualNames = json.load(file1)
    
    with open("topic_and_count.json") as file2:
        topic_and_count = json.load(file2)

    clean_topic = cleanName(topic)
    actualNames[clean_topic] = topic

    if clean_topic:
        if clean_topic in topic_and_count:
            topic_and_count[clean_topic] += 1
        else:
            topic_and_count[clean_topic] = 1
        
        with open('actualNames.json', 'w') as f:
            json.dump(actualNames, f)
        
        with open('topic_and_count.json', 'w') as f:
            json.dump(topic_and_count, f)

    return create_dataframe_from_dict(actualNames, topic_and_count)

def sort_by_count(df, sort_state):
    if sort_state:
        return df.sort_values('Count', ascending=False)
    else:
        return df.sort_index()

def remove_topic(topic):
    with open("actualNames.json") as file1:
        actualNames = json.load(file1)
    
    with open("topic_and_count.json") as file2:
        topic_and_count = json.load(file2)

    clean_topic = cleanName(topic)
    if clean_topic in actualNames and clean_topic in topic_and_count:
        del actualNames[clean_topic]
        del topic_and_count[clean_topic]

        with open('actualNames.json', 'w') as f:
            json.dump(actualNames, f)

        with open('topic_and_count.json', 'w') as f:
            json.dump(topic_and_count, f)

    return create_dataframe_from_dict(actualNames, topic_and_count)


def clear_text():
    st.session_state["text"] = ""

