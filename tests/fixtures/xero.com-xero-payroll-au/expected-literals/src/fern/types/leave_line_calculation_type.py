

import typing

LeaveLineCalculationType = typing.Union[
    typing.Literal[
        "NOCALCULATIONREQUIRED", "FIXEDAMOUNTEACHPERIOD", "ENTERRATEINPAYTEMPLATE", "BASEDONORDINARYEARNINGS", ""
    ],
    typing.Any,
]
