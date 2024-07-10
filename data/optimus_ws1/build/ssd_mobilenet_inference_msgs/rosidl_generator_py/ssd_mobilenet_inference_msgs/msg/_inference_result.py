# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InferenceResult(type):
    """Metaclass of message 'InferenceResult'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ssd_mobilenet_inference_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ssd_mobilenet_inference_msgs.msg.InferenceResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__inference_result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__inference_result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__inference_result
            cls._TYPE_SUPPORT = module.type_support_msg__msg__inference_result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__inference_result

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class InferenceResult(metaclass=Metaclass_InferenceResult):
    """Message class 'InferenceResult'."""

    __slots__ = [
        '_class_name',
        '_spatial_x',
        '_spatial_y',
        '_spatial_z',
    ]

    _fields_and_field_types = {
        'class_name': 'string',
        'spatial_x': 'int64',
        'spatial_y': 'int64',
        'spatial_z': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.class_name = kwargs.get('class_name', str())
        self.spatial_x = kwargs.get('spatial_x', int())
        self.spatial_y = kwargs.get('spatial_y', int())
        self.spatial_z = kwargs.get('spatial_z', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.class_name != other.class_name:
            return False
        if self.spatial_x != other.spatial_x:
            return False
        if self.spatial_y != other.spatial_y:
            return False
        if self.spatial_z != other.spatial_z:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def class_name(self):
        """Message field 'class_name'."""
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'class_name' field must be of type 'str'"
        self._class_name = value

    @builtins.property
    def spatial_x(self):
        """Message field 'spatial_x'."""
        return self._spatial_x

    @spatial_x.setter
    def spatial_x(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'spatial_x' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'spatial_x' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._spatial_x = value

    @builtins.property
    def spatial_y(self):
        """Message field 'spatial_y'."""
        return self._spatial_y

    @spatial_y.setter
    def spatial_y(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'spatial_y' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'spatial_y' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._spatial_y = value

    @builtins.property
    def spatial_z(self):
        """Message field 'spatial_z'."""
        return self._spatial_z

    @spatial_z.setter
    def spatial_z(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'spatial_z' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'spatial_z' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._spatial_z = value
