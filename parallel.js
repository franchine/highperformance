Plotly.d3.csv('all.csv', function (err, rows) {

    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    var allAlg = unpack(rows, "algorithm"),
        allApp = unpack(rows, "app"),
        allBW = unpack(rows, "bw_level"),
        allIP0 = unpack(rows, "ipath_0"),
        allIP1 = unpack(rows, "ipath_1"),
        allPoCap = unpack(rows, "power_cap"),
        allRun = unpack(rows, "runtime"),
        allThrCount = unpack(rows, "thread_count"),
        displayAlg = [],
        listofApps = [],
        displayBW = [],
        displayIP0 = [],
        displayIP1 = [],
        displayPoCap = [],
        displayRun = [],
        displayThrCount = [],
        algColorRange = [],
        appColorRange = [],
        minBW,
        maxBW,
        minIP0,
        maxIP0,
        minIP1,
        maxIP1,
        minPoCap,
        maxPoCap,
        minThrCount,
        maxThrCount;

    function onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
    }

    //getting data
    for (var i = 0; i < allAlg.length; i++) {
        displayAlg.push(allAlg[i]);
        listofApps.push(allApp[i]);
        displayBW.push(allBW[i]);
        displayIP0.push(allIP0[i]);
        displayIP1.push(allIP1[i]);
        displayPoCap.push(allPoCap[i]);
        displayRun.push(allRun[i]);
        displayThrCount.push(allThrCount[i]);
    }

    var uniqueApps = listofApps.filter(onlyUnique);
    var uniqueAlgs = displayAlg.filter(onlyUnique); 
    console.log(uniqueApps);
    console.log(uniqueAlgs);
    var mapApps = new Map(),
        mapAlgs = new Map();
    var algnum = 0.4,
        appnum = 0.2; 

    for (var i = 0; i < uniqueAlgs.length; i++){
        console.log(uniqueAlgs.length);
        mapAlgs.set(uniqueAlgs[i], algnum);
        algnum = algnum + (1 / (uniqueAlgs.length));
    }

    for (var i = 0; i < uniqueApps.length; i++){
        mapApps.set(uniqueApps[i], appnum);
        appnum = appnum + (1 / (uniqueApps.length));
    }
    console.log(mapAlgs);
    console.log(mapApps);

    for (var i = 0; i < allAlg.length; i++){
        algColorRange.push(mapAlgs.get(allAlg[i]));
        appColorRange.push(mapApps.get(allApp[i]));
    }

    //set max & mins for ranges
    minBW = Math.min.apply(null, displayBW);
    maxBW = Math.max.apply(null, displayBW);
    minIP0 = Math.min.apply(null, displayIP0);
    maxIP0 = Math.max.apply(null, displayIP0);
    minIP1 = Math.min.apply(null, displayIP1);
    maxIP1 = Math.max.apply(null, displayIP1);
    minPoCap = Math.min.apply(null, displayPoCap);
    maxPoCap = Math.max.apply(null, displayPoCap);
    minRun = Math.min.apply(null, displayRun);
    maxRun = Math.max.apply(null, displayRun);
    minThrCount = Math.min.apply(null, displayThrCount);
    maxThrCount = Math.max.apply(null, displayThrCount);

    var data = [{
        type: 'parcoords',
        pad: [80, 80, 80, 80],
        line: {
            color: appColorRange,
            colorscale: "Greens"
        },

        dimensions: [
            {
                range: [minBW, maxBW],
                label: "Badwidth Level",
                values: displayBW
            },
            {
                range: [minIP0, maxIP0],
                label: "IPath 0",
                values: displayIP0
            },
            {
                label: "IPath 1",
                range: [minIP1, maxIP1],
                values: displayIP1
            },
            {
                label: "Power Cap",
                range: [minPoCap, maxPoCap],
                values: displayPoCap
            },
            {
                label: "Runtime",
                range: [minRun, maxRun],
                values: displayRun
            },
            {
                label: "Thread Count",
                range: [minThrCount, maxThrCount],
                values: displayThrCount
            }
        ]
    }];
    var layout = {
        title: "Parallel Coordinates",
        width: 800,
        height: 550
    };

    Plotly.plot('parCoordsContain', data, layout);

});