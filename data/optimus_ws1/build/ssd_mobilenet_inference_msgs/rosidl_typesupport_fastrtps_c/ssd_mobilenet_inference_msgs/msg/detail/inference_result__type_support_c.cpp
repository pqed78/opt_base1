// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ssd_mobilenet_inference_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // class_name
#include "rosidl_runtime_c/string_functions.h"  // class_name

// forward declare type support functions


using _InferenceResult__ros_msg_type = ssd_mobilenet_inference_msgs__msg__InferenceResult;

static bool _InferenceResult__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _InferenceResult__ros_msg_type * ros_message = static_cast<const _InferenceResult__ros_msg_type *>(untyped_ros_message);
  // Field name: class_name
  {
    const rosidl_runtime_c__String * str = &ros_message->class_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: spatial_x
  {
    cdr << ros_message->spatial_x;
  }

  // Field name: spatial_y
  {
    cdr << ros_message->spatial_y;
  }

  // Field name: spatial_z
  {
    cdr << ros_message->spatial_z;
  }

  return true;
}

static bool _InferenceResult__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _InferenceResult__ros_msg_type * ros_message = static_cast<_InferenceResult__ros_msg_type *>(untyped_ros_message);
  // Field name: class_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->class_name.data) {
      rosidl_runtime_c__String__init(&ros_message->class_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->class_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'class_name'\n");
      return false;
    }
  }

  // Field name: spatial_x
  {
    cdr >> ros_message->spatial_x;
  }

  // Field name: spatial_y
  {
    cdr >> ros_message->spatial_y;
  }

  // Field name: spatial_z
  {
    cdr >> ros_message->spatial_z;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ssd_mobilenet_inference_msgs
size_t get_serialized_size_ssd_mobilenet_inference_msgs__msg__InferenceResult(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _InferenceResult__ros_msg_type * ros_message = static_cast<const _InferenceResult__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name class_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->class_name.size + 1);
  // field.name spatial_x
  {
    size_t item_size = sizeof(ros_message->spatial_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name spatial_y
  {
    size_t item_size = sizeof(ros_message->spatial_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name spatial_z
  {
    size_t item_size = sizeof(ros_message->spatial_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _InferenceResult__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ssd_mobilenet_inference_msgs__msg__InferenceResult(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ssd_mobilenet_inference_msgs
size_t max_serialized_size_ssd_mobilenet_inference_msgs__msg__InferenceResult(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: class_name
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: spatial_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: spatial_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: spatial_z
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _InferenceResult__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ssd_mobilenet_inference_msgs__msg__InferenceResult(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_InferenceResult = {
  "ssd_mobilenet_inference_msgs::msg",
  "InferenceResult",
  _InferenceResult__cdr_serialize,
  _InferenceResult__cdr_deserialize,
  _InferenceResult__get_serialized_size,
  _InferenceResult__max_serialized_size
};

static rosidl_message_type_support_t _InferenceResult__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_InferenceResult,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ssd_mobilenet_inference_msgs, msg, InferenceResult)() {
  return &_InferenceResult__type_support;
}

#if defined(__cplusplus)
}
#endif
