import os
cars = ["Ford", "Volvo", "BMW"]
carss = [f"\t\"{car}\"" for _, car in enumerate(cars)]
c_code=f'char *myArray[] = {{{os.linesep}{f",{os.linesep}".join(carss)}{os.linesep}}};'

print(f'{c_code}')
