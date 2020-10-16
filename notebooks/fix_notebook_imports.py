"""
import this file within a given jupyter notebook to allow imports from the project root dir instead of notebooks dir
e.g., 
Run ```import fix_notebook_imports```
```from <package_name> import util``` is now possible 
"""

import os
import sys

module_path = os.path.abspath(os.path.join(".."))
if module_path not in sys.path:
    sys.path.append(module_path)
