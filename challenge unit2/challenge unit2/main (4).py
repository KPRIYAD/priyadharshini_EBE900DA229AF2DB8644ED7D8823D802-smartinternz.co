class player:
  def play(self):
    print("The player is playing cricket")
class Batsman(player):
  def paly(self):
    print("The Batsman is Batting")
class Bowler(player):
  def play(self):
    print("The Bowler is nBowling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()