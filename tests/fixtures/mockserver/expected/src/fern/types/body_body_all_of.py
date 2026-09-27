

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .body_body_all_of_type import BodyBodyAllOfType


class BodyBodyAllOf(UniversalBaseModel):
    """
    all-of body matcher — matches only when every one of its component body matchers matches the same request body
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    optional: typing.Optional[bool] = None
    type: typing.Optional[BodyBodyAllOfType] = None
    body_all_of: typing_extensions.Annotated[
        typing.List["Body"], FieldMetadata(alias="bodyAllOf"), pydantic.Field(alias="bodyAllOf")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .body import Body

update_forward_refs(BodyBodyAllOf, Body=Body)
