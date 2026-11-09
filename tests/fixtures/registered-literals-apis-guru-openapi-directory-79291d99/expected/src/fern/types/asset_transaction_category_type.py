

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetTransactionCategoryType(enum.StrEnum):
    """
    Asset Transaction Category Type Enumerated derived by Vendor.
    """

    ATM_FEE = "ATMFee"
    ADVERTISING = "Advertising"
    AIR_TRAVEL = "AirTravel"
    ALCOHOL_BARS = "AlcoholBars"
    ALLOWANCE = "Allowance"
    AMUSEMENT = "Amusement"
    ARTS = "Arts"
    AUTO_TRANSPORT = "AutoTransport"
    AUTO_INSURANCE = "AutoInsurance"
    AUTO_PAYMENT = "AutoPayment"
    BABY_SUPPLIES = "BabySupplies"
    BABYSITTER_DAYCARE = "BabysitterDaycare"
    BANK_FEE = "BankFee"
    BILLS_UTILITIES = "BillsUtilities"
    BONUS = "Bonus"
    BOOKS_SUPPLIES = "BooksSupplies"
    BUSINESS_SERVICES = "Business Services"
    BUY = "Buy"
    CASH_ATM = "CashATM"
    CHARITY = "Charity"
    CHECK = "Check"
    CHILD_SUPPORT = "ChildSupport"
    CLOTHING = "Clothing"
    COFFEE_SHOPS = "CoffeeShops"
    CREDIT_CARD_PAYMENT = "CreditCardPayment"
    DENTIST = "Dentist"
    DOCTOR = "Doctor"
    EDUCATION = "Education"
    ELECTRONICS_SOFTWARE = "ElectronicsSoftware"
    ENTERTAINMENT = "Entertainment"
    EYECARE = "Eyecare"
    FAST_FOOD = "FastFood"
    FEDERAL_TAX = "FederalTax"
    FEES_CHARGES = "FeesCharges"
    FINANCE_CHARGE = "FinanceCharge"
    FINANCIAL = "Financial"
    FINANCIAL_ADVISOR = "FinancialAdvisor"
    FOOD_DINING = "FoodDining"
    FURNISHINGS = "Furnishings"
    GAS_FUEL = "GasFuel"
    GIFTS_DONATIONS = "GiftsDonations"
    GROCERIES = "Groceries"
    GYM = "Gym"
    HAIR = "Hair"
    HEALTH_FITNESS = "HealthFitness"
    HEALTH_INSURANCE = "HealthInsurance"
    HOBBIES = "Hobbies"
    HOME = "Home"
    HOME_IMPROVEMENT = "HomeImprovement"
    HOME_INSURANCE = "HomeInsurance"
    HOME_PHONE = "HomePhone"
    HOME_SERVICES = "HomeServices"
    HOME_SUPPLIES = "HomeSupplies"
    HOTEL = "Hotel"
    INCOME = "Income"
    INTEREST_INCOME = "InterestIncome"
    INTERNET = "Internet"
    INVESTMENTS = "Investments"
    KIDS = "Kids"
    KIDS_ACTIVITIES = "KidsActivities"
    LATE_FEE = "LateFee"
    LAUNDRY = "Laundry"
    LAWN_GARDEN = "LawnGarden"
    LEGAL = "Legal"
    LIFE_INSURANCE = "LifeInsurance"
    LOAN_INSURANCE = "LoanInsurance"
    LOAN_PAYMENT = "LoanPayment"
    LOANS = "Loans"
    MOBILE_PHONE = "MobilePhone"
    MORTGAGE_RENT = "MortgageRent"
    MOVIES_DV_DS = "MoviesDVDs"
    MUSIC = "Music"
    NEWSPAPERS_MAGAZINES = "NewspapersMagazines"
    OFFICE_SUPPLIES = "OfficeSupplies"
    PARKING = "Parking"
    PAYCHECK = "Paycheck"
    PERSONAL_CARE = "PersonalCare"
    PET_FOOD_SUPPLIES = "PetFoodSupplies"
    PET_GROOMING = "PetGrooming"
    PETS = "Pets"
    PHARMACY = "Pharmacy"
    PRINTING = "Printing"
    PROPERTY_TAX = "Property Tax"
    PUBLIC_TRANSPORTATION = "Public Transportation"
    REIMBURSEMENT = "Reimbursement"
    RENTAL_CAR_TAXI = "RentalCarTaxi"
    RESTAURANTS = "Restaurants"
    SALES_TAX = "SalesTax"
    SERVICE_PARTS = "ServiceParts"
    SERVICE_FEE = "ServiceFee"
    SHIPPING = "Shipping"
    SHOPPING = "Shopping"
    SPA_MASSAGE = "SpaMassage"
    SPORTING_GOODS = "SportingGoods"
    SPORTS = "Sports"
    STATE_TAX = "StateTax"
    STUDENT_LOAN = "Student Loan"
    TAXES = "Taxes"
    TELEVISION = "Television"
    TOYS = "Toys"
    TRANSFER = "Transfer"
    TRAVEL = "Travel"
    TUITION = "Tuition"
    UNCATEGORIZED = "Uncategorized"
    UTILITIES = "Utilities"
    VACATION = "Vacation"
    VETERINARY = "Veterinary"

    def visit(
        self,
        atm_fee: typing.Callable[[], T_Result],
        advertising: typing.Callable[[], T_Result],
        air_travel: typing.Callable[[], T_Result],
        alcohol_bars: typing.Callable[[], T_Result],
        allowance: typing.Callable[[], T_Result],
        amusement: typing.Callable[[], T_Result],
        arts: typing.Callable[[], T_Result],
        auto_transport: typing.Callable[[], T_Result],
        auto_insurance: typing.Callable[[], T_Result],
        auto_payment: typing.Callable[[], T_Result],
        baby_supplies: typing.Callable[[], T_Result],
        babysitter_daycare: typing.Callable[[], T_Result],
        bank_fee: typing.Callable[[], T_Result],
        bills_utilities: typing.Callable[[], T_Result],
        bonus: typing.Callable[[], T_Result],
        books_supplies: typing.Callable[[], T_Result],
        business_services: typing.Callable[[], T_Result],
        buy: typing.Callable[[], T_Result],
        cash_atm: typing.Callable[[], T_Result],
        charity: typing.Callable[[], T_Result],
        check: typing.Callable[[], T_Result],
        child_support: typing.Callable[[], T_Result],
        clothing: typing.Callable[[], T_Result],
        coffee_shops: typing.Callable[[], T_Result],
        credit_card_payment: typing.Callable[[], T_Result],
        dentist: typing.Callable[[], T_Result],
        doctor: typing.Callable[[], T_Result],
        education: typing.Callable[[], T_Result],
        electronics_software: typing.Callable[[], T_Result],
        entertainment: typing.Callable[[], T_Result],
        eyecare: typing.Callable[[], T_Result],
        fast_food: typing.Callable[[], T_Result],
        federal_tax: typing.Callable[[], T_Result],
        fees_charges: typing.Callable[[], T_Result],
        finance_charge: typing.Callable[[], T_Result],
        financial: typing.Callable[[], T_Result],
        financial_advisor: typing.Callable[[], T_Result],
        food_dining: typing.Callable[[], T_Result],
        furnishings: typing.Callable[[], T_Result],
        gas_fuel: typing.Callable[[], T_Result],
        gifts_donations: typing.Callable[[], T_Result],
        groceries: typing.Callable[[], T_Result],
        gym: typing.Callable[[], T_Result],
        hair: typing.Callable[[], T_Result],
        health_fitness: typing.Callable[[], T_Result],
        health_insurance: typing.Callable[[], T_Result],
        hobbies: typing.Callable[[], T_Result],
        home: typing.Callable[[], T_Result],
        home_improvement: typing.Callable[[], T_Result],
        home_insurance: typing.Callable[[], T_Result],
        home_phone: typing.Callable[[], T_Result],
        home_services: typing.Callable[[], T_Result],
        home_supplies: typing.Callable[[], T_Result],
        hotel: typing.Callable[[], T_Result],
        income: typing.Callable[[], T_Result],
        interest_income: typing.Callable[[], T_Result],
        internet: typing.Callable[[], T_Result],
        investments: typing.Callable[[], T_Result],
        kids: typing.Callable[[], T_Result],
        kids_activities: typing.Callable[[], T_Result],
        late_fee: typing.Callable[[], T_Result],
        laundry: typing.Callable[[], T_Result],
        lawn_garden: typing.Callable[[], T_Result],
        legal: typing.Callable[[], T_Result],
        life_insurance: typing.Callable[[], T_Result],
        loan_insurance: typing.Callable[[], T_Result],
        loan_payment: typing.Callable[[], T_Result],
        loans: typing.Callable[[], T_Result],
        mobile_phone: typing.Callable[[], T_Result],
        mortgage_rent: typing.Callable[[], T_Result],
        movies_dv_ds: typing.Callable[[], T_Result],
        music: typing.Callable[[], T_Result],
        newspapers_magazines: typing.Callable[[], T_Result],
        office_supplies: typing.Callable[[], T_Result],
        parking: typing.Callable[[], T_Result],
        paycheck: typing.Callable[[], T_Result],
        personal_care: typing.Callable[[], T_Result],
        pet_food_supplies: typing.Callable[[], T_Result],
        pet_grooming: typing.Callable[[], T_Result],
        pets: typing.Callable[[], T_Result],
        pharmacy: typing.Callable[[], T_Result],
        printing: typing.Callable[[], T_Result],
        property_tax: typing.Callable[[], T_Result],
        public_transportation: typing.Callable[[], T_Result],
        reimbursement: typing.Callable[[], T_Result],
        rental_car_taxi: typing.Callable[[], T_Result],
        restaurants: typing.Callable[[], T_Result],
        sales_tax: typing.Callable[[], T_Result],
        service_parts: typing.Callable[[], T_Result],
        service_fee: typing.Callable[[], T_Result],
        shipping: typing.Callable[[], T_Result],
        shopping: typing.Callable[[], T_Result],
        spa_massage: typing.Callable[[], T_Result],
        sporting_goods: typing.Callable[[], T_Result],
        sports: typing.Callable[[], T_Result],
        state_tax: typing.Callable[[], T_Result],
        student_loan: typing.Callable[[], T_Result],
        taxes: typing.Callable[[], T_Result],
        television: typing.Callable[[], T_Result],
        toys: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
        travel: typing.Callable[[], T_Result],
        tuition: typing.Callable[[], T_Result],
        uncategorized: typing.Callable[[], T_Result],
        utilities: typing.Callable[[], T_Result],
        vacation: typing.Callable[[], T_Result],
        veterinary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetTransactionCategoryType.ATM_FEE:
            return atm_fee()
        if self is AssetTransactionCategoryType.ADVERTISING:
            return advertising()
        if self is AssetTransactionCategoryType.AIR_TRAVEL:
            return air_travel()
        if self is AssetTransactionCategoryType.ALCOHOL_BARS:
            return alcohol_bars()
        if self is AssetTransactionCategoryType.ALLOWANCE:
            return allowance()
        if self is AssetTransactionCategoryType.AMUSEMENT:
            return amusement()
        if self is AssetTransactionCategoryType.ARTS:
            return arts()
        if self is AssetTransactionCategoryType.AUTO_TRANSPORT:
            return auto_transport()
        if self is AssetTransactionCategoryType.AUTO_INSURANCE:
            return auto_insurance()
        if self is AssetTransactionCategoryType.AUTO_PAYMENT:
            return auto_payment()
        if self is AssetTransactionCategoryType.BABY_SUPPLIES:
            return baby_supplies()
        if self is AssetTransactionCategoryType.BABYSITTER_DAYCARE:
            return babysitter_daycare()
        if self is AssetTransactionCategoryType.BANK_FEE:
            return bank_fee()
        if self is AssetTransactionCategoryType.BILLS_UTILITIES:
            return bills_utilities()
        if self is AssetTransactionCategoryType.BONUS:
            return bonus()
        if self is AssetTransactionCategoryType.BOOKS_SUPPLIES:
            return books_supplies()
        if self is AssetTransactionCategoryType.BUSINESS_SERVICES:
            return business_services()
        if self is AssetTransactionCategoryType.BUY:
            return buy()
        if self is AssetTransactionCategoryType.CASH_ATM:
            return cash_atm()
        if self is AssetTransactionCategoryType.CHARITY:
            return charity()
        if self is AssetTransactionCategoryType.CHECK:
            return check()
        if self is AssetTransactionCategoryType.CHILD_SUPPORT:
            return child_support()
        if self is AssetTransactionCategoryType.CLOTHING:
            return clothing()
        if self is AssetTransactionCategoryType.COFFEE_SHOPS:
            return coffee_shops()
        if self is AssetTransactionCategoryType.CREDIT_CARD_PAYMENT:
            return credit_card_payment()
        if self is AssetTransactionCategoryType.DENTIST:
            return dentist()
        if self is AssetTransactionCategoryType.DOCTOR:
            return doctor()
        if self is AssetTransactionCategoryType.EDUCATION:
            return education()
        if self is AssetTransactionCategoryType.ELECTRONICS_SOFTWARE:
            return electronics_software()
        if self is AssetTransactionCategoryType.ENTERTAINMENT:
            return entertainment()
        if self is AssetTransactionCategoryType.EYECARE:
            return eyecare()
        if self is AssetTransactionCategoryType.FAST_FOOD:
            return fast_food()
        if self is AssetTransactionCategoryType.FEDERAL_TAX:
            return federal_tax()
        if self is AssetTransactionCategoryType.FEES_CHARGES:
            return fees_charges()
        if self is AssetTransactionCategoryType.FINANCE_CHARGE:
            return finance_charge()
        if self is AssetTransactionCategoryType.FINANCIAL:
            return financial()
        if self is AssetTransactionCategoryType.FINANCIAL_ADVISOR:
            return financial_advisor()
        if self is AssetTransactionCategoryType.FOOD_DINING:
            return food_dining()
        if self is AssetTransactionCategoryType.FURNISHINGS:
            return furnishings()
        if self is AssetTransactionCategoryType.GAS_FUEL:
            return gas_fuel()
        if self is AssetTransactionCategoryType.GIFTS_DONATIONS:
            return gifts_donations()
        if self is AssetTransactionCategoryType.GROCERIES:
            return groceries()
        if self is AssetTransactionCategoryType.GYM:
            return gym()
        if self is AssetTransactionCategoryType.HAIR:
            return hair()
        if self is AssetTransactionCategoryType.HEALTH_FITNESS:
            return health_fitness()
        if self is AssetTransactionCategoryType.HEALTH_INSURANCE:
            return health_insurance()
        if self is AssetTransactionCategoryType.HOBBIES:
            return hobbies()
        if self is AssetTransactionCategoryType.HOME:
            return home()
        if self is AssetTransactionCategoryType.HOME_IMPROVEMENT:
            return home_improvement()
        if self is AssetTransactionCategoryType.HOME_INSURANCE:
            return home_insurance()
        if self is AssetTransactionCategoryType.HOME_PHONE:
            return home_phone()
        if self is AssetTransactionCategoryType.HOME_SERVICES:
            return home_services()
        if self is AssetTransactionCategoryType.HOME_SUPPLIES:
            return home_supplies()
        if self is AssetTransactionCategoryType.HOTEL:
            return hotel()
        if self is AssetTransactionCategoryType.INCOME:
            return income()
        if self is AssetTransactionCategoryType.INTEREST_INCOME:
            return interest_income()
        if self is AssetTransactionCategoryType.INTERNET:
            return internet()
        if self is AssetTransactionCategoryType.INVESTMENTS:
            return investments()
        if self is AssetTransactionCategoryType.KIDS:
            return kids()
        if self is AssetTransactionCategoryType.KIDS_ACTIVITIES:
            return kids_activities()
        if self is AssetTransactionCategoryType.LATE_FEE:
            return late_fee()
        if self is AssetTransactionCategoryType.LAUNDRY:
            return laundry()
        if self is AssetTransactionCategoryType.LAWN_GARDEN:
            return lawn_garden()
        if self is AssetTransactionCategoryType.LEGAL:
            return legal()
        if self is AssetTransactionCategoryType.LIFE_INSURANCE:
            return life_insurance()
        if self is AssetTransactionCategoryType.LOAN_INSURANCE:
            return loan_insurance()
        if self is AssetTransactionCategoryType.LOAN_PAYMENT:
            return loan_payment()
        if self is AssetTransactionCategoryType.LOANS:
            return loans()
        if self is AssetTransactionCategoryType.MOBILE_PHONE:
            return mobile_phone()
        if self is AssetTransactionCategoryType.MORTGAGE_RENT:
            return mortgage_rent()
        if self is AssetTransactionCategoryType.MOVIES_DV_DS:
            return movies_dv_ds()
        if self is AssetTransactionCategoryType.MUSIC:
            return music()
        if self is AssetTransactionCategoryType.NEWSPAPERS_MAGAZINES:
            return newspapers_magazines()
        if self is AssetTransactionCategoryType.OFFICE_SUPPLIES:
            return office_supplies()
        if self is AssetTransactionCategoryType.PARKING:
            return parking()
        if self is AssetTransactionCategoryType.PAYCHECK:
            return paycheck()
        if self is AssetTransactionCategoryType.PERSONAL_CARE:
            return personal_care()
        if self is AssetTransactionCategoryType.PET_FOOD_SUPPLIES:
            return pet_food_supplies()
        if self is AssetTransactionCategoryType.PET_GROOMING:
            return pet_grooming()
        if self is AssetTransactionCategoryType.PETS:
            return pets()
        if self is AssetTransactionCategoryType.PHARMACY:
            return pharmacy()
        if self is AssetTransactionCategoryType.PRINTING:
            return printing()
        if self is AssetTransactionCategoryType.PROPERTY_TAX:
            return property_tax()
        if self is AssetTransactionCategoryType.PUBLIC_TRANSPORTATION:
            return public_transportation()
        if self is AssetTransactionCategoryType.REIMBURSEMENT:
            return reimbursement()
        if self is AssetTransactionCategoryType.RENTAL_CAR_TAXI:
            return rental_car_taxi()
        if self is AssetTransactionCategoryType.RESTAURANTS:
            return restaurants()
        if self is AssetTransactionCategoryType.SALES_TAX:
            return sales_tax()
        if self is AssetTransactionCategoryType.SERVICE_PARTS:
            return service_parts()
        if self is AssetTransactionCategoryType.SERVICE_FEE:
            return service_fee()
        if self is AssetTransactionCategoryType.SHIPPING:
            return shipping()
        if self is AssetTransactionCategoryType.SHOPPING:
            return shopping()
        if self is AssetTransactionCategoryType.SPA_MASSAGE:
            return spa_massage()
        if self is AssetTransactionCategoryType.SPORTING_GOODS:
            return sporting_goods()
        if self is AssetTransactionCategoryType.SPORTS:
            return sports()
        if self is AssetTransactionCategoryType.STATE_TAX:
            return state_tax()
        if self is AssetTransactionCategoryType.STUDENT_LOAN:
            return student_loan()
        if self is AssetTransactionCategoryType.TAXES:
            return taxes()
        if self is AssetTransactionCategoryType.TELEVISION:
            return television()
        if self is AssetTransactionCategoryType.TOYS:
            return toys()
        if self is AssetTransactionCategoryType.TRANSFER:
            return transfer()
        if self is AssetTransactionCategoryType.TRAVEL:
            return travel()
        if self is AssetTransactionCategoryType.TUITION:
            return tuition()
        if self is AssetTransactionCategoryType.UNCATEGORIZED:
            return uncategorized()
        if self is AssetTransactionCategoryType.UTILITIES:
            return utilities()
        if self is AssetTransactionCategoryType.VACATION:
            return vacation()
        if self is AssetTransactionCategoryType.VETERINARY:
            return veterinary()
