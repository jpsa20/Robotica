#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math  # Importar la biblioteca math

class ProcessNode(Node):
    def __init__(self):
        super().__init__('process')
        
        # Suscriptores para /signal y /time
        self.signal_sub = self.create_subscription(Float32, '/signal', self.signal_callback, 10)
        self.time_sub = self.create_subscription(Float32, '/time', self.time_callback, 10)
        
        # Publicador para /proc_signal
        self.proc_signal_pub = self.create_publisher(Float32, '/proc_signal', 10)
        
        # Variable para almacenar el tiempo
        self.current_time = 0.0
        
        # Parámetro de fase (hardcoded)
        self.phase_shift = 0.5  

    def signal_callback(self, msg):
        # Procesar la señal
        processed_signal = Float32()
        
        # Aumentar la amplitud de la señal (por ejemplo, multiplicar por 2)
        processed_signal.data = msg.data * 2.0  # Aumentar la amplitud
        
        # Agregar un desfase (fase shift)
        processed_signal.data = math.sin((msg.data * 2.0) + self.phase_shift)
        
        # Publicar la señal procesada
        self.proc_signal_pub.publish(processed_signal)
        
        # Imprimir en la terminal
        self.get_logger().info(f'Processed Signal: {processed_signal.data:.2f}')

    def time_callback(self, msg):
        # Almacenar el tiempo recibido
        self.current_time = msg.data

def main(args=None):
    rclpy.init(args=args)
    process_node = ProcessNode()
    rclpy.spin(process_node)
    process_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
