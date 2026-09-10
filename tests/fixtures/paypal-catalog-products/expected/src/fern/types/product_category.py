

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductCategory(enum.StrEnum):
    """
    The product category.
    """

    AC_REFRIGERATION_REPAIR = "AC_REFRIGERATION_REPAIR"
    ACADEMIC_SOFTWARE = "ACADEMIC_SOFTWARE"
    ACCESSORIES = "ACCESSORIES"
    ACCOUNTING = "ACCOUNTING"
    ADULT = "ADULT"
    ADVERTISING = "ADVERTISING"
    AFFILIATED_AUTO_RENTAL = "AFFILIATED_AUTO_RENTAL"
    AGENCIES = "AGENCIES"
    AGGREGATORS = "AGGREGATORS"
    AGRICULTURAL_COOPERATIVE_FOR_MAIL_ORDER = "AGRICULTURAL_COOPERATIVE_FOR_MAIL_ORDER"
    AIR_CARRIERS_AIRLINES = "AIR_CARRIERS_AIRLINES"
    AIRLINES = "AIRLINES"
    AIRPORTS_FLYING_FIELDS = "AIRPORTS_FLYING_FIELDS"
    ALCOHOLIC_BEVERAGES = "ALCOHOLIC_BEVERAGES"
    AMUSEMENT_PARKS_CARNIVALS = "AMUSEMENT_PARKS_CARNIVALS"
    ANIMATION = "ANIMATION"
    ANTIQUES = "ANTIQUES"
    APPLIANCES = "APPLIANCES"
    AQUARIAMS_SEAQUARIUMS_DOLPHINARIUMS = "AQUARIAMS_SEAQUARIUMS_DOLPHINARIUMS"
    ARCHITECTURAL_ENGINEERING_AND_SURVEYING_SERVICES = "ARCHITECTURAL_ENGINEERING_AND_SURVEYING_SERVICES"
    ART_AND_CRAFT_SUPPLIES = "ART_AND_CRAFT_SUPPLIES"
    ART_DEALERS_AND_GALLERIES = "ART_DEALERS_AND_GALLERIES"
    ARTIFACTS_GRAVE_RELATED_AND_NATIVE_AMERICAN_CRAFTS = "ARTIFACTS_GRAVE_RELATED_AND_NATIVE_AMERICAN_CRAFTS"
    ARTS_AND_CRAFTS = "ARTS_AND_CRAFTS"
    ARTS_CRAFTS_AND_COLLECTIBLES = "ARTS_CRAFTS_AND_COLLECTIBLES"
    AUDIO_BOOKS = "AUDIO_BOOKS"
    AUTO_ASSOCIATIONS_CLUBS = "AUTO_ASSOCIATIONS_CLUBS"
    AUTO_DEALER_USED_ONLY = "AUTO_DEALER_USED_ONLY"
    AUTO_RENTALS = "AUTO_RENTALS"
    AUTO_SERVICE = "AUTO_SERVICE"
    AUTOMATED_FUEL_DISPENSERS = "AUTOMATED_FUEL_DISPENSERS"
    AUTOMOBILE_ASSOCIATIONS = "AUTOMOBILE_ASSOCIATIONS"
    AUTOMOTIVE = "AUTOMOTIVE"
    AUTOMOTIVE_REPAIR_SHOPS_NON_DEALER = "AUTOMOTIVE_REPAIR_SHOPS_NON_DEALER"
    AUTOMOTIVE_TOP_AND_BODY_SHOPS = "AUTOMOTIVE_TOP_AND_BODY_SHOPS"
    AVIATION = "AVIATION"
    BABIES_CLOTHING_AND_SUPPLIES = "BABIES_CLOTHING_AND_SUPPLIES"
    BABY = "BABY"
    BANDS_ORCHESTRAS_ENTERTAINERS = "BANDS_ORCHESTRAS_ENTERTAINERS"
    BARBIES = "BARBIES"
    BATH_AND_BODY = "BATH_AND_BODY"
    BATTERIES = "BATTERIES"
    BEAN_BABIES = "BEAN_BABIES"
    BEAUTY = "BEAUTY"
    BEAUTY_AND_FRAGRANCES = "BEAUTY_AND_FRAGRANCES"
    BED_AND_BATH = "BED_AND_BATH"
    BICYCLE_SHOPS_SALES_AND_SERVICE = "BICYCLE_SHOPS_SALES_AND_SERVICE"
    BICYCLES_AND_ACCESSORIES = "BICYCLES_AND_ACCESSORIES"
    BILLIARD_POOL_ESTABLISHMENTS = "BILLIARD_POOL_ESTABLISHMENTS"
    BOAT_DEALERS = "BOAT_DEALERS"
    BOAT_RENTALS_AND_LEASING = "BOAT_RENTALS_AND_LEASING"
    BOATING_SAILING_AND_ACCESSORIES = "BOATING_SAILING_AND_ACCESSORIES"
    BOOKS = "BOOKS"
    BOOKS_AND_MAGAZINES = "BOOKS_AND_MAGAZINES"
    BOOKS_MANUSCRIPTS = "BOOKS_MANUSCRIPTS"
    BOOKS_PERIODICALS_AND_NEWSPAPERS = "BOOKS_PERIODICALS_AND_NEWSPAPERS"
    BOWLING_ALLEYS = "BOWLING_ALLEYS"
    BULLETIN_BOARD = "BULLETIN_BOARD"
    BUS_LINE = "BUS_LINE"
    BUS_LINES_CHARTERS_TOUR_BUSES = "BUS_LINES_CHARTERS_TOUR_BUSES"
    BUSINESS = "BUSINESS"
    BUSINESS_AND_SECRETARIAL_SCHOOLS = "BUSINESS_AND_SECRETARIAL_SCHOOLS"
    BUYING_AND_SHOPPING_SERVICES_AND_CLUBS = "BUYING_AND_SHOPPING_SERVICES_AND_CLUBS"
    CABLE_SATELLITE_AND_OTHER_PAY_TELEVISION_AND_RADIO_SERVICES = (
        "CABLE_SATELLITE_AND_OTHER_PAY_TELEVISION_AND_RADIO_SERVICES"
    )
    CABLE_SATELLITE_AND_OTHER_PAY_TV_AND_RADIO = "CABLE_SATELLITE_AND_OTHER_PAY_TV_AND_RADIO"
    CAMERA_AND_PHOTOGRAPHIC_SUPPLIES = "CAMERA_AND_PHOTOGRAPHIC_SUPPLIES"
    CAMERAS = "CAMERAS"
    CAMERAS_AND_PHOTOGRAPHY = "CAMERAS_AND_PHOTOGRAPHY"
    CAMPER_RECREATIONAL_AND_UTILITY_TRAILER_DEALERS = "CAMPER_RECREATIONAL_AND_UTILITY_TRAILER_DEALERS"
    CAMPING_AND_OUTDOORS = "CAMPING_AND_OUTDOORS"
    CAMPING_AND_SURVIVAL = "CAMPING_AND_SURVIVAL"
    CAR_AND_TRUCK_DEALERS = "CAR_AND_TRUCK_DEALERS"
    CAR_AND_TRUCK_DEALERS_USED_ONLY = "CAR_AND_TRUCK_DEALERS_USED_ONLY"
    CAR_AUDIO_AND_ELECTRONICS = "CAR_AUDIO_AND_ELECTRONICS"
    CAR_RENTAL_AGENCY = "CAR_RENTAL_AGENCY"
    CATALOG_MERCHANT = "CATALOG_MERCHANT"
    CATALOG_RETAIL_MERCHANT = "CATALOG_RETAIL_MERCHANT"
    CATERING_SERVICES = "CATERING_SERVICES"
    CHARITY = "CHARITY"
    CHECK_CASHIER = "CHECK_CASHIER"
    CHILD_CARE_SERVICES = "CHILD_CARE_SERVICES"
    CHILDREN_BOOKS = "CHILDREN_BOOKS"
    CHIROPODISTS_PODIATRISTS = "CHIROPODISTS_PODIATRISTS"
    CHIROPRACTORS = "CHIROPRACTORS"
    CIGAR_STORES_AND_STANDS = "CIGAR_STORES_AND_STANDS"
    CIVIC_SOCIAL_FRATERNAL_ASSOCIATIONS = "CIVIC_SOCIAL_FRATERNAL_ASSOCIATIONS"
    CIVIL_SOCIAL_FRAT_ASSOCIATIONS = "CIVIL_SOCIAL_FRAT_ASSOCIATIONS"
    CLOTHING = "CLOTHING"
    CLOTHING_ACCESSORIES_AND_SHOES = "CLOTHING_ACCESSORIES_AND_SHOES"
    CLOTHING_RENTAL = "CLOTHING_RENTAL"
    COFFEE_AND_TEA = "COFFEE_AND_TEA"
    COIN_OPERATED_BANKS_AND_CASINOS = "COIN_OPERATED_BANKS_AND_CASINOS"
    COLLECTIBLES = "COLLECTIBLES"
    COLLECTION_AGENCY = "COLLECTION_AGENCY"
    COLLEGES_AND_UNIVERSITIES = "COLLEGES_AND_UNIVERSITIES"
    COMMERCIAL_EQUIPMENT = "COMMERCIAL_EQUIPMENT"
    COMMERCIAL_FOOTWEAR = "COMMERCIAL_FOOTWEAR"
    COMMERCIAL_PHOTOGRAPHY = "COMMERCIAL_PHOTOGRAPHY"
    COMMERCIAL_PHOTOGRAPHY_ART_AND_GRAPHICS = "COMMERCIAL_PHOTOGRAPHY_ART_AND_GRAPHICS"
    COMMERCIAL_SPORTS_PROFESSIONA = "COMMERCIAL_SPORTS_PROFESSIONA"
    COMMODITIES_AND_FUTURES_EXCHANGE = "COMMODITIES_AND_FUTURES_EXCHANGE"
    COMPUTER_AND_DATA_PROCESSING_SERVICES = "COMPUTER_AND_DATA_PROCESSING_SERVICES"
    COMPUTER_HARDWARE_AND_SOFTWARE = "COMPUTER_HARDWARE_AND_SOFTWARE"
    COMPUTER_MAINTENANCE_REPAIR_AND_SERVICES_NOT_ELSEWHERE_CLAS = (
        "COMPUTER_MAINTENANCE_REPAIR_AND_SERVICES_NOT_ELSEWHERE_CLAS"
    )
    CONSTRUCTION = "CONSTRUCTION"
    CONSTRUCTION_MATERIALS_NOT_ELSEWHERE_CLASSIFIED = "CONSTRUCTION_MATERIALS_NOT_ELSEWHERE_CLASSIFIED"
    CONSULTING_SERVICES = "CONSULTING_SERVICES"
    CONSUMER_CREDIT_REPORTING_AGENCIES = "CONSUMER_CREDIT_REPORTING_AGENCIES"
    CONVALESCENT_HOMES = "CONVALESCENT_HOMES"
    COSMETIC_STORES = "COSMETIC_STORES"
    COUNSELING_SERVICES_DEBT_MARRIAGE_PERSONAL = "COUNSELING_SERVICES_DEBT_MARRIAGE_PERSONAL"
    COUNTERFEIT_CURRENCY_AND_STAMPS = "COUNTERFEIT_CURRENCY_AND_STAMPS"
    COUNTERFEIT_ITEMS = "COUNTERFEIT_ITEMS"
    COUNTRY_CLUBS = "COUNTRY_CLUBS"
    COURIER_SERVICES = "COURIER_SERVICES"
    COURIER_SERVICES_AIR_AND_GROUND_AND_FREIGHT_FORWARDERS = "COURIER_SERVICES_AIR_AND_GROUND_AND_FREIGHT_FORWARDERS"
    COURT_COSTS_ALIMNY_CHILD_SUPT = "COURT_COSTS_ALIMNY_CHILD_SUPT"
    COURT_COSTS_INCLUDING_ALIMONY_AND_CHILD_SUPPORT_COURTS_OF_LAW = (
        "COURT_COSTS_INCLUDING_ALIMONY_AND_CHILD_SUPPORT_COURTS_OF_LAW"
    )
    CREDIT_CARDS = "CREDIT_CARDS"
    CREDIT_UNION = "CREDIT_UNION"
    CULTURE_AND_RELIGION = "CULTURE_AND_RELIGION"
    DAIRY_PRODUCTS_STORES = "DAIRY_PRODUCTS_STORES"
    DANCE_HALLS_STUDIOS_AND_SCHOOLS = "DANCE_HALLS_STUDIOS_AND_SCHOOLS"
    DECORATIVE = "DECORATIVE"
    DENTAL = "DENTAL"
    DENTISTS_AND_ORTHODONTISTS = "DENTISTS_AND_ORTHODONTISTS"
    DEPARTMENT_STORES = "DEPARTMENT_STORES"
    DESKTOP_PCS = "DESKTOP_PCS"
    DEVICES = "DEVICES"
    DIECAST_TOYS_VEHICLES = "DIECAST_TOYS_VEHICLES"
    DIGITAL_GAMES = "DIGITAL_GAMES"
    DIGITAL_MEDIA_BOOKS_MOVIES_MUSIC = "DIGITAL_MEDIA_BOOKS_MOVIES_MUSIC"
    DIRECT_MARKETING = "DIRECT_MARKETING"
    DIRECT_MARKETING_CATALOG_MERCHANT = "DIRECT_MARKETING_CATALOG_MERCHANT"
    DIRECT_MARKETING_INBOUND_TELE = "DIRECT_MARKETING_INBOUND_TELE"
    DIRECT_MARKETING_OUTBOUND_TELE = "DIRECT_MARKETING_OUTBOUND_TELE"
    DIRECT_MARKETING_SUBSCRIPTION = "DIRECT_MARKETING_SUBSCRIPTION"
    DISCOUNT_STORES = "DISCOUNT_STORES"
    DOOR_TO_DOOR_SALES = "DOOR_TO_DOOR_SALES"
    DRAPERY_WINDOW_COVERING_AND_UPHOLSTERY = "DRAPERY_WINDOW_COVERING_AND_UPHOLSTERY"
    DRINKING_PLACES = "DRINKING_PLACES"
    DRUGSTORE = "DRUGSTORE"
    DURABLE_GOODS = "DURABLE_GOODS"
    ECOMMERCE_DEVELOPMENT = "ECOMMERCE_DEVELOPMENT"
    ECOMMERCE_SERVICES = "ECOMMERCE_SERVICES"
    EDUCATIONAL_AND_TEXTBOOKS = "EDUCATIONAL_AND_TEXTBOOKS"
    ELECTRIC_RAZOR_STORES = "ELECTRIC_RAZOR_STORES"
    ELECTRICAL_AND_SMALL_APPLIANCE_REPAIR = "ELECTRICAL_AND_SMALL_APPLIANCE_REPAIR"
    ELECTRICAL_CONTRACTORS = "ELECTRICAL_CONTRACTORS"
    ELECTRICAL_PARTS_AND_EQUIPMENT = "ELECTRICAL_PARTS_AND_EQUIPMENT"
    ELECTRONIC_CASH = "ELECTRONIC_CASH"
    ELEMENTARY_AND_SECONDARY_SCHOOLS = "ELEMENTARY_AND_SECONDARY_SCHOOLS"
    EMPLOYMENT = "EMPLOYMENT"
    ENTERTAINERS = "ENTERTAINERS"
    ENTERTAINMENT_AND_MEDIA = "ENTERTAINMENT_AND_MEDIA"
    EQUIP_TOOL_FURNITURE_AND_APPLIANCE_RENTAL_AND_LEASING = "EQUIP_TOOL_FURNITURE_AND_APPLIANCE_RENTAL_AND_LEASING"
    ESCROW = "ESCROW"
    EVENT_AND_WEDDING_PLANNING = "EVENT_AND_WEDDING_PLANNING"
    EXERCISE_AND_FITNESS = "EXERCISE_AND_FITNESS"
    EXERCISE_EQUIPMENT = "EXERCISE_EQUIPMENT"
    EXTERMINATING_AND_DISINFECTING_SERVICES = "EXTERMINATING_AND_DISINFECTING_SERVICES"
    FABRICS_AND_SEWING = "FABRICS_AND_SEWING"
    FAMILY_CLOTHING_STORES = "FAMILY_CLOTHING_STORES"
    FASHION_JEWELRY = "FASHION_JEWELRY"
    FAST_FOOD_RESTAURANTS = "FAST_FOOD_RESTAURANTS"
    FICTION_AND_NONFICTION = "FICTION_AND_NONFICTION"
    FINANCE_COMPANY = "FINANCE_COMPANY"
    FINANCIAL_AND_INVESTMENT_ADVICE = "FINANCIAL_AND_INVESTMENT_ADVICE"
    FINANCIAL_INSTITUTIONS_MERCHANDISE_AND_SERVICES = "FINANCIAL_INSTITUTIONS_MERCHANDISE_AND_SERVICES"
    FIREARM_ACCESSORIES = "FIREARM_ACCESSORIES"
    FIREARMS_WEAPONS_AND_KNIVES = "FIREARMS_WEAPONS_AND_KNIVES"
    FIREPLACE_AND_FIREPLACE_SCREENS = "FIREPLACE_AND_FIREPLACE_SCREENS"
    FIREWORKS = "FIREWORKS"
    FISHING = "FISHING"
    FLORISTS = "FLORISTS"
    FLOWERS = "FLOWERS"
    FOOD_DRINK_AND_NUTRITION = "FOOD_DRINK_AND_NUTRITION"
    FOOD_PRODUCTS = "FOOD_PRODUCTS"
    FOOD_RETAIL_AND_SERVICE = "FOOD_RETAIL_AND_SERVICE"
    FRAGRANCES_AND_PERFUMES = "FRAGRANCES_AND_PERFUMES"
    FREEZER_AND_LOCKER_MEAT_PROVISIONERS = "FREEZER_AND_LOCKER_MEAT_PROVISIONERS"
    FUEL_DEALERS_FUEL_OIL_WOOD_AND_COAL = "FUEL_DEALERS_FUEL_OIL_WOOD_AND_COAL"
    FUEL_DEALERS_NON_AUTOMOTIVE = "FUEL_DEALERS_NON_AUTOMOTIVE"
    FUNERAL_SERVICES_AND_CREMATORIES = "FUNERAL_SERVICES_AND_CREMATORIES"
    FURNISHING_AND_DECORATING = "FURNISHING_AND_DECORATING"
    FURNITURE = "FURNITURE"
    FURRIERS_AND_FUR_SHOPS = "FURRIERS_AND_FUR_SHOPS"
    GADGETS_AND_OTHER_ELECTRONICS = "GADGETS_AND_OTHER_ELECTRONICS"
    GAMBLING = "GAMBLING"
    GAME_SOFTWARE = "GAME_SOFTWARE"
    GAMES = "GAMES"
    GARDEN_SUPPLIES = "GARDEN_SUPPLIES"
    GENERAL = "GENERAL"
    GENERAL_CONTRACTORS = "GENERAL_CONTRACTORS"
    GENERAL_GOVERNMENT = "GENERAL_GOVERNMENT"
    GENERAL_SOFTWARE = "GENERAL_SOFTWARE"
    GENERAL_TELECOM = "GENERAL_TELECOM"
    GIFTS_AND_FLOWERS = "GIFTS_AND_FLOWERS"
    GLASS_PAINT_AND_WALLPAPER_STORES = "GLASS_PAINT_AND_WALLPAPER_STORES"
    GLASSWARE_CRYSTAL_STORES = "GLASSWARE_CRYSTAL_STORES"
    GOVERNMENT = "GOVERNMENT"
    GOVERNMENT_IDS_AND_LICENSES = "GOVERNMENT_IDS_AND_LICENSES"
    GOVERNMENT_LICENSED_ON_LINE_CASINOS_ON_LINE_GAMBLING = "GOVERNMENT_LICENSED_ON_LINE_CASINOS_ON_LINE_GAMBLING"
    GOVERNMENT_OWNED_LOTTERIES = "GOVERNMENT_OWNED_LOTTERIES"
    GOVERNMENT_SERVICES = "GOVERNMENT_SERVICES"
    GRAPHIC_AND_COMMERCIAL_DESIGN = "GRAPHIC_AND_COMMERCIAL_DESIGN"
    GREETING_CARDS = "GREETING_CARDS"
    GROCERY_STORES_AND_SUPERMARKETS = "GROCERY_STORES_AND_SUPERMARKETS"
    HARDWARE_AND_TOOLS = "HARDWARE_AND_TOOLS"
    HARDWARE_EQUIPMENT_AND_SUPPLIES = "HARDWARE_EQUIPMENT_AND_SUPPLIES"
    HAZARDOUS_RESTRICTED_AND_PERISHABLE_ITEMS = "HAZARDOUS_RESTRICTED_AND_PERISHABLE_ITEMS"
    HEALTH_AND_BEAUTY_SPAS = "HEALTH_AND_BEAUTY_SPAS"
    HEALTH_AND_NUTRITION = "HEALTH_AND_NUTRITION"
    HEALTH_AND_PERSONAL_CARE = "HEALTH_AND_PERSONAL_CARE"
    HEARING_AIDS_SALES_AND_SUPPLIES = "HEARING_AIDS_SALES_AND_SUPPLIES"
    HEATING_PLUMBING_AC = "HEATING_PLUMBING_AC"
    HIGH_RISK_MERCHANT = "HIGH_RISK_MERCHANT"
    HIRING_SERVICES = "HIRING_SERVICES"
    HOBBIES_TOYS_AND_GAMES = "HOBBIES_TOYS_AND_GAMES"
    HOME_AND_GARDEN = "HOME_AND_GARDEN"
    HOME_AUDIO = "HOME_AUDIO"
    HOME_DECOR = "HOME_DECOR"
    HOME_ELECTRONICS = "HOME_ELECTRONICS"
    HOSPITALS = "HOSPITALS"
    HOTELS_MOTELS_INNS_RESORTS = "HOTELS_MOTELS_INNS_RESORTS"
    HOUSEWARES = "HOUSEWARES"
    HUMAN_PARTS_AND_REMAINS = "HUMAN_PARTS_AND_REMAINS"
    HUMOROUS_GIFTS_AND_NOVELTIES = "HUMOROUS_GIFTS_AND_NOVELTIES"
    HUNTING = "HUNTING"
    IDS_LICENSES_AND_PASSPORTS = "IDS_LICENSES_AND_PASSPORTS"
    ILLEGAL_DRUGS_AND_PARAPHERNALIA = "ILLEGAL_DRUGS_AND_PARAPHERNALIA"
    INDUSTRIAL = "INDUSTRIAL"
    INDUSTRIAL_AND_MANUFACTURING_SUPPLIES = "INDUSTRIAL_AND_MANUFACTURING_SUPPLIES"
    INSURANCE_AUTO_AND_HOME = "INSURANCE_AUTO_AND_HOME"
    INSURANCE_DIRECT = "INSURANCE_DIRECT"
    INSURANCE_LIFE_AND_ANNUITY = "INSURANCE_LIFE_AND_ANNUITY"
    INSURANCE_SALES_UNDERWRITING = "INSURANCE_SALES_UNDERWRITING"
    INSURANCE_UNDERWRITING_PREMIUMS = "INSURANCE_UNDERWRITING_PREMIUMS"
    INTERNET_AND_NETWORK_SERVICES = "INTERNET_AND_NETWORK_SERVICES"
    INTRA_COMPANY_PURCHASES = "INTRA_COMPANY_PURCHASES"
    LABORATORIES_DENTAL_MEDICAL = "LABORATORIES_DENTAL_MEDICAL"
    LANDSCAPING = "LANDSCAPING"
    LANDSCAPING_AND_HORTICULTURAL_SERVICES = "LANDSCAPING_AND_HORTICULTURAL_SERVICES"
    LAUNDRY_CLEANING_SERVICES = "LAUNDRY_CLEANING_SERVICES"
    LEGAL = "LEGAL"
    LEGAL_SERVICES_AND_ATTORNEYS = "LEGAL_SERVICES_AND_ATTORNEYS"
    LOCAL_DELIVERY_SERVICE = "LOCAL_DELIVERY_SERVICE"
    LOCKSMITH = "LOCKSMITH"
    LODGING_AND_ACCOMMODATIONS = "LODGING_AND_ACCOMMODATIONS"
    LOTTERY_AND_CONTESTS = "LOTTERY_AND_CONTESTS"
    LUGGAGE_AND_LEATHER_GOODS = "LUGGAGE_AND_LEATHER_GOODS"
    LUMBER_AND_BUILDING_MATERIALS = "LUMBER_AND_BUILDING_MATERIALS"
    MAGAZINES = "MAGAZINES"
    MAINTENANCE_AND_REPAIR_SERVICES = "MAINTENANCE_AND_REPAIR_SERVICES"
    MAKEUP_AND_COSMETICS = "MAKEUP_AND_COSMETICS"
    MANUAL_CASH_DISBURSEMENTS = "MANUAL_CASH_DISBURSEMENTS"
    MASSAGE_PARLORS = "MASSAGE_PARLORS"
    MEDICAL = "MEDICAL"
    MEDICAL_AND_PHARMACEUTICAL = "MEDICAL_AND_PHARMACEUTICAL"
    MEDICAL_CARE = "MEDICAL_CARE"
    MEDICAL_EQUIPMENT_AND_SUPPLIES = "MEDICAL_EQUIPMENT_AND_SUPPLIES"
    MEDICAL_SERVICES = "MEDICAL_SERVICES"
    MEETING_PLANNERS = "MEETING_PLANNERS"
    MEMBERSHIP_CLUBS_AND_ORGANIZATIONS = "MEMBERSHIP_CLUBS_AND_ORGANIZATIONS"
    MEMBERSHIP_COUNTRY_CLUBS_GOLF = "MEMBERSHIP_COUNTRY_CLUBS_GOLF"
    MEMORABILIA = "MEMORABILIA"
    MEN_AND_BOY_CLOTHING_AND_ACCESSORY_STORES = "MEN_AND_BOY_CLOTHING_AND_ACCESSORY_STORES"
    MEN_CLOTHING = "MEN_CLOTHING"
    MERCHANDISE = "MERCHANDISE"
    METAPHYSICAL = "METAPHYSICAL"
    MILITARIA = "MILITARIA"
    MILITARY_AND_CIVIL_SERVICE_UNIFORMS = "MILITARY_AND_CIVIL_SERVICE_UNIFORMS"
    MISC_AUTOMOTIVE_AIRCRAFT_AND_FARM_EQUIPMENT_DEALERS = "MISC._AUTOMOTIVE_AIRCRAFT_AND_FARM_EQUIPMENT_DEALERS"
    MISC_GENERAL_MERCHANDISE = "MISC._GENERAL_MERCHANDISE"
    MISCELLANEOUS_GENERAL_SERVICES = "MISCELLANEOUS_GENERAL_SERVICES"
    MISCELLANEOUS_REPAIR_SHOPS_AND_RELATED_SERVICES = "MISCELLANEOUS_REPAIR_SHOPS_AND_RELATED_SERVICES"
    MODEL_KITS = "MODEL_KITS"
    MONEY_TRANSFER_MEMBER_FINANCIAL_INSTITUTION = "MONEY_TRANSFER_MEMBER_FINANCIAL_INSTITUTION"
    MONEY_TRANSFER_MERCHANT = "MONEY_TRANSFER_MERCHANT"
    MOTION_PICTURE_THEATERS = "MOTION_PICTURE_THEATERS"
    MOTOR_FREIGHT_CARRIERS_AND_TRUCKING = "MOTOR_FREIGHT_CARRIERS_AND_TRUCKING"
    MOTOR_HOME_AND_RECREATIONAL_VEHICLE_RENTAL = "MOTOR_HOME_AND_RECREATIONAL_VEHICLE_RENTAL"
    MOTOR_HOMES_DEALERS = "MOTOR_HOMES_DEALERS"
    MOTOR_VEHICLE_SUPPLIES_AND_NEW_PARTS = "MOTOR_VEHICLE_SUPPLIES_AND_NEW_PARTS"
    MOTORCYCLE_DEALERS = "MOTORCYCLE_DEALERS"
    MOTORCYCLES = "MOTORCYCLES"
    MOVIE = "MOVIE"
    MOVIE_TICKETS = "MOVIE_TICKETS"
    MOVING_AND_STORAGE = "MOVING_AND_STORAGE"
    MULTI_LEVEL_MARKETING = "MULTI_LEVEL_MARKETING"
    MUSIC_CDS_CASSETTES_AND_ALBUMS = "MUSIC_CDS_CASSETTES_AND_ALBUMS"
    MUSIC_STORE_INSTRUMENTS_AND_SHEET_MUSIC = "MUSIC_STORE_INSTRUMENTS_AND_SHEET_MUSIC"
    NETWORKING = "NETWORKING"
    NEW_AGE = "NEW_AGE"
    NEW_PARTS_AND_SUPPLIES_MOTOR_VEHICLE = "NEW_PARTS_AND_SUPPLIES_MOTOR_VEHICLE"
    NEWS_DEALERS_AND_NEWSTANDS = "NEWS_DEALERS_AND_NEWSTANDS"
    NON_DURABLE_GOODS = "NON_DURABLE_GOODS"
    NON_FICTION = "NON_FICTION"
    NON_PROFIT_POLITICAL_AND_RELIGION = "NON_PROFIT_POLITICAL_AND_RELIGION"
    NONPROFIT = "NONPROFIT"
    NOVELTIES = "NOVELTIES"
    OEM_SOFTWARE = "OEM_SOFTWARE"
    OFFICE_SUPPLIES_AND_EQUIPMENT = "OFFICE_SUPPLIES_AND_EQUIPMENT"
    ONLINE_DATING = "ONLINE_DATING"
    ONLINE_GAMING = "ONLINE_GAMING"
    ONLINE_GAMING_CURRENCY = "ONLINE_GAMING_CURRENCY"
    ONLINE_SERVICES = "ONLINE_SERVICES"
    OOUTBOUND_TELEMARKETING_MERCH = "OOUTBOUND_TELEMARKETING_MERCH"
    OPHTHALMOLOGISTS_OPTOMETRIST = "OPHTHALMOLOGISTS_OPTOMETRIST"
    OPTICIANS_AND_DISPENSING = "OPTICIANS_AND_DISPENSING"
    ORTHOPEDIC_GOODS_PROSTHETICS = "ORTHOPEDIC_GOODS_PROSTHETICS"
    OSTEOPATHS = "OSTEOPATHS"
    OTHER = "OTHER"
    PACKAGE_TOUR_OPERATORS = "PACKAGE_TOUR_OPERATORS"
    PAINTBALL = "PAINTBALL"
    PAINTS_VARNISHES_AND_SUPPLIES = "PAINTS_VARNISHES_AND_SUPPLIES"
    PARKING_LOTS_AND_GARAGES = "PARKING_LOTS_AND_GARAGES"
    PARTS_AND_ACCESSORIES = "PARTS_AND_ACCESSORIES"
    PAWN_SHOPS = "PAWN_SHOPS"
    PAYCHECK_LENDER_OR_CASH_ADVANCE = "PAYCHECK_LENDER_OR_CASH_ADVANCE"
    PERIPHERALS = "PERIPHERALS"
    PERSONALIZED_GIFTS = "PERSONALIZED_GIFTS"
    PET_SHOPS_PET_FOOD_AND_SUPPLIES = "PET_SHOPS_PET_FOOD_AND_SUPPLIES"
    PETROLEUM_AND_PETROLEUM_PRODUCTS = "PETROLEUM_AND_PETROLEUM_PRODUCTS"
    PETS_AND_ANIMALS = "PETS_AND_ANIMALS"
    PHOTOFINISHING_LABORATORIES_PHOTO_DEVELOPING = "PHOTOFINISHING_LABORATORIES_PHOTO_DEVELOPING"
    PHOTOGRAPHIC_STUDIOS_PORTRAITS = "PHOTOGRAPHIC_STUDIOS_PORTRAITS"
    PHOTOGRAPHY = "PHOTOGRAPHY"
    PHYSICAL_GOOD = "PHYSICAL_GOOD"
    PICTURE_VIDEO_PRODUCTION = "PICTURE_VIDEO_PRODUCTION"
    PIECE_GOODS_NOTIONS_AND_OTHER_DRY_GOODS = "PIECE_GOODS_NOTIONS_AND_OTHER_DRY_GOODS"
    PLANTS_AND_SEEDS = "PLANTS_AND_SEEDS"
    PLUMBING_AND_HEATING_EQUIPMENTS_AND_SUPPLIES = "PLUMBING_AND_HEATING_EQUIPMENTS_AND_SUPPLIES"
    POLICE_RELATED_ITEMS = "POLICE_RELATED_ITEMS"
    POLITICAL_ORGANIZATIONS = "POLITICAL_ORGANIZATIONS"
    POSTAL_SERVICES_GOVERNMENT_ONLY = "POSTAL_SERVICES_GOVERNMENT_ONLY"
    POSTERS = "POSTERS"
    PREPAID_AND_STORED_VALUE_CARDS = "PREPAID_AND_STORED_VALUE_CARDS"
    PRESCRIPTION_DRUGS = "PRESCRIPTION_DRUGS"
    PROMOTIONAL_ITEMS = "PROMOTIONAL_ITEMS"
    PUBLIC_WAREHOUSING_AND_STORAGE = "PUBLIC_WAREHOUSING_AND_STORAGE"
    PUBLISHING_AND_PRINTING = "PUBLISHING_AND_PRINTING"
    PUBLISHING_SERVICES = "PUBLISHING_SERVICES"
    RADAR_DECTORS = "RADAR_DECTORS"
    RADIO_TELEVISION_AND_STEREO_REPAIR = "RADIO_TELEVISION_AND_STEREO_REPAIR"
    REAL_ESTATE = "REAL_ESTATE"
    REAL_ESTATE_AGENT = "REAL_ESTATE_AGENT"
    REAL_ESTATE_AGENTS_AND_MANAGERS_RENTALS = "REAL_ESTATE_AGENTS_AND_MANAGERS_RENTALS"
    RELIGION_AND_SPIRITUALITY_FOR_PROFIT = "RELIGION_AND_SPIRITUALITY_FOR_PROFIT"
    RELIGIOUS = "RELIGIOUS"
    RELIGIOUS_ORGANIZATIONS = "RELIGIOUS_ORGANIZATIONS"
    REMITTANCE = "REMITTANCE"
    RENTAL_PROPERTY_MANAGEMENT = "RENTAL_PROPERTY_MANAGEMENT"
    RESIDENTIAL = "RESIDENTIAL"
    RETAIL = "RETAIL"
    RETAIL_FINE_JEWELRY_AND_WATCHES = "RETAIL_FINE_JEWELRY_AND_WATCHES"
    REUPHOLSTERY_AND_FURNITURE_REPAIR = "REUPHOLSTERY_AND_FURNITURE_REPAIR"
    RINGS = "RINGS"
    ROOFING_SIDING_SHEET_METAL = "ROOFING_SIDING_SHEET_METAL"
    RUGS_AND_CARPETS = "RUGS_AND_CARPETS"
    SCHOOLS_AND_COLLEGES = "SCHOOLS_AND_COLLEGES"
    SCIENCE_FICTION = "SCIENCE_FICTION"
    SCRAPBOOKING = "SCRAPBOOKING"
    SCULPTURES = "SCULPTURES"
    SECURITIES_BROKERS_AND_DEALERS = "SECURITIES_BROKERS_AND_DEALERS"
    SECURITY_AND_SURVEILLANCE = "SECURITY_AND_SURVEILLANCE"
    SECURITY_AND_SURVEILLANCE_EQUIPMENT = "SECURITY_AND_SURVEILLANCE_EQUIPMENT"
    SECURITY_BROKERS_AND_DEALERS = "SECURITY_BROKERS_AND_DEALERS"
    SEMINARS = "SEMINARS"
    SERVICE_STATIONS = "SERVICE_STATIONS"
    SERVICES = "SERVICES"
    SEWING_NEEDLEWORK_FABRIC_AND_PIECE_GOODS_STORES = "SEWING_NEEDLEWORK_FABRIC_AND_PIECE_GOODS_STORES"
    SHIPPING_AND_PACKING = "SHIPPING_AND_PACKING"
    SHOE_REPAIR_HAT_CLEANING = "SHOE_REPAIR_HAT_CLEANING"
    SHOE_STORES = "SHOE_STORES"
    SHOES = "SHOES"
    SNOWMOBILE_DEALERS = "SNOWMOBILE_DEALERS"
    SOFTWARE = "SOFTWARE"
    SPECIALTY_AND_MISC_FOOD_STORES = "SPECIALTY_AND_MISC._FOOD_STORES"
    SPECIALTY_CLEANING_POLISHING_AND_SANITATION_PREPARATIONS = (
        "SPECIALTY_CLEANING_POLISHING_AND_SANITATION_PREPARATIONS"
    )
    SPECIALTY_OR_RARE_PETS = "SPECIALTY_OR_RARE_PETS"
    SPORT_GAMES_AND_TOYS = "SPORT_GAMES_AND_TOYS"
    SPORTING_AND_RECREATIONAL_CAMPS = "SPORTING_AND_RECREATIONAL_CAMPS"
    SPORTING_GOODS = "SPORTING_GOODS"
    SPORTS_AND_OUTDOORS = "SPORTS_AND_OUTDOORS"
    SPORTS_AND_RECREATION = "SPORTS_AND_RECREATION"
    STAMP_AND_COIN = "STAMP_AND_COIN"
    STATIONARY_PRINTING_AND_WRITING_PAPER = "STATIONARY_PRINTING_AND_WRITING_PAPER"
    STENOGRAPHIC_AND_SECRETARIAL_SUPPORT_SERVICES = "STENOGRAPHIC_AND_SECRETARIAL_SUPPORT_SERVICES"
    STOCKS_BONDS_SECURITIES_AND_RELATED_CERTIFICATES = "STOCKS_BONDS_SECURITIES_AND_RELATED_CERTIFICATES"
    STORED_VALUE_CARDS = "STORED_VALUE_CARDS"
    SUPPLIES = "SUPPLIES"
    SUPPLIES_AND_TOYS = "SUPPLIES_AND_TOYS"
    SURVEILLANCE_EQUIPMENT = "SURVEILLANCE_EQUIPMENT"
    SWIMMING_POOLS_AND_SPAS = "SWIMMING_POOLS_AND_SPAS"
    SWIMMING_POOLS_SALES_SUPPLIES_SERVICES = "SWIMMING_POOLS_SALES_SUPPLIES_SERVICES"
    TAILORS_AND_ALTERATIONS = "TAILORS_AND_ALTERATIONS"
    TAX_PAYMENTS = "TAX_PAYMENTS"
    TAX_PAYMENTS_GOVERNMENT_AGENCIES = "TAX_PAYMENTS_GOVERNMENT_AGENCIES"
    TAXICABS_AND_LIMOUSINES = "TAXICABS_AND_LIMOUSINES"
    TELECOMMUNICATION_SERVICES = "TELECOMMUNICATION_SERVICES"
    TELEPHONE_CARDS = "TELEPHONE_CARDS"
    TELEPHONE_EQUIPMENT = "TELEPHONE_EQUIPMENT"
    TELEPHONE_SERVICES = "TELEPHONE_SERVICES"
    THEATER = "THEATER"
    TIRE_RETREADING_AND_REPAIR = "TIRE_RETREADING_AND_REPAIR"
    TOLL_OR_BRIDGE_FEES = "TOLL_OR_BRIDGE_FEES"
    TOOLS_AND_EQUIPMENT = "TOOLS_AND_EQUIPMENT"
    TOURIST_ATTRACTIONS_AND_EXHIBITS = "TOURIST_ATTRACTIONS_AND_EXHIBITS"
    TOWING_SERVICE = "TOWING_SERVICE"
    TOYS_AND_GAMES = "TOYS_AND_GAMES"
    TRADE_AND_VOCATIONAL_SCHOOLS = "TRADE_AND_VOCATIONAL_SCHOOLS"
    TRADEMARK_INFRINGEMENT = "TRADEMARK_INFRINGEMENT"
    TRAILER_PARKS_AND_CAMPGROUNDS = "TRAILER_PARKS_AND_CAMPGROUNDS"
    TRAINING_SERVICES = "TRAINING_SERVICES"
    TRANSPORTATION_SERVICES = "TRANSPORTATION_SERVICES"
    TRAVEL = "TRAVEL"
    TRUCK_AND_UTILITY_TRAILER_RENTALS = "TRUCK_AND_UTILITY_TRAILER_RENTALS"
    TRUCK_STOP = "TRUCK_STOP"
    TYPESETTING_PLATE_MAKING_AND_RELATED_SERVICES = "TYPESETTING_PLATE_MAKING_AND_RELATED_SERVICES"
    USED_MERCHANDISE_AND_SECONDHAND_STORES = "USED_MERCHANDISE_AND_SECONDHAND_STORES"
    USED_PARTS_MOTOR_VEHICLE = "USED_PARTS_MOTOR_VEHICLE"
    UTILITIES = "UTILITIES"
    UTILITIES_ELECTRIC_GAS_WATER_SANITARY = "UTILITIES_ELECTRIC_GAS_WATER_SANITARY"
    VARIETY_STORES = "VARIETY_STORES"
    VEHICLE_SALES = "VEHICLE_SALES"
    VEHICLE_SERVICE_AND_ACCESSORIES = "VEHICLE_SERVICE_AND_ACCESSORIES"
    VIDEO_EQUIPMENT = "VIDEO_EQUIPMENT"
    VIDEO_GAME_ARCADES_ESTABLISH = "VIDEO_GAME_ARCADES_ESTABLISH"
    VIDEO_GAMES_AND_SYSTEMS = "VIDEO_GAMES_AND_SYSTEMS"
    VIDEO_TAPE_RENTAL_STORES = "VIDEO_TAPE_RENTAL_STORES"
    VINTAGE_AND_COLLECTIBLE_VEHICLES = "VINTAGE_AND_COLLECTIBLE_VEHICLES"
    VINTAGE_AND_COLLECTIBLES = "VINTAGE_AND_COLLECTIBLES"
    VITAMINS_AND_SUPPLEMENTS = "VITAMINS_AND_SUPPLEMENTS"
    VOCATIONAL_AND_TRADE_SCHOOLS = "VOCATIONAL_AND_TRADE_SCHOOLS"
    WATCH_CLOCK_AND_JEWELRY_REPAIR = "WATCH_CLOCK_AND_JEWELRY_REPAIR"
    WEB_HOSTING_AND_DESIGN = "WEB_HOSTING_AND_DESIGN"
    WELDING_REPAIR = "WELDING_REPAIR"
    WHOLESALE_CLUBS = "WHOLESALE_CLUBS"
    WHOLESALE_FLORIST_SUPPLIERS = "WHOLESALE_FLORIST_SUPPLIERS"
    WHOLESALE_PRESCRIPTION_DRUGS = "WHOLESALE_PRESCRIPTION_DRUGS"
    WILDLIFE_PRODUCTS = "WILDLIFE_PRODUCTS"
    WIRE_TRANSFER = "WIRE_TRANSFER"
    WIRE_TRANSFER_AND_MONEY_ORDER = "WIRE_TRANSFER_AND_MONEY_ORDER"
    WOMEN_ACCESSORY_SPECIALITY = "WOMEN_ACCESSORY_SPECIALITY"
    WOMEN_CLOTHING = "WOMEN_CLOTHING"

    def visit(
        self,
        ac_refrigeration_repair: typing.Callable[[], T_Result],
        academic_software: typing.Callable[[], T_Result],
        accessories: typing.Callable[[], T_Result],
        accounting: typing.Callable[[], T_Result],
        adult: typing.Callable[[], T_Result],
        advertising: typing.Callable[[], T_Result],
        affiliated_auto_rental: typing.Callable[[], T_Result],
        agencies: typing.Callable[[], T_Result],
        aggregators: typing.Callable[[], T_Result],
        agricultural_cooperative_for_mail_order: typing.Callable[[], T_Result],
        air_carriers_airlines: typing.Callable[[], T_Result],
        airlines: typing.Callable[[], T_Result],
        airports_flying_fields: typing.Callable[[], T_Result],
        alcoholic_beverages: typing.Callable[[], T_Result],
        amusement_parks_carnivals: typing.Callable[[], T_Result],
        animation: typing.Callable[[], T_Result],
        antiques: typing.Callable[[], T_Result],
        appliances: typing.Callable[[], T_Result],
        aquariams_seaquariums_dolphinariums: typing.Callable[[], T_Result],
        architectural_engineering_and_surveying_services: typing.Callable[[], T_Result],
        art_and_craft_supplies: typing.Callable[[], T_Result],
        art_dealers_and_galleries: typing.Callable[[], T_Result],
        artifacts_grave_related_and_native_american_crafts: typing.Callable[[], T_Result],
        arts_and_crafts: typing.Callable[[], T_Result],
        arts_crafts_and_collectibles: typing.Callable[[], T_Result],
        audio_books: typing.Callable[[], T_Result],
        auto_associations_clubs: typing.Callable[[], T_Result],
        auto_dealer_used_only: typing.Callable[[], T_Result],
        auto_rentals: typing.Callable[[], T_Result],
        auto_service: typing.Callable[[], T_Result],
        automated_fuel_dispensers: typing.Callable[[], T_Result],
        automobile_associations: typing.Callable[[], T_Result],
        automotive: typing.Callable[[], T_Result],
        automotive_repair_shops_non_dealer: typing.Callable[[], T_Result],
        automotive_top_and_body_shops: typing.Callable[[], T_Result],
        aviation: typing.Callable[[], T_Result],
        babies_clothing_and_supplies: typing.Callable[[], T_Result],
        baby: typing.Callable[[], T_Result],
        bands_orchestras_entertainers: typing.Callable[[], T_Result],
        barbies: typing.Callable[[], T_Result],
        bath_and_body: typing.Callable[[], T_Result],
        batteries: typing.Callable[[], T_Result],
        bean_babies: typing.Callable[[], T_Result],
        beauty: typing.Callable[[], T_Result],
        beauty_and_fragrances: typing.Callable[[], T_Result],
        bed_and_bath: typing.Callable[[], T_Result],
        bicycle_shops_sales_and_service: typing.Callable[[], T_Result],
        bicycles_and_accessories: typing.Callable[[], T_Result],
        billiard_pool_establishments: typing.Callable[[], T_Result],
        boat_dealers: typing.Callable[[], T_Result],
        boat_rentals_and_leasing: typing.Callable[[], T_Result],
        boating_sailing_and_accessories: typing.Callable[[], T_Result],
        books: typing.Callable[[], T_Result],
        books_and_magazines: typing.Callable[[], T_Result],
        books_manuscripts: typing.Callable[[], T_Result],
        books_periodicals_and_newspapers: typing.Callable[[], T_Result],
        bowling_alleys: typing.Callable[[], T_Result],
        bulletin_board: typing.Callable[[], T_Result],
        bus_line: typing.Callable[[], T_Result],
        bus_lines_charters_tour_buses: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        business_and_secretarial_schools: typing.Callable[[], T_Result],
        buying_and_shopping_services_and_clubs: typing.Callable[[], T_Result],
        cable_satellite_and_other_pay_television_and_radio_services: typing.Callable[[], T_Result],
        cable_satellite_and_other_pay_tv_and_radio: typing.Callable[[], T_Result],
        camera_and_photographic_supplies: typing.Callable[[], T_Result],
        cameras: typing.Callable[[], T_Result],
        cameras_and_photography: typing.Callable[[], T_Result],
        camper_recreational_and_utility_trailer_dealers: typing.Callable[[], T_Result],
        camping_and_outdoors: typing.Callable[[], T_Result],
        camping_and_survival: typing.Callable[[], T_Result],
        car_and_truck_dealers: typing.Callable[[], T_Result],
        car_and_truck_dealers_used_only: typing.Callable[[], T_Result],
        car_audio_and_electronics: typing.Callable[[], T_Result],
        car_rental_agency: typing.Callable[[], T_Result],
        catalog_merchant: typing.Callable[[], T_Result],
        catalog_retail_merchant: typing.Callable[[], T_Result],
        catering_services: typing.Callable[[], T_Result],
        charity: typing.Callable[[], T_Result],
        check_cashier: typing.Callable[[], T_Result],
        child_care_services: typing.Callable[[], T_Result],
        children_books: typing.Callable[[], T_Result],
        chiropodists_podiatrists: typing.Callable[[], T_Result],
        chiropractors: typing.Callable[[], T_Result],
        cigar_stores_and_stands: typing.Callable[[], T_Result],
        civic_social_fraternal_associations: typing.Callable[[], T_Result],
        civil_social_frat_associations: typing.Callable[[], T_Result],
        clothing: typing.Callable[[], T_Result],
        clothing_accessories_and_shoes: typing.Callable[[], T_Result],
        clothing_rental: typing.Callable[[], T_Result],
        coffee_and_tea: typing.Callable[[], T_Result],
        coin_operated_banks_and_casinos: typing.Callable[[], T_Result],
        collectibles: typing.Callable[[], T_Result],
        collection_agency: typing.Callable[[], T_Result],
        colleges_and_universities: typing.Callable[[], T_Result],
        commercial_equipment: typing.Callable[[], T_Result],
        commercial_footwear: typing.Callable[[], T_Result],
        commercial_photography: typing.Callable[[], T_Result],
        commercial_photography_art_and_graphics: typing.Callable[[], T_Result],
        commercial_sports_professiona: typing.Callable[[], T_Result],
        commodities_and_futures_exchange: typing.Callable[[], T_Result],
        computer_and_data_processing_services: typing.Callable[[], T_Result],
        computer_hardware_and_software: typing.Callable[[], T_Result],
        computer_maintenance_repair_and_services_not_elsewhere_clas: typing.Callable[[], T_Result],
        construction: typing.Callable[[], T_Result],
        construction_materials_not_elsewhere_classified: typing.Callable[[], T_Result],
        consulting_services: typing.Callable[[], T_Result],
        consumer_credit_reporting_agencies: typing.Callable[[], T_Result],
        convalescent_homes: typing.Callable[[], T_Result],
        cosmetic_stores: typing.Callable[[], T_Result],
        counseling_services_debt_marriage_personal: typing.Callable[[], T_Result],
        counterfeit_currency_and_stamps: typing.Callable[[], T_Result],
        counterfeit_items: typing.Callable[[], T_Result],
        country_clubs: typing.Callable[[], T_Result],
        courier_services: typing.Callable[[], T_Result],
        courier_services_air_and_ground_and_freight_forwarders: typing.Callable[[], T_Result],
        court_costs_alimny_child_supt: typing.Callable[[], T_Result],
        court_costs_including_alimony_and_child_support_courts_of_law: typing.Callable[[], T_Result],
        credit_cards: typing.Callable[[], T_Result],
        credit_union: typing.Callable[[], T_Result],
        culture_and_religion: typing.Callable[[], T_Result],
        dairy_products_stores: typing.Callable[[], T_Result],
        dance_halls_studios_and_schools: typing.Callable[[], T_Result],
        decorative: typing.Callable[[], T_Result],
        dental: typing.Callable[[], T_Result],
        dentists_and_orthodontists: typing.Callable[[], T_Result],
        department_stores: typing.Callable[[], T_Result],
        desktop_pcs: typing.Callable[[], T_Result],
        devices: typing.Callable[[], T_Result],
        diecast_toys_vehicles: typing.Callable[[], T_Result],
        digital_games: typing.Callable[[], T_Result],
        digital_media_books_movies_music: typing.Callable[[], T_Result],
        direct_marketing: typing.Callable[[], T_Result],
        direct_marketing_catalog_merchant: typing.Callable[[], T_Result],
        direct_marketing_inbound_tele: typing.Callable[[], T_Result],
        direct_marketing_outbound_tele: typing.Callable[[], T_Result],
        direct_marketing_subscription: typing.Callable[[], T_Result],
        discount_stores: typing.Callable[[], T_Result],
        door_to_door_sales: typing.Callable[[], T_Result],
        drapery_window_covering_and_upholstery: typing.Callable[[], T_Result],
        drinking_places: typing.Callable[[], T_Result],
        drugstore: typing.Callable[[], T_Result],
        durable_goods: typing.Callable[[], T_Result],
        ecommerce_development: typing.Callable[[], T_Result],
        ecommerce_services: typing.Callable[[], T_Result],
        educational_and_textbooks: typing.Callable[[], T_Result],
        electric_razor_stores: typing.Callable[[], T_Result],
        electrical_and_small_appliance_repair: typing.Callable[[], T_Result],
        electrical_contractors: typing.Callable[[], T_Result],
        electrical_parts_and_equipment: typing.Callable[[], T_Result],
        electronic_cash: typing.Callable[[], T_Result],
        elementary_and_secondary_schools: typing.Callable[[], T_Result],
        employment: typing.Callable[[], T_Result],
        entertainers: typing.Callable[[], T_Result],
        entertainment_and_media: typing.Callable[[], T_Result],
        equip_tool_furniture_and_appliance_rental_and_leasing: typing.Callable[[], T_Result],
        escrow: typing.Callable[[], T_Result],
        event_and_wedding_planning: typing.Callable[[], T_Result],
        exercise_and_fitness: typing.Callable[[], T_Result],
        exercise_equipment: typing.Callable[[], T_Result],
        exterminating_and_disinfecting_services: typing.Callable[[], T_Result],
        fabrics_and_sewing: typing.Callable[[], T_Result],
        family_clothing_stores: typing.Callable[[], T_Result],
        fashion_jewelry: typing.Callable[[], T_Result],
        fast_food_restaurants: typing.Callable[[], T_Result],
        fiction_and_nonfiction: typing.Callable[[], T_Result],
        finance_company: typing.Callable[[], T_Result],
        financial_and_investment_advice: typing.Callable[[], T_Result],
        financial_institutions_merchandise_and_services: typing.Callable[[], T_Result],
        firearm_accessories: typing.Callable[[], T_Result],
        firearms_weapons_and_knives: typing.Callable[[], T_Result],
        fireplace_and_fireplace_screens: typing.Callable[[], T_Result],
        fireworks: typing.Callable[[], T_Result],
        fishing: typing.Callable[[], T_Result],
        florists: typing.Callable[[], T_Result],
        flowers: typing.Callable[[], T_Result],
        food_drink_and_nutrition: typing.Callable[[], T_Result],
        food_products: typing.Callable[[], T_Result],
        food_retail_and_service: typing.Callable[[], T_Result],
        fragrances_and_perfumes: typing.Callable[[], T_Result],
        freezer_and_locker_meat_provisioners: typing.Callable[[], T_Result],
        fuel_dealers_fuel_oil_wood_and_coal: typing.Callable[[], T_Result],
        fuel_dealers_non_automotive: typing.Callable[[], T_Result],
        funeral_services_and_crematories: typing.Callable[[], T_Result],
        furnishing_and_decorating: typing.Callable[[], T_Result],
        furniture: typing.Callable[[], T_Result],
        furriers_and_fur_shops: typing.Callable[[], T_Result],
        gadgets_and_other_electronics: typing.Callable[[], T_Result],
        gambling: typing.Callable[[], T_Result],
        game_software: typing.Callable[[], T_Result],
        games: typing.Callable[[], T_Result],
        garden_supplies: typing.Callable[[], T_Result],
        general: typing.Callable[[], T_Result],
        general_contractors: typing.Callable[[], T_Result],
        general_government: typing.Callable[[], T_Result],
        general_software: typing.Callable[[], T_Result],
        general_telecom: typing.Callable[[], T_Result],
        gifts_and_flowers: typing.Callable[[], T_Result],
        glass_paint_and_wallpaper_stores: typing.Callable[[], T_Result],
        glassware_crystal_stores: typing.Callable[[], T_Result],
        government: typing.Callable[[], T_Result],
        government_ids_and_licenses: typing.Callable[[], T_Result],
        government_licensed_on_line_casinos_on_line_gambling: typing.Callable[[], T_Result],
        government_owned_lotteries: typing.Callable[[], T_Result],
        government_services: typing.Callable[[], T_Result],
        graphic_and_commercial_design: typing.Callable[[], T_Result],
        greeting_cards: typing.Callable[[], T_Result],
        grocery_stores_and_supermarkets: typing.Callable[[], T_Result],
        hardware_and_tools: typing.Callable[[], T_Result],
        hardware_equipment_and_supplies: typing.Callable[[], T_Result],
        hazardous_restricted_and_perishable_items: typing.Callable[[], T_Result],
        health_and_beauty_spas: typing.Callable[[], T_Result],
        health_and_nutrition: typing.Callable[[], T_Result],
        health_and_personal_care: typing.Callable[[], T_Result],
        hearing_aids_sales_and_supplies: typing.Callable[[], T_Result],
        heating_plumbing_ac: typing.Callable[[], T_Result],
        high_risk_merchant: typing.Callable[[], T_Result],
        hiring_services: typing.Callable[[], T_Result],
        hobbies_toys_and_games: typing.Callable[[], T_Result],
        home_and_garden: typing.Callable[[], T_Result],
        home_audio: typing.Callable[[], T_Result],
        home_decor: typing.Callable[[], T_Result],
        home_electronics: typing.Callable[[], T_Result],
        hospitals: typing.Callable[[], T_Result],
        hotels_motels_inns_resorts: typing.Callable[[], T_Result],
        housewares: typing.Callable[[], T_Result],
        human_parts_and_remains: typing.Callable[[], T_Result],
        humorous_gifts_and_novelties: typing.Callable[[], T_Result],
        hunting: typing.Callable[[], T_Result],
        ids_licenses_and_passports: typing.Callable[[], T_Result],
        illegal_drugs_and_paraphernalia: typing.Callable[[], T_Result],
        industrial: typing.Callable[[], T_Result],
        industrial_and_manufacturing_supplies: typing.Callable[[], T_Result],
        insurance_auto_and_home: typing.Callable[[], T_Result],
        insurance_direct: typing.Callable[[], T_Result],
        insurance_life_and_annuity: typing.Callable[[], T_Result],
        insurance_sales_underwriting: typing.Callable[[], T_Result],
        insurance_underwriting_premiums: typing.Callable[[], T_Result],
        internet_and_network_services: typing.Callable[[], T_Result],
        intra_company_purchases: typing.Callable[[], T_Result],
        laboratories_dental_medical: typing.Callable[[], T_Result],
        landscaping: typing.Callable[[], T_Result],
        landscaping_and_horticultural_services: typing.Callable[[], T_Result],
        laundry_cleaning_services: typing.Callable[[], T_Result],
        legal: typing.Callable[[], T_Result],
        legal_services_and_attorneys: typing.Callable[[], T_Result],
        local_delivery_service: typing.Callable[[], T_Result],
        locksmith: typing.Callable[[], T_Result],
        lodging_and_accommodations: typing.Callable[[], T_Result],
        lottery_and_contests: typing.Callable[[], T_Result],
        luggage_and_leather_goods: typing.Callable[[], T_Result],
        lumber_and_building_materials: typing.Callable[[], T_Result],
        magazines: typing.Callable[[], T_Result],
        maintenance_and_repair_services: typing.Callable[[], T_Result],
        makeup_and_cosmetics: typing.Callable[[], T_Result],
        manual_cash_disbursements: typing.Callable[[], T_Result],
        massage_parlors: typing.Callable[[], T_Result],
        medical: typing.Callable[[], T_Result],
        medical_and_pharmaceutical: typing.Callable[[], T_Result],
        medical_care: typing.Callable[[], T_Result],
        medical_equipment_and_supplies: typing.Callable[[], T_Result],
        medical_services: typing.Callable[[], T_Result],
        meeting_planners: typing.Callable[[], T_Result],
        membership_clubs_and_organizations: typing.Callable[[], T_Result],
        membership_country_clubs_golf: typing.Callable[[], T_Result],
        memorabilia: typing.Callable[[], T_Result],
        men_and_boy_clothing_and_accessory_stores: typing.Callable[[], T_Result],
        men_clothing: typing.Callable[[], T_Result],
        merchandise: typing.Callable[[], T_Result],
        metaphysical: typing.Callable[[], T_Result],
        militaria: typing.Callable[[], T_Result],
        military_and_civil_service_uniforms: typing.Callable[[], T_Result],
        misc_automotive_aircraft_and_farm_equipment_dealers: typing.Callable[[], T_Result],
        misc_general_merchandise: typing.Callable[[], T_Result],
        miscellaneous_general_services: typing.Callable[[], T_Result],
        miscellaneous_repair_shops_and_related_services: typing.Callable[[], T_Result],
        model_kits: typing.Callable[[], T_Result],
        money_transfer_member_financial_institution: typing.Callable[[], T_Result],
        money_transfer_merchant: typing.Callable[[], T_Result],
        motion_picture_theaters: typing.Callable[[], T_Result],
        motor_freight_carriers_and_trucking: typing.Callable[[], T_Result],
        motor_home_and_recreational_vehicle_rental: typing.Callable[[], T_Result],
        motor_homes_dealers: typing.Callable[[], T_Result],
        motor_vehicle_supplies_and_new_parts: typing.Callable[[], T_Result],
        motorcycle_dealers: typing.Callable[[], T_Result],
        motorcycles: typing.Callable[[], T_Result],
        movie: typing.Callable[[], T_Result],
        movie_tickets: typing.Callable[[], T_Result],
        moving_and_storage: typing.Callable[[], T_Result],
        multi_level_marketing: typing.Callable[[], T_Result],
        music_cds_cassettes_and_albums: typing.Callable[[], T_Result],
        music_store_instruments_and_sheet_music: typing.Callable[[], T_Result],
        networking: typing.Callable[[], T_Result],
        new_age: typing.Callable[[], T_Result],
        new_parts_and_supplies_motor_vehicle: typing.Callable[[], T_Result],
        news_dealers_and_newstands: typing.Callable[[], T_Result],
        non_durable_goods: typing.Callable[[], T_Result],
        non_fiction: typing.Callable[[], T_Result],
        non_profit_political_and_religion: typing.Callable[[], T_Result],
        nonprofit: typing.Callable[[], T_Result],
        novelties: typing.Callable[[], T_Result],
        oem_software: typing.Callable[[], T_Result],
        office_supplies_and_equipment: typing.Callable[[], T_Result],
        online_dating: typing.Callable[[], T_Result],
        online_gaming: typing.Callable[[], T_Result],
        online_gaming_currency: typing.Callable[[], T_Result],
        online_services: typing.Callable[[], T_Result],
        ooutbound_telemarketing_merch: typing.Callable[[], T_Result],
        ophthalmologists_optometrist: typing.Callable[[], T_Result],
        opticians_and_dispensing: typing.Callable[[], T_Result],
        orthopedic_goods_prosthetics: typing.Callable[[], T_Result],
        osteopaths: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        package_tour_operators: typing.Callable[[], T_Result],
        paintball: typing.Callable[[], T_Result],
        paints_varnishes_and_supplies: typing.Callable[[], T_Result],
        parking_lots_and_garages: typing.Callable[[], T_Result],
        parts_and_accessories: typing.Callable[[], T_Result],
        pawn_shops: typing.Callable[[], T_Result],
        paycheck_lender_or_cash_advance: typing.Callable[[], T_Result],
        peripherals: typing.Callable[[], T_Result],
        personalized_gifts: typing.Callable[[], T_Result],
        pet_shops_pet_food_and_supplies: typing.Callable[[], T_Result],
        petroleum_and_petroleum_products: typing.Callable[[], T_Result],
        pets_and_animals: typing.Callable[[], T_Result],
        photofinishing_laboratories_photo_developing: typing.Callable[[], T_Result],
        photographic_studios_portraits: typing.Callable[[], T_Result],
        photography: typing.Callable[[], T_Result],
        physical_good: typing.Callable[[], T_Result],
        picture_video_production: typing.Callable[[], T_Result],
        piece_goods_notions_and_other_dry_goods: typing.Callable[[], T_Result],
        plants_and_seeds: typing.Callable[[], T_Result],
        plumbing_and_heating_equipments_and_supplies: typing.Callable[[], T_Result],
        police_related_items: typing.Callable[[], T_Result],
        political_organizations: typing.Callable[[], T_Result],
        postal_services_government_only: typing.Callable[[], T_Result],
        posters: typing.Callable[[], T_Result],
        prepaid_and_stored_value_cards: typing.Callable[[], T_Result],
        prescription_drugs: typing.Callable[[], T_Result],
        promotional_items: typing.Callable[[], T_Result],
        public_warehousing_and_storage: typing.Callable[[], T_Result],
        publishing_and_printing: typing.Callable[[], T_Result],
        publishing_services: typing.Callable[[], T_Result],
        radar_dectors: typing.Callable[[], T_Result],
        radio_television_and_stereo_repair: typing.Callable[[], T_Result],
        real_estate: typing.Callable[[], T_Result],
        real_estate_agent: typing.Callable[[], T_Result],
        real_estate_agents_and_managers_rentals: typing.Callable[[], T_Result],
        religion_and_spirituality_for_profit: typing.Callable[[], T_Result],
        religious: typing.Callable[[], T_Result],
        religious_organizations: typing.Callable[[], T_Result],
        remittance: typing.Callable[[], T_Result],
        rental_property_management: typing.Callable[[], T_Result],
        residential: typing.Callable[[], T_Result],
        retail: typing.Callable[[], T_Result],
        retail_fine_jewelry_and_watches: typing.Callable[[], T_Result],
        reupholstery_and_furniture_repair: typing.Callable[[], T_Result],
        rings: typing.Callable[[], T_Result],
        roofing_siding_sheet_metal: typing.Callable[[], T_Result],
        rugs_and_carpets: typing.Callable[[], T_Result],
        schools_and_colleges: typing.Callable[[], T_Result],
        science_fiction: typing.Callable[[], T_Result],
        scrapbooking: typing.Callable[[], T_Result],
        sculptures: typing.Callable[[], T_Result],
        securities_brokers_and_dealers: typing.Callable[[], T_Result],
        security_and_surveillance: typing.Callable[[], T_Result],
        security_and_surveillance_equipment: typing.Callable[[], T_Result],
        security_brokers_and_dealers: typing.Callable[[], T_Result],
        seminars: typing.Callable[[], T_Result],
        service_stations: typing.Callable[[], T_Result],
        services: typing.Callable[[], T_Result],
        sewing_needlework_fabric_and_piece_goods_stores: typing.Callable[[], T_Result],
        shipping_and_packing: typing.Callable[[], T_Result],
        shoe_repair_hat_cleaning: typing.Callable[[], T_Result],
        shoe_stores: typing.Callable[[], T_Result],
        shoes: typing.Callable[[], T_Result],
        snowmobile_dealers: typing.Callable[[], T_Result],
        software: typing.Callable[[], T_Result],
        specialty_and_misc_food_stores: typing.Callable[[], T_Result],
        specialty_cleaning_polishing_and_sanitation_preparations: typing.Callable[[], T_Result],
        specialty_or_rare_pets: typing.Callable[[], T_Result],
        sport_games_and_toys: typing.Callable[[], T_Result],
        sporting_and_recreational_camps: typing.Callable[[], T_Result],
        sporting_goods: typing.Callable[[], T_Result],
        sports_and_outdoors: typing.Callable[[], T_Result],
        sports_and_recreation: typing.Callable[[], T_Result],
        stamp_and_coin: typing.Callable[[], T_Result],
        stationary_printing_and_writing_paper: typing.Callable[[], T_Result],
        stenographic_and_secretarial_support_services: typing.Callable[[], T_Result],
        stocks_bonds_securities_and_related_certificates: typing.Callable[[], T_Result],
        stored_value_cards: typing.Callable[[], T_Result],
        supplies: typing.Callable[[], T_Result],
        supplies_and_toys: typing.Callable[[], T_Result],
        surveillance_equipment: typing.Callable[[], T_Result],
        swimming_pools_and_spas: typing.Callable[[], T_Result],
        swimming_pools_sales_supplies_services: typing.Callable[[], T_Result],
        tailors_and_alterations: typing.Callable[[], T_Result],
        tax_payments: typing.Callable[[], T_Result],
        tax_payments_government_agencies: typing.Callable[[], T_Result],
        taxicabs_and_limousines: typing.Callable[[], T_Result],
        telecommunication_services: typing.Callable[[], T_Result],
        telephone_cards: typing.Callable[[], T_Result],
        telephone_equipment: typing.Callable[[], T_Result],
        telephone_services: typing.Callable[[], T_Result],
        theater: typing.Callable[[], T_Result],
        tire_retreading_and_repair: typing.Callable[[], T_Result],
        toll_or_bridge_fees: typing.Callable[[], T_Result],
        tools_and_equipment: typing.Callable[[], T_Result],
        tourist_attractions_and_exhibits: typing.Callable[[], T_Result],
        towing_service: typing.Callable[[], T_Result],
        toys_and_games: typing.Callable[[], T_Result],
        trade_and_vocational_schools: typing.Callable[[], T_Result],
        trademark_infringement: typing.Callable[[], T_Result],
        trailer_parks_and_campgrounds: typing.Callable[[], T_Result],
        training_services: typing.Callable[[], T_Result],
        transportation_services: typing.Callable[[], T_Result],
        travel: typing.Callable[[], T_Result],
        truck_and_utility_trailer_rentals: typing.Callable[[], T_Result],
        truck_stop: typing.Callable[[], T_Result],
        typesetting_plate_making_and_related_services: typing.Callable[[], T_Result],
        used_merchandise_and_secondhand_stores: typing.Callable[[], T_Result],
        used_parts_motor_vehicle: typing.Callable[[], T_Result],
        utilities: typing.Callable[[], T_Result],
        utilities_electric_gas_water_sanitary: typing.Callable[[], T_Result],
        variety_stores: typing.Callable[[], T_Result],
        vehicle_sales: typing.Callable[[], T_Result],
        vehicle_service_and_accessories: typing.Callable[[], T_Result],
        video_equipment: typing.Callable[[], T_Result],
        video_game_arcades_establish: typing.Callable[[], T_Result],
        video_games_and_systems: typing.Callable[[], T_Result],
        video_tape_rental_stores: typing.Callable[[], T_Result],
        vintage_and_collectible_vehicles: typing.Callable[[], T_Result],
        vintage_and_collectibles: typing.Callable[[], T_Result],
        vitamins_and_supplements: typing.Callable[[], T_Result],
        vocational_and_trade_schools: typing.Callable[[], T_Result],
        watch_clock_and_jewelry_repair: typing.Callable[[], T_Result],
        web_hosting_and_design: typing.Callable[[], T_Result],
        welding_repair: typing.Callable[[], T_Result],
        wholesale_clubs: typing.Callable[[], T_Result],
        wholesale_florist_suppliers: typing.Callable[[], T_Result],
        wholesale_prescription_drugs: typing.Callable[[], T_Result],
        wildlife_products: typing.Callable[[], T_Result],
        wire_transfer: typing.Callable[[], T_Result],
        wire_transfer_and_money_order: typing.Callable[[], T_Result],
        women_accessory_speciality: typing.Callable[[], T_Result],
        women_clothing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProductCategory.AC_REFRIGERATION_REPAIR:
            return ac_refrigeration_repair()
        if self is ProductCategory.ACADEMIC_SOFTWARE:
            return academic_software()
        if self is ProductCategory.ACCESSORIES:
            return accessories()
        if self is ProductCategory.ACCOUNTING:
            return accounting()
        if self is ProductCategory.ADULT:
            return adult()
        if self is ProductCategory.ADVERTISING:
            return advertising()
        if self is ProductCategory.AFFILIATED_AUTO_RENTAL:
            return affiliated_auto_rental()
        if self is ProductCategory.AGENCIES:
            return agencies()
        if self is ProductCategory.AGGREGATORS:
            return aggregators()
        if self is ProductCategory.AGRICULTURAL_COOPERATIVE_FOR_MAIL_ORDER:
            return agricultural_cooperative_for_mail_order()
        if self is ProductCategory.AIR_CARRIERS_AIRLINES:
            return air_carriers_airlines()
        if self is ProductCategory.AIRLINES:
            return airlines()
        if self is ProductCategory.AIRPORTS_FLYING_FIELDS:
            return airports_flying_fields()
        if self is ProductCategory.ALCOHOLIC_BEVERAGES:
            return alcoholic_beverages()
        if self is ProductCategory.AMUSEMENT_PARKS_CARNIVALS:
            return amusement_parks_carnivals()
        if self is ProductCategory.ANIMATION:
            return animation()
        if self is ProductCategory.ANTIQUES:
            return antiques()
        if self is ProductCategory.APPLIANCES:
            return appliances()
        if self is ProductCategory.AQUARIAMS_SEAQUARIUMS_DOLPHINARIUMS:
            return aquariams_seaquariums_dolphinariums()
        if self is ProductCategory.ARCHITECTURAL_ENGINEERING_AND_SURVEYING_SERVICES:
            return architectural_engineering_and_surveying_services()
        if self is ProductCategory.ART_AND_CRAFT_SUPPLIES:
            return art_and_craft_supplies()
        if self is ProductCategory.ART_DEALERS_AND_GALLERIES:
            return art_dealers_and_galleries()
        if self is ProductCategory.ARTIFACTS_GRAVE_RELATED_AND_NATIVE_AMERICAN_CRAFTS:
            return artifacts_grave_related_and_native_american_crafts()
        if self is ProductCategory.ARTS_AND_CRAFTS:
            return arts_and_crafts()
        if self is ProductCategory.ARTS_CRAFTS_AND_COLLECTIBLES:
            return arts_crafts_and_collectibles()
        if self is ProductCategory.AUDIO_BOOKS:
            return audio_books()
        if self is ProductCategory.AUTO_ASSOCIATIONS_CLUBS:
            return auto_associations_clubs()
        if self is ProductCategory.AUTO_DEALER_USED_ONLY:
            return auto_dealer_used_only()
        if self is ProductCategory.AUTO_RENTALS:
            return auto_rentals()
        if self is ProductCategory.AUTO_SERVICE:
            return auto_service()
        if self is ProductCategory.AUTOMATED_FUEL_DISPENSERS:
            return automated_fuel_dispensers()
        if self is ProductCategory.AUTOMOBILE_ASSOCIATIONS:
            return automobile_associations()
        if self is ProductCategory.AUTOMOTIVE:
            return automotive()
        if self is ProductCategory.AUTOMOTIVE_REPAIR_SHOPS_NON_DEALER:
            return automotive_repair_shops_non_dealer()
        if self is ProductCategory.AUTOMOTIVE_TOP_AND_BODY_SHOPS:
            return automotive_top_and_body_shops()
        if self is ProductCategory.AVIATION:
            return aviation()
        if self is ProductCategory.BABIES_CLOTHING_AND_SUPPLIES:
            return babies_clothing_and_supplies()
        if self is ProductCategory.BABY:
            return baby()
        if self is ProductCategory.BANDS_ORCHESTRAS_ENTERTAINERS:
            return bands_orchestras_entertainers()
        if self is ProductCategory.BARBIES:
            return barbies()
        if self is ProductCategory.BATH_AND_BODY:
            return bath_and_body()
        if self is ProductCategory.BATTERIES:
            return batteries()
        if self is ProductCategory.BEAN_BABIES:
            return bean_babies()
        if self is ProductCategory.BEAUTY:
            return beauty()
        if self is ProductCategory.BEAUTY_AND_FRAGRANCES:
            return beauty_and_fragrances()
        if self is ProductCategory.BED_AND_BATH:
            return bed_and_bath()
        if self is ProductCategory.BICYCLE_SHOPS_SALES_AND_SERVICE:
            return bicycle_shops_sales_and_service()
        if self is ProductCategory.BICYCLES_AND_ACCESSORIES:
            return bicycles_and_accessories()
        if self is ProductCategory.BILLIARD_POOL_ESTABLISHMENTS:
            return billiard_pool_establishments()
        if self is ProductCategory.BOAT_DEALERS:
            return boat_dealers()
        if self is ProductCategory.BOAT_RENTALS_AND_LEASING:
            return boat_rentals_and_leasing()
        if self is ProductCategory.BOATING_SAILING_AND_ACCESSORIES:
            return boating_sailing_and_accessories()
        if self is ProductCategory.BOOKS:
            return books()
        if self is ProductCategory.BOOKS_AND_MAGAZINES:
            return books_and_magazines()
        if self is ProductCategory.BOOKS_MANUSCRIPTS:
            return books_manuscripts()
        if self is ProductCategory.BOOKS_PERIODICALS_AND_NEWSPAPERS:
            return books_periodicals_and_newspapers()
        if self is ProductCategory.BOWLING_ALLEYS:
            return bowling_alleys()
        if self is ProductCategory.BULLETIN_BOARD:
            return bulletin_board()
        if self is ProductCategory.BUS_LINE:
            return bus_line()
        if self is ProductCategory.BUS_LINES_CHARTERS_TOUR_BUSES:
            return bus_lines_charters_tour_buses()
        if self is ProductCategory.BUSINESS:
            return business()
        if self is ProductCategory.BUSINESS_AND_SECRETARIAL_SCHOOLS:
            return business_and_secretarial_schools()
        if self is ProductCategory.BUYING_AND_SHOPPING_SERVICES_AND_CLUBS:
            return buying_and_shopping_services_and_clubs()
        if self is ProductCategory.CABLE_SATELLITE_AND_OTHER_PAY_TELEVISION_AND_RADIO_SERVICES:
            return cable_satellite_and_other_pay_television_and_radio_services()
        if self is ProductCategory.CABLE_SATELLITE_AND_OTHER_PAY_TV_AND_RADIO:
            return cable_satellite_and_other_pay_tv_and_radio()
        if self is ProductCategory.CAMERA_AND_PHOTOGRAPHIC_SUPPLIES:
            return camera_and_photographic_supplies()
        if self is ProductCategory.CAMERAS:
            return cameras()
        if self is ProductCategory.CAMERAS_AND_PHOTOGRAPHY:
            return cameras_and_photography()
        if self is ProductCategory.CAMPER_RECREATIONAL_AND_UTILITY_TRAILER_DEALERS:
            return camper_recreational_and_utility_trailer_dealers()
        if self is ProductCategory.CAMPING_AND_OUTDOORS:
            return camping_and_outdoors()
        if self is ProductCategory.CAMPING_AND_SURVIVAL:
            return camping_and_survival()
        if self is ProductCategory.CAR_AND_TRUCK_DEALERS:
            return car_and_truck_dealers()
        if self is ProductCategory.CAR_AND_TRUCK_DEALERS_USED_ONLY:
            return car_and_truck_dealers_used_only()
        if self is ProductCategory.CAR_AUDIO_AND_ELECTRONICS:
            return car_audio_and_electronics()
        if self is ProductCategory.CAR_RENTAL_AGENCY:
            return car_rental_agency()
        if self is ProductCategory.CATALOG_MERCHANT:
            return catalog_merchant()
        if self is ProductCategory.CATALOG_RETAIL_MERCHANT:
            return catalog_retail_merchant()
        if self is ProductCategory.CATERING_SERVICES:
            return catering_services()
        if self is ProductCategory.CHARITY:
            return charity()
        if self is ProductCategory.CHECK_CASHIER:
            return check_cashier()
        if self is ProductCategory.CHILD_CARE_SERVICES:
            return child_care_services()
        if self is ProductCategory.CHILDREN_BOOKS:
            return children_books()
        if self is ProductCategory.CHIROPODISTS_PODIATRISTS:
            return chiropodists_podiatrists()
        if self is ProductCategory.CHIROPRACTORS:
            return chiropractors()
        if self is ProductCategory.CIGAR_STORES_AND_STANDS:
            return cigar_stores_and_stands()
        if self is ProductCategory.CIVIC_SOCIAL_FRATERNAL_ASSOCIATIONS:
            return civic_social_fraternal_associations()
        if self is ProductCategory.CIVIL_SOCIAL_FRAT_ASSOCIATIONS:
            return civil_social_frat_associations()
        if self is ProductCategory.CLOTHING:
            return clothing()
        if self is ProductCategory.CLOTHING_ACCESSORIES_AND_SHOES:
            return clothing_accessories_and_shoes()
        if self is ProductCategory.CLOTHING_RENTAL:
            return clothing_rental()
        if self is ProductCategory.COFFEE_AND_TEA:
            return coffee_and_tea()
        if self is ProductCategory.COIN_OPERATED_BANKS_AND_CASINOS:
            return coin_operated_banks_and_casinos()
        if self is ProductCategory.COLLECTIBLES:
            return collectibles()
        if self is ProductCategory.COLLECTION_AGENCY:
            return collection_agency()
        if self is ProductCategory.COLLEGES_AND_UNIVERSITIES:
            return colleges_and_universities()
        if self is ProductCategory.COMMERCIAL_EQUIPMENT:
            return commercial_equipment()
        if self is ProductCategory.COMMERCIAL_FOOTWEAR:
            return commercial_footwear()
        if self is ProductCategory.COMMERCIAL_PHOTOGRAPHY:
            return commercial_photography()
        if self is ProductCategory.COMMERCIAL_PHOTOGRAPHY_ART_AND_GRAPHICS:
            return commercial_photography_art_and_graphics()
        if self is ProductCategory.COMMERCIAL_SPORTS_PROFESSIONA:
            return commercial_sports_professiona()
        if self is ProductCategory.COMMODITIES_AND_FUTURES_EXCHANGE:
            return commodities_and_futures_exchange()
        if self is ProductCategory.COMPUTER_AND_DATA_PROCESSING_SERVICES:
            return computer_and_data_processing_services()
        if self is ProductCategory.COMPUTER_HARDWARE_AND_SOFTWARE:
            return computer_hardware_and_software()
        if self is ProductCategory.COMPUTER_MAINTENANCE_REPAIR_AND_SERVICES_NOT_ELSEWHERE_CLAS:
            return computer_maintenance_repair_and_services_not_elsewhere_clas()
        if self is ProductCategory.CONSTRUCTION:
            return construction()
        if self is ProductCategory.CONSTRUCTION_MATERIALS_NOT_ELSEWHERE_CLASSIFIED:
            return construction_materials_not_elsewhere_classified()
        if self is ProductCategory.CONSULTING_SERVICES:
            return consulting_services()
        if self is ProductCategory.CONSUMER_CREDIT_REPORTING_AGENCIES:
            return consumer_credit_reporting_agencies()
        if self is ProductCategory.CONVALESCENT_HOMES:
            return convalescent_homes()
        if self is ProductCategory.COSMETIC_STORES:
            return cosmetic_stores()
        if self is ProductCategory.COUNSELING_SERVICES_DEBT_MARRIAGE_PERSONAL:
            return counseling_services_debt_marriage_personal()
        if self is ProductCategory.COUNTERFEIT_CURRENCY_AND_STAMPS:
            return counterfeit_currency_and_stamps()
        if self is ProductCategory.COUNTERFEIT_ITEMS:
            return counterfeit_items()
        if self is ProductCategory.COUNTRY_CLUBS:
            return country_clubs()
        if self is ProductCategory.COURIER_SERVICES:
            return courier_services()
        if self is ProductCategory.COURIER_SERVICES_AIR_AND_GROUND_AND_FREIGHT_FORWARDERS:
            return courier_services_air_and_ground_and_freight_forwarders()
        if self is ProductCategory.COURT_COSTS_ALIMNY_CHILD_SUPT:
            return court_costs_alimny_child_supt()
        if self is ProductCategory.COURT_COSTS_INCLUDING_ALIMONY_AND_CHILD_SUPPORT_COURTS_OF_LAW:
            return court_costs_including_alimony_and_child_support_courts_of_law()
        if self is ProductCategory.CREDIT_CARDS:
            return credit_cards()
        if self is ProductCategory.CREDIT_UNION:
            return credit_union()
        if self is ProductCategory.CULTURE_AND_RELIGION:
            return culture_and_religion()
        if self is ProductCategory.DAIRY_PRODUCTS_STORES:
            return dairy_products_stores()
        if self is ProductCategory.DANCE_HALLS_STUDIOS_AND_SCHOOLS:
            return dance_halls_studios_and_schools()
        if self is ProductCategory.DECORATIVE:
            return decorative()
        if self is ProductCategory.DENTAL:
            return dental()
        if self is ProductCategory.DENTISTS_AND_ORTHODONTISTS:
            return dentists_and_orthodontists()
        if self is ProductCategory.DEPARTMENT_STORES:
            return department_stores()
        if self is ProductCategory.DESKTOP_PCS:
            return desktop_pcs()
        if self is ProductCategory.DEVICES:
            return devices()
        if self is ProductCategory.DIECAST_TOYS_VEHICLES:
            return diecast_toys_vehicles()
        if self is ProductCategory.DIGITAL_GAMES:
            return digital_games()
        if self is ProductCategory.DIGITAL_MEDIA_BOOKS_MOVIES_MUSIC:
            return digital_media_books_movies_music()
        if self is ProductCategory.DIRECT_MARKETING:
            return direct_marketing()
        if self is ProductCategory.DIRECT_MARKETING_CATALOG_MERCHANT:
            return direct_marketing_catalog_merchant()
        if self is ProductCategory.DIRECT_MARKETING_INBOUND_TELE:
            return direct_marketing_inbound_tele()
        if self is ProductCategory.DIRECT_MARKETING_OUTBOUND_TELE:
            return direct_marketing_outbound_tele()
        if self is ProductCategory.DIRECT_MARKETING_SUBSCRIPTION:
            return direct_marketing_subscription()
        if self is ProductCategory.DISCOUNT_STORES:
            return discount_stores()
        if self is ProductCategory.DOOR_TO_DOOR_SALES:
            return door_to_door_sales()
        if self is ProductCategory.DRAPERY_WINDOW_COVERING_AND_UPHOLSTERY:
            return drapery_window_covering_and_upholstery()
        if self is ProductCategory.DRINKING_PLACES:
            return drinking_places()
        if self is ProductCategory.DRUGSTORE:
            return drugstore()
        if self is ProductCategory.DURABLE_GOODS:
            return durable_goods()
        if self is ProductCategory.ECOMMERCE_DEVELOPMENT:
            return ecommerce_development()
        if self is ProductCategory.ECOMMERCE_SERVICES:
            return ecommerce_services()
        if self is ProductCategory.EDUCATIONAL_AND_TEXTBOOKS:
            return educational_and_textbooks()
        if self is ProductCategory.ELECTRIC_RAZOR_STORES:
            return electric_razor_stores()
        if self is ProductCategory.ELECTRICAL_AND_SMALL_APPLIANCE_REPAIR:
            return electrical_and_small_appliance_repair()
        if self is ProductCategory.ELECTRICAL_CONTRACTORS:
            return electrical_contractors()
        if self is ProductCategory.ELECTRICAL_PARTS_AND_EQUIPMENT:
            return electrical_parts_and_equipment()
        if self is ProductCategory.ELECTRONIC_CASH:
            return electronic_cash()
        if self is ProductCategory.ELEMENTARY_AND_SECONDARY_SCHOOLS:
            return elementary_and_secondary_schools()
        if self is ProductCategory.EMPLOYMENT:
            return employment()
        if self is ProductCategory.ENTERTAINERS:
            return entertainers()
        if self is ProductCategory.ENTERTAINMENT_AND_MEDIA:
            return entertainment_and_media()
        if self is ProductCategory.EQUIP_TOOL_FURNITURE_AND_APPLIANCE_RENTAL_AND_LEASING:
            return equip_tool_furniture_and_appliance_rental_and_leasing()
        if self is ProductCategory.ESCROW:
            return escrow()
        if self is ProductCategory.EVENT_AND_WEDDING_PLANNING:
            return event_and_wedding_planning()
        if self is ProductCategory.EXERCISE_AND_FITNESS:
            return exercise_and_fitness()
        if self is ProductCategory.EXERCISE_EQUIPMENT:
            return exercise_equipment()
        if self is ProductCategory.EXTERMINATING_AND_DISINFECTING_SERVICES:
            return exterminating_and_disinfecting_services()
        if self is ProductCategory.FABRICS_AND_SEWING:
            return fabrics_and_sewing()
        if self is ProductCategory.FAMILY_CLOTHING_STORES:
            return family_clothing_stores()
        if self is ProductCategory.FASHION_JEWELRY:
            return fashion_jewelry()
        if self is ProductCategory.FAST_FOOD_RESTAURANTS:
            return fast_food_restaurants()
        if self is ProductCategory.FICTION_AND_NONFICTION:
            return fiction_and_nonfiction()
        if self is ProductCategory.FINANCE_COMPANY:
            return finance_company()
        if self is ProductCategory.FINANCIAL_AND_INVESTMENT_ADVICE:
            return financial_and_investment_advice()
        if self is ProductCategory.FINANCIAL_INSTITUTIONS_MERCHANDISE_AND_SERVICES:
            return financial_institutions_merchandise_and_services()
        if self is ProductCategory.FIREARM_ACCESSORIES:
            return firearm_accessories()
        if self is ProductCategory.FIREARMS_WEAPONS_AND_KNIVES:
            return firearms_weapons_and_knives()
        if self is ProductCategory.FIREPLACE_AND_FIREPLACE_SCREENS:
            return fireplace_and_fireplace_screens()
        if self is ProductCategory.FIREWORKS:
            return fireworks()
        if self is ProductCategory.FISHING:
            return fishing()
        if self is ProductCategory.FLORISTS:
            return florists()
        if self is ProductCategory.FLOWERS:
            return flowers()
        if self is ProductCategory.FOOD_DRINK_AND_NUTRITION:
            return food_drink_and_nutrition()
        if self is ProductCategory.FOOD_PRODUCTS:
            return food_products()
        if self is ProductCategory.FOOD_RETAIL_AND_SERVICE:
            return food_retail_and_service()
        if self is ProductCategory.FRAGRANCES_AND_PERFUMES:
            return fragrances_and_perfumes()
        if self is ProductCategory.FREEZER_AND_LOCKER_MEAT_PROVISIONERS:
            return freezer_and_locker_meat_provisioners()
        if self is ProductCategory.FUEL_DEALERS_FUEL_OIL_WOOD_AND_COAL:
            return fuel_dealers_fuel_oil_wood_and_coal()
        if self is ProductCategory.FUEL_DEALERS_NON_AUTOMOTIVE:
            return fuel_dealers_non_automotive()
        if self is ProductCategory.FUNERAL_SERVICES_AND_CREMATORIES:
            return funeral_services_and_crematories()
        if self is ProductCategory.FURNISHING_AND_DECORATING:
            return furnishing_and_decorating()
        if self is ProductCategory.FURNITURE:
            return furniture()
        if self is ProductCategory.FURRIERS_AND_FUR_SHOPS:
            return furriers_and_fur_shops()
        if self is ProductCategory.GADGETS_AND_OTHER_ELECTRONICS:
            return gadgets_and_other_electronics()
        if self is ProductCategory.GAMBLING:
            return gambling()
        if self is ProductCategory.GAME_SOFTWARE:
            return game_software()
        if self is ProductCategory.GAMES:
            return games()
        if self is ProductCategory.GARDEN_SUPPLIES:
            return garden_supplies()
        if self is ProductCategory.GENERAL:
            return general()
        if self is ProductCategory.GENERAL_CONTRACTORS:
            return general_contractors()
        if self is ProductCategory.GENERAL_GOVERNMENT:
            return general_government()
        if self is ProductCategory.GENERAL_SOFTWARE:
            return general_software()
        if self is ProductCategory.GENERAL_TELECOM:
            return general_telecom()
        if self is ProductCategory.GIFTS_AND_FLOWERS:
            return gifts_and_flowers()
        if self is ProductCategory.GLASS_PAINT_AND_WALLPAPER_STORES:
            return glass_paint_and_wallpaper_stores()
        if self is ProductCategory.GLASSWARE_CRYSTAL_STORES:
            return glassware_crystal_stores()
        if self is ProductCategory.GOVERNMENT:
            return government()
        if self is ProductCategory.GOVERNMENT_IDS_AND_LICENSES:
            return government_ids_and_licenses()
        if self is ProductCategory.GOVERNMENT_LICENSED_ON_LINE_CASINOS_ON_LINE_GAMBLING:
            return government_licensed_on_line_casinos_on_line_gambling()
        if self is ProductCategory.GOVERNMENT_OWNED_LOTTERIES:
            return government_owned_lotteries()
        if self is ProductCategory.GOVERNMENT_SERVICES:
            return government_services()
        if self is ProductCategory.GRAPHIC_AND_COMMERCIAL_DESIGN:
            return graphic_and_commercial_design()
        if self is ProductCategory.GREETING_CARDS:
            return greeting_cards()
        if self is ProductCategory.GROCERY_STORES_AND_SUPERMARKETS:
            return grocery_stores_and_supermarkets()
        if self is ProductCategory.HARDWARE_AND_TOOLS:
            return hardware_and_tools()
        if self is ProductCategory.HARDWARE_EQUIPMENT_AND_SUPPLIES:
            return hardware_equipment_and_supplies()
        if self is ProductCategory.HAZARDOUS_RESTRICTED_AND_PERISHABLE_ITEMS:
            return hazardous_restricted_and_perishable_items()
        if self is ProductCategory.HEALTH_AND_BEAUTY_SPAS:
            return health_and_beauty_spas()
        if self is ProductCategory.HEALTH_AND_NUTRITION:
            return health_and_nutrition()
        if self is ProductCategory.HEALTH_AND_PERSONAL_CARE:
            return health_and_personal_care()
        if self is ProductCategory.HEARING_AIDS_SALES_AND_SUPPLIES:
            return hearing_aids_sales_and_supplies()
        if self is ProductCategory.HEATING_PLUMBING_AC:
            return heating_plumbing_ac()
        if self is ProductCategory.HIGH_RISK_MERCHANT:
            return high_risk_merchant()
        if self is ProductCategory.HIRING_SERVICES:
            return hiring_services()
        if self is ProductCategory.HOBBIES_TOYS_AND_GAMES:
            return hobbies_toys_and_games()
        if self is ProductCategory.HOME_AND_GARDEN:
            return home_and_garden()
        if self is ProductCategory.HOME_AUDIO:
            return home_audio()
        if self is ProductCategory.HOME_DECOR:
            return home_decor()
        if self is ProductCategory.HOME_ELECTRONICS:
            return home_electronics()
        if self is ProductCategory.HOSPITALS:
            return hospitals()
        if self is ProductCategory.HOTELS_MOTELS_INNS_RESORTS:
            return hotels_motels_inns_resorts()
        if self is ProductCategory.HOUSEWARES:
            return housewares()
        if self is ProductCategory.HUMAN_PARTS_AND_REMAINS:
            return human_parts_and_remains()
        if self is ProductCategory.HUMOROUS_GIFTS_AND_NOVELTIES:
            return humorous_gifts_and_novelties()
        if self is ProductCategory.HUNTING:
            return hunting()
        if self is ProductCategory.IDS_LICENSES_AND_PASSPORTS:
            return ids_licenses_and_passports()
        if self is ProductCategory.ILLEGAL_DRUGS_AND_PARAPHERNALIA:
            return illegal_drugs_and_paraphernalia()
        if self is ProductCategory.INDUSTRIAL:
            return industrial()
        if self is ProductCategory.INDUSTRIAL_AND_MANUFACTURING_SUPPLIES:
            return industrial_and_manufacturing_supplies()
        if self is ProductCategory.INSURANCE_AUTO_AND_HOME:
            return insurance_auto_and_home()
        if self is ProductCategory.INSURANCE_DIRECT:
            return insurance_direct()
        if self is ProductCategory.INSURANCE_LIFE_AND_ANNUITY:
            return insurance_life_and_annuity()
        if self is ProductCategory.INSURANCE_SALES_UNDERWRITING:
            return insurance_sales_underwriting()
        if self is ProductCategory.INSURANCE_UNDERWRITING_PREMIUMS:
            return insurance_underwriting_premiums()
        if self is ProductCategory.INTERNET_AND_NETWORK_SERVICES:
            return internet_and_network_services()
        if self is ProductCategory.INTRA_COMPANY_PURCHASES:
            return intra_company_purchases()
        if self is ProductCategory.LABORATORIES_DENTAL_MEDICAL:
            return laboratories_dental_medical()
        if self is ProductCategory.LANDSCAPING:
            return landscaping()
        if self is ProductCategory.LANDSCAPING_AND_HORTICULTURAL_SERVICES:
            return landscaping_and_horticultural_services()
        if self is ProductCategory.LAUNDRY_CLEANING_SERVICES:
            return laundry_cleaning_services()
        if self is ProductCategory.LEGAL:
            return legal()
        if self is ProductCategory.LEGAL_SERVICES_AND_ATTORNEYS:
            return legal_services_and_attorneys()
        if self is ProductCategory.LOCAL_DELIVERY_SERVICE:
            return local_delivery_service()
        if self is ProductCategory.LOCKSMITH:
            return locksmith()
        if self is ProductCategory.LODGING_AND_ACCOMMODATIONS:
            return lodging_and_accommodations()
        if self is ProductCategory.LOTTERY_AND_CONTESTS:
            return lottery_and_contests()
        if self is ProductCategory.LUGGAGE_AND_LEATHER_GOODS:
            return luggage_and_leather_goods()
        if self is ProductCategory.LUMBER_AND_BUILDING_MATERIALS:
            return lumber_and_building_materials()
        if self is ProductCategory.MAGAZINES:
            return magazines()
        if self is ProductCategory.MAINTENANCE_AND_REPAIR_SERVICES:
            return maintenance_and_repair_services()
        if self is ProductCategory.MAKEUP_AND_COSMETICS:
            return makeup_and_cosmetics()
        if self is ProductCategory.MANUAL_CASH_DISBURSEMENTS:
            return manual_cash_disbursements()
        if self is ProductCategory.MASSAGE_PARLORS:
            return massage_parlors()
        if self is ProductCategory.MEDICAL:
            return medical()
        if self is ProductCategory.MEDICAL_AND_PHARMACEUTICAL:
            return medical_and_pharmaceutical()
        if self is ProductCategory.MEDICAL_CARE:
            return medical_care()
        if self is ProductCategory.MEDICAL_EQUIPMENT_AND_SUPPLIES:
            return medical_equipment_and_supplies()
        if self is ProductCategory.MEDICAL_SERVICES:
            return medical_services()
        if self is ProductCategory.MEETING_PLANNERS:
            return meeting_planners()
        if self is ProductCategory.MEMBERSHIP_CLUBS_AND_ORGANIZATIONS:
            return membership_clubs_and_organizations()
        if self is ProductCategory.MEMBERSHIP_COUNTRY_CLUBS_GOLF:
            return membership_country_clubs_golf()
        if self is ProductCategory.MEMORABILIA:
            return memorabilia()
        if self is ProductCategory.MEN_AND_BOY_CLOTHING_AND_ACCESSORY_STORES:
            return men_and_boy_clothing_and_accessory_stores()
        if self is ProductCategory.MEN_CLOTHING:
            return men_clothing()
        if self is ProductCategory.MERCHANDISE:
            return merchandise()
        if self is ProductCategory.METAPHYSICAL:
            return metaphysical()
        if self is ProductCategory.MILITARIA:
            return militaria()
        if self is ProductCategory.MILITARY_AND_CIVIL_SERVICE_UNIFORMS:
            return military_and_civil_service_uniforms()
        if self is ProductCategory.MISC_AUTOMOTIVE_AIRCRAFT_AND_FARM_EQUIPMENT_DEALERS:
            return misc_automotive_aircraft_and_farm_equipment_dealers()
        if self is ProductCategory.MISC_GENERAL_MERCHANDISE:
            return misc_general_merchandise()
        if self is ProductCategory.MISCELLANEOUS_GENERAL_SERVICES:
            return miscellaneous_general_services()
        if self is ProductCategory.MISCELLANEOUS_REPAIR_SHOPS_AND_RELATED_SERVICES:
            return miscellaneous_repair_shops_and_related_services()
        if self is ProductCategory.MODEL_KITS:
            return model_kits()
        if self is ProductCategory.MONEY_TRANSFER_MEMBER_FINANCIAL_INSTITUTION:
            return money_transfer_member_financial_institution()
        if self is ProductCategory.MONEY_TRANSFER_MERCHANT:
            return money_transfer_merchant()
        if self is ProductCategory.MOTION_PICTURE_THEATERS:
            return motion_picture_theaters()
        if self is ProductCategory.MOTOR_FREIGHT_CARRIERS_AND_TRUCKING:
            return motor_freight_carriers_and_trucking()
        if self is ProductCategory.MOTOR_HOME_AND_RECREATIONAL_VEHICLE_RENTAL:
            return motor_home_and_recreational_vehicle_rental()
        if self is ProductCategory.MOTOR_HOMES_DEALERS:
            return motor_homes_dealers()
        if self is ProductCategory.MOTOR_VEHICLE_SUPPLIES_AND_NEW_PARTS:
            return motor_vehicle_supplies_and_new_parts()
        if self is ProductCategory.MOTORCYCLE_DEALERS:
            return motorcycle_dealers()
        if self is ProductCategory.MOTORCYCLES:
            return motorcycles()
        if self is ProductCategory.MOVIE:
            return movie()
        if self is ProductCategory.MOVIE_TICKETS:
            return movie_tickets()
        if self is ProductCategory.MOVING_AND_STORAGE:
            return moving_and_storage()
        if self is ProductCategory.MULTI_LEVEL_MARKETING:
            return multi_level_marketing()
        if self is ProductCategory.MUSIC_CDS_CASSETTES_AND_ALBUMS:
            return music_cds_cassettes_and_albums()
        if self is ProductCategory.MUSIC_STORE_INSTRUMENTS_AND_SHEET_MUSIC:
            return music_store_instruments_and_sheet_music()
        if self is ProductCategory.NETWORKING:
            return networking()
        if self is ProductCategory.NEW_AGE:
            return new_age()
        if self is ProductCategory.NEW_PARTS_AND_SUPPLIES_MOTOR_VEHICLE:
            return new_parts_and_supplies_motor_vehicle()
        if self is ProductCategory.NEWS_DEALERS_AND_NEWSTANDS:
            return news_dealers_and_newstands()
        if self is ProductCategory.NON_DURABLE_GOODS:
            return non_durable_goods()
        if self is ProductCategory.NON_FICTION:
            return non_fiction()
        if self is ProductCategory.NON_PROFIT_POLITICAL_AND_RELIGION:
            return non_profit_political_and_religion()
        if self is ProductCategory.NONPROFIT:
            return nonprofit()
        if self is ProductCategory.NOVELTIES:
            return novelties()
        if self is ProductCategory.OEM_SOFTWARE:
            return oem_software()
        if self is ProductCategory.OFFICE_SUPPLIES_AND_EQUIPMENT:
            return office_supplies_and_equipment()
        if self is ProductCategory.ONLINE_DATING:
            return online_dating()
        if self is ProductCategory.ONLINE_GAMING:
            return online_gaming()
        if self is ProductCategory.ONLINE_GAMING_CURRENCY:
            return online_gaming_currency()
        if self is ProductCategory.ONLINE_SERVICES:
            return online_services()
        if self is ProductCategory.OOUTBOUND_TELEMARKETING_MERCH:
            return ooutbound_telemarketing_merch()
        if self is ProductCategory.OPHTHALMOLOGISTS_OPTOMETRIST:
            return ophthalmologists_optometrist()
        if self is ProductCategory.OPTICIANS_AND_DISPENSING:
            return opticians_and_dispensing()
        if self is ProductCategory.ORTHOPEDIC_GOODS_PROSTHETICS:
            return orthopedic_goods_prosthetics()
        if self is ProductCategory.OSTEOPATHS:
            return osteopaths()
        if self is ProductCategory.OTHER:
            return other()
        if self is ProductCategory.PACKAGE_TOUR_OPERATORS:
            return package_tour_operators()
        if self is ProductCategory.PAINTBALL:
            return paintball()
        if self is ProductCategory.PAINTS_VARNISHES_AND_SUPPLIES:
            return paints_varnishes_and_supplies()
        if self is ProductCategory.PARKING_LOTS_AND_GARAGES:
            return parking_lots_and_garages()
        if self is ProductCategory.PARTS_AND_ACCESSORIES:
            return parts_and_accessories()
        if self is ProductCategory.PAWN_SHOPS:
            return pawn_shops()
        if self is ProductCategory.PAYCHECK_LENDER_OR_CASH_ADVANCE:
            return paycheck_lender_or_cash_advance()
        if self is ProductCategory.PERIPHERALS:
            return peripherals()
        if self is ProductCategory.PERSONALIZED_GIFTS:
            return personalized_gifts()
        if self is ProductCategory.PET_SHOPS_PET_FOOD_AND_SUPPLIES:
            return pet_shops_pet_food_and_supplies()
        if self is ProductCategory.PETROLEUM_AND_PETROLEUM_PRODUCTS:
            return petroleum_and_petroleum_products()
        if self is ProductCategory.PETS_AND_ANIMALS:
            return pets_and_animals()
        if self is ProductCategory.PHOTOFINISHING_LABORATORIES_PHOTO_DEVELOPING:
            return photofinishing_laboratories_photo_developing()
        if self is ProductCategory.PHOTOGRAPHIC_STUDIOS_PORTRAITS:
            return photographic_studios_portraits()
        if self is ProductCategory.PHOTOGRAPHY:
            return photography()
        if self is ProductCategory.PHYSICAL_GOOD:
            return physical_good()
        if self is ProductCategory.PICTURE_VIDEO_PRODUCTION:
            return picture_video_production()
        if self is ProductCategory.PIECE_GOODS_NOTIONS_AND_OTHER_DRY_GOODS:
            return piece_goods_notions_and_other_dry_goods()
        if self is ProductCategory.PLANTS_AND_SEEDS:
            return plants_and_seeds()
        if self is ProductCategory.PLUMBING_AND_HEATING_EQUIPMENTS_AND_SUPPLIES:
            return plumbing_and_heating_equipments_and_supplies()
        if self is ProductCategory.POLICE_RELATED_ITEMS:
            return police_related_items()
        if self is ProductCategory.POLITICAL_ORGANIZATIONS:
            return political_organizations()
        if self is ProductCategory.POSTAL_SERVICES_GOVERNMENT_ONLY:
            return postal_services_government_only()
        if self is ProductCategory.POSTERS:
            return posters()
        if self is ProductCategory.PREPAID_AND_STORED_VALUE_CARDS:
            return prepaid_and_stored_value_cards()
        if self is ProductCategory.PRESCRIPTION_DRUGS:
            return prescription_drugs()
        if self is ProductCategory.PROMOTIONAL_ITEMS:
            return promotional_items()
        if self is ProductCategory.PUBLIC_WAREHOUSING_AND_STORAGE:
            return public_warehousing_and_storage()
        if self is ProductCategory.PUBLISHING_AND_PRINTING:
            return publishing_and_printing()
        if self is ProductCategory.PUBLISHING_SERVICES:
            return publishing_services()
        if self is ProductCategory.RADAR_DECTORS:
            return radar_dectors()
        if self is ProductCategory.RADIO_TELEVISION_AND_STEREO_REPAIR:
            return radio_television_and_stereo_repair()
        if self is ProductCategory.REAL_ESTATE:
            return real_estate()
        if self is ProductCategory.REAL_ESTATE_AGENT:
            return real_estate_agent()
        if self is ProductCategory.REAL_ESTATE_AGENTS_AND_MANAGERS_RENTALS:
            return real_estate_agents_and_managers_rentals()
        if self is ProductCategory.RELIGION_AND_SPIRITUALITY_FOR_PROFIT:
            return religion_and_spirituality_for_profit()
        if self is ProductCategory.RELIGIOUS:
            return religious()
        if self is ProductCategory.RELIGIOUS_ORGANIZATIONS:
            return religious_organizations()
        if self is ProductCategory.REMITTANCE:
            return remittance()
        if self is ProductCategory.RENTAL_PROPERTY_MANAGEMENT:
            return rental_property_management()
        if self is ProductCategory.RESIDENTIAL:
            return residential()
        if self is ProductCategory.RETAIL:
            return retail()
        if self is ProductCategory.RETAIL_FINE_JEWELRY_AND_WATCHES:
            return retail_fine_jewelry_and_watches()
        if self is ProductCategory.REUPHOLSTERY_AND_FURNITURE_REPAIR:
            return reupholstery_and_furniture_repair()
        if self is ProductCategory.RINGS:
            return rings()
        if self is ProductCategory.ROOFING_SIDING_SHEET_METAL:
            return roofing_siding_sheet_metal()
        if self is ProductCategory.RUGS_AND_CARPETS:
            return rugs_and_carpets()
        if self is ProductCategory.SCHOOLS_AND_COLLEGES:
            return schools_and_colleges()
        if self is ProductCategory.SCIENCE_FICTION:
            return science_fiction()
        if self is ProductCategory.SCRAPBOOKING:
            return scrapbooking()
        if self is ProductCategory.SCULPTURES:
            return sculptures()
        if self is ProductCategory.SECURITIES_BROKERS_AND_DEALERS:
            return securities_brokers_and_dealers()
        if self is ProductCategory.SECURITY_AND_SURVEILLANCE:
            return security_and_surveillance()
        if self is ProductCategory.SECURITY_AND_SURVEILLANCE_EQUIPMENT:
            return security_and_surveillance_equipment()
        if self is ProductCategory.SECURITY_BROKERS_AND_DEALERS:
            return security_brokers_and_dealers()
        if self is ProductCategory.SEMINARS:
            return seminars()
        if self is ProductCategory.SERVICE_STATIONS:
            return service_stations()
        if self is ProductCategory.SERVICES:
            return services()
        if self is ProductCategory.SEWING_NEEDLEWORK_FABRIC_AND_PIECE_GOODS_STORES:
            return sewing_needlework_fabric_and_piece_goods_stores()
        if self is ProductCategory.SHIPPING_AND_PACKING:
            return shipping_and_packing()
        if self is ProductCategory.SHOE_REPAIR_HAT_CLEANING:
            return shoe_repair_hat_cleaning()
        if self is ProductCategory.SHOE_STORES:
            return shoe_stores()
        if self is ProductCategory.SHOES:
            return shoes()
        if self is ProductCategory.SNOWMOBILE_DEALERS:
            return snowmobile_dealers()
        if self is ProductCategory.SOFTWARE:
            return software()
        if self is ProductCategory.SPECIALTY_AND_MISC_FOOD_STORES:
            return specialty_and_misc_food_stores()
        if self is ProductCategory.SPECIALTY_CLEANING_POLISHING_AND_SANITATION_PREPARATIONS:
            return specialty_cleaning_polishing_and_sanitation_preparations()
        if self is ProductCategory.SPECIALTY_OR_RARE_PETS:
            return specialty_or_rare_pets()
        if self is ProductCategory.SPORT_GAMES_AND_TOYS:
            return sport_games_and_toys()
        if self is ProductCategory.SPORTING_AND_RECREATIONAL_CAMPS:
            return sporting_and_recreational_camps()
        if self is ProductCategory.SPORTING_GOODS:
            return sporting_goods()
        if self is ProductCategory.SPORTS_AND_OUTDOORS:
            return sports_and_outdoors()
        if self is ProductCategory.SPORTS_AND_RECREATION:
            return sports_and_recreation()
        if self is ProductCategory.STAMP_AND_COIN:
            return stamp_and_coin()
        if self is ProductCategory.STATIONARY_PRINTING_AND_WRITING_PAPER:
            return stationary_printing_and_writing_paper()
        if self is ProductCategory.STENOGRAPHIC_AND_SECRETARIAL_SUPPORT_SERVICES:
            return stenographic_and_secretarial_support_services()
        if self is ProductCategory.STOCKS_BONDS_SECURITIES_AND_RELATED_CERTIFICATES:
            return stocks_bonds_securities_and_related_certificates()
        if self is ProductCategory.STORED_VALUE_CARDS:
            return stored_value_cards()
        if self is ProductCategory.SUPPLIES:
            return supplies()
        if self is ProductCategory.SUPPLIES_AND_TOYS:
            return supplies_and_toys()
        if self is ProductCategory.SURVEILLANCE_EQUIPMENT:
            return surveillance_equipment()
        if self is ProductCategory.SWIMMING_POOLS_AND_SPAS:
            return swimming_pools_and_spas()
        if self is ProductCategory.SWIMMING_POOLS_SALES_SUPPLIES_SERVICES:
            return swimming_pools_sales_supplies_services()
        if self is ProductCategory.TAILORS_AND_ALTERATIONS:
            return tailors_and_alterations()
        if self is ProductCategory.TAX_PAYMENTS:
            return tax_payments()
        if self is ProductCategory.TAX_PAYMENTS_GOVERNMENT_AGENCIES:
            return tax_payments_government_agencies()
        if self is ProductCategory.TAXICABS_AND_LIMOUSINES:
            return taxicabs_and_limousines()
        if self is ProductCategory.TELECOMMUNICATION_SERVICES:
            return telecommunication_services()
        if self is ProductCategory.TELEPHONE_CARDS:
            return telephone_cards()
        if self is ProductCategory.TELEPHONE_EQUIPMENT:
            return telephone_equipment()
        if self is ProductCategory.TELEPHONE_SERVICES:
            return telephone_services()
        if self is ProductCategory.THEATER:
            return theater()
        if self is ProductCategory.TIRE_RETREADING_AND_REPAIR:
            return tire_retreading_and_repair()
        if self is ProductCategory.TOLL_OR_BRIDGE_FEES:
            return toll_or_bridge_fees()
        if self is ProductCategory.TOOLS_AND_EQUIPMENT:
            return tools_and_equipment()
        if self is ProductCategory.TOURIST_ATTRACTIONS_AND_EXHIBITS:
            return tourist_attractions_and_exhibits()
        if self is ProductCategory.TOWING_SERVICE:
            return towing_service()
        if self is ProductCategory.TOYS_AND_GAMES:
            return toys_and_games()
        if self is ProductCategory.TRADE_AND_VOCATIONAL_SCHOOLS:
            return trade_and_vocational_schools()
        if self is ProductCategory.TRADEMARK_INFRINGEMENT:
            return trademark_infringement()
        if self is ProductCategory.TRAILER_PARKS_AND_CAMPGROUNDS:
            return trailer_parks_and_campgrounds()
        if self is ProductCategory.TRAINING_SERVICES:
            return training_services()
        if self is ProductCategory.TRANSPORTATION_SERVICES:
            return transportation_services()
        if self is ProductCategory.TRAVEL:
            return travel()
        if self is ProductCategory.TRUCK_AND_UTILITY_TRAILER_RENTALS:
            return truck_and_utility_trailer_rentals()
        if self is ProductCategory.TRUCK_STOP:
            return truck_stop()
        if self is ProductCategory.TYPESETTING_PLATE_MAKING_AND_RELATED_SERVICES:
            return typesetting_plate_making_and_related_services()
        if self is ProductCategory.USED_MERCHANDISE_AND_SECONDHAND_STORES:
            return used_merchandise_and_secondhand_stores()
        if self is ProductCategory.USED_PARTS_MOTOR_VEHICLE:
            return used_parts_motor_vehicle()
        if self is ProductCategory.UTILITIES:
            return utilities()
        if self is ProductCategory.UTILITIES_ELECTRIC_GAS_WATER_SANITARY:
            return utilities_electric_gas_water_sanitary()
        if self is ProductCategory.VARIETY_STORES:
            return variety_stores()
        if self is ProductCategory.VEHICLE_SALES:
            return vehicle_sales()
        if self is ProductCategory.VEHICLE_SERVICE_AND_ACCESSORIES:
            return vehicle_service_and_accessories()
        if self is ProductCategory.VIDEO_EQUIPMENT:
            return video_equipment()
        if self is ProductCategory.VIDEO_GAME_ARCADES_ESTABLISH:
            return video_game_arcades_establish()
        if self is ProductCategory.VIDEO_GAMES_AND_SYSTEMS:
            return video_games_and_systems()
        if self is ProductCategory.VIDEO_TAPE_RENTAL_STORES:
            return video_tape_rental_stores()
        if self is ProductCategory.VINTAGE_AND_COLLECTIBLE_VEHICLES:
            return vintage_and_collectible_vehicles()
        if self is ProductCategory.VINTAGE_AND_COLLECTIBLES:
            return vintage_and_collectibles()
        if self is ProductCategory.VITAMINS_AND_SUPPLEMENTS:
            return vitamins_and_supplements()
        if self is ProductCategory.VOCATIONAL_AND_TRADE_SCHOOLS:
            return vocational_and_trade_schools()
        if self is ProductCategory.WATCH_CLOCK_AND_JEWELRY_REPAIR:
            return watch_clock_and_jewelry_repair()
        if self is ProductCategory.WEB_HOSTING_AND_DESIGN:
            return web_hosting_and_design()
        if self is ProductCategory.WELDING_REPAIR:
            return welding_repair()
        if self is ProductCategory.WHOLESALE_CLUBS:
            return wholesale_clubs()
        if self is ProductCategory.WHOLESALE_FLORIST_SUPPLIERS:
            return wholesale_florist_suppliers()
        if self is ProductCategory.WHOLESALE_PRESCRIPTION_DRUGS:
            return wholesale_prescription_drugs()
        if self is ProductCategory.WILDLIFE_PRODUCTS:
            return wildlife_products()
        if self is ProductCategory.WIRE_TRANSFER:
            return wire_transfer()
        if self is ProductCategory.WIRE_TRANSFER_AND_MONEY_ORDER:
            return wire_transfer_and_money_order()
        if self is ProductCategory.WOMEN_ACCESSORY_SPECIALITY:
            return women_accessory_speciality()
        if self is ProductCategory.WOMEN_CLOTHING:
            return women_clothing()
