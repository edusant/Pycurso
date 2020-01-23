import pandas as pd

data = {
        'alunos':['Eduardo', 'Lucas', 'Guilherme', 'Leozinho', 'Gabriel', 'Enrique'],
        'idade':[24, 26, 20, 22, 20, 26],
        'notas':[10, 10, 8, 7, 10, 6]
        }


df = pd.DataFrame(data, columns=['alunos', 'idade','notas'])


df.describe()


df.drop(5)

df = df.drop(5)



df.drop('idade', axis=1)