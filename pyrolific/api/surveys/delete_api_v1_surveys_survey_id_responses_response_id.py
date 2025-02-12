from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    survey_id: str,
    response_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/surveys/{survey_id}/responses/{response_id}".format(
        client.base_url, survey_id=survey_id, response_id=response_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    survey_id: str,
    response_id: str,
    *,
    client: Client,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete a response

     Delete a single Response.

    Args:
        survey_id (str):
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        survey_id=survey_id,
        response_id=response_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    survey_id: str,
    response_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete a response

     Delete a single Response.

    Args:
        survey_id (str):
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        survey_id=survey_id,
        response_id=response_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    survey_id: str,
    response_id: str,
    *,
    client: Client,
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete a response

     Delete a single Response.

    Args:
        survey_id (str):
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        survey_id=survey_id,
        response_id=response_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    survey_id: str,
    response_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete a response

     Delete a single Response.

    Args:
        survey_id (str):
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            survey_id=survey_id,
            response_id=response_id,
            client=client,
        )
    ).parsed
