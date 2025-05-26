from datetime import datetime

def selection_sort(data, key, ascending=True):
    n = len(data)
    for i in range(n):
        min_or_max_index = i
        for j in range(i + 1, n):
            if ascending:
                condition = data[j][key] < data[min_or_max_index][key]
            else:
                condition = data[j][key] > data[min_or_max_index][key]
            if condition:
                min_or_max_index = j
        data[i], data[min_or_max_index] = data[min_or_max_index], data[i]
    return data

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def get_medical_data():
    patients = []
    print("Enter patient data. Type 'done' when finished.")
    while True:
        name = input("Name: ")
        if name.lower() == 'done':
            break
        dob_str = input("Date of Birth (YYYY-MM-DD): ")
        height = float(input("Height (in cm): "))
        weight = float(input("Weight (in kg): "))

        patient = {
            "name": name,
            "dob": parse_date(dob_str),
            "height": height,
            "weight": weight
        }
        patients.append(patient)
    return patients

def display_data(data):
    print("\nSorted Medical Data:")
    for p in data:
        print(f"Name: {p['name']}, DOB: {p['dob'].date()}, Height: {p['height']} cm, Weight: {p['weight']} kg")

def main():
    print("Medical Data Sorting Program")
    data = get_medical_data()
    
    print("\nFields to sort by: name, dob, height, weight")
    key = input("Enter field to sort by: ").lower()
    order = input("Sort in ascending order? (y/n): ").lower() == 'y'

    if key not in ["name", "dob", "height", "weight"]:
        print("Invalid field!")
        return

    sorted_data = selection_sort(data, key, ascending=order)
    display_data(sorted_data)

if __name__ == "__main__":
    main()