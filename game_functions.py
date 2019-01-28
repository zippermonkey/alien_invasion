# 重构 模块game_functions

import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹 并将其加入编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 停止移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 停止移动
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 加入飞船
    ship.blitme()
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置 并且删除已经消失的子弹"""
    # 更新子弹
    bullets.update()
    
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)