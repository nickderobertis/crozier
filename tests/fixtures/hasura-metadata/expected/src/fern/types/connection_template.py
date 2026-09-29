

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectionTemplate(UniversalBaseModel):
    """
    https://hasura.io/docs/latest/graphql/core/api-reference/syntax-defs.html#pgconnectiontemplate
    """

    template: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Connection kriti template (read more in the docs)
    KritiTemplate
    """

    version: typing.Optional[float] = pydantic.Field(default=None)
    """
    Optional connection template version (supported versions: [1], default: 1)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
