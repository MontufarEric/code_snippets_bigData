## 1 Create a list qith 30 random numbers 

import random 

random_list = [random.rand() for i in range(30)]

### 2 Crete a method that returns the name and id of the instance of an object 

def nameAndId(object):
	return(object.name, object.id)

## given an unsorted integer array, find the smallest missing positive integer 

def missingInteger(integerArray):
	for i in range(max(integerArray)):
		if i not in integerArray:
			return i 
	return(max(integerArray)+1)

## 5 difference betweent yield and return 

yield is used in iterators to grab the following value in the sequence. return is used in
 to retrieve a value from a function


# 6 remove duplicates from a list

weekdays = [‘sun’,’mon’,’tue’, ‘sun’,’mon’,’tue’,’wed’,’thu’,’fri’,’wed’,’thu’,’fri’’sat’]

weekdays_unique = lsit(set(weekdays))

## SQL 
# a)  create table quiz1
CREATE TABLE quiz1(
	name VARCHAR(25),
	Id INT );

# b) insert into table 1 record
INSERT INTO quiz1("James", 1001);

# c) Read all data from client 
SELECT * FROM quiz1;

# d) Delete table 
DROP TABLE quiz1;