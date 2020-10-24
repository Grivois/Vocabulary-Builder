import PyPDF2 
from collections import Counter
import pandas

#A program that runs through a text and counts the number of times words appear to make vocab list
#Supports .txt and some .pdf files

#enter title of file
title = 'Saint-Exupery - Le Petit Prince'

#input file adress       
input_file = 'D:\\LIBRARY\\eBooks\\Saint-Exupery - Le Petit Prince.pdf'

#location to save file
output_file = 'D:\\Personal Study\\Vocab Lists\\'


class Vocab_builder():
    def __init__(self, file):
        self.file = input_file
        self.title = title
        self.text = ''
        self.vocab = None
        
    def title(self):
         filename = self.split('/')
         filetitle = filename[-1].split('.')
         return filetitle[0]

    def txt(self):
        text = ''
        with open(self.file, 'r') as f:
            for line in f:
                for character in line:
                    text += (character.lower())
            f.close()
        return text
        
    def pdf(self):
        pdfReader = PyPDF2.PdfFileReader(self.file)
        num_pages = pdfReader.numPages
        count = 0
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            self.text += pageObj.extractText().lower()   
        return self.text
    
    def vocab_extractor(self):
        words_in_book = self.text.split()
        removetable = str.maketrans('', '', '@#%\'\"?.,!;')
        words_in_book = [s.translate(removetable) for s in words_in_book]        
        x = str(Counter(words_in_book))
        self.vocab = x.split(',')
        return self.vocab   
     
    def vocab_count(self, save_location):     
        word_count = []
        words = []
        
        for line in self.vocab:
            number = []
            word= []            
            for character in line:
                if character.isdigit():
                    number.append(character)    
                if character.isalpha():    
                    word.append(character)        
            snumber = ''.join([str(elem) for elem in number]) 
            sword = ''.join([str(elem) for elem in word])
            word_count.append(snumber)  
            words.append(sword)
            
        with open(save_location + self.title + 'vocab list.CSV', 'w', encoding='utf-8') as w:
           for word,number in zip(words,word_count):
               w.write(word + ',' + number + '\n')  
               
    def run(self, save_location):
        if self.file[-1] == 't':
            y = Vocab_builder
            y.txt(self)
            y.vocab_extractor(self)
            y.vocab_count(self, save_location)
            print('The Vocabulary List is at: ' + save_location + '\\' + self.title + '.CSV')
        elif self.file[-1] == 'f':
            y = Vocab_builder
            y.pdf(self)
            y.vocab_extractor(self)
            y.vocab_count(self, save_location)
            print('The Vocabulary List is at: ' + save_location + '\\' + self.title +'.CSV')
        else:
            print('Invalid file') 
        
#to initiate:        
builder = Vocab_builder(input_file)
builder.run(output_file)
