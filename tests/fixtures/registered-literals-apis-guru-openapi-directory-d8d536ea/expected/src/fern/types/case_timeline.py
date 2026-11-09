

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseTimeline(UniversalBaseModel):
    first_case_filed_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstCaseFiledDate"),
        pydantic.Field(
            alias="firstCaseFiledDate",
            description="The first date when the two entities have appeared together in the case. (These dates are determined from case filed dates)",
        ),
    ]
    """
    The first date when the two entities have appeared together in the case. (These dates are determined from case filed dates)
    """

    last_case_filed_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastCaseFiledDate"),
        pydantic.Field(
            alias="lastCaseFiledDate",
            description="The last date when the two entities have appeared together in the case. (These dates are determined from case filed dates)",
        ),
    ]
    """
    The last date when the two entities have appeared together in the case. (These dates are determined from case filed dates)
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
