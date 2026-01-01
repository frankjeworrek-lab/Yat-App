"""
KI Chat Pattern - NiceGUI Desktop Version
Main entry point for the NiceGUI implementation
"""
import asyncio
from dotenv import load_dotenv
from nicegui import ui, app
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


if __name__ in {"__main__", "__mp_main__"}:
    # NiceGUI Desktop Mode Options:
    # 
    # Option 1: Browser-based (current, easiest)
    # - Opens in default browser automatically
    # - Full NiceGUI features
    # - Easy to develop and debug
    
    # Option 2: Native window with PyWebView
    # - Install: pip install nicegui[native]
    # - Uncomment below section
    # - Comment out ui.run() section
    
    # from nicegui import native
    # native.start_server_and_native_window(
    #     main_page,
    #     window_title='KI Chat Pattern',
    #     width=1200,
    #     height=800,
    # )
    
    # Current: Browser-based (auto-opens in browser)
    ui.run(
        title='KI Chat Pattern',
        dark=True,
        reload=False,
        show=True,  # Auto-open browser
        port=8080,
        binding_refresh_interval=0.1,
    )
