function tournamentWinner(competitions, results) {
    // Write your code here.
    let scores = {}
    let i = 0;
    for (let comp of competitions) {
        let [homeTeam, awayTeam] = comp;
        // 0 - away team
        // 1 - home team
        let result = results[i]
        if (result === 0) {
            scores[awayTeam] = (scores[awayTeam] || 0) + 1;
        } else {
            scores[homeTeam] = (scores[homeTeam] || 0) + 1;
        }
        i++;
    }
    let winner = '';
    let highest = -Infinity;
    for (let team in scores) {
        if (scores[team] > highest) {
            highest = scores[team];
            winner = team;
        }
    }
    return winner;
}
