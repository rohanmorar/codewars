
/* 

8 kyu - Calculate average

Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.

a = [1, 2, 3, 4]

findAverage(a) ---> 10

*/

function findAverage(array) {
  return array.length === 0 ? 0 : array.reduce((sum, num) => sum + num, 0) / array.length;
}
