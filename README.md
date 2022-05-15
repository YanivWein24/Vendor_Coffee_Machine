<img src="https://user-images.githubusercontent.com/97472180/168475388-f4eed0d0-b131-4409-ac21-939e403bc0e4.PNG" alt="Art"/>
 
## *Requirements :*
* Python 3.0 or above.
* Download the code or clone it to your local repository.
* Choose version: 
   * written in functional programming
   * written in Object Oriented Programming 
* Change `admin_password` - this password is used when refilling the machine
* Run the machine on your chosen version using  `coffee_machine_functional.py` or `oop-coffee-machine/main.py`
<br>  
  
## *Features :*
* 4 Different types of coffee beverages
* Resource control - check the machine's stock, and refill at any time! (refill is protected with administrator password)
* If one or more ingredients is insufficient, the machine will abort from making coffee and ask for a stock refill.
* Money machine - calculates the received coins and checks if the amount if sufficient. returns change if necessary.
* Support Quarters, Dimes, Nickles and Pennis as inputs.
<br>  
  
## *Changing the `admin_password` :* 
In both versions you can find the variable "admin_password" in the beginning of the `main()` function:
```python
def main():
    admin_password = "1234"
```
Change the default value `"1234"`to your preferred password.  
Use this password whenever you need to refill the machine's stock  
<br>  
  
## *Screenshots :*
Options:  
<img src="https://user-images.githubusercontent.com/97472180/168475391-9972fbdb-3699-4753-b955-5a83435c3f61.PNG" alt="Options" width="400" height="160"/>
<br>  
Order:  
<img src="https://user-images.githubusercontent.com/97472180/168475392-ec4fc9dc-f72c-46e8-8db9-5c5142b32d85.PNG" alt="Order" width="400" height="160"/>
<br>  
Menu:  
<img src="https://user-images.githubusercontent.com/97472180/168475390-1016ad54-33b7-4f49-a581-c26487c521d5.PNG" alt="Menu" width="250" height="300"/>
<br>  
Report:  
<img src="https://user-images.githubusercontent.com/97472180/168475396-67277cdc-09b1-4b6e-b780-1aa51a7e2f2c.PNG" alt="Report"/>
<br>  
Refill:  
<img src="https://user-images.githubusercontent.com/97472180/168475394-d28064a2-ae5e-4cf4-9dc1-9e538c76b8fa.PNG" alt="Refill" width="450" height="130"/>
<br>  

