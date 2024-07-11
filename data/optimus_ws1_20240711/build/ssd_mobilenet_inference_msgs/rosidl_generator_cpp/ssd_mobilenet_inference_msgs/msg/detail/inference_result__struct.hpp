// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__STRUCT_HPP_
#define SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ssd_mobilenet_inference_msgs__msg__InferenceResult __attribute__((deprecated))
#else
# define DEPRECATED__ssd_mobilenet_inference_msgs__msg__InferenceResult __declspec(deprecated)
#endif

namespace ssd_mobilenet_inference_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InferenceResult_
{
  using Type = InferenceResult_<ContainerAllocator>;

  explicit InferenceResult_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->class_name = "";
      this->spatial_x = 0ll;
      this->spatial_y = 0ll;
      this->spatial_z = 0ll;
    }
  }

  explicit InferenceResult_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : class_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->class_name = "";
      this->spatial_x = 0ll;
      this->spatial_y = 0ll;
      this->spatial_z = 0ll;
    }
  }

  // field types and members
  using _class_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _class_name_type class_name;
  using _spatial_x_type =
    int64_t;
  _spatial_x_type spatial_x;
  using _spatial_y_type =
    int64_t;
  _spatial_y_type spatial_y;
  using _spatial_z_type =
    int64_t;
  _spatial_z_type spatial_z;

  // setters for named parameter idiom
  Type & set__class_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->class_name = _arg;
    return *this;
  }
  Type & set__spatial_x(
    const int64_t & _arg)
  {
    this->spatial_x = _arg;
    return *this;
  }
  Type & set__spatial_y(
    const int64_t & _arg)
  {
    this->spatial_y = _arg;
    return *this;
  }
  Type & set__spatial_z(
    const int64_t & _arg)
  {
    this->spatial_z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator> *;
  using ConstRawPtr =
    const ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ssd_mobilenet_inference_msgs__msg__InferenceResult
    std::shared_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ssd_mobilenet_inference_msgs__msg__InferenceResult
    std::shared_ptr<ssd_mobilenet_inference_msgs::msg::InferenceResult_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InferenceResult_ & other) const
  {
    if (this->class_name != other.class_name) {
      return false;
    }
    if (this->spatial_x != other.spatial_x) {
      return false;
    }
    if (this->spatial_y != other.spatial_y) {
      return false;
    }
    if (this->spatial_z != other.spatial_z) {
      return false;
    }
    return true;
  }
  bool operator!=(const InferenceResult_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InferenceResult_

// alias to use template instance with default allocator
using InferenceResult =
  ssd_mobilenet_inference_msgs::msg::InferenceResult_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ssd_mobilenet_inference_msgs

#endif  // SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__STRUCT_HPP_
