# KI Chat Pattern (NiceGUI Edition)

A professional, extensible AI Chat application built with **Python**, **NiceGUI**, and **PyWebView**.

## 🌟 Features

- **Dual-Mode Architecture**:
  - 🌐 **Browser Mode**: Develop and run in your favorite browser.
  - 🖥️ **Desktop Mode**: Native window experience using PyWebView.
- **True Plugin System**:
  - 🔌 **Auto-Discovery**: Drop `.py` files in `plugins/` to add providers.
  - 🧩 **Extensible**: Add any LLM provider (OpenAI, Anthropic, Ollama, etc.).
  - 🔄 **Hot-Reload**: Change API keys and configs without restarting.
- **Professional UI**:
  - 🎨 **Dark Theme**: Modern, high-contrast design.
  - 💬 **Rich Chat**: Markdown support, code highlighting, streams.
  - ⚙️ **GUI Configuration**: Manage keys and providers visually.

## 🚀 Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run Application
**Desktop Mode (Native Window):**
```bash
python main_nicegui_desktop.py
```

**Browser Mode:**
```bash
python main_nicegui.py
```

## ⚙️ Configuration

### Managing Providers
1. Click **"Manage Providers"** in the sidebar.
2. Toggle providers (OpenAI, Anthropic, Mock) ON/OFF.
3. Edit provider-specific settings.

### API Keys
1. Click **"Configure API Keys"** in the sidebar.
2. Enter your keys (stored securely in `.env`).
3. **Hot-Reload**: Keys apply immediately – no restart needed!

## 🧩 Plugin System

The app uses a strict plugin architecture. Providers are **not** hardcoded.

- **Location**: `plugins/` directory.
- **Create New**: Copy `plugins/_template_plugin.py`.
- **Logic**: Plugins are auto-discovered at startup. Only enabled plugins are loaded.

--> [📖 Read the Plugin Documentation](docs/PLUGIN_SYSTEM.md)

## 📁 Project Structure

```
ki_chat_pattern_nicegui/
├── main_nicegui_desktop.py # Native Desktop Launcher
├── main_nicegui.py         # Browser Launcher
├── plugins/                # LLM Provider Plugins
│   ├── openai_plugin.py
│   └── ...
├── core/                   # Core Logic (Managers)
├── ui_nicegui/             # User Interface Components
├── provider_config.json    # Provider Configuration
└── .env                    # Secrets (Git-ignored)
```
