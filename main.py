from flask import Flask, render_template
from  utills import get_candidate, get_candidate_pk, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)

@app.route('/')
def index():
    data = get_candidate()
    return render_template('list.html', list_candidates=data)


@app.route('/candidate/<int:x>/')
def index_1(x):
    data_1 = get_candidate_pk(x)
    return render_template('single.html', candidate=data_1)


@app.route('/search/<candidate_name>')
def index_2(candidate_name):
    data_2 = get_candidates_by_name(candidate_name)
    count = len(data_2)
    return render_template('search.html', cand=data_2, count_1 = count)


@app.route('/skill/<skill_name>')
def index_3(skill_name):
    data_3 = get_candidates_by_skill(skill_name)
    count = len(data_3)
    return render_template('skill.html', cand=data_3, count_2 = count)




if __name__ == '__main__':
    app.run(debug=True)