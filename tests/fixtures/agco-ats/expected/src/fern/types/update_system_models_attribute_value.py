

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsAttributeValue(UniversalBaseModel):
    key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Key"),
        pydantic.Field(
            alias="Key",
            description="The attribute name. Limit 50 characters. Attributes with names exceeding this limit will be ignored.",
        ),
    ]
    """
    The attribute name. Limit 50 characters. Attributes with names exceeding this limit will be ignored.
    """

    time_stamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="TimeStamp"),
        pydantic.Field(alias="TimeStamp", description="Read Only. The timestamp."),
    ] = None
    """
    Read Only. The timestamp.
    """

    value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Value"), pydantic.Field(alias="Value", description="The value")
    ] = None
    """
    The value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
