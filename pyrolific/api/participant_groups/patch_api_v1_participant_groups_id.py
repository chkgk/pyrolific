from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.participant_group import ParticipantGroup
from ...models.participant_group_update import ParticipantGroupUpdate
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: ParticipantGroupUpdate,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/participant-groups/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ParticipantGroup]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ParticipantGroup.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ParticipantGroup]]:
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
    json_body: ParticipantGroupUpdate,
    
) -> Response[Union[Any, ParticipantGroup]]:
    """Update a participant group

    Args:
        id (str):
        
        json_body (ParticipantGroupUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ParticipantGroup]]
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
    json_body: ParticipantGroupUpdate,
    
) -> Optional[Union[Any, ParticipantGroup]]:
    """Update a participant group

    Args:
        id (str):
        
        json_body (ParticipantGroupUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ParticipantGroup]
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
    json_body: ParticipantGroupUpdate,
    
) -> Response[Union[Any, ParticipantGroup]]:
    """Update a participant group

    Args:
        id (str):
        
        json_body (ParticipantGroupUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ParticipantGroup]]
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
    json_body: ParticipantGroupUpdate,
    
) -> Optional[Union[Any, ParticipantGroup]]:
    """Update a participant group

    Args:
        id (str):
        
        json_body (ParticipantGroupUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ParticipantGroup]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            
        )
    ).parsed
