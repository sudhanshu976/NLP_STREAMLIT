import streamlit as st
import numpy as np


st.set_page_config(
    page_title="NLP WEB APP"
)

st.title("NEXT WORD PREDICTOR")
st.sidebar.success("Select a page above")


string1 = st.text_area("Enter the training text   (Note : This may take time depending upon the data size )")



test = st.text_input("ENTER THE WORD")
number = st.number_input("Enter the number of next words" )
number = int(number)


import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,Dense,LSTM

if st.button("PREDICT"):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([string1])

    input_sequences =[]
    for sentence in string1.split("\n"):
        tokenized_sentences = tokenizer.texts_to_sequences([sentence])[0]
        
        for i in range(1,len(tokenized_sentences)):
            input_sequences.append(tokenized_sentences[:i+1])


    max_len = max([len(x) for x in input_sequences])

    padded_input_sentences = pad_sequences(input_sequences , maxlen = max_len , padding ="pre")
    X = padded_input_sentences[:,:-1]
    Y = padded_input_sentences[:,-1]
    num_class = len(tokenizer.word_index)
    Y = to_categorical(Y , num_classes=num_class+1)



    model = Sequential()

    model.add(Embedding(num_class+1,100,input_length = None))

    model.add(Embedding(num_class+1,100,input_length = None ))


    model.add(LSTM(250))
    
    model.add(Dense(num_class+1,activation ="softmax"))

    model.compile(loss="categorical_crossentropy" , optimizer="adam" , metrics=["accuracy"])
    

    model.fit(X,Y,epochs=100)

    for i in  range(number):
    

        output_token = tokenizer.texts_to_sequences([test])[0]
        padded_token = pad_sequences([output_token] , maxlen=max_len,padding="pre")
        output = np.argmax(model.predict(padded_token))
        for word,index in tokenizer.word_index.items():
            if index == output:
                test =test + " " + word
                     
    st.header(test) 
