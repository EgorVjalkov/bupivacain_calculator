from DataBase import DataBase


db = DataBase()
#patient = db.change_patient_with_missing_data_and_get_index()
#print(patient)
db.write_patient_data_to_file(behavior='add')
