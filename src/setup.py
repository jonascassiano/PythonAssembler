from distutils.core import setup
import py2exe
 
setup(console=['assembler.py'])
setup(console=[
    {
        'script': "assembler.py", 
        "icon_resources": [(0,"processor.ico")]
    }
])