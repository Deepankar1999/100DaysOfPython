import pandas
import turtle

screen=turtle.Screen()
screen.title("U.S. States Game")
image="./day25/US_States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("./day25/US_States/50_states.csv")
all_states=data["state"].tolist()
guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                  prompt="Enter the state name , you guessed").title()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("./day25/US_States/to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        
        t.write(state_data.state.item())







screen.exitonclick()