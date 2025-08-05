import pandas as pd

data = {
    'Student': ['Amit', 'Amit', 'Neha', 'Neha', 'Ravi', 'Ravi', 'Sara', 'Sara'],
    'Subject': ['Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English'],
    'Score': [88, 76, 92, 85, 79, 90, 95, 89]
}

df = pd.DataFrame(data)


#Find the average score of each student. Then, return a DataFrame of only those students whose average score is greater than 85.

''' 
Expected Output:
A DataFrame that looks like this:

Student	AverageScore
Neha	88.5
Sara	92.0  '''

average_scores = df.groupby('Student')['Score'].mean().reset_index()
filtered = average_scores[average_scores['Score'] > 85]
print(filtered)