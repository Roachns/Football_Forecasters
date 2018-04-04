var teamA,
    teamB;

function optionChanged() {
    let value = document.getElementById(this.id).value;

    if(this.id == 'team-a') {
        teamA = value;
    }
    else if (this.id == 'team-b') {
        teamB = value;
    }
}

function submitButton() {
    var element = document.getElementById("chart");
    element.innerHTML = "";

    plot_donut(teamA, teamB);

}

createDropdowns();

function createDropdowns() {
    var teams_route = '/teams/';
    
    d3.json(teams_route, function(error, data) {
        if (error) throw error;

        d3.select('#dropdown-a')
            .append('select')
            .attr('id','team-a')
            .on('change', optionChanged)
            .selectAll('option')
            .data(data)
            .enter()
            .append('option')
            .attr('value', d => d['TEAM'])
            .text(d => d['NAME'])

        d3.select('#dropdown-b')
            .append('select')
            .attr('id','team-b')
            .on('change', optionChanged)
            .selectAll('option')
            .data(data)
            .enter()
            .append('option')
            .attr('value', d => d.TEAM)
            .text(d => d.NAME)
    });

}