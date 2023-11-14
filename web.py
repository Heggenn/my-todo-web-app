import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title('Rzeczy do zrobienia')
st.subheader('To jest moja aplikacja rzeczy do zrobienia.')
st.write('Ta aplikacja podniesie Twoja produktywnosc')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # jako key przyjmuje
    if checkbox:                            # nazwe poszcz. todo
        todos.pop(index)                    # gdyby byl jeden key to wszystkie pozycje nazywalyby sie tak samo i nadpisywalyby sie
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


todo_input = st.text_input(label='Dupa',
                           placeholder='Dodaj rzecz do zrobienia.',
                           on_change=add_todo,
                           key='new_todo')