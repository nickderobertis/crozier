

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExperienceCompanyLocationMetro(enum.StrEnum):
    """
    Company metro area
    """

    ABILENE_TEXAS = "abilene, texas"
    AKRON_OHIO = "akron, ohio"
    ALBANY_GEORGIA = "albany, georgia"
    ALBANY_NEW_YORK = "albany, new york"
    ALBANY_OREGON = "albany, oregon"
    ALBUQUERQUE_NEW_MEXICO = "albuquerque, new mexico"
    ALEXANDRIA_LOUISIANA = "alexandria, louisiana"
    ALLENTOWN_PENNSYLVANIA = "allentown, pennsylvania"
    ALTOONA_PENNSYLVANIA = "altoona, pennsylvania"
    AMARILLO_TEXAS = "amarillo, texas"
    AMES_IOWA = "ames, iowa"
    ANCHORAGE_ALASKA = "anchorage, alaska"
    ANN_ARBOR_MICHIGAN = "ann arbor, michigan"
    ANNISTON_ALABAMA = "anniston, alabama"
    APPLETON_WISCONSIN = "appleton, wisconsin"
    ASHEVILLE_NORTH_CAROLINA = "asheville, north carolina"
    ATHENS_GEORGIA = "athens, georgia"
    ATLANTA_GEORGIA = "atlanta, georgia"
    ATLANTIC_CITY_NEW_JERSEY = "atlantic city, new jersey"
    AUBURN_ALABAMA = "auburn, alabama"
    AUGUSTA_GEORGIA = "augusta, georgia"
    AUSTIN_TEXAS = "austin, texas"
    BAKERSFIELD_CALIFORNIA = "bakersfield, california"
    BALTIMORE_MARYLAND = "baltimore, maryland"
    BANGOR_MAINE = "bangor, maine"
    BARNSTABLE_TOWN_MASSACHUSETTS = "barnstable town, massachusetts"
    BATON_ROUGE_LOUISIANA = "baton rouge, louisiana"
    BATTLE_CREEK_MICHIGAN = "battle creek, michigan"
    BAY_CITY_MICHIGAN = "bay city, michigan"
    BEAUMONT_TEXAS = "beaumont, texas"
    BELLINGHAM_WASHINGTON = "bellingham, washington"
    BILLINGS_MONTANA = "billings, montana"
    BINGHAMTON_NEW_YORK = "binghamton, new york"
    BIRMINGHAM_ALABAMA = "birmingham, alabama"
    BISMARCK_NORTH_DAKOTA = "bismarck, north dakota"
    BLACKSBURG_VIRGINIA = "blacksburg, virginia"
    BLOOMINGTON_ILLINOIS = "bloomington, illinois"
    BLOOMINGTON_INDIANA = "bloomington, indiana"
    BOISE_CITY_IDAHO = "boise city, idaho"
    BOSTON_MASSACHUSETTS = "boston, massachusetts"
    BOULDER_COLORADO = "boulder, colorado"
    BOWLING_GREEN_KENTUCKY = "bowling green, kentucky"
    BREMERTON_WASHINGTON = "bremerton, washington"
    BRIDGEPORT_CONNECTICUT = "bridgeport, connecticut"
    BROWNSVILLE_TEXAS = "brownsville, texas"
    BUFFALO_NEW_YORK = "buffalo, new york"
    BURLINGTON_NORTH_CAROLINA = "burlington, north carolina"
    BURLINGTON_VERMONT = "burlington, vermont"
    CANTON_OHIO = "canton, ohio"
    CAPE_CORAL_FLORIDA = "cape coral, florida"
    CAPE_GIRARDEAU_MISSOURI = "cape girardeau, missouri"
    CARBONDALE_ILLINOIS = "carbondale, illinois"
    CARSON_CITY_NEVADA = "carson city, nevada"
    CASPER_WYOMING = "casper, wyoming"
    CEDAR_RAPIDS_IOWA = "cedar rapids, iowa"
    CHAMPAIGN_ILLINOIS = "champaign, illinois"
    CHARLESTON_SOUTH_CAROLINA = "charleston, south carolina"
    CHARLESTON_WEST_VIRGINIA = "charleston, west virginia"
    CHARLOTTE_NORTH_CAROLINA = "charlotte, north carolina"
    CHARLOTTESVILLE_VIRGINIA = "charlottesville, virginia"
    CHATTANOOGA_TENNESSEE = "chattanooga, tennessee"
    CHEYENNE_WYOMING = "cheyenne, wyoming"
    CHICAGO_ILLINOIS = "chicago, illinois"
    CHICO_CALIFORNIA = "chico, california"
    CINCINNATI_OHIO = "cincinnati, ohio"
    CLARKSVILLE_TENNESSEE = "clarksville, tennessee"
    CLEVELAND_OHIO = "cleveland, ohio"
    CLEVELAND_TENNESSEE = "cleveland, tennessee"
    COEUR_DALENE_IDAHO = "coeur d'alene, idaho"
    COLLEGE_STATION_TEXAS = "college station, texas"
    COLORADO_SPRINGS_COLORADO = "colorado springs, colorado"
    COLUMBIA_MISSOURI = "columbia, missouri"
    COLUMBIA_SOUTH_CAROLINA = "columbia, south carolina"
    COLUMBUS_GEORGIA = "columbus, georgia"
    COLUMBUS_INDIANA = "columbus, indiana"
    COLUMBUS_OHIO = "columbus, ohio"
    CORPUS_CHRISTI_TEXAS = "corpus christi, texas"
    CORVALLIS_OREGON = "corvallis, oregon"
    CRESTVIEW_FLORIDA = "crestview, florida"
    CUMBERLAND_MARYLAND = "cumberland, maryland"
    DALLAS_TEXAS = "dallas, texas"
    DALTON_GEORGIA = "dalton, georgia"
    DANVILLE_ILLINOIS = "danville, illinois"
    DAVENPORT_IOWA = "davenport, iowa"
    DAYTON_OHIO = "dayton, ohio"
    DECATUR_ALABAMA = "decatur, alabama"
    DECATUR_ILLINOIS = "decatur, illinois"
    DELTONA_FLORIDA = "deltona, florida"
    DENVER_COLORADO = "denver, colorado"
    DES_MOINES_IOWA = "des moines, iowa"
    DETROIT_MICHIGAN = "detroit, michigan"
    DISTRICT_OF_COLUMBIA = "district of columbia"
    DOTHAN_ALABAMA = "dothan, alabama"
    DOVER_DELAWARE = "dover, delaware"
    DUBUQUE_IOWA = "dubuque, iowa"
    DULUTH_MINNESOTA = "duluth, minnesota"
    DURHAM_NORTH_CAROLINA = "durham, north carolina"
    EAU_CLAIRE_WISCONSIN = "eau claire, wisconsin"
    EL_CENTRO_CALIFORNIA = "el centro, california"
    EL_PASO_TEXAS = "el paso, texas"
    ELIZABETHTOWN_KENTUCKY = "elizabethtown, kentucky"
    ELKHART_INDIANA = "elkhart, indiana"
    ELMIRA_NEW_YORK = "elmira, new york"
    ENID_OKLAHOMA = "enid, oklahoma"
    ERIE_PENNSYLVANIA = "erie, pennsylvania"
    EUGENE_OREGON = "eugene, oregon"
    EVANSVILLE_INDIANA = "evansville, indiana"
    FAIRBANKS_ALASKA = "fairbanks, alaska"
    FARGO_NORTH_DAKOTA = "fargo, north dakota"
    FARMINGTON_NEW_MEXICO = "farmington, new mexico"
    FAYETTEVILLE_ARKANSAS = "fayetteville, arkansas"
    FAYETTEVILLE_NORTH_CAROLINA = "fayetteville, north carolina"
    FLAGSTAFF_ARIZONA = "flagstaff, arizona"
    FLINT_MICHIGAN = "flint, michigan"
    FLORENCE_ALABAMA = "florence, alabama"
    FLORENCE_SOUTH_CAROLINA = "florence, south carolina"
    FOND_DU_LAC_WISCONSIN = "fond du lac, wisconsin"
    FORT_COLLINS_COLORADO = "fort collins, colorado"
    FORT_SMITH_ARKANSAS = "fort smith, arkansas"
    FORT_WAYNE_INDIANA = "fort wayne, indiana"
    FRESNO_CALIFORNIA = "fresno, california"
    GADSDEN_ALABAMA = "gadsden, alabama"
    GAINESVILLE_FLORIDA = "gainesville, florida"
    GAINESVILLE_GEORGIA = "gainesville, georgia"
    GOLDSBORO_NORTH_CAROLINA = "goldsboro, north carolina"
    GRAND_FORKS_NORTH_DAKOTA = "grand forks, north dakota"
    GRAND_ISLAND_NEBRASKA = "grand island, nebraska"
    GRAND_JUNCTION_COLORADO = "grand junction, colorado"
    GRAND_RAPIDS_MICHIGAN = "grand rapids, michigan"
    GRANTS_PASS_OREGON = "grants pass, oregon"
    GREAT_FALLS_MONTANA = "great falls, montana"
    GREELEY_COLORADO = "greeley, colorado"
    GREEN_BAY_WISCONSIN = "green bay, wisconsin"
    GREENSBORO_NORTH_CAROLINA = "greensboro, north carolina"
    GREENVILLE_NORTH_CAROLINA = "greenville, north carolina"
    GREENVILLE_SOUTH_CAROLINA = "greenville, south carolina"
    GULFPORT_MISSISSIPPI = "gulfport, mississippi"
    HAGERSTOWN_MARYLAND = "hagerstown, maryland"
    HANFORD_CALIFORNIA = "hanford, california"
    HARRISBURG_PENNSYLVANIA = "harrisburg, pennsylvania"
    HARRISONBURG_VIRGINIA = "harrisonburg, virginia"
    HARTFORD_CONNECTICUT = "hartford, connecticut"
    HATTIESBURG_MISSISSIPPI = "hattiesburg, mississippi"
    HICKORY_NORTH_CAROLINA = "hickory, north carolina"
    HILTON_HEAD_ISLAND_SOUTH_CAROLINA = "hilton head island, south carolina"
    HINESVILLE_GEORGIA = "hinesville, georgia"
    HOT_SPRINGS_ARKANSAS = "hot springs, arkansas"
    HOUMA_LOUISIANA = "houma, louisiana"
    HOUSTON_TEXAS = "houston, texas"
    HUNTINGTON_WEST_VIRGINIA = "huntington, west virginia"
    HUNTSVILLE_ALABAMA = "huntsville, alabama"
    IDAHO_FALLS_IDAHO = "idaho falls, idaho"
    INDIANAPOLIS_INDIANA = "indianapolis, indiana"
    IOWA_CITY_IOWA = "iowa city, iowa"
    ITHACA_NEW_YORK = "ithaca, new york"
    JACKSON_MICHIGAN = "jackson, michigan"
    JACKSON_MISSISSIPPI = "jackson, mississippi"
    JACKSON_TENNESSEE = "jackson, tennessee"
    JACKSONVILLE_FLORIDA = "jacksonville, florida"
    JACKSONVILLE_NORTH_CAROLINA = "jacksonville, north carolina"
    JANESVILLE_WISCONSIN = "janesville, wisconsin"
    JEFFERSON_CITY_MISSOURI = "jefferson city, missouri"
    JOHNSON_CITY_TENNESSEE = "johnson city, tennessee"
    JOHNSTOWN_PENNSYLVANIA = "johnstown, pennsylvania"
    JONESBORO_ARKANSAS = "jonesboro, arkansas"
    JOPLIN_MISSOURI = "joplin, missouri"
    KAHULUI_HAWAII = "kahului, hawaii"
    KALAMAZOO_MICHIGAN = "kalamazoo, michigan"
    KANKAKEE_ILLINOIS = "kankakee, illinois"
    KANSAS_CITY_MISSOURI = "kansas city, missouri"
    KENNEWICK_WASHINGTON = "kennewick, washington"
    KILLEEN_TEXAS = "killeen, texas"
    KINGSPORT_TENNESSEE = "kingsport, tennessee"
    KINGSTON_NEW_YORK = "kingston, new york"
    KNOXVILLE_TENNESSEE = "knoxville, tennessee"
    KOKOMO_INDIANA = "kokomo, indiana"
    LA_CROSSE_WISCONSIN = "la crosse, wisconsin"
    LAFAYETTE_INDIANA = "lafayette, indiana"
    LAFAYETTE_LOUISIANA = "lafayette, louisiana"
    LAKE_CHARLES_LOUISIANA = "lake charles, louisiana"
    LAKE_HAVASU_CITY_ARIZONA = "lake havasu city, arizona"
    LAKELAND_FLORIDA = "lakeland, florida"
    LANCASTER_PENNSYLVANIA = "lancaster, pennsylvania"
    LANSING_MICHIGAN = "lansing, michigan"
    LAREDO_TEXAS = "laredo, texas"
    LAS_CRUCES_NEW_MEXICO = "las cruces, new mexico"
    LAS_VEGAS_NEVADA = "las vegas, nevada"
    LAWRENCE_KANSAS = "lawrence, kansas"
    LAWTON_OKLAHOMA = "lawton, oklahoma"
    LEBANON_PENNSYLVANIA = "lebanon, pennsylvania"
    LEWISTON_IDAHO = "lewiston, idaho"
    LEWISTON_MAINE = "lewiston, maine"
    LEXINGTON_KENTUCKY = "lexington, kentucky"
    LIMA_OHIO = "lima, ohio"
    LINCOLN_NEBRASKA = "lincoln, nebraska"
    LITTLE_ROCK_ARKANSAS = "little rock, arkansas"
    LOGAN_UTAH = "logan, utah"
    LONGVIEW_TEXAS = "longview, texas"
    LONGVIEW_WASHINGTON = "longview, washington"
    LOS_ANGELES_CALIFORNIA = "los angeles, california"
    LOUISVILLE_KENTUCKY = "louisville, kentucky"
    LUBBOCK_TEXAS = "lubbock, texas"
    LYNCHBURG_VIRGINIA = "lynchburg, virginia"
    MACON_GEORGIA = "macon, georgia"
    MADERA_CALIFORNIA = "madera, california"
    MADISON_WISCONSIN = "madison, wisconsin"
    MANCHESTER_NEW_HAMPSHIRE = "manchester, new hampshire"
    MANHATTAN_KANSAS = "manhattan, kansas"
    MANKATO_MINNESOTA = "mankato, minnesota"
    MANSFIELD_OHIO = "mansfield, ohio"
    MCALLEN_TEXAS = "mcallen, texas"
    MEDFORD_OREGON = "medford, oregon"
    MEMPHIS_TENNESSEE = "memphis, tennessee"
    MERCED_CALIFORNIA = "merced, california"
    MIAMI_FLORIDA = "miami, florida"
    MICHIGAN_CITY_INDIANA = "michigan city, indiana"
    MIDLAND_MICHIGAN = "midland, michigan"
    MIDLAND_TEXAS = "midland, texas"
    MILWAUKEE_WISCONSIN = "milwaukee, wisconsin"
    MINNEAPOLIS_MINNESOTA = "minneapolis, minnesota"
    MISSOULA_MONTANA = "missoula, montana"
    MOBILE_ALABAMA = "mobile, alabama"
    MODESTO_CALIFORNIA = "modesto, california"
    MONROE_LOUISIANA = "monroe, louisiana"
    MONROE_MICHIGAN = "monroe, michigan"
    MONTGOMERY_ALABAMA = "montgomery, alabama"
    MORGANTOWN_WEST_VIRGINIA = "morgantown, west virginia"
    MORRISTOWN_TENNESSEE = "morristown, tennessee"
    MOUNT_VERNON_WASHINGTON = "mount vernon, washington"
    MUNCIE_INDIANA = "muncie, indiana"
    MUSKEGON_MICHIGAN = "muskegon, michigan"
    MYRTLE_BEACH_SOUTH_CAROLINA = "myrtle beach, south carolina"
    NAPA_CALIFORNIA = "napa, california"
    NAPLES_FLORIDA = "naples, florida"
    NASHVILLE_TENNESSEE = "nashville, tennessee"
    NEW_BERN_NORTH_CAROLINA = "new bern, north carolina"
    NEW_HAVEN_CONNECTICUT = "new haven, connecticut"
    NEW_ORLEANS_LOUISIANA = "new orleans, louisiana"
    NEW_YORK_NEW_YORK = "new york, new york"
    NORTH_PORT_FLORIDA = "north port, florida"
    NORWICH_CONNECTICUT = "norwich, connecticut"
    OCALA_FLORIDA = "ocala, florida"
    ODESSA_TEXAS = "odessa, texas"
    OGDEN_UTAH = "ogden, utah"
    OKLAHOMA_CITY_OKLAHOMA = "oklahoma city, oklahoma"
    OLYMPIA_WASHINGTON = "olympia, washington"
    OMAHA_NEBRASKA = "omaha, nebraska"
    ORLANDO_FLORIDA = "orlando, florida"
    OSHKOSH_WISCONSIN = "oshkosh, wisconsin"
    OWENSBORO_KENTUCKY = "owensboro, kentucky"
    OXNARD_CALIFORNIA = "oxnard, california"
    PALM_BAY_FLORIDA = "palm bay, florida"
    PANAMA_CITY_FLORIDA = "panama city, florida"
    PARKERSBURG_WEST_VIRGINIA = "parkersburg, west virginia"
    PENSACOLA_FLORIDA = "pensacola, florida"
    PEORIA_ILLINOIS = "peoria, illinois"
    PHILADELPHIA_PENNSYLVANIA = "philadelphia, pennsylvania"
    PHOENIX_ARIZONA = "phoenix, arizona"
    PINE_BLUFF_ARKANSAS = "pine bluff, arkansas"
    PITTSBURGH_PENNSYLVANIA = "pittsburgh, pennsylvania"
    PITTSFIELD_MASSACHUSETTS = "pittsfield, massachusetts"
    POCATELLO_IDAHO = "pocatello, idaho"
    PORT_ST_LUCIE_FLORIDA = "port st. lucie, florida"
    PORTLAND_MAINE = "portland, maine"
    PORTLAND_OREGON = "portland, oregon"
    POUGHKEEPSIE_NEW_YORK = "poughkeepsie, new york"
    PRESCOTT_VALLEY_ARIZONA = "prescott valley, arizona"
    PROVIDENCE_RHODE_ISLAND = "providence, rhode island"
    PROVO_UTAH = "provo, utah"
    PUEBLO_COLORADO = "pueblo, colorado"
    PUNTA_GORDA_FLORIDA = "punta gorda, florida"
    RACINE_WISCONSIN = "racine, wisconsin"
    RALEIGH_NORTH_CAROLINA = "raleigh, north carolina"
    RAPID_CITY_SOUTH_DAKOTA = "rapid city, south dakota"
    READING_PENNSYLVANIA = "reading, pennsylvania"
    REDDING_CALIFORNIA = "redding, california"
    RENO_NEVADA = "reno, nevada"
    RICHMOND_VIRGINIA = "richmond, virginia"
    RIVERSIDE_CALIFORNIA = "riverside, california"
    ROANOKE_VIRGINIA = "roanoke, virginia"
    ROCHESTER_MINNESOTA = "rochester, minnesota"
    ROCHESTER_NEW_YORK = "rochester, new york"
    ROCKFORD_ILLINOIS = "rockford, illinois"
    ROCKY_MOUNT_NORTH_CAROLINA = "rocky mount, north carolina"
    ROME_GEORGIA = "rome, georgia"
    SACRAMENTO_CALIFORNIA = "sacramento, california"
    SAGINAW_MICHIGAN = "saginaw, michigan"
    SALEM_OREGON = "salem, oregon"
    SALINAS_CALIFORNIA = "salinas, california"
    SALISBURY_MARYLAND = "salisbury, maryland"
    SALT_LAKE_CITY_UTAH = "salt lake city, utah"
    SAN_ANGELO_TEXAS = "san angelo, texas"
    SAN_ANTONIO_TEXAS = "san antonio, texas"
    SAN_DIEGO_CALIFORNIA = "san diego, california"
    SAN_FRANCISCO_CALIFORNIA = "san francisco, california"
    SAN_JOSE_CALIFORNIA = "san jose, california"
    SAN_LUIS_OBISPO_CALIFORNIA = "san luis obispo, california"
    SANTA_CRUZ_CALIFORNIA = "santa cruz, california"
    SANTA_FE_NEW_MEXICO = "santa fe, new mexico"
    SANTA_MARIA_CALIFORNIA = "santa maria, california"
    SANTA_ROSA_CALIFORNIA = "santa rosa, california"
    SAVANNAH_GEORGIA = "savannah, georgia"
    SCRANTON_PENNSYLVANIA = "scranton, pennsylvania"
    SEATTLE_WASHINGTON = "seattle, washington"
    SEBASTIAN_FLORIDA = "sebastian, florida"
    SHEBOYGAN_WISCONSIN = "sheboygan, wisconsin"
    SHERMAN_TEXAS = "sherman, texas"
    SHREVEPORT_LOUISIANA = "shreveport, louisiana"
    SIERRA_VISTA_ARIZONA = "sierra vista, arizona"
    SIOUX_CITY_IOWA = "sioux city, iowa"
    SIOUX_FALLS_SOUTH_DAKOTA = "sioux falls, south dakota"
    SOUTH_BEND_INDIANA = "south bend, indiana"
    SPARTANBURG_SOUTH_CAROLINA = "spartanburg, south carolina"
    SPOKANE_WASHINGTON = "spokane, washington"
    SPRINGFIELD_ILLINOIS = "springfield, illinois"
    SPRINGFIELD_MASSACHUSETTS = "springfield, massachusetts"
    SPRINGFIELD_MISSOURI = "springfield, missouri"
    SPRINGFIELD_OHIO = "springfield, ohio"
    ST_CLOUD_MINNESOTA = "st. cloud, minnesota"
    ST_GEORGE_UTAH = "st. george, utah"
    ST_JOSEPH_MISSOURI = "st. joseph, missouri"
    ST_LOUIS_MISSOURI = "st. louis, missouri"
    STATE_COLLEGE_PENNSYLVANIA = "state college, pennsylvania"
    STAUNTON_VIRGINIA = "staunton, virginia"
    STOCKTON_CALIFORNIA = "stockton, california"
    SUMTER_SOUTH_CAROLINA = "sumter, south carolina"
    SYRACUSE_NEW_YORK = "syracuse, new york"
    TALLAHASSEE_FLORIDA = "tallahassee, florida"
    TAMPA_FLORIDA = "tampa, florida"
    TERRE_HAUTE_INDIANA = "terre haute, indiana"
    TEXARKANA_TEXAS = "texarkana, texas"
    TOLEDO_OHIO = "toledo, ohio"
    TOPEKA_KANSAS = "topeka, kansas"
    TRENTON_NEW_JERSEY = "trenton, new jersey"
    TUCSON_ARIZONA = "tucson, arizona"
    TULSA_OKLAHOMA = "tulsa, oklahoma"
    TUSCALOOSA_ALABAMA = "tuscaloosa, alabama"
    TWIN_FALLS_IDAHO = "twin falls, idaho"
    TYLER_TEXAS = "tyler, texas"
    URBAN_HONOLULU_HAWAII = "urban honolulu, hawaii"
    UTICA_NEW_YORK = "utica, new york"
    VALDOSTA_GEORGIA = "valdosta, georgia"
    VALLEJO_CALIFORNIA = "vallejo, california"
    VICTORIA_TEXAS = "victoria, texas"
    VINELAND_NEW_JERSEY = "vineland, new jersey"
    VIRGINIA_BEACH_VIRGINIA = "virginia beach, virginia"
    VISALIA_CALIFORNIA = "visalia, california"
    WACO_TEXAS = "waco, texas"
    WALLA_WALLA_WASHINGTON = "walla walla, washington"
    WARNER_ROBINS_GEORGIA = "warner robins, georgia"
    WATERLOO_IOWA = "waterloo, iowa"
    WATERTOWN_NEW_YORK = "watertown, new york"
    WAUSAU_WISCONSIN = "wausau, wisconsin"
    WEIRTON_WEST_VIRGINIA = "weirton, west virginia"
    WENATCHEE_WASHINGTON = "wenatchee, washington"
    WHEELING_WEST_VIRGINIA = "wheeling, west virginia"
    WICHITA_FALLS_TEXAS = "wichita falls, texas"
    WICHITA_KANSAS = "wichita, kansas"
    WILLIAMSPORT_PENNSYLVANIA = "williamsport, pennsylvania"
    WILMINGTON_NORTH_CAROLINA = "wilmington, north carolina"
    WINCHESTER_VIRGINIA = "winchester, virginia"
    WORCESTER_MASSACHUSETTS = "worcester, massachusetts"
    YAKIMA_WASHINGTON = "yakima, washington"
    YORK_PENNSYLVANIA = "york, pennsylvania"
    YOUNGSTOWN_OHIO = "youngstown, ohio"
    YUBA_CITY_CALIFORNIA = "yuba city, california"
    YUMA_ARIZONA = "yuma, arizona"

    def visit(
        self,
        abilene_texas: typing.Callable[[], T_Result],
        akron_ohio: typing.Callable[[], T_Result],
        albany_georgia: typing.Callable[[], T_Result],
        albany_new_york: typing.Callable[[], T_Result],
        albany_oregon: typing.Callable[[], T_Result],
        albuquerque_new_mexico: typing.Callable[[], T_Result],
        alexandria_louisiana: typing.Callable[[], T_Result],
        allentown_pennsylvania: typing.Callable[[], T_Result],
        altoona_pennsylvania: typing.Callable[[], T_Result],
        amarillo_texas: typing.Callable[[], T_Result],
        ames_iowa: typing.Callable[[], T_Result],
        anchorage_alaska: typing.Callable[[], T_Result],
        ann_arbor_michigan: typing.Callable[[], T_Result],
        anniston_alabama: typing.Callable[[], T_Result],
        appleton_wisconsin: typing.Callable[[], T_Result],
        asheville_north_carolina: typing.Callable[[], T_Result],
        athens_georgia: typing.Callable[[], T_Result],
        atlanta_georgia: typing.Callable[[], T_Result],
        atlantic_city_new_jersey: typing.Callable[[], T_Result],
        auburn_alabama: typing.Callable[[], T_Result],
        augusta_georgia: typing.Callable[[], T_Result],
        austin_texas: typing.Callable[[], T_Result],
        bakersfield_california: typing.Callable[[], T_Result],
        baltimore_maryland: typing.Callable[[], T_Result],
        bangor_maine: typing.Callable[[], T_Result],
        barnstable_town_massachusetts: typing.Callable[[], T_Result],
        baton_rouge_louisiana: typing.Callable[[], T_Result],
        battle_creek_michigan: typing.Callable[[], T_Result],
        bay_city_michigan: typing.Callable[[], T_Result],
        beaumont_texas: typing.Callable[[], T_Result],
        bellingham_washington: typing.Callable[[], T_Result],
        billings_montana: typing.Callable[[], T_Result],
        binghamton_new_york: typing.Callable[[], T_Result],
        birmingham_alabama: typing.Callable[[], T_Result],
        bismarck_north_dakota: typing.Callable[[], T_Result],
        blacksburg_virginia: typing.Callable[[], T_Result],
        bloomington_illinois: typing.Callable[[], T_Result],
        bloomington_indiana: typing.Callable[[], T_Result],
        boise_city_idaho: typing.Callable[[], T_Result],
        boston_massachusetts: typing.Callable[[], T_Result],
        boulder_colorado: typing.Callable[[], T_Result],
        bowling_green_kentucky: typing.Callable[[], T_Result],
        bremerton_washington: typing.Callable[[], T_Result],
        bridgeport_connecticut: typing.Callable[[], T_Result],
        brownsville_texas: typing.Callable[[], T_Result],
        buffalo_new_york: typing.Callable[[], T_Result],
        burlington_north_carolina: typing.Callable[[], T_Result],
        burlington_vermont: typing.Callable[[], T_Result],
        canton_ohio: typing.Callable[[], T_Result],
        cape_coral_florida: typing.Callable[[], T_Result],
        cape_girardeau_missouri: typing.Callable[[], T_Result],
        carbondale_illinois: typing.Callable[[], T_Result],
        carson_city_nevada: typing.Callable[[], T_Result],
        casper_wyoming: typing.Callable[[], T_Result],
        cedar_rapids_iowa: typing.Callable[[], T_Result],
        champaign_illinois: typing.Callable[[], T_Result],
        charleston_south_carolina: typing.Callable[[], T_Result],
        charleston_west_virginia: typing.Callable[[], T_Result],
        charlotte_north_carolina: typing.Callable[[], T_Result],
        charlottesville_virginia: typing.Callable[[], T_Result],
        chattanooga_tennessee: typing.Callable[[], T_Result],
        cheyenne_wyoming: typing.Callable[[], T_Result],
        chicago_illinois: typing.Callable[[], T_Result],
        chico_california: typing.Callable[[], T_Result],
        cincinnati_ohio: typing.Callable[[], T_Result],
        clarksville_tennessee: typing.Callable[[], T_Result],
        cleveland_ohio: typing.Callable[[], T_Result],
        cleveland_tennessee: typing.Callable[[], T_Result],
        coeur_dalene_idaho: typing.Callable[[], T_Result],
        college_station_texas: typing.Callable[[], T_Result],
        colorado_springs_colorado: typing.Callable[[], T_Result],
        columbia_missouri: typing.Callable[[], T_Result],
        columbia_south_carolina: typing.Callable[[], T_Result],
        columbus_georgia: typing.Callable[[], T_Result],
        columbus_indiana: typing.Callable[[], T_Result],
        columbus_ohio: typing.Callable[[], T_Result],
        corpus_christi_texas: typing.Callable[[], T_Result],
        corvallis_oregon: typing.Callable[[], T_Result],
        crestview_florida: typing.Callable[[], T_Result],
        cumberland_maryland: typing.Callable[[], T_Result],
        dallas_texas: typing.Callable[[], T_Result],
        dalton_georgia: typing.Callable[[], T_Result],
        danville_illinois: typing.Callable[[], T_Result],
        davenport_iowa: typing.Callable[[], T_Result],
        dayton_ohio: typing.Callable[[], T_Result],
        decatur_alabama: typing.Callable[[], T_Result],
        decatur_illinois: typing.Callable[[], T_Result],
        deltona_florida: typing.Callable[[], T_Result],
        denver_colorado: typing.Callable[[], T_Result],
        des_moines_iowa: typing.Callable[[], T_Result],
        detroit_michigan: typing.Callable[[], T_Result],
        district_of_columbia: typing.Callable[[], T_Result],
        dothan_alabama: typing.Callable[[], T_Result],
        dover_delaware: typing.Callable[[], T_Result],
        dubuque_iowa: typing.Callable[[], T_Result],
        duluth_minnesota: typing.Callable[[], T_Result],
        durham_north_carolina: typing.Callable[[], T_Result],
        eau_claire_wisconsin: typing.Callable[[], T_Result],
        el_centro_california: typing.Callable[[], T_Result],
        el_paso_texas: typing.Callable[[], T_Result],
        elizabethtown_kentucky: typing.Callable[[], T_Result],
        elkhart_indiana: typing.Callable[[], T_Result],
        elmira_new_york: typing.Callable[[], T_Result],
        enid_oklahoma: typing.Callable[[], T_Result],
        erie_pennsylvania: typing.Callable[[], T_Result],
        eugene_oregon: typing.Callable[[], T_Result],
        evansville_indiana: typing.Callable[[], T_Result],
        fairbanks_alaska: typing.Callable[[], T_Result],
        fargo_north_dakota: typing.Callable[[], T_Result],
        farmington_new_mexico: typing.Callable[[], T_Result],
        fayetteville_arkansas: typing.Callable[[], T_Result],
        fayetteville_north_carolina: typing.Callable[[], T_Result],
        flagstaff_arizona: typing.Callable[[], T_Result],
        flint_michigan: typing.Callable[[], T_Result],
        florence_alabama: typing.Callable[[], T_Result],
        florence_south_carolina: typing.Callable[[], T_Result],
        fond_du_lac_wisconsin: typing.Callable[[], T_Result],
        fort_collins_colorado: typing.Callable[[], T_Result],
        fort_smith_arkansas: typing.Callable[[], T_Result],
        fort_wayne_indiana: typing.Callable[[], T_Result],
        fresno_california: typing.Callable[[], T_Result],
        gadsden_alabama: typing.Callable[[], T_Result],
        gainesville_florida: typing.Callable[[], T_Result],
        gainesville_georgia: typing.Callable[[], T_Result],
        goldsboro_north_carolina: typing.Callable[[], T_Result],
        grand_forks_north_dakota: typing.Callable[[], T_Result],
        grand_island_nebraska: typing.Callable[[], T_Result],
        grand_junction_colorado: typing.Callable[[], T_Result],
        grand_rapids_michigan: typing.Callable[[], T_Result],
        grants_pass_oregon: typing.Callable[[], T_Result],
        great_falls_montana: typing.Callable[[], T_Result],
        greeley_colorado: typing.Callable[[], T_Result],
        green_bay_wisconsin: typing.Callable[[], T_Result],
        greensboro_north_carolina: typing.Callable[[], T_Result],
        greenville_north_carolina: typing.Callable[[], T_Result],
        greenville_south_carolina: typing.Callable[[], T_Result],
        gulfport_mississippi: typing.Callable[[], T_Result],
        hagerstown_maryland: typing.Callable[[], T_Result],
        hanford_california: typing.Callable[[], T_Result],
        harrisburg_pennsylvania: typing.Callable[[], T_Result],
        harrisonburg_virginia: typing.Callable[[], T_Result],
        hartford_connecticut: typing.Callable[[], T_Result],
        hattiesburg_mississippi: typing.Callable[[], T_Result],
        hickory_north_carolina: typing.Callable[[], T_Result],
        hilton_head_island_south_carolina: typing.Callable[[], T_Result],
        hinesville_georgia: typing.Callable[[], T_Result],
        hot_springs_arkansas: typing.Callable[[], T_Result],
        houma_louisiana: typing.Callable[[], T_Result],
        houston_texas: typing.Callable[[], T_Result],
        huntington_west_virginia: typing.Callable[[], T_Result],
        huntsville_alabama: typing.Callable[[], T_Result],
        idaho_falls_idaho: typing.Callable[[], T_Result],
        indianapolis_indiana: typing.Callable[[], T_Result],
        iowa_city_iowa: typing.Callable[[], T_Result],
        ithaca_new_york: typing.Callable[[], T_Result],
        jackson_michigan: typing.Callable[[], T_Result],
        jackson_mississippi: typing.Callable[[], T_Result],
        jackson_tennessee: typing.Callable[[], T_Result],
        jacksonville_florida: typing.Callable[[], T_Result],
        jacksonville_north_carolina: typing.Callable[[], T_Result],
        janesville_wisconsin: typing.Callable[[], T_Result],
        jefferson_city_missouri: typing.Callable[[], T_Result],
        johnson_city_tennessee: typing.Callable[[], T_Result],
        johnstown_pennsylvania: typing.Callable[[], T_Result],
        jonesboro_arkansas: typing.Callable[[], T_Result],
        joplin_missouri: typing.Callable[[], T_Result],
        kahului_hawaii: typing.Callable[[], T_Result],
        kalamazoo_michigan: typing.Callable[[], T_Result],
        kankakee_illinois: typing.Callable[[], T_Result],
        kansas_city_missouri: typing.Callable[[], T_Result],
        kennewick_washington: typing.Callable[[], T_Result],
        killeen_texas: typing.Callable[[], T_Result],
        kingsport_tennessee: typing.Callable[[], T_Result],
        kingston_new_york: typing.Callable[[], T_Result],
        knoxville_tennessee: typing.Callable[[], T_Result],
        kokomo_indiana: typing.Callable[[], T_Result],
        la_crosse_wisconsin: typing.Callable[[], T_Result],
        lafayette_indiana: typing.Callable[[], T_Result],
        lafayette_louisiana: typing.Callable[[], T_Result],
        lake_charles_louisiana: typing.Callable[[], T_Result],
        lake_havasu_city_arizona: typing.Callable[[], T_Result],
        lakeland_florida: typing.Callable[[], T_Result],
        lancaster_pennsylvania: typing.Callable[[], T_Result],
        lansing_michigan: typing.Callable[[], T_Result],
        laredo_texas: typing.Callable[[], T_Result],
        las_cruces_new_mexico: typing.Callable[[], T_Result],
        las_vegas_nevada: typing.Callable[[], T_Result],
        lawrence_kansas: typing.Callable[[], T_Result],
        lawton_oklahoma: typing.Callable[[], T_Result],
        lebanon_pennsylvania: typing.Callable[[], T_Result],
        lewiston_idaho: typing.Callable[[], T_Result],
        lewiston_maine: typing.Callable[[], T_Result],
        lexington_kentucky: typing.Callable[[], T_Result],
        lima_ohio: typing.Callable[[], T_Result],
        lincoln_nebraska: typing.Callable[[], T_Result],
        little_rock_arkansas: typing.Callable[[], T_Result],
        logan_utah: typing.Callable[[], T_Result],
        longview_texas: typing.Callable[[], T_Result],
        longview_washington: typing.Callable[[], T_Result],
        los_angeles_california: typing.Callable[[], T_Result],
        louisville_kentucky: typing.Callable[[], T_Result],
        lubbock_texas: typing.Callable[[], T_Result],
        lynchburg_virginia: typing.Callable[[], T_Result],
        macon_georgia: typing.Callable[[], T_Result],
        madera_california: typing.Callable[[], T_Result],
        madison_wisconsin: typing.Callable[[], T_Result],
        manchester_new_hampshire: typing.Callable[[], T_Result],
        manhattan_kansas: typing.Callable[[], T_Result],
        mankato_minnesota: typing.Callable[[], T_Result],
        mansfield_ohio: typing.Callable[[], T_Result],
        mcallen_texas: typing.Callable[[], T_Result],
        medford_oregon: typing.Callable[[], T_Result],
        memphis_tennessee: typing.Callable[[], T_Result],
        merced_california: typing.Callable[[], T_Result],
        miami_florida: typing.Callable[[], T_Result],
        michigan_city_indiana: typing.Callable[[], T_Result],
        midland_michigan: typing.Callable[[], T_Result],
        midland_texas: typing.Callable[[], T_Result],
        milwaukee_wisconsin: typing.Callable[[], T_Result],
        minneapolis_minnesota: typing.Callable[[], T_Result],
        missoula_montana: typing.Callable[[], T_Result],
        mobile_alabama: typing.Callable[[], T_Result],
        modesto_california: typing.Callable[[], T_Result],
        monroe_louisiana: typing.Callable[[], T_Result],
        monroe_michigan: typing.Callable[[], T_Result],
        montgomery_alabama: typing.Callable[[], T_Result],
        morgantown_west_virginia: typing.Callable[[], T_Result],
        morristown_tennessee: typing.Callable[[], T_Result],
        mount_vernon_washington: typing.Callable[[], T_Result],
        muncie_indiana: typing.Callable[[], T_Result],
        muskegon_michigan: typing.Callable[[], T_Result],
        myrtle_beach_south_carolina: typing.Callable[[], T_Result],
        napa_california: typing.Callable[[], T_Result],
        naples_florida: typing.Callable[[], T_Result],
        nashville_tennessee: typing.Callable[[], T_Result],
        new_bern_north_carolina: typing.Callable[[], T_Result],
        new_haven_connecticut: typing.Callable[[], T_Result],
        new_orleans_louisiana: typing.Callable[[], T_Result],
        new_york_new_york: typing.Callable[[], T_Result],
        north_port_florida: typing.Callable[[], T_Result],
        norwich_connecticut: typing.Callable[[], T_Result],
        ocala_florida: typing.Callable[[], T_Result],
        odessa_texas: typing.Callable[[], T_Result],
        ogden_utah: typing.Callable[[], T_Result],
        oklahoma_city_oklahoma: typing.Callable[[], T_Result],
        olympia_washington: typing.Callable[[], T_Result],
        omaha_nebraska: typing.Callable[[], T_Result],
        orlando_florida: typing.Callable[[], T_Result],
        oshkosh_wisconsin: typing.Callable[[], T_Result],
        owensboro_kentucky: typing.Callable[[], T_Result],
        oxnard_california: typing.Callable[[], T_Result],
        palm_bay_florida: typing.Callable[[], T_Result],
        panama_city_florida: typing.Callable[[], T_Result],
        parkersburg_west_virginia: typing.Callable[[], T_Result],
        pensacola_florida: typing.Callable[[], T_Result],
        peoria_illinois: typing.Callable[[], T_Result],
        philadelphia_pennsylvania: typing.Callable[[], T_Result],
        phoenix_arizona: typing.Callable[[], T_Result],
        pine_bluff_arkansas: typing.Callable[[], T_Result],
        pittsburgh_pennsylvania: typing.Callable[[], T_Result],
        pittsfield_massachusetts: typing.Callable[[], T_Result],
        pocatello_idaho: typing.Callable[[], T_Result],
        port_st_lucie_florida: typing.Callable[[], T_Result],
        portland_maine: typing.Callable[[], T_Result],
        portland_oregon: typing.Callable[[], T_Result],
        poughkeepsie_new_york: typing.Callable[[], T_Result],
        prescott_valley_arizona: typing.Callable[[], T_Result],
        providence_rhode_island: typing.Callable[[], T_Result],
        provo_utah: typing.Callable[[], T_Result],
        pueblo_colorado: typing.Callable[[], T_Result],
        punta_gorda_florida: typing.Callable[[], T_Result],
        racine_wisconsin: typing.Callable[[], T_Result],
        raleigh_north_carolina: typing.Callable[[], T_Result],
        rapid_city_south_dakota: typing.Callable[[], T_Result],
        reading_pennsylvania: typing.Callable[[], T_Result],
        redding_california: typing.Callable[[], T_Result],
        reno_nevada: typing.Callable[[], T_Result],
        richmond_virginia: typing.Callable[[], T_Result],
        riverside_california: typing.Callable[[], T_Result],
        roanoke_virginia: typing.Callable[[], T_Result],
        rochester_minnesota: typing.Callable[[], T_Result],
        rochester_new_york: typing.Callable[[], T_Result],
        rockford_illinois: typing.Callable[[], T_Result],
        rocky_mount_north_carolina: typing.Callable[[], T_Result],
        rome_georgia: typing.Callable[[], T_Result],
        sacramento_california: typing.Callable[[], T_Result],
        saginaw_michigan: typing.Callable[[], T_Result],
        salem_oregon: typing.Callable[[], T_Result],
        salinas_california: typing.Callable[[], T_Result],
        salisbury_maryland: typing.Callable[[], T_Result],
        salt_lake_city_utah: typing.Callable[[], T_Result],
        san_angelo_texas: typing.Callable[[], T_Result],
        san_antonio_texas: typing.Callable[[], T_Result],
        san_diego_california: typing.Callable[[], T_Result],
        san_francisco_california: typing.Callable[[], T_Result],
        san_jose_california: typing.Callable[[], T_Result],
        san_luis_obispo_california: typing.Callable[[], T_Result],
        santa_cruz_california: typing.Callable[[], T_Result],
        santa_fe_new_mexico: typing.Callable[[], T_Result],
        santa_maria_california: typing.Callable[[], T_Result],
        santa_rosa_california: typing.Callable[[], T_Result],
        savannah_georgia: typing.Callable[[], T_Result],
        scranton_pennsylvania: typing.Callable[[], T_Result],
        seattle_washington: typing.Callable[[], T_Result],
        sebastian_florida: typing.Callable[[], T_Result],
        sheboygan_wisconsin: typing.Callable[[], T_Result],
        sherman_texas: typing.Callable[[], T_Result],
        shreveport_louisiana: typing.Callable[[], T_Result],
        sierra_vista_arizona: typing.Callable[[], T_Result],
        sioux_city_iowa: typing.Callable[[], T_Result],
        sioux_falls_south_dakota: typing.Callable[[], T_Result],
        south_bend_indiana: typing.Callable[[], T_Result],
        spartanburg_south_carolina: typing.Callable[[], T_Result],
        spokane_washington: typing.Callable[[], T_Result],
        springfield_illinois: typing.Callable[[], T_Result],
        springfield_massachusetts: typing.Callable[[], T_Result],
        springfield_missouri: typing.Callable[[], T_Result],
        springfield_ohio: typing.Callable[[], T_Result],
        st_cloud_minnesota: typing.Callable[[], T_Result],
        st_george_utah: typing.Callable[[], T_Result],
        st_joseph_missouri: typing.Callable[[], T_Result],
        st_louis_missouri: typing.Callable[[], T_Result],
        state_college_pennsylvania: typing.Callable[[], T_Result],
        staunton_virginia: typing.Callable[[], T_Result],
        stockton_california: typing.Callable[[], T_Result],
        sumter_south_carolina: typing.Callable[[], T_Result],
        syracuse_new_york: typing.Callable[[], T_Result],
        tallahassee_florida: typing.Callable[[], T_Result],
        tampa_florida: typing.Callable[[], T_Result],
        terre_haute_indiana: typing.Callable[[], T_Result],
        texarkana_texas: typing.Callable[[], T_Result],
        toledo_ohio: typing.Callable[[], T_Result],
        topeka_kansas: typing.Callable[[], T_Result],
        trenton_new_jersey: typing.Callable[[], T_Result],
        tucson_arizona: typing.Callable[[], T_Result],
        tulsa_oklahoma: typing.Callable[[], T_Result],
        tuscaloosa_alabama: typing.Callable[[], T_Result],
        twin_falls_idaho: typing.Callable[[], T_Result],
        tyler_texas: typing.Callable[[], T_Result],
        urban_honolulu_hawaii: typing.Callable[[], T_Result],
        utica_new_york: typing.Callable[[], T_Result],
        valdosta_georgia: typing.Callable[[], T_Result],
        vallejo_california: typing.Callable[[], T_Result],
        victoria_texas: typing.Callable[[], T_Result],
        vineland_new_jersey: typing.Callable[[], T_Result],
        virginia_beach_virginia: typing.Callable[[], T_Result],
        visalia_california: typing.Callable[[], T_Result],
        waco_texas: typing.Callable[[], T_Result],
        walla_walla_washington: typing.Callable[[], T_Result],
        warner_robins_georgia: typing.Callable[[], T_Result],
        waterloo_iowa: typing.Callable[[], T_Result],
        watertown_new_york: typing.Callable[[], T_Result],
        wausau_wisconsin: typing.Callable[[], T_Result],
        weirton_west_virginia: typing.Callable[[], T_Result],
        wenatchee_washington: typing.Callable[[], T_Result],
        wheeling_west_virginia: typing.Callable[[], T_Result],
        wichita_falls_texas: typing.Callable[[], T_Result],
        wichita_kansas: typing.Callable[[], T_Result],
        williamsport_pennsylvania: typing.Callable[[], T_Result],
        wilmington_north_carolina: typing.Callable[[], T_Result],
        winchester_virginia: typing.Callable[[], T_Result],
        worcester_massachusetts: typing.Callable[[], T_Result],
        yakima_washington: typing.Callable[[], T_Result],
        york_pennsylvania: typing.Callable[[], T_Result],
        youngstown_ohio: typing.Callable[[], T_Result],
        yuba_city_california: typing.Callable[[], T_Result],
        yuma_arizona: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExperienceCompanyLocationMetro.ABILENE_TEXAS:
            return abilene_texas()
        if self is ExperienceCompanyLocationMetro.AKRON_OHIO:
            return akron_ohio()
        if self is ExperienceCompanyLocationMetro.ALBANY_GEORGIA:
            return albany_georgia()
        if self is ExperienceCompanyLocationMetro.ALBANY_NEW_YORK:
            return albany_new_york()
        if self is ExperienceCompanyLocationMetro.ALBANY_OREGON:
            return albany_oregon()
        if self is ExperienceCompanyLocationMetro.ALBUQUERQUE_NEW_MEXICO:
            return albuquerque_new_mexico()
        if self is ExperienceCompanyLocationMetro.ALEXANDRIA_LOUISIANA:
            return alexandria_louisiana()
        if self is ExperienceCompanyLocationMetro.ALLENTOWN_PENNSYLVANIA:
            return allentown_pennsylvania()
        if self is ExperienceCompanyLocationMetro.ALTOONA_PENNSYLVANIA:
            return altoona_pennsylvania()
        if self is ExperienceCompanyLocationMetro.AMARILLO_TEXAS:
            return amarillo_texas()
        if self is ExperienceCompanyLocationMetro.AMES_IOWA:
            return ames_iowa()
        if self is ExperienceCompanyLocationMetro.ANCHORAGE_ALASKA:
            return anchorage_alaska()
        if self is ExperienceCompanyLocationMetro.ANN_ARBOR_MICHIGAN:
            return ann_arbor_michigan()
        if self is ExperienceCompanyLocationMetro.ANNISTON_ALABAMA:
            return anniston_alabama()
        if self is ExperienceCompanyLocationMetro.APPLETON_WISCONSIN:
            return appleton_wisconsin()
        if self is ExperienceCompanyLocationMetro.ASHEVILLE_NORTH_CAROLINA:
            return asheville_north_carolina()
        if self is ExperienceCompanyLocationMetro.ATHENS_GEORGIA:
            return athens_georgia()
        if self is ExperienceCompanyLocationMetro.ATLANTA_GEORGIA:
            return atlanta_georgia()
        if self is ExperienceCompanyLocationMetro.ATLANTIC_CITY_NEW_JERSEY:
            return atlantic_city_new_jersey()
        if self is ExperienceCompanyLocationMetro.AUBURN_ALABAMA:
            return auburn_alabama()
        if self is ExperienceCompanyLocationMetro.AUGUSTA_GEORGIA:
            return augusta_georgia()
        if self is ExperienceCompanyLocationMetro.AUSTIN_TEXAS:
            return austin_texas()
        if self is ExperienceCompanyLocationMetro.BAKERSFIELD_CALIFORNIA:
            return bakersfield_california()
        if self is ExperienceCompanyLocationMetro.BALTIMORE_MARYLAND:
            return baltimore_maryland()
        if self is ExperienceCompanyLocationMetro.BANGOR_MAINE:
            return bangor_maine()
        if self is ExperienceCompanyLocationMetro.BARNSTABLE_TOWN_MASSACHUSETTS:
            return barnstable_town_massachusetts()
        if self is ExperienceCompanyLocationMetro.BATON_ROUGE_LOUISIANA:
            return baton_rouge_louisiana()
        if self is ExperienceCompanyLocationMetro.BATTLE_CREEK_MICHIGAN:
            return battle_creek_michigan()
        if self is ExperienceCompanyLocationMetro.BAY_CITY_MICHIGAN:
            return bay_city_michigan()
        if self is ExperienceCompanyLocationMetro.BEAUMONT_TEXAS:
            return beaumont_texas()
        if self is ExperienceCompanyLocationMetro.BELLINGHAM_WASHINGTON:
            return bellingham_washington()
        if self is ExperienceCompanyLocationMetro.BILLINGS_MONTANA:
            return billings_montana()
        if self is ExperienceCompanyLocationMetro.BINGHAMTON_NEW_YORK:
            return binghamton_new_york()
        if self is ExperienceCompanyLocationMetro.BIRMINGHAM_ALABAMA:
            return birmingham_alabama()
        if self is ExperienceCompanyLocationMetro.BISMARCK_NORTH_DAKOTA:
            return bismarck_north_dakota()
        if self is ExperienceCompanyLocationMetro.BLACKSBURG_VIRGINIA:
            return blacksburg_virginia()
        if self is ExperienceCompanyLocationMetro.BLOOMINGTON_ILLINOIS:
            return bloomington_illinois()
        if self is ExperienceCompanyLocationMetro.BLOOMINGTON_INDIANA:
            return bloomington_indiana()
        if self is ExperienceCompanyLocationMetro.BOISE_CITY_IDAHO:
            return boise_city_idaho()
        if self is ExperienceCompanyLocationMetro.BOSTON_MASSACHUSETTS:
            return boston_massachusetts()
        if self is ExperienceCompanyLocationMetro.BOULDER_COLORADO:
            return boulder_colorado()
        if self is ExperienceCompanyLocationMetro.BOWLING_GREEN_KENTUCKY:
            return bowling_green_kentucky()
        if self is ExperienceCompanyLocationMetro.BREMERTON_WASHINGTON:
            return bremerton_washington()
        if self is ExperienceCompanyLocationMetro.BRIDGEPORT_CONNECTICUT:
            return bridgeport_connecticut()
        if self is ExperienceCompanyLocationMetro.BROWNSVILLE_TEXAS:
            return brownsville_texas()
        if self is ExperienceCompanyLocationMetro.BUFFALO_NEW_YORK:
            return buffalo_new_york()
        if self is ExperienceCompanyLocationMetro.BURLINGTON_NORTH_CAROLINA:
            return burlington_north_carolina()
        if self is ExperienceCompanyLocationMetro.BURLINGTON_VERMONT:
            return burlington_vermont()
        if self is ExperienceCompanyLocationMetro.CANTON_OHIO:
            return canton_ohio()
        if self is ExperienceCompanyLocationMetro.CAPE_CORAL_FLORIDA:
            return cape_coral_florida()
        if self is ExperienceCompanyLocationMetro.CAPE_GIRARDEAU_MISSOURI:
            return cape_girardeau_missouri()
        if self is ExperienceCompanyLocationMetro.CARBONDALE_ILLINOIS:
            return carbondale_illinois()
        if self is ExperienceCompanyLocationMetro.CARSON_CITY_NEVADA:
            return carson_city_nevada()
        if self is ExperienceCompanyLocationMetro.CASPER_WYOMING:
            return casper_wyoming()
        if self is ExperienceCompanyLocationMetro.CEDAR_RAPIDS_IOWA:
            return cedar_rapids_iowa()
        if self is ExperienceCompanyLocationMetro.CHAMPAIGN_ILLINOIS:
            return champaign_illinois()
        if self is ExperienceCompanyLocationMetro.CHARLESTON_SOUTH_CAROLINA:
            return charleston_south_carolina()
        if self is ExperienceCompanyLocationMetro.CHARLESTON_WEST_VIRGINIA:
            return charleston_west_virginia()
        if self is ExperienceCompanyLocationMetro.CHARLOTTE_NORTH_CAROLINA:
            return charlotte_north_carolina()
        if self is ExperienceCompanyLocationMetro.CHARLOTTESVILLE_VIRGINIA:
            return charlottesville_virginia()
        if self is ExperienceCompanyLocationMetro.CHATTANOOGA_TENNESSEE:
            return chattanooga_tennessee()
        if self is ExperienceCompanyLocationMetro.CHEYENNE_WYOMING:
            return cheyenne_wyoming()
        if self is ExperienceCompanyLocationMetro.CHICAGO_ILLINOIS:
            return chicago_illinois()
        if self is ExperienceCompanyLocationMetro.CHICO_CALIFORNIA:
            return chico_california()
        if self is ExperienceCompanyLocationMetro.CINCINNATI_OHIO:
            return cincinnati_ohio()
        if self is ExperienceCompanyLocationMetro.CLARKSVILLE_TENNESSEE:
            return clarksville_tennessee()
        if self is ExperienceCompanyLocationMetro.CLEVELAND_OHIO:
            return cleveland_ohio()
        if self is ExperienceCompanyLocationMetro.CLEVELAND_TENNESSEE:
            return cleveland_tennessee()
        if self is ExperienceCompanyLocationMetro.COEUR_DALENE_IDAHO:
            return coeur_dalene_idaho()
        if self is ExperienceCompanyLocationMetro.COLLEGE_STATION_TEXAS:
            return college_station_texas()
        if self is ExperienceCompanyLocationMetro.COLORADO_SPRINGS_COLORADO:
            return colorado_springs_colorado()
        if self is ExperienceCompanyLocationMetro.COLUMBIA_MISSOURI:
            return columbia_missouri()
        if self is ExperienceCompanyLocationMetro.COLUMBIA_SOUTH_CAROLINA:
            return columbia_south_carolina()
        if self is ExperienceCompanyLocationMetro.COLUMBUS_GEORGIA:
            return columbus_georgia()
        if self is ExperienceCompanyLocationMetro.COLUMBUS_INDIANA:
            return columbus_indiana()
        if self is ExperienceCompanyLocationMetro.COLUMBUS_OHIO:
            return columbus_ohio()
        if self is ExperienceCompanyLocationMetro.CORPUS_CHRISTI_TEXAS:
            return corpus_christi_texas()
        if self is ExperienceCompanyLocationMetro.CORVALLIS_OREGON:
            return corvallis_oregon()
        if self is ExperienceCompanyLocationMetro.CRESTVIEW_FLORIDA:
            return crestview_florida()
        if self is ExperienceCompanyLocationMetro.CUMBERLAND_MARYLAND:
            return cumberland_maryland()
        if self is ExperienceCompanyLocationMetro.DALLAS_TEXAS:
            return dallas_texas()
        if self is ExperienceCompanyLocationMetro.DALTON_GEORGIA:
            return dalton_georgia()
        if self is ExperienceCompanyLocationMetro.DANVILLE_ILLINOIS:
            return danville_illinois()
        if self is ExperienceCompanyLocationMetro.DAVENPORT_IOWA:
            return davenport_iowa()
        if self is ExperienceCompanyLocationMetro.DAYTON_OHIO:
            return dayton_ohio()
        if self is ExperienceCompanyLocationMetro.DECATUR_ALABAMA:
            return decatur_alabama()
        if self is ExperienceCompanyLocationMetro.DECATUR_ILLINOIS:
            return decatur_illinois()
        if self is ExperienceCompanyLocationMetro.DELTONA_FLORIDA:
            return deltona_florida()
        if self is ExperienceCompanyLocationMetro.DENVER_COLORADO:
            return denver_colorado()
        if self is ExperienceCompanyLocationMetro.DES_MOINES_IOWA:
            return des_moines_iowa()
        if self is ExperienceCompanyLocationMetro.DETROIT_MICHIGAN:
            return detroit_michigan()
        if self is ExperienceCompanyLocationMetro.DISTRICT_OF_COLUMBIA:
            return district_of_columbia()
        if self is ExperienceCompanyLocationMetro.DOTHAN_ALABAMA:
            return dothan_alabama()
        if self is ExperienceCompanyLocationMetro.DOVER_DELAWARE:
            return dover_delaware()
        if self is ExperienceCompanyLocationMetro.DUBUQUE_IOWA:
            return dubuque_iowa()
        if self is ExperienceCompanyLocationMetro.DULUTH_MINNESOTA:
            return duluth_minnesota()
        if self is ExperienceCompanyLocationMetro.DURHAM_NORTH_CAROLINA:
            return durham_north_carolina()
        if self is ExperienceCompanyLocationMetro.EAU_CLAIRE_WISCONSIN:
            return eau_claire_wisconsin()
        if self is ExperienceCompanyLocationMetro.EL_CENTRO_CALIFORNIA:
            return el_centro_california()
        if self is ExperienceCompanyLocationMetro.EL_PASO_TEXAS:
            return el_paso_texas()
        if self is ExperienceCompanyLocationMetro.ELIZABETHTOWN_KENTUCKY:
            return elizabethtown_kentucky()
        if self is ExperienceCompanyLocationMetro.ELKHART_INDIANA:
            return elkhart_indiana()
        if self is ExperienceCompanyLocationMetro.ELMIRA_NEW_YORK:
            return elmira_new_york()
        if self is ExperienceCompanyLocationMetro.ENID_OKLAHOMA:
            return enid_oklahoma()
        if self is ExperienceCompanyLocationMetro.ERIE_PENNSYLVANIA:
            return erie_pennsylvania()
        if self is ExperienceCompanyLocationMetro.EUGENE_OREGON:
            return eugene_oregon()
        if self is ExperienceCompanyLocationMetro.EVANSVILLE_INDIANA:
            return evansville_indiana()
        if self is ExperienceCompanyLocationMetro.FAIRBANKS_ALASKA:
            return fairbanks_alaska()
        if self is ExperienceCompanyLocationMetro.FARGO_NORTH_DAKOTA:
            return fargo_north_dakota()
        if self is ExperienceCompanyLocationMetro.FARMINGTON_NEW_MEXICO:
            return farmington_new_mexico()
        if self is ExperienceCompanyLocationMetro.FAYETTEVILLE_ARKANSAS:
            return fayetteville_arkansas()
        if self is ExperienceCompanyLocationMetro.FAYETTEVILLE_NORTH_CAROLINA:
            return fayetteville_north_carolina()
        if self is ExperienceCompanyLocationMetro.FLAGSTAFF_ARIZONA:
            return flagstaff_arizona()
        if self is ExperienceCompanyLocationMetro.FLINT_MICHIGAN:
            return flint_michigan()
        if self is ExperienceCompanyLocationMetro.FLORENCE_ALABAMA:
            return florence_alabama()
        if self is ExperienceCompanyLocationMetro.FLORENCE_SOUTH_CAROLINA:
            return florence_south_carolina()
        if self is ExperienceCompanyLocationMetro.FOND_DU_LAC_WISCONSIN:
            return fond_du_lac_wisconsin()
        if self is ExperienceCompanyLocationMetro.FORT_COLLINS_COLORADO:
            return fort_collins_colorado()
        if self is ExperienceCompanyLocationMetro.FORT_SMITH_ARKANSAS:
            return fort_smith_arkansas()
        if self is ExperienceCompanyLocationMetro.FORT_WAYNE_INDIANA:
            return fort_wayne_indiana()
        if self is ExperienceCompanyLocationMetro.FRESNO_CALIFORNIA:
            return fresno_california()
        if self is ExperienceCompanyLocationMetro.GADSDEN_ALABAMA:
            return gadsden_alabama()
        if self is ExperienceCompanyLocationMetro.GAINESVILLE_FLORIDA:
            return gainesville_florida()
        if self is ExperienceCompanyLocationMetro.GAINESVILLE_GEORGIA:
            return gainesville_georgia()
        if self is ExperienceCompanyLocationMetro.GOLDSBORO_NORTH_CAROLINA:
            return goldsboro_north_carolina()
        if self is ExperienceCompanyLocationMetro.GRAND_FORKS_NORTH_DAKOTA:
            return grand_forks_north_dakota()
        if self is ExperienceCompanyLocationMetro.GRAND_ISLAND_NEBRASKA:
            return grand_island_nebraska()
        if self is ExperienceCompanyLocationMetro.GRAND_JUNCTION_COLORADO:
            return grand_junction_colorado()
        if self is ExperienceCompanyLocationMetro.GRAND_RAPIDS_MICHIGAN:
            return grand_rapids_michigan()
        if self is ExperienceCompanyLocationMetro.GRANTS_PASS_OREGON:
            return grants_pass_oregon()
        if self is ExperienceCompanyLocationMetro.GREAT_FALLS_MONTANA:
            return great_falls_montana()
        if self is ExperienceCompanyLocationMetro.GREELEY_COLORADO:
            return greeley_colorado()
        if self is ExperienceCompanyLocationMetro.GREEN_BAY_WISCONSIN:
            return green_bay_wisconsin()
        if self is ExperienceCompanyLocationMetro.GREENSBORO_NORTH_CAROLINA:
            return greensboro_north_carolina()
        if self is ExperienceCompanyLocationMetro.GREENVILLE_NORTH_CAROLINA:
            return greenville_north_carolina()
        if self is ExperienceCompanyLocationMetro.GREENVILLE_SOUTH_CAROLINA:
            return greenville_south_carolina()
        if self is ExperienceCompanyLocationMetro.GULFPORT_MISSISSIPPI:
            return gulfport_mississippi()
        if self is ExperienceCompanyLocationMetro.HAGERSTOWN_MARYLAND:
            return hagerstown_maryland()
        if self is ExperienceCompanyLocationMetro.HANFORD_CALIFORNIA:
            return hanford_california()
        if self is ExperienceCompanyLocationMetro.HARRISBURG_PENNSYLVANIA:
            return harrisburg_pennsylvania()
        if self is ExperienceCompanyLocationMetro.HARRISONBURG_VIRGINIA:
            return harrisonburg_virginia()
        if self is ExperienceCompanyLocationMetro.HARTFORD_CONNECTICUT:
            return hartford_connecticut()
        if self is ExperienceCompanyLocationMetro.HATTIESBURG_MISSISSIPPI:
            return hattiesburg_mississippi()
        if self is ExperienceCompanyLocationMetro.HICKORY_NORTH_CAROLINA:
            return hickory_north_carolina()
        if self is ExperienceCompanyLocationMetro.HILTON_HEAD_ISLAND_SOUTH_CAROLINA:
            return hilton_head_island_south_carolina()
        if self is ExperienceCompanyLocationMetro.HINESVILLE_GEORGIA:
            return hinesville_georgia()
        if self is ExperienceCompanyLocationMetro.HOT_SPRINGS_ARKANSAS:
            return hot_springs_arkansas()
        if self is ExperienceCompanyLocationMetro.HOUMA_LOUISIANA:
            return houma_louisiana()
        if self is ExperienceCompanyLocationMetro.HOUSTON_TEXAS:
            return houston_texas()
        if self is ExperienceCompanyLocationMetro.HUNTINGTON_WEST_VIRGINIA:
            return huntington_west_virginia()
        if self is ExperienceCompanyLocationMetro.HUNTSVILLE_ALABAMA:
            return huntsville_alabama()
        if self is ExperienceCompanyLocationMetro.IDAHO_FALLS_IDAHO:
            return idaho_falls_idaho()
        if self is ExperienceCompanyLocationMetro.INDIANAPOLIS_INDIANA:
            return indianapolis_indiana()
        if self is ExperienceCompanyLocationMetro.IOWA_CITY_IOWA:
            return iowa_city_iowa()
        if self is ExperienceCompanyLocationMetro.ITHACA_NEW_YORK:
            return ithaca_new_york()
        if self is ExperienceCompanyLocationMetro.JACKSON_MICHIGAN:
            return jackson_michigan()
        if self is ExperienceCompanyLocationMetro.JACKSON_MISSISSIPPI:
            return jackson_mississippi()
        if self is ExperienceCompanyLocationMetro.JACKSON_TENNESSEE:
            return jackson_tennessee()
        if self is ExperienceCompanyLocationMetro.JACKSONVILLE_FLORIDA:
            return jacksonville_florida()
        if self is ExperienceCompanyLocationMetro.JACKSONVILLE_NORTH_CAROLINA:
            return jacksonville_north_carolina()
        if self is ExperienceCompanyLocationMetro.JANESVILLE_WISCONSIN:
            return janesville_wisconsin()
        if self is ExperienceCompanyLocationMetro.JEFFERSON_CITY_MISSOURI:
            return jefferson_city_missouri()
        if self is ExperienceCompanyLocationMetro.JOHNSON_CITY_TENNESSEE:
            return johnson_city_tennessee()
        if self is ExperienceCompanyLocationMetro.JOHNSTOWN_PENNSYLVANIA:
            return johnstown_pennsylvania()
        if self is ExperienceCompanyLocationMetro.JONESBORO_ARKANSAS:
            return jonesboro_arkansas()
        if self is ExperienceCompanyLocationMetro.JOPLIN_MISSOURI:
            return joplin_missouri()
        if self is ExperienceCompanyLocationMetro.KAHULUI_HAWAII:
            return kahului_hawaii()
        if self is ExperienceCompanyLocationMetro.KALAMAZOO_MICHIGAN:
            return kalamazoo_michigan()
        if self is ExperienceCompanyLocationMetro.KANKAKEE_ILLINOIS:
            return kankakee_illinois()
        if self is ExperienceCompanyLocationMetro.KANSAS_CITY_MISSOURI:
            return kansas_city_missouri()
        if self is ExperienceCompanyLocationMetro.KENNEWICK_WASHINGTON:
            return kennewick_washington()
        if self is ExperienceCompanyLocationMetro.KILLEEN_TEXAS:
            return killeen_texas()
        if self is ExperienceCompanyLocationMetro.KINGSPORT_TENNESSEE:
            return kingsport_tennessee()
        if self is ExperienceCompanyLocationMetro.KINGSTON_NEW_YORK:
            return kingston_new_york()
        if self is ExperienceCompanyLocationMetro.KNOXVILLE_TENNESSEE:
            return knoxville_tennessee()
        if self is ExperienceCompanyLocationMetro.KOKOMO_INDIANA:
            return kokomo_indiana()
        if self is ExperienceCompanyLocationMetro.LA_CROSSE_WISCONSIN:
            return la_crosse_wisconsin()
        if self is ExperienceCompanyLocationMetro.LAFAYETTE_INDIANA:
            return lafayette_indiana()
        if self is ExperienceCompanyLocationMetro.LAFAYETTE_LOUISIANA:
            return lafayette_louisiana()
        if self is ExperienceCompanyLocationMetro.LAKE_CHARLES_LOUISIANA:
            return lake_charles_louisiana()
        if self is ExperienceCompanyLocationMetro.LAKE_HAVASU_CITY_ARIZONA:
            return lake_havasu_city_arizona()
        if self is ExperienceCompanyLocationMetro.LAKELAND_FLORIDA:
            return lakeland_florida()
        if self is ExperienceCompanyLocationMetro.LANCASTER_PENNSYLVANIA:
            return lancaster_pennsylvania()
        if self is ExperienceCompanyLocationMetro.LANSING_MICHIGAN:
            return lansing_michigan()
        if self is ExperienceCompanyLocationMetro.LAREDO_TEXAS:
            return laredo_texas()
        if self is ExperienceCompanyLocationMetro.LAS_CRUCES_NEW_MEXICO:
            return las_cruces_new_mexico()
        if self is ExperienceCompanyLocationMetro.LAS_VEGAS_NEVADA:
            return las_vegas_nevada()
        if self is ExperienceCompanyLocationMetro.LAWRENCE_KANSAS:
            return lawrence_kansas()
        if self is ExperienceCompanyLocationMetro.LAWTON_OKLAHOMA:
            return lawton_oklahoma()
        if self is ExperienceCompanyLocationMetro.LEBANON_PENNSYLVANIA:
            return lebanon_pennsylvania()
        if self is ExperienceCompanyLocationMetro.LEWISTON_IDAHO:
            return lewiston_idaho()
        if self is ExperienceCompanyLocationMetro.LEWISTON_MAINE:
            return lewiston_maine()
        if self is ExperienceCompanyLocationMetro.LEXINGTON_KENTUCKY:
            return lexington_kentucky()
        if self is ExperienceCompanyLocationMetro.LIMA_OHIO:
            return lima_ohio()
        if self is ExperienceCompanyLocationMetro.LINCOLN_NEBRASKA:
            return lincoln_nebraska()
        if self is ExperienceCompanyLocationMetro.LITTLE_ROCK_ARKANSAS:
            return little_rock_arkansas()
        if self is ExperienceCompanyLocationMetro.LOGAN_UTAH:
            return logan_utah()
        if self is ExperienceCompanyLocationMetro.LONGVIEW_TEXAS:
            return longview_texas()
        if self is ExperienceCompanyLocationMetro.LONGVIEW_WASHINGTON:
            return longview_washington()
        if self is ExperienceCompanyLocationMetro.LOS_ANGELES_CALIFORNIA:
            return los_angeles_california()
        if self is ExperienceCompanyLocationMetro.LOUISVILLE_KENTUCKY:
            return louisville_kentucky()
        if self is ExperienceCompanyLocationMetro.LUBBOCK_TEXAS:
            return lubbock_texas()
        if self is ExperienceCompanyLocationMetro.LYNCHBURG_VIRGINIA:
            return lynchburg_virginia()
        if self is ExperienceCompanyLocationMetro.MACON_GEORGIA:
            return macon_georgia()
        if self is ExperienceCompanyLocationMetro.MADERA_CALIFORNIA:
            return madera_california()
        if self is ExperienceCompanyLocationMetro.MADISON_WISCONSIN:
            return madison_wisconsin()
        if self is ExperienceCompanyLocationMetro.MANCHESTER_NEW_HAMPSHIRE:
            return manchester_new_hampshire()
        if self is ExperienceCompanyLocationMetro.MANHATTAN_KANSAS:
            return manhattan_kansas()
        if self is ExperienceCompanyLocationMetro.MANKATO_MINNESOTA:
            return mankato_minnesota()
        if self is ExperienceCompanyLocationMetro.MANSFIELD_OHIO:
            return mansfield_ohio()
        if self is ExperienceCompanyLocationMetro.MCALLEN_TEXAS:
            return mcallen_texas()
        if self is ExperienceCompanyLocationMetro.MEDFORD_OREGON:
            return medford_oregon()
        if self is ExperienceCompanyLocationMetro.MEMPHIS_TENNESSEE:
            return memphis_tennessee()
        if self is ExperienceCompanyLocationMetro.MERCED_CALIFORNIA:
            return merced_california()
        if self is ExperienceCompanyLocationMetro.MIAMI_FLORIDA:
            return miami_florida()
        if self is ExperienceCompanyLocationMetro.MICHIGAN_CITY_INDIANA:
            return michigan_city_indiana()
        if self is ExperienceCompanyLocationMetro.MIDLAND_MICHIGAN:
            return midland_michigan()
        if self is ExperienceCompanyLocationMetro.MIDLAND_TEXAS:
            return midland_texas()
        if self is ExperienceCompanyLocationMetro.MILWAUKEE_WISCONSIN:
            return milwaukee_wisconsin()
        if self is ExperienceCompanyLocationMetro.MINNEAPOLIS_MINNESOTA:
            return minneapolis_minnesota()
        if self is ExperienceCompanyLocationMetro.MISSOULA_MONTANA:
            return missoula_montana()
        if self is ExperienceCompanyLocationMetro.MOBILE_ALABAMA:
            return mobile_alabama()
        if self is ExperienceCompanyLocationMetro.MODESTO_CALIFORNIA:
            return modesto_california()
        if self is ExperienceCompanyLocationMetro.MONROE_LOUISIANA:
            return monroe_louisiana()
        if self is ExperienceCompanyLocationMetro.MONROE_MICHIGAN:
            return monroe_michigan()
        if self is ExperienceCompanyLocationMetro.MONTGOMERY_ALABAMA:
            return montgomery_alabama()
        if self is ExperienceCompanyLocationMetro.MORGANTOWN_WEST_VIRGINIA:
            return morgantown_west_virginia()
        if self is ExperienceCompanyLocationMetro.MORRISTOWN_TENNESSEE:
            return morristown_tennessee()
        if self is ExperienceCompanyLocationMetro.MOUNT_VERNON_WASHINGTON:
            return mount_vernon_washington()
        if self is ExperienceCompanyLocationMetro.MUNCIE_INDIANA:
            return muncie_indiana()
        if self is ExperienceCompanyLocationMetro.MUSKEGON_MICHIGAN:
            return muskegon_michigan()
        if self is ExperienceCompanyLocationMetro.MYRTLE_BEACH_SOUTH_CAROLINA:
            return myrtle_beach_south_carolina()
        if self is ExperienceCompanyLocationMetro.NAPA_CALIFORNIA:
            return napa_california()
        if self is ExperienceCompanyLocationMetro.NAPLES_FLORIDA:
            return naples_florida()
        if self is ExperienceCompanyLocationMetro.NASHVILLE_TENNESSEE:
            return nashville_tennessee()
        if self is ExperienceCompanyLocationMetro.NEW_BERN_NORTH_CAROLINA:
            return new_bern_north_carolina()
        if self is ExperienceCompanyLocationMetro.NEW_HAVEN_CONNECTICUT:
            return new_haven_connecticut()
        if self is ExperienceCompanyLocationMetro.NEW_ORLEANS_LOUISIANA:
            return new_orleans_louisiana()
        if self is ExperienceCompanyLocationMetro.NEW_YORK_NEW_YORK:
            return new_york_new_york()
        if self is ExperienceCompanyLocationMetro.NORTH_PORT_FLORIDA:
            return north_port_florida()
        if self is ExperienceCompanyLocationMetro.NORWICH_CONNECTICUT:
            return norwich_connecticut()
        if self is ExperienceCompanyLocationMetro.OCALA_FLORIDA:
            return ocala_florida()
        if self is ExperienceCompanyLocationMetro.ODESSA_TEXAS:
            return odessa_texas()
        if self is ExperienceCompanyLocationMetro.OGDEN_UTAH:
            return ogden_utah()
        if self is ExperienceCompanyLocationMetro.OKLAHOMA_CITY_OKLAHOMA:
            return oklahoma_city_oklahoma()
        if self is ExperienceCompanyLocationMetro.OLYMPIA_WASHINGTON:
            return olympia_washington()
        if self is ExperienceCompanyLocationMetro.OMAHA_NEBRASKA:
            return omaha_nebraska()
        if self is ExperienceCompanyLocationMetro.ORLANDO_FLORIDA:
            return orlando_florida()
        if self is ExperienceCompanyLocationMetro.OSHKOSH_WISCONSIN:
            return oshkosh_wisconsin()
        if self is ExperienceCompanyLocationMetro.OWENSBORO_KENTUCKY:
            return owensboro_kentucky()
        if self is ExperienceCompanyLocationMetro.OXNARD_CALIFORNIA:
            return oxnard_california()
        if self is ExperienceCompanyLocationMetro.PALM_BAY_FLORIDA:
            return palm_bay_florida()
        if self is ExperienceCompanyLocationMetro.PANAMA_CITY_FLORIDA:
            return panama_city_florida()
        if self is ExperienceCompanyLocationMetro.PARKERSBURG_WEST_VIRGINIA:
            return parkersburg_west_virginia()
        if self is ExperienceCompanyLocationMetro.PENSACOLA_FLORIDA:
            return pensacola_florida()
        if self is ExperienceCompanyLocationMetro.PEORIA_ILLINOIS:
            return peoria_illinois()
        if self is ExperienceCompanyLocationMetro.PHILADELPHIA_PENNSYLVANIA:
            return philadelphia_pennsylvania()
        if self is ExperienceCompanyLocationMetro.PHOENIX_ARIZONA:
            return phoenix_arizona()
        if self is ExperienceCompanyLocationMetro.PINE_BLUFF_ARKANSAS:
            return pine_bluff_arkansas()
        if self is ExperienceCompanyLocationMetro.PITTSBURGH_PENNSYLVANIA:
            return pittsburgh_pennsylvania()
        if self is ExperienceCompanyLocationMetro.PITTSFIELD_MASSACHUSETTS:
            return pittsfield_massachusetts()
        if self is ExperienceCompanyLocationMetro.POCATELLO_IDAHO:
            return pocatello_idaho()
        if self is ExperienceCompanyLocationMetro.PORT_ST_LUCIE_FLORIDA:
            return port_st_lucie_florida()
        if self is ExperienceCompanyLocationMetro.PORTLAND_MAINE:
            return portland_maine()
        if self is ExperienceCompanyLocationMetro.PORTLAND_OREGON:
            return portland_oregon()
        if self is ExperienceCompanyLocationMetro.POUGHKEEPSIE_NEW_YORK:
            return poughkeepsie_new_york()
        if self is ExperienceCompanyLocationMetro.PRESCOTT_VALLEY_ARIZONA:
            return prescott_valley_arizona()
        if self is ExperienceCompanyLocationMetro.PROVIDENCE_RHODE_ISLAND:
            return providence_rhode_island()
        if self is ExperienceCompanyLocationMetro.PROVO_UTAH:
            return provo_utah()
        if self is ExperienceCompanyLocationMetro.PUEBLO_COLORADO:
            return pueblo_colorado()
        if self is ExperienceCompanyLocationMetro.PUNTA_GORDA_FLORIDA:
            return punta_gorda_florida()
        if self is ExperienceCompanyLocationMetro.RACINE_WISCONSIN:
            return racine_wisconsin()
        if self is ExperienceCompanyLocationMetro.RALEIGH_NORTH_CAROLINA:
            return raleigh_north_carolina()
        if self is ExperienceCompanyLocationMetro.RAPID_CITY_SOUTH_DAKOTA:
            return rapid_city_south_dakota()
        if self is ExperienceCompanyLocationMetro.READING_PENNSYLVANIA:
            return reading_pennsylvania()
        if self is ExperienceCompanyLocationMetro.REDDING_CALIFORNIA:
            return redding_california()
        if self is ExperienceCompanyLocationMetro.RENO_NEVADA:
            return reno_nevada()
        if self is ExperienceCompanyLocationMetro.RICHMOND_VIRGINIA:
            return richmond_virginia()
        if self is ExperienceCompanyLocationMetro.RIVERSIDE_CALIFORNIA:
            return riverside_california()
        if self is ExperienceCompanyLocationMetro.ROANOKE_VIRGINIA:
            return roanoke_virginia()
        if self is ExperienceCompanyLocationMetro.ROCHESTER_MINNESOTA:
            return rochester_minnesota()
        if self is ExperienceCompanyLocationMetro.ROCHESTER_NEW_YORK:
            return rochester_new_york()
        if self is ExperienceCompanyLocationMetro.ROCKFORD_ILLINOIS:
            return rockford_illinois()
        if self is ExperienceCompanyLocationMetro.ROCKY_MOUNT_NORTH_CAROLINA:
            return rocky_mount_north_carolina()
        if self is ExperienceCompanyLocationMetro.ROME_GEORGIA:
            return rome_georgia()
        if self is ExperienceCompanyLocationMetro.SACRAMENTO_CALIFORNIA:
            return sacramento_california()
        if self is ExperienceCompanyLocationMetro.SAGINAW_MICHIGAN:
            return saginaw_michigan()
        if self is ExperienceCompanyLocationMetro.SALEM_OREGON:
            return salem_oregon()
        if self is ExperienceCompanyLocationMetro.SALINAS_CALIFORNIA:
            return salinas_california()
        if self is ExperienceCompanyLocationMetro.SALISBURY_MARYLAND:
            return salisbury_maryland()
        if self is ExperienceCompanyLocationMetro.SALT_LAKE_CITY_UTAH:
            return salt_lake_city_utah()
        if self is ExperienceCompanyLocationMetro.SAN_ANGELO_TEXAS:
            return san_angelo_texas()
        if self is ExperienceCompanyLocationMetro.SAN_ANTONIO_TEXAS:
            return san_antonio_texas()
        if self is ExperienceCompanyLocationMetro.SAN_DIEGO_CALIFORNIA:
            return san_diego_california()
        if self is ExperienceCompanyLocationMetro.SAN_FRANCISCO_CALIFORNIA:
            return san_francisco_california()
        if self is ExperienceCompanyLocationMetro.SAN_JOSE_CALIFORNIA:
            return san_jose_california()
        if self is ExperienceCompanyLocationMetro.SAN_LUIS_OBISPO_CALIFORNIA:
            return san_luis_obispo_california()
        if self is ExperienceCompanyLocationMetro.SANTA_CRUZ_CALIFORNIA:
            return santa_cruz_california()
        if self is ExperienceCompanyLocationMetro.SANTA_FE_NEW_MEXICO:
            return santa_fe_new_mexico()
        if self is ExperienceCompanyLocationMetro.SANTA_MARIA_CALIFORNIA:
            return santa_maria_california()
        if self is ExperienceCompanyLocationMetro.SANTA_ROSA_CALIFORNIA:
            return santa_rosa_california()
        if self is ExperienceCompanyLocationMetro.SAVANNAH_GEORGIA:
            return savannah_georgia()
        if self is ExperienceCompanyLocationMetro.SCRANTON_PENNSYLVANIA:
            return scranton_pennsylvania()
        if self is ExperienceCompanyLocationMetro.SEATTLE_WASHINGTON:
            return seattle_washington()
        if self is ExperienceCompanyLocationMetro.SEBASTIAN_FLORIDA:
            return sebastian_florida()
        if self is ExperienceCompanyLocationMetro.SHEBOYGAN_WISCONSIN:
            return sheboygan_wisconsin()
        if self is ExperienceCompanyLocationMetro.SHERMAN_TEXAS:
            return sherman_texas()
        if self is ExperienceCompanyLocationMetro.SHREVEPORT_LOUISIANA:
            return shreveport_louisiana()
        if self is ExperienceCompanyLocationMetro.SIERRA_VISTA_ARIZONA:
            return sierra_vista_arizona()
        if self is ExperienceCompanyLocationMetro.SIOUX_CITY_IOWA:
            return sioux_city_iowa()
        if self is ExperienceCompanyLocationMetro.SIOUX_FALLS_SOUTH_DAKOTA:
            return sioux_falls_south_dakota()
        if self is ExperienceCompanyLocationMetro.SOUTH_BEND_INDIANA:
            return south_bend_indiana()
        if self is ExperienceCompanyLocationMetro.SPARTANBURG_SOUTH_CAROLINA:
            return spartanburg_south_carolina()
        if self is ExperienceCompanyLocationMetro.SPOKANE_WASHINGTON:
            return spokane_washington()
        if self is ExperienceCompanyLocationMetro.SPRINGFIELD_ILLINOIS:
            return springfield_illinois()
        if self is ExperienceCompanyLocationMetro.SPRINGFIELD_MASSACHUSETTS:
            return springfield_massachusetts()
        if self is ExperienceCompanyLocationMetro.SPRINGFIELD_MISSOURI:
            return springfield_missouri()
        if self is ExperienceCompanyLocationMetro.SPRINGFIELD_OHIO:
            return springfield_ohio()
        if self is ExperienceCompanyLocationMetro.ST_CLOUD_MINNESOTA:
            return st_cloud_minnesota()
        if self is ExperienceCompanyLocationMetro.ST_GEORGE_UTAH:
            return st_george_utah()
        if self is ExperienceCompanyLocationMetro.ST_JOSEPH_MISSOURI:
            return st_joseph_missouri()
        if self is ExperienceCompanyLocationMetro.ST_LOUIS_MISSOURI:
            return st_louis_missouri()
        if self is ExperienceCompanyLocationMetro.STATE_COLLEGE_PENNSYLVANIA:
            return state_college_pennsylvania()
        if self is ExperienceCompanyLocationMetro.STAUNTON_VIRGINIA:
            return staunton_virginia()
        if self is ExperienceCompanyLocationMetro.STOCKTON_CALIFORNIA:
            return stockton_california()
        if self is ExperienceCompanyLocationMetro.SUMTER_SOUTH_CAROLINA:
            return sumter_south_carolina()
        if self is ExperienceCompanyLocationMetro.SYRACUSE_NEW_YORK:
            return syracuse_new_york()
        if self is ExperienceCompanyLocationMetro.TALLAHASSEE_FLORIDA:
            return tallahassee_florida()
        if self is ExperienceCompanyLocationMetro.TAMPA_FLORIDA:
            return tampa_florida()
        if self is ExperienceCompanyLocationMetro.TERRE_HAUTE_INDIANA:
            return terre_haute_indiana()
        if self is ExperienceCompanyLocationMetro.TEXARKANA_TEXAS:
            return texarkana_texas()
        if self is ExperienceCompanyLocationMetro.TOLEDO_OHIO:
            return toledo_ohio()
        if self is ExperienceCompanyLocationMetro.TOPEKA_KANSAS:
            return topeka_kansas()
        if self is ExperienceCompanyLocationMetro.TRENTON_NEW_JERSEY:
            return trenton_new_jersey()
        if self is ExperienceCompanyLocationMetro.TUCSON_ARIZONA:
            return tucson_arizona()
        if self is ExperienceCompanyLocationMetro.TULSA_OKLAHOMA:
            return tulsa_oklahoma()
        if self is ExperienceCompanyLocationMetro.TUSCALOOSA_ALABAMA:
            return tuscaloosa_alabama()
        if self is ExperienceCompanyLocationMetro.TWIN_FALLS_IDAHO:
            return twin_falls_idaho()
        if self is ExperienceCompanyLocationMetro.TYLER_TEXAS:
            return tyler_texas()
        if self is ExperienceCompanyLocationMetro.URBAN_HONOLULU_HAWAII:
            return urban_honolulu_hawaii()
        if self is ExperienceCompanyLocationMetro.UTICA_NEW_YORK:
            return utica_new_york()
        if self is ExperienceCompanyLocationMetro.VALDOSTA_GEORGIA:
            return valdosta_georgia()
        if self is ExperienceCompanyLocationMetro.VALLEJO_CALIFORNIA:
            return vallejo_california()
        if self is ExperienceCompanyLocationMetro.VICTORIA_TEXAS:
            return victoria_texas()
        if self is ExperienceCompanyLocationMetro.VINELAND_NEW_JERSEY:
            return vineland_new_jersey()
        if self is ExperienceCompanyLocationMetro.VIRGINIA_BEACH_VIRGINIA:
            return virginia_beach_virginia()
        if self is ExperienceCompanyLocationMetro.VISALIA_CALIFORNIA:
            return visalia_california()
        if self is ExperienceCompanyLocationMetro.WACO_TEXAS:
            return waco_texas()
        if self is ExperienceCompanyLocationMetro.WALLA_WALLA_WASHINGTON:
            return walla_walla_washington()
        if self is ExperienceCompanyLocationMetro.WARNER_ROBINS_GEORGIA:
            return warner_robins_georgia()
        if self is ExperienceCompanyLocationMetro.WATERLOO_IOWA:
            return waterloo_iowa()
        if self is ExperienceCompanyLocationMetro.WATERTOWN_NEW_YORK:
            return watertown_new_york()
        if self is ExperienceCompanyLocationMetro.WAUSAU_WISCONSIN:
            return wausau_wisconsin()
        if self is ExperienceCompanyLocationMetro.WEIRTON_WEST_VIRGINIA:
            return weirton_west_virginia()
        if self is ExperienceCompanyLocationMetro.WENATCHEE_WASHINGTON:
            return wenatchee_washington()
        if self is ExperienceCompanyLocationMetro.WHEELING_WEST_VIRGINIA:
            return wheeling_west_virginia()
        if self is ExperienceCompanyLocationMetro.WICHITA_FALLS_TEXAS:
            return wichita_falls_texas()
        if self is ExperienceCompanyLocationMetro.WICHITA_KANSAS:
            return wichita_kansas()
        if self is ExperienceCompanyLocationMetro.WILLIAMSPORT_PENNSYLVANIA:
            return williamsport_pennsylvania()
        if self is ExperienceCompanyLocationMetro.WILMINGTON_NORTH_CAROLINA:
            return wilmington_north_carolina()
        if self is ExperienceCompanyLocationMetro.WINCHESTER_VIRGINIA:
            return winchester_virginia()
        if self is ExperienceCompanyLocationMetro.WORCESTER_MASSACHUSETTS:
            return worcester_massachusetts()
        if self is ExperienceCompanyLocationMetro.YAKIMA_WASHINGTON:
            return yakima_washington()
        if self is ExperienceCompanyLocationMetro.YORK_PENNSYLVANIA:
            return york_pennsylvania()
        if self is ExperienceCompanyLocationMetro.YOUNGSTOWN_OHIO:
            return youngstown_ohio()
        if self is ExperienceCompanyLocationMetro.YUBA_CITY_CALIFORNIA:
            return yuba_city_california()
        if self is ExperienceCompanyLocationMetro.YUMA_ARIZONA:
            return yuma_arizona()
