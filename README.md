```
                         \(______     ______)/
                         /`.----.\   /.----.`\
                        } /      :} {:      \ { 
                       / {        } {        } \ 
                       } }      ) } { (      { { 
                      / {      /|\}!{/|\      } \ 
                      } }     ( (."^".) )     { { 
                     / {       (d\   /b)       } \ 
                     } }       |\~   ~/|       { { 
                    / /        | )   ( |        \ \ 
                   { {        _)(,   ,)(_        } } 
                    } }      //  `";"`  \\      { { 
                   / /      //     (     \\      \ \ 
                  { {      {(     -=)     )}      } } 
                   \ \     /)    -=(=-     (\    / / 
                    `\\  /'/    /-=|\-\    \`\  //' 
                      `\{  |   ( -===- )   |  }/' 
                        `  _\   \-===-/   /_  '
                    jgs   (_(_(_)'-=-'(_)_)_)
                          `"`"`"       "`"`"`
  (     (                         (   (                      )  (         
  )\ )  )\ )   (     (            )\ ))\ )   (      *   ) ( /(  )\ )   
 (()/( (()/(   )\    )\ )      ( (()/(()/(   )\   ` )  /( )\())(()/(  
  /(_)) /(_)|(((_)( (()/(      )\ /(_))(_)|(((_)(  ( )(_)|(_)\  /(_)) 
 (_))_ (_))  )\ _ )\ /(_))_ _ ((_|_))(_))  )\ _ )\(_(_())  ((_)(_))   
  |   \| _ \ (_)_\(_|_)) __| | | |_ _| |   (_)_\(_)_   _| / _ \| _ \   
  | |) |   /  / _ \   | (_ | |_| || || |__  / _ \   | |  | (_) |   /   
  |___/|_|_\ /_/ \_\   \___|\___/|___|____|/_/ \_\  |_|   \___/|_|_\  

```
This is a compile implementation for INE5426 - Contrução de Compiladores
class in Federal University of Santa Catarina.
 ### Authors:
 - Mateus Favarin da Costa
 - Robson Zagre Junior
 - Wesly Carmesini Ataide

The name was choose as a reference to the book "Compilers: Principles, Techniques, and Tools".

# How to Install

The present code was write in python3, more specific in version 3.9, but we
think that using a version that is >= 3.6 will not create big problems.

Requirements:
```
ply >= 3.11
```

There are two ways to install the requirements to run the project. 

 1. Installing in the local environment using the `requirements.txt` 
```
make install_local
```
2. Installing in a specific environment using `poetry` manager.
```
make install
```
# How to compile a file

To compile a file (In this first version there are only the lexical step) you can execute in terminal:
```
make run file={path/to/file.lcc}
```
Please note that this is a compiler for CC-2021-2 grammar that is represent with `.lcc` extension.
Obs: If a file isn't specified, by default the `lcc/example1.lcc` will be executed.

Currently there are some examples and test codes implemented in CC-2021-2 that are located in `lcc` directory. 

