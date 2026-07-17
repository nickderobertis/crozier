

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FeaturesConfigRepositoryFilter(UniversalBaseModel):
    """
    Repository filtering feature properties
    """

    enabled: typing.Optional[str] = None
    label_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="label-key"), pydantic.Field(alias="label-key")
    ] = None
    label_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="label-label"), pydantic.Field(alias="label-label")
    ] = None
    label_list: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="label-list"), pydantic.Field(alias="label-list")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
