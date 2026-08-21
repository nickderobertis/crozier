

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.medication import Medication


class GetMedicationResponse(UniversalBaseModel):
    status: typing.Optional[str] = None
    rows: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of rows that matched the search
    """

    data: typing.Optional[typing.List[Medication]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
