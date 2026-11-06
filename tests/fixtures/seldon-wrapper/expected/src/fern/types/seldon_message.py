

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .default_data import DefaultData
from .meta import Meta
from .status import Status


class SeldonMessage(UniversalBaseModel):
    bin_data: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="binData"), pydantic.Field(alias="binData")
    ] = None
    data: typing.Optional[DefaultData] = None
    meta: typing.Optional[Meta] = None
    status: typing.Optional[Status] = None
    str_data: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="strData"), pydantic.Field(alias="strData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(SeldonMessage)
