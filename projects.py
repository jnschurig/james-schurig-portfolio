import streamlit as st 
import general as gen
import os

def display_progress(project_name:str, status_val:str, color:str='normal', super_title:str=''):
    if color not in ["normal", "inverse", "off"]:
        return

    st.metric(
        label=super_title,
        value=project_name,
        delta=status_val,
        delta_color=color
    )

    return

def show_project(
        project_name:str, 
        status_val:str, 
        color:str='normal', 
        super_title:str='', 
        markdown_file:str=None, 
        image_file=None,
        image_caption:str=None,
        supplemental_text:str=None
    ):
    st.divider()
    display_progress(project_name, status_val, color, super_title)

    if markdown_file is not None:
        st.markdown(gen.import_md_text(markdown_file))

    if supplemental_text is not None:
        st.markdown(supplemental_text)

    if image_file is not None:
        if type(image_file) is not list:
            image_file = [image_file]

        for image in image_file:
            st.image(os.path.join('images', image), image_caption)

    return 

def go():
    st.markdown(gen.import_md_text('projects_intro.md'))

    show_project(
        project_name='Enkibot Prime ST',
        status_val='0.2.2 Available. In Active Development',
        markdown_file='enkibot.md',
        image_file='enkibot_example.png',
        image_caption='Enkibot Hint Generator'
    )

    show_project(
        project_name='Snowflake Assistant',
        status_val='1.0 Complete',
        markdown_file='snowflake_assistant.md',
        image_file=None,
        image_caption='Warehouses and Tags'
    )

    show_project(
        project_name='OCRemix Manager',
        status_val='1.0 Complete',
        markdown_file='ocremix_manager.md',
        image_file=['remix_manager_sample.png', 'remix_manager_dl.png'],
    )

    show_project(
        project_name='RandoBlazer Generator Sim',
        status_val='Postponed',
        color='inverse',
        markdown_file='randoblazer.md',
        image_file='randoblazer_gen_sim.png',
    )

    show_project(
        project_name='James Schurig Portfolio',
        status_val='1.0 Complete',
        supplemental_text='''
        Wait, isn't this the app I'm viewing right now?

        _Yes, it certainly is. Check out the source code._

        * [Github Repository](https://github.com/jnschurig/james-schurig-portfolio)
        '''
    )

    return 

if __name__ == '__main__':
    st.set_page_config(
        page_title='Projects',
        page_icon='🧑‍💻',
        layout='centered',
        initial_sidebar_state='auto'
    )
    go()