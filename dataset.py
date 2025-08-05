import pandas as pd

data = {
    'patient_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008', 'P009', 'P010'],
    'Name': ['viajy', 'aloha', 'john', 'doe', 'eswar', None, 'lisa', 'ram', 'kiran', 'sai'],
    'Age': [34, 30, None, 60, 25, 50, 28, 40, 33, 45],
    'Department': ['corona', 'cardiology', 'orthopedics', 'neurology', 'pediatrics', 'dermatology', 'oncology', 'ent', 'urology', 'gastroenterology'],
    'admission_date': ['2025-08-01', '2025-08-02', '2025-08-03', '2025-08-04', '2025-08-05', '2025-08-06', '2025-08-07', '2025-08-08', '2025-08-09', '2025-08-10'],
    'bill': [2000, 3500, 1500, 5000, 1200, 2200, 4000, 1800, 2700, 3300],
    'gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M'],
    'doctor': ['Dr. Rao', 'Dr. Singh', 'Dr. Kumar', 'Dr. Mehta', 'Dr. Patel', 'Dr. Reddy', 'Dr. Shah', 'Dr. Verma', 'Dr. Iyer', 'Dr. Joshi'],
    'discharge_date': ['2025-08-05', '2025-08-06', '2025-08-05', '2025-08-10', '2025-08-06', '2025-08-08', '2025-08-12', '2025-08-09', '2025-08-11', '2025-08-13'],
    'diagnosis': ['Flu', 'Heart issue', 'Fracture', 'Stroke', 'Fever', 'Allergy', 'Cancer', 'Ear infection', 'Kidney stone', 'Ulcer'],
    'treatment': ['Medication', 'Surgery', 'Cast', 'Therapy', 'Medication', 'Cream', 'Chemotherapy', 'Antibiotics', 'Surgery', 'Endoscopy'],
    'insurance': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'contact_number': ['9999990001', '9999990002', '9999990003', '9999990004', '9999990005', '9999990006', '9999990007', '9999990008', '9999990009', '9999990010'],
    'address': ['CityA', 'CityB', 'CityC', 'CityD', 'CityE', 'CityF', 'CityG', 'CityH', 'CityI', 'CityJ'],
    'room_type': ['General', 'Private', 'General', 'ICU', 'General', 'Semi-Private', 'ICU', 'General', 'Private', 'Semi-Private'],
    'payment_status': ['Paid', 'Unpaid', 'Paid', 'Paid', 'Paid', 'Unpaid', 'Paid', 'Paid', 'Unpaid', 'Paid']
}

df = pd.DataFrame(data)
df.to_csv("data_hospital.csv",index=False)
print("created data sucessfully")
