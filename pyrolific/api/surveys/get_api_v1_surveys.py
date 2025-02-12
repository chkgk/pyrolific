from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    researcher_id: str,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
) -> Dict[str, Any]:
    url = "{}/api/v1/surveys/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["researcher_id"] = researcher_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[HTTPValidationError]:
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    researcher_id: str,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
) -> Response[HTTPValidationError]:
    """Get all surveys

     Get all the surveys for a researcher.

    Args:
        researcher_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        client=client,
        researcher_id=researcher_id,
        offset=offset,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    researcher_id: str,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
) -> Optional[HTTPValidationError]:
    """Get all surveys

     Get all the surveys for a researcher.

    Args:
        researcher_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        client=client,
        researcher_id=researcher_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    researcher_id: str,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
) -> Response[HTTPValidationError]:
    """Get all surveys

     Get all the surveys for a researcher.

    Args:
        researcher_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        client=client,
        researcher_id=researcher_id,
        offset=offset,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    researcher_id: str,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
) -> Optional[HTTPValidationError]:
    """Get all surveys

     Get all the surveys for a researcher.

    Args:
        researcher_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            researcher_id=researcher_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
