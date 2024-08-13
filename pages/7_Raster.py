import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "https://github.com/fener95/tiffs-repo/raw/main/img23_true_color.tif"
        after = "https://github.com/fener95/tiffs-repo/raw/main/img24_true_color.tif"
        m.split_map(
            left_layer=before, right_layer=after, left_label = "one day July 2023", right_label="one day july 2024",
        )

m.to_streamlit(height=700)
