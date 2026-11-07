

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstitutionsListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the institution entity.
    """

    auth_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Url used to authenticate institution specific login.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the institution.
    """

    logo_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Static path to the institution specific logo.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
