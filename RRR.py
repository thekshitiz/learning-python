
# enter Entry point, stop loss point, profit target

entryPoint = float(input("Enter your entry Point: "))
stopLoss = float(input("Enter your Stop Loss: "))
ProfitTarget = float(input("Enter your Profit Target: "))

# profit - stopLoss distance

profitDistance = ProfitTarget - entryPoint
stopLossDistance = entryPoint - stopLoss

def reward_to_risk ():
    riskToReward = profitDistance / stopLossDistance
    print("The risk to reward ratio is", riskToReward) 
    return;

reward_to_risk()




