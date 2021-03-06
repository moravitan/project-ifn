from skltemplate import IfnClassifier
from skltemplate import _csvConveter

clf = IfnClassifier(0.999)
x = []


data = _csvConveter.CsvConverter.convert("Credit_full.csv")

clf.fit(data[0], data[1], data[2])
clf.add_training_set_error_rate(data[0], data[1])
clf.network.create_network_structure_file()


z = _csvConveter.CsvConverter.convert_predict("pred_credit.csv")
# -------------- predict will return the classes and write it to file --------------

# print(clf.predict(z)

# -------------- predict_proba will return the probability for every class and write it to file --------------
print(clf.predict_proba(z))

