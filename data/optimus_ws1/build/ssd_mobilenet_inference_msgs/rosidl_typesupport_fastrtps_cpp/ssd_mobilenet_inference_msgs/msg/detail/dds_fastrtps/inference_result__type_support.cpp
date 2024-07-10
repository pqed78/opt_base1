// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace ssd_mobilenet_inference_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
cdr_serialize(
  const ssd_mobilenet_inference_msgs::msg::InferenceResult & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: class_name
  cdr << ros_message.class_name;
  // Member: spatial_x
  cdr << ros_message.spatial_x;
  // Member: spatial_y
  cdr << ros_message.spatial_y;
  // Member: spatial_z
  cdr << ros_message.spatial_z;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ssd_mobilenet_inference_msgs::msg::InferenceResult & ros_message)
{
  // Member: class_name
  cdr >> ros_message.class_name;

  // Member: spatial_x
  cdr >> ros_message.spatial_x;

  // Member: spatial_y
  cdr >> ros_message.spatial_y;

  // Member: spatial_z
  cdr >> ros_message.spatial_z;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
get_serialized_size(
  const ssd_mobilenet_inference_msgs::msg::InferenceResult & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: class_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.class_name.size() + 1);
  // Member: spatial_x
  {
    size_t item_size = sizeof(ros_message.spatial_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: spatial_y
  {
    size_t item_size = sizeof(ros_message.spatial_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: spatial_z
  {
    size_t item_size = sizeof(ros_message.spatial_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
max_serialized_size_InferenceResult(
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


  // Member: class_name
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

  // Member: spatial_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: spatial_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: spatial_z
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _InferenceResult__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ssd_mobilenet_inference_msgs::msg::InferenceResult *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _InferenceResult__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ssd_mobilenet_inference_msgs::msg::InferenceResult *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _InferenceResult__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ssd_mobilenet_inference_msgs::msg::InferenceResult *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _InferenceResult__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_InferenceResult(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _InferenceResult__callbacks = {
  "ssd_mobilenet_inference_msgs::msg",
  "InferenceResult",
  _InferenceResult__cdr_serialize,
  _InferenceResult__cdr_deserialize,
  _InferenceResult__get_serialized_size,
  _InferenceResult__max_serialized_size
};

static rosidl_message_type_support_t _InferenceResult__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_InferenceResult__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ssd_mobilenet_inference_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ssd_mobilenet_inference_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<ssd_mobilenet_inference_msgs::msg::InferenceResult>()
{
  return &ssd_mobilenet_inference_msgs::msg::typesupport_fastrtps_cpp::_InferenceResult__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ssd_mobilenet_inference_msgs, msg, InferenceResult)() {
  return &ssd_mobilenet_inference_msgs::msg::typesupport_fastrtps_cpp::_InferenceResult__handle;
}

#ifdef __cplusplus
}
#endif
