## Vendor_Coffee_Machine
The machine offers 4 kinds of drinks: Espresso, Latte, Cappuccino, and Americano!  
Each drink have its own ingredients and price.  
The machine can count the money and return change, alert for insufficient resources, refill (using `admin password`),  
and serve the drink to the client!

## *Requirements :*
* Python 3.0 or above.
* Download the code or clone it to your local repository.
* Choose version: 
   * written in functional programming
   * written in Object Oriented Programming 
* Change `admin_password` - this password is used when refilling the machine
* Run the machine on your chosen version using  `coffee_machine_functional.py` or `oop-coffee-machine/main.py`

## *Changing the `admin_password` :* 
In both versions you can find the variable "admin_password" in the beginning of the `main()` function:
```python
def main():
    admin_password = "1234"
```
Change the default value `"1234"`to your preferred password.  
Use this password whenever you need to refill the machine's stock
