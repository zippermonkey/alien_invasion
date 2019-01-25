class Settings():
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1280
        self.screen_height = 768
        # 背景颜色设置
        self.bg_color = (230,230,230)
        # 速度设置
        self.ship_speed_factor = 1.5