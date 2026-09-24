

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DischargeState(UniversalBaseModel):
    current_limit: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="currentLimit"),
        pydantic.Field(alias="currentLimit", description="The current limit of the discharge"),
    ]
    """
    The current limit of the discharge
    """

    enabled: bool = pydantic.Field()
    """
    Whether the discharge is enabled
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the discharge"),
    ]
    """
    The updated at time of the discharge
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
