from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.submission_list_response import SubmissionListResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/studies/{id}/submissions/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SubmissionListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubmissionListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SubmissionListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    
) -> Response[SubmissionListResponse]:
    """List study submissions

     Returns basic information of the submissions, including the study id, participant id, status and
    start timestamp

    Args:
        id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmissionListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    
) -> Optional[SubmissionListResponse]:
    """List study submissions

     Returns basic information of the submissions, including the study id, participant id, status and
    start timestamp

    Args:
        id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmissionListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    
) -> Response[SubmissionListResponse]:
    """List study submissions

     Returns basic information of the submissions, including the study id, participant id, status and
    start timestamp

    Args:
        id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmissionListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    
) -> Optional[SubmissionListResponse]:
    """List study submissions

     Returns basic information of the submissions, including the study id, participant id, status and
    start timestamp

    Args:
        id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmissionListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            
        )
    ).parsed
