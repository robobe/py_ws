import rclpy
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from rclpy.node import Node
import time

from custom_interfaces.action import Counter  # pylint: disable=E0401

TOPIC = "my_action_demo"


class MyNode(Node):
    def __init__(self):
        node_name = "action_server"
        super().__init__(node_name)
        self._action_server = ActionServer(self, Counter, TOPIC, self.execute_callback)
        self.get_logger().info("Hello ROS2")

    def execute_callback(self, goal_handle: ServerGoalHandle):
        feedback_msg = Counter.Feedback()
        for i in range(goal_handle.request.count):
            self.get_logger().info(f"current: {i}")
            feedback_msg.current = i
            time.sleep(1)
            goal_handle.publish_feedback(feedback_msg)

        self.get_logger().info("Action ended")
        goal_handle.succeed()

        result = Counter.Result()
        result.total = i
        return result


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("User exit")
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()