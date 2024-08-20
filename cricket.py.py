class Team:
    MAX_PLAYERS = 11
    
    def __init__(self):
        self.team_name = ""
        self.p_name = ["Player" + str(i + 1) for i in range(self.MAX_PLAYERS)]
        self.p_run = [0] * self.MAX_PLAYERS
        self.p_status = [0] * self.MAX_PLAYERS
        self.p_ball = [0] * self.MAX_PLAYERS
        self.extra_run = 0

    def init(self):
        self.team_name = input("Enter the team name: ")
        print(f"Enter the number of players: {self.MAX_PLAYERS}")
        print("Enter the name of players:")
        for i in range(self.MAX_PLAYERS):
            self.p_name[i] = input(f"Player {i + 1} Name: ")
            self.p_run[i] = 0
            self.p_status[i] = 0

    def get_name(self, i):
        return self.p_name[i]

    def get_run(self, i):
        return self.p_run[i]

    def get_status(self, i):
        return self.p_status[i]

    def get_extra(self):
        return self.extra_run

    def get_ball(self, i):
        return self.p_ball[i]

    def get_team_name(self):
        return self.team_name

    def get_total(self):
        return sum(self.p_run) + self.extra_run

    def add_runs(self, player_num, run):
        self.p_run[player_num] += run

    def set_status(self, player, status):
        self.p_status[player] = status

    def set_out(self, out_player, type, new_player):
        self.p_status[out_player] = type
        self.p_status[new_player] = 1

    def set_ball(self, player):
        self.p_ball[player] += 1

    def set_extra(self, run):
        self.extra_run += run


class Score(Team):
    MAX_OVERS = 50

    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.ball_count = 0
        self.over = 0
        self.max_over = self.MAX_OVERS
        self.out = 0
        self.max_out = 10
        self.extra = 0
        self.init()
        self.max_over = int(input("Enter the number of overs: "))
        print("Choose opening batsmen:")
        while True:
            self.player1 = int(input("Player 1: ")) - 1
            self.player2 = int(input("Player 2: ")) - 1
            if (self.player1 < 0 or self.player1 >= self.MAX_PLAYERS or
                self.player2 < 0 or self.player2 >= self.MAX_PLAYERS or
                self.player1 == self.player2):
                print("Invalid entry. Try again.")
            else:
                self.set_status(self.player1, 1)
                self.set_status(self.player2, 1)
                break

    def show(self):
        print(f"{self.get_team_name()} Score:")
        for i in range(self.MAX_PLAYERS):
            print(f"{self.get_name(i)}  {self.show_status(self.get_status(i))}  {self.get_run(i)}  ", end="")
            if self.get_status(i):
                print(f"({self.get_ball(i)})", end=" ")
            print()
        print(f"Extra: {self.get_extra()}\n")
        print(f"Over: {self.over}.{self.ball_count}")
        print(f"Wicket: {self.out}")
        print(f"Total score: {self.get_total()}")

        if self.ball_count < 6 and self.over < self.max_over:
            self.choose()

    def show_status(self, i):
        status = {
            0: "",
            1: "not out",
            2: "bold out",
            3: "caught out",
            4: "run out"
        }
        return status.get(i, "unknown")

    def choose(self):
        print("\nChoose option:")
        print("Dot Ball 1  Add Run 2  Extra 3  Wicket 4  Exit 10: ", end="")
        option = int(input())
        
        if option == 1:
            self.dot_ball()
        elif option == 2:
            self.add_run()
        elif option == 3:
            self.extra1()
        elif option == 4:
            self.wicket()
        elif option == 10:
            return
        else:
            print("\nInvalid input")
            self.dot_ball()

    def dot_ball(self):
        print("Dot Ball")
        self.ball_count += 1
        self.set_ball(self.player1)
        if self.ball_count == 6:
            self.over_complete()
        else:
            self.show()

    def extra1(self):
        print("Extra Run")
        self.extra = int(input("Extra? "))
        self.set_extra(self.extra)
        self.show()

    def add_run(self):
        print("Add Run")
        runs = int(input("Runs? "))
        self.ball_count += 1
        self.set_ball(self.player1)
        self.add_runs(self.player1, runs)

        if runs == 1 or runs == 3:
            # Change position of batsmen
            self.player1, self.player2 = self.player2, self.player1
        
        if self.ball_count == 6:
            self.over_complete()
        else:
            self.show()

    def over_complete(self):
        print("Over Complete")
        self.over += 1
        self.ball_count = 0
        # Change position of batsmen
        self.player1, self.player2 = self.player2, self.player1
        
        if self.over == self.max_over:
            print("Inning Complete")
            self.show()
        else:
            self.show()

    def wicket(self):
        print("Wicket")
        o_type = int(input("Out type? (Bold-1 Caught-2 Run_out-3) "))
        self.out += 1
        self.ball_count += 1
        self.set_ball(self.player1)
        
        if self.out == self.max_out:
            print("Inning Complete")
            self.show()
            return
        
        self.player1 = int(input("New Batsman's number: ")) - 1
        self.set_out(self.player1, o_type + 1, self.player1)
        
        if self.ball_count == 6:
            self.over_complete()
        else:
            self.show()


if __name__ == "__main__":
    game = Score()
    game.show()
