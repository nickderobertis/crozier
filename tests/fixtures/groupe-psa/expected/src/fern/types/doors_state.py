

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .doors_state_base import DoorsStateBase


class DoorsState(DoorsStateBase):
    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Date when the resource has been created."),
    ]
    """
    Date when the resource has been created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
