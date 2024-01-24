# Created by Hansi at 12/16/2022

import json

predictions = [141.6638, 141.6638, 142.6638, 141.6638, 141.6638]

data = []
for pred in predictions:
    data.append({'prediction': pred})

print(data[0:5])

submission_file_path = "submission.json"
with open(submission_file_path, 'w') as fp:
    fp.write('\n'.join(json.dumps(i) for i in data))
