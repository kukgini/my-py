# https://okky.kr/article/410619

from rx import Observable, Observer

def push_hello_world(observer):
    observer.on_next("hello")
    observer.on_next("world")
    observer.on_completed()
    
class ObservablePrinter(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))
    def on_completed(self):
        print("Done.")
    def on_error(self, error):
        print("Error Occurred: {0}".format(error))
        
class ObservableLister(Observer):
    def __init__(self):
        self.my_list = []
    def on_next(self, value):
        self.my_list.append(value)
    def on_completed(self):
        print(self.my_list)
        print("Done.")
    def on_error(self, error):
        print("Error Occurred: {0}".format(error))
        
if __name__ == '__main__':
    source = Observable.create(push_hello_world)
    source.subscribe(ObservablePrinter())
    source.subscribe(ObservableLister())