from ..DTO.RobotDTO import RobotDTO

from ..controller.RobotController import RobotController
from ..External.yaskawaHC10Connection import yaskawaHC10Connection
from ..adapter.YaskawaRobotAdapter import YaskawaRobotAdapter

from ..DTO.RequestDTO import RequestDTO

from ..controller.RequestController import RequestController
from ..adapter.RequestDashboardAdapter import RequestDashboardAdapter
import json

def test():
    newRobot = RobotDTO("Yaskawa", "Robo de montagem do lab 10", 6)

    robotConnector = yaskawaHC10Connection("0.0.0.0", 1234)
    robotAdapter = YaskawaRobotAdapter()

    robot_information = RobotController.getRobotInfo(newRobot, robotConnector, robotAdapter)

    return robot_information

def testLatency(payload):
    
    jsonPayload = json.loads(payload)
    
    newRequest = RequestDTO(1, jsonPayload["request_timestemp"], jsonPayload["robot_fun_process_time"])
    
    requestAdapter = RequestDashboardAdapter()
    
    DtInfo = RequestController.calculateTime(newRequest, requestAdapter)
    
    return(DtInfo)
