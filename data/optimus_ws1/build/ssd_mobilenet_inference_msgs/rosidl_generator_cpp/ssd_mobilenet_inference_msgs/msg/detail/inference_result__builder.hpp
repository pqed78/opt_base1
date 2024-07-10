// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_
#define SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ssd_mobilenet_inference_msgs
{

namespace msg
{

namespace builder
{

class Init_InferenceResult_spatial_z
{
public:
  explicit Init_InferenceResult_spatial_z(::ssd_mobilenet_inference_msgs::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  ::ssd_mobilenet_inference_msgs::msg::InferenceResult spatial_z(::ssd_mobilenet_inference_msgs::msg::InferenceResult::_spatial_z_type arg)
  {
    msg_.spatial_z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ssd_mobilenet_inference_msgs::msg::InferenceResult msg_;
};

class Init_InferenceResult_spatial_y
{
public:
  explicit Init_InferenceResult_spatial_y(::ssd_mobilenet_inference_msgs::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_spatial_z spatial_y(::ssd_mobilenet_inference_msgs::msg::InferenceResult::_spatial_y_type arg)
  {
    msg_.spatial_y = std::move(arg);
    return Init_InferenceResult_spatial_z(msg_);
  }

private:
  ::ssd_mobilenet_inference_msgs::msg::InferenceResult msg_;
};

class Init_InferenceResult_spatial_x
{
public:
  explicit Init_InferenceResult_spatial_x(::ssd_mobilenet_inference_msgs::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_spatial_y spatial_x(::ssd_mobilenet_inference_msgs::msg::InferenceResult::_spatial_x_type arg)
  {
    msg_.spatial_x = std::move(arg);
    return Init_InferenceResult_spatial_y(msg_);
  }

private:
  ::ssd_mobilenet_inference_msgs::msg::InferenceResult msg_;
};

class Init_InferenceResult_class_name
{
public:
  Init_InferenceResult_class_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InferenceResult_spatial_x class_name(::ssd_mobilenet_inference_msgs::msg::InferenceResult::_class_name_type arg)
  {
    msg_.class_name = std::move(arg);
    return Init_InferenceResult_spatial_x(msg_);
  }

private:
  ::ssd_mobilenet_inference_msgs::msg::InferenceResult msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ssd_mobilenet_inference_msgs::msg::InferenceResult>()
{
  return ssd_mobilenet_inference_msgs::msg::builder::Init_InferenceResult_class_name();
}

}  // namespace ssd_mobilenet_inference_msgs

#endif  // SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_
