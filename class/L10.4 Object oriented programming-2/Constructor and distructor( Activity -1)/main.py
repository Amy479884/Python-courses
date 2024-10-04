class Employee:
    # Initializing (Constructor)
     def __init__(self):
         print('Employee created.')

        #Deleating (Destructor)
     def __del__(self):
         print('Descructor called, Employee deleted.')

obj = Employee()
del obj
