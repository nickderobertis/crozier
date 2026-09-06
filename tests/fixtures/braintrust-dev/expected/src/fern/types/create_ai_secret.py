

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateAiSecret(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the AI secret
    """

    type: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secret value. If omitted in a PUT request, the existing secret value will be left intact, not replaced with null.
    """

    org_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
