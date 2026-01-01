"""
ChatView component for NiceGUI
Displays chat messages with markdown support and auto-scroll
"""
from nicegui import ui
from core.providers.types import Message, Role


class ChatView:
    def __init__(self):
        self.messages_container = None
        self.message_rows = []
        
    def build(self):
        """Build the chat view UI"""
        with ui.column().classes('flex-1 overflow-auto p-4 gap-4') as container:
            self.messages_container = container
        return self.messages_container
    
    def add_message(self, message: Message):
        """Add a new message to the chat"""
        is_user = message.role == Role.USER
        
        with self.messages_container:
            with ui.row().classes('w-full items-start gap-3' + (' justify-end' if is_user else '')):
                if not is_user:
                    # AI Avatar (left side)
                    ui.icon('auto_awesome', size='sm').classes('text-teal-600 mt-1')
                
                # Message bubble
                with ui.card().classes(
                    'max-w-2xl p-4 ' + 
                    ('bg-primary text-white' if is_user else 'bg-grey-2 dark:bg-grey-9')
                ):
                    msg_element = ui.markdown(message.content).classes('prose dark:prose-invert')
                    self.message_rows.append({
                        'element': msg_element,
                        'is_user': is_user
                    })
                
                if is_user:
                    # User Avatar (right side)
                    ui.icon('person', size='sm').classes('text-blue-grey-600 mt-1')
        
        # Auto-scroll handled by scroll_area naturally
    
    def update_last_message(self, content: str):
        """Update the content of the last message (for streaming)"""
        if self.message_rows:
            last_msg = self.message_rows[-1]
            last_msg['element'].set_content(content)
    
    def clear(self):
        """Clear all messages"""
        self.messages_container.clear()
        self.message_rows.clear()
