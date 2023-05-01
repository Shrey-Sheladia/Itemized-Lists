import streamlit as st
import pandas as pd
import requests
import json
import re
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

URL = os.environ.get("URL")


def create_dataframe_from_dict(actualNames, topic_and_count):
    try:
        data_list = []

        for topic in topic_and_count:
            data_list.append((actualNames[topic], str(topic_and_count[topic])))

        df = pd.DataFrame(data_list, columns=['Topic', 'Count'])

        return df
    except:
        print("Error with DF")
        return None

def cleanName(name):
    name = name.lower()
    name = re.sub(r'\W+', '', name)
    return name

def update_topic_counts(topic):


    response = requests.get(URL+"/get_list_data")
    print(URL+"/get_list_data")

    print(f"STATUS CODE\n{response.status_code}\nSTATUS CODE OVER")
    if response.status_code == 200:
        data = response.json()
        actualNames = data['actualNames']
        topic_and_count = data['topicAndCount']
    else:
        print('Error: failed to retrieve data')

    print(actualNames)
    clean_topic = cleanName(topic)
    actualNames[clean_topic] = topic

    if clean_topic:
        if clean_topic in topic_and_count:
            topic_and_count[clean_topic] += 1
        else:
            topic_and_count[clean_topic] = 1


        jsonFile = json.dumps({
            'actualNames': actualNames,
            'topicAndCount': topic_and_count})
        headers = {'Content-Type': 'application/json'}

        try:
            r = requests.post(url = URL+"/change_list_data", data=jsonFile, headers=headers)
            print("RETURN STATEMENT START",r.text, "RETURN STATEMENT OVER")
        except:
            print("Error with request")


    return create_dataframe_from_dict(actualNames, topic_and_count)

def sort_by_count(df, sort_state):
    if sort_state:
        return df.sort_values('Count', ascending=False)
    else:
        return df.sort_index()

def remove_topic(topic):
    # with open("actualNames.json") as file1:
    #     actualNames = json.load(file1)
    
    # with open("topic_and_count.json") as file2:
    #     topic_and_count = json.load(file2)

    response = requests.get(URL+"/get_list_data")
    if response.status_code == 200:
        data = response.json()
        actualNames = data['actualNames']
        topic_and_count = data['topicAndCount']
    else:
        print('Error: failed to retrieve data')

    clean_topic = cleanName(topic)
    if clean_topic in actualNames and clean_topic in topic_and_count:
        del actualNames[clean_topic]
        del topic_and_count[clean_topic]

        jsonFile = json.dumps({
            'actualNames': actualNames,
            'topicAndCount': topic_and_count})
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url = URL+"/change_list_data", data=jsonFile, headers=headers)
        print(r.text)


        # with open('actualNames.json', 'w') as f:
        #     json.dump(actualNames, f)

        # with open('topic_and_count.json', 'w') as f:
        #     json.dump(topic_and_count, f)

    return create_dataframe_from_dict(actualNames, topic_and_count)


def clear_text():
    st.session_state["text"] = ""

