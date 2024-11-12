import openpyxl
import random

def generate_random_phone_number():
    """Generates a random international phone number."""
    country_codes = [
        "+1", "+44", "+91", "+81", "+33", "+86", "+61", "+55", "+27", "+63",
        "+254", "+353", "+49", "+82", "+90", "+39", "+7", "+92", "+65", "+36",
        "+94", "+66", "+45", "+370", "+371", "+372", "+373", "+374", "+375", "+376",
        "+377", "+378", "+379", "+380", "+381", "+382", "+383", "+384", "+385", "+386",
        "+387", "+388", "+389", "+390", "+391", "+392", "+393", "+394", "+395", "+396"
    ]
    country_code = random.choice(country_codes)
    area_code = random.randint(100, 999)
    local_number = random.randint(1000000, 9999999)
    return f"{country_code} {area_code} {local_number}"

def create_excel_file(filename, num_phone_numbers):
    """Creates an Excel file with the specified number of phone numbers."""
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for i in range(1, num_phone_numbers + 1):
        sheet.cell(row=i, column=1).value = generate_random_phone_number()
    workbook.save(filename)

if __name__ == "__main__":
    filename = "phone_numbers.xlsx"
    num_phone_numbers = 50
    create_excel_file(filename, num_phone_numbers)
    print(f"Excel file '{filename}' created with {num_phone_numbers} phone numbers.")