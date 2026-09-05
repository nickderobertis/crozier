

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchUsersRequestIndustry(enum.StrEnum):
    ACCOUNTING = "Accounting"
    AIRLINES_AVIATION = "Airlines/Aviation"
    ALTERNATIVE_DISPUTE_RESOLUTION = "Alternative Dispute Resolution"
    ALTERNATIVE_MEDICINE = "Alternative Medicine"
    ANIMATION = "Animation"
    APPAREL_FASHION = "Apparel & Fashion"
    ARCHITECTURE_PLANNING = "Architecture & Planning"
    ARTS_AND_CRAFTS = "Arts and Crafts"
    AUTOMOTIVE = "Automotive"
    AVIATION_AEROSPACE = "Aviation & Aerospace"
    BANKING = "Banking"
    BIOTECHNOLOGY = "Biotechnology"
    BROADCAST_MEDIA = "Broadcast Media"
    BUILDING_MATERIALS = "Building Materials"
    BUSINESS_SUPPLIES_AND_EQUIPMENT = "Business Supplies and Equipment"
    CAPITAL_MARKETS = "Capital Markets"
    CHEMICALS = "Chemicals"
    CIVIC_SOCIAL_ORGANIZATION = "Civic & Social Organization"
    CIVIL_ENGINEERING = "Civil Engineering"
    COMMERCIAL_REAL_ESTATE = "Commercial Real Estate"
    COMPUTER_NETWORK_SECURITY = "Computer & Network Security"
    COMPUTER_GAMES = "Computer Games"
    COMPUTER_HARDWARE = "Computer Hardware"
    COMPUTER_NETWORKING = "Computer Networking"
    COMPUTER_SOFTWARE = "Computer Software"
    CONSTRUCTION = "Construction"
    CONSUMER_ELECTRONICS = "Consumer Electronics"
    CONSUMER_GOODS = "Consumer Goods"
    CONSUMER_SERVICES = "Consumer Services"
    COSMETICS = "Cosmetics"
    DAIRY = "Dairy"
    DEFENSE_SPACE = "Defense & Space"
    DESIGN = "Design"
    E_LEARNING = "E-Learning"
    EDUCATION_MANAGEMENT = "Education Management"
    ELECTRICAL_ELECTRONIC_MANUFACTURING = "Electrical/Electronic Manufacturing"
    ENTERTAINMENT = "Entertainment"
    ENVIRONMENTAL_SERVICES = "Environmental Services"
    EVENTS_SERVICES = "Events Services"
    EXECUTIVE_OFFICE = "Executive Office"
    FACILITIES_SERVICES = "Facilities Services"
    FARMING = "Farming"
    FINANCIAL_SERVICES = "Financial Services"
    FINE_ART = "Fine Art"
    FISHERY = "Fishery"
    FOOD_BEVERAGES = "Food & Beverages"
    FOOD_PRODUCTION = "Food Production"
    FUND_RAISING = "Fund-Raising"
    FURNITURE = "Furniture"
    GAMBLING_CASINOS = "Gambling & Casinos"
    GLASS_CERAMICS_CONCRETE = "Glass, Ceramics & Concrete"
    GOVERNMENT_ADMINISTRATION = "Government Administration"
    GOVERNMENT_RELATIONS = "Government Relations"
    GRAPHIC_DESIGN = "Graphic Design"
    HEALTH_WELLNESS_AND_FITNESS = "Health, Wellness and Fitness"
    HIGHER_EDUCATION = "Higher Education"
    HOSPITAL_HEALTH_CARE = "Hospital & Health Care"
    HOSPITALITY = "Hospitality"
    HUMAN_RESOURCES = "Human Resources"
    IMPORT_AND_EXPORT = "Import and Export"
    INDIVIDUAL_FAMILY_SERVICES = "Individual & Family Services"
    INDUSTRIAL_AUTOMATION = "Industrial Automation"
    INFORMATION_SERVICES = "Information Services"
    INFORMATION_TECHNOLOGY_AND_SERVICES = "Information Technology and Services"
    INSURANCE = "Insurance"
    INTERNATIONAL_AFFAIRS = "International Affairs"
    INTERNATIONAL_TRADE_AND_DEVELOPMENT = "International Trade and Development"
    INTERNET = "Internet"
    INVESTMENT_BANKING = "Investment Banking"
    INVESTMENT_MANAGEMENT = "Investment Management"
    JUDICIARY = "Judiciary"
    LAW_ENFORCEMENT = "Law Enforcement"
    LAW_PRACTICE = "Law Practice"
    LEGAL_SERVICES = "Legal Services"
    LEGISLATIVE_OFFICE = "Legislative Office"
    LEISURE_TRAVEL_TOURISM = "Leisure, Travel & Tourism"
    LIBRARIES = "Libraries"
    LOGISTICS_AND_SUPPLY_CHAIN = "Logistics and Supply Chain"
    LUXURY_GOODS_JEWELRY = "Luxury Goods & Jewelry"
    MACHINERY = "Machinery"
    MANAGEMENT_CONSULTING = "Management Consulting"
    MARITIME = "Maritime"
    MARKET_RESEARCH = "Market Research"
    MARKETING_AND_ADVERTISING = "Marketing and Advertising"
    MECHANICAL_OR_INDUSTRIAL_ENGINEERING = "Mechanical or Industrial Engineering"
    MEDIA_PRODUCTION = "Media Production"
    MEDICAL_DEVICES = "Medical Devices"
    MEDICAL_PRACTICE = "Medical Practice"
    MENTAL_HEALTH_CARE = "Mental Health Care"
    MILITARY = "Military"
    MINING_METALS = "Mining & Metals"
    MOTION_PICTURES_AND_FILM = "Motion Pictures and Film"
    MUSEUMS_AND_INSTITUTIONS = "Museums and Institutions"
    MUSIC = "Music"
    NANOTECHNOLOGY = "Nanotechnology"
    NEWSPAPERS = "Newspapers"
    NON_PROFIT_ORGANIZATION_MANAGEMENT = "Non-Profit Organization Management"
    OIL_ENERGY = "Oil & Energy"
    ONLINE_MEDIA = "Online Media"
    OUTSOURCING_OFFSHORING = "Outsourcing/Offshoring"
    PACKAGE_FREIGHT_DELIVERY = "Package/Freight Delivery"
    PACKAGING_AND_CONTAINERS = "Packaging and Containers"
    PAPER_FOREST_PRODUCTS = "Paper & Forest Products"
    PERFORMING_ARTS = "Performing Arts"
    PHARMACEUTICALS = "Pharmaceuticals"
    PHILANTHROPY = "Philanthropy"
    PHOTOGRAPHY = "Photography"
    PLASTICS = "Plastics"
    POLITICAL_ORGANIZATION = "Political Organization"
    PRIMARY_SECONDARY_EDUCATION = "Primary/Secondary Education"
    PRINTING = "Printing"
    PROFESSIONAL_TRAINING_COACHING = "Professional Training & Coaching"
    PROGRAM_DEVELOPMENT = "Program Development"
    PUBLIC_POLICY = "Public Policy"
    PUBLIC_RELATIONS_AND_COMMUNICATIONS = "Public Relations and Communications"
    PUBLIC_SAFETY = "Public Safety"
    PUBLISHING = "Publishing"
    RAILROAD_MANUFACTURE = "Railroad Manufacture"
    RANCHING = "Ranching"
    REAL_ESTATE = "Real Estate"
    RECREATIONAL_FACILITIES_AND_SERVICES = "Recreational Facilities and Services"
    RELIGIOUS_INSTITUTIONS = "Religious Institutions"
    RENEWABLES_ENVIRONMENT = "Renewables & Environment"
    RESEARCH = "Research"
    RESTAURANTS = "Restaurants"
    RETAIL = "Retail"
    SECURITY_AND_INVESTIGATIONS = "Security and Investigations"
    SEMICONDUCTORS = "Semiconductors"
    SHIPBUILDING = "Shipbuilding"
    SPORTING_GOODS = "Sporting Goods"
    SPORTS = "Sports"
    STAFFING_AND_RECRUITING = "Staffing and Recruiting"
    SUPERMARKETS = "Supermarkets"
    TELECOMMUNICATIONS = "Telecommunications"
    TEXTILES = "Textiles"
    THINK_TANKS = "Think Tanks"
    TOBACCO = "Tobacco"
    TRANSLATION_AND_LOCALIZATION = "Translation and Localization"
    TRANSPORTATION_TRUCKING_RAILROAD = "Transportation/Trucking/Railroad"
    UTILITIES = "Utilities"
    VENTURE_CAPITAL_PRIVATE_EQUITY = "Venture Capital & Private Equity"
    VETERINARY = "Veterinary"
    WAREHOUSING = "Warehousing"
    WHOLESALE = "Wholesale"
    WINE_AND_SPIRITS = "Wine and Spirits"
    WIRELESS = "Wireless"
    WRITING_AND_EDITING = "Writing and Editing"

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
        if self is PatchUsersRequestIndustry.ACCOUNTING:
            return accounting()
        if self is PatchUsersRequestIndustry.AIRLINES_AVIATION:
            return airlines_aviation()
        if self is PatchUsersRequestIndustry.ALTERNATIVE_DISPUTE_RESOLUTION:
            return alternative_dispute_resolution()
        if self is PatchUsersRequestIndustry.ALTERNATIVE_MEDICINE:
            return alternative_medicine()
        if self is PatchUsersRequestIndustry.ANIMATION:
            return animation()
        if self is PatchUsersRequestIndustry.APPAREL_FASHION:
            return apparel_fashion()
        if self is PatchUsersRequestIndustry.ARCHITECTURE_PLANNING:
            return architecture_planning()
        if self is PatchUsersRequestIndustry.ARTS_AND_CRAFTS:
            return arts_and_crafts()
        if self is PatchUsersRequestIndustry.AUTOMOTIVE:
            return automotive()
        if self is PatchUsersRequestIndustry.AVIATION_AEROSPACE:
            return aviation_aerospace()
        if self is PatchUsersRequestIndustry.BANKING:
            return banking()
        if self is PatchUsersRequestIndustry.BIOTECHNOLOGY:
            return biotechnology()
        if self is PatchUsersRequestIndustry.BROADCAST_MEDIA:
            return broadcast_media()
        if self is PatchUsersRequestIndustry.BUILDING_MATERIALS:
            return building_materials()
        if self is PatchUsersRequestIndustry.BUSINESS_SUPPLIES_AND_EQUIPMENT:
            return business_supplies_and_equipment()
        if self is PatchUsersRequestIndustry.CAPITAL_MARKETS:
            return capital_markets()
        if self is PatchUsersRequestIndustry.CHEMICALS:
            return chemicals()
        if self is PatchUsersRequestIndustry.CIVIC_SOCIAL_ORGANIZATION:
            return civic_social_organization()
        if self is PatchUsersRequestIndustry.CIVIL_ENGINEERING:
            return civil_engineering()
        if self is PatchUsersRequestIndustry.COMMERCIAL_REAL_ESTATE:
            return commercial_real_estate()
        if self is PatchUsersRequestIndustry.COMPUTER_NETWORK_SECURITY:
            return computer_network_security()
        if self is PatchUsersRequestIndustry.COMPUTER_GAMES:
            return computer_games()
        if self is PatchUsersRequestIndustry.COMPUTER_HARDWARE:
            return computer_hardware()
        if self is PatchUsersRequestIndustry.COMPUTER_NETWORKING:
            return computer_networking()
        if self is PatchUsersRequestIndustry.COMPUTER_SOFTWARE:
            return computer_software()
        if self is PatchUsersRequestIndustry.CONSTRUCTION:
            return construction()
        if self is PatchUsersRequestIndustry.CONSUMER_ELECTRONICS:
            return consumer_electronics()
        if self is PatchUsersRequestIndustry.CONSUMER_GOODS:
            return consumer_goods()
        if self is PatchUsersRequestIndustry.CONSUMER_SERVICES:
            return consumer_services()
        if self is PatchUsersRequestIndustry.COSMETICS:
            return cosmetics()
        if self is PatchUsersRequestIndustry.DAIRY:
            return dairy()
        if self is PatchUsersRequestIndustry.DEFENSE_SPACE:
            return defense_space()
        if self is PatchUsersRequestIndustry.DESIGN:
            return design()
        if self is PatchUsersRequestIndustry.E_LEARNING:
            return e_learning()
        if self is PatchUsersRequestIndustry.EDUCATION_MANAGEMENT:
            return education_management()
        if self is PatchUsersRequestIndustry.ELECTRICAL_ELECTRONIC_MANUFACTURING:
            return electrical_electronic_manufacturing()
        if self is PatchUsersRequestIndustry.ENTERTAINMENT:
            return entertainment()
        if self is PatchUsersRequestIndustry.ENVIRONMENTAL_SERVICES:
            return environmental_services()
        if self is PatchUsersRequestIndustry.EVENTS_SERVICES:
            return events_services()
        if self is PatchUsersRequestIndustry.EXECUTIVE_OFFICE:
            return executive_office()
        if self is PatchUsersRequestIndustry.FACILITIES_SERVICES:
            return facilities_services()
        if self is PatchUsersRequestIndustry.FARMING:
            return farming()
        if self is PatchUsersRequestIndustry.FINANCIAL_SERVICES:
            return financial_services()
        if self is PatchUsersRequestIndustry.FINE_ART:
            return fine_art()
        if self is PatchUsersRequestIndustry.FISHERY:
            return fishery()
        if self is PatchUsersRequestIndustry.FOOD_BEVERAGES:
            return food_beverages()
        if self is PatchUsersRequestIndustry.FOOD_PRODUCTION:
            return food_production()
        if self is PatchUsersRequestIndustry.FUND_RAISING:
            return fund_raising()
        if self is PatchUsersRequestIndustry.FURNITURE:
            return furniture()
        if self is PatchUsersRequestIndustry.GAMBLING_CASINOS:
            return gambling_casinos()
        if self is PatchUsersRequestIndustry.GLASS_CERAMICS_CONCRETE:
            return glass_ceramics_concrete()
        if self is PatchUsersRequestIndustry.GOVERNMENT_ADMINISTRATION:
            return government_administration()
        if self is PatchUsersRequestIndustry.GOVERNMENT_RELATIONS:
            return government_relations()
        if self is PatchUsersRequestIndustry.GRAPHIC_DESIGN:
            return graphic_design()
        if self is PatchUsersRequestIndustry.HEALTH_WELLNESS_AND_FITNESS:
            return health_wellness_and_fitness()
        if self is PatchUsersRequestIndustry.HIGHER_EDUCATION:
            return higher_education()
        if self is PatchUsersRequestIndustry.HOSPITAL_HEALTH_CARE:
            return hospital_health_care()
        if self is PatchUsersRequestIndustry.HOSPITALITY:
            return hospitality()
        if self is PatchUsersRequestIndustry.HUMAN_RESOURCES:
            return human_resources()
        if self is PatchUsersRequestIndustry.IMPORT_AND_EXPORT:
            return import_and_export()
        if self is PatchUsersRequestIndustry.INDIVIDUAL_FAMILY_SERVICES:
            return individual_family_services()
        if self is PatchUsersRequestIndustry.INDUSTRIAL_AUTOMATION:
            return industrial_automation()
        if self is PatchUsersRequestIndustry.INFORMATION_SERVICES:
            return information_services()
        if self is PatchUsersRequestIndustry.INFORMATION_TECHNOLOGY_AND_SERVICES:
            return information_technology_and_services()
        if self is PatchUsersRequestIndustry.INSURANCE:
            return insurance()
        if self is PatchUsersRequestIndustry.INTERNATIONAL_AFFAIRS:
            return international_affairs()
        if self is PatchUsersRequestIndustry.INTERNATIONAL_TRADE_AND_DEVELOPMENT:
            return international_trade_and_development()
        if self is PatchUsersRequestIndustry.INTERNET:
            return internet()
        if self is PatchUsersRequestIndustry.INVESTMENT_BANKING:
            return investment_banking()
        if self is PatchUsersRequestIndustry.INVESTMENT_MANAGEMENT:
            return investment_management()
        if self is PatchUsersRequestIndustry.JUDICIARY:
            return judiciary()
        if self is PatchUsersRequestIndustry.LAW_ENFORCEMENT:
            return law_enforcement()
        if self is PatchUsersRequestIndustry.LAW_PRACTICE:
            return law_practice()
        if self is PatchUsersRequestIndustry.LEGAL_SERVICES:
            return legal_services()
        if self is PatchUsersRequestIndustry.LEGISLATIVE_OFFICE:
            return legislative_office()
        if self is PatchUsersRequestIndustry.LEISURE_TRAVEL_TOURISM:
            return leisure_travel_tourism()
        if self is PatchUsersRequestIndustry.LIBRARIES:
            return libraries()
        if self is PatchUsersRequestIndustry.LOGISTICS_AND_SUPPLY_CHAIN:
            return logistics_and_supply_chain()
        if self is PatchUsersRequestIndustry.LUXURY_GOODS_JEWELRY:
            return luxury_goods_jewelry()
        if self is PatchUsersRequestIndustry.MACHINERY:
            return machinery()
        if self is PatchUsersRequestIndustry.MANAGEMENT_CONSULTING:
            return management_consulting()
        if self is PatchUsersRequestIndustry.MARITIME:
            return maritime()
        if self is PatchUsersRequestIndustry.MARKET_RESEARCH:
            return market_research()
        if self is PatchUsersRequestIndustry.MARKETING_AND_ADVERTISING:
            return marketing_and_advertising()
        if self is PatchUsersRequestIndustry.MECHANICAL_OR_INDUSTRIAL_ENGINEERING:
            return mechanical_or_industrial_engineering()
        if self is PatchUsersRequestIndustry.MEDIA_PRODUCTION:
            return media_production()
        if self is PatchUsersRequestIndustry.MEDICAL_DEVICES:
            return medical_devices()
        if self is PatchUsersRequestIndustry.MEDICAL_PRACTICE:
            return medical_practice()
        if self is PatchUsersRequestIndustry.MENTAL_HEALTH_CARE:
            return mental_health_care()
        if self is PatchUsersRequestIndustry.MILITARY:
            return military()
        if self is PatchUsersRequestIndustry.MINING_METALS:
            return mining_metals()
        if self is PatchUsersRequestIndustry.MOTION_PICTURES_AND_FILM:
            return motion_pictures_and_film()
        if self is PatchUsersRequestIndustry.MUSEUMS_AND_INSTITUTIONS:
            return museums_and_institutions()
        if self is PatchUsersRequestIndustry.MUSIC:
            return music()
        if self is PatchUsersRequestIndustry.NANOTECHNOLOGY:
            return nanotechnology()
        if self is PatchUsersRequestIndustry.NEWSPAPERS:
            return newspapers()
        if self is PatchUsersRequestIndustry.NON_PROFIT_ORGANIZATION_MANAGEMENT:
            return non_profit_organization_management()
        if self is PatchUsersRequestIndustry.OIL_ENERGY:
            return oil_energy()
        if self is PatchUsersRequestIndustry.ONLINE_MEDIA:
            return online_media()
        if self is PatchUsersRequestIndustry.OUTSOURCING_OFFSHORING:
            return outsourcing_offshoring()
        if self is PatchUsersRequestIndustry.PACKAGE_FREIGHT_DELIVERY:
            return package_freight_delivery()
        if self is PatchUsersRequestIndustry.PACKAGING_AND_CONTAINERS:
            return packaging_and_containers()
        if self is PatchUsersRequestIndustry.PAPER_FOREST_PRODUCTS:
            return paper_forest_products()
        if self is PatchUsersRequestIndustry.PERFORMING_ARTS:
            return performing_arts()
        if self is PatchUsersRequestIndustry.PHARMACEUTICALS:
            return pharmaceuticals()
        if self is PatchUsersRequestIndustry.PHILANTHROPY:
            return philanthropy()
        if self is PatchUsersRequestIndustry.PHOTOGRAPHY:
            return photography()
        if self is PatchUsersRequestIndustry.PLASTICS:
            return plastics()
        if self is PatchUsersRequestIndustry.POLITICAL_ORGANIZATION:
            return political_organization()
        if self is PatchUsersRequestIndustry.PRIMARY_SECONDARY_EDUCATION:
            return primary_secondary_education()
        if self is PatchUsersRequestIndustry.PRINTING:
            return printing()
        if self is PatchUsersRequestIndustry.PROFESSIONAL_TRAINING_COACHING:
            return professional_training_coaching()
        if self is PatchUsersRequestIndustry.PROGRAM_DEVELOPMENT:
            return program_development()
        if self is PatchUsersRequestIndustry.PUBLIC_POLICY:
            return public_policy()
        if self is PatchUsersRequestIndustry.PUBLIC_RELATIONS_AND_COMMUNICATIONS:
            return public_relations_and_communications()
        if self is PatchUsersRequestIndustry.PUBLIC_SAFETY:
            return public_safety()
        if self is PatchUsersRequestIndustry.PUBLISHING:
            return publishing()
        if self is PatchUsersRequestIndustry.RAILROAD_MANUFACTURE:
            return railroad_manufacture()
        if self is PatchUsersRequestIndustry.RANCHING:
            return ranching()
        if self is PatchUsersRequestIndustry.REAL_ESTATE:
            return real_estate()
        if self is PatchUsersRequestIndustry.RECREATIONAL_FACILITIES_AND_SERVICES:
            return recreational_facilities_and_services()
        if self is PatchUsersRequestIndustry.RELIGIOUS_INSTITUTIONS:
            return religious_institutions()
        if self is PatchUsersRequestIndustry.RENEWABLES_ENVIRONMENT:
            return renewables_environment()
        if self is PatchUsersRequestIndustry.RESEARCH:
            return research()
        if self is PatchUsersRequestIndustry.RESTAURANTS:
            return restaurants()
        if self is PatchUsersRequestIndustry.RETAIL:
            return retail()
        if self is PatchUsersRequestIndustry.SECURITY_AND_INVESTIGATIONS:
            return security_and_investigations()
        if self is PatchUsersRequestIndustry.SEMICONDUCTORS:
            return semiconductors()
        if self is PatchUsersRequestIndustry.SHIPBUILDING:
            return shipbuilding()
        if self is PatchUsersRequestIndustry.SPORTING_GOODS:
            return sporting_goods()
        if self is PatchUsersRequestIndustry.SPORTS:
            return sports()
        if self is PatchUsersRequestIndustry.STAFFING_AND_RECRUITING:
            return staffing_and_recruiting()
        if self is PatchUsersRequestIndustry.SUPERMARKETS:
            return supermarkets()
        if self is PatchUsersRequestIndustry.TELECOMMUNICATIONS:
            return telecommunications()
        if self is PatchUsersRequestIndustry.TEXTILES:
            return textiles()
        if self is PatchUsersRequestIndustry.THINK_TANKS:
            return think_tanks()
        if self is PatchUsersRequestIndustry.TOBACCO:
            return tobacco()
        if self is PatchUsersRequestIndustry.TRANSLATION_AND_LOCALIZATION:
            return translation_and_localization()
        if self is PatchUsersRequestIndustry.TRANSPORTATION_TRUCKING_RAILROAD:
            return transportation_trucking_railroad()
        if self is PatchUsersRequestIndustry.UTILITIES:
            return utilities()
        if self is PatchUsersRequestIndustry.VENTURE_CAPITAL_PRIVATE_EQUITY:
            return venture_capital_private_equity()
        if self is PatchUsersRequestIndustry.VETERINARY:
            return veterinary()
        if self is PatchUsersRequestIndustry.WAREHOUSING:
            return warehousing()
        if self is PatchUsersRequestIndustry.WHOLESALE:
            return wholesale()
        if self is PatchUsersRequestIndustry.WINE_AND_SPIRITS:
            return wine_and_spirits()
        if self is PatchUsersRequestIndustry.WIRELESS:
            return wireless()
        if self is PatchUsersRequestIndustry.WRITING_AND_EDITING:
            return writing_and_editing()
