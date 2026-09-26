

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_components_dynamo import HealthComponentsDynamo
from .health_components_taxdata import HealthComponentsTaxdata


class HealthComponents(UniversalBaseModel):
    dynamo: HealthComponentsDynamo = pydantic.Field()
    """
    DynamoDB connectivity status: 'ok', 'config_error' (AWS config could not be loaded), or 'connection_error' (table could not be described).
    """

    taxdata: HealthComponentsTaxdata = pydantic.Field()
    """
    Tax-data cache status: 'ok', 'empty' (cache not loaded), or 'partial' (fewer than the expected number of records loaded).
    """

    taxdata_count: int = pydantic.Field()
    """
    Number of tax-data records currently loaded in the in-memory cache.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
