

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWebhooksResponseDataItemTriggersItem(enum.StrEnum):
    RESPONSE_FINISHED = "responseFinished"
    RESPONSE_CREATED = "responseCreated"
    RESPONSE_UPDATED = "responseUpdated"

    def visit(
        self,
        response_finished: typing.Callable[[], T_Result],
        response_created: typing.Callable[[], T_Result],
        response_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWebhooksResponseDataItemTriggersItem.RESPONSE_FINISHED:
            return response_finished()
        if self is GetWebhooksResponseDataItemTriggersItem.RESPONSE_CREATED:
            return response_created()
        if self is GetWebhooksResponseDataItemTriggersItem.RESPONSE_UPDATED:
            return response_updated()
