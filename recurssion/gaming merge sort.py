class Leaderboard:
    Leaderboard = None

    def __init__(self, leaderboard):
        self.leaderboard = leaderboard

    # using this method you add a score of aew user.
    def add_score(self):
        print("Please enter the user name: ")
        username = str(input())
        print("please enter the corresponding score: ")
        score = int(input())
        key = 1 + max(self.leaderboard.keys())
        self.leaderboard[key] = [str(username), int(score)]
        self.make_leaderboard()

    # This method will make leader board based on score.
    def make_leaderboard(self):
        score_list = [[item[1],[0],item[1],[1]] for item in self.leaderboard.items()]
        #Implement merge sort and replace the line below.
        #Soretd_score_list = sorted(score_list, reverse = True, key= lambda x: x[1])
        self.mergesort(score_list)
        score_list.reverse()
        print(score_list)
        self.leaderboard.clear()
        for key, value in enumerate(score_list):
            self.leaderboard[int(key + 1)] = value

        print(self.leaderboard)


    #This method prints the leaderboard
    def show_leaderboard(self):
        leaderboard_items = self.leaderboard.items()
        for item in leaderboard_items:
            print(str(item[1][0]) + "score: " +str(item[1][1]) + ", and rank: "+ str(item[0]))
