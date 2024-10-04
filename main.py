
import os
  
def run_main_code_source():
    import pygame
    import mygemma as mygeam

    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Chatbot")

    # Load fonts and colors
    font = pygame.font.Font(None, 24)
    text_color = (255, 255, 255)  # White text
    background_color = (0, 0, 0)  # Black background

    # Function to display text on the screen
    def display_text(text, x, y):
        text_surface = font.render(text, True, text_color)
        screen.blit(text_surface, (x, y))

    # Define input box class
    class InputBox:
        def __init__(self, x, y, w, h, text=""):
            self.rect = pygame.Rect(x, y, w, h)
            self.color_inactive = (255, 255, 255)  # White background
            self.color_active = (0, 255, 0)  # Green background (active)
            self.color = self.color_inactive
            self.text = text
            self.txt_surface = font.render(text, True, text_color)
            self.active = False

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                    self.color = self.color_active if self.active else self.color_inactive
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        self.text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.txt_surface = font.render(self.text, True, text_color)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    # Main game loop
    running = True
    input_box = InputBox(100, screen_height - 40, 140, 32)
    response = ""  # Initialize response variable
    chat_history = []  # Store chat history
    scroll_offset = 0  # For scrolling

    while running:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                running = False
            input_box.handle_event(event)

            # Process input only when Enter is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                response = mygeam.askbot(input_box.text)
                input_box.text = ""  # Clear input box
                chat_history.append((input_box.text, response))

        # Clear the screen
        screen.fill(background_color)

        # Draw input box and response
        input_box.draw(screen)

        # Calculate response position based on chat history
        response_y = screen_height - input_box.rect.height - 20 - scroll_offset
        display_text(response, 50, response_y)

        # Draw chat history (adjusting scroll offset as needed)
        y_offset = 50
        for message in chat_history:
            if y_offset + 30 >= screen_height - input_box.rect.height - 20:
                scroll_offset += 30
            display_text(message[0], 50, y_offset - scroll_offset)
            display_text(message[1], 150, y_offset - scroll_offset)
            y_offset += 30

        # Update the display
        pygame.display.update()

    pygame.quit()
import sys
import pygame


HEIGHT ,WIDTH =500 ,800

screen =pygame.display.set_mode((HEIGHT ,WIDTH))
pygame.display.set_caption("Choose")
screen_width = screen.get_width()
screen_height =screen.get_height()
button_width = 200
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2
button_color = (0, 128, 255)  # Blue
button_hover_color = (0, 0, 255)  # Darker blue
text_color = (255, 255, 255)  # White
pygame.font.init()
font = pygame.font.Font(None, 36)
pygame.font.init()

def backround():
    color =0 ,0 , 0 
    screen.fill(color)

def updater():
    pygame.display.update()

def worked():
    run_main_code_source()
running = True
runing =True

while runing:
    updater()
    backround()
    button_text = "Chat bot"
    text_surface = font.render(button_text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (button_x + button_width // 2, button_y + button_height // 2)
    runing =True
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        # Check if the mouse is over the button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:  

            pygame.draw.rect(screen, button_hover_color,  
 (button_x, button_y, button_width, button_height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Button clicked! Perform your desired action here
                worked()
                print("HIII")
        else:
            pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))

    # Draw the button text
    screen.blit(text_surface, text_rect)