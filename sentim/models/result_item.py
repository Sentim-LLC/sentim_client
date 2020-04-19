# coding: utf-8

"""
    Sentim's Emotion APIs

    An emotion recognition api that tells you the emotion of text, and not just the connotation.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: help@sentimllc.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ResultItem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'index': 'int',
        'emotion': 'str',
        'emotion_score': 'EmotionScore'
    }

    attribute_map = {
        'index': 'Index',
        'emotion': 'Emotion',
        'emotion_score': 'EmotionScore'
    }

    def __init__(self, index=None, emotion=None, emotion_score=None):  # noqa: E501
        """ResultItem - a model defined in OpenAPI"""  # noqa: E501

        self._index = None
        self._emotion = None
        self._emotion_score = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if emotion is not None:
            self.emotion = emotion
        if emotion_score is not None:
            self.emotion_score = emotion_score

    @property
    def index(self):
        """Gets the index of this ResultItem.  # noqa: E501

        The index of the conversation or list that was classified.  # noqa: E501

        :return: The index of this ResultItem.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ResultItem.

        The index of the conversation or list that was classified.  # noqa: E501

        :param index: The index of this ResultItem.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def emotion(self):
        """Gets the emotion of this ResultItem.  # noqa: E501

        The classified emotion of the message.  # noqa: E501

        :return: The emotion of this ResultItem.  # noqa: E501
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """Sets the emotion of this ResultItem.

        The classified emotion of the message.  # noqa: E501

        :param emotion: The emotion of this ResultItem.  # noqa: E501
        :type: str
        """

        self._emotion = emotion

    @property
    def emotion_score(self):
        """Gets the emotion_score of this ResultItem.  # noqa: E501


        :return: The emotion_score of this ResultItem.  # noqa: E501
        :rtype: EmotionScore
        """
        return self._emotion_score

    @emotion_score.setter
    def emotion_score(self, emotion_score):
        """Sets the emotion_score of this ResultItem.


        :param emotion_score: The emotion_score of this ResultItem.  # noqa: E501
        :type: EmotionScore
        """

        self._emotion_score = emotion_score

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other