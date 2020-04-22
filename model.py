from random import randint
from numpy import mean
from time import sleep

class WorkerUnit():
    def __init__(self, max_throughput=None, next_worker=None):
        
        self.inventory = 0
        self.max_throughput = max_throughput if max_throughput else randint(1,6) 
        self.throughput = 0
        self.leader = False if next_worker else True
        self.id = next_worker.id + 1 if next_worker else 1
        self.next_worker = next_worker

    def process(self, demand):

        # simulate statistical variance

        self.throughput = mean([randint(1, self.max_throughput) for _ in range(100)])

        if self.throughput > demand:
            self.throughput = demand

        # determine processed_work capacity
        self.inventory += (demand - self.throughput)

        # do the work
        sleep(self.throughput)
        print(f'Work Center {self.id} processed {self.throughput:0.02} units at {self.throughput:0.02}/{self.max_throughput} rate | Inventory: {self.inventory:0.02}')

        # pass work to next work center
        return self.inventory if self.leader else self.next_worker.process(self.inventory)
        
        
wc1 = WorkerUnit()
wc2 = WorkerUnit(next_worker=wc1)
wc3 = WorkerUnit(next_worker=wc2)
wc4 = WorkerUnit(next_worker=wc3)
wc5 = WorkerUnit(next_worker=wc4)
wc6 = WorkerUnit(next_worker=wc5)


initial_demand = 6
system_throughput = 6
final_throughput = 0
cycle = 1

while final_throughput < initial_demand:
    print(f'-----------------Starting Cycle {cycle}------------------')

    final_throughput += wc6.process(system_throughput)
    system_throughput = final_throughput
