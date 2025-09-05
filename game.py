import pygame
import random
pygame.init()

#define variables
width = 284
height = 512
frame=0
FPS=60
pipes=[[200,4]]
bird = [40, height//2-50]
gravity = 0.15  # Reduced from 0.2 to make falling slower
velocity = 0
game_over = False
score = 0
victory = False

game_screen = pygame.display.set_mode((width,height))
game_background = pygame.image.load("images/background.png")
wing_up = pygame.image.load("images/bird_wing_up.png")
wing_down = pygame.image.load("images/bird_wing_down.png")
pipe_body = pygame.image.load("images/pipe_body.png")
pipe_end = pygame.image.load("images/pipe_end.png")
clock=pygame.time.Clock()

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)

def draw_pipes():
    global pipes, score
    for n in range(len(pipes)):
        for m in range(0,pipes[n][1]):
            game_screen.blit(pipe_body,(pipes[n][0], m*32))
        for m in range(pipes[n][1]+6,16):
            game_screen.blit(pipe_body,(pipes[n][0], m*32))
        game_screen.blit(pipe_end,(pipes[n][0], (pipes[n][1])*32))
        game_screen.blit(pipe_end,(pipes[n][0], (pipes[n][1]+5)*32))
        pipes[n][0] -= 1
        
        # Check if bird passed the pipe (increase score)
        if pipes[n][0] == 8:  # When pipe moves to bird position
            score += 1

def draw_bird(x,y):
    global frame
    if 0 <= frame <= 30:
        game_screen.blit(wing_up,(x,y))
        frame += 1
    elif 30 <= frame <=60:
        game_screen.blit(wing_down,(x,y))
        frame += 1
        if frame == 60 : frame = 0

def safe():
    """Check if bird is safe (not hitting pipes)"""
    global bird
    
    # Bird collision box
    bird_rect = pygame.Rect(bird[0], bird[1], 32, 32)
    
    # Check if bird hits screen boundaries
    if bird[1] < 0 or bird[1] > height - 32:
        return False
    
    # Check if bird hits pipes
    for pipe in pipes:
        pipe_x = pipe[0]
        pipe_y = pipe[1]
        
        # Top pipe
        top_pipe_rect = pygame.Rect(pipe_x, 0, 32, pipe_y * 32)
        if bird_rect.colliderect(top_pipe_rect):
            return False
        
        # Bottom pipe
        bottom_pipe_rect = pygame.Rect(pipe_x, (pipe_y + 5) * 32, 32, height - (pipe_y + 5) * 32)
        if bird_rect.colliderect(bottom_pipe_rect):
            return False
    
    return True

def draw_victory_screen():
    """Draw victory screen"""
    # Semi-transparent black overlay
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    game_screen.blit(overlay, (0, 0))
    
    # Victory text
    victory_text = font.render("VICTORY!", True, (255, 255, 0))
    text_rect = victory_text.get_rect(center=(width//2, height//2 - 50))
    game_screen.blit(victory_text, text_rect)
    
    # Score display
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width//2, height//2))
    game_screen.blit(score_text, score_rect)
    
    # Restart button
    restart_button = pygame.Rect(width//2 - 60, height//2 + 30, 120, 40)
    pygame.draw.rect(game_screen, (0, 255, 0), restart_button)
    restart_text = font.render("RESTART", True, (0, 0, 0))
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    game_screen.blit(restart_text, restart_text_rect)
    
    # Quit button
    quit_button = pygame.Rect(width//2 - 60, height//2 + 90, 120, 40)
    pygame.draw.rect(game_screen, (255, 0, 0), quit_button)
    quit_text = font.render("CLOSE", True, (255, 255, 255))
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    game_screen.blit(quit_text, quit_text_rect)
    
    return restart_button, quit_button

def draw_game_over_screen():
    """Draw game over screen"""
    # Semi-transparent black overlay
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    game_screen.blit(overlay, (0, 0))
    
    # Game over text
    game_over_text = font.render("GAME OVER!", True, (255, 255, 255))
    text_rect = game_over_text.get_rect(center=(width//2, height//2 - 50))
    game_screen.blit(game_over_text, text_rect)
    
    # Score display
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width//2, height//2))
    game_screen.blit(score_text, score_rect)
    
    # Restart button
    restart_button = pygame.Rect(width//2 - 60, height//2 + 30, 120, 40)
    pygame.draw.rect(game_screen, (0, 255, 0), restart_button)
    restart_text = font.render("RESTART", True, (0, 0, 0))
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    game_screen.blit(restart_text, restart_text_rect)
    
    # Quit button
    quit_button = pygame.Rect(width//2 - 60, height//2 + 90, 120, 40)
    pygame.draw.rect(game_screen, (255, 0, 0), quit_button)
    quit_text = font.render("CLOSE", True, (255, 255, 255))
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    game_screen.blit(quit_text, quit_text_rect)
    
    return restart_button, quit_button

def reset_game():
    """Reset game state"""
    global bird, velocity, pipes, game_over, score, victory
    bird = [40, height//2-50]
    velocity = 0
    pipes = [[200,4]]
    game_over = False
    score = 0
    victory = False

def gameloop():
    global bird, velocity, game_over, score, victory
    
    while True:
        if not game_over and not victory:
            if len(pipes) < 4:
                x= pipes[-1][0]+200
                open_pos = random.randrange(1,9)
                pipes.append([x,open_pos])
            if pipes[0][0] <-100:
                pipes.pop(0)
            
            game_screen.blit(game_background,(0,0))
            draw_bird(bird[0], bird[1])
            
            # Display current score
            score_display = font.render(f"Score: {score}", True, (255, 255, 255))
            game_screen.blit(score_display, (10, 10))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird[1] -= 40
                        velocity = 0
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            velocity += gravity
            bird[1] += velocity
            
            # Check collision
            if not safe():
                game_over = True
            
            # Check victory condition
            if score >= 20:
                victory = True
            
            draw_pipes()
        elif victory:
            # Victory screen
            restart_button, quit_button = draw_victory_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_button.collidepoint(mouse_pos):
                        reset_game()
                    elif quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        else:
            # Game over screen
            restart_button, quit_button = draw_game_over_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_button.collidepoint(mouse_pos):
                        reset_game()
                    elif quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        
        pygame.display.update()
        clock.tick(FPS)

gameloop()
