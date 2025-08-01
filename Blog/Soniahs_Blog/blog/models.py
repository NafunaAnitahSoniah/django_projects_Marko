from django.db import models

# Create your models here.
#models get data from the user and validate it

######DATA TYPES FIELDS ######

## String related data types
# Charfield
#TextField
#EmailField (I want a string, but as an email address)
#URLField (https://refratory.academy)

## Numeric Fields
# Integer Field
# SmallIntegerField, BigIntegerField, PositiveIntegerField (integers of various sizes)
# FloatField and DecimalField (0.23, 32.12)

## Date Fields
#DateField 15/07/2025
#DatetimeField (15/07/2027 10:23am)
#TimeField(10:23:23)

## Boolean Field
#BooleanField (True of False)

##Fiels and Image fields
#FileField
#ImageField

## Relationship Field
#ForeignKey
#Manytomanyfield
#onetoonefield


#a class describes the attributes we expect an item to have
class Blog(models.Model):
    title = models.CharField(max_length=255) #a blog should have a title as a string not longer than 255 characters
    body = models.TextField() #a body should be a text with any amount of characters 
    excerpt = models.TextField()
    author = models.CharField(max_length=15, default='Admin') # admin part means, if the person doesn't fill in their name, just use the Amin's name
    date = models.DateField(auto_now_add=True) #I want a column for dates. But if someone doesn't provide the date, automatically fill in for them that day's date
    image = models.TextField() #image link
    status = models.CharField(default='draft', max_length=15) #either draft or published 
    link = models.TextField()
