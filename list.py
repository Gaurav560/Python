nums=[122,22,45,4,5,6,76,7];
print(nums)

mil=[nums,4554,3462];
print(mil);
# to insert a particular element at a particular index
nums.insert(2,666);
print(nums)
# to delete a particular element
nums.remove(666);
print(nums)
#to delete last element
nums.pop();
print(nums);
#to delete from index 2
del nums[2:];
print(nums);

# to get the minimum value
print(min(nums));

print(nums);

# to get the maximum value
print(max(nums));

#to get the sum  of all the values in the list
print(sum(nums));

#to sort all the values in ascending order
nums.sort();
print(nums);