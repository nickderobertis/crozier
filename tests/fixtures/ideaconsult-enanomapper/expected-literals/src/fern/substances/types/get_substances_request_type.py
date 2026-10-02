

import typing

GetSubstancesRequestType = typing.Union[
    typing.Literal[
        "substancetype",
        "name",
        "like",
        "regexp",
        "uuif",
        "CompTox",
        "DOI",
        "reliability",
        "purposeFlag",
        "studyResultType",
        "isRobustStudy",
        "citation",
        "citationowner",
        "topcategory",
        "endpointcategory",
        "params",
        "owner_name",
        "owner_uuid",
        "related",
        "reference",
        "facet",
    ],
    typing.Any,
]
