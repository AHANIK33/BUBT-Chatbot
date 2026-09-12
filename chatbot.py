from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knowledge_base import knowledge_base
from text_processing import clean_text

question = []

for item in knowledge_base:
    text = (
        item["question"]
          + " " 
          + " ".join(item["keywords"])
    )

    question.append(text)

    vectorizer = TfidfVectorizer(
        lowercase = True,
        stop_words = "english"
    )

    questions_vectorizer = vectorizer.fit_transform(question)

    def chatbot(user_question):
        user_question = clean_text(user_question)


        if not user_question:

            return "Please enter your question."


        user_vector = vectorizer.transform(
            [user_question]
        )

        similarities = cosine_similarity(
            user_vector,
            questions_vectorizer
        )[0]

        best_index = similarities.argmax()

        best_score = similarities[best_index]

        if best_score < 0.20:
            return (
            "Sorry, I don't have enough information to answer that. "
            "Please ask me about BUBT, CSE, courses, admission, "
            "registration, CGPA, fees, results or other student topics."
        )

        answer = knowledge_base[best_index]["answer"]

        return answer






