

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServiceDescription(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the service.
    """

    import_source_uri: str = pydantic.Field()
    """
    The URI of the source service description document used to load the service into OSDB.
    """

    service_id: str = pydantic.Field()
    """
    A unique one word identifier for the service.
    """

    service_name: str = pydantic.Field()
    """
    A word or phrase naming the service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
