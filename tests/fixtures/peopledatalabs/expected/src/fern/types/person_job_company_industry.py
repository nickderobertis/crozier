

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersonJobCompanyIndustry(enum.StrEnum):
    """
    A person's current company's industry
    """

    ACCOUNTING = "accounting"
    AIRLINES_AVIATION = "airlines/aviation"
    ALTERNATIVE_DISPUTE_RESOLUTION = "alternative dispute resolution"
    ALTERNATIVE_MEDICINE = "alternative medicine"
    ANIMATION = "animation"
    APPAREL_FASHION = "apparel & fashion"
    ARCHITECTURE_PLANNING = "architecture & planning"
    ARTS_AND_CRAFTS = "arts and crafts"
    AUTOMOTIVE = "automotive"
    AVIATION_AEROSPACE = "aviation & aerospace"
    BANKING = "banking"
    BIOTECHNOLOGY = "biotechnology"
    BROADCAST_MEDIA = "broadcast media"
    BUILDING_MATERIALS = "building materials"
    BUSINESS_SUPPLIES_AND_EQUIPMENT = "business supplies and equipment"
    CAPITAL_MARKETS = "capital markets"
    CHEMICALS = "chemicals"
    CIVIC_SOCIAL_ORGANIZATION = "civic & social organization"
    CIVIL_ENGINEERING = "civil engineering"
    COMMERCIAL_REAL_ESTATE = "commercial real estate"
    COMPUTER_NETWORK_SECURITY = "computer & network security"
    COMPUTER_GAMES = "computer games"
    COMPUTER_HARDWARE = "computer hardware"
    COMPUTER_NETWORKING = "computer networking"
    COMPUTER_SOFTWARE = "computer software"
    CONSTRUCTION = "construction"
    CONSUMER_ELECTRONICS = "consumer electronics"
    CONSUMER_GOODS = "consumer goods"
    CONSUMER_SERVICES = "consumer services"
    COSMETICS = "cosmetics"
    DAIRY = "dairy"
    DEFENSE_SPACE = "defense & space"
    DESIGN = "design"
    E_LEARNING = "e-learning"
    EDUCATION_MANAGEMENT = "education management"
    ELECTRICAL_ELECTRONIC_MANUFACTURING = "electrical/electronic manufacturing"
    ENTERTAINMENT = "entertainment"
    ENVIRONMENTAL_SERVICES = "environmental services"
    EVENTS_SERVICES = "events services"
    EXECUTIVE_OFFICE = "executive office"
    FACILITIES_SERVICES = "facilities services"
    FARMING = "farming"
    FINANCIAL_SERVICES = "financial services"
    FINE_ART = "fine art"
    FISHERY = "fishery"
    FOOD_BEVERAGES = "food & beverages"
    FOOD_PRODUCTION = "food production"
    FUND_RAISING = "fund-raising"
    FURNITURE = "furniture"
    GAMBLING_CASINOS = "gambling & casinos"
    GLASS_CERAMICS_CONCRETE = "glass, ceramics, & concrete"
    GOVERNMENT_ADMINISTRATION = "government administration"
    GOVERNMENT_RELATIONS = "government relations"
    GRAPHIC_DESIGN = "graphic design"
    HEALTH_WELLNESS_AND_FITNESS = "health, wellness and fitness"
    HIGHER_EDUCATION = "higher education"
    HOSPITAL_HEALTH_CARE = "hospital & health care"
    HOSPITALITY = "hospitality"
    HUMAN_RESOURCES = "human resources"
    IMPORT_AND_EXPORT = "import and export"
    INDIVIDUAL_FAMILY_SERVICES = "individual & family services"
    INDUSTRIAL_AUTOMATION = "industrial automation"
    INFORMATION_SERVICES = "information services"
    INFORMATION_TECHNOLOGY_AND_SERVICES = "information technology and services"
    INSURANCE = "insurance"
    INTERNATIONAL_AFFAIRS = "international affairs"
    INTERNATIONAL_TRADE_AND_DEVELOPMENT = "international trade and development"
    INTERNET = "internet"
    INVESTMENT_BANKING = "investment banking"
    INVESTMENT_MANAGEMENT = "investment management"
    JUDICIARY = "judiciary"
    LAW_ENFORCEMENT = "law enforcement"
    LAW_PRACTICE = "law practice"
    LEGAL_SERVICES = "legal services"
    LEGISLATIVE_OFFICE = "legislative office"
    LEISURE_TRAVEL_TOURISM = "leisure, travel, & tourism"
    LIBRARIES = "libraries"
    LOGISTICS_AND_SUPPLY_CHAIN = "logistics and supply chain"
    LUXURY_GOODS_JEWELRY = "luxury goods & jewelry"
    MACHINERY = "machinery"
    MANAGEMENT_CONSULTING = "management consulting"
    MARITIME = "maritime"
    MARKET_RESEARCH = "market research"
    MARKETING_AND_ADVERTISING = "marketing and advertising"
    MECHANICAL_OR_INDUSTRIAL_ENGINEERING = "mechanical or industrial engineering"
    MEDIA_PRODUCTION = "media production"
    MEDICAL_DEVICES = "medical devices"
    MEDICAL_PRACTICE = "medical practice"
    MENTAL_HEALTH_CARE = "mental health care"
    MILITARY = "military"
    MINING_METALS = "mining & metals"
    MOTION_PICTURES_AND_FILM = "motion pictures and film"
    MUSEUMS_AND_INSTITUTIONS = "museums and institutions"
    MUSIC = "music"
    NANOTECHNOLOGY = "nanotechnology"
    NEWSPAPERS = "newspapers"
    NON_PROFIT_ORGANIZATION_MANAGEMENT = "non-profit organization management"
    OIL_ENERGY = "oil & energy"
    ONLINE_MEDIA = "online media"
    OUTSOURCING_OFFSHORING = "outsourcing/offshoring"
    PACKAGE_FREIGHT_DELIVERY = "package/freight delivery"
    PACKAGING_AND_CONTAINERS = "packaging and containers"
    PAPER_FOREST_PRODUCTS = "paper & forest products"
    PERFORMING_ARTS = "performing arts"
    PHARMACEUTICALS = "pharmaceuticals"
    PHILANTHROPY = "philanthropy"
    PHOTOGRAPHY = "photography"
    PLASTICS = "plastics"
    POLITICAL_ORGANIZATION = "political organization"
    PRIMARY_SECONDARY_EDUCATION = "primary/secondary education"
    PRINTING = "printing"
    PROFESSIONAL_TRAINING_COACHING = "professional training & coaching"
    PROGRAM_DEVELOPMENT = "program development"
    PUBLIC_POLICY = "public policy"
    PUBLIC_RELATIONS_AND_COMMUNICATIONS = "public relations and communications"
    PUBLIC_SAFETY = "public safety"
    PUBLISHING = "publishing"
    RAILROAD_MANUFACTURE = "railroad manufacture"
    RANCHING = "ranching"
    REAL_ESTATE = "real estate"
    RECREATIONAL_FACILITIES_AND_SERVICES = "recreational facilities and services"
    RELIGIOUS_INSTITUTIONS = "religious institutions"
    RENEWABLES_ENVIRONMENT = "renewables & environment"
    RESEARCH = "research"
    RESTAURANTS = "restaurants"
    RETAIL = "retail"
    SECURITY_AND_INVESTIGATIONS = "security and investigations"
    SEMICONDUCTORS = "semiconductors"
    SHIPBUILDING = "shipbuilding"
    SPORTING_GOODS = "sporting goods"
    SPORTS = "sports"
    STAFFING_AND_RECRUITING = "staffing and recruiting"
    SUPERMARKETS = "supermarkets"
    TELECOMMUNICATIONS = "telecommunications"
    TEXTILES = "textiles"
    THINK_TANKS = "think tanks"
    TOBACCO = "tobacco"
    TRANSLATION_AND_LOCALIZATION = "translation and localization"
    TRANSPORTATION_TRUCKING_RAILROAD = "transportation/trucking/railroad"
    UTILITIES = "utilities"
    VENTURE_CAPITAL_PRIVATE_EQUITY = "venture capital & private equity"
    VETERINARY = "veterinary"
    WAREHOUSING = "warehousing"
    WHOLESALE = "wholesale"
    WINE_AND_SPIRITS = "wine and spirits"
    WIRELESS = "wireless"
    WRITING_AND_EDITING = "writing and editing"

    def visit(
        self,
        accounting: typing.Callable[[], T_Result],
        airlines_aviation: typing.Callable[[], T_Result],
        alternative_dispute_resolution: typing.Callable[[], T_Result],
        alternative_medicine: typing.Callable[[], T_Result],
        animation: typing.Callable[[], T_Result],
        apparel_fashion: typing.Callable[[], T_Result],
        architecture_planning: typing.Callable[[], T_Result],
        arts_and_crafts: typing.Callable[[], T_Result],
        automotive: typing.Callable[[], T_Result],
        aviation_aerospace: typing.Callable[[], T_Result],
        banking: typing.Callable[[], T_Result],
        biotechnology: typing.Callable[[], T_Result],
        broadcast_media: typing.Callable[[], T_Result],
        building_materials: typing.Callable[[], T_Result],
        business_supplies_and_equipment: typing.Callable[[], T_Result],
        capital_markets: typing.Callable[[], T_Result],
        chemicals: typing.Callable[[], T_Result],
        civic_social_organization: typing.Callable[[], T_Result],
        civil_engineering: typing.Callable[[], T_Result],
        commercial_real_estate: typing.Callable[[], T_Result],
        computer_network_security: typing.Callable[[], T_Result],
        computer_games: typing.Callable[[], T_Result],
        computer_hardware: typing.Callable[[], T_Result],
        computer_networking: typing.Callable[[], T_Result],
        computer_software: typing.Callable[[], T_Result],
        construction: typing.Callable[[], T_Result],
        consumer_electronics: typing.Callable[[], T_Result],
        consumer_goods: typing.Callable[[], T_Result],
        consumer_services: typing.Callable[[], T_Result],
        cosmetics: typing.Callable[[], T_Result],
        dairy: typing.Callable[[], T_Result],
        defense_space: typing.Callable[[], T_Result],
        design: typing.Callable[[], T_Result],
        e_learning: typing.Callable[[], T_Result],
        education_management: typing.Callable[[], T_Result],
        electrical_electronic_manufacturing: typing.Callable[[], T_Result],
        entertainment: typing.Callable[[], T_Result],
        environmental_services: typing.Callable[[], T_Result],
        events_services: typing.Callable[[], T_Result],
        executive_office: typing.Callable[[], T_Result],
        facilities_services: typing.Callable[[], T_Result],
        farming: typing.Callable[[], T_Result],
        financial_services: typing.Callable[[], T_Result],
        fine_art: typing.Callable[[], T_Result],
        fishery: typing.Callable[[], T_Result],
        food_beverages: typing.Callable[[], T_Result],
        food_production: typing.Callable[[], T_Result],
        fund_raising: typing.Callable[[], T_Result],
        furniture: typing.Callable[[], T_Result],
        gambling_casinos: typing.Callable[[], T_Result],
        glass_ceramics_concrete: typing.Callable[[], T_Result],
        government_administration: typing.Callable[[], T_Result],
        government_relations: typing.Callable[[], T_Result],
        graphic_design: typing.Callable[[], T_Result],
        health_wellness_and_fitness: typing.Callable[[], T_Result],
        higher_education: typing.Callable[[], T_Result],
        hospital_health_care: typing.Callable[[], T_Result],
        hospitality: typing.Callable[[], T_Result],
        human_resources: typing.Callable[[], T_Result],
        import_and_export: typing.Callable[[], T_Result],
        individual_family_services: typing.Callable[[], T_Result],
        industrial_automation: typing.Callable[[], T_Result],
        information_services: typing.Callable[[], T_Result],
        information_technology_and_services: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        international_affairs: typing.Callable[[], T_Result],
        international_trade_and_development: typing.Callable[[], T_Result],
        internet: typing.Callable[[], T_Result],
        investment_banking: typing.Callable[[], T_Result],
        investment_management: typing.Callable[[], T_Result],
        judiciary: typing.Callable[[], T_Result],
        law_enforcement: typing.Callable[[], T_Result],
        law_practice: typing.Callable[[], T_Result],
        legal_services: typing.Callable[[], T_Result],
        legislative_office: typing.Callable[[], T_Result],
        leisure_travel_tourism: typing.Callable[[], T_Result],
        libraries: typing.Callable[[], T_Result],
        logistics_and_supply_chain: typing.Callable[[], T_Result],
        luxury_goods_jewelry: typing.Callable[[], T_Result],
        machinery: typing.Callable[[], T_Result],
        management_consulting: typing.Callable[[], T_Result],
        maritime: typing.Callable[[], T_Result],
        market_research: typing.Callable[[], T_Result],
        marketing_and_advertising: typing.Callable[[], T_Result],
        mechanical_or_industrial_engineering: typing.Callable[[], T_Result],
        media_production: typing.Callable[[], T_Result],
        medical_devices: typing.Callable[[], T_Result],
        medical_practice: typing.Callable[[], T_Result],
        mental_health_care: typing.Callable[[], T_Result],
        military: typing.Callable[[], T_Result],
        mining_metals: typing.Callable[[], T_Result],
        motion_pictures_and_film: typing.Callable[[], T_Result],
        museums_and_institutions: typing.Callable[[], T_Result],
        music: typing.Callable[[], T_Result],
        nanotechnology: typing.Callable[[], T_Result],
        newspapers: typing.Callable[[], T_Result],
        non_profit_organization_management: typing.Callable[[], T_Result],
        oil_energy: typing.Callable[[], T_Result],
        online_media: typing.Callable[[], T_Result],
        outsourcing_offshoring: typing.Callable[[], T_Result],
        package_freight_delivery: typing.Callable[[], T_Result],
        packaging_and_containers: typing.Callable[[], T_Result],
        paper_forest_products: typing.Callable[[], T_Result],
        performing_arts: typing.Callable[[], T_Result],
        pharmaceuticals: typing.Callable[[], T_Result],
        philanthropy: typing.Callable[[], T_Result],
        photography: typing.Callable[[], T_Result],
        plastics: typing.Callable[[], T_Result],
        political_organization: typing.Callable[[], T_Result],
        primary_secondary_education: typing.Callable[[], T_Result],
        printing: typing.Callable[[], T_Result],
        professional_training_coaching: typing.Callable[[], T_Result],
        program_development: typing.Callable[[], T_Result],
        public_policy: typing.Callable[[], T_Result],
        public_relations_and_communications: typing.Callable[[], T_Result],
        public_safety: typing.Callable[[], T_Result],
        publishing: typing.Callable[[], T_Result],
        railroad_manufacture: typing.Callable[[], T_Result],
        ranching: typing.Callable[[], T_Result],
        real_estate: typing.Callable[[], T_Result],
        recreational_facilities_and_services: typing.Callable[[], T_Result],
        religious_institutions: typing.Callable[[], T_Result],
        renewables_environment: typing.Callable[[], T_Result],
        research: typing.Callable[[], T_Result],
        restaurants: typing.Callable[[], T_Result],
        retail: typing.Callable[[], T_Result],
        security_and_investigations: typing.Callable[[], T_Result],
        semiconductors: typing.Callable[[], T_Result],
        shipbuilding: typing.Callable[[], T_Result],
        sporting_goods: typing.Callable[[], T_Result],
        sports: typing.Callable[[], T_Result],
        staffing_and_recruiting: typing.Callable[[], T_Result],
        supermarkets: typing.Callable[[], T_Result],
        telecommunications: typing.Callable[[], T_Result],
        textiles: typing.Callable[[], T_Result],
        think_tanks: typing.Callable[[], T_Result],
        tobacco: typing.Callable[[], T_Result],
        translation_and_localization: typing.Callable[[], T_Result],
        transportation_trucking_railroad: typing.Callable[[], T_Result],
        utilities: typing.Callable[[], T_Result],
        venture_capital_private_equity: typing.Callable[[], T_Result],
        veterinary: typing.Callable[[], T_Result],
        warehousing: typing.Callable[[], T_Result],
        wholesale: typing.Callable[[], T_Result],
        wine_and_spirits: typing.Callable[[], T_Result],
        wireless: typing.Callable[[], T_Result],
        writing_and_editing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PersonJobCompanyIndustry.ACCOUNTING:
            return accounting()
        if self is PersonJobCompanyIndustry.AIRLINES_AVIATION:
            return airlines_aviation()
        if self is PersonJobCompanyIndustry.ALTERNATIVE_DISPUTE_RESOLUTION:
            return alternative_dispute_resolution()
        if self is PersonJobCompanyIndustry.ALTERNATIVE_MEDICINE:
            return alternative_medicine()
        if self is PersonJobCompanyIndustry.ANIMATION:
            return animation()
        if self is PersonJobCompanyIndustry.APPAREL_FASHION:
            return apparel_fashion()
        if self is PersonJobCompanyIndustry.ARCHITECTURE_PLANNING:
            return architecture_planning()
        if self is PersonJobCompanyIndustry.ARTS_AND_CRAFTS:
            return arts_and_crafts()
        if self is PersonJobCompanyIndustry.AUTOMOTIVE:
            return automotive()
        if self is PersonJobCompanyIndustry.AVIATION_AEROSPACE:
            return aviation_aerospace()
        if self is PersonJobCompanyIndustry.BANKING:
            return banking()
        if self is PersonJobCompanyIndustry.BIOTECHNOLOGY:
            return biotechnology()
        if self is PersonJobCompanyIndustry.BROADCAST_MEDIA:
            return broadcast_media()
        if self is PersonJobCompanyIndustry.BUILDING_MATERIALS:
            return building_materials()
        if self is PersonJobCompanyIndustry.BUSINESS_SUPPLIES_AND_EQUIPMENT:
            return business_supplies_and_equipment()
        if self is PersonJobCompanyIndustry.CAPITAL_MARKETS:
            return capital_markets()
        if self is PersonJobCompanyIndustry.CHEMICALS:
            return chemicals()
        if self is PersonJobCompanyIndustry.CIVIC_SOCIAL_ORGANIZATION:
            return civic_social_organization()
        if self is PersonJobCompanyIndustry.CIVIL_ENGINEERING:
            return civil_engineering()
        if self is PersonJobCompanyIndustry.COMMERCIAL_REAL_ESTATE:
            return commercial_real_estate()
        if self is PersonJobCompanyIndustry.COMPUTER_NETWORK_SECURITY:
            return computer_network_security()
        if self is PersonJobCompanyIndustry.COMPUTER_GAMES:
            return computer_games()
        if self is PersonJobCompanyIndustry.COMPUTER_HARDWARE:
            return computer_hardware()
        if self is PersonJobCompanyIndustry.COMPUTER_NETWORKING:
            return computer_networking()
        if self is PersonJobCompanyIndustry.COMPUTER_SOFTWARE:
            return computer_software()
        if self is PersonJobCompanyIndustry.CONSTRUCTION:
            return construction()
        if self is PersonJobCompanyIndustry.CONSUMER_ELECTRONICS:
            return consumer_electronics()
        if self is PersonJobCompanyIndustry.CONSUMER_GOODS:
            return consumer_goods()
        if self is PersonJobCompanyIndustry.CONSUMER_SERVICES:
            return consumer_services()
        if self is PersonJobCompanyIndustry.COSMETICS:
            return cosmetics()
        if self is PersonJobCompanyIndustry.DAIRY:
            return dairy()
        if self is PersonJobCompanyIndustry.DEFENSE_SPACE:
            return defense_space()
        if self is PersonJobCompanyIndustry.DESIGN:
            return design()
        if self is PersonJobCompanyIndustry.E_LEARNING:
            return e_learning()
        if self is PersonJobCompanyIndustry.EDUCATION_MANAGEMENT:
            return education_management()
        if self is PersonJobCompanyIndustry.ELECTRICAL_ELECTRONIC_MANUFACTURING:
            return electrical_electronic_manufacturing()
        if self is PersonJobCompanyIndustry.ENTERTAINMENT:
            return entertainment()
        if self is PersonJobCompanyIndustry.ENVIRONMENTAL_SERVICES:
            return environmental_services()
        if self is PersonJobCompanyIndustry.EVENTS_SERVICES:
            return events_services()
        if self is PersonJobCompanyIndustry.EXECUTIVE_OFFICE:
            return executive_office()
        if self is PersonJobCompanyIndustry.FACILITIES_SERVICES:
            return facilities_services()
        if self is PersonJobCompanyIndustry.FARMING:
            return farming()
        if self is PersonJobCompanyIndustry.FINANCIAL_SERVICES:
            return financial_services()
        if self is PersonJobCompanyIndustry.FINE_ART:
            return fine_art()
        if self is PersonJobCompanyIndustry.FISHERY:
            return fishery()
        if self is PersonJobCompanyIndustry.FOOD_BEVERAGES:
            return food_beverages()
        if self is PersonJobCompanyIndustry.FOOD_PRODUCTION:
            return food_production()
        if self is PersonJobCompanyIndustry.FUND_RAISING:
            return fund_raising()
        if self is PersonJobCompanyIndustry.FURNITURE:
            return furniture()
        if self is PersonJobCompanyIndustry.GAMBLING_CASINOS:
            return gambling_casinos()
        if self is PersonJobCompanyIndustry.GLASS_CERAMICS_CONCRETE:
            return glass_ceramics_concrete()
        if self is PersonJobCompanyIndustry.GOVERNMENT_ADMINISTRATION:
            return government_administration()
        if self is PersonJobCompanyIndustry.GOVERNMENT_RELATIONS:
            return government_relations()
        if self is PersonJobCompanyIndustry.GRAPHIC_DESIGN:
            return graphic_design()
        if self is PersonJobCompanyIndustry.HEALTH_WELLNESS_AND_FITNESS:
            return health_wellness_and_fitness()
        if self is PersonJobCompanyIndustry.HIGHER_EDUCATION:
            return higher_education()
        if self is PersonJobCompanyIndustry.HOSPITAL_HEALTH_CARE:
            return hospital_health_care()
        if self is PersonJobCompanyIndustry.HOSPITALITY:
            return hospitality()
        if self is PersonJobCompanyIndustry.HUMAN_RESOURCES:
            return human_resources()
        if self is PersonJobCompanyIndustry.IMPORT_AND_EXPORT:
            return import_and_export()
        if self is PersonJobCompanyIndustry.INDIVIDUAL_FAMILY_SERVICES:
            return individual_family_services()
        if self is PersonJobCompanyIndustry.INDUSTRIAL_AUTOMATION:
            return industrial_automation()
        if self is PersonJobCompanyIndustry.INFORMATION_SERVICES:
            return information_services()
        if self is PersonJobCompanyIndustry.INFORMATION_TECHNOLOGY_AND_SERVICES:
            return information_technology_and_services()
        if self is PersonJobCompanyIndustry.INSURANCE:
            return insurance()
        if self is PersonJobCompanyIndustry.INTERNATIONAL_AFFAIRS:
            return international_affairs()
        if self is PersonJobCompanyIndustry.INTERNATIONAL_TRADE_AND_DEVELOPMENT:
            return international_trade_and_development()
        if self is PersonJobCompanyIndustry.INTERNET:
            return internet()
        if self is PersonJobCompanyIndustry.INVESTMENT_BANKING:
            return investment_banking()
        if self is PersonJobCompanyIndustry.INVESTMENT_MANAGEMENT:
            return investment_management()
        if self is PersonJobCompanyIndustry.JUDICIARY:
            return judiciary()
        if self is PersonJobCompanyIndustry.LAW_ENFORCEMENT:
            return law_enforcement()
        if self is PersonJobCompanyIndustry.LAW_PRACTICE:
            return law_practice()
        if self is PersonJobCompanyIndustry.LEGAL_SERVICES:
            return legal_services()
        if self is PersonJobCompanyIndustry.LEGISLATIVE_OFFICE:
            return legislative_office()
        if self is PersonJobCompanyIndustry.LEISURE_TRAVEL_TOURISM:
            return leisure_travel_tourism()
        if self is PersonJobCompanyIndustry.LIBRARIES:
            return libraries()
        if self is PersonJobCompanyIndustry.LOGISTICS_AND_SUPPLY_CHAIN:
            return logistics_and_supply_chain()
        if self is PersonJobCompanyIndustry.LUXURY_GOODS_JEWELRY:
            return luxury_goods_jewelry()
        if self is PersonJobCompanyIndustry.MACHINERY:
            return machinery()
        if self is PersonJobCompanyIndustry.MANAGEMENT_CONSULTING:
            return management_consulting()
        if self is PersonJobCompanyIndustry.MARITIME:
            return maritime()
        if self is PersonJobCompanyIndustry.MARKET_RESEARCH:
            return market_research()
        if self is PersonJobCompanyIndustry.MARKETING_AND_ADVERTISING:
            return marketing_and_advertising()
        if self is PersonJobCompanyIndustry.MECHANICAL_OR_INDUSTRIAL_ENGINEERING:
            return mechanical_or_industrial_engineering()
        if self is PersonJobCompanyIndustry.MEDIA_PRODUCTION:
            return media_production()
        if self is PersonJobCompanyIndustry.MEDICAL_DEVICES:
            return medical_devices()
        if self is PersonJobCompanyIndustry.MEDICAL_PRACTICE:
            return medical_practice()
        if self is PersonJobCompanyIndustry.MENTAL_HEALTH_CARE:
            return mental_health_care()
        if self is PersonJobCompanyIndustry.MILITARY:
            return military()
        if self is PersonJobCompanyIndustry.MINING_METALS:
            return mining_metals()
        if self is PersonJobCompanyIndustry.MOTION_PICTURES_AND_FILM:
            return motion_pictures_and_film()
        if self is PersonJobCompanyIndustry.MUSEUMS_AND_INSTITUTIONS:
            return museums_and_institutions()
        if self is PersonJobCompanyIndustry.MUSIC:
            return music()
        if self is PersonJobCompanyIndustry.NANOTECHNOLOGY:
            return nanotechnology()
        if self is PersonJobCompanyIndustry.NEWSPAPERS:
            return newspapers()
        if self is PersonJobCompanyIndustry.NON_PROFIT_ORGANIZATION_MANAGEMENT:
            return non_profit_organization_management()
        if self is PersonJobCompanyIndustry.OIL_ENERGY:
            return oil_energy()
        if self is PersonJobCompanyIndustry.ONLINE_MEDIA:
            return online_media()
        if self is PersonJobCompanyIndustry.OUTSOURCING_OFFSHORING:
            return outsourcing_offshoring()
        if self is PersonJobCompanyIndustry.PACKAGE_FREIGHT_DELIVERY:
            return package_freight_delivery()
        if self is PersonJobCompanyIndustry.PACKAGING_AND_CONTAINERS:
            return packaging_and_containers()
        if self is PersonJobCompanyIndustry.PAPER_FOREST_PRODUCTS:
            return paper_forest_products()
        if self is PersonJobCompanyIndustry.PERFORMING_ARTS:
            return performing_arts()
        if self is PersonJobCompanyIndustry.PHARMACEUTICALS:
            return pharmaceuticals()
        if self is PersonJobCompanyIndustry.PHILANTHROPY:
            return philanthropy()
        if self is PersonJobCompanyIndustry.PHOTOGRAPHY:
            return photography()
        if self is PersonJobCompanyIndustry.PLASTICS:
            return plastics()
        if self is PersonJobCompanyIndustry.POLITICAL_ORGANIZATION:
            return political_organization()
        if self is PersonJobCompanyIndustry.PRIMARY_SECONDARY_EDUCATION:
            return primary_secondary_education()
        if self is PersonJobCompanyIndustry.PRINTING:
            return printing()
        if self is PersonJobCompanyIndustry.PROFESSIONAL_TRAINING_COACHING:
            return professional_training_coaching()
        if self is PersonJobCompanyIndustry.PROGRAM_DEVELOPMENT:
            return program_development()
        if self is PersonJobCompanyIndustry.PUBLIC_POLICY:
            return public_policy()
        if self is PersonJobCompanyIndustry.PUBLIC_RELATIONS_AND_COMMUNICATIONS:
            return public_relations_and_communications()
        if self is PersonJobCompanyIndustry.PUBLIC_SAFETY:
            return public_safety()
        if self is PersonJobCompanyIndustry.PUBLISHING:
            return publishing()
        if self is PersonJobCompanyIndustry.RAILROAD_MANUFACTURE:
            return railroad_manufacture()
        if self is PersonJobCompanyIndustry.RANCHING:
            return ranching()
        if self is PersonJobCompanyIndustry.REAL_ESTATE:
            return real_estate()
        if self is PersonJobCompanyIndustry.RECREATIONAL_FACILITIES_AND_SERVICES:
            return recreational_facilities_and_services()
        if self is PersonJobCompanyIndustry.RELIGIOUS_INSTITUTIONS:
            return religious_institutions()
        if self is PersonJobCompanyIndustry.RENEWABLES_ENVIRONMENT:
            return renewables_environment()
        if self is PersonJobCompanyIndustry.RESEARCH:
            return research()
        if self is PersonJobCompanyIndustry.RESTAURANTS:
            return restaurants()
        if self is PersonJobCompanyIndustry.RETAIL:
            return retail()
        if self is PersonJobCompanyIndustry.SECURITY_AND_INVESTIGATIONS:
            return security_and_investigations()
        if self is PersonJobCompanyIndustry.SEMICONDUCTORS:
            return semiconductors()
        if self is PersonJobCompanyIndustry.SHIPBUILDING:
            return shipbuilding()
        if self is PersonJobCompanyIndustry.SPORTING_GOODS:
            return sporting_goods()
        if self is PersonJobCompanyIndustry.SPORTS:
            return sports()
        if self is PersonJobCompanyIndustry.STAFFING_AND_RECRUITING:
            return staffing_and_recruiting()
        if self is PersonJobCompanyIndustry.SUPERMARKETS:
            return supermarkets()
        if self is PersonJobCompanyIndustry.TELECOMMUNICATIONS:
            return telecommunications()
        if self is PersonJobCompanyIndustry.TEXTILES:
            return textiles()
        if self is PersonJobCompanyIndustry.THINK_TANKS:
            return think_tanks()
        if self is PersonJobCompanyIndustry.TOBACCO:
            return tobacco()
        if self is PersonJobCompanyIndustry.TRANSLATION_AND_LOCALIZATION:
            return translation_and_localization()
        if self is PersonJobCompanyIndustry.TRANSPORTATION_TRUCKING_RAILROAD:
            return transportation_trucking_railroad()
        if self is PersonJobCompanyIndustry.UTILITIES:
            return utilities()
        if self is PersonJobCompanyIndustry.VENTURE_CAPITAL_PRIVATE_EQUITY:
            return venture_capital_private_equity()
        if self is PersonJobCompanyIndustry.VETERINARY:
            return veterinary()
        if self is PersonJobCompanyIndustry.WAREHOUSING:
            return warehousing()
        if self is PersonJobCompanyIndustry.WHOLESALE:
            return wholesale()
        if self is PersonJobCompanyIndustry.WINE_AND_SPIRITS:
            return wine_and_spirits()
        if self is PersonJobCompanyIndustry.WIRELESS:
            return wireless()
        if self is PersonJobCompanyIndustry.WRITING_AND_EDITING:
            return writing_and_editing()
