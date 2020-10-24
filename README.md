# Vocabulary-Builder
Counts words in .txt and some .pdf files, organizing them by highest frequency

A simple python code that converts the text of a .txt or .pdf file into a list of strings.
Each unique word is counted and a new list is created containing the word and it's frequency in the text.
This list is saved as .CSV file.

The code is useful when reading text in foregin languages. It gives an overview of words you'll see in the text. The most frequently occuring words will be the articles (if the language has articles), and this code could easily be modified to exclude the articles, but depending on ones familiarity with the language the articles may be instructive. 


## Example:

### Input
> ### Le Soleil  
> Le long du vieux faubourg, où pendent aux masures  
> Les persiennes, abri des secrètes luxures,  
> ...  
> Dans tous les hôpitaux et dans tous les palais.  

```markdown
#enter title of file
title = 'le soleil'

#input file address       
input_file = 'C:\\Users\\PC-Name\\Desktop\\le soleil.txt'

#location to save file
output_file = 'C:\\Users\\PC-Name\Desktop\\'

builder = Vocab_builder(input_file)
builder.run(output_file)

```
### Output

|Word | Frequency|
|------------ | -------------|
|les | 20|
|et | 11|
|le | 6|
|... | ...|
|valets | 1|
|hôpitaux | 1|
|palais | 1|



