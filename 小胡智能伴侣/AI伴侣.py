import streamlit as st
import os
import json
from openai import OpenAI
from datetime import datetime
#logo
st.logo("小胡智能伴侣/Page_resource/LOGO.png",size="large")
#大标题
st.title("基于Streamlit的AI智能助手")

#页面设置
st.set_page_config(
    page_title="AI Chat",         #网站名称
    page_icon="🦀",               #网站图标
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        #'Report a bug': "https://www.deepseek.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#AI人格设置
system_prompt = """
        你叫%s，现在是用户的全能助手。：
        规则：
            1. 会理解用户的语言
            2. 回复细致周全
            3. 有需要的话可以用❤️等emoji表情
            4. 用符合助理性格的方式对话
            5. 回复的内容, 要充分体现助手的性格特征
        助手性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """


def save_session():
    session_data = {
        "nick_name": st.session_state.nick_name,
        "character": st.session_state.character,
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages
    }
    # 如果文件目录不存在，则创建
    if not os.path.exists("./小胡智能伴侣/sessions"):
        os.mkdir("./小胡智能伴侣/sessions")
    # 保存会话数据
    with open(f"./小胡智能伴侣/sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

def history_sessions(): #历史会话列表展示
    session_list = []
    if os.path.exists("./小胡智能伴侣/sessions"):
        file_list = os.listdir("./小胡智能伴侣/sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
                session_list.sort(reverse=True)   #新的会话会在上面
    return session_list

def load_session(session_name):   #加载指定会话
    try:
        if os.path.exists(f"./小胡智能伴侣/sessions/{session_name}.json"):
            with open(f"./小胡智能伴侣/sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.character = session_data["character"]
                st.session_state.current_session = session_data["current_session"]
                st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("加载会话信息失败！")


def del_session(session_name):   #删除指定会话
    try:
        if os.path.exists(f"./小胡智能伴侣/sessions/{session_name}.json"):
            os.remove(f"./小胡智能伴侣/sessions/{session_name}.json")
            #如果是删除当前会话，则清空消息列表
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                st.session_state.toast_message = f"会话:{session_name}已删除。"
    except Exception:
        st.error("删除会话信息失败！")

#初始化聊天记忆
if 'messages' not in st.session_state:
    st.session_state.messages =[]
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "大螃蟹"       #默认的昵称
if 'character' not in st.session_state:
    st.session_state.character = "活泼开朗的百事通" #默认的性格
if 'current_session' not in st.session_state:
    st.session_state.current_session =datetime.now().strftime("%Y-%m-%d-%H-%M-%S") #默认的会话标识

#从cache读回所有聊天记录
st.text(f"当前会话名称:{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

#侧边栏设置
with st.sidebar:                     #with语句（上下文管理器）确保资源总是被正确获取和释放，即使发生异常，也会被正确释放。
    st.subheader("AI控制面板")
    if st.button("新建会话",width="stretch",icon="✍️") and st.session_state.messages:  #如果聊天记录为空，则不会新建会话
        #1.保存当前会话
        save_session()
        #2.创建新会话
        st.session_state.messages=[]
        st.session_state.current_session =datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # 3. 设置提示消息（在刷新后显示）
        st.session_state.toast_message = f"新会话已创建：{st.session_state.current_session}"
        st.rerun()   #重新运行当前页面
    if 'toast_message' in st.session_state:
        st.toast(st.session_state.toast_message, icon="🥳")
        del st.session_state.toast_message


    #历史会话
    st.subheader("历史会话")
    session_list = history_sessions()
    for session in session_list:
        co1,co2=st.columns([4,1])
        with co1:
            #加载会话信息
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if session==st.session_state.current_session else "secondary"): #三元运算符 语法：值1 if 条件 else 值2
                load_session(session)   #调用load_session函数
                st.rerun()
        with co2:
            #删除该会话
            if st.button("",width="stretch",icon="❌️",key=f"delete_{session}"):
                del_session(session)     #调用del_session函数
                st.rerun()
    #分割线
    st.divider()

    st.subheader("AI助手信息设置")
    nick_name =st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)         #昵称设定输入框
    character=st.text_area("性格",placeholder="请输入性格",value=st.session_state.character)           #性格设定输入框
    if nick_name:
        st.session_state.nick_name = nick_name
    if character:
        st.session_state.character = character


#大模型客服端设置
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")





#聊天框
user_prompt = st.chat_input("Say something")
if user_prompt:
    st.chat_message("user").write(user_prompt)           #用户聊天框
    st.session_state.messages.append({"role": "user", "content": user_prompt}) #cache缓存用户输入
    print("---------->调用AI大模型，提示词：",user_prompt)  #后端相应提示
    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt %(st.session_state.nick_name,st.session_state.character)},
            *st.session_state.messages,
        ],
        stream=True
    )
    print(f"===========> 当前昵称：{st.session_state.nick_name}, 性格：{st.session_state.character}")
    print(f"===========> System Prompt: {system_prompt % (st.session_state.nick_name, st.session_state.character)}")

    #大模型返回结果的输出（流式输出方式）
    response_message=st.empty ()
    full_response=''
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content=chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response}) #cache缓存机器人输入


                              #大模型返回结果的输出（非流式输出方式）
    #print("---------->大模型的回复为：",response.choices[0].message.content)  #后端相应提示
    #st.chat_message("assistant").write(response.choices[0].message.content)  # 机器人聊天框
    #st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content}) #cache缓存机器人输入

    save_session() #最后保存信息
    st.rerun()