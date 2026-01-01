"""
KI Chat Pattern - NiceGUI Desktop App (Native Window)
Uses PyWebView for true desktop window experience
"""
import asyncio
from dotenv import load_dotenv
from nicegui import ui, app
import webview
import threading
from core.llm_manager import LLMManager
from core.providers.mock_provider import MockProvider
from core.providers.types import ProviderConfig
from ui_nicegui.app_layout import AppLayout

load_dotenv(override=True)

# Global LLM Manager (initialized on startup)
llm_manager = None


async def initialize_providers():
    """Initialize all providers on app startup"""
    global llm_manager
    
    if llm_manager is not None:
        return  # Already initialized
    
    llm_manager = LLMManager()
    
    # Register Mock Provider
    mock_config = ProviderConfig(name="Mock Provider")
    llm_manager.register_provider("mock", MockProvider(mock_config))
    
    # Register OpenAI
    from core.providers.openai_provider import OpenAIProvider
    openai_config = ProviderConfig(name="OpenAI")
    openai_provider = OpenAIProvider(openai_config)
    await openai_provider.initialize()
    llm_manager.register_provider("openai", openai_provider)
    
    # Register Anthropic
    from core.providers.anthropic_provider import AnthropicProvider
    anthropic_config = ProviderConfig(name="Anthropic")
    anthropic_provider = AnthropicProvider(anthropic_config)
    await anthropic_provider.initialize()
    llm_manager.register_provider("anthropic", anthropic_provider)
    
    # Set initial defaults
    llm_manager.active_provider_id = "mock"
    llm_manager.active_model_id = "mock-gpt-4"
    
    print("✓ Providers initialized successfully")


@ui.page('/')
async def main_page():
    """Main application page"""
    # Ensure providers are initialized
    await initialize_providers()
    
    # Create and build layout
    app_layout = AppLayout(llm_manager)
    app_layout.build()
    
    # Initialize async components
    await app_layout.initialize_async()


def start_nicegui_server():
    """Start NiceGUI server in background thread"""
    ui.run(
        title='KI Chat Pattern',
        dark=True,
        reload=False,
        show=False,  # Don't open browser - PyWebView will handle display
        port=8080,
        binding_refresh_interval=0.1,
    )


if __name__ in {"__main__", "__mp_main__"}:
    print("🚀 Starting KI Chat Pattern (Desktop Mode)...")
    
    # Start NiceGUI server in separate thread
    server_thread = threading.Thread(target=start_nicegui_server, daemon=True)
    server_thread.start()
    
    # Wait for server to be ready
    import time
    time.sleep(2)
    
    # Create native desktop window with PyWebView
    print("🪟 Creating desktop window...")
    webview.create_window(
        title='KI Chat Pattern',
        url='http://localhost:8080',
        width=1200,
        height=800,
        resizable=True,
        fullscreen=False,
        min_size=(800, 600),
        background_color='#1E1E1E',
        text_select=True,
    )
    
    # Start PyWebView (blocks until window is closed)
    webview.start(debug=False)
    
    print("👋 Desktop app closed")
