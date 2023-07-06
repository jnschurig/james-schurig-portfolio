import streamlit as st 
import os
import general as gen
import personal, professional, projects

# This file is intended to be run with Streamlit.
# From the commandline, try `streamlit run ./portfolio_main.py`

def go():
    intro_col, picture_col = st.columns([3, 2])

    intro_tab, professional_tab, projects_tab, personal_tab = st.tabs(['Introduction', 'Professional', 'Projects', 'Personal'])

    with intro_col:
        st.markdown('### Hello!')
        
        st.markdown("### I'm James Schurig")

        st.markdown('''A data architect and engineer focused on building 
        exceptional analytics systems and tooling for developer support.''')

        st.markdown('''
        Socials
        | [Email](mailto:jnschurig@gmail.com)
        | [LinkedIn](https://www.linkedin.com/in/james-schurig/)
        | [Github](https://github.com/jnschurig)
        ''')

    with picture_col:
        profile_image_path = os.path.join('images', 'profile_picture.jpg')
        st.image(profile_image_path)

    with intro_tab:
        st.markdown(gen.import_md_text('intro.md'))

    with personal_tab:
        personal.go()

    with professional_tab:
        professional.go()

    with projects_tab:
        projects.go()

    return 

if __name__ == '__main__':
    st.set_page_config(
        page_title='James Schurig Portfolio',
        page_icon='🧑‍💻',
        layout='centered',
        initial_sidebar_state='auto',
        menu_items={
            'About': gen.import_md_text('about.md')
        }
    )
    go()