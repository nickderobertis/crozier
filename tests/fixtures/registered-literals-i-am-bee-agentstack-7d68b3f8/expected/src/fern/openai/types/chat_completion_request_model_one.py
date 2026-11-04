

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRequestModelOne(enum.StrEnum):
    GPT52 = "gpt-5.2"
    GPT5220251211 = "gpt-5.2-2025-12-11"
    GPT52CHAT_LATEST = "gpt-5.2-chat-latest"
    GPT52PRO = "gpt-5.2-pro"
    GPT52PRO20251211 = "gpt-5.2-pro-2025-12-11"
    GPT51 = "gpt-5.1"
    GPT5120251113 = "gpt-5.1-2025-11-13"
    GPT51CODEX = "gpt-5.1-codex"
    GPT51MINI = "gpt-5.1-mini"
    GPT51CHAT_LATEST = "gpt-5.1-chat-latest"
    GPT5 = "gpt-5"
    GPT5MINI = "gpt-5-mini"
    GPT5NANO = "gpt-5-nano"
    GPT520250807 = "gpt-5-2025-08-07"
    GPT5MINI20250807 = "gpt-5-mini-2025-08-07"
    GPT5NANO20250807 = "gpt-5-nano-2025-08-07"
    GPT5CHAT_LATEST = "gpt-5-chat-latest"
    GPT41 = "gpt-4.1"
    GPT41MINI = "gpt-4.1-mini"
    GPT41NANO = "gpt-4.1-nano"
    GPT4120250414 = "gpt-4.1-2025-04-14"
    GPT41MINI20250414 = "gpt-4.1-mini-2025-04-14"
    GPT41NANO20250414 = "gpt-4.1-nano-2025-04-14"
    O4MINI = "o4-mini"
    O4MINI20250416 = "o4-mini-2025-04-16"
    O3 = "o3"
    O320250416 = "o3-2025-04-16"
    O3MINI = "o3-mini"
    O3MINI20250131 = "o3-mini-2025-01-31"
    O1 = "o1"
    O120241217 = "o1-2024-12-17"
    O1PREVIEW = "o1-preview"
    O1PREVIEW20240912 = "o1-preview-2024-09-12"
    O1MINI = "o1-mini"
    O1MINI20240912 = "o1-mini-2024-09-12"
    GPT4O = "gpt-4o"
    GPT4O20241120 = "gpt-4o-2024-11-20"
    GPT4O20240806 = "gpt-4o-2024-08-06"
    GPT4O20240513 = "gpt-4o-2024-05-13"
    GPT4O_AUDIO_PREVIEW = "gpt-4o-audio-preview"
    GPT4O_AUDIO_PREVIEW20241001 = "gpt-4o-audio-preview-2024-10-01"
    GPT4O_AUDIO_PREVIEW20241217 = "gpt-4o-audio-preview-2024-12-17"
    GPT4O_AUDIO_PREVIEW20250603 = "gpt-4o-audio-preview-2025-06-03"
    GPT4O_MINI_AUDIO_PREVIEW = "gpt-4o-mini-audio-preview"
    GPT4O_MINI_AUDIO_PREVIEW20241217 = "gpt-4o-mini-audio-preview-2024-12-17"
    GPT4O_SEARCH_PREVIEW = "gpt-4o-search-preview"
    GPT4O_MINI_SEARCH_PREVIEW = "gpt-4o-mini-search-preview"
    GPT4O_SEARCH_PREVIEW20250311 = "gpt-4o-search-preview-2025-03-11"
    GPT4O_MINI_SEARCH_PREVIEW20250311 = "gpt-4o-mini-search-preview-2025-03-11"
    CHATGPT4O_LATEST = "chatgpt-4o-latest"
    CODEX_MINI_LATEST = "codex-mini-latest"
    GPT4O_MINI = "gpt-4o-mini"
    GPT4O_MINI20240718 = "gpt-4o-mini-2024-07-18"
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
    GPT35TURBO0301 = "gpt-3.5-turbo-0301"
    GPT35TURBO0613 = "gpt-3.5-turbo-0613"
    GPT35TURBO1106 = "gpt-3.5-turbo-1106"
    GPT35TURBO0125 = "gpt-3.5-turbo-0125"
    GPT35TURBO16K0613 = "gpt-3.5-turbo-16k-0613"

    def visit(
        self,
        gpt52: typing.Callable[[], T_Result],
        gpt5220251211: typing.Callable[[], T_Result],
        gpt52chat_latest: typing.Callable[[], T_Result],
        gpt52pro: typing.Callable[[], T_Result],
        gpt52pro20251211: typing.Callable[[], T_Result],
        gpt51: typing.Callable[[], T_Result],
        gpt5120251113: typing.Callable[[], T_Result],
        gpt51codex: typing.Callable[[], T_Result],
        gpt51mini: typing.Callable[[], T_Result],
        gpt51chat_latest: typing.Callable[[], T_Result],
        gpt5: typing.Callable[[], T_Result],
        gpt5mini: typing.Callable[[], T_Result],
        gpt5nano: typing.Callable[[], T_Result],
        gpt520250807: typing.Callable[[], T_Result],
        gpt5mini20250807: typing.Callable[[], T_Result],
        gpt5nano20250807: typing.Callable[[], T_Result],
        gpt5chat_latest: typing.Callable[[], T_Result],
        gpt41: typing.Callable[[], T_Result],
        gpt41mini: typing.Callable[[], T_Result],
        gpt41nano: typing.Callable[[], T_Result],
        gpt4120250414: typing.Callable[[], T_Result],
        gpt41mini20250414: typing.Callable[[], T_Result],
        gpt41nano20250414: typing.Callable[[], T_Result],
        o4mini: typing.Callable[[], T_Result],
        o4mini20250416: typing.Callable[[], T_Result],
        o3: typing.Callable[[], T_Result],
        o320250416: typing.Callable[[], T_Result],
        o3mini: typing.Callable[[], T_Result],
        o3mini20250131: typing.Callable[[], T_Result],
        o1: typing.Callable[[], T_Result],
        o120241217: typing.Callable[[], T_Result],
        o1preview: typing.Callable[[], T_Result],
        o1preview20240912: typing.Callable[[], T_Result],
        o1mini: typing.Callable[[], T_Result],
        o1mini20240912: typing.Callable[[], T_Result],
        gpt4o: typing.Callable[[], T_Result],
        gpt4o20241120: typing.Callable[[], T_Result],
        gpt4o20240806: typing.Callable[[], T_Result],
        gpt4o20240513: typing.Callable[[], T_Result],
        gpt4o_audio_preview: typing.Callable[[], T_Result],
        gpt4o_audio_preview20241001: typing.Callable[[], T_Result],
        gpt4o_audio_preview20241217: typing.Callable[[], T_Result],
        gpt4o_audio_preview20250603: typing.Callable[[], T_Result],
        gpt4o_mini_audio_preview: typing.Callable[[], T_Result],
        gpt4o_mini_audio_preview20241217: typing.Callable[[], T_Result],
        gpt4o_search_preview: typing.Callable[[], T_Result],
        gpt4o_mini_search_preview: typing.Callable[[], T_Result],
        gpt4o_search_preview20250311: typing.Callable[[], T_Result],
        gpt4o_mini_search_preview20250311: typing.Callable[[], T_Result],
        chatgpt4o_latest: typing.Callable[[], T_Result],
        codex_mini_latest: typing.Callable[[], T_Result],
        gpt4o_mini: typing.Callable[[], T_Result],
        gpt4o_mini20240718: typing.Callable[[], T_Result],
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
        gpt35turbo0301: typing.Callable[[], T_Result],
        gpt35turbo0613: typing.Callable[[], T_Result],
        gpt35turbo1106: typing.Callable[[], T_Result],
        gpt35turbo0125: typing.Callable[[], T_Result],
        gpt35turbo16k0613: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionRequestModelOne.GPT52:
            return gpt52()
        if self is ChatCompletionRequestModelOne.GPT5220251211:
            return gpt5220251211()
        if self is ChatCompletionRequestModelOne.GPT52CHAT_LATEST:
            return gpt52chat_latest()
        if self is ChatCompletionRequestModelOne.GPT52PRO:
            return gpt52pro()
        if self is ChatCompletionRequestModelOne.GPT52PRO20251211:
            return gpt52pro20251211()
        if self is ChatCompletionRequestModelOne.GPT51:
            return gpt51()
        if self is ChatCompletionRequestModelOne.GPT5120251113:
            return gpt5120251113()
        if self is ChatCompletionRequestModelOne.GPT51CODEX:
            return gpt51codex()
        if self is ChatCompletionRequestModelOne.GPT51MINI:
            return gpt51mini()
        if self is ChatCompletionRequestModelOne.GPT51CHAT_LATEST:
            return gpt51chat_latest()
        if self is ChatCompletionRequestModelOne.GPT5:
            return gpt5()
        if self is ChatCompletionRequestModelOne.GPT5MINI:
            return gpt5mini()
        if self is ChatCompletionRequestModelOne.GPT5NANO:
            return gpt5nano()
        if self is ChatCompletionRequestModelOne.GPT520250807:
            return gpt520250807()
        if self is ChatCompletionRequestModelOne.GPT5MINI20250807:
            return gpt5mini20250807()
        if self is ChatCompletionRequestModelOne.GPT5NANO20250807:
            return gpt5nano20250807()
        if self is ChatCompletionRequestModelOne.GPT5CHAT_LATEST:
            return gpt5chat_latest()
        if self is ChatCompletionRequestModelOne.GPT41:
            return gpt41()
        if self is ChatCompletionRequestModelOne.GPT41MINI:
            return gpt41mini()
        if self is ChatCompletionRequestModelOne.GPT41NANO:
            return gpt41nano()
        if self is ChatCompletionRequestModelOne.GPT4120250414:
            return gpt4120250414()
        if self is ChatCompletionRequestModelOne.GPT41MINI20250414:
            return gpt41mini20250414()
        if self is ChatCompletionRequestModelOne.GPT41NANO20250414:
            return gpt41nano20250414()
        if self is ChatCompletionRequestModelOne.O4MINI:
            return o4mini()
        if self is ChatCompletionRequestModelOne.O4MINI20250416:
            return o4mini20250416()
        if self is ChatCompletionRequestModelOne.O3:
            return o3()
        if self is ChatCompletionRequestModelOne.O320250416:
            return o320250416()
        if self is ChatCompletionRequestModelOne.O3MINI:
            return o3mini()
        if self is ChatCompletionRequestModelOne.O3MINI20250131:
            return o3mini20250131()
        if self is ChatCompletionRequestModelOne.O1:
            return o1()
        if self is ChatCompletionRequestModelOne.O120241217:
            return o120241217()
        if self is ChatCompletionRequestModelOne.O1PREVIEW:
            return o1preview()
        if self is ChatCompletionRequestModelOne.O1PREVIEW20240912:
            return o1preview20240912()
        if self is ChatCompletionRequestModelOne.O1MINI:
            return o1mini()
        if self is ChatCompletionRequestModelOne.O1MINI20240912:
            return o1mini20240912()
        if self is ChatCompletionRequestModelOne.GPT4O:
            return gpt4o()
        if self is ChatCompletionRequestModelOne.GPT4O20241120:
            return gpt4o20241120()
        if self is ChatCompletionRequestModelOne.GPT4O20240806:
            return gpt4o20240806()
        if self is ChatCompletionRequestModelOne.GPT4O20240513:
            return gpt4o20240513()
        if self is ChatCompletionRequestModelOne.GPT4O_AUDIO_PREVIEW:
            return gpt4o_audio_preview()
        if self is ChatCompletionRequestModelOne.GPT4O_AUDIO_PREVIEW20241001:
            return gpt4o_audio_preview20241001()
        if self is ChatCompletionRequestModelOne.GPT4O_AUDIO_PREVIEW20241217:
            return gpt4o_audio_preview20241217()
        if self is ChatCompletionRequestModelOne.GPT4O_AUDIO_PREVIEW20250603:
            return gpt4o_audio_preview20250603()
        if self is ChatCompletionRequestModelOne.GPT4O_MINI_AUDIO_PREVIEW:
            return gpt4o_mini_audio_preview()
        if self is ChatCompletionRequestModelOne.GPT4O_MINI_AUDIO_PREVIEW20241217:
            return gpt4o_mini_audio_preview20241217()
        if self is ChatCompletionRequestModelOne.GPT4O_SEARCH_PREVIEW:
            return gpt4o_search_preview()
        if self is ChatCompletionRequestModelOne.GPT4O_MINI_SEARCH_PREVIEW:
            return gpt4o_mini_search_preview()
        if self is ChatCompletionRequestModelOne.GPT4O_SEARCH_PREVIEW20250311:
            return gpt4o_search_preview20250311()
        if self is ChatCompletionRequestModelOne.GPT4O_MINI_SEARCH_PREVIEW20250311:
            return gpt4o_mini_search_preview20250311()
        if self is ChatCompletionRequestModelOne.CHATGPT4O_LATEST:
            return chatgpt4o_latest()
        if self is ChatCompletionRequestModelOne.CODEX_MINI_LATEST:
            return codex_mini_latest()
        if self is ChatCompletionRequestModelOne.GPT4O_MINI:
            return gpt4o_mini()
        if self is ChatCompletionRequestModelOne.GPT4O_MINI20240718:
            return gpt4o_mini20240718()
        if self is ChatCompletionRequestModelOne.GPT4TURBO:
            return gpt4turbo()
        if self is ChatCompletionRequestModelOne.GPT4TURBO20240409:
            return gpt4turbo20240409()
        if self is ChatCompletionRequestModelOne.GPT40125PREVIEW:
            return gpt40125preview()
        if self is ChatCompletionRequestModelOne.GPT4TURBO_PREVIEW:
            return gpt4turbo_preview()
        if self is ChatCompletionRequestModelOne.GPT41106PREVIEW:
            return gpt41106preview()
        if self is ChatCompletionRequestModelOne.GPT4VISION_PREVIEW:
            return gpt4vision_preview()
        if self is ChatCompletionRequestModelOne.GPT4:
            return gpt4()
        if self is ChatCompletionRequestModelOne.GPT40314:
            return gpt40314()
        if self is ChatCompletionRequestModelOne.GPT40613:
            return gpt40613()
        if self is ChatCompletionRequestModelOne.GPT432K:
            return gpt432k()
        if self is ChatCompletionRequestModelOne.GPT432K0314:
            return gpt432k0314()
        if self is ChatCompletionRequestModelOne.GPT432K0613:
            return gpt432k0613()
        if self is ChatCompletionRequestModelOne.GPT35TURBO:
            return gpt35turbo()
        if self is ChatCompletionRequestModelOne.GPT35TURBO16K:
            return gpt35turbo16k()
        if self is ChatCompletionRequestModelOne.GPT35TURBO0301:
            return gpt35turbo0301()
        if self is ChatCompletionRequestModelOne.GPT35TURBO0613:
            return gpt35turbo0613()
        if self is ChatCompletionRequestModelOne.GPT35TURBO1106:
            return gpt35turbo1106()
        if self is ChatCompletionRequestModelOne.GPT35TURBO0125:
            return gpt35turbo0125()
        if self is ChatCompletionRequestModelOne.GPT35TURBO16K0613:
            return gpt35turbo16k0613()
