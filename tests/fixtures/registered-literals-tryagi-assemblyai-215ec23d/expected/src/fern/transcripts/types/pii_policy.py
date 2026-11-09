

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PiiPolicy(enum.StrEnum):
    """
    The type of PII to redact
    """

    ACCOUNT_NUMBER = "account_number"
    """
    Customer account or membership identification number (e.g., Policy No. 10042992, Member ID: HZ-5235-001)
    """

    BANKING_INFORMATION = "banking_information"
    """
    Banking information, including account and routing numbers
    """

    BLOOD_TYPE = "blood_type"
    """
    Blood type (e.g., O-, AB positive)
    """

    CREDIT_CARD_CVV = "credit_card_cvv"
    """
    Credit card verification code (e.g., CVV: 080)
    """

    CREDIT_CARD_EXPIRATION = "credit_card_expiration"
    """
    Expiration date of a credit card
    """

    CREDIT_CARD_NUMBER = "credit_card_number"
    """
    Credit card number
    """

    DATE = "date"
    """
    Specific calendar date (e.g., December 18)
    """

    DATE_INTERVAL = "date_interval"
    """
    Broader time periods, including date ranges, months, seasons, years, and decades (e.g., 2020-2021, 5-9 May, January 1984)
    """

    DATE_OF_BIRTH = "date_of_birth"
    """
    Date of birth (e.g., Date of Birth: March 7,1961)
    """

    DRIVERS_LICENSE = "drivers_license"
    """
    Driver's license number. (e.g., DL# 356933-540)
    """

    DRUG = "drug"
    """
    Medications, vitamins, or supplements (e.g., Advil, Acetaminophen, Panadol)
    """

    DURATION = "duration"
    """
    Measurements of time expressed as a numerical value plus a unit (e.g., 8 months, 2 years)
    """

    EMAIL_ADDRESS = "email_address"
    """
    Email address (e.g., support@assemblyai.com)
    """

    EVENT = "event"
    """
    Name of an event or holiday (e.g., Olympics, Yom Kippur)
    """

    FILENAME = "filename"
    """
    Names of computer files, including the extension or filepath (e.g., Taxes/2012/brad-tax-returns.pdf)
    """

    GENDER = "gender"
    """
    Terms indicating gender identity (e.g., female, male, non-binary)
    """

    GENDER_SEXUALITY = "gender_sexuality"
    """
    Terms indicating gender identity or sexual orientation, including slang terms (e.g., female, bisexual, trans)
    """

    HEALTHCARE_NUMBER = "healthcare_number"
    """
    Healthcare numbers and health plan beneficiary numbers (e.g., Policy No.: 5584-486-674-YM)
    """

    INJURY = "injury"
    """
    Bodily injury (e.g., I broke my arm, I have a sprained wrist)
    """

    IP_ADDRESS = "ip_address"
    """
    Internet IP address, including IPv4 and IPv6 formats (e.g., 192.168.0.1)
    """

    LANGUAGE = "language"
    """
    Name of a natural language (e.g., Spanish, French)
    """

    LOCATION = "location"
    """
    Any Location reference including mailing address, postal code, city, state, province, country, or coordinates. (e.g., Lake Victoria, 145 Windsor St., 90210)
    """

    LOCATION_ADDRESS = "location_address"
    """
    A complete mailing address (e.g., 145 Windsor St., Toronto, ON M5A 2P5)
    """

    LOCATION_ADDRESS_STREET = "location_address_street"
    """
    Street-level component of an address (e.g., 145 Windsor St.)
    """

    LOCATION_CITY = "location_city"
    """
    City name (e.g., Toronto, San Francisco)
    """

    LOCATION_COORDINATE = "location_coordinate"
    """
    Geographic coordinates (e.g., 40.7128° N, 74.0060° W)
    """

    LOCATION_COUNTRY = "location_country"
    """
    Country name (e.g., Canada, United States)
    """

    LOCATION_STATE = "location_state"
    """
    State, province, or region name (e.g., Ontario, California)
    """

    LOCATION_ZIP = "location_zip"
    """
    Postal or ZIP code (e.g., M5A 2P5, 90210)
    """

    MARITAL_STATUS = "marital_status"
    """
    Terms indicating marital status (e.g., Single, common-law, ex-wife, married)
    """

    MEDICAL_CONDITION = "medical_condition"
    """
    Name of a medical condition, disease, syndrome, deficit, or disorder (e.g., chronic fatigue syndrome, arrhythmia, depression)
    """

    MEDICAL_PROCESS = "medical_process"
    """
    Medical process, including treatments, procedures, and tests (e.g., heart surgery, CT scan)
    """

    MONEY_AMOUNT = "money_amount"
    """
    Name and/or amount of currency (e.g., 15 pesos, $94.50)
    """

    NATIONALITY = "nationality"
    """
    Terms indicating nationality, ethnicity, or race (e.g., American, Asian, Caucasian)
    """

    NUMBER_SEQUENCE = "number_sequence"
    """
    Numerical PII (including alphanumeric strings) that doesn't fall under other categories
    """

    OCCUPATION = "occupation"
    """
    Job title or profession (e.g., professor, actors, engineer, CPA)
    """

    ORGANIZATION = "organization"
    """
    Name of an organization (e.g., CNN, McDonalds, University of Alaska, Northwest General Hospital)
    """

    ORGANIZATION_MEDICAL_FACILITY = "organization_medical_facility"
    """
    Name of a medical facility (e.g., Mayo Clinic, Northwest General Hospital)
    """

    PASSPORT_NUMBER = "passport_number"
    """
    Passport numbers, issued by any country (e.g., PA4568332, NU3C6L86S12)
    """

    PASSWORD = "password"
    """
    Account passwords, PINs, access keys, or verification answers (e.g., 27%alfalfa, temp1234, My mother's maiden name is Smith)
    """

    PERSON_AGE = "person_age"
    """
    Number associated with an age (e.g., 27, 75)
    """

    PERSON_NAME = "person_name"
    """
    Name of a person (e.g., Bob, Doug Jones, Dr. Kay Martinez, MD)
    """

    PHONE_NUMBER = "phone_number"
    """
    Telephone or fax number
    """

    PHYSICAL_ATTRIBUTE = "physical_attribute"
    """
    Distinctive bodily attributes, including race (e.g., I'm 190cm tall, He belongs to the Black students' association)
    """

    POLITICAL_AFFILIATION = "political_affiliation"
    """
    Terms referring to a political party, movement, or ideology (e.g., Republican, Liberal)
    """

    RELIGION = "religion"
    """
    Terms indicating religious affiliation (e.g., Hindu, Catholic)
    """

    SEXUALITY = "sexuality"
    """
    Terms indicating sexual orientation (e.g., heterosexual, bisexual, gay)
    """

    STATISTICS = "statistics"
    """
    Medical statistics (e.g., 18%, 18 percent)
    """

    TIME = "time"
    """
    Expressions indicating clock times (e.g., 19:37:28, 10pm EST)
    """

    URL = "url"
    """
    Internet addresses (e.g., https://www.assemblyai.com/)
    """

    US_SOCIAL_SECURITY_NUMBER = "us_social_security_number"
    """
    Social Security Number or equivalent
    """

    USERNAME = "username"
    """
    Usernames, login names, or handles (e.g., @AssemblyAI)
    """

    VEHICLE_ID = "vehicle_id"
    """
    Vehicle identification numbers (VINs), vehicle serial numbers, and license plate numbers (e.g., 5FNRL38918B111818, BIF7547)
    """

    ZODIAC_SIGN = "zodiac_sign"
    """
    Names of Zodiac signs (e.g., Aries, Taurus)
    """

    def visit(
        self,
        account_number: typing.Callable[[], T_Result],
        banking_information: typing.Callable[[], T_Result],
        blood_type: typing.Callable[[], T_Result],
        credit_card_cvv: typing.Callable[[], T_Result],
        credit_card_expiration: typing.Callable[[], T_Result],
        credit_card_number: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        date_interval: typing.Callable[[], T_Result],
        date_of_birth: typing.Callable[[], T_Result],
        drivers_license: typing.Callable[[], T_Result],
        drug: typing.Callable[[], T_Result],
        duration: typing.Callable[[], T_Result],
        email_address: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        filename: typing.Callable[[], T_Result],
        gender: typing.Callable[[], T_Result],
        gender_sexuality: typing.Callable[[], T_Result],
        healthcare_number: typing.Callable[[], T_Result],
        injury: typing.Callable[[], T_Result],
        ip_address: typing.Callable[[], T_Result],
        language: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        location_address: typing.Callable[[], T_Result],
        location_address_street: typing.Callable[[], T_Result],
        location_city: typing.Callable[[], T_Result],
        location_coordinate: typing.Callable[[], T_Result],
        location_country: typing.Callable[[], T_Result],
        location_state: typing.Callable[[], T_Result],
        location_zip: typing.Callable[[], T_Result],
        marital_status: typing.Callable[[], T_Result],
        medical_condition: typing.Callable[[], T_Result],
        medical_process: typing.Callable[[], T_Result],
        money_amount: typing.Callable[[], T_Result],
        nationality: typing.Callable[[], T_Result],
        number_sequence: typing.Callable[[], T_Result],
        occupation: typing.Callable[[], T_Result],
        organization: typing.Callable[[], T_Result],
        organization_medical_facility: typing.Callable[[], T_Result],
        passport_number: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        person_age: typing.Callable[[], T_Result],
        person_name: typing.Callable[[], T_Result],
        phone_number: typing.Callable[[], T_Result],
        physical_attribute: typing.Callable[[], T_Result],
        political_affiliation: typing.Callable[[], T_Result],
        religion: typing.Callable[[], T_Result],
        sexuality: typing.Callable[[], T_Result],
        statistics: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        us_social_security_number: typing.Callable[[], T_Result],
        username: typing.Callable[[], T_Result],
        vehicle_id: typing.Callable[[], T_Result],
        zodiac_sign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PiiPolicy.ACCOUNT_NUMBER:
            return account_number()
        if self is PiiPolicy.BANKING_INFORMATION:
            return banking_information()
        if self is PiiPolicy.BLOOD_TYPE:
            return blood_type()
        if self is PiiPolicy.CREDIT_CARD_CVV:
            return credit_card_cvv()
        if self is PiiPolicy.CREDIT_CARD_EXPIRATION:
            return credit_card_expiration()
        if self is PiiPolicy.CREDIT_CARD_NUMBER:
            return credit_card_number()
        if self is PiiPolicy.DATE:
            return date()
        if self is PiiPolicy.DATE_INTERVAL:
            return date_interval()
        if self is PiiPolicy.DATE_OF_BIRTH:
            return date_of_birth()
        if self is PiiPolicy.DRIVERS_LICENSE:
            return drivers_license()
        if self is PiiPolicy.DRUG:
            return drug()
        if self is PiiPolicy.DURATION:
            return duration()
        if self is PiiPolicy.EMAIL_ADDRESS:
            return email_address()
        if self is PiiPolicy.EVENT:
            return event()
        if self is PiiPolicy.FILENAME:
            return filename()
        if self is PiiPolicy.GENDER:
            return gender()
        if self is PiiPolicy.GENDER_SEXUALITY:
            return gender_sexuality()
        if self is PiiPolicy.HEALTHCARE_NUMBER:
            return healthcare_number()
        if self is PiiPolicy.INJURY:
            return injury()
        if self is PiiPolicy.IP_ADDRESS:
            return ip_address()
        if self is PiiPolicy.LANGUAGE:
            return language()
        if self is PiiPolicy.LOCATION:
            return location()
        if self is PiiPolicy.LOCATION_ADDRESS:
            return location_address()
        if self is PiiPolicy.LOCATION_ADDRESS_STREET:
            return location_address_street()
        if self is PiiPolicy.LOCATION_CITY:
            return location_city()
        if self is PiiPolicy.LOCATION_COORDINATE:
            return location_coordinate()
        if self is PiiPolicy.LOCATION_COUNTRY:
            return location_country()
        if self is PiiPolicy.LOCATION_STATE:
            return location_state()
        if self is PiiPolicy.LOCATION_ZIP:
            return location_zip()
        if self is PiiPolicy.MARITAL_STATUS:
            return marital_status()
        if self is PiiPolicy.MEDICAL_CONDITION:
            return medical_condition()
        if self is PiiPolicy.MEDICAL_PROCESS:
            return medical_process()
        if self is PiiPolicy.MONEY_AMOUNT:
            return money_amount()
        if self is PiiPolicy.NATIONALITY:
            return nationality()
        if self is PiiPolicy.NUMBER_SEQUENCE:
            return number_sequence()
        if self is PiiPolicy.OCCUPATION:
            return occupation()
        if self is PiiPolicy.ORGANIZATION:
            return organization()
        if self is PiiPolicy.ORGANIZATION_MEDICAL_FACILITY:
            return organization_medical_facility()
        if self is PiiPolicy.PASSPORT_NUMBER:
            return passport_number()
        if self is PiiPolicy.PASSWORD:
            return password()
        if self is PiiPolicy.PERSON_AGE:
            return person_age()
        if self is PiiPolicy.PERSON_NAME:
            return person_name()
        if self is PiiPolicy.PHONE_NUMBER:
            return phone_number()
        if self is PiiPolicy.PHYSICAL_ATTRIBUTE:
            return physical_attribute()
        if self is PiiPolicy.POLITICAL_AFFILIATION:
            return political_affiliation()
        if self is PiiPolicy.RELIGION:
            return religion()
        if self is PiiPolicy.SEXUALITY:
            return sexuality()
        if self is PiiPolicy.STATISTICS:
            return statistics()
        if self is PiiPolicy.TIME:
            return time()
        if self is PiiPolicy.URL:
            return url()
        if self is PiiPolicy.US_SOCIAL_SECURITY_NUMBER:
            return us_social_security_number()
        if self is PiiPolicy.USERNAME:
            return username()
        if self is PiiPolicy.VEHICLE_ID:
            return vehicle_id()
        if self is PiiPolicy.ZODIAC_SIGN:
            return zodiac_sign()
