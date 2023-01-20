
import phonenumbers

def get_number_info(number):
    try:
        parsed_number = phonenumbers.parse(number, "AU")
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number."
        else:
            return {
                "Country code": parsed_number.country_code,
                "National number": parsed_number.national_number,
                "Country name": phonenumbers.region_code_for_number(parsed_number),
                "Is valid": phonenumbers.is_valid_number(parsed_number)
            }
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return "Error: {}".format(e)

number = input("Enter a phone number in Australia: ")
print(get_number_info(number))
