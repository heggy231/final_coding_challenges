
input = [-2, -2, -2, -2, 3, 5];

function maxFrequencyInt(input) {

    let integerFrequencies = {};

    mostOccuringInt = null;
    count = 0;

    for(let i = 0; i < input.length; i ++) {
        if (integerFrequencies[input[i]] !== undefined) {
            integerFrequencies[input[i]] += 1;

        } else {
            integerFrequencies[input[i]] = 1

        }

        if (integerFrequencies[input[i]] > count) {
            count = integerFrequencies[input[i]];
            mostOccuringInt = input[i];
        }
    }

    return mostOccuringInt

}

console.log(maxFrequencyInt(input));