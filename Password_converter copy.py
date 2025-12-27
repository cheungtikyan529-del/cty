import streamlit as st
import openai
import random
import streamlit as st
import time
# 在侧边栏添加标题
st.sidebar.title("这是侧边栏标题")

# 在侧边栏添加输入框
user_name = st.sidebar.text_input("请输入姓名")

# 在侧边栏添加下拉框
option = st.sidebar.selectbox(
    "请选择一个选项",
    ("选项 A", "选项 B", "选项 C")
)

# 主页面内容
st.write(f"你好，{user_name}！你选择了：{option}")

change_icon = "🛠"
st.subheader(f"密碼轉換器{change_icon}")
# ========== 关键修改：使用 Streamlit Session State 保存状态 ==========
# 初始化会话状态（替代全局变量，解决页面刷新后状态丢失问题）
if 'custom_mode' not in st.session_state:
    st.session_state.custom_mode = 0  # 0=关闭自定义窗口，1=打开
if 'type_input' not in st.session_state:
    st.session_state.type_input = 0    # 0=默认转换，1=自定义转换
if 'ai_mode' not in st.session_state:
    st.session_state.ai_mode = 0       # 0=关闭AI窗口，1=打开

# 全局配置（和之前一致，省略重复部分）
the_name = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
que = ["密碼有多長的歷史？","密碼最好要有那些符號？","密碼學是什麼？","密碼最好要多長？","給我一個關於密碼歷史的冷知識。"]
文字 = [
    "「Password」 連續多年蟬聯最爛密碼榜首：根據密碼管理軟體公司的年度報告,「123456」 和 「password」 是全球被使用最頻繁且最易被破解的密碼。",
    "美國核彈發射密碼曾長期設為「00000000」：在冷戰時期的 20 年間（1962-1977 年），為了確保在緊急情況下能迅速發射，美國民兵核飛彈的啟動代碼被設為極為簡單的 8 個零。",
    "增加長度比增加複雜性更有效：一個 12 位元的純小寫字母密碼（如 correcthorse）通常比一個 8 位元的複雜密碼（如 P@ssw0rd）更難被暴力破解，因為長度指數級地增加了計算組合數。",
    "密碼發明者的初衷是為了隱私而非安全：計算機科學家 Fernando Corbató 於 1960 年在 MIT 引入了密碼概念，最初是為了讓多個研究員在共用一台大型計算機時，能保護各自的文件不被他人看到。",
    "定期強制更改密碼反而不安全：許多安全機構（如 NIST）現在建議，除非有證據表明密碼已洩露，否則不要強制使用者定期更改密碼。因為強制變更會導致使用者傾向於使用簡單的遞增規律（如 Password123 改為 Password124）。",
    "生物辨識密碼無法更改：雖然指紋和人臉辨識很方便，但它們被視為「不可更改的密碼」。一旦你的生物特徵資料洩露，你無法像修改數位密碼那樣修改自己的指紋。",
    "“哈希值”才是服务器真正存储的东西：负责任的网站不会直接存储你的明文密码，而是存储经过哈希算法（如 SHA-256）处理后的乱码。即使数据库泄露，黑客也无法直接看到你的原始密码。"
]
# ========== 修复：保存自定义密码（使用会话状态） ==========
def save(text):
    if len(text) != len(the_name):
        st.error(f"你需要輸入{len(the_name)}個字（當前輸入：{len(text)}）!!!")
    else:
        text_list = list(text)
        st.session_state.type_input = 1  # 切换为自定义转换模式
        # 清空旧的自定义字典（避免残留）
        st.session_state.custom_dict_en.clear()
        st.session_state.custom_dict_la.clear()
        # 建立自定义映射
        for char, code in zip(text_list, the_name):
            st.session_state.custom_dict_en[code] = char  # 密文→明文：自定义符号→原字符
            st.session_state.custom_dict_la[char] = code  # 明文→密文：原字符→自定义符号
        st.success("自定义密码映射已保存！当前为【自定义转换模式】")

# ========== 修复：自定义密码窗口（使用Session State） ==========
def custom():
    # 按钮1：打开自定义窗口
    if st.session_state.custom_mode == 0:
        if st.button("自訂密碼", key="open_custom"):
            st.session_state.custom_mode = 1  # 切换状态
            st.rerun()  # 强制刷新页面，立即显示输入框
    # 按钮2：关闭自定义窗口 + 输入框
    else:
        user_input = st.text_area(
            label=f'请输入{len(the_name)}個字的自定义密码（用于映射）：',
            value='',
            height=150,
            max_chars=len(the_name),
            help=f'必须输入{len(the_name)}个字符（当前the_name长度：{len(the_name)}）',
            key="custom_input"
        )
        col1, col2 = st.columns(2)
        with col1:
            if st.button("保存自定义密码", key="save_custom"):
                save(user_input)
        with col2:
            if st.button("關閉自訂視窗", key="close_custom"):
                st.session_state.custom_mode = 0  # 切换状态
                st.rerun()  # 强制刷新页面，关闭输入框

# ========== 其他函数（和之前一致，仅适配Session State） ==========
def run(ask):
    client = openai.OpenAI(
        api_key = "Q5vslq7a8w3gP605eAMxnH6Ec0lSO3-0_34N0i2rfGI",
        base_url = "https://api.poe.com/v1",
    )
    try:
        chat = client.chat.completions.create(
            model = "gemini-3-flash",
            messages = [{"role": "user", "content": ask}]
        )
        return chat.choices[0].message.content
    except Exception as e:
        st.error(f"AI调用失败：{str(e)}")
        return "請檢查API Key或網絡連接"

def loading():
    progress_bar = st.empty()
    for i in range(21):
        progress_bar.progress(i/20, "进度")
        time.sleep(0.05)
    progress_bar.empty()

# ========== 修复：AI提问窗口（同样使用Session State） ==========
def asking():
    if st.session_state.ai_mode == 0:
        if st.button("問AI關於密碼的問題~", key="open_ai"):
            st.session_state.ai_mode = 1
            st.rerun()
    else:
        url = "https://qph.cf2.poecdn.net/main-thumb-pb-6023-200-tmjxdrusvxhxxlsabsspmpthsjrtedpq.jpeg"
        st.image(
            "https://qph.cf2.poecdn.net/main-thumb-pb-6023-200-tmjxdrusvxhxxlsabsspmpthsjrtedpq.jpeg",
            width=50,
            caption="调用的ai"
        )
        user = st.text_area(
            label='試問一下:',
            value=random.choice(que),
            height=150,
            max_chars=350,
            help='最大长度限制为350字',
            key="ai_input"
        )
        col1, col2 = st.columns(2)
        with col1:
            if st.button("提問！", key="ask_ai"):
                loading()
                st.write(run(user))
        with col2:
            if st.button("關閉視窗", key="close_ai"):
                st.session_state.ai_mode = 0
                st.rerun()

def surprise(*args):
    return random.choice(文字)

# ========== 转换字典（和之前一致） ==========
en_language ={
    '△ ': 'a', 'ɔ': 'b', 'c': 'c', 'ㄹ': 'd', '-': 'e',
    '丨': 'f', '乛': 'g', 'ㅂ': 'h', ',': 'i', '/': 'j',
    '<': 'k', '∠': 'l', 'θ': 'm', '^': 'n', '⊙': 'o',
    'ㄴ': 'p', '∅': 'q', '∧': 'r', '~': 's', '∟': 't',
    'u': 'u', 'v': 'v',"=":"w", '∂': 'x', 'ㅍ': 'y', 'ㅠ': 'z',
    'i': '!', 'a': '@', './': '#',';': ':', '_': ' ', '.': ',', "'": '.',
    '!': '1',"'":'"', '"':"'", '@': '2', '#': '3', '$': '4', '%': '5', 
    '&': '7', '*': '8', '(': '9', ')': '0'
}
la_language = {
    'A': '△ ', 'B': 'ɔ', 'C': 'c', 'D': 'ㄹ', 'E': '-',
    'F': '丨', 'G': '乛', 'H': 'ㅂ', 'I': ',', 'J': '/',
    'K': '<', 'L': '∠', 'M': 'θ', 'N': '\\', 'O': '⊙',
    'P': 'ㄴ', 'Q': '∅', 'R': '∧', 'S': '~', 'T': '∟',
    'U': 'u', 'V': 'v', 'W': '=', 'X': '∂', 'Y': 'ㅍ', 'Z': 'ㅠ',
    'a': '△', 'b': 'ɔ', 'c': 'c', 'd': 'ㄹ', 'e': '-',
    'f': '丨', 'g': '乛', 'h': 'ㅂ', 'i': ',', 'j': '/',
    'k': '<', 'l': '∠', 'm': 'θ', 'n': '^', 'o': '⊙',
    'p': 'ㄴ', 'q': '∅', 'r': '∧', 's': '~', 't': '∟',
    'u': 'u', 'v': 'v', 'w': '=', 'x': '∂', 'y': 'ㅍ', 'z':'ㅠ',
    "!":"i", "@":"a", "#":"./", "$":"&", ":":";", " ":"_",
    ",":".", ".":"'", "'":'"', '"':"'", "1":"!","2":"@","3":"#",
    "4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")"
}
# ========== 转换函数（适配Session State） ==========
def la_to_english(text):
    result = ""
    for char in text:
        if st.session_state.type_input == 0:
            result += en_language.get(char, char)
        else:
            result += st.session_state.custom_dict_en.get(char, char)
    return result

def english_to_la(text):
    result = ""
    for char in text:
        if st.session_state.type_input == 0:
            result += la_language.get(char, char)
        else:
            result += st.session_state.custom_dict_la.get(char, char)
    return result

# ========== 页面主逻辑 ==========
# 初始化会话状态的字典（避免KeyError）
if 'custom_dict_en' not in st.session_state:
    st.session_state.custom_dict_en = {}
if 'custom_dict_la' not in st.session_state:
    st.session_state.custom_dict_la = {}

#页面样式
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

# 冷知识展示
st.divider()
st.subheader("冷知識：")
st.write(surprise())
st.write("========================================================================================\n")

# 页面布局
col1, col2, col3 = st.columns([9, 11, 5])

with col3:
    st.subheader("自定义设置")
    custom()  # 现在可以正常打开/关闭自定义窗口
with col2:
    # 转换模式选择
    choice = st.selectbox(
        label = "選擇轉換方式:",
        options = ('明文->密文','明文<-密文'),
    )
    type_ = 0 if choice == "明文->密文" else 1
    
    # 输入框+转换按钮
    test_text = st.text_input("請輸入需要轉換的文字：", placeholder="例如：password123 或 △,⊙⊙∟∟∟i123")
    if st.button("运行转换"):
        change_icon = "💡"
        if not test_text.strip():
            st.info("⚠️ 你需要输入一些文字！")
        else:
            loading()
            if type_ == 0:
                result = english_to_la(test_text)
                st.success(f"原文：{test_text}\n轉換後（密文）：{result}")
            else:
                result = la_to_english(test_text)
                st.success(f"原文（密文）：{test_text}\n轉換後（明文）：{result}")
#标题设置
st.set_page_config(
    page_title="密碼轉換器~",
    page_icon=f"{change_icon}",
    layout="wide"
)
# AI提问模块
st.divider()
asking()