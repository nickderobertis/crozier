

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .v1label_tic import V1LabelTic


class V1Label(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the label
    """

    name: str = pydantic.Field()
    """
    Name of the label
    """

    sequence: int = pydantic.Field()
    """
    Sequence order for the label
    """

    parent_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Parent label ID for hierarchical labels
    """

    emoji: typing.Optional[str] = pydantic.Field(default=None)
    """
    Emoji identifier for the label
    """

    active: bool = pydantic.Field()
    """
    Whether the label is active (false means archived)
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External ID for mapping with external systems (alphanumeric with underscores, max 512 chars)
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO8601 timestamp of when the label was created
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO8601 timestamp of when the label was last updated
    """

    tic: typing.Optional[V1LabelTic] = pydantic.Field(default=None)
    """
    Integration metadata (internal only). Present for synced labels.
    """

    children: typing.Optional[typing.List["V1Label"]] = pydantic.Field(default=None)
    """
    Child labels in the hierarchy (recursive structure)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(V1Label)
