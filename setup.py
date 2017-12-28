#steup file for ugates(universal gates)


from setuptools import setup

setup(
    name="ugates",                #name of command
    version='10.0',              #use different veesion name for each
    py_modules=['ugates'],        #python script to be included
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ugates=ugates:gates        
    ''',
)
 #'command'='python_script':'function_name'
