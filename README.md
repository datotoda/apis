# Chucknorris Api

chucknorris.py პროგრამის გაშვებისას ტერმინალში იბეჭდება ხუმრობა ჩაკ ნორისზე და მომხმარებელს აქ არჩევანი ნახოს მთლიანი API-ის პასუხი, ხოლო შემდეგ სურვილის შემთხვევაში შეინახოს ბაზაში. 

---

## საჭირო მოდულების ინსტალაცია

``$ pip install -r requirements.txt``

## გამოყენების მაგალითი

``$ python chucknorris.py``
```
Response:       
status code: 200
headers:        
Date: Wed, 04 May 2022 17:32:28 GMT         
Content Type: application/json;charset=UTF-8
                                            
Joke:                                       
Chuck Norris is a proud sponsor of death!   
                                            
Do you want full json? (y / n)              
> y                                         
{                                                                             
    "categories": [],                                                         
    "created_at": "2020-01-05 13:42:25.628594",                               
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "pFoxZAFaSRais9-SHBJlMg",                                           
    "updated_at": "2020-01-05 13:42:25.628594",                               
    "url": "https://api.chucknorris.io/jokes/pFoxZAFaSRais9-SHBJlMg",         
    "value": "Chuck Norris is a proud sponsor of death!"                      
}                                                                             

Do you want to save? (y / n)
> n
```

---


# Currencies Api

currencies.py პროგრამის გაშვებისას ტერმინალში გამოდის დიალოგური რეჟიმი, სადაც შეგიძლიათ აირჩიოთ რა თარიღის მიხედვით რა ინფორმაცია გინდათ. ასევე შესაძლებელია პროგრამას გაშვებისას გადაეცეს გარკვეული არგუმენტები. იხილეთ მაგალითები.

---

## საჭირო მოდულების ინსტალაცია

``$ pip install -r requirements.txt``

## გამოყენების მაგალითები

### მაგალითი 1

``$ python currencies.py``
```
choice time:       
(1) - specific date
(2) - latest  
```

``> 2``
```
(1) - all currencies
(2) - one valute
(3) - get currency
(4) - convert 
```

``> 3``
```
from: 
```

``> usd``
```
to: 
```

``> gel``
```
{
    "date": "2022-05-04",
    "gel": 3.034985
} 
```


### მაგალითი 2



``$ python currencies.py eur gel``
```
{
    "date": "2022-05-04",
    "gel": 3.193882
}
```

``$ python currencies.py 300 usd gel``
```
910.5 gel
```



