import statistics
datasets = [5, 2, 7, 4, 2, 6, 9]
x = statistics.mean(datasets)
print("Mean is :", x)
datasets2 = [4, -5, 6, 6, 9, 4, 5, -2,5]
print("Median of data-set is : % s "
        % (statistics.median(datasets2)))
dataset3 =[2, 4, 7, 7, 2, 2, 3, 6, 6, 8]

print("Calculated Mode %s" % (statistics.mode(dataset3)))
sample = [7, 8, 9, 10, 11]

print("Standard Deviation of sample is % s "
                % (statistics.stdev(sample)))
set1 = [4, 6, 2, 5, 7, 7,3]
print("Low median of data-set is %s "
        % (statistics.median_low(set1)))
dataset5 = [2, 1, 7, 6, 1]
print("High median of data-set is %s "
        % (statistics.median_high(dataset5)))
