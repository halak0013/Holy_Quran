import sys
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication
from src.static.colors import Colors

co=Colors()
def set_custom_theme(app:QApplication):
    app_palette = QPalette()
    app_palette.setColor(QPalette.Window, QColor(co.main_color[0],co.main_color[1],co.main_color[2]))  # Pencere arkaplan rengi
    app_palette.setColor(QPalette.WindowText, QColor(co.seconder_color[0],co.seconder_color[1],co.seconder_color[2]))  # Pencere metin rengi
    app_palette.setColor(QPalette.Highlight, QColor(co.third_color[0],co.third_color[1],co.third_color[2]))  # Buton metin rengi

    
    combo_stylesheet = f"""
        
        QComboBox {{
            background-color: rgb{co.third_color};
            color: rgb{co.seconder_color};
            selection-background-color: rgb{co.highlight_color};
            selection-color: rgb{co.seconder_color};
        }}
        QComboBox QAbstractItemView {{
            background-color: rgb{co.third_color};
            color: rgb{co.seconder_color};
            selection-background-color: rgb{co.highlight_color};
            selection-color: rgb{co.seconder_color};
        }}
        
        QSpinBox {{
            background-color: rgb{co.third_color};
            color: rgb{co.seconder_color};
            selection-background-color: rgb{co.third_color};
            selection-color: rgb{co.seconder_color};
        }}
        
        QPushButton {{
            background-color: rgb{co.third_color};
            color: rgb{co.seconder_color};
            selection-background-color: rgb{co.main_color};
            selection-color: rgb{co.seconder_color};
            border: 1px solid rgb{co.border_color};
            
        }}
    """

    app.setPalette(app_palette)
    app.setStyleSheet(combo_stylesheet)
