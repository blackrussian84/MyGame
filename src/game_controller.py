class GameController:
    def __init__(self):
        self.game_state = "initialized"
        self.score = 0
        self.players = []

    def start_game(self):
        self.game_state = "running"
        self.score = 0
        self.players = self.initialize_players()
        self.run_game_loop()

    def initialize_players(self):
        # Initialize player objects and return them
        return []

    def run_game_loop(self):
        while self.game_state == "running":
            self.handle_player_actions()
            self.update_game_state()
            self.check_game_over()

    def handle_player_actions(self):
        # Handle player inputs and actions
        pass

    def update_game_state(self):
        # Update game state based on player actions and game rules
        pass

    def check_game_over(self):
        # Check if the game is over and update the game state accordingly
        pass

    def end_game(self):
        self.game_state = "ended"
        self.display_final_score()

    def display_final_score(self):
        print(f"Final Score: {self.score}")