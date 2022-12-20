# Created by Hansi at 12/16/2022

import json

predictions = [141.6638, 148.0821, 152.7391, 150.4859, 164.362, 154.0438, 189.0814, 158.2101, 188.8857, 136.9342,
               162.6193, 146.4478, 164.132, 164.0043, 106.8663, 124.5214, 122.1789, 160.0563, 182.0148, 145.097]

data = []
for pred in predictions:
    data.append({'prediction': pred})

print(data[0:5])

submission_file_path = "submission.json"
with open(submission_file_path, 'w') as fp:
    fp.write('\n'.join(json.dumps(i) for i in data))
