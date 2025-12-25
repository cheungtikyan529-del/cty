import streamlit as st
import openai
import random
#@_@
#@cheungtikyan529-del
type_input = 0
the_name =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
custom_dict_en ={}
custom_dict_la = {}
文字 = ["「Password」 連續多年蟬聯最爛密碼榜首：根據密碼管理軟體公司的年度報告,「123456」 和 「password」 是全球被使用最頻繁且最易被破解的密碼。","美國核彈發射密碼曾長期設為「00000000」：在冷戰時期的 20 年間（1962-1977 年），為了確保在緊急情況下能迅速發射，美國民兵核飛彈的啟動代碼被設為極為簡單的 8 個零。","增加長度比增加複雜性更有效：一個 12 位元的純小寫字母密碼（如 correcthorse）通常比一個 8 位元的複雜密碼（如 P@ssw0rd）更難被暴力破解，因為長度指數級地增加了計算組合數。","密碼發明者的初衷是為了隱私而非安全：計算機科學家 Fernando Corbató 於 1960 年在 MIT 引入了密碼概念，最初是為了讓多個研究員在共用一台大型計算機時，能保護各自的文件不被他人看到。","定期強制更改密碼反而不安全：許多安全機構（如 NIST）現在建議，除非有證據表明密碼已洩露，否則不要強制使用者定期更改密碼。因為強制變更會導致使用者傾向於使用簡單的遞增規律（如 Password123 改為 Password124）。",
"生物辨識密碼無法更改：雖然指紋和人臉辨識很方便，但它們被視為「不可更改的密碼」。一旦你的生物特徵資料洩露，你無法像修改數位密碼那樣修改自己的指紋。","“哈希值”才是服务器真正存储的东西：负责任的网站不会直接存储你的明文密码，而是存储经过哈希算法（如 SHA-256）处理后的乱码。即使数据库泄露，黑客也无法直接看到你的原始密码。"
]#冷知识（文字）
# ==============================================================================#
def save(text):#储存自定义密码
	if len(text) != len(the_name):
		st.error(f"你需要輸入至少{len(the_name)}個字!!!")
	else:
		list(text)
		type_input = 1
		for i in range(len(text)):
			custom_dict_en[text[i]] = the_name[i]
			i+=1
		for i in range(len(text)):
			custom_dict_la[text[i]] = the_name[i]
			i +=1
# ==============================================================================#
def run(ask):#用来问和调用ai
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
	return result
# ==============================================================================#
def loading():#纯是动画
	progress_bar = st.empty()
	for i in range(51):
		progress_bar.progress(i/50, "进度")
		time.sleep(0.05)
# ==============================================================================#
i = a = 0
def asking():#输入文字给ai
	global a
	if a == 0:
		if st.button("問AI關於密碼的問題~"):
			a = 1
			st.info("testing")
	if a == 1:
		if st.button("關閉視窗"):
			a = 0
# ==============================================================================#
def custom():#自定义密码的开关视窗
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
def surprise(text):#冷知识
	if text == 1:
		return run("给我1个关于密码的冷知识(不要事情背景,要尽可能简略,)")
	else:
		return random.choice(文字)
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
def la_to_english(text):#转换
	result = ""
	for char in text:
		if type_input == 0:
		# 存在對應符號就替換，否則保留原字符
			result += en_language.get(char, char)
		else:
			result += custom_dict_en.get(char,char)
	return result
# ==============================================================================#
def english_to_la(text):#转换
	result = ""
	for char in text:
		if text_input == 0:
		# 存在對應符號就替換，否則保留原字符
			result += la_language.get(char, char)
		else:
			result += custom_dict_la.get(char,char)

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
st.title(f"冷知识:\n{surprise(random.randint(1,25))}")