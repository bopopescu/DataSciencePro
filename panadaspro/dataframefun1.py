import pandas as pd
info1 = pd.DataFrame({"x":[25,15,12,19],
                    "y":[47, 24, 17, 29]})
Info2 = pd.DataFrame({"x":[25, 15, 12],
                    "y":[47, 24, 17],
                    "z":[38, 12, 45]})
print(info1.append(Info2, ignore_index = True,sort=True))
