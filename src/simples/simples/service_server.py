import rclpy
from rclpy.node import Node
import time

from custom_interfaces.srv import Counter  # pylint: disable=E0401
from custom_interfaces.srv._counter import Counter_Request, Counter_Response

TOPIC = "my_service_demo"

SRV_TOPIC = "/my_service"

class MyNode(Node):
    def __init__(self):
        node_name = "service_server"
        super().__init__(node_name)
        self.srv = self.create_service(Counter, SRV_TOPIC, self.service_handler)

    def service_handler(self, request: Counter_Request, response: Counter_Response):
        for i in range(request.count):
            self.get_logger().info(f"Service current count: {i}")
            time.sleep(1)
        response.total = i
        return response

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