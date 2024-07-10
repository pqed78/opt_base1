// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__TRAITS_HPP_
#define SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ssd_mobilenet_inference_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const InferenceResult & msg,
  std::ostream & out)
{
  out << "{";
  // member: class_name
  {
    out << "class_name: ";
    rosidl_generator_traits::value_to_yaml(msg.class_name, out);
    out << ", ";
  }

  // member: spatial_x
  {
    out << "spatial_x: ";
    rosidl_generator_traits::value_to_yaml(msg.spatial_x, out);
    out << ", ";
  }

  // member: spatial_y
  {
    out << "spatial_y: ";
    rosidl_generator_traits::value_to_yaml(msg.spatial_y, out);
    out << ", ";
  }

  // member: spatial_z
  {
    out << "spatial_z: ";
    rosidl_generator_traits::value_to_yaml(msg.spatial_z, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InferenceResult & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: class_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "class_name: ";
    rosidl_generator_traits::value_to_yaml(msg.class_name, out);
    out << "\n";
  }

  // member: spatial_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "spatial_x: ";
    rosidl_generator_traits::value_to_yaml(msg.spatial_x, out);
    out << "\n";
  }

  // member: spatial_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "spatial_y: ";
    rosidl_generator_traits::value_to_yaml(msg.spatial_y, out);
    out << "\n";
  }

  // member: spatial_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "spatial_z: ";
    rosidl_generator_traits::value_to_yaml(msg.spatial_z, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InferenceResult & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ssd_mobilenet_inference_msgs

namespace rosidl_generator_traits
{

[[deprecated("use ssd_mobilenet_inference_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ssd_mobilenet_inference_msgs::msg::InferenceResult & msg,
  std::ostream & out, size_t indentation = 0)
{
  ssd_mobilenet_inference_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ssd_mobilenet_inference_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ssd_mobilenet_inference_msgs::msg::InferenceResult & msg)
{
  return ssd_mobilenet_inference_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ssd_mobilenet_inference_msgs::msg::InferenceResult>()
{
  return "ssd_mobilenet_inference_msgs::msg::InferenceResult";
}

template<>
inline const char * name<ssd_mobilenet_inference_msgs::msg::InferenceResult>()
{
  return "ssd_mobilenet_inference_msgs/msg/InferenceResult";
}

template<>
struct has_fixed_size<ssd_mobilenet_inference_msgs::msg::InferenceResult>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ssd_mobilenet_inference_msgs::msg::InferenceResult>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ssd_mobilenet_inference_msgs::msg::InferenceResult>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__TRAITS_HPP_
