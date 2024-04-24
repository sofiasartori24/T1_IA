import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

class Tic_Tac_Toe_Models:
    def __init__(self):
        separator = ','
        names = ['1','2','3','4','5','6','7','8','9','result']
        #reading the dataset using the separator
        db = pd.read_csv('T1_IA/tic-tac-toe.data', sep=separator, names=names)

        #separating the data in features and target
        X = db.drop(columns=['result'])
        y = db['result']

        print(X)

        #transforming the data from string to number using one-hot encoding
        X = pd.get_dummies(X)

        #separating the data in training, test and validation (80% for training, 20% for testing, 10% for validation)
        self.X_train_test, self.X_val, self.y_train_test, self.y_val = train_test_split(X, y, test_size=0.1, stratify=y, random_state=0)
        self.X_train,self. X_test, self.y_train, self.y_test = train_test_split(self.X_train_test, self.y_train_test, test_size=0.2, stratify=self.y_train_test, random_state=0)

        #training the models
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.knn.fit(self.X_train,self.y_train)

        self.decison_tree = DecisionTreeClassifier()
        self.decison_tree.fit(self.X_train,self.y_train)

        self.mlp = MLPClassifier(hidden_layer_sizes=(50, 25), activation='relu', solver='adam')
        self.mlp.fit(self.X_train,self.y_train)

        self.naive_bayes = GaussianNB()
        self.naive_bayes.fit(self.X_train,self.y_train)

        #training a model expert in Draw or inGame: 
    
        #filtering database to only have Draw or inGame 
        db_draw_inGame = db[(db['result'] != 'owins') & (db['result'] != 'xwins')]
        X_draw_inGame = pd.get_dummies(db_draw_inGame.drop(columns=['result']))
        Y_draw_inGame = db_draw_inGame['result']

        #training a decision tree for draw or inGame
        self.decison_tree_draw_inGame = DecisionTreeClassifier()
        self.decison_tree_draw_inGame.fit(X_draw_inGame, Y_draw_inGame)

        #training a mlp for draw or inGame
        self.mlp_draw_inGame = MLPClassifier(hidden_layer_sizes=(50, 25), activation='relu', solver='adam')
        self.mlp_draw_inGame.fit(X_draw_inGame, Y_draw_inGame)

    #funcs to make a prediction using a specific model
    def predict_knn(self, x):
        data_encoded = pd.get_dummies(x)
        data_encoded = data_encoded.reindex(columns=self.X_train.columns, fill_value=0)

        return self.knn.predict(data_encoded)   
    
    def predict_tree(self, x):
        data_encoded = pd.get_dummies(x)
        data_encoded = data_encoded.reindex(columns=self.X_train.columns, fill_value=0)
        
        return self.decison_tree.predict(data_encoded)
    
    def predict_mlp(self, x):
        data_encoded = pd.get_dummies(x)
        data_encoded = data_encoded.reindex(columns=self.X_train.columns, fill_value=0)

        return self.mlp.predict(x)
    
    def predict_naive_bayes(self, x):
        data_encoded = pd.get_dummies(x)
        data_encoded = data_encoded.reindex(columns=self.X_train.columns, fill_value=0)
        return self.naive_bayes.predict(data_encoded)
    
    #func to make prediction using the Draw experts
    def predict_tree_with_draw_experts(self,x):
        data_encoded = pd.get_dummies(x)
        data_encoded = data_encoded.reindex(columns=self.X_train.columns, fill_value=0)

        #getting the experts predictions
        prediction_draw_inGame_tree = self.decison_tree_draw_inGame.predict(data_encoded)
        prediction_draw_inGame_mpl = self.mlp_draw_inGame.predict(data_encoded)

        if prediction_draw_inGame_mpl[0] == 'Draw':
            return prediction_draw_inGame_mpl
        if prediction_draw_inGame_tree[0] == 'Draw':
            return prediction_draw_inGame_tree 
        
        return self.mlp.predict(data_encoded)
    
    def print_evaluations(self):
        #testing the models
        self.knn_predictions = self.knn.predict(self.X_test)
        self.tree_predictions = self.decison_tree.predict(self.X_test)
        self.mlp_predictions = self.mlp.predict(self.X_test)
        self.naive_bayes_predictions = self.naive_bayes.predict(self.X_test)
        self.experts_predctions = self.predict_tree_with_draw_experts(self.X_test)

        print('KNN EVALUATION ON TEST')
        print('Accuracy:', accuracy_score(self.y_test, self.knn_predictions))
        print('F1:', f1_score(self.y_test, self.knn_predictions, average='macro'))
        print('----------------------------------')

        print('DECISION TREE EVALUATION ON TEST')
        print('Accuracy:', accuracy_score(self.y_test, self.tree_predictions))
        print('F1:', f1_score(self.y_test, self.tree_predictions, average='macro'))
        print('----------------------------------')

        print('MLP EVALUATION ON TEST')
        print('Accuracy:', accuracy_score(self.y_test, self.mlp_predictions))
        print('F1:', f1_score(self.y_test, self.mlp_predictions, average='macro'))
        print('----------------------------------')

        print('NAIVE BAYES EVALUATION ON TEST')
        print('Accuracy:', accuracy_score(self.y_test, self.naive_bayes_predictions))
        print('F1:', f1_score(self.y_test, self.naive_bayes_predictions, average='macro'))
        print('----------------------------------')

        print('EXPERT EVALUATION ON TEST')
        print('Accuracy:', accuracy_score(self.y_test, self.experts_predctions))
        print('F1:', f1_score(self.y_test, self.experts_predctions, average='macro'))
        print('----------------------------------')

model = Tic_Tac_Toe_Models()
model.print_evaluations()