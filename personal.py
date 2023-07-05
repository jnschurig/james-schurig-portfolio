import streamlit as st 
import general as gen

def go():
    st.markdown(gen.import_md_text('personal.md'))

    gen.show_picture_section(
        'timpanogos.jpg', 
        'timpanogos.md', 
        'Timpanogos Summit and the Mysterious Shack Thereon', 
        [3, 2]
    )

    gen.show_picture_section(
        'petit_suisse.jpg', 
        'cheesemaking.md', 
        'Petit Suisse Made and Eaten by Me', 
        [3, 2], 
        picture_orientation='right'
    )

    gen.show_picture_section(
        'tomatoes.jpg', 
        'gardening.md', 
        '2023, The Year of Tomatoes', 
        [1, 3], 
        picture_orientation='left'
    )

    with st.container():
        st.divider()

        text_col, image_col = st.columns([3, 1])
        
        with text_col:
            st.markdown(gen.import_md_text('gaming.md'))

        with image_col:
            st.image(
                'https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg',
                caption='Zelda: A Link to my Past'
                )


    return 

if __name__ == '__main__':
    st.set_page_config(
        page_title='Personal',
        page_icon='🏔️',
        layout='centered',
        initial_sidebar_state='auto'
    )
    go()