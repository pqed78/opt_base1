// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "ssd_mobilenet_inference_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.hpp"

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

#include "fastcdr/Cdr.h"

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
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ssd_mobilenet_inference_msgs::msg::InferenceResult & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
get_serialized_size(
  const ssd_mobilenet_inference_msgs::msg::InferenceResult & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
max_serialized_size_InferenceResult(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace ssd_mobilenet_inference_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ssd_mobilenet_inference_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ssd_mobilenet_inference_msgs, msg, InferenceResult)();

#ifdef __cplusplus
}
#endif

#endif  // SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
