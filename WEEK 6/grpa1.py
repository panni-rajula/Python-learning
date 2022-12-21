scores_dataset = [{'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 
 'Mathematics': 6, 'Physics': 48, 'Chemistry': 79, 'Biology': 75, 
 'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 55},        {'SeqNo': 2, 'Name': 'Devikalipa', 'Gender': 'M', 'City': 'Munmbai', 
 'Mathematics': 60, 'Physics': 84, 'Chemistry': 79, 'Biology': 75, 
 'Computer Science': 88, 'History': 43, 'Civics': 87, 'Philosophy': 55},            {'SeqNo': 3, 'Name': 'Dabang', 'Gender': 'F', 'City': 'Munmbai', 
 'Mathematics': 6, 'Physics': 84, 'Chemistry': 79, 'Biology': 75, 
 'Computer Science': 88, 'History': 3, 'Civics': 87, 'Philosophy': 55}]
def get_toppers(scores_dataset,subject, gender):
    l = []
    max_subject = 0
    
    for student in range(len(scores_dataset)):
        
        if scores_dataset[student]['Gender'] == gender:
            
            if scores_dataset[student][subject] >= max_subject:
                max_subject = scores_dataset[student][subject]
    for student in range(len(scores_dataset)):
        if scores_dataset[student][subject] == max_subject and scores_dataset[student]['Gender']== gender:
            l.append(scores_dataset[student]['Name'])
    return l
print(get_toppers(scores_dataset,'Mathematics','F'))
#print(scores_dataset[1])