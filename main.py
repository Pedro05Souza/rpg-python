from gamehandler import event_loop, character_creator

if __name__ == "__main__":
  c = character_creator()
  event_loop(c)