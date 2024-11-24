
from  game_handler import event_loop, character_creator

def test_game_session():
    # Create a character
    character = character_creator()
    character.scalability(50, 25, 5)
    
    # Simulate the event loop
    try:
        event_loop(character)
    except Exception as e:
        print(f"An error occurred during the game session: {e}")

if __name__ == "__main__":
    test_game_session()