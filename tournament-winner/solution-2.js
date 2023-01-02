function tournamentWinner(competitions, results) {
    // Write your code here.
    let winner = '';
    let highest = -Infinity;
    let scores = {}
    let i = 0;
    for(let comp of competitions) {
      let [homeTeam, awayTeam] = comp;
      // 0 - away team
      // 1 - home team
      let result = results[i]
      if(result === 0) {
        scores[awayTeam] = (scores[awayTeam] || 0) + 1;
        if(scores[awayTeam] > highest) {
          highest = scores[awayTeam];
          winner = awayTeam;
        }
      } else {
        scores[homeTeam] = (scores[homeTeam] || 0) + 1;
        if(scores[homeTeam] > highest) {
          highest = scores[homeTeam];
          winner = homeTeam;
        }
      }
      i++;
    }
    return winner;
  }
  
  // Do not edit the line below.
  exports.tournamentWinner = tournamentWinner;
  