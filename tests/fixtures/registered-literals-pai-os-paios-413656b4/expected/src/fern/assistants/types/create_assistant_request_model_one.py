

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAssistantRequestModelOne(enum.StrEnum):
    GPT4TURBO = "gpt-4-turbo"
    GPT4TURBO20240409 = "gpt-4-turbo-2024-04-09"
    GPT40125PREVIEW = "gpt-4-0125-preview"
    GPT4TURBO_PREVIEW = "gpt-4-turbo-preview"
    GPT41106PREVIEW = "gpt-4-1106-preview"
    GPT4VISION_PREVIEW = "gpt-4-vision-preview"
    GPT4 = "gpt-4"
    GPT40314 = "gpt-4-0314"
    GPT40613 = "gpt-4-0613"
    GPT432K = "gpt-4-32k"
    GPT432K0314 = "gpt-4-32k-0314"
    GPT432K0613 = "gpt-4-32k-0613"
    GPT35TURBO = "gpt-3.5-turbo"
    GPT35TURBO16K = "gpt-3.5-turbo-16k"
    GPT35TURBO0613 = "gpt-3.5-turbo-0613"
    GPT35TURBO1106 = "gpt-3.5-turbo-1106"
    GPT35TURBO0125 = "gpt-3.5-turbo-0125"
    GPT35TURBO16K0613 = "gpt-3.5-turbo-16k-0613"

    def visit(
        self,
        gpt4turbo: typing.Callable[[], T_Result],
        gpt4turbo20240409: typing.Callable[[], T_Result],
        gpt40125preview: typing.Callable[[], T_Result],
        gpt4turbo_preview: typing.Callable[[], T_Result],
        gpt41106preview: typing.Callable[[], T_Result],
        gpt4vision_preview: typing.Callable[[], T_Result],
        gpt4: typing.Callable[[], T_Result],
        gpt40314: typing.Callable[[], T_Result],
        gpt40613: typing.Callable[[], T_Result],
        gpt432k: typing.Callable[[], T_Result],
        gpt432k0314: typing.Callable[[], T_Result],
        gpt432k0613: typing.Callable[[], T_Result],
        gpt35turbo: typing.Callable[[], T_Result],
        gpt35turbo16k: typing.Callable[[], T_Result],
        gpt35turbo0613: typing.Callable[[], T_Result],
        gpt35turbo1106: typing.Callable[[], T_Result],
        gpt35turbo0125: typing.Callable[[], T_Result],
        gpt35turbo16k0613: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateAssistantRequestModelOne.GPT4TURBO:
            return gpt4turbo()
        if self is CreateAssistantRequestModelOne.GPT4TURBO20240409:
            return gpt4turbo20240409()
        if self is CreateAssistantRequestModelOne.GPT40125PREVIEW:
            return gpt40125preview()
        if self is CreateAssistantRequestModelOne.GPT4TURBO_PREVIEW:
            return gpt4turbo_preview()
        if self is CreateAssistantRequestModelOne.GPT41106PREVIEW:
            return gpt41106preview()
        if self is CreateAssistantRequestModelOne.GPT4VISION_PREVIEW:
            return gpt4vision_preview()
        if self is CreateAssistantRequestModelOne.GPT4:
            return gpt4()
        if self is CreateAssistantRequestModelOne.GPT40314:
            return gpt40314()
        if self is CreateAssistantRequestModelOne.GPT40613:
            return gpt40613()
        if self is CreateAssistantRequestModelOne.GPT432K:
            return gpt432k()
        if self is CreateAssistantRequestModelOne.GPT432K0314:
            return gpt432k0314()
        if self is CreateAssistantRequestModelOne.GPT432K0613:
            return gpt432k0613()
        if self is CreateAssistantRequestModelOne.GPT35TURBO:
            return gpt35turbo()
        if self is CreateAssistantRequestModelOne.GPT35TURBO16K:
            return gpt35turbo16k()
        if self is CreateAssistantRequestModelOne.GPT35TURBO0613:
            return gpt35turbo0613()
        if self is CreateAssistantRequestModelOne.GPT35TURBO1106:
            return gpt35turbo1106()
        if self is CreateAssistantRequestModelOne.GPT35TURBO0125:
            return gpt35turbo0125()
        if self is CreateAssistantRequestModelOne.GPT35TURBO16K0613:
            return gpt35turbo16k0613()
