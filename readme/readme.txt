Plugin "ASCII Art" for CudaText.
It gives command to render any text via ASCII Art font. Many fonts are available. Uses PyFiglet library.

For example, string "Test..." will be converted to:

  ______          __     
 /_  __/__  _____/ /_    
  / / / _ \/ ___/ __/    
 / / /  __(__  ) /__ _ _ 
/_/  \___/____/\__(_|_|_)

or, with another font:

 _____             _            
(_   _)           ( )_          
  | |   __    ___ | ,_)         
  | | /'__`\/',__)| |           
  | |(  ___/\__, \| |_  _  _  _ 
  (_)`\____)(____/`\__)(_)(_)(_)

Plugin has few commands in Plugins menu.
You can open config file using one of Plugins commands. Details:

- direction: possible values are 'auto', 'left-to-right', 'right-to-left'
- justify: possible values are 'auto' (inherit from direction), 'left', 'right'
- width: has effect when justify is 'right' 

Author: Alexey Torgashin (CudaText)
License: MIT
