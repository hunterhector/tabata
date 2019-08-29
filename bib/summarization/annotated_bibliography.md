# Papers for Text Generation Evaluation
## Existing Works
1. n-gram matching 
    * BLEU
    * METEOR
    * NIST, CHRF ...

2. Embedding based model: use pretrained embeddings 
    * [MEANT 2.0](http://www.statmt.org/wmt17/pdf/WMT67.pdf) uses pre-trained word embeddings to compute lexical similarity and exploits shallow semantic parses to evaluate structural similarity
    * [Sharma et al.](https://arxiv.org/pdf/1706.09799.pdf) explore using average-pooling and max-pooling on word embeddings to construct sentence-level representation, which is used to compute cosine similarity between hypothesis and reference. 

3. Learning based models: methods require human judgments as supervision, which are necessary for each dataset and costly to obtain.

    * [BEER](https://www.statmt.org/wmt15/pdf/WMT50.pdf) uses a regression model based on character n-grams and word bigrams. 
    * [BLEND](https://www.statmt.org/wmt17/pdf/WMT68.pdf) employs SVM regression to combine 29 existing metrics for English. 
    * [RUSE](https://www.aclweb.org/anthology/W18-6456) uses a multi-layer perceptron regressor on three pre-trained sentence embedding models.

## [Neural Text Summarization : A Critical Evaluation](https://arxiv.org/pdf/1908.08960.pdf). 
> Kryscisnski, W., Keskar, N. S., McCann, B., Xiong, C., & Socher, R. EMNLP 2019

This paper describes several problems in the current summarization evaluation, including problems on the dataset such as layout bias, and problems on the evaluation protocol such as the
poor overlap between the evaluation metric and human judgement. An appendix on the human study is attached which makes this paper more useful to us.

## [BERTSCORE: Evaluating Text Generation with BERT](https://arxiv.org/pdf/1904.09675.pdf)
> ACL 2019

![](https://i.imgur.com/X53g9Mo.png)

This paper proposed to use pre-trained BERT model as the evaluation metric for text generation (MT). It shows better correlation with human judgement compared to other methods.

### Previous Works
* fail to robustly match paraphrases -> use contextualized word embedding to represent each word
* lack of distinction between tokens that are important or unimportant to the meaning of the sentence (e.g. articles might not very important) -> use tf-idf to weight words
* n-gram models fail to capture distant dependencies and penalize semantically- critical ordering changes (A because B vs B because A)-> bert is good at capturing these relations 
