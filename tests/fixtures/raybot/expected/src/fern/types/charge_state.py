

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChargeState(UniversalBaseModel):
    current_limit: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="currentLimit"),
        pydantic.Field(alias="currentLimit", description="The current limit of the charge"),
    ]
    """
    The current limit of the charge
    """

    enabled: bool = pydantic.Field()
    """
    Whether the charge is enabled
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the charge"),
    ]
    """
    The updated at time of the charge
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
