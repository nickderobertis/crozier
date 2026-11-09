

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JudgeType(UniversalBaseModel):
    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate",
            description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.",
        ),
    ]
    """
    The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    """

    judge_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="judgeTypeId"), pydantic.Field(alias="judgeTypeId")
    ]
    name: str
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
