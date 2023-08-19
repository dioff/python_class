import pygame
import random

# 初始化游戏
pygame.init()

# 设置游戏窗口大小
screen_width = 1024
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞机大战游戏")

# 定义颜色
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)

# 加载飞机和敌人的图像
player_img = pygame.image.load(r"C:\Users\Lazzy\Desktop\python\飞机大战\飞机.png")  # 你需要有一个名为"player.png"的飞机图像
enemy_img = pygame.image.load(r"C:\Users\Lazzy\Desktop\python\飞机大战\敌机.png")    # 你需要有一个名为"enemy.png"的敌人图像

# 获取图像的宽度和高度
player_width, player_height = player_img.get_width(), player_img.get_height()
enemy_width, enemy_height = enemy_img.get_width(), enemy_img.get_height()

# 初始化飞机位置
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 20
player_speed = 5

# 初始化敌人
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3

# 创建一个字体对象用于显示 "Game Over"
game_over_font = pygame.font.Font(None, 64)


# 游戏主循环
running = True
clock = pygame.time.Clock()

game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动飞机
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 移动敌人
    enemy_y += enemy_speed

    # 碰撞检测
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width

    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0

    # 在游戏主循环中的碰撞检测部分添加以下代码
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    if player_rect.colliderect(enemy_rect):
        game_over = True
        
    # 渲染画面
    screen.fill(blue)
    if game_over:
        game_over_text = game_over_font.render("Game Over", True, red)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    else:
        screen.blit(player_img, (player_x, player_y))
        screen.blit(enemy_img, (enemy_x, enemy_y))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
