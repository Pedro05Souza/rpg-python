from gamehandler import event_loop, character_creator

if __name__ == "__main__":
  c = character_creator()
  c.scalability(50, 25, 5)
  event_loop(c)