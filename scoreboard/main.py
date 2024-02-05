import curses

class BasketballScoreboard:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.home_team = self.get_team_name("Enter home team name (default: Home): ") or "Home"
        self.guest_team = self.get_team_name("Enter guest team name (default: Guest): ") or "Guest"
        self.score_font_size = self.get_font_size("Enter font size for scores (default: 10): ") or 10
        self.team_font_size = self.get_font_size("Enter font size for team names (default: 10): ") or 10
        self.home_score = 0
        self.guest_score = 0
        self.init_curses()

    def get_team_name(self, prompt):
        self.stdscr.addstr(prompt)
        self.stdscr.refresh()
        return self.stdscr.getstr().decode("utf-8")

    def get_font_size(self, prompt):
        self.stdscr.addstr(prompt)
        self.stdscr.refresh()
        return int(self.stdscr.getstr().decode("utf-8") or 10)

    def init_curses(self):
        curses.curs_set(0)  # Hide the cursor
        curses.noecho()     # Disable automatic echoing of keys
        curses.cbreak()     # Disable line buffering
        self.stdscr.clear()
        self.stdscr.refresh()

    def display_scoreboard(self):
        self.stdscr.clear()

        # Display home team
        home_team_format = "{:^" + str(curses.COLS // 2 - 2) + "}"
        self.stdscr.addstr(1, 2, home_team_format.format(self.home_team), curses.A_BOLD )

        # Display guest team
        guest_team_format = "{:^" + str(curses.COLS // 2 - 2) + "}"
        self.stdscr.addstr(1, curses.COLS // 2 + 2, guest_team_format.format(self.guest_team), curses.A_BOLD )

        # Display scores with custom font size and centered
        score_format = "{:^" + str(curses.COLS // 2 - 2) + "}"
        self.stdscr.addstr(3, 2, score_format.format(str(self.home_score)), curses.A_BOLD )
        self.stdscr.addstr(3, curses.COLS // 2 + 2, score_format.format(str(self.guest_score)), curses.A_BOLD )

        # Display help prompt
        self.stdscr.addstr(curses.LINES - 2, 2, "Home +1/-1 (q/a), Guest +1/-1 (i/k), ESC to quit")

        self.stdscr.refresh()

    def update_score(self, team, increment):
        if team == 'home':
            self.home_score += increment
        elif team == 'guest':
            self.guest_score += increment

    def run_game(self):
        self.display_scoreboard()

        while True:
            user_input = self.stdscr.getch()

            if user_input == 27:  # 27 is the ASCII code for the 'Esc' key
                break  # Exit the loop and end the program
            elif user_input == ord('q'):
                self.update_score('home', 1)
            elif user_input == ord('a'):
                self.update_score('home', -1)
            elif user_input == ord('i'):
                self.update_score('guest', 1)
            elif user_input == ord('k'):
                self.update_score('guest', -1)

            self.display_scoreboard()

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: BasketballScoreboard(stdscr).run_game())
