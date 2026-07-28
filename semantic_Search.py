from sentence_transformers import SentenceTransformer

import numpy as np 

''''embeddingg are numerical vector representation of data (text, image, audio, etc...)
 that captuere maening and relationships.'''

sentances =[
    "i like bike",
    "i like  bike color"
]

model =  SentenceTransformer('sentence-transformers/all-MiniLM-L6-V2')

embeddings = model.encode(sentances)

similarity =np.dot(
    embeddings[0],
    embeddings[1]
)

print(f"{similarity *100:.2f}% similar")

