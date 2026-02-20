import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")
        
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 5
        
        self.create_widgets()
    
    def create_widgets(self):
        title_frame = tk.Frame(self.root, bg="#2b2b2b")
        title_frame.pack(pady=10)
        
        title = tk.Label(title_frame, text="ROCK  PAPER  SCISSORS", 
                        font=("Arial", 28, "bold"), 
                        fg="#ffd700", bg="#2b2b2b")
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Click on your weapon!", 
                          font=("Arial", 14), 
                          fg="#888888", bg="#2b2b2b")
        subtitle.pack()
        
        score_frame = tk.Frame(self.root, bg="#2b2b2b", relief="raised", bd=2)
        score_frame.pack(pady=10)
        
        self.score_label = tk.Label(score_frame, 
                                   text="YOU: 0  |  COMPUTER: 0", 
                                   font=("Arial", 18, "bold"),
                                   fg="white", bg="#444444", padx=20, pady=5)
        self.score_label.pack()
        
        game_frame = tk.Frame(self.root, bg="#2b2b2b")
        game_frame.pack(pady=20, expand=True)
        
        player_frame = tk.Frame(game_frame, bg="#2b2b2b")
        player_frame.pack(side=tk.LEFT, padx=50)
        
        tk.Label(player_frame, text="YOUR CHOICE", font=("Arial", 14, "bold"),
                fg="#00ff00", bg="#2b2b2b").pack()
        
        self.player_display = tk.Label(player_frame, text="???", 
                                      font=("Arial", 40, "bold"),
                                      fg="white", bg="#444444", width=10, height=2)
        self.player_display.pack()
        
        vs_frame = tk.Frame(game_frame, bg="#2b2b2b")
        vs_frame.pack(side=tk.LEFT)
        
        tk.Label(vs_frame, text="VS", font=("Arial", 30, "bold"),
                fg="red", bg="#2b2b2b").pack()
        
        computer_frame = tk.Frame(game_frame, bg="#2b2b2b")
        computer_frame.pack(side=tk.LEFT, padx=50)
        
        tk.Label(computer_frame, text="COMPUTER'S CHOICE", font=("Arial", 14, "bold"),
                fg="#ff4444", bg="#2b2b2b").pack()
        
        self.computer_display = tk.Label(computer_frame, text="???",
                                       font=("Arial", 40, "bold"),
                                       fg="white", bg="#444444", width=10, height=2)
        self.computer_display.pack()
        
        self.result_label = tk.Label(self.root, 
                                    text="READY TO PLAY? CLICK A BUTTON!",
                                    font=("Arial", 16, "bold"),
                                    fg="#ffd700", bg="#2b2b2b")
        self.result_label.pack(pady=10)
        
        button_frame = tk.Frame(self.root, bg="#2b2b2b")
        button_frame.pack(pady=30)
        
        rock_btn = tk.Button(button_frame, text="ROCK", font=("Arial", 20, "bold"),
                           command=lambda: self.play("rock"),
                           bg="#2b2b2b", fg="white", width=10, height=2)
        rock_btn.pack(side=tk.LEFT, padx=10)
        
        paper_btn = tk.Button(button_frame, text="PAPER", font=("Arial", 20, "bold"),
                            command=lambda: self.play("paper"),
                            bg="#2b2b2b", fg="white", width=10, height=2)
        paper_btn.pack(side=tk.LEFT, padx=10)
        
        scissors_btn = tk.Button(button_frame, text="SCISSORS", font=("Arial", 20, "bold"),
                               command=lambda: self.play("scissors"),
                               bg="#2b2b2b", fg="white", width=10, height=2)
        scissors_btn.pack(side=tk.LEFT, padx=10)
        
        reset_btn = tk.Button(self.root, text="RESET GAME", 
                            font=("Arial", 12, "bold"),
                            command=self.reset_game,
                            bg="#ff4444", fg="white", padx=20, pady=5)
        reset_btn.pack(pady=10)
    
    def play(self, player_choice):
        if self.rounds_played >= self.max_rounds:
            messagebox.showinfo("Game Over", "Game is finished! Click RESET to play again.")
            return
        
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        self.player_display.config(text=player_choice.upper())
        self.computer_display.config(text=computer_choice.upper())
        
        result = self.determine_winner(player_choice, computer_choice)
        
        if result == "player":
            self.result_label.config(text="YOU WIN!", fg="#00ff00")
        elif result == "computer":
            self.result_label.config(text="COMPUTER WINS!", fg="#ff4444")
        else:
            self.result_label.config(text="IT'S A TIE!", fg="#ffd700")
        
        if result == "player":
            self.player_score += 1
        elif result == "computer":
            self.computer_score += 1
        
        self.rounds_played += 1
        self.update_score()
        
        if self.rounds_played >= self.max_rounds:
            self.root.after(2000, self.show_game_over)
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        
        if player == "rock":
            return "player" if computer == "scissors" else "computer"
        elif player == "paper":
            return "player" if computer == "rock" else "computer"
        else:
            return "player" if computer == "paper" else "computer"
    
    def update_score(self):
        self.score_label.config(text=f"YOU: {self.player_score}  |  COMPUTER: {self.computer_score}")
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.update_score()
        self.player_display.config(text="???")
        self.computer_display.config(text="???")
        self.result_label.config(text="READY TO PLAY? CLICK A BUTTON!", fg="#ffd700")
    
    def show_game_over(self):
        if self.player_score > self.computer_score:
            msg = f"YOU WIN! {self.player_score} - {self.computer_score}"
        elif self.computer_score > self.player_score:
            msg = f"COMPUTER WINS! {self.computer_score} - {self.player_score}"
        else:
            msg = f"IT'S A TIE! {self.player_score} - {self.computer_score}"
        
        messagebox.showinfo("GAME OVER", msg)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()