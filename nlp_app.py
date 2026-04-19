import streamlit as st
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

nltk.download("wordnet")
st.title("Sentiment Analysis")
st.subheader("Sentiment Analysis for user")
text=st.text_area("Enter some text: ")
text=re.sub(r'[^A-za-z0-9]+',"",text)
text=re.sub(r"\s","",text)
text=re.sub(r'http\S+',"link",text)
text=re.sub(r'[\b\d+(?:\.\d+)?\s]+',"",text)
text=text.split()

lemmatizer=WordNetLemmatizer()
lemmatized_words=[lemmatizer.lemmatize(word) for word in text]
text="".join(lemmatized_words)

if st.button("Analyze"):
    blob=TextBlob(text)
    sentiment_score=blob.sentiment.polarity
    if (sentiment_score>0):
        custom_emoji=":blush:"
        st.success(f'Happy: {custom_emoji}')
    elif (sentiment_score<0):
        custom_emoji=":dissapointed:"
        st.warning(f"Sad: {custom_emoji}")
    else:
        custom_emoji = ':confused:'
        st.info(f'Confused : {custom_emoji}')
    st.success(f'Polarity Score is: {sentiment_score}')


