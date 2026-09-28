

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchoolLocationCountry(enum.StrEnum):
    """
    The country associated with the school
    """

    AFGHANISTAN = "afghanistan"
    ALBANIA = "albania"
    ALGERIA = "algeria"
    AMERICAN_SAMOA = "american samoa"
    ANDORRA = "andorra"
    ANGOLA = "angola"
    ANGUILLA = "anguilla"
    ANTARCTICA = "antarctica"
    ANTIGUA_AND_BARBUDA = "antigua and barbuda"
    ARGENTINA = "argentina"
    ARMENIA = "armenia"
    ARUBA = "aruba"
    AUSTRALIA = "australia"
    AUSTRIA = "austria"
    AZERBAIJAN = "azerbaijan"
    BAHAMAS = "bahamas"
    BAHRAIN = "bahrain"
    BANGLADESH = "bangladesh"
    BARBADOS = "barbados"
    BELARUS = "belarus"
    BELGIUM = "belgium"
    BELIZE = "belize"
    BENIN = "benin"
    BERMUDA = "bermuda"
    BHUTAN = "bhutan"
    BOLIVIA = "bolivia"
    BOSNIA_AND_HERZEGOVINA = "bosnia and herzegovina"
    BOTSWANA = "botswana"
    BOUVET_ISLAND = "bouvet island"
    BRAZIL = "brazil"
    BRITISH_INDIAN_OCEAN_TERRITORY = "british indian ocean territory"
    BRITISH_VIRGIN_ISLANDS = "british virgin islands"
    BRUNEI = "brunei"
    BULGARIA = "bulgaria"
    BURKINA_FASO = "burkina faso"
    BURUNDI = "burundi"
    CAMBODIA = "cambodia"
    CAMEROON = "cameroon"
    CANADA = "canada"
    CAPE_VERDE = "cape verde"
    CARIBBEAN_NETHERLANDS = "caribbean netherlands"
    CAYMAN_ISLANDS = "cayman islands"
    CENTRAL_AFRICAN_REPUBLIC = "central african republic"
    CHAD = "chad"
    CHILE = "chile"
    CHINA = "china"
    CHRISTMAS_ISLAND = "christmas island"
    COCOS_KEELING_ISLANDS = "cocos (keeling) islands"
    COLOMBIA = "colombia"
    COMOROS = "comoros"
    COOK_ISLANDS = "cook islands"
    COSTA_RICA = "costa rica"
    CROATIA = "croatia"
    CUBA = "cuba"
    CURACAO = "curaçao"
    CYPRUS = "cyprus"
    CZECHIA = "czechia"
    DEMOCRATIC_REPUBLIC_OF_THE_CONGO = "democratic republic of the congo"
    DENMARK = "denmark"
    DJIBOUTI = "djibouti"
    DOMINICA = "dominica"
    DOMINICAN_REPUBLIC = "dominican republic"
    ECUADOR = "ecuador"
    EGYPT = "egypt"
    EL_SALVADOR = "el salvador"
    EQUATORIAL_GUINEA = "equatorial guinea"
    ERITREA = "eritrea"
    ESTONIA = "estonia"
    ETHIOPIA = "ethiopia"
    FALKLAND_ISLANDS = "falkland islands"
    FAROE_ISLANDS = "faroe islands"
    FIJI = "fiji"
    FINLAND = "finland"
    FRANCE = "france"
    FRENCH_GUIANA = "french guiana"
    FRENCH_POLYNESIA = "french polynesia"
    FRENCH_SOUTHERN_TERRITORIES = "french southern territories"
    GABON = "gabon"
    GAMBIA = "gambia"
    GEORGIA = "georgia"
    GERMANY = "germany"
    GHANA = "ghana"
    GIBRALTAR = "gibraltar"
    GREECE = "greece"
    GREENLAND = "greenland"
    GRENADA = "grenada"
    GUADELOUPE = "guadeloupe"
    GUAM = "guam"
    GUATEMALA = "guatemala"
    GUERNSEY = "guernsey"
    GUINEA = "guinea"
    GUINEA_BISSAU = "guinea-bissau"
    GUYANA = "guyana"
    HAITI = "haiti"
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = "heard island and mcdonald islands"
    HONDURAS = "honduras"
    HONG_KONG = "hong kong"
    HUNGARY = "hungary"
    ICELAND = "iceland"
    INDIA = "india"
    INDONESIA = "indonesia"
    IRAN = "iran"
    IRAQ = "iraq"
    IRELAND = "ireland"
    ISLE_OF_MAN = "isle of man"
    ISRAEL = "israel"
    ITALY = "italy"
    IVORY_COAST = "ivory coast"
    JAMAICA = "jamaica"
    JAPAN = "japan"
    JERSEY = "jersey"
    JORDAN = "jordan"
    KAZAKHSTAN = "kazakhstan"
    KENYA = "kenya"
    KIRIBATI = "kiribati"
    KOSOVO = "kosovo"
    KUWAIT = "kuwait"
    KYRGYZSTAN = "kyrgyzstan"
    LAOS = "laos"
    LATVIA = "latvia"
    LEBANON = "lebanon"
    LESOTHO = "lesotho"
    LIBERIA = "liberia"
    LIBYA = "libya"
    LIECHTENSTEIN = "liechtenstein"
    LITHUANIA = "lithuania"
    LUXEMBOURG = "luxembourg"
    MACAU = "macau"
    MACEDONIA = "macedonia"
    MADAGASCAR = "madagascar"
    MALAWI = "malawi"
    MALAYSIA = "malaysia"
    MALDIVES = "maldives"
    MALI = "mali"
    MALTA = "malta"
    MARSHALL_ISLANDS = "marshall islands"
    MARTINIQUE = "martinique"
    MAURITANIA = "mauritania"
    MAURITIUS = "mauritius"
    MAYOTTE = "mayotte"
    MEXICO = "mexico"
    MICRONESIA = "micronesia"
    MOLDOVA = "moldova"
    MONACO = "monaco"
    MONGOLIA = "mongolia"
    MONTENEGRO = "montenegro"
    MONTSERRAT = "montserrat"
    MOROCCO = "morocco"
    MOZAMBIQUE = "mozambique"
    MYANMAR = "myanmar"
    NAMIBIA = "namibia"
    NAURU = "nauru"
    NEPAL = "nepal"
    NETHERLANDS = "netherlands"
    NETHERLANDS_ANTILLES = "netherlands antilles"
    NEW_CALEDONIA = "new caledonia"
    NEW_ZEALAND = "new zealand"
    NICARAGUA = "nicaragua"
    NIGER = "niger"
    NIGERIA = "nigeria"
    NIUE = "niue"
    NORFOLK_ISLAND = "norfolk island"
    NORTH_KOREA = "north korea"
    NORTHERN_MARIANA_ISLANDS = "northern mariana islands"
    NORWAY = "norway"
    OMAN = "oman"
    PAKISTAN = "pakistan"
    PALAU = "palau"
    PALESTINE = "palestine"
    PANAMA = "panama"
    PAPUA_NEW_GUINEA = "papua new guinea"
    PARAGUAY = "paraguay"
    PERU = "peru"
    PHILIPPINES = "philippines"
    PITCAIRN = "pitcairn"
    POLAND = "poland"
    PORTUGAL = "portugal"
    PUERTO_RICO = "puerto rico"
    QATAR = "qatar"
    REPUBLIC_OF_THE_CONGO = "republic of the congo"
    ROMANIA = "romania"
    RUSSIA = "russia"
    RWANDA = "rwanda"
    REUNION = "réunion"
    SAINT_BARTHELEMY = "saint barthélemy"
    SAINT_HELENA = "saint helena"
    SAINT_KITTS_AND_NEVIS = "saint kitts and nevis"
    SAINT_LUCIA = "saint lucia"
    SAINT_MARTIN = "saint martin"
    SAINT_PIERRE_AND_MIQUELON = "saint pierre and miquelon"
    SAINT_VINCENT_AND_THE_GRENADINES = "saint vincent and the grenadines"
    SAMOA = "samoa"
    SAN_MARINO = "san marino"
    SAUDI_ARABIA = "saudi arabia"
    SENEGAL = "senegal"
    SERBIA = "serbia"
    SEYCHELLES = "seychelles"
    SIERRA_LEONE = "sierra leone"
    SINGAPORE = "singapore"
    SINT_MAARTEN = "sint maarten"
    SLOVAKIA = "slovakia"
    SLOVENIA = "slovenia"
    SOLOMON_ISLANDS = "solomon islands"
    SOMALIA = "somalia"
    SOUTH_AFRICA = "south africa"
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = "south georgia and the south sandwich islands"
    SOUTH_KOREA = "south korea"
    SOUTH_SUDAN = "south sudan"
    SPAIN = "spain"
    SRI_LANKA = "sri lanka"
    SUDAN = "sudan"
    SURINAME = "suriname"
    SVALBARD_AND_JAN_MAYEN = "svalbard and jan mayen"
    SWAZILAND = "swaziland"
    SWEDEN = "sweden"
    SWITZERLAND = "switzerland"
    SYRIA = "syria"
    SAO_TOME_AND_PRINCIPE = "são tomé and príncipe"
    TAIWAN = "taiwan"
    TAJIKISTAN = "tajikistan"
    TANZANIA = "tanzania"
    THAILAND = "thailand"
    TIMOR_LESTE = "timor-leste"
    TOGO = "togo"
    TOKELAU = "tokelau"
    TONGA = "tonga"
    TRINIDAD_AND_TOBAGO = "trinidad and tobago"
    TUNISIA = "tunisia"
    TURKEY = "turkey"
    TURKMENISTAN = "turkmenistan"
    TURKS_AND_CAICOS_ISLANDS = "turks and caicos islands"
    TUVALU = "tuvalu"
    US_VIRGIN_ISLANDS = "u.s. virgin islands"
    UGANDA = "uganda"
    UKRAINE = "ukraine"
    UNITED_ARAB_EMIRATES = "united arab emirates"
    UNITED_KINGDOM = "united kingdom"
    UNITED_STATES = "united states"
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = "united states minor outlying islands"
    URUGUAY = "uruguay"
    UZBEKISTAN = "uzbekistan"
    VANUATU = "vanuatu"
    VATICAN_CITY = "vatican city"
    VENEZUELA = "venezuela"
    VIETNAM = "vietnam"
    WALLIS_AND_FUTUNA = "wallis and futuna"
    WESTERN_SAHARA = "western sahara"
    YEMEN = "yemen"
    ZAMBIA = "zambia"
    ZIMBABWE = "zimbabwe"
    ALAND_ISLANDS = "åland islands"

    def visit(
        self,
        afghanistan: typing.Callable[[], T_Result],
        albania: typing.Callable[[], T_Result],
        algeria: typing.Callable[[], T_Result],
        american_samoa: typing.Callable[[], T_Result],
        andorra: typing.Callable[[], T_Result],
        angola: typing.Callable[[], T_Result],
        anguilla: typing.Callable[[], T_Result],
        antarctica: typing.Callable[[], T_Result],
        antigua_and_barbuda: typing.Callable[[], T_Result],
        argentina: typing.Callable[[], T_Result],
        armenia: typing.Callable[[], T_Result],
        aruba: typing.Callable[[], T_Result],
        australia: typing.Callable[[], T_Result],
        austria: typing.Callable[[], T_Result],
        azerbaijan: typing.Callable[[], T_Result],
        bahamas: typing.Callable[[], T_Result],
        bahrain: typing.Callable[[], T_Result],
        bangladesh: typing.Callable[[], T_Result],
        barbados: typing.Callable[[], T_Result],
        belarus: typing.Callable[[], T_Result],
        belgium: typing.Callable[[], T_Result],
        belize: typing.Callable[[], T_Result],
        benin: typing.Callable[[], T_Result],
        bermuda: typing.Callable[[], T_Result],
        bhutan: typing.Callable[[], T_Result],
        bolivia: typing.Callable[[], T_Result],
        bosnia_and_herzegovina: typing.Callable[[], T_Result],
        botswana: typing.Callable[[], T_Result],
        bouvet_island: typing.Callable[[], T_Result],
        brazil: typing.Callable[[], T_Result],
        british_indian_ocean_territory: typing.Callable[[], T_Result],
        british_virgin_islands: typing.Callable[[], T_Result],
        brunei: typing.Callable[[], T_Result],
        bulgaria: typing.Callable[[], T_Result],
        burkina_faso: typing.Callable[[], T_Result],
        burundi: typing.Callable[[], T_Result],
        cambodia: typing.Callable[[], T_Result],
        cameroon: typing.Callable[[], T_Result],
        canada: typing.Callable[[], T_Result],
        cape_verde: typing.Callable[[], T_Result],
        caribbean_netherlands: typing.Callable[[], T_Result],
        cayman_islands: typing.Callable[[], T_Result],
        central_african_republic: typing.Callable[[], T_Result],
        chad: typing.Callable[[], T_Result],
        chile: typing.Callable[[], T_Result],
        china: typing.Callable[[], T_Result],
        christmas_island: typing.Callable[[], T_Result],
        cocos_keeling_islands: typing.Callable[[], T_Result],
        colombia: typing.Callable[[], T_Result],
        comoros: typing.Callable[[], T_Result],
        cook_islands: typing.Callable[[], T_Result],
        costa_rica: typing.Callable[[], T_Result],
        croatia: typing.Callable[[], T_Result],
        cuba: typing.Callable[[], T_Result],
        curacao: typing.Callable[[], T_Result],
        cyprus: typing.Callable[[], T_Result],
        czechia: typing.Callable[[], T_Result],
        democratic_republic_of_the_congo: typing.Callable[[], T_Result],
        denmark: typing.Callable[[], T_Result],
        djibouti: typing.Callable[[], T_Result],
        dominica: typing.Callable[[], T_Result],
        dominican_republic: typing.Callable[[], T_Result],
        ecuador: typing.Callable[[], T_Result],
        egypt: typing.Callable[[], T_Result],
        el_salvador: typing.Callable[[], T_Result],
        equatorial_guinea: typing.Callable[[], T_Result],
        eritrea: typing.Callable[[], T_Result],
        estonia: typing.Callable[[], T_Result],
        ethiopia: typing.Callable[[], T_Result],
        falkland_islands: typing.Callable[[], T_Result],
        faroe_islands: typing.Callable[[], T_Result],
        fiji: typing.Callable[[], T_Result],
        finland: typing.Callable[[], T_Result],
        france: typing.Callable[[], T_Result],
        french_guiana: typing.Callable[[], T_Result],
        french_polynesia: typing.Callable[[], T_Result],
        french_southern_territories: typing.Callable[[], T_Result],
        gabon: typing.Callable[[], T_Result],
        gambia: typing.Callable[[], T_Result],
        georgia: typing.Callable[[], T_Result],
        germany: typing.Callable[[], T_Result],
        ghana: typing.Callable[[], T_Result],
        gibraltar: typing.Callable[[], T_Result],
        greece: typing.Callable[[], T_Result],
        greenland: typing.Callable[[], T_Result],
        grenada: typing.Callable[[], T_Result],
        guadeloupe: typing.Callable[[], T_Result],
        guam: typing.Callable[[], T_Result],
        guatemala: typing.Callable[[], T_Result],
        guernsey: typing.Callable[[], T_Result],
        guinea: typing.Callable[[], T_Result],
        guinea_bissau: typing.Callable[[], T_Result],
        guyana: typing.Callable[[], T_Result],
        haiti: typing.Callable[[], T_Result],
        heard_island_and_mcdonald_islands: typing.Callable[[], T_Result],
        honduras: typing.Callable[[], T_Result],
        hong_kong: typing.Callable[[], T_Result],
        hungary: typing.Callable[[], T_Result],
        iceland: typing.Callable[[], T_Result],
        india: typing.Callable[[], T_Result],
        indonesia: typing.Callable[[], T_Result],
        iran: typing.Callable[[], T_Result],
        iraq: typing.Callable[[], T_Result],
        ireland: typing.Callable[[], T_Result],
        isle_of_man: typing.Callable[[], T_Result],
        israel: typing.Callable[[], T_Result],
        italy: typing.Callable[[], T_Result],
        ivory_coast: typing.Callable[[], T_Result],
        jamaica: typing.Callable[[], T_Result],
        japan: typing.Callable[[], T_Result],
        jersey: typing.Callable[[], T_Result],
        jordan: typing.Callable[[], T_Result],
        kazakhstan: typing.Callable[[], T_Result],
        kenya: typing.Callable[[], T_Result],
        kiribati: typing.Callable[[], T_Result],
        kosovo: typing.Callable[[], T_Result],
        kuwait: typing.Callable[[], T_Result],
        kyrgyzstan: typing.Callable[[], T_Result],
        laos: typing.Callable[[], T_Result],
        latvia: typing.Callable[[], T_Result],
        lebanon: typing.Callable[[], T_Result],
        lesotho: typing.Callable[[], T_Result],
        liberia: typing.Callable[[], T_Result],
        libya: typing.Callable[[], T_Result],
        liechtenstein: typing.Callable[[], T_Result],
        lithuania: typing.Callable[[], T_Result],
        luxembourg: typing.Callable[[], T_Result],
        macau: typing.Callable[[], T_Result],
        macedonia: typing.Callable[[], T_Result],
        madagascar: typing.Callable[[], T_Result],
        malawi: typing.Callable[[], T_Result],
        malaysia: typing.Callable[[], T_Result],
        maldives: typing.Callable[[], T_Result],
        mali: typing.Callable[[], T_Result],
        malta: typing.Callable[[], T_Result],
        marshall_islands: typing.Callable[[], T_Result],
        martinique: typing.Callable[[], T_Result],
        mauritania: typing.Callable[[], T_Result],
        mauritius: typing.Callable[[], T_Result],
        mayotte: typing.Callable[[], T_Result],
        mexico: typing.Callable[[], T_Result],
        micronesia: typing.Callable[[], T_Result],
        moldova: typing.Callable[[], T_Result],
        monaco: typing.Callable[[], T_Result],
        mongolia: typing.Callable[[], T_Result],
        montenegro: typing.Callable[[], T_Result],
        montserrat: typing.Callable[[], T_Result],
        morocco: typing.Callable[[], T_Result],
        mozambique: typing.Callable[[], T_Result],
        myanmar: typing.Callable[[], T_Result],
        namibia: typing.Callable[[], T_Result],
        nauru: typing.Callable[[], T_Result],
        nepal: typing.Callable[[], T_Result],
        netherlands: typing.Callable[[], T_Result],
        netherlands_antilles: typing.Callable[[], T_Result],
        new_caledonia: typing.Callable[[], T_Result],
        new_zealand: typing.Callable[[], T_Result],
        nicaragua: typing.Callable[[], T_Result],
        niger: typing.Callable[[], T_Result],
        nigeria: typing.Callable[[], T_Result],
        niue: typing.Callable[[], T_Result],
        norfolk_island: typing.Callable[[], T_Result],
        north_korea: typing.Callable[[], T_Result],
        northern_mariana_islands: typing.Callable[[], T_Result],
        norway: typing.Callable[[], T_Result],
        oman: typing.Callable[[], T_Result],
        pakistan: typing.Callable[[], T_Result],
        palau: typing.Callable[[], T_Result],
        palestine: typing.Callable[[], T_Result],
        panama: typing.Callable[[], T_Result],
        papua_new_guinea: typing.Callable[[], T_Result],
        paraguay: typing.Callable[[], T_Result],
        peru: typing.Callable[[], T_Result],
        philippines: typing.Callable[[], T_Result],
        pitcairn: typing.Callable[[], T_Result],
        poland: typing.Callable[[], T_Result],
        portugal: typing.Callable[[], T_Result],
        puerto_rico: typing.Callable[[], T_Result],
        qatar: typing.Callable[[], T_Result],
        republic_of_the_congo: typing.Callable[[], T_Result],
        romania: typing.Callable[[], T_Result],
        russia: typing.Callable[[], T_Result],
        rwanda: typing.Callable[[], T_Result],
        reunion: typing.Callable[[], T_Result],
        saint_barthelemy: typing.Callable[[], T_Result],
        saint_helena: typing.Callable[[], T_Result],
        saint_kitts_and_nevis: typing.Callable[[], T_Result],
        saint_lucia: typing.Callable[[], T_Result],
        saint_martin: typing.Callable[[], T_Result],
        saint_pierre_and_miquelon: typing.Callable[[], T_Result],
        saint_vincent_and_the_grenadines: typing.Callable[[], T_Result],
        samoa: typing.Callable[[], T_Result],
        san_marino: typing.Callable[[], T_Result],
        saudi_arabia: typing.Callable[[], T_Result],
        senegal: typing.Callable[[], T_Result],
        serbia: typing.Callable[[], T_Result],
        seychelles: typing.Callable[[], T_Result],
        sierra_leone: typing.Callable[[], T_Result],
        singapore: typing.Callable[[], T_Result],
        sint_maarten: typing.Callable[[], T_Result],
        slovakia: typing.Callable[[], T_Result],
        slovenia: typing.Callable[[], T_Result],
        solomon_islands: typing.Callable[[], T_Result],
        somalia: typing.Callable[[], T_Result],
        south_africa: typing.Callable[[], T_Result],
        south_georgia_and_the_south_sandwich_islands: typing.Callable[[], T_Result],
        south_korea: typing.Callable[[], T_Result],
        south_sudan: typing.Callable[[], T_Result],
        spain: typing.Callable[[], T_Result],
        sri_lanka: typing.Callable[[], T_Result],
        sudan: typing.Callable[[], T_Result],
        suriname: typing.Callable[[], T_Result],
        svalbard_and_jan_mayen: typing.Callable[[], T_Result],
        swaziland: typing.Callable[[], T_Result],
        sweden: typing.Callable[[], T_Result],
        switzerland: typing.Callable[[], T_Result],
        syria: typing.Callable[[], T_Result],
        sao_tome_and_principe: typing.Callable[[], T_Result],
        taiwan: typing.Callable[[], T_Result],
        tajikistan: typing.Callable[[], T_Result],
        tanzania: typing.Callable[[], T_Result],
        thailand: typing.Callable[[], T_Result],
        timor_leste: typing.Callable[[], T_Result],
        togo: typing.Callable[[], T_Result],
        tokelau: typing.Callable[[], T_Result],
        tonga: typing.Callable[[], T_Result],
        trinidad_and_tobago: typing.Callable[[], T_Result],
        tunisia: typing.Callable[[], T_Result],
        turkey: typing.Callable[[], T_Result],
        turkmenistan: typing.Callable[[], T_Result],
        turks_and_caicos_islands: typing.Callable[[], T_Result],
        tuvalu: typing.Callable[[], T_Result],
        us_virgin_islands: typing.Callable[[], T_Result],
        uganda: typing.Callable[[], T_Result],
        ukraine: typing.Callable[[], T_Result],
        united_arab_emirates: typing.Callable[[], T_Result],
        united_kingdom: typing.Callable[[], T_Result],
        united_states: typing.Callable[[], T_Result],
        united_states_minor_outlying_islands: typing.Callable[[], T_Result],
        uruguay: typing.Callable[[], T_Result],
        uzbekistan: typing.Callable[[], T_Result],
        vanuatu: typing.Callable[[], T_Result],
        vatican_city: typing.Callable[[], T_Result],
        venezuela: typing.Callable[[], T_Result],
        vietnam: typing.Callable[[], T_Result],
        wallis_and_futuna: typing.Callable[[], T_Result],
        western_sahara: typing.Callable[[], T_Result],
        yemen: typing.Callable[[], T_Result],
        zambia: typing.Callable[[], T_Result],
        zimbabwe: typing.Callable[[], T_Result],
        aland_islands: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchoolLocationCountry.AFGHANISTAN:
            return afghanistan()
        if self is SchoolLocationCountry.ALBANIA:
            return albania()
        if self is SchoolLocationCountry.ALGERIA:
            return algeria()
        if self is SchoolLocationCountry.AMERICAN_SAMOA:
            return american_samoa()
        if self is SchoolLocationCountry.ANDORRA:
            return andorra()
        if self is SchoolLocationCountry.ANGOLA:
            return angola()
        if self is SchoolLocationCountry.ANGUILLA:
            return anguilla()
        if self is SchoolLocationCountry.ANTARCTICA:
            return antarctica()
        if self is SchoolLocationCountry.ANTIGUA_AND_BARBUDA:
            return antigua_and_barbuda()
        if self is SchoolLocationCountry.ARGENTINA:
            return argentina()
        if self is SchoolLocationCountry.ARMENIA:
            return armenia()
        if self is SchoolLocationCountry.ARUBA:
            return aruba()
        if self is SchoolLocationCountry.AUSTRALIA:
            return australia()
        if self is SchoolLocationCountry.AUSTRIA:
            return austria()
        if self is SchoolLocationCountry.AZERBAIJAN:
            return azerbaijan()
        if self is SchoolLocationCountry.BAHAMAS:
            return bahamas()
        if self is SchoolLocationCountry.BAHRAIN:
            return bahrain()
        if self is SchoolLocationCountry.BANGLADESH:
            return bangladesh()
        if self is SchoolLocationCountry.BARBADOS:
            return barbados()
        if self is SchoolLocationCountry.BELARUS:
            return belarus()
        if self is SchoolLocationCountry.BELGIUM:
            return belgium()
        if self is SchoolLocationCountry.BELIZE:
            return belize()
        if self is SchoolLocationCountry.BENIN:
            return benin()
        if self is SchoolLocationCountry.BERMUDA:
            return bermuda()
        if self is SchoolLocationCountry.BHUTAN:
            return bhutan()
        if self is SchoolLocationCountry.BOLIVIA:
            return bolivia()
        if self is SchoolLocationCountry.BOSNIA_AND_HERZEGOVINA:
            return bosnia_and_herzegovina()
        if self is SchoolLocationCountry.BOTSWANA:
            return botswana()
        if self is SchoolLocationCountry.BOUVET_ISLAND:
            return bouvet_island()
        if self is SchoolLocationCountry.BRAZIL:
            return brazil()
        if self is SchoolLocationCountry.BRITISH_INDIAN_OCEAN_TERRITORY:
            return british_indian_ocean_territory()
        if self is SchoolLocationCountry.BRITISH_VIRGIN_ISLANDS:
            return british_virgin_islands()
        if self is SchoolLocationCountry.BRUNEI:
            return brunei()
        if self is SchoolLocationCountry.BULGARIA:
            return bulgaria()
        if self is SchoolLocationCountry.BURKINA_FASO:
            return burkina_faso()
        if self is SchoolLocationCountry.BURUNDI:
            return burundi()
        if self is SchoolLocationCountry.CAMBODIA:
            return cambodia()
        if self is SchoolLocationCountry.CAMEROON:
            return cameroon()
        if self is SchoolLocationCountry.CANADA:
            return canada()
        if self is SchoolLocationCountry.CAPE_VERDE:
            return cape_verde()
        if self is SchoolLocationCountry.CARIBBEAN_NETHERLANDS:
            return caribbean_netherlands()
        if self is SchoolLocationCountry.CAYMAN_ISLANDS:
            return cayman_islands()
        if self is SchoolLocationCountry.CENTRAL_AFRICAN_REPUBLIC:
            return central_african_republic()
        if self is SchoolLocationCountry.CHAD:
            return chad()
        if self is SchoolLocationCountry.CHILE:
            return chile()
        if self is SchoolLocationCountry.CHINA:
            return china()
        if self is SchoolLocationCountry.CHRISTMAS_ISLAND:
            return christmas_island()
        if self is SchoolLocationCountry.COCOS_KEELING_ISLANDS:
            return cocos_keeling_islands()
        if self is SchoolLocationCountry.COLOMBIA:
            return colombia()
        if self is SchoolLocationCountry.COMOROS:
            return comoros()
        if self is SchoolLocationCountry.COOK_ISLANDS:
            return cook_islands()
        if self is SchoolLocationCountry.COSTA_RICA:
            return costa_rica()
        if self is SchoolLocationCountry.CROATIA:
            return croatia()
        if self is SchoolLocationCountry.CUBA:
            return cuba()
        if self is SchoolLocationCountry.CURACAO:
            return curacao()
        if self is SchoolLocationCountry.CYPRUS:
            return cyprus()
        if self is SchoolLocationCountry.CZECHIA:
            return czechia()
        if self is SchoolLocationCountry.DEMOCRATIC_REPUBLIC_OF_THE_CONGO:
            return democratic_republic_of_the_congo()
        if self is SchoolLocationCountry.DENMARK:
            return denmark()
        if self is SchoolLocationCountry.DJIBOUTI:
            return djibouti()
        if self is SchoolLocationCountry.DOMINICA:
            return dominica()
        if self is SchoolLocationCountry.DOMINICAN_REPUBLIC:
            return dominican_republic()
        if self is SchoolLocationCountry.ECUADOR:
            return ecuador()
        if self is SchoolLocationCountry.EGYPT:
            return egypt()
        if self is SchoolLocationCountry.EL_SALVADOR:
            return el_salvador()
        if self is SchoolLocationCountry.EQUATORIAL_GUINEA:
            return equatorial_guinea()
        if self is SchoolLocationCountry.ERITREA:
            return eritrea()
        if self is SchoolLocationCountry.ESTONIA:
            return estonia()
        if self is SchoolLocationCountry.ETHIOPIA:
            return ethiopia()
        if self is SchoolLocationCountry.FALKLAND_ISLANDS:
            return falkland_islands()
        if self is SchoolLocationCountry.FAROE_ISLANDS:
            return faroe_islands()
        if self is SchoolLocationCountry.FIJI:
            return fiji()
        if self is SchoolLocationCountry.FINLAND:
            return finland()
        if self is SchoolLocationCountry.FRANCE:
            return france()
        if self is SchoolLocationCountry.FRENCH_GUIANA:
            return french_guiana()
        if self is SchoolLocationCountry.FRENCH_POLYNESIA:
            return french_polynesia()
        if self is SchoolLocationCountry.FRENCH_SOUTHERN_TERRITORIES:
            return french_southern_territories()
        if self is SchoolLocationCountry.GABON:
            return gabon()
        if self is SchoolLocationCountry.GAMBIA:
            return gambia()
        if self is SchoolLocationCountry.GEORGIA:
            return georgia()
        if self is SchoolLocationCountry.GERMANY:
            return germany()
        if self is SchoolLocationCountry.GHANA:
            return ghana()
        if self is SchoolLocationCountry.GIBRALTAR:
            return gibraltar()
        if self is SchoolLocationCountry.GREECE:
            return greece()
        if self is SchoolLocationCountry.GREENLAND:
            return greenland()
        if self is SchoolLocationCountry.GRENADA:
            return grenada()
        if self is SchoolLocationCountry.GUADELOUPE:
            return guadeloupe()
        if self is SchoolLocationCountry.GUAM:
            return guam()
        if self is SchoolLocationCountry.GUATEMALA:
            return guatemala()
        if self is SchoolLocationCountry.GUERNSEY:
            return guernsey()
        if self is SchoolLocationCountry.GUINEA:
            return guinea()
        if self is SchoolLocationCountry.GUINEA_BISSAU:
            return guinea_bissau()
        if self is SchoolLocationCountry.GUYANA:
            return guyana()
        if self is SchoolLocationCountry.HAITI:
            return haiti()
        if self is SchoolLocationCountry.HEARD_ISLAND_AND_MCDONALD_ISLANDS:
            return heard_island_and_mcdonald_islands()
        if self is SchoolLocationCountry.HONDURAS:
            return honduras()
        if self is SchoolLocationCountry.HONG_KONG:
            return hong_kong()
        if self is SchoolLocationCountry.HUNGARY:
            return hungary()
        if self is SchoolLocationCountry.ICELAND:
            return iceland()
        if self is SchoolLocationCountry.INDIA:
            return india()
        if self is SchoolLocationCountry.INDONESIA:
            return indonesia()
        if self is SchoolLocationCountry.IRAN:
            return iran()
        if self is SchoolLocationCountry.IRAQ:
            return iraq()
        if self is SchoolLocationCountry.IRELAND:
            return ireland()
        if self is SchoolLocationCountry.ISLE_OF_MAN:
            return isle_of_man()
        if self is SchoolLocationCountry.ISRAEL:
            return israel()
        if self is SchoolLocationCountry.ITALY:
            return italy()
        if self is SchoolLocationCountry.IVORY_COAST:
            return ivory_coast()
        if self is SchoolLocationCountry.JAMAICA:
            return jamaica()
        if self is SchoolLocationCountry.JAPAN:
            return japan()
        if self is SchoolLocationCountry.JERSEY:
            return jersey()
        if self is SchoolLocationCountry.JORDAN:
            return jordan()
        if self is SchoolLocationCountry.KAZAKHSTAN:
            return kazakhstan()
        if self is SchoolLocationCountry.KENYA:
            return kenya()
        if self is SchoolLocationCountry.KIRIBATI:
            return kiribati()
        if self is SchoolLocationCountry.KOSOVO:
            return kosovo()
        if self is SchoolLocationCountry.KUWAIT:
            return kuwait()
        if self is SchoolLocationCountry.KYRGYZSTAN:
            return kyrgyzstan()
        if self is SchoolLocationCountry.LAOS:
            return laos()
        if self is SchoolLocationCountry.LATVIA:
            return latvia()
        if self is SchoolLocationCountry.LEBANON:
            return lebanon()
        if self is SchoolLocationCountry.LESOTHO:
            return lesotho()
        if self is SchoolLocationCountry.LIBERIA:
            return liberia()
        if self is SchoolLocationCountry.LIBYA:
            return libya()
        if self is SchoolLocationCountry.LIECHTENSTEIN:
            return liechtenstein()
        if self is SchoolLocationCountry.LITHUANIA:
            return lithuania()
        if self is SchoolLocationCountry.LUXEMBOURG:
            return luxembourg()
        if self is SchoolLocationCountry.MACAU:
            return macau()
        if self is SchoolLocationCountry.MACEDONIA:
            return macedonia()
        if self is SchoolLocationCountry.MADAGASCAR:
            return madagascar()
        if self is SchoolLocationCountry.MALAWI:
            return malawi()
        if self is SchoolLocationCountry.MALAYSIA:
            return malaysia()
        if self is SchoolLocationCountry.MALDIVES:
            return maldives()
        if self is SchoolLocationCountry.MALI:
            return mali()
        if self is SchoolLocationCountry.MALTA:
            return malta()
        if self is SchoolLocationCountry.MARSHALL_ISLANDS:
            return marshall_islands()
        if self is SchoolLocationCountry.MARTINIQUE:
            return martinique()
        if self is SchoolLocationCountry.MAURITANIA:
            return mauritania()
        if self is SchoolLocationCountry.MAURITIUS:
            return mauritius()
        if self is SchoolLocationCountry.MAYOTTE:
            return mayotte()
        if self is SchoolLocationCountry.MEXICO:
            return mexico()
        if self is SchoolLocationCountry.MICRONESIA:
            return micronesia()
        if self is SchoolLocationCountry.MOLDOVA:
            return moldova()
        if self is SchoolLocationCountry.MONACO:
            return monaco()
        if self is SchoolLocationCountry.MONGOLIA:
            return mongolia()
        if self is SchoolLocationCountry.MONTENEGRO:
            return montenegro()
        if self is SchoolLocationCountry.MONTSERRAT:
            return montserrat()
        if self is SchoolLocationCountry.MOROCCO:
            return morocco()
        if self is SchoolLocationCountry.MOZAMBIQUE:
            return mozambique()
        if self is SchoolLocationCountry.MYANMAR:
            return myanmar()
        if self is SchoolLocationCountry.NAMIBIA:
            return namibia()
        if self is SchoolLocationCountry.NAURU:
            return nauru()
        if self is SchoolLocationCountry.NEPAL:
            return nepal()
        if self is SchoolLocationCountry.NETHERLANDS:
            return netherlands()
        if self is SchoolLocationCountry.NETHERLANDS_ANTILLES:
            return netherlands_antilles()
        if self is SchoolLocationCountry.NEW_CALEDONIA:
            return new_caledonia()
        if self is SchoolLocationCountry.NEW_ZEALAND:
            return new_zealand()
        if self is SchoolLocationCountry.NICARAGUA:
            return nicaragua()
        if self is SchoolLocationCountry.NIGER:
            return niger()
        if self is SchoolLocationCountry.NIGERIA:
            return nigeria()
        if self is SchoolLocationCountry.NIUE:
            return niue()
        if self is SchoolLocationCountry.NORFOLK_ISLAND:
            return norfolk_island()
        if self is SchoolLocationCountry.NORTH_KOREA:
            return north_korea()
        if self is SchoolLocationCountry.NORTHERN_MARIANA_ISLANDS:
            return northern_mariana_islands()
        if self is SchoolLocationCountry.NORWAY:
            return norway()
        if self is SchoolLocationCountry.OMAN:
            return oman()
        if self is SchoolLocationCountry.PAKISTAN:
            return pakistan()
        if self is SchoolLocationCountry.PALAU:
            return palau()
        if self is SchoolLocationCountry.PALESTINE:
            return palestine()
        if self is SchoolLocationCountry.PANAMA:
            return panama()
        if self is SchoolLocationCountry.PAPUA_NEW_GUINEA:
            return papua_new_guinea()
        if self is SchoolLocationCountry.PARAGUAY:
            return paraguay()
        if self is SchoolLocationCountry.PERU:
            return peru()
        if self is SchoolLocationCountry.PHILIPPINES:
            return philippines()
        if self is SchoolLocationCountry.PITCAIRN:
            return pitcairn()
        if self is SchoolLocationCountry.POLAND:
            return poland()
        if self is SchoolLocationCountry.PORTUGAL:
            return portugal()
        if self is SchoolLocationCountry.PUERTO_RICO:
            return puerto_rico()
        if self is SchoolLocationCountry.QATAR:
            return qatar()
        if self is SchoolLocationCountry.REPUBLIC_OF_THE_CONGO:
            return republic_of_the_congo()
        if self is SchoolLocationCountry.ROMANIA:
            return romania()
        if self is SchoolLocationCountry.RUSSIA:
            return russia()
        if self is SchoolLocationCountry.RWANDA:
            return rwanda()
        if self is SchoolLocationCountry.REUNION:
            return reunion()
        if self is SchoolLocationCountry.SAINT_BARTHELEMY:
            return saint_barthelemy()
        if self is SchoolLocationCountry.SAINT_HELENA:
            return saint_helena()
        if self is SchoolLocationCountry.SAINT_KITTS_AND_NEVIS:
            return saint_kitts_and_nevis()
        if self is SchoolLocationCountry.SAINT_LUCIA:
            return saint_lucia()
        if self is SchoolLocationCountry.SAINT_MARTIN:
            return saint_martin()
        if self is SchoolLocationCountry.SAINT_PIERRE_AND_MIQUELON:
            return saint_pierre_and_miquelon()
        if self is SchoolLocationCountry.SAINT_VINCENT_AND_THE_GRENADINES:
            return saint_vincent_and_the_grenadines()
        if self is SchoolLocationCountry.SAMOA:
            return samoa()
        if self is SchoolLocationCountry.SAN_MARINO:
            return san_marino()
        if self is SchoolLocationCountry.SAUDI_ARABIA:
            return saudi_arabia()
        if self is SchoolLocationCountry.SENEGAL:
            return senegal()
        if self is SchoolLocationCountry.SERBIA:
            return serbia()
        if self is SchoolLocationCountry.SEYCHELLES:
            return seychelles()
        if self is SchoolLocationCountry.SIERRA_LEONE:
            return sierra_leone()
        if self is SchoolLocationCountry.SINGAPORE:
            return singapore()
        if self is SchoolLocationCountry.SINT_MAARTEN:
            return sint_maarten()
        if self is SchoolLocationCountry.SLOVAKIA:
            return slovakia()
        if self is SchoolLocationCountry.SLOVENIA:
            return slovenia()
        if self is SchoolLocationCountry.SOLOMON_ISLANDS:
            return solomon_islands()
        if self is SchoolLocationCountry.SOMALIA:
            return somalia()
        if self is SchoolLocationCountry.SOUTH_AFRICA:
            return south_africa()
        if self is SchoolLocationCountry.SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS:
            return south_georgia_and_the_south_sandwich_islands()
        if self is SchoolLocationCountry.SOUTH_KOREA:
            return south_korea()
        if self is SchoolLocationCountry.SOUTH_SUDAN:
            return south_sudan()
        if self is SchoolLocationCountry.SPAIN:
            return spain()
        if self is SchoolLocationCountry.SRI_LANKA:
            return sri_lanka()
        if self is SchoolLocationCountry.SUDAN:
            return sudan()
        if self is SchoolLocationCountry.SURINAME:
            return suriname()
        if self is SchoolLocationCountry.SVALBARD_AND_JAN_MAYEN:
            return svalbard_and_jan_mayen()
        if self is SchoolLocationCountry.SWAZILAND:
            return swaziland()
        if self is SchoolLocationCountry.SWEDEN:
            return sweden()
        if self is SchoolLocationCountry.SWITZERLAND:
            return switzerland()
        if self is SchoolLocationCountry.SYRIA:
            return syria()
        if self is SchoolLocationCountry.SAO_TOME_AND_PRINCIPE:
            return sao_tome_and_principe()
        if self is SchoolLocationCountry.TAIWAN:
            return taiwan()
        if self is SchoolLocationCountry.TAJIKISTAN:
            return tajikistan()
        if self is SchoolLocationCountry.TANZANIA:
            return tanzania()
        if self is SchoolLocationCountry.THAILAND:
            return thailand()
        if self is SchoolLocationCountry.TIMOR_LESTE:
            return timor_leste()
        if self is SchoolLocationCountry.TOGO:
            return togo()
        if self is SchoolLocationCountry.TOKELAU:
            return tokelau()
        if self is SchoolLocationCountry.TONGA:
            return tonga()
        if self is SchoolLocationCountry.TRINIDAD_AND_TOBAGO:
            return trinidad_and_tobago()
        if self is SchoolLocationCountry.TUNISIA:
            return tunisia()
        if self is SchoolLocationCountry.TURKEY:
            return turkey()
        if self is SchoolLocationCountry.TURKMENISTAN:
            return turkmenistan()
        if self is SchoolLocationCountry.TURKS_AND_CAICOS_ISLANDS:
            return turks_and_caicos_islands()
        if self is SchoolLocationCountry.TUVALU:
            return tuvalu()
        if self is SchoolLocationCountry.US_VIRGIN_ISLANDS:
            return us_virgin_islands()
        if self is SchoolLocationCountry.UGANDA:
            return uganda()
        if self is SchoolLocationCountry.UKRAINE:
            return ukraine()
        if self is SchoolLocationCountry.UNITED_ARAB_EMIRATES:
            return united_arab_emirates()
        if self is SchoolLocationCountry.UNITED_KINGDOM:
            return united_kingdom()
        if self is SchoolLocationCountry.UNITED_STATES:
            return united_states()
        if self is SchoolLocationCountry.UNITED_STATES_MINOR_OUTLYING_ISLANDS:
            return united_states_minor_outlying_islands()
        if self is SchoolLocationCountry.URUGUAY:
            return uruguay()
        if self is SchoolLocationCountry.UZBEKISTAN:
            return uzbekistan()
        if self is SchoolLocationCountry.VANUATU:
            return vanuatu()
        if self is SchoolLocationCountry.VATICAN_CITY:
            return vatican_city()
        if self is SchoolLocationCountry.VENEZUELA:
            return venezuela()
        if self is SchoolLocationCountry.VIETNAM:
            return vietnam()
        if self is SchoolLocationCountry.WALLIS_AND_FUTUNA:
            return wallis_and_futuna()
        if self is SchoolLocationCountry.WESTERN_SAHARA:
            return western_sahara()
        if self is SchoolLocationCountry.YEMEN:
            return yemen()
        if self is SchoolLocationCountry.ZAMBIA:
            return zambia()
        if self is SchoolLocationCountry.ZIMBABWE:
            return zimbabwe()
        if self is SchoolLocationCountry.ALAND_ISLANDS:
            return aland_islands()
