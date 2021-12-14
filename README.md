## Text-Generation-using-RNN

#### This project is about subword segmentation for handing the oov rates of the two language English and Bengali. We aimed to achive the lowest perplexity rate and oov rate. The oov rate for Bengali is more when comapred to English since Bengali is morphologically rich langauge.
#### We have considered three different models for two languages English and Bengali:
#### 1. The S1 model is pure character-level, ie words are segmented as characters and there are no meaningful units.
#### 2. The S2 model is near the character-level, the words with high frequency remain as it is whereas low frequency words are segmented into subwords.
#### 3. The S3 model is near word-level, the words are segmented same as stemming. For example: nearly -> _near _ly

