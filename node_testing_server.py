from concurrent import futures
import logging
import datetime
from dotenv import dotenv_values

import grpc
import node_conn_pb2 as ReqResModule
import node_conn_pb2_grpc as ClientServerModule
# from led_routines import rutina_secuencia1, rutina_secuencia2, rutina_secuencia3 

# print(rutina_secuencia1)

venv_dict = dict(dotenv_values(".env"))

# put here aux functions
print(f'Iniciando servidor en puerto {venv_dict["PORT"]}')

class LedManipulationServiceServicer(ClientServerModule.LedManipulationServiceServicer):
    """Provides methods that implement functionality of testing server."""
    def StartLedPerformance(self, request, context):    
        messageReceived = request.message

        print(f'The received message is {messageReceived}')
        
        return ReqResModule.TextMessage(
            message = f"{messageReceived} accepted. Happy capstone huehue"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ClientServerModule.add_LedManipulationServiceServicer_to_server(
        LedManipulationServiceServicer(), server)
    server.add_insecure_port(f'[::]:{venv_dict["PORT"]}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
