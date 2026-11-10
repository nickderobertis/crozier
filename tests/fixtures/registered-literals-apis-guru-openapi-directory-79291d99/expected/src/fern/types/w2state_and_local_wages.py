

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class W2StateAndLocalWages(UniversalBaseModel):
    """
    W2 state and local wages
    """

    employer_state_id_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    State identification number of the employer.
    """

    local_income_tax: typing.Optional[str] = pydantic.Field(default=None)
    """
    Income tax from the locality.
    """

    local_wages_tips: typing.Optional[str] = pydantic.Field(default=None)
    """
    Wages and tips from the locality.
    """

    locality_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the locality.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State associated with the wage.
    """

    state_income_tax: typing.Optional[str] = pydantic.Field(default=None)
    """
    Income tax from the specified state.
    """

    state_wages_tips: typing.Optional[str] = pydantic.Field(default=None)
    """
    Wages and tips from the specified state.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
