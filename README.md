## Text-Generation-using-RNN

#### This project is about subword segmentation for handling the oov rates of the two languages English and Bengali. We aimed to achive the lowest perplexity rate and oov rate. The oov rate for Bengali is more when compared to English since Bengali is morphologically rich langauge.
#### We have considered three different models for two languages English and Bengali:
#### 1. The S1 model is pure character-level, ie words are segmented as characters and there are no meaningful units.
#### 2. The S2 model is near the character-level, the words with high frequency remain as it is whereas low frequency words are segmented into subwords.
#### 3. The S3 model is near word-level, the words are segmented same as stemming. For example: nearly -> _near _ly
#### The OOV rate for English language is lesser than the Bangali as the vocabulary size of English is less then the Bengali. For English, we achieved the oov rate on origonal corpora as 6 % which got reduced to 3.9 % for S1 Model, 3.6 % for S2 Model, and 4.5 % for S3 model. For Bengali, we achieved the oov rate on origonal corpora as 12 % which got reduced to 9.5 % for S1 Model, 9.3 % for S2 Model, and 9.6 % for S3 model.

