local function rollDice(diceAmount, diceType)
    local amount = 0
    for i = diceAmount, 1, -1 do
        amount = amount + math.random(1, diceType)
    end
    return amount
end

local function caculateAverage(accuracy, diceAmount, diceType)
    local result = 0
    if accuracy >= 1 then
        warn("Accuracy Must Be A Value Above 1")
    end
    for i = accuracy, 1, -1 do
        result = result + rollDice(diceAmount, diceType)
    end
    result = result / accuracy
    return result
end

print(caculateAverage(1000, 100, 2))
