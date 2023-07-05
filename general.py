import streamlit as st
import os

# This file is intended to be run with Streamlit.
# From the commandline, try `streamlit run ./portfolio_main.py`

def import_md_text(file_name:str):
    text_body = ''
    file_name = os.path.join('text_snippets', file_name)

    with open(file_name, 'r') as f:
        text_body = f.read()

    return text_body

def show_picture_section(
        image_name:str, 
        markdown_name:str, 
        image_caption:str=None, 
        column_spacing:list=[2, 2], 
        picture_orientation:str='left',
        section_title:str=None
        ):
    orientation_options = ['left', 'right', 'full']
    if picture_orientation not in orientation_options:
        return

    with st.container():
        st.divider()
        if section_title is not None:
            st.markdown(section_title)

        profile_image_path = os.path.join('images', image_name)

        if picture_orientation == 'left':
            picture_col, text_col = st.columns(column_spacing)
        elif picture_orientation == 'right':
            text_col, picture_col = st.columns(column_spacing)
        
        with picture_col:
            st.image(profile_image_path, caption=image_caption)

        with text_col:
            st.markdown(import_md_text(markdown_name))

        if picture_orientation == 'full':
            st.image(profile_image_path, caption=image_caption)
            st.markdown(import_md_text(markdown_name))

    return
