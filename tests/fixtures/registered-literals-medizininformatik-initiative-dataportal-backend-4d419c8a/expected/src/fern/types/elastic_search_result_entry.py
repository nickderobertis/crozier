

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry


class ElasticSearchResultEntry(UniversalBaseModel):
    display: typing.Optional[DisplayEntry] = None
    id: typing.Optional[str] = None
    availability: typing.Optional[int] = pydantic.Field(default=None)
    """
    How often is this available
    """

    context: typing.Optional[str] = None
    terminology: typing.Optional[str] = None
    termcode: typing.Optional[str] = None
    kds_module: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kdsModule"), pydantic.Field(alias="kdsModule")
    ] = None
    selectable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
