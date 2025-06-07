
from abc import ABC, abstractmethod

class Server:
    def __init__(self, server_id : str):
        self.server_id = server_id
        self.active_connections = 0
    
    def handle_request(self):
         self.active_connections += 1
         
    def __repr__(self):
        return f"Server({self.server_id}, Active: {self.active_connections})"

class RoutingStrategy(ABC):
    @abstractmethod
    def select_strategy(self, servers):
        pass

class RoundRobin(RoutingStrategy):
    def __init__ (self):
        self.index = 0
        
    def select_strategy(self, servers):
        if not servers:
            raise Exception("No servers available")

        server_list = list(servers.values())
        server = server_list[self.index % len(server_list)]
        self.index += 1
        return server
    
class LeastConnectionsStrategy(RoutingStrategy):
    def select_strategy(self, servers):
        if not servers:
            raise Exception("No servers available")
        return min(servers.values(), key=lambda s: s.active_connections)


class LoadBalancer:
    def __init__(self, strategy : RoutingStrategy):
        self.servers = {}
        self.strategy  = strategy 
        
    def add_server(self, server : Server):
        self.servers[server.server_id] = server
        
    def remove_server(self, server_id : str):
        del self.servers[server_id]
    
    def route_request(self):
        if not self.servers:
            print("No Active servers")
            return 
        
        server = self.strategy.select_strategy(self.servers)
        server.handle_request()
    
    def show_servers(self):
        for  server in self.servers.values():
            print(server)
            
        
        
        
        
        
         

        