

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpenseCategory(enum.StrEnum):
    """
    The category of expenses.
    """

    ADVERTISING_AND_MARKETING = "ADVERTISING_AND_MARKETING"
    GROCERY = "GROCERY"
    TELEPHONY = "TELEPHONY"
    OFFICE_SUPPLIES = "OFFICE_SUPPLIES"
    PRIVATE_AIR_TRAVEL = "PRIVATE_AIR_TRAVEL"
    CLOTHING = "CLOTHING"
    CAR_RENTAL = "CAR_RENTAL"
    VEHICLE_EXPENSES = "VEHICLE_EXPENSES"
    RESTAURANTS = "RESTAURANTS"
    GAMBLING = "GAMBLING"
    FLOWERS = "FLOWERS"
    ELECTRONICS = "ELECTRONICS"
    LEGAL_SERVICES = "LEGAL_SERVICES"
    UTILITIES = "UTILITIES"
    FURNITURE = "FURNITURE"
    BARS_AND_NIGHTLIFE = "BARS_AND_NIGHTLIFE"
    LAUNDRY = "LAUNDRY"
    EVENT_EXPENSES = "EVENT_EXPENSES"
    SHIPPING = "SHIPPING"
    OTHER_TRAVEL_EXPENSES = "OTHER_TRAVEL_EXPENSES"
    CHARITY = "CHARITY"
    SOFTWARE_NON_RECURRING = "SOFTWARE_NON_RECURRING"
    LODGING = "LODGING"
    FACILITIES_EXPENSES = "FACILITIES_EXPENSES"
    SERVERS = "SERVERS"
    CONFERENCES = "CONFERENCES"
    FOOD_DELIVERY = "FOOD_DELIVERY"
    RENT = "RENT"
    AIRLINE_EXPENSES = "AIRLINE_EXPENSES"
    OTHER_BUSINESS_EXPENSES = "OTHER_BUSINESS_EXPENSES"
    BANK_AND_FINANCIAL_FEES = "BANK_AND_FINANCIAL_FEES"
    BOOKS_AND_NEWSPAPERS = "BOOKS_AND_NEWSPAPERS"
    CONSULTANT_AND_CONTRACTOR = "CONSULTANT_AND_CONTRACTOR"
    CORPORATE_INSURANCE = "CORPORATE_INSURANCE"
    DIGITAL_GOODS = "DIGITAL_GOODS"
    FEES_AND_LICENSES_AND_TAXES = "FEES_AND_LICENSES_AND_TAXES"
    GAS_AND_FUEL = "GAS_AND_FUEL"
    GENERAL_MERCHANDISE = "GENERAL_MERCHANDISE"
    MEDICAL = "MEDICAL"
    MEMBERSHIPS_AND_CLUBS = "MEMBERSHIPS_AND_CLUBS"
    PARKING_EXPENSES = "PARKING_EXPENSES"
    POLITICAL_DONATIONS = "POLITICAL_DONATIONS"
    PUBLIC_TRANSPORTATION = "PUBLIC_TRANSPORTATION"
    RECURRING_SOFTWARE_AND_SAAS = "RECURRING_SOFTWARE_AND_SAAS"
    RIDESHARE_AND_TAXI = "RIDESHARE_AND_TAXI"
    TOLL_AND_BRIDGE_FEES = "TOLL_AND_BRIDGE_FEES"
    TRAINING_AND_EDUCATION = "TRAINING_AND_EDUCATION"
    TRAVEL_WIFI = "TRAVEL_WIFI"

    def visit(
        self,
        advertising_and_marketing: typing.Callable[[], T_Result],
        grocery: typing.Callable[[], T_Result],
        telephony: typing.Callable[[], T_Result],
        office_supplies: typing.Callable[[], T_Result],
        private_air_travel: typing.Callable[[], T_Result],
        clothing: typing.Callable[[], T_Result],
        car_rental: typing.Callable[[], T_Result],
        vehicle_expenses: typing.Callable[[], T_Result],
        restaurants: typing.Callable[[], T_Result],
        gambling: typing.Callable[[], T_Result],
        flowers: typing.Callable[[], T_Result],
        electronics: typing.Callable[[], T_Result],
        legal_services: typing.Callable[[], T_Result],
        utilities: typing.Callable[[], T_Result],
        furniture: typing.Callable[[], T_Result],
        bars_and_nightlife: typing.Callable[[], T_Result],
        laundry: typing.Callable[[], T_Result],
        event_expenses: typing.Callable[[], T_Result],
        shipping: typing.Callable[[], T_Result],
        other_travel_expenses: typing.Callable[[], T_Result],
        charity: typing.Callable[[], T_Result],
        software_non_recurring: typing.Callable[[], T_Result],
        lodging: typing.Callable[[], T_Result],
        facilities_expenses: typing.Callable[[], T_Result],
        servers: typing.Callable[[], T_Result],
        conferences: typing.Callable[[], T_Result],
        food_delivery: typing.Callable[[], T_Result],
        rent: typing.Callable[[], T_Result],
        airline_expenses: typing.Callable[[], T_Result],
        other_business_expenses: typing.Callable[[], T_Result],
        bank_and_financial_fees: typing.Callable[[], T_Result],
        books_and_newspapers: typing.Callable[[], T_Result],
        consultant_and_contractor: typing.Callable[[], T_Result],
        corporate_insurance: typing.Callable[[], T_Result],
        digital_goods: typing.Callable[[], T_Result],
        fees_and_licenses_and_taxes: typing.Callable[[], T_Result],
        gas_and_fuel: typing.Callable[[], T_Result],
        general_merchandise: typing.Callable[[], T_Result],
        medical: typing.Callable[[], T_Result],
        memberships_and_clubs: typing.Callable[[], T_Result],
        parking_expenses: typing.Callable[[], T_Result],
        political_donations: typing.Callable[[], T_Result],
        public_transportation: typing.Callable[[], T_Result],
        recurring_software_and_saas: typing.Callable[[], T_Result],
        rideshare_and_taxi: typing.Callable[[], T_Result],
        toll_and_bridge_fees: typing.Callable[[], T_Result],
        training_and_education: typing.Callable[[], T_Result],
        travel_wifi: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpenseCategory.ADVERTISING_AND_MARKETING:
            return advertising_and_marketing()
        if self is ExpenseCategory.GROCERY:
            return grocery()
        if self is ExpenseCategory.TELEPHONY:
            return telephony()
        if self is ExpenseCategory.OFFICE_SUPPLIES:
            return office_supplies()
        if self is ExpenseCategory.PRIVATE_AIR_TRAVEL:
            return private_air_travel()
        if self is ExpenseCategory.CLOTHING:
            return clothing()
        if self is ExpenseCategory.CAR_RENTAL:
            return car_rental()
        if self is ExpenseCategory.VEHICLE_EXPENSES:
            return vehicle_expenses()
        if self is ExpenseCategory.RESTAURANTS:
            return restaurants()
        if self is ExpenseCategory.GAMBLING:
            return gambling()
        if self is ExpenseCategory.FLOWERS:
            return flowers()
        if self is ExpenseCategory.ELECTRONICS:
            return electronics()
        if self is ExpenseCategory.LEGAL_SERVICES:
            return legal_services()
        if self is ExpenseCategory.UTILITIES:
            return utilities()
        if self is ExpenseCategory.FURNITURE:
            return furniture()
        if self is ExpenseCategory.BARS_AND_NIGHTLIFE:
            return bars_and_nightlife()
        if self is ExpenseCategory.LAUNDRY:
            return laundry()
        if self is ExpenseCategory.EVENT_EXPENSES:
            return event_expenses()
        if self is ExpenseCategory.SHIPPING:
            return shipping()
        if self is ExpenseCategory.OTHER_TRAVEL_EXPENSES:
            return other_travel_expenses()
        if self is ExpenseCategory.CHARITY:
            return charity()
        if self is ExpenseCategory.SOFTWARE_NON_RECURRING:
            return software_non_recurring()
        if self is ExpenseCategory.LODGING:
            return lodging()
        if self is ExpenseCategory.FACILITIES_EXPENSES:
            return facilities_expenses()
        if self is ExpenseCategory.SERVERS:
            return servers()
        if self is ExpenseCategory.CONFERENCES:
            return conferences()
        if self is ExpenseCategory.FOOD_DELIVERY:
            return food_delivery()
        if self is ExpenseCategory.RENT:
            return rent()
        if self is ExpenseCategory.AIRLINE_EXPENSES:
            return airline_expenses()
        if self is ExpenseCategory.OTHER_BUSINESS_EXPENSES:
            return other_business_expenses()
        if self is ExpenseCategory.BANK_AND_FINANCIAL_FEES:
            return bank_and_financial_fees()
        if self is ExpenseCategory.BOOKS_AND_NEWSPAPERS:
            return books_and_newspapers()
        if self is ExpenseCategory.CONSULTANT_AND_CONTRACTOR:
            return consultant_and_contractor()
        if self is ExpenseCategory.CORPORATE_INSURANCE:
            return corporate_insurance()
        if self is ExpenseCategory.DIGITAL_GOODS:
            return digital_goods()
        if self is ExpenseCategory.FEES_AND_LICENSES_AND_TAXES:
            return fees_and_licenses_and_taxes()
        if self is ExpenseCategory.GAS_AND_FUEL:
            return gas_and_fuel()
        if self is ExpenseCategory.GENERAL_MERCHANDISE:
            return general_merchandise()
        if self is ExpenseCategory.MEDICAL:
            return medical()
        if self is ExpenseCategory.MEMBERSHIPS_AND_CLUBS:
            return memberships_and_clubs()
        if self is ExpenseCategory.PARKING_EXPENSES:
            return parking_expenses()
        if self is ExpenseCategory.POLITICAL_DONATIONS:
            return political_donations()
        if self is ExpenseCategory.PUBLIC_TRANSPORTATION:
            return public_transportation()
        if self is ExpenseCategory.RECURRING_SOFTWARE_AND_SAAS:
            return recurring_software_and_saas()
        if self is ExpenseCategory.RIDESHARE_AND_TAXI:
            return rideshare_and_taxi()
        if self is ExpenseCategory.TOLL_AND_BRIDGE_FEES:
            return toll_and_bridge_fees()
        if self is ExpenseCategory.TRAINING_AND_EDUCATION:
            return training_and_education()
        if self is ExpenseCategory.TRAVEL_WIFI:
            return travel_wifi()
