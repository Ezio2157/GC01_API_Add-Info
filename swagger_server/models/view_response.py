# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ViewResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, views: int=None):  # noqa: E501
        """ViewResponse - a model defined in Swagger

        :param views: The views of this ViewResponse.  # noqa: E501
        :type views: int
        """
        self.swagger_types = {
            'views': int
        }

        self.attribute_map = {
            'views': 'views'
        }
        self._views = views

    @classmethod
    def from_dict(cls, dikt) -> 'ViewResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ViewResponse of this ViewResponse.  # noqa: E501
        :rtype: ViewResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def views(self) -> int:
        """Gets the views of this ViewResponse.

        Total number of views for the content  # noqa: E501

        :return: The views of this ViewResponse.
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views: int):
        """Sets the views of this ViewResponse.

        Total number of views for the content  # noqa: E501

        :param views: The views of this ViewResponse.
        :type views: int
        """

        self._views = views