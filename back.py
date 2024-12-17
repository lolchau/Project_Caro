import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Example with Back Button")

# Màu sắc và phông chữ
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
font = pygame.font.Font(None, 50)

# Biến trạng thái màn hình
current_screen = "menu"  # Mặc định hiển thị menu

# Tạo các nút
play_text = "Play"
help_text = "Help"
settings_text = "Settings"
back_text = "Back"

play_surface = font.render(play_text, True, TEXT_COLOR)
help_surface = font.render(help_text, True, TEXT_COLOR)
settings_surface = font.render(settings_text, True, TEXT_COLOR)
back_surface = font.render(back_text, True, TEXT_COLOR)

# Vị trí các nút
play_rect = play_surface.get_rect(center=(WIDTH // 2, 300))
help_rect = help_surface.get_rect(center=(WIDTH // 2, 400))
settings_rect = settings_surface.get_rect(center=(WIDTH // 2, 500))
back_rect = back_surface.get_rect(center=(WIDTH // 2, 700))  # Nút Back

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if current_screen == "menu":
                if play_rect.collidepoint(mouse_x, mouse_y):
                    print("Play selected!")  # Chuyển sang màn hình Play nếu có
                elif help_rect.collidepoint(mouse_x, mouse_y):
                    current_screen = "help"  # Chuyển sang màn hình Help
                elif settings_rect.collidepoint(mouse_x, mouse_y):
                    current_screen = "settings"  # Chuyển sang màn hình Settings

            elif current_screen in ["help", "settings"]:
                if back_rect.collidepoint(mouse_x, mouse_y):
                    current_screen = "menu"  # Quay lại menu

    # Hiển thị nội dung theo trạng thái màn hình
    screen.fill(BACKGROUND_COLOR)  # Xóa màn hình với màu nền

    if current_screen == "menu":
        screen.blit(play_surface, play_rect)
        screen.blit(help_surface, help_rect)
        screen.blit(settings_surface, settings_rect)

    elif current_screen == "help":
        help_message = font.render("This is the Help Screen", True, TEXT_COLOR)
        help_message_rect = help_message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(help_message, help_message_rect)
        screen.blit(back_surface, back_rect)

    elif current_screen == "settings":
        settings_message = font.render("This is the Settings Screen", True, TEXT_COLOR)
        settings_message_rect = settings_message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(settings_message, settings_message_rect)
        screen.blit(back_surface, back_rect)

    pygame.display.flip()  # Cập nhật màn hình

pygame.quit()
sys.exit()
