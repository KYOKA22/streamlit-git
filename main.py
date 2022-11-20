import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit 入門')

st.write('プログレスバー')
'Start'

latest_iteration =st.empty()
bar =st.progress(0.0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.2)

'Done'

st.write('DataFrame')

df =pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.dataframe(df,width=500)

st.write('TABLE')
st.table(df)

st.write('マジックコマンド')
"""
# 章
## 節
### 項
#の後には空白を入れる

```python
import streamlit as st
import numpy as np
import pandas as pd
```
「'」ではなく「`」
"""

st.write('MAP')
df2 =pd.DataFrame(
    np.random.rand(100,2)/[50,50]+(35.69,139.70),
    columns=['lat','lon']
)
st.map(df2)
st.bar_chart(df2)


st.write('IMAGE')
if st.checkbox('Show Image'):
    img=Image.open('cow.png')
    st.image(img,caption='cow',use_column_width=True)
"""
use_column_width=True
ディスプレイのサイズに合わせる
"""

st.sidebar.write('インタラクティブウィジェット')
option=st.selectbox(
    '好きな数字は?',
    options=list(range(1,11))
)
'好きな数字は',option,'です'

#option2=st.sidebar.text_input(
option2=st.text_input('your hobby?')
'your hobby is',option2

option3 = st.slider('How old are you?', 0, 100, 25)
#option3 = st.sidebar.slider('How old are you?', 0, 100, 25)
'your old is',option3



left_column,right_columns=st.columns(2)
button=left_column.button('右からむに表示')
if button:
    right_columns.write('右からむ')

sxpander=st.expander('問い合わせ')
sxpander.write('問い合わせの回答')






