def main():
    print("Welcome to the min final grade calculator!")
    print("Use this to find the minimum grade you need on your final to earn your desired grade")
    currentGrade = 0
    currentWeight = 0
    while True:
        categoryWeight = float(input(
            "Enter how much the grade category is worth in decimal form or 0 to continue: (Ex. if a project is worth 30% of your grade, enter 0.3)\n"))
        if categoryWeight == 0:
            finalWeight = float(input("Enter how much your final is worth in decimal form:\n"))
            totalWeight = currentWeight + finalWeight
            if totalWeight != 1:
                print(
                    f'Your final and your other grades only add up to a weight of {totalWeight}, did you forget a category maybe? or typo how much one was worth?')
                continue
            break
        stringGrade = input(
            "Enter your grade for that category as a fraction OR in decimal form: (Ex. if you got 75/100 on the project, enter 75/100 OR 0.75)\n")
        splitGrade = stringGrade.split('/')
        if len(splitGrade) == 1:
            categoryGrade = float(splitGrade[0])
        else:
            categoryGrade = float(splitGrade[0]) / float(splitGrade[1])
        weightedCategoryGrade = categoryWeight * categoryGrade
        currentGrade += weightedCategoryGrade
        currentWeight += categoryWeight
        print(f'current grade: {currentGrade}')
    while True:
        desiredGrade = float(input("Enter your desired overall class grade in decimal form or 0 to quit:\n"))
        if desiredGrade == 0:
            break
        requiredPoints = desiredGrade - currentGrade
        requiredFinalGrade = requiredPoints / finalWeight
        print(
            f'In order to get a(n) {desiredGrade} in the class, the minimum grade you need on the final is a(n) {requiredFinalGrade}')


if __name__ == '__main__':
    main()
