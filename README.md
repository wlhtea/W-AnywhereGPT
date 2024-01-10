<div align="center">
  <img src="favicon.ico" alt="W-AnywhereGPT" width="200px" />
</div>

***

# W-AnywhereGPT 应用程序指南

W-AnywhereGPT，一款创新的桌面应用程序，让您能在任何场景下快速利用 ChatGPT 的强大功能。无论是专业术语查询、语言翻译、编程帮助，还是日常生活中的小问题，W-AnywhereGPT 都能助您一臂之力。

***

[https://github.com/wlhtea/W-AnywhereGPT/blob/master/W-AnywhereGPT.mp4](https://github.com/wlhtea/W-AnywhereGPT/assets/115779315/e32af71e-a71c-42e7-a2e6-494f9df4ecb9)

***

## 🚀 核心功能

- **快速生成内容**：通过 GPT 模型，快速生成与剪贴板文本相关的内容。
- **多模式选择**：学术GPT、翻译GPT 和代码GPT，多种模式应对不同需求。
- **系统托盘集成**：简洁的系统托盘集成，便于访问和控制。
- **一键快捷操作**：通过 `Ctrl+C+C` 快捷键，轻松激活应用程序。

## ⚙️ 安装指南

### 直接运行

1. 下载 `W-AnywhereGPT.zip` 文件。
2. 并执行其中./dist/W-AnywhereGPT.exe（如果你觉得不方便可以创建快捷键到桌面或者你喜欢的任何地方）
3. 如果exe用不了，应该是没有额度了，你自己看后面进行配置
4. 在 Windows 系统中运行，程序将自动在系统托盘启动。

### 源代码运行

1. 克隆 GitHub 仓库：
   ```sh
   git clone https://github.com/wlhtea/W-AnywhereGPT.git
   ```
2. 安装依赖：
   ```sh
   pip install -r requirements.txt
   ```
3. 运行程序：
   ```sh
   python main.py
   ```
### 源代码配置说明（更新）

在配置和运行 W-AnywhereGPT 应用程序的源代码时，请按照以下步骤设置 `.env` 文件，以确保应用程序能够正确连接到 OpenAI 的服务器：

1. 将 `.env.example` 文件重命名为 `.env`。
2. 在 `.env` 文件中填写必要的环境变量：

   ```
   API_KEY=Your_api_key
   openai_base_url=openai_base_url(例如openai.api.com -> https://api.openai.com/v1/chat/completions)
   ```

   - **API_KEY**：填入您的 OpenAI API 密钥。
   - **openai_base_url**：根据您的网络环境选择合适的 API 请求地址。
     - 如果您有翻墙软件，使用 OpenAI 官方的请求地址 `https://api.openai.com/v1/chat/completions`。
     - 如果您没有翻墙能力，可以使用我提供的 CDN 加速地址 `https://w-l-h.xyz/ -> https://w-l-h.xyz/v1/chat/completions`（部署在 Cloudflare 上，不进行任何信息处理和拦截，可放心使用）。

3. 如果您没有翻墙软件和 API 密钥，可以访问我的网站 `https://openai.w-l-h.xyz` 注册并获取免费的 OpenAI GPT-3.5 API 使用额度，初始提供 10 美元额度。如需更多额度，可以通过联系我进行购买。

确保这些设置正确，便可顺利运行 W-AnywhereGPT 应用程序，无论您的网络环境如何。(openai_base_url -> https://openai.w-l-h.xyz/v1/chat/completions)


## 📖 使用说明

- **程序启动**：应用程序在系统托盘中静默运行，通过快捷键 `Ctrl+C+C` 激活。
- **界面操作**：激活后，可在弹出窗口中选择 GPT 模式，查看生成内容。

## 🛠️ 系统托盘功能

- **显示/隐藏窗口**：控制应用程序窗口的显示或隐藏。
- **退出应用**：安全关闭程序。

## 📋 前提条件

- Windows 系统（可执行文件）。
- Python 环境（源代码运行）。
- 互联网连接。

## 🛠️ 故障排除

遇到快捷键不响应？请检查应用程序的系统权限，确保其能注册全局快捷键。

## 📄 许可与贡献

- **许可协议**：MIT License。
- **开源贡献**：欢迎 star 和贡献代码！
- **问题反馈**：通过 GitHub Issue 提交问题。

## 📞 联系与支持

- **问题咨询**：欢迎在 GitHub Issue 提出问题。
- **服务购买**：如需购买 OpenAI 3.5 或 4 账号，请通过微信联系，号码为 13549957404，并备注 GitHub。

W-AnywhereGPT，您的日常生活和专业工作的 AI 助手！🌟
