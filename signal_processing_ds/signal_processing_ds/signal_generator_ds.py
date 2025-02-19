#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class SignalGenerator(Node):
    def __init__(self):
        super().__init__('signal_generator')
        
        # Publicadores para /signal y /time
        self.signal_pub = self.create_publisher(Float32, '/signal', 10)
        self.time_pub = self.create_publisher(Float32, '/time', 10)
        
        # Temporizador para generar la señal a 10 Hz
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.time = 0.0  # Variable para almacenar el tiempo

    def timer_callback(self):
        # Generar la señal sinusoidal
        signal_msg = Float32()
        signal_msg.data = math.sin(self.time)  # Señal sinusoidal
        self.signal_pub.publish(signal_msg)
        
        # Publicar el tiempo
        time_msg = Float32()
        time_msg.data = self.time
        self.time_pub.publish(time_msg)
        
        # Imprimir en la terminal
        self.get_logger().info(f'Time: {self.time:.2f}, Signal: {signal_msg.data:.2f}')
        
        # Incrementar el tiempo
        self.time += 0.1  # Incremento de tiempo para 10 Hz

def main(args=None):
    rclpy.init(args=args)
    signal_generator = SignalGenerator()
    rclpy.spin(signal_generator)
    signal_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()