"""
InputArea component for NiceGUI
Text input with send button and auto-focus
"""
from nicegui import ui
import asyncio


class InputArea:
    def __init__(self, on_submit):
        self.on_submit = on_submit
        self.text_input = None
        self.send_button = None
        
    def build(self):
        """Build the input area UI"""
        with ui.card().classes('w-full m-4 p-2'):
            with ui.row().classes('w-full gap-2 items-center'):
                self.text_input = ui.input(
                    placeholder='Ask anything...',
                    on_change=self._check_enter
                ).classes('flex-1').props('outlined dense')
                
                # Bind Enter key
                self.text_input.on('keydown', self._handle_keydown)
                
                self.send_button = ui.button(
                    icon='send',
                    on_click=self._handle_submit
                ).props('round color=primary').classes('ml-2')
    
    async def _handle_keydown(self, e):
        """Handle keyboard events"""
        if e.args.get('keycode') == 13 and not e.args.get('shiftKey'):
            await self._handle_submit()
    
    def _check_enter(self, e):
        """Placeholder for on_change"""
        pass
    
    async def _handle_submit(self, e=None):
        """Handle message submission"""
        text = self.text_input.value.strip()
        if text and self.on_submit:
            self.text_input.value = ''
            self.text_input.update()
            await self.on_submit(text)
            # Re-focus input
            try:
                await asyncio.sleep(0.1)
                self.text_input.run_method('focus')
            except Exception as err:
                print(f"Focus error: {err}")
    
    def disable(self):
        """Disable input during processing"""
        if self.send_button:
            self.send_button.disable()
    
    def enable(self):
        """Enable input after processing"""
        if self.send_button:
            self.send_button.enable()
        if self.text_input:
            try:
                self.text_input.run_method('focus')
            except:
                pass
