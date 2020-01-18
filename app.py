def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, -1) 
    loaded_model = pickle.load(open("random_forest_tuned.pickle", "rb")) 
    result = loaded_model.predict_proba(to_predict) 
    return result[0]

@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 1: 
            prediction ='Income more than 50K'
        else: 
            prediction ='Income less that 50K'            
        return render_template("result.html", prediction = prediction) 
