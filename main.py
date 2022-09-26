from GUI.game import *

if __name__ == "__main__":
    init_game()

    # Binding, setting
    screen.bind("<Button-1>", click_handle)
    screen.bind("<Key>", key_handle)
    screen.focus_set()

    # Run forever
    Root.wm_title("Mini AlphaGo")
    Root.mainloop()

