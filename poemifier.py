from flask import Flask, render_template, request
import random


def insert_enjambment(string, index):
    return string[:index] + '\n' + string[index+1:]

def get_number_of_words(string):
    ind = []
    j = 0
    for i in string:
        if(i == ' '):
            ind.append(j)
        j = j + 1
    return ind

def poemify(notpoem):
    random.seed()

    ind = get_number_of_words(notpoem)
    poem = notpoem

    count = 0
    for element in ind:
        flip = random.randint(0, 2)
        if(flip == 0 or flip == 1):
            continue
        elif(flip == 2):
            poem = insert_enjambment(poem, element)
            count = count + 1
    print(poem)
    return poem, count



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="HOME PAGE")

@app.route("/result", methods = ["POST","GET"])
def result():
    if(request.method == 'POST'):
        return('ok')
    elif request.method=='GET':
        result = request.args
        for key,value in result.items():
            poem = poemify(value)
            print(poem[0])
        return render_template('result.html', Not_Poem = poem[0])
    else:
        return("ok")

if __name__ == "__main__":
    app.run(debug=True)



