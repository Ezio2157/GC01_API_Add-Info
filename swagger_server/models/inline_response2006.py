# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2006(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, recommendations: List[object]=None):  # noqa: E501
        """InlineResponse2006 - a model defined in Swagger

        :param recommendations: The recommendations of this InlineResponse2006.  # noqa: E501
        :type recommendations: List[object]
        """
        self.swagger_types = {
            'recommendations': List[object]
        }

        self.attribute_map = {
            'recommendations': 'recommendations'
        }
        self._recommendations = recommendations

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2006':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_6 of this InlineResponse2006.  # noqa: E501
        :rtype: InlineResponse2006
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recommendations(self) -> List[object]:
        """Gets the recommendations of this InlineResponse2006.


        :return: The recommendations of this InlineResponse2006.
        :rtype: List[object]
        """
        return self._recommendations

    @recommendations.setter
    def recommendations(self, recommendations: List[object]):
        """Sets the recommendations of this InlineResponse2006.


        :param recommendations: The recommendations of this InlineResponse2006.
        :type recommendations: List[object]
        """

        self._recommendations = recommendations