

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GeoTarget(UniversalBaseModel):
    """
    Granular proxy geo-targeting request with country, optional subdivision, and optional city.
    """

    country: str = pydantic.Field()
    """
    ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB', 'DE')
    """

    subdivision: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 3166-2 subdivision code without country prefix (e.g., 'CA' for California, 'NY' for New York)
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City name in English from GeoNames (e.g., 'New York', 'Los Angeles', 'London')
    """

    is_isp: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isISP"),
        pydantic.Field(alias="isISP", description="Whether this geo target is marked as an ISP proxy location."),
    ] = None
    """
    Whether this geo target is marked as an ISP proxy location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
