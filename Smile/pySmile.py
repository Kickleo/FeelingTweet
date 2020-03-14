import os
import string
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from tkinter import *

__all__ = ['Smile']



class Smile():


  def __init__(self,text):

    
      happy=[]
      unhappy=[]

      f = open("positive_dico.txt",'r')
      happy=f.readlines()
  


      f = open("negative_dico.txt",'r')
      unhappy=f.readlines()
 




  
      unhappy = [x.replace('\n', '') for x in unhappy]
      unhappy=[x.lower() for x in unhappy]

      happy = [x.replace('\n', '') for x in happy]
      happy=[x.lower() for x in happy]

   
      negative_word=[]
 
      o=[]
      c=[]
      positive_word=[]
      a=""
      content_french=[]
      content_french.append(text)
    
      for i in content_french:
     
              res=i.split()
        
              res=[x.lower() for x in res]
              
        

              print(res)
              o=[i for i in res if i in happy]
              print(o)
              positive_word=positive_word+o
              r=[i for i in res if i in unhappy]
              print(r)
              negative_word=negative_word+r
           
              a=i

              c=re.findall(r"[\w']+",a)

          
      v=''
      w=''
      print(c)
      for i in res:
        if not i in c:
         if i in happy:
          [s + i for s in positive_word]
         if i in unhappy:
          [s + i for s in negative_word]
      for i in c:
        result = re.search('(erai|eras|era|ions|iepositive_word|ent)',i)
        if result:
          v=i
          w=v.replace('erai','er').replace('ions','er').replace('iepositive_word','er').replace('ent','er').replace('era','er').replace('eras','er')
          if w in happy:
            [s + i for s in positive_word]
          if w in unhappy:
            [s + i for s in negative_word]      
      
          print(w)
          print(v)

      count=(len(positive_word))
      print("nombre de mot postitif",count)
      print("nombre de mot négatfi",len(negative_word))
      print("pourcentage mot positif",(count/(len(negative_word)+count))*100,"%")
      print("pourcentage mot négatif",(len(negative_word)/(len(negative_word)+count))*100,"%")
      cp=(count/(len(negative_word)+count))*100
      cn=(len(negative_word)/(len(negative_word)+count))*100

      if len(positive_word) > len(negative_word):
        print("L'analyse des sentiments de la phrase est : positif")
      if len(positive_word) < len(negative_word) :
        print("L'analyse des sentiments de la phrase est : negatif")
      if len(positive_word) == len(negative_word):
        print("L'analyse des sentiments de la phrase est : neutre")

  def interface(self,text):
      happy=[]
      unhappy=[]

      f = open("positive_dico.txt",'r')
      happy=f.readlines()
  


      f = open("negative_dico.txt",'r')
      unhappy=f.readlines()
 




  
      unhappy = [x.replace('\n', '') for x in unhappy]
      unhappy=[x.lower() for x in unhappy]

      happy = [x.replace('\n', '') for x in happy]
      happy=[x.lower() for x in happy]

   
      negative_word=[]
 
      o=[]
      c=[]
      positive_word=[]
      a=""
      content_french=[]
      content_french.append(text)
    
      for i in content_french:
     
              res=i.split()
        
              res=[x.lower() for x in res]
              
        

              print(res)
              o=[i for i in res if i in happy]
              print(o)
              positive_word=positive_word+o
              r=[i for i in res if i in unhappy]
              print(r)
              negative_word=negative_word+r
           
              a=i

              c=re.findall(r"[\w']+",a)

          
      v=''
      w=''
      print(c)
      for i in res:
        if not i in c:
         if i in happy:
          [s + i for s in positive_word]
         if i in unhappy:
          [s + i for s in negative_word]
      for i in c:
        result = re.search('(erai|eras|era|ions|iepositive_word|ent)',i)
        if result:
          v=i
          w=v.replace('erai','er').replace('ions','er').replace('iepositive_word','er').replace('ent','er').replace('era','er').replace('eras','er')
          if w in happy:
            [s + i for s in positive_word]
          if w in unhappy:
            [s + i for s in negative_word]      
      
          print(w)
          print(v)

      count=(len(positive_word))
      print("nombre de mot postitif",count)
      print("nombre de mot négatfi",len(negative_word))
      
      #print("pourcentage mot positif",(count/(len(negative_word)+count))*100,"%")
  
       
      if len(negative_word) != 0 and len(positive_word) !=0:
         cn=(len(negative_word)/(len(negative_word)+count))*100
         cp=(count/(len(negative_word)+count))*100
         print("pourcentage mot positif ",cn)
         print("pourcentage mot negatif",cp)

      else : 
        cn=0
        cp=0


      if len(positive_word) > len(negative_word):
        print("L'analyse des sentiments de la phrase est : positif")
      if len(positive_word) < len(negative_word) :
        print("L'analyse des sentiments de la phrase est : negatif")
      if len(positive_word) == len(negative_word):
        print("L'analyse des sentiments de la phrase est : neutre")
    
     #print(positive_word)
     
      def aler2():

  
        labels = 'Positif', 'Negatif', 
        sizes = [cp, cn]
        colors = ['yellowgreen', 'gold']

        plt.pie(sizes, labels=labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')

        plt.savefig('PieChart01.png')
        plt.show()

      
      def aler():

        #convert list to string and generate
        if len(positive_word)>=1:
          unique_string=(" ").join(positive_word)
          wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
          plt.figure(figsize=(15,8))
          plt.imshow(wordcloud)
          plt.axis("off")
          plt.savefig("your_file_name"+".png", bbox_inches='tight')
          plt.show()
          plt.close()
        else : print("veuillez inséré u ntweet avec au moins un mot positif")
      def aler1():
        if len(negative_word)>=1:
          unique_string=(" ").join(negative_word)
          wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
          plt.figure(figsize=(15,8))
          plt.imshow(wordcloud)
          plt.axis("off")
          plt.savefig("your_file_name"+".png", bbox_inches='tight')
          plt.show()
          plt.close()

        else: print("veuillez inséré un tweet avec au moins un mot négatif")
      
      fenetre = Tk()

      def alert():
         showinfo("alerte", "Bravo!")

      menubar = Menu(fenetre)
      photo = PhotoImage(file="unnamed.png")

      canvas = Canvas(fenetre,width=350, height=200)
      canvas.create_image(0, 0, anchor=NW, image=photo)
      canvas.pack()

      menu1 = Menu(menubar, tearoff=0)
      menu1.add_command(label="mot positif", command=aler)
      menu1.add_command(label="mot négatif", command=aler1)
      menu1.add_command(label="graphique", command=aler2)
      menu1.add_separator()
      menu1.add_command(label="Quitter", command=fenetre.quit)
      menubar.add_cascade(label="Fichier", menu=menu1)

      menu2 = Menu(menubar, tearoff=0)
      menu2.add_command(label="Couper", command=alert)
      menu2.add_command(label="Copier", command=alert)
      menu2.add_command(label="Coller", command=alert)
      menubar.add_cascade(label="Editer", menu=menu2)

      menu3 = Menu(menubar, tearoff=0)
      menu3.add_command(label="A propos", command=alert)
      menubar.add_cascade(label="Aide", menu=menu3)

      fenetre.config(menu=menubar)
      fenetre.mainloop()
if __name__ == '__main__':
    test = Smile("Ma classe fonctionne bien, c'est :( ;) bien délice méchant sympathique non ?")
    test.interface("Ma classe fonctionne bien, c'est :( ;) .Crainte régal coronavirus Crainte délice méchant sympathique non ?")
    