# CMake generated Testfile for 
# Source directory: /data/optimus_ws1/src/ssd_mobilenet_inference_msgs
# Build directory: /data/optimus_ws1/build/ssd_mobilenet_inference_msgs
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(lint_cmake "/env/bin/python3.8" "-u" "/opt/ros/humble/install/share/ament_cmake_test/cmake/run_test.py" "/data/optimus_ws1/build/ssd_mobilenet_inference_msgs/test_results/ssd_mobilenet_inference_msgs/lint_cmake.xunit.xml" "--package-name" "ssd_mobilenet_inference_msgs" "--output-file" "/data/optimus_ws1/build/ssd_mobilenet_inference_msgs/ament_lint_cmake/lint_cmake.txt" "--command" "/opt/ros/humble/install/bin/ament_lint_cmake" "--xunit-file" "/data/optimus_ws1/build/ssd_mobilenet_inference_msgs/test_results/ssd_mobilenet_inference_msgs/lint_cmake.xunit.xml")
set_tests_properties(lint_cmake PROPERTIES  LABELS "lint_cmake;linter" TIMEOUT "60" WORKING_DIRECTORY "/data/optimus_ws1/src/ssd_mobilenet_inference_msgs" _BACKTRACE_TRIPLES "/opt/ros/humble/install/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/install/share/ament_cmake_lint_cmake/cmake/ament_lint_cmake.cmake;47;ament_add_test;/opt/ros/humble/install/share/ament_cmake_lint_cmake/cmake/ament_cmake_lint_cmake_lint_hook.cmake;21;ament_lint_cmake;/opt/ros/humble/install/share/ament_cmake_lint_cmake/cmake/ament_cmake_lint_cmake_lint_hook.cmake;0;;/opt/ros/humble/install/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/opt/ros/humble/install/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/opt/ros/humble/install/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/opt/ros/humble/install/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/opt/ros/humble/install/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/data/optimus_ws1/src/ssd_mobilenet_inference_msgs/CMakeLists.txt;34;ament_package;/data/optimus_ws1/src/ssd_mobilenet_inference_msgs/CMakeLists.txt;0;")
add_test(xmllint "/env/bin/python3.8" "-u" "/opt/ros/humble/install/share/ament_cmake_test/cmake/run_test.py" "/data/optimus_ws1/build/ssd_mobilenet_inference_msgs/test_results/ssd_mobilenet_inference_msgs/xmllint.xunit.xml" "--package-name" "ssd_mobilenet_inference_msgs" "--output-file" "/data/optimus_ws1/build/ssd_mobilenet_inference_msgs/ament_xmllint/xmllint.txt" "--command" "/opt/ros/humble/install/bin/ament_xmllint" "--xunit-file" "/data/optimus_ws1/build/ssd_mobilenet_inference_msgs/test_results/ssd_mobilenet_inference_msgs/xmllint.xunit.xml")
set_tests_properties(xmllint PROPERTIES  LABELS "xmllint;linter" TIMEOUT "60" WORKING_DIRECTORY "/data/optimus_ws1/src/ssd_mobilenet_inference_msgs" _BACKTRACE_TRIPLES "/opt/ros/humble/install/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/install/share/ament_cmake_xmllint/cmake/ament_xmllint.cmake;50;ament_add_test;/opt/ros/humble/install/share/ament_cmake_xmllint/cmake/ament_cmake_xmllint_lint_hook.cmake;18;ament_xmllint;/opt/ros/humble/install/share/ament_cmake_xmllint/cmake/ament_cmake_xmllint_lint_hook.cmake;0;;/opt/ros/humble/install/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/opt/ros/humble/install/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/opt/ros/humble/install/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/opt/ros/humble/install/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/opt/ros/humble/install/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/data/optimus_ws1/src/ssd_mobilenet_inference_msgs/CMakeLists.txt;34;ament_package;/data/optimus_ws1/src/ssd_mobilenet_inference_msgs/CMakeLists.txt;0;")
subdirs("ssd_mobilenet_inference_msgs__py")
