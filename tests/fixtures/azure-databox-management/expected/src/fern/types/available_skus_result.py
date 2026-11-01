

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sku_information import SkuInformation


class AvailableSkusResult(UniversalBaseModel):
    """
    The available skus operation response.
    """

    next_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextLink"),
        pydantic.Field(alias="nextLink", description="Link for the next set of skus."),
    ] = None
    """
    Link for the next set of skus.
    """

    value: typing.Optional[typing.List[SkuInformation]] = pydantic.Field(default=None)
    """
    List of available skus.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
