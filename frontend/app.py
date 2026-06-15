import streamlit as st

import apis

st.set_page_config(
    page_title="TODO-mon",
    page_icon="✅",
    layout="centered"
)

st.title("Tasks")

st.subheader("Add Task")
with st.form("task_form"):
    
    def clear_form():
        st.session_state.update({
            "title": "",
            "description": ""
        })

    col1, col2 = st.columns([6, 1])
    with col1:
        title = st.text_input("Task", label_visibility="collapsed", placeholder="Task Name", key="title")
        description = st.text_input("Description", label_visibility="collapsed", placeholder="Task Description", key="description")
    with col2:
        submitted = st.form_submit_button("Add")
        clear = st.form_submit_button("Clear", on_click=clear_form)

    if submitted and title:
        response = apis.create_task(title, description)

        if response.status_code == 200:
            st.success("Task Added!")
            st.rerun()

tasks = apis.get_tasks()

active_tasks = [t for t in tasks if not t["is_completed"]]
completed_tasks = [t for t in tasks if t["is_completed"]]

st.subheader("Active Tasks")
for task in active_tasks:
    with st.container(border=True):
        col1, col2, col3 = st.columns([5, 1, 1])

        with col1:
            st.write(task["title"])
            st.write(task["description"])

        with col2:
            if st.button("✓", key=f"complete_{task['id']}"):
                apis.change_task_status(task["id"], True)
                st.rerun()

        with col3:
            if st.button("🗑", key=f"delete_{task['id']}"):
                apis.delete_task(task["id"])
                st.rerun()

st.subheader("Completed Tasks")
for task in completed_tasks:
    with st.container(border=True):
        col1, col2, col3 = st.columns([5, 1, 1])

        with col1:
            st.write(f"~~{task['title']}~~")
            st.write(task["description"])

        with col2:
            if st.button("✗", key=f"uncomplete_{task['id']}"):
                apis.change_task_status(task["id"], False)
                st.rerun()

        with col3:
            if st.button("🗑", key=f"delete_{task['id']}"):
                apis.delete_task(task["id"])
                st.rerun()