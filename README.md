 AI 智能助手
 一个使用 Streamlit 和 大模型 AI 构建的智能对话助手应用。

✨ 功能特性

- 🤖 AI 智能对话：可集成各类大模型，提供自然流畅的对话体验
- 🎭 性化设置：可自定义 AI 助手的昵称和性格特征
- 💾 会话管理：支持创建、保存和加载历史会话
- 🎨 美观界面：基于 Streamlit 的现代化 Web 界面
- 📱 响应式布局：适配不同设备的显示需求

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Streamlit
- OpenAI Python SDK

### 安装步骤

1. **克隆项目**
```
bash
git clone <your-repo-url>
cd 小胡智能伴侣
```
2. **安装依赖**
```
bash
pip install streamlit openai
```
3. **配置 API Key**

创建 `.env` 文件并设置 DeepSeek API Key：
```
bash
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```
或者在命令行中设置环境变量：

**Windows (PowerShell):**
```
powershell
$env:DEEPSEEK_API_KEY="your_deepseek_api_key_here"
```
**Windows (CMD):**
```
cmd
set DEEPSEEK_API_KEY=your_deepseek_api_key_here
```
**Linux/Mac:**
```
bash
export DEEPSEEK_API_KEY="your_deepseek_api_key_here"
```
4. **运行应用**
```
bash
streamlit run 小胡智能伴侣/AI伴侣.py
```
5. **访问应用**

打开浏览器访问：`http://localhost:8501`

## 📖 使用说明

### 基本对话
- 在底部输入框输入消息，按回车发送
- AI 会自动回复你的消息

### 自定义 AI 助手
1. 在左侧边栏的"AI 助手信息设置"区域
2. 输入你想要的昵称（如："小明"、"智慧助手"等）
3. 输入性格描述（如："活泼开朗"、"温柔体贴"、"专业严谨"等）

### 会话管理
- **新建会话**：点击侧边栏的"新建会话"按钮
- **加载历史**：在"历史会话"区域点击会话名称
- **删除会话**：点击会话旁边的 ❌ 按钮

## 📁 项目结构

```

小胡智能伴侣/
├── AI伴侣.py              # 主程序文件
├── Page_resource/         # 页面资源（图片等）
│   ├── LOGO.png
│   └── AI (1).png
└── sessions/              # 会话数据目录（自动创建）
    └── *.json            # 保存的会话记录
```
## ⚙️ 配置说明

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | 是 |

### 获取 DeepSeek API Key

1. 访问 [DeepSeek 开放平台](https://platform.deepseek.com/)
2. 注册/登录账户
3. 在 API Keys 页面创建新的密钥
4. 复制密钥并设置到环境变量中

## 🔒 隐私与安全

- API Key 通过环境变量管理，不会被提交到代码仓库
- 建议将 `sessions/` 目录添加到 `.gitignore`，避免泄露聊天数据
- 不要在公共网络环境中使用敏感的个人信息

## 🛠️ 技术栈

- **前端框架**: Streamlit
- **AI 服务**: DeepSeek Chat API
- **编程语言**: Python 3.8+
- **数据持久化**: JSON 本地存储

## 📝 更新日志

### v1.0.0
- 初始版本发布
- 实现基础对话功能
- 支持会话管理
- 支持 AI 人格自定义

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👤 作者

如有问题或建议，欢迎通过 GitHub Issues 联系。

**注意**: 使用本项目需要有效的 DeepSeek API Key，请确保遵守 DeepSeek 的使用条款和服务协议。
