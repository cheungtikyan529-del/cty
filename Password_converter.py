import streamlit as st
import openai
import time
#@_@
#cheungtikyan529-del
the_name =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
custom_dict ={}
def save(text):
	if len(text) != len(the_name):
		st.error(f"你需要輸入至少{len(the_name)}個字!!!")
	else:
		for i in range(len(text)):
			pass


# ==============================================================================#
def run(ask):
	client = openai.OpenAI(
	api_key = "Q5vslq7a8w3gP605eAMxnH6Ec0lSO3-0_34N0i2rfGI",  # or os.getenv("POE_API_KEY")
	base_url = "https://api.poe.com/v1",
	)
	chat = client.chat.completions.create(
	model = "gemini-3-flash",
	messages = [{
	"role": "user",
	"content": ask
	}]
	)
	result = chat.choices[0].message.content
# ==============================================================================#
def loading():
	progress_bar = st.empty()
	for i in range(51):
		progress_bar.progress(i/50, "进度")
		time.sleep(0.05)
# ==============================================================================#
i = a = 0
def asking():
	global a
	if a == 0:
		if st.button("問AI關於密碼的問題~"):
			a = 1
			st.info("testing")
	if a == 1:
		if st.button("關閉視窗"):
			a = 0
# ==============================================================================#
def custom():
	global i
	if i == 0:
		if st.button("自訂密碼"):
			i = 1
			user_input = st.text_area(
			label='请输入您自订的密码：',
			value='',
			height=150,
			max_chars=500,
			help='最大长度限制为500字'
			)
			if st.button("save"):
				st.write(list(user_input))

	if i == 1:
		if st.button("關閉視窗"):
			i = 0
# ==============================================================================#
type_ = 0
en_language ={
    '△ ': 'a', 'ɔ': 'b', 'c': 'c', 'ㄹ': 'd', '-': 'e',
    '丨': 'f', '乛': 'g', 'ㅂ': 'h', ',': 'i', '/': 'j',
    '<': 'k', '∠': 'l', 'θ': 'm', '^': 'n', '⊙': 'o',
    'ㄴ': 'p', '∅': 'q', '∧': 'r', '~': 's', '∟': 't',
    'u': 'u', 'v': 'v',"=":"w", '∂': 'x', 'ㅍ': 'y', 'ㅠ': 'z',
    'i': '!', 'a': '@', './': '#',';': ':', '_': ' ', '.': ',', "'": '.',
     '!': '1',"'":'"', '"':"'",
    '@': '2', '#': '3', '$': '4', '%': '5', '&': '7', '*': '8',
    '(': '9', ')': '0'
}
# ==============================================================================#
la_language = {
	'A': '△ ', 'B': 'ɔ', 'C': 'c', 'D': 'ㄹ', 'E': '-',
	'F': '丨', 'G': '乛', 'H': 'ㅂ', 'I': ',', 'J': '/',
	'K': '<', 'L': '∠', 'M': 'θ', 'N': '\\', 'O': '⊙',
	'P': 'ㄴ', 'Q': '∅', 'R': '∧', 'S': '~', 'T': '∟',
	'U': 'u', 'V': 'v', 'W': '=', 'X': '∂', 'Y': 'ㅍ',
	'Z': 'ㅠ',#大写
    'a': '△', 'b': 'ɔ', 'c': 'c', 'd': 'ㄹ', 'e': '-',
	'f': '丨', 'g': '乛', 'h': 'ㅂ', 'i': ',', 'j': '/',
	'k': '<', 'l': '∠', 'm': 'θ', 'n': '^', 'o': '⊙',
	'p': 'ㄴ', 'q': '∅', 'r': '∧', 's': '~', 't': '∟',
	'u': 'u', 'v': 'v', 'w': '=', 'x': '∂', 'y': 'ㅍ',
	'z':'ㅠ',#小写
	"!":"i", "@":"a", "#":"./", "$":"&", ":":";", " ":"_",
	",":".", ".":"'", "'":'"', '"':"'"#符号
	,"1":"!","2":"@","3":"#","4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")"
}
# ==============================================================================#
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
col2, col3 = st.columns([11, 5])
with col3:
	custom()
# ==============================================================================#
#位置分配总共13个
# 文字轉換函數
# ==============================================================================#
def la_to_english(text):
	result = ""
	for char in text:
		# 存在對應符號就替換，否則保留原字符
		result += en_language.get(char, char)
	return result
# ==============================================================================#
def english_to_la(text):
	result = ""
	for char in text:
		# 存在對應符號就替換，否則保留原字符
		result += la_language.get(char, char)
	return result
# ==============================================================================#
# 測試範例
# ==============================================================================#
with col2:
	st.title("密碼轉換器")
	choice = st.selectbox(
	label = "選擇轉換方式:",
	options = ('明文->密文','明文<-密文'),
	)
	if choice == "明文->密文":
		type_ = 0
	else:
		type_ = 1

	if __name__ == "__main__":
		test_text = str(st.text_input("请输入:"))
		if st.button("运行"):
			if not test_text.strip():
				st.info("你需要輸入一些文字!")
			else:
				if type_ == 0:
					st.write(f"原文：{test_text}")
					st.write(f"轉換後：{str(english_to_la(test_text))}")
				else:
					st.write(f"原文：{test_text}")
					st.write(f"轉換後:{str(la_to_english(test_text))}")
	
asking()