import streamlit as st # to run use: streamlit run name-of-file.py
from modules import functions

# declare the todos
todos = functions.read_file_todos()

def add_todo():
    new_todo = st.session_state["new_todo_key"]
    todos.append(new_todo + "\n")
    functions.write_file_todos(todos)
    st.session_state["new_todo_key"] = ""  # Clear the input

st.title("To-Do App")
st.write("<font color=green><b>Get Organized</b></font>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new to-do...",
              on_change=add_todo, key="new_todo_key")

# Optional: Display session state for debugging
# st.session_state