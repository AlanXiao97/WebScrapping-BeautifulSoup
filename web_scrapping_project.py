import random
import requests
from bs4 import BeautifulSoup

#Gaming_Logic
def generate_puzzle():
	n=len(quote_text)
	x=random.randint(0,n-1)
	quote=quote_text[x]
	author=author_text[x]
	bio=author_bio[x]
	return [quote,author,bio]

def input_answer():
	answer=input(f"Who said the following quote:{quote}\n")
	return answer

def determine_the_answer(answer,guess_ramaining):
	while guess_ramaining!=-1:
		if answer.lower()==author.lower():
			print("Congratulation! Your answer is correct.\n")
			response=input("Do you want to play again? (y/n) ")
			return response
		else:
			print(f"Incorrect. Please try again!\nYou have {guess_ramaining-1} guesses remained.\n")
			guess_ramaining-=1
			if guess_ramaining==2:
				print(f"Hint-1:{Hint_1}")
				answer=input()
			elif guess_ramaining==1:
				print(f"Hint-2:{Hint_2}")
				answer=input()
			elif guess_ramaining==0:
				print(f"Hint-3:{Hint_3}")
				answer=input()
	print(f"Correct answer is {author}.\n")
	response=input("Do you want to play again? (y/n) ")
	return response

def hint_generator():
	url=requests.get(f"https://quotes.toscrape.com{bio}")
	soup=BeautifulSoup(url.text,"html.parser")
	birth_date=soup.find(class_="author-born-date").get_text()
	birth_location=soup.find(class_="author-born-location").get_text()
	list1=author.split(" ")
	initials=list1[0][0]+list1[1][0]
	Hint_1=f"The birth date of the author is {birth_date}."
	Hint_2=f"The birth location of the author is {birth_location}."
	Hint_3=f"The initials of author is {initials}."
	return [Hint_1, Hint_2, Hint_3]

#Scrapping Part
url=requests.get("https://quotes.toscrape.com/")
i=0
quote_text=[]
author_text=[]
author_bio=[]
while i==0:
	soup=BeautifulSoup(url.text,"html.parser")
	quotes=soup.find_all(class_="quote")
	for quote in quotes:
		quote_text.append(quote.find(class_="text").get_text())
		author_text.append(quote.find(class_="author").get_text())
		author_bio.append(quote.find("a").attrs["href"])
	# turn to next page of the website
	if soup.find(class_="next") != None:
		next_page=soup.find(class_="next")
		next_page_url=next_page.find("a").attrs["href"]
		url=requests.get(f"https://quotes.toscrape.com{next_page_url}")
	else:
		i=1

z=0
while z==0:
	guess_ramaining=3
	puzzle_list=generate_puzzle()
	quote=puzzle_list[0]
	author=puzzle_list[1]
	bio=puzzle_list[2]
	hints=hint_generator()
	Hint_1=hints[0]
	Hint_2=hints[1]
	Hint_3=hints[2]
	answer=input_answer()
	response=determine_the_answer(answer,guess_ramaining)
	if response.lower()=="n":
		z+=1



