import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port = 5500
server.bind((ip_address,port))
server.listen()
clients=[]

questions=[
    "What is the pH value of the human body? \n a. 9.2 to 9.8 \n b. 7.0 to 7.8 \n c. 6.1 to 6.3 \n d. 5.4 to 5.6",
    "How many wonder are there in the world? \n a.7\n b.9\n c.4\n d.8",
    "Which planet is closest to the sun? \n a.Mercury\n b.Pluto\n c.Earth\n d.Venus",
    "Who was the first Indian to win the World Amateur Billiards title? \n a. Geet Sethi \n b. Wilson Jones \n c. Michael Ferreira \n d. Manoj Kothari",
    "How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196",
    "What is the German word for Cheese? \n a.Mozarella\n b.Cheese\n c.Kase\n d.Chipotle",
    "Who gifted the Statue of Libery to the US? \n a.Brazil\n b.Germany\n c.Wales\n d.France",
    "How many players are on the field in baseball? \n a.6\n b.7\n c.9\n d.8",
    "Who is the father of Geometry? \ a.Aristotle\n b.Euclid\n c.Pythagoras\n d.Kepler"
    ]

answers=['b','a','a','b','a','c','c','d','c','b']

def clientthread(conn):
    score=0
    conn.send("Welcome to the Quiz Game!!!".encode('utf-8'))
    conn.send("You wil recieve a question. The answer to that questions will be a, b, c or d/n".encode('utf-8'))
    conn.send("You wil recieve a question. The answer to that questions will be a, b, c or d/n".encode('utf-8'))
    index,question,answer = get_random_question_answer(conn)
    while True:
        try:
            message=conn.recv(2048).decode('utf-8')
            if message:
                if message.lower()==answer:
                    score +=1
                    conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Your Answer is Incorrect! Better Luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answer=get_random_question_answer(conn)
            # else:
            #     remove(conn)
        except:
            continue

def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions)-1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_question,random_question,random_index

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

def remove_nickname(nicknames):
    if nicknames in nicknames:
        nicknames.remove(nicknames)



while True:
    conn, addr = server.accept()
    conn.send('NICKNAMES'.encode('utf-8'))
    nicknames = conn.recv(2048).decode('utf-8')
    clients.append(conn)
    nicknames.append(nicknames)
    print (nicknames + " connected")
    new_thread = Thread(target= clientthread,args=(conn , nicknames))
    new_thread.start()