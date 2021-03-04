def standard_dev(dataset):
    mean = average(dataset)
    deviations = [(data - mean)**2 for data in dataset]
    variance = sum(deviations)/len(dataset)

    return variance**0.5


def average(dataset):
    return sum(dataset) / len(dataset)


listA = [4, 6, 9, 2, 7, 6]
listB = [12, 63, 92, 36, 74]
listC = [105, 263, 843, 462, 735]
listD = [1035, 1287, 1721, 1532]

print("Sum of List A :", sum(listA))
print("Average of List A :", "%.2f" % average(listA))
print("Standard deviation of List A :", "%.2f" % standard_dev(listA))

print("Sum of List B :", sum(listB))
print("Average of List B :", "%.2f" % average(listB))
print("Standard deviation of List B :", "%.2f" % standard_dev(listB))

print("Sum of List C :", sum(listC))
print("Average of List C :", "%.2f" % average(listC))
print("Standard deviation of List C :", "%.2f" % standard_dev(listC))

print("Sum of List D :", sum(listD))
print("Average of List D :", "%.2f" % average(listD))
print("Standard deviation of List D :", "%.2f" % standard_dev(listD))
