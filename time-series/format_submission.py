# Created by Hansi at 12/16/2022

import json

predictions = [141.6638, 148.0821, 152.7391, 150.4859, 164.362]

data = []
for pred in predictions:
    data.append({'prediction': pred})

print(data[0:5])

submission_file_path = "submission.json"
with open(submission_file_path, 'w') as fp:
    fp.write('\n'.join(json.dumps(i) for i in data))
