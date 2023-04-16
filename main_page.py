import streamlit as st
import pandas as pd

view = [100,150,30]
st.write('# youtube view') # markdown
st.write('## raw')
view
st.write('## bar chart')

st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview