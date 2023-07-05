from PySide6.QtGui import QColor


class Colors:
    main_color = (18, 18, 18)  # koyu lacivert
    seconder_color = (238, 238, 238)  # grimsi mavi
    third_color = (34, 34, 34)  # truncumsu kahve
    border_color = (45, 45, 45)
    highlight_color = (55, 200, 195)  # cam öbeği

    def light_theme(self):
        self.main_color = (233, 243, 252)
        self.seconder_color = (48, 72, 108)
        self.third_color = (235, 245, 255)
        self.border_color = (45, 45, 45)
        self.highlight_color = (247, 146, 92)

    def dark_theme(self):
        self.main_color = (18, 18, 18)  # koyu lacivert
        self.seconder_color = (238, 238, 238)  # grimsi mavi
        self.third_color = (34, 34, 34)  # truncumsu kahve
        self.border_color = (45, 45, 45)
        self.highlight_color = (55, 200, 195)  # cam öbeği
