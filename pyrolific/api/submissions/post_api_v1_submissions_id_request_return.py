from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.post_api_v1_submissions_id_request_return_json_body import PostApiV1SubmissionsIdRequestReturnJsonBody
from ...models.return_requested_response import ReturnRequestedResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: PostApiV1SubmissionsIdRequestReturnJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/submissions/{id}/request-return/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ReturnRequestedResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReturnRequestedResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ReturnRequestedResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: PostApiV1SubmissionsIdRequestReturnJsonBody,
) -> Response[Union[Any, ReturnRequestedResponse]]:
    r"""Request the participant who submitted the response to return their response

     **This is an experimental feature that may be subject to change in the future.** <br/>
    It offers researchers the ability to ask a participant to return a submission. The return reason
    must be provided in the request and can be any free text string. <br/> The Prolific UI allows users
    to select any of the following options:
    * Didn't finish the study
    * Encountered technical problems
    * Withdrew consent
    * Other ( uses the free text input)

    This constructs a message around the reasons provided so there is no need to provide additional text
    beyond the reasons.
    <img alt=\"Example\" src=\"/assets/img/api/message.png\" />

    Args:
        id (str):
        json_body (PostApiV1SubmissionsIdRequestReturnJsonBody):  Example:
            {'request_return_reasons': ['Withdrew consent.', 'Did not finish study.']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReturnRequestedResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: PostApiV1SubmissionsIdRequestReturnJsonBody,
) -> Optional[Union[Any, ReturnRequestedResponse]]:
    r"""Request the participant who submitted the response to return their response

     **This is an experimental feature that may be subject to change in the future.** <br/>
    It offers researchers the ability to ask a participant to return a submission. The return reason
    must be provided in the request and can be any free text string. <br/> The Prolific UI allows users
    to select any of the following options:
    * Didn't finish the study
    * Encountered technical problems
    * Withdrew consent
    * Other ( uses the free text input)

    This constructs a message around the reasons provided so there is no need to provide additional text
    beyond the reasons.
    <img alt=\"Example\" src=\"/assets/img/api/message.png\" />

    Args:
        id (str):
        json_body (PostApiV1SubmissionsIdRequestReturnJsonBody):  Example:
            {'request_return_reasons': ['Withdrew consent.', 'Did not finish study.']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReturnRequestedResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: PostApiV1SubmissionsIdRequestReturnJsonBody,
) -> Response[Union[Any, ReturnRequestedResponse]]:
    r"""Request the participant who submitted the response to return their response

     **This is an experimental feature that may be subject to change in the future.** <br/>
    It offers researchers the ability to ask a participant to return a submission. The return reason
    must be provided in the request and can be any free text string. <br/> The Prolific UI allows users
    to select any of the following options:
    * Didn't finish the study
    * Encountered technical problems
    * Withdrew consent
    * Other ( uses the free text input)

    This constructs a message around the reasons provided so there is no need to provide additional text
    beyond the reasons.
    <img alt=\"Example\" src=\"/assets/img/api/message.png\" />

    Args:
        id (str):
        json_body (PostApiV1SubmissionsIdRequestReturnJsonBody):  Example:
            {'request_return_reasons': ['Withdrew consent.', 'Did not finish study.']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReturnRequestedResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: PostApiV1SubmissionsIdRequestReturnJsonBody,
) -> Optional[Union[Any, ReturnRequestedResponse]]:
    r"""Request the participant who submitted the response to return their response

     **This is an experimental feature that may be subject to change in the future.** <br/>
    It offers researchers the ability to ask a participant to return a submission. The return reason
    must be provided in the request and can be any free text string. <br/> The Prolific UI allows users
    to select any of the following options:
    * Didn't finish the study
    * Encountered technical problems
    * Withdrew consent
    * Other ( uses the free text input)

    This constructs a message around the reasons provided so there is no need to provide additional text
    beyond the reasons.
    <img alt=\"Example\" src=\"/assets/img/api/message.png\" />

    Args:
        id (str):
        json_body (PostApiV1SubmissionsIdRequestReturnJsonBody):  Example:
            {'request_return_reasons': ['Withdrew consent.', 'Did not finish study.']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReturnRequestedResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
