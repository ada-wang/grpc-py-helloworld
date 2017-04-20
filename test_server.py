from concurrent import futures
import grpc
import simple_test_pb2
import simple_test_pb2_grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SimpleTestServicer(simple_test_pb2_grpc.SimpleTestServicer):
    
    def GetOne(self, request, context):
        print "get request from client:"
        print type(request)
        print request
        the_response = "Hello !! " + request.hello
        return simple_test_pb2.ResponseOne(result=the_response)
        pass

    def GetList(self, request, context):
        print "get request from client:"
        print type(request)
        print request
        for x in xrange(5):
            yield simple_test_pb2.ResponseList(resultlist="test" + str(x))
            pass
        pass

    def PostList(self, request, context):
        print "get request from client:"
        print type(request)
        for target_list in request:
            print target_list
            pass
        return simple_test_pb2.ResponseOne(result="PostList OK")
        pass

    def PostAndPost(self, request, context):
        pass
    
    pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_test_pb2_grpc.add_SimpleTestServicer_to_server(
        SimpleTestServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while 1:
            time.sleep(_ONE_DAY_IN_SECONDS)
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()