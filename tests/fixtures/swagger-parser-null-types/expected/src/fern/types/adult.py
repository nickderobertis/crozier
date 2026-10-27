

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .child import Child


class Adult(UniversalBaseModel):
    """
    A representation of an adult
    """

    children: typing.Optional[typing.List[Child]] = None
    nullable_children: typing_extensions.Annotated[
        typing.Optional[typing.List[Child]],
        FieldMetadata(alias="nullableChildren"),
        pydantic.Field(alias="nullableChildren"),
    ] = None
    nullable_children_variant2: typing_extensions.Annotated[
        typing.Optional[typing.List[Child]],
        FieldMetadata(alias="nullableChildrenVariant2"),
        pydantic.Field(alias="nullableChildrenVariant2"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
