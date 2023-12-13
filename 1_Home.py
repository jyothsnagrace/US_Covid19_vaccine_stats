import streamlit as st

APP_TITLE = 'COVID-19 Vaccinations in the United States'
APP_SUB_TITLE = 'Source: COVID-19 Case Surveillance Public Use Data with Geography'



def main():

    ### Page Config
    st.set_page_config(page_title=APP_TITLE, page_icon=":mask", layout="wide")
    st.markdown("""
        <style>
            .st-emotion-cache-zt5igj {
                color: teal;
                padding-top: 15px;
                padding-bottom: 15px;
            }
        </style>""", unsafe_allow_html=True)
    st.title(f":microbe: {APP_TITLE} :mask:")
    # st.caption(APP_SUB_TITLE)
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    
    with open('lib/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
        :gray[A Streamlit App to visualize and analyze USA Covid-19 Vaccination stats]
        * :gray[**Libraries Used:** Streamlit, Pandas, Plotly]
        * :gray[**Data Source:** CDC]
        ''')


    with col2:
        # st.caption("Author: Leela Josna Kona")
        st.markdown('<div style="text-align: right;color:gray";>Author: Leela Josna Kona</div>', unsafe_allow_html=True)
        


    with st.container():
        st.image('data/banner.jpg', caption="Image by Leela Josna Kona")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)


if __name__ == "__main__":
    main()