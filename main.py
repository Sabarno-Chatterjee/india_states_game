import pandas
import turtle

screen = turtle.Screen()
screen.title("India States Game")
image = "image.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_data.csv.txt")
all_states = data.state.to_list()

# GAME VARIABLES:
guessed_states = []

while len(guessed_states) < 28:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/29 Correct guesses.", prompt="Guess another state.")
    answer_text = answer_text.title()
    if answer_text == "Exit":
        break
    if answer_text in all_states:
        guessed_states.append(answer_text)
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_data = data[data.state == answer_text]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(f"{state_data.state.item()}", font=("Courier", 8, "normal"))

missed_states = [state for state in all_states if state not in guessed_states]

file = pandas.DataFrame(missed_states)
file.to_csv("Learn.csv")
