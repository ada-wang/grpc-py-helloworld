import grpc
import simple_test_pb2
import simple_test_pb2_grpc
import time

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = simple_test_pb2_grpc.SimpleTestStub(channel)

    the_input = raw_input("unary_unary print sth:")
    # print the_input
    response = stub.GetOne(simple_test_pb2.RequestOne(hello=the_input))
    print "response from server:"
    print type(response)
    print response.result

    the_input = raw_input("unary_stream print sth:")
    # print the_input
    response = stub.GetList(simple_test_pb2.RequestOne(hello=the_input))
    print "response from server:"
    print type(response)
    print response
    for target_list in response:
        print type(target_list)
        print target_list
        print target_list.resultlist
        pass
    
    the_iter = request_iterator()
    print(type(the_iter))
    response = stub.PostList(the_iter)
    print "response from server:"
    print type(response)
    print response.result

def request_iterator():
    for x in xrange(4):
        print "x:", x
        yield simple_test_pb2.RequestList(namelist=str(x))
        pass
    pass

if __name__ == '__main__':
    main()