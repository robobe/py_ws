import rclpy
from rclpy import Future
from rclpy.node import Node
import time

from custom_interfaces.srv import Counter  # pylint: disable=E0401
from custom_interfaces.srv._counter import Counter_Request, Counter_Response

TOPIC = "my_service_demo"

SRV_TOPIC = "/my_service"

class MyNode(Node):
    def __init__(self):
        node_name = "service_client"
        super().__init__(node_name)
        self.client = self.create_client(Counter, SRV_TOPIC)
        while not self.client.wait_for_service(1.0):
            self.get_logger().warning("Service not ready")

        msg = Counter.Request()
        msg.count = 10
        self.future = self.client.call_async(msg)
        self.future.add_done_callback(self.service_handler)

    def service_handler(self, future: Future):
        response: Counter_Response
        response = future.result()
        self.get_logger().info(f"Service result: {response.total}")
        
        

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