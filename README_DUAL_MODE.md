# KI Chat Pattern - Dual Mode Setup 🚀

Eine AI-Chat-Anwendung mit **zwei Launch-Modi** aus **einer Codebasis**!

## 🎯 Zwei Modi, gleicher Code

### 🌐 Browser-Mode (Entwicklung)
- Öffnet im Standard-Browser
- DevTools verfügbar (F12)
- Hot-Reload & schnelles Debugging
- **Start:** `python main_nicegui.py`

### 🖥️ Desktop-Mode (Production)
- Natives Desktop-Fenster (PyWebView)
- Kein Browser-UI
- Erscheint als eigenständige App
- **Start:** `python main_nicegui_desktop.py`

## 📋 Installation

```bash
# Dependencies installieren
pip install -r requirements.txt

# API Keys konfigurieren (optional)
cp .env.example .env
# Bearbeite .env und füge deine Keys ein
```

## 🚀 Verwendung

### Browser-Version (empfohlen für Entwicklung)
```bash
python main_nicegui.py
```
→ Öffnet automatisch `http://localhost:8080` im Browser

### Desktop-Version (natives Fenster)
```bash
python main_nicegui_desktop.py
```
→ Startet als eigenständige Desktop-App

## 🛠️ Entwicklungs-Workflow

1. **Entwickeln** im Browser-Mode
   - Schnelles Debugging mit DevTools
   - UI-Änderungen in `ui_nicegui/` sofort sichtbar

2. **Testen** im Desktop-Mode
   - Desktop-Feeling überprüfen
   - Native Window-Verhalten testen

3. **Code-Änderungen** betreffen beide Modi!
   - UI-Komponenten in `ui_nicegui/` sind identisch
   - Core-Logik in `core/` ist identisch
   - Nur Launcher unterscheiden sich

## 📁 Projekt-Struktur

```
ki_chat_pattern_nicegui/
├── main_nicegui.py              # 🌐 Browser-Launcher
├── main_nicegui_desktop.py      # 🖥️ Desktop-Launcher
│
├── core/                        # Business Logic (shared!)
│   ├── llm_manager.py
│   └── providers/
│
├── ui_nicegui/                  # UI Components (shared!)
│   ├── app_layout.py
│   ├── sidebar.py
│   ├── chat_view.py
│   └── input_area.py
│
├── storage/                     # Persistence (shared!)
│   └── chat_db.py
│
└── ui/                          # Legacy Flet UI (Fallback)
```

## 🎨 Features

- ✅ Multi-Provider Support (OpenAI, Anthropic, Mock)
- ✅ Streaming-Antworten
- ✅ Chat-History (SQLite)
- ✅ Model-Auswahl
- ✅ Dark Mode
- ✅ Markdown-Rendering
- ✅ **Zwei Launch-Modi aus einer Codebasis!**

## 🌍 Cross-Platform

### Browser-Mode
- ✅ macOS
- ✅ Windows
- ✅ Linux
- → 100% portabel (nutzt Standard-Browser)

### Desktop-Mode (PyWebView)
- ✅ macOS (WebKit)
- ✅ Windows (Edge WebView2)
- ✅ Linux (GTK WebKit)
- → ~85% portabel (kleine Rendering-Unterschiede möglich)

## 📦 Distribution

### Browser-Mode als Web-App
```bash
# Deploy auf Server
uvicorn main_nicegui:app --host 0.0.0.0 --port 80
```

### Desktop-Mode als Binary
```bash
# macOS/Windows/Linux
pyinstaller main_nicegui_desktop.py --windowed --onefile
```

## 🐛 Troubleshooting

### Desktop-Mode startet nicht
```bash
# Prüfe ob PyWebView installiert ist
python -c "import webview; print(webview.__version__)"

# Windows: Installiere WebView2 Runtime
# https://developer.microsoft.com/en-us/microsoft-edge/webview2/
```

### Port 8080 bereits belegt
```bash
# Ändere Port in main_nicegui.py oder main_nicegui_desktop.py
# Zeile: port=8080 → port=8081
```

## 💡 Tipp

**Entwickle im Browser-Mode, teste im Desktop-Mode!**

Der Browser bietet die beste Developer-Experience, während Desktop-Mode das finale User-Experience zeigt.

---

**Viel Erfolg! 🎉**
