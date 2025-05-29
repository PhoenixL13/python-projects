#Create Task
#March 17 2025
#Init
from PIL import Image
import requests
from io import BytesIO
import random
import time
salads=["Chicken Caeser Salad","Garden Salad","Caprese Salad"]
saladingredients=["chicken,lettuce,crouton,parmesancheese,oliveoil,lemon,worcestershiresauce,mustard,gar
saladrestrictions=["none","vegan,vegeterian,glutenfree,lactosefree","vegan,vegetarian"]
sandwiches=["BLT","Gluten Free Grilled Cheese","Club Sandwich","Veggie Sandwich"]
sandwichingredients=["bacon,lettuce,tomato,bread","cheddar,bread","avocado,tomato,lettuce,mayo,bread,chi
sandwichrestrictions=["lactosefree","vegetarian,glutenfree","none","vegetarian,vegan,lactosefree"]
soups=["Chicken Noodle Soup","Chili","Tomato Soup"]
soupingredients=["chicken,chickenbroth,noodles,carrot,celery,water","beef,blackbeans,tomato,onion,garlic
souprestrictions=["glutenfree,lactosefree","glutenfree,lactosefree","glutenfree,vegan,vegetarian"]
drinks=["Still Water","Sparkling Water","Soda","Apple Juice","Orange Juice","Strawberry Banana Smoothie"
drinkingredients=["water","water","ingredients vary","water,apple","water,orange","strawberry,banana,mil
drinkrestrictions=["glutenfree,vegan,vegetarian,lactosefree","glutenfree,vegan,vegetarian,lactosefree","
saladphotolinks=["https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_auto,w_728,h_
soupphotolinks =["https://www.bigbearswife.com/wp-content/uploads/2020/05/30-Minute-Pantry-Chicken-Noodl
sandwichphotolinks=["https://dyvn6jpt1f0d3.cloudfront.net/wp-content/uploads/2023/10/14154227/BLT-for-re
drinkphotolinks=["https://sojo.net/sites/default/files/blog/shutterstock_65621872_0.jpg","https://www.ne
recommendeditems=[]
recommendedingredients=[]
finalrecommendations=[]
finalingredients=[]
#Functions
def open_image(url):
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()
def saladselection(): #function allows customers to get a salad reccomendation.
recommendeditems.clear()
recommendedingredients.clear()
print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), la
print(" ")
restriction=input("Enter restriction/choice here:")
if restriction=="V" or restriction=="v": #ensures the customer will recieve a recomendation whether
print("Vegan selected")
print(" ")
time.sleep(1)
for i in range(len(salads)): #if a customer selects vegan, the function will only reccomend a sa
if "vegan" in saladrestrictions[i]:
recommendeditems.append(salads[i])
recommendedingredients.append(saladingredients[i])
4/4/25, 1:52 PM bakerfranke.github.io/codePrint/

https://bakerfranke.github.io/codePrint/ 1/7

print("Generating random salad now...")
time.sleep(1)
elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
print("Vegetarian selected") #tells the customer which dietary restriction they selected after t
print(" ")
time.sleep(1) #gives code a second before selecting salad reccomendation.
for i in range(len(salads)):
if "vegetarian" in saladrestrictions[i]:
recommendeditems.append(salads[i])
recommendedingredients.append(saladingredients[i])
print("Generating random salad now...")
time.sleep(1)
elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
print("Gluten free selected")
print(" ")
time.sleep(1)
for i in range(len(salads)): #reccomends a salad if the customer is gluten free.
if "glutenfree" in saladrestrictions[i]:
recommendeditems.append(salads[i])
recommendedingredients.append(saladingredients[i])
print("Generating random salad now...")
time.sleep(1)
elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
print("Lactose free selected")
print(" ")
time.sleep(1)
for i in range(len(salads)):
if "lactosefree" in saladrestrictions[i]:
recommendeditems.append(salads[i])
recommendedingredients.append(saladingredients[i])
print("Generating random salad now...")
time.sleep(1)
else:
print("No dietary restrictions/choices selected.")
print(" ")
print("Generating random salad now...")
time.sleep(1)
for i in range(len(salads)):
recommendeditems.append(salads[i])
recommendedingredients.append(saladingredients[i])
randomindex=random.randint(0,(len(recommendeditems)-1))
generateditem = recommendeditems[randomindex]
generateditemingredients = recommendedingredients[randomindex]
print(" ")
print("Suggested salad: " + generateditem) #if the customer doesnt select a dietary restriction, the
photoindex = salads.index(generateditem)
open_image(saladphotolinks[photoindex]) #shows customer an image of the food they were recomended
time.sleep(1)
finalrecommendations.append(generateditem)
finalingredients.append(generateditemingredients)
def soupselection():
recommendeditems.clear()
recommendedingredients.clear()
print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), or
print(" ") #allows customer to select their dietary restriction.
4/4/25, 1:52 PM bakerfranke.github.io/codePrint/

https://bakerfranke.github.io/codePrint/ 2/7

restriction=input("Enter restriction/choice here:")
if restriction=="V" or restriction=="v":
print("Vegan selected")
print(" ")
time.sleep(1)
for i in range(len(soups)): #selects a soup if the customer selects vegan.
if "vegan" in souprestrictions[i]:
recommendeditems.append(soups[i])
recommendedingredients.append(soupingredients[i])
print("Generating random soup now...")
time.sleep(1)
elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
print("Vegetarian selected")
print(" ")
time.sleep(1)
for i in range(len(soups)):
if "vegetarian" in souprestrictions[i]:
recommendeditems.append(soups[i])
recommendedingredients.append(soupingredients[i])
print("Generating random soup now...")
time.sleep(1)
elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
print("Gluten free selected")
print(" ")
time.sleep(1)
for i in range(len(soups)):
if "glutenfree" in souprestrictions[i]:
recommendeditems.append(soups[i])
recommendedingredients.append(soupingredients[i])
print("Generating random soup now...")
time.sleep(1)
elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
print("Lactose free selected")
print(" ")
time.sleep(1)
for i in range(len(soups)):
if "lactosefree" in souprestrictions[i]:
recommendeditems.append(soups[i])
recommendedingredients.append(soupingredients[i])
print("Generating random soup now...")
time.sleep(1)
else:
print("No dietary restrictions/choices selected.")
print(" ")
print("Generating random soup now...")
time.sleep(1)
for i in range(len(soups)):
recommendeditems.append(soups[i])
recommendedingredients.append(soupingredients[i])
randomindex=random.randint(0,(len(recommendeditems)-1))
generateditem=recommendeditems[randomindex]
generateditemingredients=recommendedingredients[randomindex]
print(" ")
print("Suggested soup: " + generateditem) #if the customer doesnt select a dietary restriction, they
photoindex = soups.index(generateditem)
open_image(soupphotolinks[photoindex]) #shows customer a picture of the soup they were reccomended

4/4/25, 1:52 PM bakerfranke.github.io/codePrint/

https://bakerfranke.github.io/codePrint/ 3/7

time.sleep(1)
finalrecommendations.append(generateditem)
finalingredients.append(generateditemingredients)
def sandwichselection():
recommendeditems.clear() #Clears list of items from previous selection
recommendedingredients.clear() #Clears list of ingredients from previous selection
print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), or
print(" ")
restriction=input("Enter restriction/choice here:")
if restriction=="V" or restriction=="v":
print("Vegan selected")
print(" ")
time.sleep(1)
for i in range(len(sandwiches)):
if "vegan" in sandwichrestrictions[i]: #Finds all vegan sandwiches
recommendeditems.append(sandwiches[i]) #Adds vegan sandwich to recommended items
recommendedingredients.append(sandwichingredients[i]) #Adds vegan sandwich ingredients t
print("Generating random sandwich now...")
time.sleep(1)
elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
print("Vegetarian selected")
print(" ")
time.sleep(1)
for i in range(len(sandwiches)):
if "vegetarian" in sandwichrestrictions[i]:
recommendeditems.append(sandwiches[i])
recommendedingredients.append(sandwichingredients[i])
print("Generating random sandwich now...")
time.sleep(1)
elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
print("Gluten free selected")
print(" ")
time.sleep(1)
for i in range(len(sandwiches)):
if "glutenfree" in sandwichrestrictions[i]:
recommendeditems.append(sandwiches[i])
recommendedingredients.append(sandwichingredients[i])
print("Generating random sandwich now...")
time.sleep(1)
elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
print("Lactose free selected")
print(" ")
time.sleep(1)
for i in range(len(sandwiches)):
if "lactosefree" in sandwichrestrictions[i]:
recommendeditems.append(sandwiches[i])
recommendedingredients.append(sandwichingredients[i])
print("Generating random sandwich now...")
time.sleep(1)
else:
print("No dietary restrictions/choices selected.")#Warns the user that there are no restrictions
print(" ")
print("Generating random sandwich now...")
time.sleep(1)
for i in range(len(sandwiches)):

4/4/25, 1:52 PM bakerfranke.github.io/codePrint/

https://bakerfranke.github.io/codePrint/ 4/7

recommendeditems.append(sandwiches[i]) #Adds the chosen sandwich to list of items
recommendedingredients.append(sandwichingredients[i]) #Adds ingredients of the sandwiches
randomindex=random.randint(0,(len(recommendeditems)-1)) #Chooses random item and assigns index
generateditem=recommendeditems[randomindex] #Gives item
generateditemingredients=recommendedingredients[randomindex] #Gives ingredients of the item
print(" ")
print("Suggested sandwich: " + generateditem)
photoindex = sandwiches.index(generateditem)
open_image(sandwichphotolinks[photoindex])
time.sleep(1)
finalrecommendations.append(generateditem) #Adds to final list of recommended items at the end
finalingredients.append(generateditemingredients) #Adds to final list of the ingredients of the item
def drinkselection():
recommendeditems.clear()
recommendedingredients.clear()
print("Please select your dietary restrictions/choices(Vegan(V), vegetarian(VG), gluten free(GF), or
print(" ")
restriction=input("Enter restriction/choice here:")
if restriction=="V" or restriction=="v":
print("Vegan selected")
print(" ")
time.sleep(1)
for i in range(len(drinks)):
if "vegan" in drinkrestrictions[i]:
recommendeditems.append(drinks[i])
recommendedingredients.append(drinkingredients[i])
print("Generating random drink now...")
time.sleep(1)
elif restriction=="VG" or restriction=="vg" or restriction=="Vg" or restriction=="vG":
print("Vegetarian selected")
print(" ")
time.sleep(1)
for i in range(len(drinks)):
if "vegetarian" in drinkrestrictions[i]:
recommendeditems.append(drinks[i])
recommendedingredients.append(drinkingredients[i])
print("Generating random drink now...")
time.sleep(1)
elif restriction=="GF" or restriction=="gf" or restriction=="Gf" or restriction=="gF":
print("Gluten free selected")
print(" ")
time.sleep(1)
for i in range(len(drinks)):
if "glutenfree" in drinkrestrictions[i]:
recommendeditems.append(drinks[i])
recommendedingredients.append(drinkingredients[i])
print("Generating random drink now...")
time.sleep(1)
elif restriction=="LF" or restriction=="lf" or restriction=="Lf" or restriction=="lF":
print("Lactose free selected")
print(" ")
time.sleep(1)
for i in range(len(drinks)):
if "lactosefree" in drinkrestrictions[i]:
recommendeditems.append(drinks[i])

4/4/25, 1:52 PM bakerfranke.github.io/codePrint/

https://bakerfranke.github.io/codePrint/ 5/7

recommendedingredients.append(drinkingredients[i])
print("Generating random drink now...")
time.sleep(1)
else:
print("No dietary restrictions/choices selected.")
print(" ")
print("Generating random drink now...")
time.sleep(1)
for i in range(len(drinks)):
recommendeditems.append(drinks[i])
recommendedingredients.append(drinkingredients[i])
randomindex=random.randint(0,(len(recommendeditems)-1))
generateditem = recommendeditems[randomindex]
generateditemingredients=recommendedingredients[randomindex]
print(" ")
print("Suggested drink: " + generateditem)
photoindex = drinks.index(generateditem)
open_image(drinkphotolinks[photoindex])
time.sleep(1)
finalrecommendations.append(generateditem)
finalingredients.append(generateditemingredients)
def itemrecommender(amountofitems):
for i in range(amountofitems):
print(" ")
print("Would you like a salad(1), sandwich(2), soup(3), or drink(4)?")
print(" ")
try:
menugroup=int(input("Please select a choice 1-4."))
except:
print("Please selected a number 1-4")
if menugroup==1:
saladselection()
elif menugroup==2:
sandwichselection()
elif menugroup==3:
soupselection()
elif menugroup==4:
drinkselection()
else:
print("Invalid choice")
print(" ")
print("Restarting recommending process...")
itemrecommender(amountofitems)
time.sleep(1)
print(" ")
print("Your final recommendations: ")
for i in range(len(finalrecommendations)):
print("-" + finalrecommendations[i])
print("(" + finalingredients[i] + ")")
def entiremenurecommender():
print("Hello! Welcome to the Eagle's Nest Cafe.")
print(" ")
time.sleep(1)
print("We use a menu recommender to ensure the best experience!")
4/4/25, 1:52 PM bakerfranke.github.io/codePrint/

https://bakerfranke.github.io/codePrint/ 6/7

PDF document made with CodePrint using Prism
time.sleep(1)
print(" ")
print("How many items will you be ordering today(enter numeric value)?")
itemrecommender(int(input("Enter numeric value here:")))
time.sleep(3)
print(" ")
print("Thank you for using the item recommender. Enjoy your food!")
#Main
entiremenurecommender()
#Photo Sources:
#Chicken Caeser Salad Photo: https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_a
#Garden Salad Photo: https://www.missinthekitchen.com/wp-content/uploads/2020/03/Green-Salad-Recipe-Imag
#Caprese Salad Photo: https://www.thespruceeats.com/thmb/QZtRJibA70fH7B5XKodp_1HTS7k=/750x0/filters:no_u
#Chicken Noodle Soup Photo: https://www.bigbearswife.com/wp-content/uploads/2020/05/30-Minute-Pantry-Chi
#Chili Photo: https://hips.hearstapps.com/hmg-prod/images/beef-chili-lead-6630087a9ab98.jpg?crop=0.99947
#Tomato Soup Photo: https://www.allrecipes.com/thmb/jbodaMY5KLc7g5gHmHMT2MUqjvE=/0x512/filters:no_upscal
#BLT Photo: https://dyvn6jpt1f0d3.cloudfront.net/wp-content/uploads/2023/10/14154227/BLT-for-recipe-1-6-
#Gluten Free Grilled Cheese Photo: https://www.allrecipes.com/thmb/CZ93z2oGv0n9ZsLp5yE2Lgb0Tyk=/0x512/fi
#Veggie Sandwich Photo: https://www.andiemitchell.com/wp-content/uploads/2019/01/best_veggie_sandwich_hu
#Club Sandwich Photo: https://www.seriouseats.com/thmb/0nUt5iaqM54mdfbWRv6A8VrP_Yo=/750x0/filters:no_ups
#Still Water Photo: https://sojo.net/sites/default/files/blog/shutterstock_65621872_0.jpg
#Sparkling Water Photo: https://www.nextlevelurgentcare.com/wp-content/uploads/elementor/thumbs/AdobeSto
#Soda Photo: https://134532506.cdn6.editmysite.com/uploads/1/3/4/5/134532506/s549469990591119337_p28_i3_
#Apple Juice Photo: https://parade.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_700/MjAwNjM4NjE1MDExNz
#Orange Juic Photo: https://images-prod.healthline.com/hlcmsresource/images/AN_images/orange-juice-1296x
#Strawberry Banana Smoothie Photo: https://www.simplyrecipes.com/thmb/YZRqiGDbKwgaw1ayN6LykaoieAA=/750x0
