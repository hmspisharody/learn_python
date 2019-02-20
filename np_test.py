import numpy as np
import pandas as pd

student_dt = np.dtype([('name','S20'), ('age','i1'), ('marks','f4')])
student_details = np.array([('Hari', 29, 99.8), ('Madhav', 28, 97.5), ('Sameer', 26, 99.4), ('Anoop', 29, 97.65)], dtype=student_dt)
print(student_details)

