import turtle
import pandas

screen= turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game = True
data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("learn.csv")
        # ALternatively⬇⬇⬇
        # a = set(all_states)
        # b = set(guessed_state)
        # c = list(a-b)
        # db = pandas.DataFrame(c)
        # t = turtle.Turtle()
        # t.hideturtle()
        # t.penup()
        # state_data = data[data]
        # db.to_csv("Left_states")

        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)








turtle.mainloop()
