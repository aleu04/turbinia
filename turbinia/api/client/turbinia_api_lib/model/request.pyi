# coding: utf-8

"""
    Turbinia API Server

    Turbinia is an open-source framework for deploying,managing, and running distributed forensic workloads  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from turbinia_api_lib import schemas  # noqa: F401


class Request(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Base request object. 
    """


    class MetaOapg:
        required = {
            "request_options",
            "evidence",
        }
        
        class properties:
            evidence = schemas.DictSchema
        
            @staticmethod
            def request_options() -> typing.Type['BaseRequestOptions']:
                return BaseRequestOptions
            description = schemas.StrSchema
            __annotations__ = {
                "evidence": evidence,
                "request_options": request_options,
                "description": description,
            }
    
    request_options: 'BaseRequestOptions'
    evidence: MetaOapg.properties.evidence
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evidence"]) -> MetaOapg.properties.evidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_options"]) -> 'BaseRequestOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["evidence", "request_options", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evidence"]) -> MetaOapg.properties.evidence: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_options"]) -> 'BaseRequestOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["evidence", "request_options", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        request_options: 'BaseRequestOptions',
        evidence: typing.Union[MetaOapg.properties.evidence, dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Request':
        return super().__new__(
            cls,
            *_args,
            request_options=request_options,
            evidence=evidence,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from turbinia_api_lib.model.base_request_options import BaseRequestOptions