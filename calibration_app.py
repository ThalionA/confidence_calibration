import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

questions = [
    {"question": "What is the atomic number of Hydrogen?", "choices": ['0', '1', '2', '3'], "answer": 1},
    {"question": "Which neurotransmitter is primarily involved in mood regulation?", "choices": ['Dopamine', 'Serotonin', 'Acetylcholine', 'GABA'], "answer": 1},
    {"question": "Who wrote the Declaration of Independence?", "choices": ['Benjamin Franklin', 'John Adams', 'Thomas Jefferson', 'George Washington'], "answer": 2},
    {"question": "Which year did World War II end?", "choices": ['1944', '1945', '1946', '1947'], "answer": 1},
    {"question": "What is the square root of 81?", "choices": ['7', '8', '9', '10'], "answer": 2},
    {"question": "Which of these is a prime number?", "choices": ['21', '29', '33', '35'], "answer": 1},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": ['Harper Lee', 'J.D. Salinger', 'Mark Twain', 'Ernest Hemingway'], "answer": 0},
    {"question": "Which play is not written by Shakespeare?", "choices": ['Macbeth', 'Hamlet', 'Waiting for Godot', 'Othello'], "answer": 2},
    {"question": "Who founded Microsoft?", "choices": ['Steve Jobs', 'Elon Musk', 'Bill Gates', 'Larry Page'], "answer": 2},
    {"question": "What does CPU stand for?", "choices": ['Central Processing Unit', 'Computer Personal Unit', 'Central Peripheral Unit', 'Centralized Power Unit'], "answer": 0},
    {"question": "What is the world record for men's 100m sprint?", "choices": ['9.58s', '9.63s', '9.69s', '9.72s'], "answer": 0},
    {"question": "How many players are there in a standard soccer team?", "choices": ['10', '11', '12', '13'], "answer": 1},
    {"question": "What is the capital of Australia?", "choices": ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], "answer": 3},
    {"question": "Which river is the longest in the world?", "choices": ['Amazon', 'Nile', 'Yangtze', 'Mississippi'], "answer": 1},
    {"question": "Who composed the 9th Symphony?", "choices": ['Wolfgang Amadeus Mozart', 'Ludwig van Beethoven', 'Johann Sebastian Bach', 'Pyotr Ilyich Tchaikovsky'], "answer": 1},
    {"question": "Which of these instruments is a woodwind?", "choices": ['Trumpet', 'Flute', 'Trombone', 'Violin'], "answer": 1},
    {"question": "Which planet is known as the Red Planet?", "choices": ['Venus', 'Mars', 'Jupiter', 'Saturn'], "answer": 1},
    {"question": "What is the currency of Japan?", "choices": ['Yen', 'Yuan', 'Won', 'Peso'], "answer": 0},
    {"question": "What is the largest mammal?", "choices": ['African Elephant', 'Blue Whale', 'Orca', 'Giraffe'], "answer": 1},
    {"question": "Who painted the Mona Lisa?", "choices": ['Michelangelo', 'Leonardo da Vinci', 'Vincent van Gogh', 'Rembrandt'], "answer": 1},
    {"question": "What is the Riemann Hypothesis?", "choices": ['Unproven theorem in number theory', 'Proven theorem in geometry', 'Algorithm in computer science', 'Quantum physics phenomenon'], "answer": 0},
    {"question": "Who developed the theory of conditioned reflex?", "choices": ['Sigmund Freud', 'Ivan Pavlov', 'B.F. Skinner', 'John Watson'], "answer": 1},
    {"question": "Which element has the atomic number 79?", "choices": ['Gold', 'Silver', 'Copper', 'Platinum'], "answer": 0},
    {"question": "Who coined the term 'Schadenfreude'?", "choices": ['Kant', 'Nietzsche', 'Schopenhauer', 'Goethe'], "answer": 2},
    {"question": "What is dark matter?", "choices": ['Antimatter', 'Black holes', 'Invisible mass', 'Supernova remnants'], "answer": 2},
    {"question": "What is the Turing Test?", "choices": ['Quantum computing model', 'Artificial intelligence test', 'Encryption algorithm', 'Programming language'], "answer": 1},
    {"question": "What does the 'H' in HBAR stand for?", "choices": ['Hydrogen', 'Helium', 'Hilbert', 'Hawking'], "answer": 3},
    {"question": "What is Gödel's incompleteness theorem?", "choices": ['Quantum physics theorem', 'Number theory statement', 'Logic and math limitation', 'Computer science algorithm'], "answer": 2},
    {"question": "Who formulated the Laws of Motion?", "choices": ['Albert Einstein', 'Isaac Newton', 'Galileo Galilei', 'Nikola Tesla'], "answer": 1},
    {"question": "What is the Heisenberg Uncertainty Principle?", "choices": ['Quantum property', 'Relativity theory', 'Photon model', 'Chaos theory'], "answer": 0},
    {"question": "What does NAFTA stand for?", "choices": ['North American Free Trade Agreement', 'National Association of Financial Traders and Accountants', 'North Atlantic Fisheries Treaty Agreement', 'National Automotive and Farming Trade Association'], "answer": 0},
    {"question": "What is the base of natural logarithms?", "choices": ['2', '10', 'e', 'π'], "answer": 2},
    {"question": "Who wrote 'Crime and Punishment'?", "choices": ['Leo Tolstoy', 'Fyodor Dostoevsky', 'Anton Chekhov', 'Nikolai Gogol'], "answer": 1},
    {"question": "Which gas contributes most to the greenhouse effect?", "choices": ['Carbon Dioxide', 'Methane', 'Nitrous Oxide', 'Water Vapor'], "answer": 0},
    {"question": "What is the primary objective of Occam's Razor?", "choices": ['Maximize complexity', 'Minimize assumptions', 'Validate hypotheses', 'Isolate variables'], "answer": 1},
    {"question": "Which philosopher argued for the separation of church and state?", "choices": ['John Locke', 'Thomas Hobbes', 'Jean-Jacques Rousseau', 'Immanuel Kant'], "answer": 0},
    {"question": "What is the Pythagorean Theorem used for?", "choices": ['Calculating area', 'Solving quadratic equations', 'Calculating triangle sides', 'Plotting parabolas'], "answer": 2},
    {"question": "Which element is a Noble Gas?", "choices": ['Argon', 'Carbon', 'Oxygen', 'Iron'], "answer": 0},
    {"question": "Who wrote 'The Art of War'?", "choices": ['Confucius', 'Laozi', 'Sun Tzu', 'Mao Zedong'], "answer": 2},
    {"question": "What is the powerhouse of the cell?", "choices": ['Nucleus', 'Endoplasmic Reticulum', 'Golgi Apparatus', 'Mitochondria'], "answer": 3},
    {"question": "Which of these artists is associated with the Baroque period?", "choices": ['Leonardo da Vinci', 'Caravaggio', 'Vincent van Gogh', 'Pablo Picasso'], "answer": 1},
    {"question": "Who wrote 'One Hundred Years of Solitude'?", "choices": ['Gabriel García Márquez', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'J.D. Salinger'], "answer": 0},
    {"question": "In which country was the game of chess invented?", "choices": ['China', 'India', 'Greece', 'Persia'], "answer": 1},
    {"question": "What is the currency of Switzerland?", "choices": ['Euro', 'Franc', 'Krone', 'Lira'], "answer": 1},
    {"question": "Who is known for composing the Four Seasons?", "choices": ['Johann Sebastian Bach', 'Antonio Vivaldi', 'Wolfgang Amadeus Mozart', 'Ludwig van Beethoven'], "answer": 1},
    {"question": "Which mountain is known as the 'Savage Mountain'?", "choices": ['Everest', 'Annapurna', 'K2', 'Denali'], "answer": 2},
    {"question": "Which country is known as the Land of the Rising Sun?", "choices": ['China', 'Japan', 'South Korea', 'Vietnam'], "answer": 1},
    {"question": "Who is the author of the 'Iliad'?", "choices": ['Homer', 'Virgil', 'Socrates', 'Plato'], "answer": 0},
    {"question": "Which city is famous for its Carnival?", "choices": ['Rio de Janeiro', 'New Orleans', 'Venice', 'Munich'], "answer": 0},
    {"question": "Who composed 'Rhapsody in Blue'?", "choices": ['Duke Ellington', 'Scott Joplin', 'George Gershwin', 'Louis Armstrong'], "answer": 2},
    {"question": "In which city is the Louvre Museum located?", "choices": ['Paris', 'London', 'New York', 'Rome'], "answer": 0},
    {"question": "What is the main ingredient in traditional Japanese Sake?", "choices": ['Potatoes', 'Wheat', 'Rice', 'Barley'], "answer": 2},
    {"question": "Who wrote 'Don Quixote'?", "choices": ['Miguel de Cervantes', 'William Shakespeare', 'Leo Tolstoy', 'Victor Hugo'], "answer": 0},
    {"question": "Which country is the origin of the dance tango?", "choices": ['Argentina', 'Spain', 'Cuba', 'Brazil'], "answer": 0},
    {"question": "What does the Latin phrase 'Carpe Diem' mean?", "choices": ['Seize the day', 'Know thyself', 'Buy the day', 'Live forever'], "answer": 0},
    {"question": "Who is the Greek god of war?", "choices": ['Zeus', 'Hermes', 'Ares', 'Apollo'], "answer": 2},
    {"question": "Which city is known as the Big Apple?", "choices": ['Los Angeles', 'Chicago', 'New York', 'San Francisco'], "answer": 2},
    {"question": "Who wrote 'Pride and Prejudice'?", "choices": ['Emily Brontë', 'Virginia Woolf', 'Jane Austen', 'Mary Shelley'], "answer": 2},
    {"question": "Which card game relies heavily on bluffing?", "choices": ['Bridge', 'Poker', 'Blackjack', 'Solitaire'], "answer": 1},
    {"question": "What is the main instrument used in flamenco?", "choices": ['Violin', 'Guitar', 'Saxophone', 'Piano'], "answer": 1},

]

if 'selected_questions' not in st.session_state:
    st.session_state.selected_questions = random.sample(questions, 20)
    random.shuffle(st.session_state.selected_questions)

if 'answers' not in st.session_state:
    st.session_state.answers = []

if 'confidences' not in st.session_state:
    st.session_state.confidences = []

st.title("Confidence Calibration App")

for i, q in enumerate(st.session_state.selected_questions):
    st.subheader(f"Question {i+1}: {q['question']}")
    answer = st.radio(f"Your Answer for question {i+1}", q['choices'], key=f"answer_{i}")
    confidence = st.slider(f"How confident are you for question {i+1}?", 0, 100, 50, key=f"confidence_{i}")

    if len(st.session_state.answers) < len(st.session_state.selected_questions):
        st.session_state.answers.append(answer == q['choices'][q['answer']])
        st.session_state.confidences.append(confidence)
    else:
        st.session_state.answers[i] = answer == q['choices'][q['answer']]
        st.session_state.confidences[i] = confidence

if st.button("Submit"):
    # Calculate the calibration curve
    bins = np.linspace(0, 100, 11)
    bin_means = np.zeros(10)
    
    for i in range(1, len(bins)):
        mask = (np.array(st.session_state.confidences) >= bins[i-1]) & (np.array(st.session_state.confidences) < bins[i])
        bin_data = np.array(st.session_state.answers)[mask]
        if len(bin_data) > 0:
            bin_means[i-1] = np.mean(bin_data)
    
    # Plot
    fig, ax = plt.subplots()
    ax.plot(bins[:-1], bin_means, marker='o')
    ax.plot([0, 100], [0, 1], '--', label="Perfect Calibration")
    ax.set_xlabel("Confidence (%)")
    ax.set_ylabel("Accuracy")
    ax.legend()
    st.pyplot(fig)
