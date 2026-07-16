

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VoiceV1ByocTrunkStatusCallbackMethod(str, enum.Enum):
    """
    The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`.
    """

    HEAD = "HEAD"
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"

    def visit(
        self,
        head: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VoiceV1ByocTrunkStatusCallbackMethod.HEAD:
            return head()
        if self is VoiceV1ByocTrunkStatusCallbackMethod.GET:
            return get()
        if self is VoiceV1ByocTrunkStatusCallbackMethod.POST:
            return post()
        if self is VoiceV1ByocTrunkStatusCallbackMethod.PATCH:
            return patch()
        if self is VoiceV1ByocTrunkStatusCallbackMethod.PUT:
            return put()
        if self is VoiceV1ByocTrunkStatusCallbackMethod.DELETE:
            return delete()
