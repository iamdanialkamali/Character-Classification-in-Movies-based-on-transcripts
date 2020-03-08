# LanguageModel

ba estefade az **SRILM** va dastoore 
**language-model** haro baraye n-gram misazim



`./ngram-count -text [source_file]  -order m -addsmooth 1 -lm [language_model_file]`

# Perplexity


ba estefade az dastoorz zir **perplexity** ro mohasebe mikoim va dar file minevisim

`./ngram -lm [Language_model_file] -ppl  [taregt_file] > result.txt `


vali formuli ke ostad ke gofte bood ba ooni ke toye doc bood farq mikone pas perplexity ha farq mikone
## DOC
[http://www.speech.sri.com/projects/srilm/manpages/srilm-faq.7.html]
linke doc