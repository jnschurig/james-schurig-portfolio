import streamlit as st 
import general as gen

def go():
    gen.show_picture_section(
        image_name='snowpro_core.png', 
        markdown_name='snowpro_core.md', 
        column_spacing=[1, 7],
        picture_orientation='left'
    )

    st.divider()
    st.markdown(gen.import_md_text('professional_intro.md'))

    gen.show_picture_section(
        image_name='verisk_logo.jpg',
        markdown_name='verisk.md',
        # image_caption='Clip: Sep 2019 - Jan 2021',
        column_spacing=[1, 6],
        picture_orientation='left',
        section_title='##### Xactware/Verisk: Jul 2014 - Sep 2019'
    )

    gen.show_picture_section(
        image_name='clip_logo.png',
        markdown_name='clip.md',
        # image_caption='Clip: Sep 2019 - Jan 2021',
        column_spacing=[1, 6],
        picture_orientation='left',
        section_title='##### Clip: Sep 2019 - Jan 2021'
    )

    gen.show_picture_section(
        image_name='ipipeline_logo.jpg',
        markdown_name='ipipeline.md',
        # image_caption='iPipeline: Jan 2021 - Jun 2023',
        column_spacing=[1, 6],
        picture_orientation='left',
        section_title='##### iPipeline: Jan 2021 - Jun 2023'
    )

    return 

if __name__ == '__main__':
    st.set_page_config(
        page_title='Professional',
        page_icon='🧑‍💻',
        layout='centered',
        initial_sidebar_state='auto'
    )
    go()