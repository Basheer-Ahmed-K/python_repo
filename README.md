1. The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example:
marks key: value pairs are
‘alpha’:[20, 30, 40]
‘beta’:[30, 50, 70]
query_name = ‘beta’

The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.

Input Format:
The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space.
The final line contains query_name, the name of a student to query.

Constraints:
2 ≤ n ≤ 10
0 ≤ marks[i] ≤ 100
length of the marks array = 3

Output Format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

2. Given the participants’ score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2 ≤  n ≤  10
-100 ≤  A[i] ≤ 100
Output Format
Print the runner-up score.