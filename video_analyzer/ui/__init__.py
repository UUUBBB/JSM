# UI modules
from .main_app import DashboardWindow as MainWindow
from .gui_app import Colors, STYLESHEET, MainWindow as NarrationWindow, NarrationWidget
from .script_editor import ScriptEditorDialog as ScriptEditor
from .style_selection_widget import StyleSelectionWidget
from .style_dashboard import StyleDashboard
from .prompt_editor_widget import PromptManagerPage as PromptEditorWidget
from .studio_window import StudioWindow
from .narration_panel import NarrationPanel
from .storyboard_panel import StoryboardPanel

__all__ = [
    'MainWindow',
    'NarrationWindow',
    'NarrationWidget',
    'ScriptEditor',
    'StyleSelectionWidget',
    'StyleDashboard',
    'PromptEditorWidget',
    'StudioWindow',
    'NarrationPanel',
    'StoryboardPanel',
]
