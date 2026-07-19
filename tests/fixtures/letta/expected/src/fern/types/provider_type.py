

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderType(enum.StrEnum):
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    BEDROCK = "bedrock"
    CEREBRAS = "cerebras"
    CHATGPT_OAUTH = "chatgpt_oauth"
    DEEPSEEK = "deepseek"
    GOOGLE_AI = "google_ai"
    GOOGLE_VERTEX = "google_vertex"
    GROQ = "groq"
    HUGGING_FACE = "hugging-face"
    LETTA = "letta"
    LMSTUDIO_OPENAI = "lmstudio_openai"
    MISTRAL = "mistral"
    OLLAMA = "ollama"
    OPENAI = "openai"
    TOGETHER = "together"
    VLLM = "vllm"
    SGLANG = "sglang"
    XAI = "xai"
    ZAI = "zai"

    def visit(
        self,
        anthropic: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        bedrock: typing.Callable[[], T_Result],
        cerebras: typing.Callable[[], T_Result],
        chatgpt_oauth: typing.Callable[[], T_Result],
        deepseek: typing.Callable[[], T_Result],
        google_ai: typing.Callable[[], T_Result],
        google_vertex: typing.Callable[[], T_Result],
        groq: typing.Callable[[], T_Result],
        hugging_face: typing.Callable[[], T_Result],
        letta: typing.Callable[[], T_Result],
        lmstudio_openai: typing.Callable[[], T_Result],
        mistral: typing.Callable[[], T_Result],
        ollama: typing.Callable[[], T_Result],
        openai: typing.Callable[[], T_Result],
        together: typing.Callable[[], T_Result],
        vllm: typing.Callable[[], T_Result],
        sglang: typing.Callable[[], T_Result],
        xai: typing.Callable[[], T_Result],
        zai: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderType.ANTHROPIC:
            return anthropic()
        if self is ProviderType.AZURE:
            return azure()
        if self is ProviderType.BEDROCK:
            return bedrock()
        if self is ProviderType.CEREBRAS:
            return cerebras()
        if self is ProviderType.CHATGPT_OAUTH:
            return chatgpt_oauth()
        if self is ProviderType.DEEPSEEK:
            return deepseek()
        if self is ProviderType.GOOGLE_AI:
            return google_ai()
        if self is ProviderType.GOOGLE_VERTEX:
            return google_vertex()
        if self is ProviderType.GROQ:
            return groq()
        if self is ProviderType.HUGGING_FACE:
            return hugging_face()
        if self is ProviderType.LETTA:
            return letta()
        if self is ProviderType.LMSTUDIO_OPENAI:
            return lmstudio_openai()
        if self is ProviderType.MISTRAL:
            return mistral()
        if self is ProviderType.OLLAMA:
            return ollama()
        if self is ProviderType.OPENAI:
            return openai()
        if self is ProviderType.TOGETHER:
            return together()
        if self is ProviderType.VLLM:
            return vllm()
        if self is ProviderType.SGLANG:
            return sglang()
        if self is ProviderType.XAI:
            return xai()
        if self is ProviderType.ZAI:
            return zai()
