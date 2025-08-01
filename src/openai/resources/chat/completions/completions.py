# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import inspect
from typing import Dict, List, Type, Union, Iterable, Optional, cast
from functools import partial
from typing_extensions import Literal, overload

import httpx
import pydantic

from .... import _legacy_response
from .messages import (
    Messages,
    AsyncMessages,
    MessagesWithRawResponse,
    AsyncMessagesWithRawResponse,
    MessagesWithStreamingResponse,
    AsyncMessagesWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._streaming import Stream, AsyncStream
from ....pagination import SyncCursorPage, AsyncCursorPage
from ....types.chat import (
    ChatCompletionAudioParam,
    completion_list_params,
    completion_create_params,
    completion_update_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....lib._parsing import (
    ResponseFormatT,
    validate_input_tools as _validate_input_tools,
    parse_chat_completion as _parse_chat_completion,
    type_to_response_format_param as _type_to_response_format,
)
from ....lib.streaming.chat import ChatCompletionStreamManager, AsyncChatCompletionStreamManager
from ....types.shared.chat_model import ChatModel
from ....types.chat.chat_completion import ChatCompletion
from ....types.shared_params.metadata import Metadata
from ....types.shared.reasoning_effort import ReasoningEffort
from ....types.chat.chat_completion_chunk import ChatCompletionChunk
from ....types.chat.parsed_chat_completion import ParsedChatCompletion
from ....types.chat.chat_completion_deleted import ChatCompletionDeleted
from ....types.chat.chat_completion_tool_param import ChatCompletionToolParam
from ....types.chat.chat_completion_audio_param import ChatCompletionAudioParam
from ....types.chat.chat_completion_message_param import ChatCompletionMessageParam
from ....types.chat.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from ....types.chat.chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
from ....types.chat.chat_completion_tool_choice_option_param import ChatCompletionToolChoiceOptionParam

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    @cached_property
    def messages(self) -> Messages:
        return Messages(self._client)

    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/openai/openai-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/openai/openai-python#with_streaming_response
        """
        return CompletionsWithStreamingResponse(self)

    def parse(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        response_format: type[ResponseFormatT] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParsedChatCompletion[ResponseFormatT]:
        """Wrapper over the `client.chat.completions.create()` method that provides richer integrations with Python specific types
        & returns a `ParsedChatCompletion` object, which is a subclass of the standard `ChatCompletion` class.

        You can pass a pydantic model to this method and it will automatically convert the model
        into a JSON schema, send it to the API and parse the response content back into the given model.

        This method will also automatically parse `function` tool calls if:
        - You use the `openai.pydantic_function_tool()` helper method
        - You mark your tool schema with `"strict": True`

        Example usage:
        ```py
        from pydantic import BaseModel
        from openai import OpenAI


        class Step(BaseModel):
            explanation: str
            output: str


        class MathResponse(BaseModel):
            steps: List[Step]
            final_answer: str


        client = OpenAI()
        completion = client.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor."},
                {"role": "user", "content": "solve 8x + 31 = 2"},
            ],
            response_format=MathResponse,
        )

        message = completion.choices[0].message
        if message.parsed:
            print(message.parsed.steps)
            print("answer: ", message.parsed.final_answer)
        ```
        """
        _validate_input_tools(tools)

        extra_headers = {
            "X-Stainless-Helper-Method": "chat.completions.parse",
            **(extra_headers or {}),
        }

        def parser(raw_completion: ChatCompletion) -> ParsedChatCompletion[ResponseFormatT]:
            return _parse_chat_completion(
                response_format=response_format,
                chat_completion=raw_completion,
                input_tools=tools,
            )

        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "response_format": _type_to_response_format(response_format),
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": False,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=parser,
            ),
            # we turn the `ChatCompletion` instance into a `ParsedChatCompletion`
            # in the `parser` function above
            cast_to=cast(Type[ParsedChatCompletion[ResponseFormatT]], ChatCompletion),
            stream=False,
        )

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.openai.com/docs/api-reference/responses) to take
        advantage of the latest OpenAI platform features. Compare
        [Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by OpenAI to cache responses for similar requests to optimize your cache
              hit rates. Replaces the `user` field.
              [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating OpenAI's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

              - If set to 'auto', then the request will be processed with the service tier
                configured in the Project settings. Unless otherwise configured, the Project
                will use 'default'.
              - If set to 'default', then the request will be processed with the standard
                pricing and performance for the selected model.
              - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
                'priority', then the request will be processed with the corresponding service
                tier. [Contact sales](https://openai.com/contact-sales) to learn more about
                Priority processing.
              - When not set, the default behavior is 'auto'.

              When the `service_tier` parameter is set, the response body will include the
              `service_tier` value based on the processing mode actually used to serve the
              request. This response value may be different from the value set in the
              parameter.

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 10MB will be dropped.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help OpenAI detect and prevent abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: Literal[True],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionChunk]:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.openai.com/docs/api-reference/responses) to take
        advantage of the latest OpenAI platform features. Compare
        [Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by OpenAI to cache responses for similar requests to optimize your cache
              hit rates. Replaces the `user` field.
              [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating OpenAI's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

              - If set to 'auto', then the request will be processed with the service tier
                configured in the Project settings. Unless otherwise configured, the Project
                will use 'default'.
              - If set to 'default', then the request will be processed with the standard
                pricing and performance for the selected model.
              - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
                'priority', then the request will be processed with the corresponding service
                tier. [Contact sales](https://openai.com/contact-sales) to learn more about
                Priority processing.
              - When not set, the default behavior is 'auto'.

              When the `service_tier` parameter is set, the response body will include the
              `service_tier` value based on the processing mode actually used to serve the
              request. This response value may be different from the value set in the
              parameter.

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 10MB will be dropped.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help OpenAI detect and prevent abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: bool,
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.openai.com/docs/api-reference/responses) to take
        advantage of the latest OpenAI platform features. Compare
        [Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by OpenAI to cache responses for similar requests to optimize your cache
              hit rates. Replaces the `user` field.
              [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating OpenAI's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

              - If set to 'auto', then the request will be processed with the service tier
                configured in the Project settings. Unless otherwise configured, the Project
                will use 'default'.
              - If set to 'default', then the request will be processed with the standard
                pricing and performance for the selected model.
              - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
                'priority', then the request will be processed with the corresponding service
                tier. [Contact sales](https://openai.com/contact-sales) to learn more about
                Priority processing.
              - When not set, the default behavior is 'auto'.

              When the `service_tier` parameter is set, the response body will include the
              `service_tier` value based on the processing mode actually used to serve the
              request. This response value may be different from the value set in the
              parameter.

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 10MB will be dropped.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help OpenAI detect and prevent abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        validate_response_format(response_format)
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "safety_identifier": safety_identifier,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )

    def retrieve(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """Get a stored chat completion.

        Only Chat Completions that have been created with
        the `store` parameter set to `true` will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._get(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
        )

    def update(
        self,
        completion_id: str,
        *,
        metadata: Optional[Metadata],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """Modify a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be modified. Currently, the only
        supported modification is to update the `metadata` field.

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._post(
            f"/chat/completions/{completion_id}",
            body=maybe_transform({"metadata": metadata}, completion_update_params.CompletionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ChatCompletion]:
        """List stored Chat Completions.

        Only Chat Completions that have been stored with
        the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last chat completion from the previous pagination request.

          limit: Number of Chat Completions to retrieve.

          metadata:
              A list of metadata keys to filter the Chat Completions by. Example:

              `metadata[key1]=value1&metadata[key2]=value2`

          model: The model used to generate the Chat Completions.

          order: Sort order for Chat Completions by timestamp. Use `asc` for ascending order or
              `desc` for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/chat/completions",
            page=SyncCursorPage[ChatCompletion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "metadata": metadata,
                        "model": model,
                        "order": order,
                    },
                    completion_list_params.CompletionListParams,
                ),
            ),
            model=ChatCompletion,
        )

    def delete(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionDeleted:
        """Delete a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return self._delete(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionDeleted,
        )

    def stream(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | type[ResponseFormatT] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionStreamManager[ResponseFormatT]:
        """Wrapper over the `client.chat.completions.create(stream=True)` method that provides a more granular event API
        and automatic accumulation of each delta.

        This also supports all of the parsing utilities that `.parse()` does.

        Unlike `.create(stream=True)`, the `.stream()` method requires usage within a context manager to prevent accidental leakage of the response:

        ```py
        with client.chat.completions.stream(
            model="gpt-4o-2024-08-06",
            messages=[...],
        ) as stream:
            for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")
        ```

        When the context manager is entered, a `ChatCompletionStream` instance is returned which, like `.create(stream=True)` is an iterator. The full list of events that are yielded by the iterator are outlined in [these docs](https://github.com/openai/openai-python/blob/main/helpers.md#chat-completions-events).

        When the context manager exits, the response will be closed, however the `stream` instance is still available outside
        the context manager.
        """
        extra_headers = {
            "X-Stainless-Helper-Method": "chat.completions.stream",
            **(extra_headers or {}),
        }

        api_request: partial[Stream[ChatCompletionChunk]] = partial(
            self.create,
            messages=messages,
            model=model,
            audio=audio,
            stream=True,
            response_format=_type_to_response_format(response_format),
            frequency_penalty=frequency_penalty,
            function_call=function_call,
            functions=functions,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_completion_tokens=max_completion_tokens,
            max_tokens=max_tokens,
            metadata=metadata,
            modalities=modalities,
            n=n,
            parallel_tool_calls=parallel_tool_calls,
            prediction=prediction,
            presence_penalty=presence_penalty,
            reasoning_effort=reasoning_effort,
            seed=seed,
            service_tier=service_tier,
            store=store,
            stop=stop,
            stream_options=stream_options,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_logprobs=top_logprobs,
            top_p=top_p,
            user=user,
            web_search_options=web_search_options,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return ChatCompletionStreamManager(
            api_request,
            response_format=response_format,
            input_tools=tools,
        )


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessages:
        return AsyncMessages(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/openai/openai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/openai/openai-python#with_streaming_response
        """
        return AsyncCompletionsWithStreamingResponse(self)

    async def parse(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        response_format: type[ResponseFormatT] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParsedChatCompletion[ResponseFormatT]:
        """Wrapper over the `client.chat.completions.create()` method that provides richer integrations with Python specific types
        & returns a `ParsedChatCompletion` object, which is a subclass of the standard `ChatCompletion` class.

        You can pass a pydantic model to this method and it will automatically convert the model
        into a JSON schema, send it to the API and parse the response content back into the given model.

        This method will also automatically parse `function` tool calls if:
        - You use the `openai.pydantic_function_tool()` helper method
        - You mark your tool schema with `"strict": True`

        Example usage:
        ```py
        from pydantic import BaseModel
        from openai import AsyncOpenAI


        class Step(BaseModel):
            explanation: str
            output: str


        class MathResponse(BaseModel):
            steps: List[Step]
            final_answer: str


        client = AsyncOpenAI()
        completion = await client.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor."},
                {"role": "user", "content": "solve 8x + 31 = 2"},
            ],
            response_format=MathResponse,
        )

        message = completion.choices[0].message
        if message.parsed:
            print(message.parsed.steps)
            print("answer: ", message.parsed.final_answer)
        ```
        """
        _validate_input_tools(tools)

        extra_headers = {
            "X-Stainless-Helper-Method": "chat.completions.parse",
            **(extra_headers or {}),
        }

        def parser(raw_completion: ChatCompletion) -> ParsedChatCompletion[ResponseFormatT]:
            return _parse_chat_completion(
                response_format=response_format,
                chat_completion=raw_completion,
                input_tools=tools,
            )

        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "response_format": _type_to_response_format(response_format),
                    "seed": seed,
                    "service_tier": service_tier,
                    "store": store,
                    "stop": stop,
                    "stream": False,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=parser,
            ),
            # we turn the `ChatCompletion` instance into a `ParsedChatCompletion`
            # in the `parser` function above
            cast_to=cast(Type[ParsedChatCompletion[ResponseFormatT]], ChatCompletion),
            stream=False,
        )

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.openai.com/docs/api-reference/responses) to take
        advantage of the latest OpenAI platform features. Compare
        [Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by OpenAI to cache responses for similar requests to optimize your cache
              hit rates. Replaces the `user` field.
              [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating OpenAI's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

              - If set to 'auto', then the request will be processed with the service tier
                configured in the Project settings. Unless otherwise configured, the Project
                will use 'default'.
              - If set to 'default', then the request will be processed with the standard
                pricing and performance for the selected model.
              - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
                'priority', then the request will be processed with the corresponding service
                tier. [Contact sales](https://openai.com/contact-sales) to learn more about
                Priority processing.
              - When not set, the default behavior is 'auto'.

              When the `service_tier` parameter is set, the response body will include the
              `service_tier` value based on the processing mode actually used to serve the
              request. This response value may be different from the value set in the
              parameter.

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 10MB will be dropped.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help OpenAI detect and prevent abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: Literal[True],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionChunk]:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.openai.com/docs/api-reference/responses) to take
        advantage of the latest OpenAI platform features. Compare
        [Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by OpenAI to cache responses for similar requests to optimize your cache
              hit rates. Replaces the `user` field.
              [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating OpenAI's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

              - If set to 'auto', then the request will be processed with the service tier
                configured in the Project settings. Unless otherwise configured, the Project
                will use 'default'.
              - If set to 'default', then the request will be processed with the standard
                pricing and performance for the selected model.
              - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
                'priority', then the request will be processed with the corresponding service
                tier. [Contact sales](https://openai.com/contact-sales) to learn more about
                Priority processing.
              - When not set, the default behavior is 'auto'.

              When the `service_tier` parameter is set, the response body will include the
              `service_tier` value based on the processing mode actually used to serve the
              request. This response value may be different from the value set in the
              parameter.

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 10MB will be dropped.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help OpenAI detect and prevent abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        stream: bool,
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """
        **Starting a new project?** We recommend trying
        [Responses](https://platform.openai.com/docs/api-reference/responses) to take
        advantage of the latest OpenAI platform features. Compare
        [Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

        ---

        Creates a model response for the given chat conversation. Learn more in the
        [text generation](https://platform.openai.com/docs/guides/text-generation),
        [vision](https://platform.openai.com/docs/guides/vision), and
        [audio](https://platform.openai.com/docs/guides/audio) guides.

        Parameter support can differ depending on the model used to generate the
        response, particularly for newer reasoning models. Parameters that are only
        supported for reasoning models are noted below. For the current state of
        unsupported parameters in reasoning models,
        [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

        Args:
          messages: A list of messages comprising the conversation so far. Depending on the
              [model](https://platform.openai.com/docs/models) you use, different message
              types (modalities) are supported, like
              [text](https://platform.openai.com/docs/guides/text-generation),
              [images](https://platform.openai.com/docs/guides/vision), and
              [audio](https://platform.openai.com/docs/guides/audio).

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
              for more information, along with the
              [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
              guide for more information on how to handle the streaming events.

          audio: Parameters for audio output. Required when audio output is requested with
              `modalities: ["audio"]`.
              [Learn more](https://platform.openai.com/docs/guides/audio).

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model.

              `none` means the model will not call a function and instead generates a message.

              `auto` means the model can pick between generating a message or calling a
              function.

              Specifying a particular function via `{"name": "my_function"}` forces the model
              to call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and
              [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion. This value can be used to control
              [costs](https://openai.com/api/pricing/) for text generated via API.

              This value is now deprecated in favor of `max_completion_tokens`, and is not
              compatible with
              [o-series models](https://platform.openai.com/docs/guides/reasoning).

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          modalities: Output types that you would like the model to generate. Most models are capable
              of generating text, which is the default:

              `["text"]`

              The `gpt-4o-audio-preview` model can also be used to
              [generate audio](https://platform.openai.com/docs/guides/audio). To request that
              this model generate both text and audio responses, you can use:

              `["text", "audio"]`

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          parallel_tool_calls: Whether to enable
              [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
              during tool use.

          prediction: Static predicted output content, such as the content of a text file that is
              being regenerated.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_cache_key: Used by OpenAI to cache responses for similar requests to optimize your cache
              hit rates. Replaces the `user` field.
              [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

          reasoning_effort: **o-series models only**

              Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
              result in faster responses and fewer tokens used on reasoning in a response.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          safety_identifier: A stable identifier used to help detect users of your application that may be
              violating OpenAI's usage policies. The IDs should be a string that uniquely
              identifies each user. We recommend hashing their username or email address, in
              order to avoid sending us any identifying information.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          service_tier: Specifies the processing type used for serving the request.

              - If set to 'auto', then the request will be processed with the service tier
                configured in the Project settings. Unless otherwise configured, the Project
                will use 'default'.
              - If set to 'default', then the request will be processed with the standard
                pricing and performance for the selected model.
              - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
                'priority', then the request will be processed with the corresponding service
                tier. [Contact sales](https://openai.com/contact-sales) to learn more about
                Priority processing.
              - When not set, the default behavior is 'auto'.

              When the `service_tier` parameter is set, the response body will include the
              `service_tier` value based on the processing mode actually used to serve the
              request. This response value may be different from the value set in the
              parameter.

          stop: Not supported with latest reasoning models `o3` and `o4-mini`.

              Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: Whether or not to store the output of this chat completion request for use in
              our [model distillation](https://platform.openai.com/docs/guides/distillation)
              or [evals](https://platform.openai.com/docs/guides/evals) products.

              Supports text and image inputs. Note: image inputs over 10MB will be dropped.

          stream_options: Options for streaming response. Only set this when you set `stream: true`.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability.
              `logprobs` must be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use
              `prompt_cache_key` instead to maintain caching optimizations. A stable
              identifier for your end-users. Used to boost cache hit rates by better bucketing
              similar requests and to help OpenAI detect and prevent abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

          web_search_options: This tool searches the web for relevant results to use in a response. Learn more
              about the
              [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt_cache_key: str | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        safety_identifier: str | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        validate_response_format(response_format)
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "audio": audio,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "modalities": modalities,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "prediction": prediction,
                    "presence_penalty": presence_penalty,
                    "prompt_cache_key": prompt_cache_key,
                    "reasoning_effort": reasoning_effort,
                    "response_format": response_format,
                    "safety_identifier": safety_identifier,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                    "web_search_options": web_search_options,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )

    async def retrieve(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """Get a stored chat completion.

        Only Chat Completions that have been created with
        the `store` parameter set to `true` will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._get(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
        )

    async def update(
        self,
        completion_id: str,
        *,
        metadata: Optional[Metadata],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """Modify a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be modified. Currently, the only
        supported modification is to update the `metadata` field.

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._post(
            f"/chat/completions/{completion_id}",
            body=await async_maybe_transform({"metadata": metadata}, completion_update_params.CompletionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ChatCompletion, AsyncCursorPage[ChatCompletion]]:
        """List stored Chat Completions.

        Only Chat Completions that have been stored with
        the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last chat completion from the previous pagination request.

          limit: Number of Chat Completions to retrieve.

          metadata:
              A list of metadata keys to filter the Chat Completions by. Example:

              `metadata[key1]=value1&metadata[key2]=value2`

          model: The model used to generate the Chat Completions.

          order: Sort order for Chat Completions by timestamp. Use `asc` for ascending order or
              `desc` for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/chat/completions",
            page=AsyncCursorPage[ChatCompletion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "metadata": metadata,
                        "model": model,
                        "order": order,
                    },
                    completion_list_params.CompletionListParams,
                ),
            ),
            model=ChatCompletion,
        )

    async def delete(
        self,
        completion_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionDeleted:
        """Delete a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not completion_id:
            raise ValueError(f"Expected a non-empty value for `completion_id` but received {completion_id!r}")
        return await self._delete(
            f"/chat/completions/{completion_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionDeleted,
        )

    def stream(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[str, ChatModel],
        audio: Optional[ChatCompletionAudioParam] | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | type[ResponseFormatT] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
        functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        modalities: Optional[List[Literal["text", "audio"]]] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: bool | NotGiven = NOT_GIVEN,
        prediction: Optional[ChatCompletionPredictionContentParam] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[ChatCompletionStreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        web_search_options: completion_create_params.WebSearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncChatCompletionStreamManager[ResponseFormatT]:
        """Wrapper over the `client.chat.completions.create(stream=True)` method that provides a more granular event API
        and automatic accumulation of each delta.

        This also supports all of the parsing utilities that `.parse()` does.

        Unlike `.create(stream=True)`, the `.stream()` method requires usage within a context manager to prevent accidental leakage of the response:

        ```py
        async with client.chat.completions.stream(
            model="gpt-4o-2024-08-06",
            messages=[...],
        ) as stream:
            async for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")
        ```

        When the context manager is entered, an `AsyncChatCompletionStream` instance is returned which, like `.create(stream=True)` is an async iterator. The full list of events that are yielded by the iterator are outlined in [these docs](https://github.com/openai/openai-python/blob/main/helpers.md#chat-completions-events).

        When the context manager exits, the response will be closed, however the `stream` instance is still available outside
        the context manager.
        """
        _validate_input_tools(tools)

        extra_headers = {
            "X-Stainless-Helper-Method": "chat.completions.stream",
            **(extra_headers or {}),
        }

        api_request = self.create(
            messages=messages,
            model=model,
            audio=audio,
            stream=True,
            response_format=_type_to_response_format(response_format),
            frequency_penalty=frequency_penalty,
            function_call=function_call,
            functions=functions,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_completion_tokens=max_completion_tokens,
            max_tokens=max_tokens,
            metadata=metadata,
            modalities=modalities,
            n=n,
            parallel_tool_calls=parallel_tool_calls,
            prediction=prediction,
            presence_penalty=presence_penalty,
            reasoning_effort=reasoning_effort,
            seed=seed,
            service_tier=service_tier,
            stop=stop,
            store=store,
            stream_options=stream_options,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_logprobs=top_logprobs,
            top_p=top_p,
            user=user,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            web_search_options=web_search_options,
        )
        return AsyncChatCompletionStreamManager(
            api_request,
            response_format=response_format,
            input_tools=tools,
        )


class CompletionsWithRawResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.parse = _legacy_response.to_raw_response_wrapper(
            completions.parse,
        )
        self.create = _legacy_response.to_raw_response_wrapper(
            completions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            completions.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            completions.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            completions.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            completions.delete,
        )

    @cached_property
    def messages(self) -> MessagesWithRawResponse:
        return MessagesWithRawResponse(self._completions.messages)


class AsyncCompletionsWithRawResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.parse = _legacy_response.async_to_raw_response_wrapper(
            completions.parse,
        )
        self.create = _legacy_response.async_to_raw_response_wrapper(
            completions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            completions.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            completions.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            completions.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            completions.delete,
        )

    @cached_property
    def messages(self) -> AsyncMessagesWithRawResponse:
        return AsyncMessagesWithRawResponse(self._completions.messages)


class CompletionsWithStreamingResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.parse = to_streamed_response_wrapper(
            completions.parse,
        )
        self.create = to_streamed_response_wrapper(
            completions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            completions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            completions.update,
        )
        self.list = to_streamed_response_wrapper(
            completions.list,
        )
        self.delete = to_streamed_response_wrapper(
            completions.delete,
        )

    @cached_property
    def messages(self) -> MessagesWithStreamingResponse:
        return MessagesWithStreamingResponse(self._completions.messages)


class AsyncCompletionsWithStreamingResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.parse = async_to_streamed_response_wrapper(
            completions.parse,
        )
        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            completions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            completions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            completions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            completions.delete,
        )

    @cached_property
    def messages(self) -> AsyncMessagesWithStreamingResponse:
        return AsyncMessagesWithStreamingResponse(self._completions.messages)


def validate_response_format(response_format: object) -> None:
    if inspect.isclass(response_format) and issubclass(response_format, pydantic.BaseModel):
        raise TypeError(
            "You tried to pass a `BaseModel` class to `chat.completions.create()`; You must use `chat.completions.parse()` instead"
        )
