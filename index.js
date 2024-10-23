// Use fetch to load the JSON file
async function provideTextDocument(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
}

function calculateRgbDistance(rgb1, rgb2) {
    return Math.sqrt(rgb1.reduce((sum, a, idx) => sum + Math.pow(a - rgb2[idx], 2), 0));
}

function findNearestBlock(data, targetRgb) {
    let nearestBlock = null;
    let nearestDistance = Infinity;

    data.forEach(block => {
        const currentDistance = calculateRgbDistance(block.rgb, targetRgb);
        if (currentDistance < nearestDistance) {
            nearestDistance = currentDistance;
            nearestBlock = block;
        }
    });

    return nearestBlock;
}

const targetRgb = [254, 24, 254];
provideTextDocument('blockcolors.json')
    .then(data => {
        const nearestBlock = findNearestBlock(data, targetRgb);
        if (nearestBlock) {
            console.log(`The block nearest to ${JSON.stringify(targetRgb)} is:`);
            console.log(JSON.stringify(nearestBlock, null, 4));
        } else {
            console.log("No blocks found.");
        }
    })
    .catch(error => {
        console.error('Error loading the JSON file:', error);
    });
