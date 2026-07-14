

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link_type import LinkType


class AppPkgSubscriptionInfoLinks(UniversalBaseModel):
    """
    Links to resources related to this resource.
    """

    self_: typing_extensions.Annotated[LinkType, FieldMetadata(alias="self")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
