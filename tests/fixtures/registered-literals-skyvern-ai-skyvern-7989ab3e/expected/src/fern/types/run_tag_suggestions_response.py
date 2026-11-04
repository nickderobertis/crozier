

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunTagSuggestionsResponse(UniversalBaseModel):
    """
    Response for ``GET /v1/run-tag-suggestions``: distinct (key, value) pairs
    ever set on a run for the org, sourced from the event log rather than the
    tag-key/tag-value registry so reserved ``skyvern.*`` system keys (never
    registered) reach the pickers too.
    """

    keys: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Distinct grouped tag keys seen on runs.
    """

    values_by_key: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    Values seen for each grouped key.
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Distinct standalone (keyless) labels seen on runs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
