import streamlit as st

la_language = {
	'A': '△ ', 'B': 'ɔ', 'C': 'c', 'D': 'ㄹ', 'E': '-',
	'F': '丨', 'G': '乛', 'H': 'ㅂ', 'I': ',', 'J': '/',
	'K': '<', 'L': '∠', 'M': 'θ', 'N': '^', 'O': '⊙',
	'P': 'ㄴ', 'Q': '∅', 'R': '∧', 'S': '~', 'T': '∟',
	'U': 'u', 'V': 'v', 'W': '^', 'X': '∂', 'Y': 'ㅍ',
	'Z': 'ㅠ',#大写
    'a': '△', 'b': 'ɔ', 'c': 'c', 'd': 'ㄹ', 'e': '-',
	'f': '丨', 'g': '乛', 'h': 'ㅂ', 'i': ',', 'j': '/',
	'k': '<', 'l': '∠', 'm': 'θ', 'n': '^', 'o': '⊙',
	'p': 'ㄴ', 'q': '∅', 'r': '∧', 's': '~', 't': '∟',
	'u': 'u', 'v': 'v', 'w': '^', 'x': '∂', 'y': 'ㅍ',
	'z':'ㅠ',#小写
	"!":"i", "@":"a", "#":"./", "$":"&", ":":";", " ":"_",
	",":".", ".":"'"#符号
}
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([1, 11, 1])
#位置分配总共13个
# 文字轉換函數
def english_to_la(text):
	result = ""
	for char in text:
		# 存在對應符號就替換，否則保留原字符
		result += la_language.get(char, char)
	return result

# 測試範例
with col2:
	st.title("Password converter")	  
	if __name__ == "__main__":
		test_text = str(st.text_input("please input"))
		if st.button("change"):
			st.write(f"原文：{test_text}")
			st.write(f"轉換後：{str(english_to_la(test_text))}")
