

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipActionDeleteOrganization(UniversalBaseModel):
    """
    Action: Delete an organization.
    """

    instance: str = pydantic.Field()
    """
    Glitchtip instance name
    """

    organization: str = pydantic.Field()
    """
    Organization name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
