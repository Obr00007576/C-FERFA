import os
import pandas as pd
import librosa
import glob
import numpy as np
from tensorflow.keras.models import model_from_json
import operator

emos=["female_angry","female_calm","female_fearful","female_happy","female_sad","male_angry","male_calm","male_fearful","male_happy","male_sad"]
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("saved_models/Emotion_Voice_Detection_Model.h5")
print("Loaded model from disk")
 

data, sampling_rate = librosa.load('output10.wav')
X, sample_rate = librosa.load('output10.wav', res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
sample_rate = np.array(sample_rate)
mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
featurelive = mfccs
livedf2 = featurelive
livedf2= pd.DataFrame(data=livedf2)
livedf2 = livedf2.stack().to_frame().T
twodim= np.expand_dims(livedf2, axis=2)
livepreds = loaded_model.predict(twodim,batch_size=32,verbose=1)[0]
emo_dict={}
for i in range(0,len(emos)):
    emo_dict[emos[i]]=livepreds[i]
sorted_x = sorted(emo_dict.items(), key=operator.itemgetter(1))
sorted_x.reverse()
print(sorted_x[0][0])