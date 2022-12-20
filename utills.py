import json


def get_candidate():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_candidate_pk(candidate_id):
    for i in get_candidate():
        if i['id'] == candidate_id:
            return i
    return None

def get_candidates_by_name(candidate_name):
    name_1 = []
    for i in get_candidate():
        if candidate_name.lower() in i["name"].lower():
                name_1.append(i)
    return name_1


def get_candidates_by_skill(skill_name):
    skill = []
    for i in get_candidate():
        if skill_name.lower() in i['skills'].lower().split(', '):
            skill.append(i)
    return skill


