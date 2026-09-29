

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildingCategoryItem(enum.StrEnum):
    APARTMENTS = "apartments"
    BAKEHOUSE = "bakehouse"
    BARN = "barn"
    BRIDGE = "bridge"
    BUNGALOW = "bungalow"
    BUNKER = "bunker"
    CATHEDRAL = "cathedral"
    CABIN = "cabin"
    CARPORT = "carport"
    CHAPEL = "chapel"
    CHURCH = "church"
    CIVIC = "civic"
    COMMERCIAL = "commercial"
    CONSERVATORY = "conservatory"
    CONSTRUCTION = "construction"
    COWSHED = "cowshed"
    DETACHED = "detached"
    DIGESTER = "digester"
    DORMITORY = "dormitory"
    FARM = "farm"
    FARM_AUXILIARY = "farm_auxiliary"
    GARAGE = "garage"
    GARAGES = "garages"
    GARBAGE_SHED = "garbage_shed"
    GRANDSTAND = "grandstand"
    GREENHOUSE = "greenhouse"
    HANGAR = "hangar"
    HOSPITAL = "hospital"
    HOTEL = "hotel"
    HOUSE = "house"
    HOUSEBOAT = "houseboat"
    HUT = "hut"
    INDUSTRIAL = "industrial"
    KINDERGARTEN = "kindergarten"
    KIOSK = "kiosk"
    MOSQUE = "mosque"
    OFFICE = "office"
    PARKING = "parking"
    PAVILION = "pavilion"
    PUBLIC = "public"
    RESIDENTIAL = "residential"
    RETAIL = "retail"
    RIDING_HALL = "riding_hall"
    ROOF = "roof"
    RUINS = "ruins"
    SCHOOL = "school"
    SERVICE = "service"
    SHED = "shed"
    SHRINE = "shrine"
    STABLE = "stable"
    STADIUM = "stadium"
    STATIC_CARAVAN = "static_caravan"
    STY = "sty"
    SYNAGOGUE = "synagogue"
    TEMPLE = "temple"
    TERRACE = "terrace"
    TRAIN_STATION = "train_station"
    TRANSFORMER_TOWER = "transformer_tower"
    TRANSPORTATION = "transportation"
    UNIVERSITY = "university"
    WAREHOUSE = "warehouse"
    WATER_TOWER = "water_tower"

    def visit(
        self,
        apartments: typing.Callable[[], T_Result],
        bakehouse: typing.Callable[[], T_Result],
        barn: typing.Callable[[], T_Result],
        bridge: typing.Callable[[], T_Result],
        bungalow: typing.Callable[[], T_Result],
        bunker: typing.Callable[[], T_Result],
        cathedral: typing.Callable[[], T_Result],
        cabin: typing.Callable[[], T_Result],
        carport: typing.Callable[[], T_Result],
        chapel: typing.Callable[[], T_Result],
        church: typing.Callable[[], T_Result],
        civic: typing.Callable[[], T_Result],
        commercial: typing.Callable[[], T_Result],
        conservatory: typing.Callable[[], T_Result],
        construction: typing.Callable[[], T_Result],
        cowshed: typing.Callable[[], T_Result],
        detached: typing.Callable[[], T_Result],
        digester: typing.Callable[[], T_Result],
        dormitory: typing.Callable[[], T_Result],
        farm: typing.Callable[[], T_Result],
        farm_auxiliary: typing.Callable[[], T_Result],
        garage: typing.Callable[[], T_Result],
        garages: typing.Callable[[], T_Result],
        garbage_shed: typing.Callable[[], T_Result],
        grandstand: typing.Callable[[], T_Result],
        greenhouse: typing.Callable[[], T_Result],
        hangar: typing.Callable[[], T_Result],
        hospital: typing.Callable[[], T_Result],
        hotel: typing.Callable[[], T_Result],
        house: typing.Callable[[], T_Result],
        houseboat: typing.Callable[[], T_Result],
        hut: typing.Callable[[], T_Result],
        industrial: typing.Callable[[], T_Result],
        kindergarten: typing.Callable[[], T_Result],
        kiosk: typing.Callable[[], T_Result],
        mosque: typing.Callable[[], T_Result],
        office: typing.Callable[[], T_Result],
        parking: typing.Callable[[], T_Result],
        pavilion: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
        residential: typing.Callable[[], T_Result],
        retail: typing.Callable[[], T_Result],
        riding_hall: typing.Callable[[], T_Result],
        roof: typing.Callable[[], T_Result],
        ruins: typing.Callable[[], T_Result],
        school: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        shed: typing.Callable[[], T_Result],
        shrine: typing.Callable[[], T_Result],
        stable: typing.Callable[[], T_Result],
        stadium: typing.Callable[[], T_Result],
        static_caravan: typing.Callable[[], T_Result],
        sty: typing.Callable[[], T_Result],
        synagogue: typing.Callable[[], T_Result],
        temple: typing.Callable[[], T_Result],
        terrace: typing.Callable[[], T_Result],
        train_station: typing.Callable[[], T_Result],
        transformer_tower: typing.Callable[[], T_Result],
        transportation: typing.Callable[[], T_Result],
        university: typing.Callable[[], T_Result],
        warehouse: typing.Callable[[], T_Result],
        water_tower: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BuildingCategoryItem.APARTMENTS:
            return apartments()
        if self is BuildingCategoryItem.BAKEHOUSE:
            return bakehouse()
        if self is BuildingCategoryItem.BARN:
            return barn()
        if self is BuildingCategoryItem.BRIDGE:
            return bridge()
        if self is BuildingCategoryItem.BUNGALOW:
            return bungalow()
        if self is BuildingCategoryItem.BUNKER:
            return bunker()
        if self is BuildingCategoryItem.CATHEDRAL:
            return cathedral()
        if self is BuildingCategoryItem.CABIN:
            return cabin()
        if self is BuildingCategoryItem.CARPORT:
            return carport()
        if self is BuildingCategoryItem.CHAPEL:
            return chapel()
        if self is BuildingCategoryItem.CHURCH:
            return church()
        if self is BuildingCategoryItem.CIVIC:
            return civic()
        if self is BuildingCategoryItem.COMMERCIAL:
            return commercial()
        if self is BuildingCategoryItem.CONSERVATORY:
            return conservatory()
        if self is BuildingCategoryItem.CONSTRUCTION:
            return construction()
        if self is BuildingCategoryItem.COWSHED:
            return cowshed()
        if self is BuildingCategoryItem.DETACHED:
            return detached()
        if self is BuildingCategoryItem.DIGESTER:
            return digester()
        if self is BuildingCategoryItem.DORMITORY:
            return dormitory()
        if self is BuildingCategoryItem.FARM:
            return farm()
        if self is BuildingCategoryItem.FARM_AUXILIARY:
            return farm_auxiliary()
        if self is BuildingCategoryItem.GARAGE:
            return garage()
        if self is BuildingCategoryItem.GARAGES:
            return garages()
        if self is BuildingCategoryItem.GARBAGE_SHED:
            return garbage_shed()
        if self is BuildingCategoryItem.GRANDSTAND:
            return grandstand()
        if self is BuildingCategoryItem.GREENHOUSE:
            return greenhouse()
        if self is BuildingCategoryItem.HANGAR:
            return hangar()
        if self is BuildingCategoryItem.HOSPITAL:
            return hospital()
        if self is BuildingCategoryItem.HOTEL:
            return hotel()
        if self is BuildingCategoryItem.HOUSE:
            return house()
        if self is BuildingCategoryItem.HOUSEBOAT:
            return houseboat()
        if self is BuildingCategoryItem.HUT:
            return hut()
        if self is BuildingCategoryItem.INDUSTRIAL:
            return industrial()
        if self is BuildingCategoryItem.KINDERGARTEN:
            return kindergarten()
        if self is BuildingCategoryItem.KIOSK:
            return kiosk()
        if self is BuildingCategoryItem.MOSQUE:
            return mosque()
        if self is BuildingCategoryItem.OFFICE:
            return office()
        if self is BuildingCategoryItem.PARKING:
            return parking()
        if self is BuildingCategoryItem.PAVILION:
            return pavilion()
        if self is BuildingCategoryItem.PUBLIC:
            return public()
        if self is BuildingCategoryItem.RESIDENTIAL:
            return residential()
        if self is BuildingCategoryItem.RETAIL:
            return retail()
        if self is BuildingCategoryItem.RIDING_HALL:
            return riding_hall()
        if self is BuildingCategoryItem.ROOF:
            return roof()
        if self is BuildingCategoryItem.RUINS:
            return ruins()
        if self is BuildingCategoryItem.SCHOOL:
            return school()
        if self is BuildingCategoryItem.SERVICE:
            return service()
        if self is BuildingCategoryItem.SHED:
            return shed()
        if self is BuildingCategoryItem.SHRINE:
            return shrine()
        if self is BuildingCategoryItem.STABLE:
            return stable()
        if self is BuildingCategoryItem.STADIUM:
            return stadium()
        if self is BuildingCategoryItem.STATIC_CARAVAN:
            return static_caravan()
        if self is BuildingCategoryItem.STY:
            return sty()
        if self is BuildingCategoryItem.SYNAGOGUE:
            return synagogue()
        if self is BuildingCategoryItem.TEMPLE:
            return temple()
        if self is BuildingCategoryItem.TERRACE:
            return terrace()
        if self is BuildingCategoryItem.TRAIN_STATION:
            return train_station()
        if self is BuildingCategoryItem.TRANSFORMER_TOWER:
            return transformer_tower()
        if self is BuildingCategoryItem.TRANSPORTATION:
            return transportation()
        if self is BuildingCategoryItem.UNIVERSITY:
            return university()
        if self is BuildingCategoryItem.WAREHOUSE:
            return warehouse()
        if self is BuildingCategoryItem.WATER_TOWER:
            return water_tower()
