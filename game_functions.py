# 重构 模块game_functions

import sys
import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event_get():
        if event.type == pygame.QUIT:
            sys.exit()

