from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Nodo generador de señales
    signal_generator_node = Node(package='signal_processing_ds',
                                 executable='signal_generator_ds',
                                 name='signal_generator',
                                 output='screen'
                                 )
    
    # Nodo procesador de señales
    process_node = Node(package='signal_processing_ds', 
                        executable='process_ds',
                        name='process_node',
                        output='screen'
                        )
    
    # Lanzar rqt_plot para graficar las señales
    rpt_plot_node = Node(package='rqt_plot',
                         executable='rqt_plot',
                         name='rqt_plot',
                         arguments=['/signal/data', '/proc_signal/data']
                         )
    
    # Lanzar rqt_graph para visualizar la estructura de los nodos
    rqt_graph_node = Node(package='rqt_graph',
                          executable='rqt_graph',
                          name='rqt_graph'
                          )

    l_d = LaunchDescription([signal_generator_node, process_node, rpt_plot_node, rqt_graph_node])

    return l_d
