

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_components import HealthComponents


class HealthResponse(UniversalBaseModel):
    components: HealthComponents = pydantic.Field()
    """
    Per-component health detail.
    """

    status: str = pydantic.Field()
    """
    Overall health of the API. Always 'ok' on a served response; component-level detail is in the components object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
