// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `class_name`
#include "rosidl_runtime_c/string_functions.h"

bool
ssd_mobilenet_inference_msgs__msg__InferenceResult__init(ssd_mobilenet_inference_msgs__msg__InferenceResult * msg)
{
  if (!msg) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__init(&msg->class_name)) {
    ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(msg);
    return false;
  }
  // spatial_x
  // spatial_y
  // spatial_z
  return true;
}

void
ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(ssd_mobilenet_inference_msgs__msg__InferenceResult * msg)
{
  if (!msg) {
    return;
  }
  // class_name
  rosidl_runtime_c__String__fini(&msg->class_name);
  // spatial_x
  // spatial_y
  // spatial_z
}

bool
ssd_mobilenet_inference_msgs__msg__InferenceResult__are_equal(const ssd_mobilenet_inference_msgs__msg__InferenceResult * lhs, const ssd_mobilenet_inference_msgs__msg__InferenceResult * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->class_name), &(rhs->class_name)))
  {
    return false;
  }
  // spatial_x
  if (lhs->spatial_x != rhs->spatial_x) {
    return false;
  }
  // spatial_y
  if (lhs->spatial_y != rhs->spatial_y) {
    return false;
  }
  // spatial_z
  if (lhs->spatial_z != rhs->spatial_z) {
    return false;
  }
  return true;
}

bool
ssd_mobilenet_inference_msgs__msg__InferenceResult__copy(
  const ssd_mobilenet_inference_msgs__msg__InferenceResult * input,
  ssd_mobilenet_inference_msgs__msg__InferenceResult * output)
{
  if (!input || !output) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__copy(
      &(input->class_name), &(output->class_name)))
  {
    return false;
  }
  // spatial_x
  output->spatial_x = input->spatial_x;
  // spatial_y
  output->spatial_y = input->spatial_y;
  // spatial_z
  output->spatial_z = input->spatial_z;
  return true;
}

ssd_mobilenet_inference_msgs__msg__InferenceResult *
ssd_mobilenet_inference_msgs__msg__InferenceResult__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ssd_mobilenet_inference_msgs__msg__InferenceResult * msg = (ssd_mobilenet_inference_msgs__msg__InferenceResult *)allocator.allocate(sizeof(ssd_mobilenet_inference_msgs__msg__InferenceResult), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ssd_mobilenet_inference_msgs__msg__InferenceResult));
  bool success = ssd_mobilenet_inference_msgs__msg__InferenceResult__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ssd_mobilenet_inference_msgs__msg__InferenceResult__destroy(ssd_mobilenet_inference_msgs__msg__InferenceResult * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__init(ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ssd_mobilenet_inference_msgs__msg__InferenceResult * data = NULL;

  if (size) {
    data = (ssd_mobilenet_inference_msgs__msg__InferenceResult *)allocator.zero_allocate(size, sizeof(ssd_mobilenet_inference_msgs__msg__InferenceResult), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ssd_mobilenet_inference_msgs__msg__InferenceResult__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__fini(ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence *
ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * array = (ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence *)allocator.allocate(sizeof(ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__destroy(ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__are_equal(const ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * lhs, const ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ssd_mobilenet_inference_msgs__msg__InferenceResult__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence__copy(
  const ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * input,
  ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ssd_mobilenet_inference_msgs__msg__InferenceResult);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ssd_mobilenet_inference_msgs__msg__InferenceResult * data =
      (ssd_mobilenet_inference_msgs__msg__InferenceResult *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ssd_mobilenet_inference_msgs__msg__InferenceResult__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ssd_mobilenet_inference_msgs__msg__InferenceResult__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
