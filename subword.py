# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:53:46 2021

@author: akash
"""
import sentencepiece as spm

def trainer(path, vocab, ch, folder='Model/English/'):
    model_pfx= folder+path[:path.index('.')]+'_seg'
    model_file= model_pfx+'.model'
    spm.SentencePieceTrainer.train(input=path, model_prefix=model_pfx, vocab_size= vocab, 
                                   character_coverage=ch, model_type= 'bpe')
    

def encode1(path= 'en_train.txt', folder= 'Model/English/', model= '/home/snlp-project-21/Project/Model/English/en_train_seg.model'):
    file = open(path, encoding='utf-8')
    piece=[]
    sp = spm.SentencePieceProcessor(model_file=model)
    for i in file:
        s= sp.EncodeAsPieces(i)
        piece.append(s)
    seg_file= folder+path[:path.index('.')]+'_seg.txt'
    with open(seg_file, "w", encoding="utf-8") as f:
        for i in piece:
            #s1= map(lambda x:x +'\n', i)
            f.write("{}".format(' '.join(i)))
            #f.writelines("'{}'".format(w for w in i))
            f.write('\n')
    f.close()

def decode(path= 'en_train_s1.txt', folder= 'Model/English/', model= '/home/snlp-project-21/Project/Model/English/en_train_seg.model'):
    sp = spm.SentencePieceProcessor(model_file='/home/snlp-project-21/Project/Model/English/en_train_seg.model')
    file= open(path, encoding='utf-8')
    org_file= folder+ path[path.rindex('/'): path.index('.')]+'_org.txt'
    org= open(org_file, 'w', encoding='utf-8')
    for i in file:
        l= [x for x in i if x != ' ']
        d= sp.DecodePieces(l)
        org.write(d)
    org.close()



#sentpiece(path='ben_train.txt')
    
