"""
Sidebar component for NiceGUI
Model selection, chat history, and controls
"""
from nicegui import ui
from core.llm_manager import LLMManager
from core.user_config import UserConfig
from .components.connection_status import ConnectionMonitor
import asyncio


class Sidebar:
    def __init__(self, llm_manager: LLMManager, on_model_change, on_new_chat=None, on_load_chat=None):
        self.llm_manager = llm_manager
        self.on_model_change = on_model_change
        self.on_new_chat = on_new_chat
        self.on_load_chat = on_load_chat
        
        self.model_select = None
        self.history_container = None
        self.status_container = None
        
        # UI References for Active Assistance
        self.status_badge_row = None
        self.provider_status_icon = None
        self.provider_status_label = None
        
    def build(self):
        """Build the sidebar UI with professional dark theme"""
        with ui.column().classes('w-72 h-screen p-5 gap-4').style(
            'background-color: var(--bg-secondary); border-right: 1px solid var(--border-color);'
        ):
            # Header with gradient
            # Header Banner
            ui.image('/logo/logo.png').classes('w-full rounded-xl shadow-md mb-2').tooltip('Y.A.T. v2.1')
            
            # Signature
            ui.label('ARCHITECT • FRANK JEWORREK').classes(
                'w-full text-center text-[10px] text-gray-500 font-bold tracking-[0.2em] mb-3 opacity-80'
            )
            
            ui.separator().classes('bg-gray-700')
            
            # Model Configuration Section
            with ui.column().classes('w-full gap-2 mt-2'):
                with ui.row().classes('w-full justify-between items-center'):
                    ui.label('Model').classes('text-sm font-semibold text-gray-300')
                    ui.button(icon='refresh', on_click=self._refresh_models).props(
                        'flat dense size=sm'
                    ).classes('text-gray-400 hover:text-blue-400')
                
                # Active Provider Status Badge (Active Assistance)
                # Styled as a pill/bubble with dynamic background and text color
                with ui.row().classes('w-full items-center gap-2 mb-2 px-3 py-2 cursor-pointer transition-colors rounded-lg border').style(
                    'border-color: var(--border-color);'
                ).on('click', self._handle_status_click) as row:
                    self.status_badge_row = row
                    self.provider_status_icon = ui.icon('circle', size='xs')
                    self.provider_status_label = ui.label('Initializing...').classes('text-xs font-medium flex-1')
                    # Assistance Arrow (Always present but styled differently)
                    self.status_action_icon = ui.label('').classes('text-xs font-bold')

                # Model Dropdown with custom styling
                self.model_select = ui.select(
                    options={},
                    label='Select Model',
                    on_change=self._handle_model_change
                ).classes('w-full').props('outlined dense dark bg-color="grey-9" label-color="grey-4"').style(
                    'background-color: var(--bg-accent); border-color: var(--border-color);'
                )
            
            # Status Container (for detailed error cards if needed)
            with ui.column().classes('w-full') as status_col:
                self.status_container = status_col
                self.status_container.visible = False
            
            # Chat History Section with margin instead of flex spacer
            with ui.column().classes('w-full flex-1 min-h-0 mt-6'):
                with ui.row().classes('w-full justify-between items-center mb-2'):
                    ui.label('History').classes('text-sm font-semibold text-gray-300')
                    ui.button(
                        icon='add',
                        on_click=self._handle_new_chat
                    ).props('flat dense size=sm color=blue-4')
                
                # History List (native vertical scroll, centered items via padding)
                with ui.column().classes('w-full flex-1 overflow-y-auto overflow-x-hidden justify-start p-2 gap-2') as history_col:
                    self.history_container = history_col
                    ui.label('No chats yet').classes('text-sm italic text-gray-500 p-2')
        
            ui.separator().classes('bg-gray-700 mt-2')
            
            # Footer Actions
            with ui.row().classes('w-full gap-2 items-center mb-2'):
                # Preferences (Main Action)
                ui.button(
                    'Preferences',
                    icon='tune',
                    on_click=lambda: self._open_settings(tab='providers')
                ).props('outline').classes('flex-1 text-gray-300').style(
                    'border-color: var(--border-color); color: var(--text-primary);'
                )
                
                # Help / Docs (Secondary Action)
                ui.button(
                    icon='help_outline',
                    on_click=self._open_docs
                ).props('outline').classes('text-gray-400 w-12').style(
                    'border-color: var(--border-color); color: var(--text-secondary);'
                ).tooltip('Knowledge Base')
            
            # Global Connection Monitor (Footer)
            ConnectionMonitor().build()
    
    def _open_settings(self, tab='providers'):
        """Open settings dialog with specific tab"""
        from .provider_settings_dialog import ProviderSettingsDialog
        dialog = ProviderSettingsDialog(llm_manager=self.llm_manager, sidebar=self)
        dialog.show(initial_tab=tab)

    def _open_docs(self):
        """Open documentation dialog"""
        from .docs_dialog import DocsDialog
        DocsDialog().show()
    
    async def _refresh_models(self):
        """Refresh models from all providers"""
        await self.load_models()

    def _update_status_badge(self, state_group, text, icon_name, animate=False, action_hint=""):
        """
        Centralized UI Update Logic for Status Matrix v2
        Enforces Generic Design Rules (Monochromatic Styling)
        
        state_group: 'green', 'blue', 'orange', 'red', 'critical'
        """
        # 1. Reset Classes
        base_classes = 'w-full items-center gap-2 mb-2 px-3 py-2 cursor-pointer transition-colors rounded-lg border'
        icon_classes = ''
        text_classes = 'text-xs font-medium flex-1'
        
        # 2. Apply Design Rules (Spec v2)
        if state_group == 'green':
            bg_class = 'bg-green-900 bg-opacity-30 border-green-800'
            fg_class = 'text-green-400'
            hover_class = 'hover:bg-opacity-40'
        elif state_group == 'blue':
            bg_class = 'bg-blue-900 bg-opacity-40 border-blue-800'
            fg_class = 'text-blue-400'
            hover_class = 'hover:bg-opacity-50'
        elif state_group == 'orange':
            bg_class = 'bg-orange-900 bg-opacity-40 border-orange-800'
            fg_class = 'text-orange-400'
            hover_class = 'hover:bg-opacity-50 hover:border-orange-600'
        elif state_group == 'red':
            bg_class = 'bg-red-900 bg-opacity-40 border-red-800'
            fg_class = 'text-red-400'
            hover_class = 'hover:bg-opacity-50 hover:border-red-600'
        elif state_group == 'critical':
            bg_class = 'bg-red-950 border-red-900'
            fg_class = 'text-red-600 font-bold'
            hover_class = 'hover:bg-black'
        else: # Fallback
            bg_class = 'bg-gray-800'
            fg_class = 'text-gray-400'
            hover_class = ''

        # 3. Apply to UI Elements
        self.status_badge_row.classes(replace=f"{base_classes} {bg_class} {hover_class}")
        
        # Icon
        self.provider_status_icon.name = icon_name
        self.provider_status_icon.props(f'color={state_group if state_group != "critical" else "red"}') # NiceGUI color prop
        # Reset animation classes first
        current_anim = 'animate-spin' if 'spin' in (self.provider_status_icon.classes or '') else ''
        current_anim = 'animate-pulse' if 'pulse' in (self.provider_status_icon.classes or '') else current_anim
        self.provider_status_icon.classes(replace=f"{fg_class} {current_anim}")
        
        if animate == 'spin':
             self.provider_status_icon.classes(add='animate-spin', remove='animate-pulse')
        elif animate == 'pulse':
             self.provider_status_icon.classes(add='animate-pulse', remove='animate-spin')
        else:
             self.provider_status_icon.classes(remove='animate-spin animate-pulse')

        # Text
        self.provider_status_label.text = text
        self.provider_status_label.classes(replace=f"{text_classes} {fg_class}")
        
        # Action Hint (Arrow)
        self.status_action_icon.text = action_hint
        self.status_action_icon.classes(replace=f"text-xs font-bold {fg_class}")


    async def _handle_status_click(self):
        """
        Active User Assistance Handler (Spec v2)
        Handles transitions based on current state.
        """
        if not self.llm_manager.active_provider_id:
            self._open_settings()
            return

        provider = self.llm_manager.providers.get(self.llm_manager.active_provider_id)
        if not provider:
            return

        # [B2] Verifying Status... (Immediate Feedback)
        self._update_status_badge('blue', 'Verifying Status...', 'search', animate='spin')
        self.status_action_icon.text = "" # Clear action during wait
        
        # Give UI a moment to breathe
        await asyncio.sleep(0.5) 
        
        try:
             # Force Re-Init (The Check)
             await provider.initialize()
             await self.load_models()
             
             # The result determines the next state (handled by load_models)
             # But if successful, show transient success [G2]
             if provider.config.status == 'active' and not provider.config.init_error:
                 self._update_status_badge('green', '✓ Verified: Operational', 'check_circle', animate=False)
                 await asyncio.sleep(2.0)
                 # Revert to standard G1/G3 display
                 await self.load_models()
             else:
                 # Failure is handled by load_models picking up the error state
                 pass
                  
        except Exception as e:
             # Fallback for crashing checks
             self._update_status_badge('red', f'{provider.config.name}: System Crash ➜ Log', 'bug_report', action_hint='➜')
             print(f"Verification Crash: {e}")

    
    def _handle_new_chat(self):
        if self.on_new_chat:
            self.on_new_chat()
    
    def _handle_load_chat(self, conversation_id):
        if self.on_load_chat:
            self.on_load_chat(conversation_id)
    
    def _handle_model_change(self, e):
        value = self.model_select.value
        if not value: return
        try:
            pid, mid = value.split('|', 1)
            self.llm_manager.active_provider_id = pid
            self.llm_manager.active_model_id = mid
            UserConfig.save('last_model', value)
            if self.on_model_change:
                self.on_model_change(f'Switched to {mid}')
        except Exception:
            pass
    
    async def load_models(self):
        """
        Load models and Map to Status Matrix v2 [G1-R6]
        """
        # This implicitly calls provider checks if needed
        models = await self.llm_manager.get_available_models()
        
        # Identify Active Provider
        active_id = self.llm_manager.active_provider_id
        active_provider = self.llm_manager.providers.get(active_id) if active_id else None
        
        # --- LOGIC MAPPING (The Brain of Assistance) ---
        
        if len(self.llm_manager.providers) == 0:
            # [R6] CRITICAL FAILURE
            self._update_status_badge('critical', 'Critical Failure ➜ Help', 'dangerous', animate='pulse', action_hint='➜')
            
        elif not active_provider:
            # [O4] No Provider
            self._update_status_badge('orange', 'No Provider ➜ Select One', 'touch_app', animate='pulse', action_hint='➜')
            
        else:
            p_name = active_provider.config.name
            init_error = active_provider.config.init_error
            status = active_provider.config.status
            
            if init_error:
                # Differentiate Errors based on message content (heuristic)
                err_text = str(init_error).lower()
                
                if '401' in err_text or 'key' in err_text or 'auth' in err_text:
                    # [R1] Auth Failed
                    self._update_status_badge('red', f'{p_name}: Auth Failed ➜ Edit Key', 'lock', animate='pulse', action_hint='🛠️')
                elif '429' in err_text or 'quota' in err_text:
                    # [R5] Quota Exceeded
                    self._update_status_badge('red', f'{p_name}: Quota Exceeded ➜ Plan', 'payments', animate=False, action_hint='➜')
                elif 'connect' in err_text or 'timeout' in err_text:
                    # [R2] Connection Lost
                    self._update_status_badge('red', f'{p_name}: Connection Lost ➜ Retry', 'wifi_off', animate='pulse', action_hint='↻')
                else:
                    # [R3/R4] Generic Error
                    self._update_status_badge('red', f'{p_name}: Error ➜ Retry', 'bug_report', animate='pulse', action_hint='↻')

            elif status == 'setup_needed':
                # [O1] Setup Needed
                 self._update_status_badge('orange', f'{p_name}: Setup Needed ➜ Configure', 'settings', animate='pulse', action_hint='⚙️')
            
            elif status == 'active':
                if not models:
                    # [O3] Empty Models (Active but empty)
                    self._update_status_badge('orange', f'{p_name}: No Models ➜ Refresh', 'folder_off', animate=False, action_hint='↻')
                else:
                    # [G1] Active Healthy (Standard)
                    # Future: Implement G3 check here if we have cache-flag
                    self._update_status_badge('green', f'Active: {p_name}', 'circle', animate=False)

            else:
                # Catch-all (Should not happen often)
                self._update_status_badge('red', f'{p_name}: Unknown State ➜ Check', 'help', action_hint='?')

        
        # Populate Dropdown
        options = {}
        if models:
            for m in models:
                pid = getattr(m, 'provider_id', 'mock')
                key = f"{pid}|{m.id}"
                options[key] = f"{m.name} ({m.provider})"
        
        self.model_select.options = options
        self.model_select.update()
        
        # Restore Selection Logic
        display_val = None
        saved = UserConfig.get('last_model')
        if saved and saved in options: display_val = saved
        elif active_id and f"{active_id}|{self.llm_manager.active_model_id}" in options:
             display_val = f"{active_id}|{self.llm_manager.active_model_id}"
        elif options:
             display_val = list(options.keys())[0]

        if display_val:
            self.model_select.value = display_val

    def update_history_list(self, conversations):
        """Update chat history list with modern card design"""
        self.history_container.clear()
        if not conversations:
            with self.history_container:
                ui.label('No chats yet').classes('text-sm italic text-gray-500 p-2')
        else:
            with self.history_container:
                for conv in conversations:
                    conv_id = conv['id']
                    with ui.card().classes('w-full p-3 cursor-pointer transition-all').style(
                        'background-color: var(--bg-secondary); border: 1px solid var(--border-color);'
                        'transition: all 0.2s ease;'
                    ).on('click', lambda cid=conv_id: self._handle_load_chat(cid)):
                        ui.add_head_html(".nicegui-content .q-card:hover { background-color: var(--bg-accent) !important; border-color: var(--accent-color) !important; }")
                        ui.label(conv['title']).classes('text-sm font-medium text-gray-200 truncate')
                        ui.label(conv['updated_at'][:10]).classes('text-xs text-gray-500 mt-1')

    def set_optimistic_state(self, provider_id: str):
        """
        [B1] CONNECTING State
        Called by Settings Dialog
        """
        # [B1] Connecting
        self._update_status_badge('blue', f'Connecting to {provider_id}...', 'sync', animate='spin')
